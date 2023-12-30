import datetime
import xlsxwriter
import sys
import os


def parse_command_line_arguments():
    """
    Parses and validates command-line arguments.
    Exits the script if the arguments are invalid.
    Returns:
        tuple: Contains Excel file name, start date, end date, and list of day names.
    """
    if len(sys.argv) < 5:
        print("Usage: python script.py <ExcelFileName.xlsx> <StartDate MM/DD/YYYY> <EndDate MM/DD/YYYY> <Day1> <Day2> ...")
        sys.exit(1)
    return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]


def get_script_directory():
    """
    Returns the directory where the script is running.
    """
    return os.path.dirname(os.path.abspath(__file__))


def create_day_mappings():
    """
    Creates mappings for day names to their corresponding weekday numbers and abbreviations.
    Returns:
        tuple: Contains two dictionaries, one for full day names and one for abbreviations.
    """
    days_map = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }
    day_abbreviations = {
        0: "M",
        1: "T",
        2: "W",
        3: "Th",
        4: "F",
        5: "Sa",
        6: "Su",
    }
    return days_map, day_abbreviations


def convert_dates_to_datetime(start_date_str, end_date_str):
    """
    Converts date strings to datetime objects.
    Args:
        start_date_str (str): Start date in MM/DD/YYYY format.
        end_date_str (str): End date in MM/DD/YYYY format.
    Returns:
        tuple: Contains datetime objects for the start and end dates.
    """
    start_date = datetime.datetime.strptime(start_date_str, '%m/%d/%Y')
    end_date = datetime.datetime.strptime(end_date_str, '%m/%d/%Y')
    return start_date, end_date


def create_excel_schedule(excel_path, days, day_abbreviations, start_date, end_date):
    """
    Creates an Excel file and populates it with a schedule based on the provided parameters.
    Args:
        excel_path (str): Path to save the Excel file.
        days (list): List of integers representing days to include in the schedule.
        day_abbreviations (dict): Mapping of day numbers to their abbreviations.
        start_date (datetime): Start date for the schedule.
        end_date (datetime): End date for the schedule.
    """
    workbook = xlsxwriter.Workbook(excel_path)
    worksheet = workbook.add_worksheet()
    num_format = format_cells(worksheet, workbook)

    write_schedule(worksheet, days, day_abbreviations, start_date, end_date, num_format)
    workbook.close()


def format_cells(worksheet, workbook):
    """
    Formats the Excel worksheet cells and writes headers.
    Args:
        worksheet: The worksheet object to format.
        workbook: The workbook object to add formats.
    Returns:
        xlsxwriter.format: The number format for cells.
    """
    num_format = workbook.add_format({'num_format': '00'})
    headers = ['Day', 'L', 'Content', 'Snippets/Quizzes', 'Readings', 'Projects']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)
    return num_format


def write_schedule(worksheet, days, day_abbreviations, start_date, end_date, num_format):
    """
    Writes the schedule to the provided worksheet based on specified days and date range.
    Args:
        worksheet: The worksheet object to write the schedule to.
        days (list): List of integers representing days to include in the schedule.
        day_abbreviations (dict): Mapping of day numbers to their abbreviations.
        start_date (datetime): Start date for the schedule.
        end_date (datetime): End date for the schedule.
        num_format (xlsxwriter.format): The number format for cells.
    """
    date_range = (end_date - start_date).days + 1
    row = 1
    counter = 0
    for single_date in (start_date + datetime.timedelta(n) for n in range(date_range)):
        if single_date.weekday() in days:
            day_abbr = day_abbreviations[single_date.weekday()]
            formatted_date = f"{day_abbr} {single_date.strftime('%m/%d')}"
            worksheet.write(row, 0, formatted_date)
            worksheet.write_number(row, 1, counter, num_format)
            row += 1
            counter += 1


def main():
    """
    Main function that orchestrates the script execution.
    """
    excel_file_name, start_date_str, end_date_str, day_names = parse_command_line_arguments()
    script_dir = get_script_directory()
    excel_path = os.path.join(script_dir, excel_file_name)
    days_map, day_abbreviations = create_day_mappings()
    days = [days_map[day] for day in day_names if day in days_map]
    start_date, end_date = convert_dates_to_datetime(start_date_str, end_date_str)

    create_excel_schedule(excel_path, days, day_abbreviations, start_date, end_date)
    print(f"Generated Excel file {excel_file_name} for specified dates and days in the script's directory.")


if __name__ == "__main__":
    main()
