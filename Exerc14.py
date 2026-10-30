# Write a function that takes a person's birth date and calculates their age in years

from datetime import date   # library to work with dates


def age_in_years(birth_date):
    today = date.today()
    years = today.year - birth_date.year
    # birthday not reached yet this year: one year less
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        years = years - 1
    return years


print(age_in_years(date(2000, 5, 17)))