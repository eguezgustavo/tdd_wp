from main import calculate_weekday_worked_hours

def test__calculate_weekday_worked_hours__returns_total_hours__given_a_person_entry():
    person_entry = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'

    weekday_worked_hours = calculate_weekday_worked_hours(person_entry)

    assert weekday_worked_hours == 6


# def test__calculate_weekday_worked_hours__returns_total_hours__given_another_person_entry():
#     person_entry = 'JC=MO10:00-13:00,TU09:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
#
#     weekday_worked_hours = calculate_weekday_worked_hours(person_entry)
#
#     assert weekday_worked_hours == 8

def test__get_time_frame_by_day__returns_day_and_time_frame():
    person_entry = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'

    time_frame_by_day = get_time_frame_by_day(person_entry)

    expected = ('MO':