import argparse
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
    date = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
    start_time = datetime.fromtimestamp(time.time()).strftime("%H:%M")
    print(f"Starting task: {project}, {description}, {tags} @ {date}:{start_time}")
    new_task = [project, description, ", ".join(tags), date, start_time, "", ""]

    timesheet_path = get_current_timesheet_path()
    print(f"Timesheet path: {timesheet_path}")
    reader = TimesheetReader(timesheet_path)
    reader.append_row(new_task)


def end_task():
    """
    End a task with the given project, description, and optional tags.
    """
    timesheet_path = get_current_timesheet_path()
    reader = TimesheetReader(timesheet_path)
    row = reader.get_last_row()
    end_time = datetime.fromtimestamp(time.time()).strftime("%H:%M")
    row[-2] = end_time
    delta = datetime.strptime(row[-2], "%H:%M") - datetime.strptime(row[-3], "%H:%M")
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    row[-1] = f"{hours}:{minutes:02d}"
    reader.edit_last_row(row)


def main():
    parser = argparse.ArgumentParser(description="Time tracking tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create parser for "start" command
    start_parser = subparsers.add_parser("start", help="Start a new task")
    start_parser.add_argument("project", help="Project name")
    start_parser.add_argument("description", help="Task description")
    start_parser.add_argument("tags", nargs="*", help="Optional tags for the task")

    # Create parser for "stop" command
    subparsers.add_parser("stop", help="Stop the currently running task")

    args = parser.parse_args()

    if args.command == "start":
        start_task(args.project, args.description, args.tags)
    elif args.command == "stop":
        end_task()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
