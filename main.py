def calculate_weekday_worked_hours(person_entry):
    weekday = [
        'MO', 'TU', 'WE', 'TH', 'FR'
    ]
    
    persona_name = person_entry.split("=")[0]
    all_days = person_entry.split("=")[1]
    daily_details = all_days.split(",")

    for day, hours in zip(weekday, daily_details):
        if day in hours:
            
    return 6