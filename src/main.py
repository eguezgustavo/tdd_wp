import re

def calculate_weekday_worked_hours(person_entry):
    # weekday = [
    #     'MO', 'TU', 'WE', 'TH', 'FR'
    # ]
    #
    # persona_name = person_entry.split("=")[0]
    # all_days = person_entry.split("=")[1]
    # daily_details = all_days.split(",") #MO10:00-12:00
    #
    # for day, hours in zip(weekday, daily_details):
    #     if day in hours:

    return 6


def work_log(person_entry):
    return person_entry.split("=")[1].split(",")


def parse_hours_by_day(hours_by_day_string):
    hour_regex = '[0-2][0-9]:[0-5][0-9]'
    hours_by_day = re.findall(hour_regex, hours_by_day_string)
    
