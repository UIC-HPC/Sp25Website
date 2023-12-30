import pandas as pd
import sys
import os
import datetime
import pytz
import re

def assign_quiz(entry):
    """Generate a markdown file for a quiz or an assignment entry based on 'Snippets/Quizzes' value."""
    if entry.get('Snippets/Quizzes'):
        formatted_date = parse_date(entry['Day'])
        if not formatted_date:
            print(f"Error parsing date for entry: {entry}")
            return  # Exit the function if the date couldn't be parsed

        snippets_quizzes = entry['Snippets/Quizzes']
        if "Quiz" in snippets_quizzes:
            # It's a quiz
            filename = f"{snippets_quizzes.lower().replace(' ', '_')}.md"
            file_path = f"../_events/{filename}"
            content = f"""---
type: quiz
date: {formatted_date}
description: {snippets_quizzes}
hide_from_announcments: true
---
Any material or readings covered prior to this quiz.
"""
        else:
            # It's an assignment
            due_date = calculate_next_tuesday(formatted_date)
            filename = f"{snippets_quizzes.replace(' ', '_')}.md"
            file_path = f"../_assignments/{filename}"
            content = f"""---
type: assignment
date: {formatted_date}
title: {snippets_quizzes}
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
due_event: 
    type: due
    date: {due_date}
    description: {snippets_quizzes} Due
---
<!-- This is a sample assignment. -->
"""

        # Check if the directory exists, create it if it doesn't
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Write the content to the markdown file
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Generated markdown file {file_path} for {'quiz' if 'Quiz' in snippets_quizzes else 'assignment'} {snippets_quizzes}.")

def calculate_next_tuesday(formatted_date):
    """Calculate the following Tuesday from the given date before class at 2:00 PM Chicago time."""
    # Parse the formatted date string into a datetime object
    date_object = datetime.datetime.strptime(formatted_date, '%Y-%m-%dT14:00:00%z')
    # Calculate the number of days to add to get to the next Tuesday (weekday 1)
    days_to_add = (1 - date_object.weekday() + 7) % 7 or 7  # Ensure it's the next Tuesday, not the current day if it's Tuesday
    next_tuesday = date_object + datetime.timedelta(days=days_to_add)
    # Set the time to 2:00 PM
    next_tuesday = next_tuesday.replace(hour=14, minute=0, second=0)
    # Return the formatted due date string
    return next_tuesday.strftime('%Y-%m-%dT14:00:00%z')

def projects(entry):
    """Generate a markdown file for a project entry if 'Projects' has a value."""
    if entry.get('Projects'):
        formatted_date = parse_date(entry['Day'])
        if not formatted_date:
            print(f"Error parsing date for entry: {entry}")
            return  # Exit the function if the date couldn't be parsed

        # Calculate the due date, 3 weeks in the future at 11:59 PM
        due_date = calculate_due_date(formatted_date)

        # Normalize the project title for the markdown file name
        project_title = re.sub(r'[^\w\s]', '', entry['Projects']).replace(' ', '_')
        project_filename = f"../_projects/{project_title}.md"

        # Create the content for the markdown file
        project_content = f"""---
type: project
date: {formatted_date}
title: {entry['Projects']}
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
due_event: 
    type: due
    date: {due_date}
    description: {entry['Projects']} Due
---
"""

        # Write the content to the markdown file
        with open(project_filename, 'w') as file:
            file.write(project_content)
        print(f"Generated markdown file {project_filename} for project {entry['Projects']}.")

def calculate_due_date(formatted_date):
    """Calculate the due date 3 weeks in the future at 11:59 PM."""
    # Parse the formatted date string back into a datetime object
    date_object = datetime.datetime.strptime(formatted_date, '%Y-%m-%dT14:00:00%z')
    
    # Calculate the due date (3 weeks later at 11:59 PM)
    due_date_object = date_object + datetime.timedelta(weeks=3)
    due_date_object = due_date_object.replace(hour=23, minute=59, second=0)
    
    # Return the formatted due date string
    return due_date_object.strftime('%Y-%m-%dT23:59:00%z')


def exam(entry):
    """Generate a markdown file for an exam entry if 'Content' contains 'Exam'."""
    # Check if 'Content' contains the word 'Exam'
    if 'Exam' in entry.get('Content', '') and entry.get('Day'):
        formatted_date = parse_date(entry['Day'])
        if not formatted_date:
            print(f"Error parsing date for entry: {entry}")
            return  # Exit the function if the date couldn't be parsed

        # Normalize the content title for the markdown file name
        content_title = re.sub(r'[^\w\s]', '', entry['Content']).replace(' ', '_')
        exam_filename = f"../_events/{content_title}.md"

        # Create the content for the markdown file
        exam_content = f"""---
type: exam
date: {formatted_date}
description: {entry['Content']}
hide_from_announcements: false
---
All material presented in class or assigned as reading prior to the date of the exam is valid material and includes at minimum the following:
"""

        # Write the content to the markdown file
        with open(exam_filename, 'w') as file:
            file.write(exam_content)
        print(f"Generated markdown file {exam_filename} for exam {entry['Content']}.")

def format_readings(readings):
    """Format the 'Readings' string into a markdown list."""
    if not readings:
        return ""  # Return an empty string if there are no readings

    # Split the readings on slashes and strip any surrounding whitespace
    chapters = [chapter.strip() for chapter in readings.split('/')]

    # Format each chapter as a markdown list item
    formatted_chapters = []
    for chapter in chapters:
        if chapter:
            # Check if 'Chapter' is already present in the string
            if chapter.startswith("Chapter"):
                formatted_chapters.append(f"- [{chapter}]()")
            else:
                formatted_chapters.append(f"- [Chapter {chapter}]()")

    return "\n".join(formatted_chapters)

