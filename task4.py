from datetime import datetime, timedelta

# returns a list of users with upcoming birthdays
def get_upcoming_birthdays(users):
    today = datetime.now()
    upcoming_birthdays = []
    for user in users:
        user_birthday = datetime.strptime(user['birthday'], '%Y.%m.%d')
        if user_birthday.month == today.month and user_birthday.day >= today.day and user_birthday.day <= today.day + 7:
            notification_date = user_birthday.replace(year=today.year)
            if notification_date.weekday() == 5 :
                notification_date = notification_date + timedelta(days=2)
            elif notification_date.weekday() == 6:
                notification_date = notification_date + timedelta(days=1)

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': notification_date.strftime('%Y.%m.%d')
            })
            
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Jane Smith", "birthday": "1990.02.22"},
    {"name": "Jane Smith 2", "birthday": "1990.02.21"},
    {"name": "Jane Smith 2", "birthday": "1990.02.28"},
    {"name": "Jane Smith 2", "birthday": "1990.03.01"},
    {"name": "Jane Smith 2", "birthday": "1990.03.22"},
]

print(get_upcoming_birthdays(users))