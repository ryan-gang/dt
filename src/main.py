import time
from datetime import datetime
from typing import Optional

from timesheet import TimesheetReader
from utils import get_current_timesheet_path


def start_task(project: str, description: str, tags: Optional[list[str]] = None):
    """
    Start a task with the given project, description, and optional tags.
    """
    if tags is None:
        tags = []
    print(f"Starting task: {project}, {description}, {tags}")
    # ROWS = ["Project", "Description", "Tags", "Start DateTime", "End DateTime", "Duration"]
    timestamp = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%S")
    rows = [project, description, ", ".join(tags), timestamp, "", ""]
    timesheet_path = get_current_timesheet_path()
    reader = TimesheetReader(timesheet_path)
    reader.append_row(rows)


def end_task():
    """
    End a task with the given project, description, and optional tags.
    """
    timesheet_path = get_current_timesheet_path()
    reader = TimesheetReader(timesheet_path)
    row = reader.get_last_row()
    timestamp = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%S")
    row[-2] = timestamp
    row[-1] = str(
        datetime.strptime(row[-2], "%Y-%m-%dT%H:%M:%S")
        - datetime.strptime(row[-3], "%Y-%m-%dT%H:%M:%S")
    )
    reader.edit_last_row(row)


def main():
    timesheet_path = get_current_timesheet_path()
    print(f"Current timesheet path: {timesheet_path}")

    reader = TimesheetReader(timesheet_path)
    data = reader.get_last_row()
    print(data)


if __name__ == "__main__":
    main()
