import datetime


def age_generator():
    birth_day = int(
        input("What is your date of birth? Please type in the day: "))
    birth_month = int(input("month: "))
    birth_year = int(input("year: "))
    date_today = datetime.date.today()
    age = date_today.year - birth_year - ((date_today.month, date_today.day)
                                          < (birth_month, birth_day))
    print(f"You are {age} year(s) old")


age_generator()
