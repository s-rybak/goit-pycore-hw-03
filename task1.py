from datetime import datetime

# returns the number of days between the given date and today  
def get_days_from_today(date):
    try:    
        today = datetime.now()
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        delta = today - date_obj
        return delta.days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."


print(get_days_from_today("2025-02-25"))
