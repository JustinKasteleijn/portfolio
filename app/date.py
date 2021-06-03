from datetime import date


def calculate_year_from_current_date(year, month, day):
    today = date.today()
    return today.year - year - ((today.month, today.day) < (month, day))
