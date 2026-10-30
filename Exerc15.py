# Improve the age function: calculate the age in years, months and days

from datetime import date


def age_in_years_months_days(birth_date):
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    if days < 0:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = days + days_in_month[today.month - 2]  # length of the previous month
        months = months - 1
    if months < 0:
        months = months + 12
        years = years - 1
    return years, months, days



print(age_in_years_months_days(date(2003, 4, 19)))