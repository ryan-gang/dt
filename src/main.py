from timesheet import CSVTimesheetReader
from utils import get_current_timesheet_path


def main():
    timesheet_path = get_current_timesheet_path()
    print(f"Current timesheet path: {timesheet_path}")

    reader = CSVTimesheetReader(timesheet_path)
    data = reader.read()
    print(f"Data read from timesheet: {data}")


if __name__ == "__main__":
    main()
