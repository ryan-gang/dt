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
