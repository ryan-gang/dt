from datetime import datetime

BASE_PATH = "/Users/ryang/Developer/timesheets"


def get_current_year_month():
    now = datetime.now()
    return now.year, now.strftime("%B")


def get_current_timesheet_path():
    year, month = get_current_year_month()
    month = month.lower()
    return f"{BASE_PATH}/{year}/{month}.csv"
