# syllabus-table-maker.py

## Overview
This Python script generates an Excel file with a schedule based on specified days within a given date range. It's designed to help users create structured schedules for courses, meetings, or any event series occurring on specific days of the week.

## Features
- **Command-Line Interface**: Easily specify the Excel file name, date range, and days of the week directly through the command line.
- **Customizable Schedule**: Generate schedules for any combination of days (e.g., Mondays and Wednesdays).
- **Formatted Output**: Excel files are generated with pre-formatted cells and headers for readability and immediate use.

## Requirements
- Python 3.x
- `xlsxwriter` library (Install via `pip install xlsxwriter`)

## Usage
To use the script, navigate to the directory containing the script and run it with the required parameters:

```bash
python schedule_generator.py <ExcelFileName.xlsx> <StartDate MM/DD/YYYY> <EndDate MM/DD/YYYY> <Day1> <Day2> ...
```

### Parameters:
- `<ExcelFileName.xlsx>`: The desired name of the Excel file to be generated.
- `<StartDate MM/DD/YYYY>`: The start date of the schedule in MM/DD/YYYY format.
- `<EndDate MM/DD/YYYY>`: The end date of the schedule in MM/DD/YYYY format.
- `<Day1> <Day2> ...`: The days of the week for which to generate the schedule (e.g., Monday Tuesday).

## Example:

```bash
python syllabus-table-maker.py <schedule.xlsx> <01/01/2023> <12/31/2023> <Monday Wednesday Friday>
```

## Structure

The script is organized into several functions, each responsible for a part of the generation process:

- parse_command_line_arguments(): Parses and validates command-line arguments.
- get_script_directory(): Determines the directory where the script is running.
- create_day_mappings(): Creates mappings for day names to their corresponding weekday numbers and abbreviations.
- convert_dates_to_datetime(): Converts date strings to datetime objects.
- create_excel_schedule(): Main function to create and populate the Excel file.
- format_cells(): Applies formatting to the Excel cells.
- write_schedule(): Writes the schedule data into the Excel file.
- main(): Orchestrates the script's execution.

## Customization

You can modify the script to fit specific needs, such as changing the Excel formatting, adjusting the date range logic, or adding additional data to the schedule.

# material_builder.py

## Overview
This Python script automates the generation of markdown files for lectures, exams, quizzes, and projects from an Excel spreadsheet. It creates markdown files with specific metadata and content based on the spreadsheet entries.

## Features
- **Lecture Files**: Generates lecture markdown files with date, title, and covered material for each entry with a numeric 'L' value.
- **Exam Files**: Creates markdown files for entries containing 'Exam' in the 'Content', including material covered up to the exam date.
- **Project Files**: Produces project markdown files with a due date set to 3 weeks from the given date, at 11:59 PM.
- **Quiz and Assignment Files**: Depending on 'Snippets/Quizzes' entries, it generates either quiz or assignment markdown files. Quizzes are hidden from announcements, while assignments include a due date on the following Tuesday at 2:00 PM.

## Usage
1. Ensure Python is installed on your system.
2. Install `pandas` and `pytz` libraries if not already present.
3. Place the Excel spreadsheet in the same directory as the script or provide the path to it.
4. Run the script with the Excel file as an argument, e.g., `python material_builder.py <schedule.xlsx>`.

## Functions
- `parse_date(date_str)`: Converts date strings to timezone-aware datetime objects considering Chicago's DST.
- `generate_latex_row(row, formatted_date)`: Creates LaTeX table rows for the schedule.
- `write_to_file(file_name, content)`: Writes content to markdown files.
- `main()`: Main function that reads the Excel file, generates markdown files, and compiles a LaTeX document.

## Input Format
The Excel file should have the following columns:
- Day
- L (Lecture Number)
- Content
- Snippets/Quizzes
- Readings
- Projects

## Output
Markdown files are generated in corresponding directories:
- `_lectures/` for lectures
- `_events/` for exams and quizzes
- `_projects/` for projects
- `_assignments/` for assignments

Files contain YAML frontmatter with metadata and markdown content for the respective academic activity.

## Customization
- Adjust `calculate_due_date()` and `calculate_next_tuesday()` for different due dates.
- Update directory paths or file naming conventions as needed.

## Dependencies
- Python 3.x
- pandas
- pytz for timezone handling
