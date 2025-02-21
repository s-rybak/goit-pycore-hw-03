from datetime import datetime, timedelta

# returns a list of users with upcoming birthdays
def get_upcoming_birthdays(users):
    today = datetime.now()
    upcoming_birthdays = []
    for user in users:
        user_birthday = get_user_birthday(user)
        if is_birthday_upcoming(user_birthday):
            upcoming_birthdays.append(get_user_notification_object(user, user_birthday))
    return upcoming_birthdays

def is_birthday_upcoming(user_birthday):
    today = datetime.now()
    b_delta = (user_birthday - today).days
    return b_delta < 7 and b_delta >= 0

def get_user_birthday(user):
    today = datetime.now()
    b_day = datetime.strptime(user['birthday'], '%Y.%m.%d').replace(year=today.year)
    if b_day < today:
        return b_day.replace(year=today.year + 1)
    return b_day

def get_user_notification_object(user, user_birthday):
    return {
        'name': user['name'],
        'congratulation_date':  get_notification_date(user_birthday).strftime('%Y.%m.%d')
    }

def get_notification_date(user_birthday):
     notification_date = user_birthday
     if notification_date.weekday() == 5 :
          notification_date = notification_date + timedelta(days=2)
     elif notification_date.weekday() == 6:
        notification_date = notification_date + timedelta(days=1)
     return notification_date

users = [
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Jane Smith", "birthday": "1990.02.22"},
    {"name": "Jane Smith 2", "birthday": "1990.02.21"},
    {"name": "Jane Smith 2", "birthday": "1990.02.28"},
    {"name": "Jane Smith 2", "birthday": "1990.03.01"},
    {"name": "Jane Smith 2", "birthday": "1990.03.22"},
    {"name": "Jane Smith 2", "birthday": "1990.02.19"},
]

print(get_upcoming_birthdays(users))