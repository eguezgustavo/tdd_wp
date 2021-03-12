def test__calculate_weekday_worked_hours__returns_total_hours__given_a_person_entry():
    person_entry = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'

    weekday_worked_hours = calculate_weekday_worked_hours(person_entry)

    assert weekday_worked_hours == 6
