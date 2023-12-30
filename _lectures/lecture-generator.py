import datetime
import sys

# Mapping day names to their corresponding weekday numbers
days_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

# Helper function to generate the content
def generate_content(date, counter):
    content = f"""---
type: lecture
date: {date.strftime('%Y-%m-%dT14:00:00-6:00')}
title: Sample Lecture {counter}
tldr: "Short text to describe what this lecture is about."
thumbnail: /_images/classlogo.png
links: 
    - url: /static_files/presentations/lec.zip
      name: notes
    - url: /static_files/presentations/code.zip
      name: codes
    - url: https://google.com
      name: slides
---
**Suggested Readings:**
- [Readings 1](http://example.com)
- [Readings 2](http://example.com)
"""
    return content

# Convert command line arguments (assuming this script is named lecture-generator.py)
start_date_str = sys.argv[1]
end_date_str = sys.argv[2]
day_names = sys.argv[3:]  # Get all the day names from the command line

# Convert day names to their corresponding weekday numbers
days = [days_map[day] for day in day_names if day in days_map]

# Convert string dates to datetime objects
start_date = datetime.datetime.strptime(start_date_str, '%m/%d/%Y')
end_date = datetime.datetime.strptime(end_date_str, '%m/%d/%Y')

# Calculate the range of dates
date_range = (end_date - start_date).days + 1  # +1 to include the end_date

counter = 0
for single_date in (start_date + datetime.timedelta(n) for n in range(date_range)):
    if single_date.weekday() in days:
        filename = f"{counter:02}_lecture.md"
        content = generate_content(single_date, counter)
        
        # Write the content to the file
        with open(filename, 'w') as file:
            file.write(content)
        
        counter += 1  # Increment the file counter

print(f"Generated {counter} files for the specified dates and days.")