def lecture(entry):
    """Generate a markdown file for a lecture entry if 'L' is numeric."""
    # Check if 'L' is a numeric value and parse the date
    if str(entry['L']).isdigit() and entry['Day']:
        formatted_date = parse_date(entry['Day'])
        if not formatted_date:
            print(f"Error parsing date for entry: {entry}")
            return  # Exit the function if the date couldn't be parsed

        # Define the markdown file name
        lecture_filename = f"{int(entry['L']):02d}-lecture.md"

        # Get the formatted readings
        formatted_readings = format_readings(entry['Readings'])

        # Create the content for the markdown file
        lecture_content = f"""---
type: lecture
date: {formatted_date}
title: {entry['Content']}
#tldr: "Short text to describe what this lecture is about."
thumbnail: /_images/classlogo.png
#links: 
#    - url: https://google.com
#      name: slides
#   - url: /static_files/presentations/code.zip
#      name: codes
---
"""
        # Only add the Material Covered section if there are formatted readings
        if formatted_readings:
            lecture_content += "**Material Covered:**\n" + formatted_readings

        # Write the content to the markdown file
        with open(lecture_filename, 'w') as file:
            file.write(lecture_content)
        print(f"Generated markdown file {lecture_filename} for lecture {entry['L']}.")


def clean_value(value):
    """Clean the string value by stripping whitespace and replacing only whitespace strings with an empty string."""
    if isinstance(value, str):
        # Strip whitespace from the ends of the string
        value = value.strip()
        # Replace strings that are entirely whitespace with an empty string
        if value == '':
            return ''
    return value

def dataframe_to_dict_of_lists(df):
    """Convert DataFrame to a list of dictionaries with cleaned values."""
    list_of_dicts = []
    for _, row in df.iterrows():
        row_dict = {column: clean_value(row[column]) for column in df.columns}
        list_of_dicts.append(row_dict)
    return list_of_dicts

def validate_input():
    """Validate command-line arguments and check file existence."""
    if len(sys.argv) != 2:
        print("Usage: python script.py <ExcelFileName.xlsx>")
        sys.exit(1)

    excel_file_name = sys.argv[1]
    if not os.path.exists(excel_file_name):
        print(f"Error: File '{excel_file_name}' not found.")
        sys.exit(1)
    
    return excel_file_name

def read_excel(file_name):
    """Read the Excel file and return a DataFrame."""
    return pd.read_excel(file_name)

def create_latex_content(df):
    """Generate LaTeX content from the DataFrame."""
    latex_content = [
        r"{\huge Schedule}",
        r"\begin{center}",
        r"\begin{table}[h]",
        r"\centering",
        r"\resizebox{\textwidth}{!}{%",
        r"\rowcolors{2}{gray!10}{gray!20}",
        r"\begin{tabular}{|l|c|l|c|l|l|}",
        r"\hline",
        r"\rowcolor{gray}\textbf{Day} & \textbf{L} & \textbf{Content} & \textbf{Snippets/Quizzes} & \textbf{Readings} & \textbf{Projects}  \\ \hline"
    ]

    for index, row in df.iterrows():
        date_str = parse_date(row['Day'])
        if not date_str:
            continue
        latex_content.append(generate_latex_row(row, date_str))
    
    latex_content.append(r'''\end{tabular}%''')
    latex_content.append(r'''}\end{table}''')
    latex_content.append(r'''\end{center}''')

    return '\n'.join(latex_content)

def parse_date(date_str):
    """Parse the date and return a formatted string with the Chicago timezone considering daylight saving time."""
    try:
        # Define the Chicago timezone
        chicago_tz = pytz.timezone('America/Chicago')
        
        # Parse the date string into a datetime object
        date_str_with_year = f"{date_str.split(' ')[1] if ' ' in date_str else date_str}/2024"
        naive_date_object = datetime.datetime.strptime(date_str_with_year, '%m/%d/%Y')
        
        # Make the date object timezone-aware
        chicago_date_object = chicago_tz.localize(naive_date_object, is_dst=None)
        
        # Convert to the desired format including the timezone offset
        return chicago_date_object.strftime('%Y-%m-%dT14:00:00%z')
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None

def generate_latex_row(row, formatted_date):
    """Generate a single LaTeX table row."""
    return f" {row['Day']} & {row['L']:0>2} & {row['Content']} & {row['Snippets/Quizzes']} & {row['Readings']} & {row['Projects']} \\\\ \\hline"

def write_to_file(file_name, content):
    """Write content to a file."""
    with open(file_name, 'w') as file:
        file.write(content)

def main():
    """Main function to execute the script."""
    excel_file_name = validate_input()
    df = read_excel(excel_file_name)
    
    # Convert DataFrame to a list of dictionaries with cleaned values
    list_of_dicts = dataframe_to_dict_of_lists(df)
    for entry in list_of_dicts:
        lecture(entry)
        exam(entry)
        projects(entry)
        assign_quiz(entry)

    # Other processing...
    latex_content = create_latex_content(df)
    latex_file_name = os.path.splitext(excel_file_name)[0] + '-schedule.tex'
    write_to_file(latex_file_name, latex_content)
    print(f"Generated LaTeX file {latex_file_name} based on {excel_file_name}.")

if __name__ == "__main__":
    main()