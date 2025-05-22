import argparse
import time
from datetime import datetime
from typing import Optional

from timesheet import TimesheetReader
from utils import get_current_timesheet_path


def start_task(
    project: Optional[str], description: Optional[str], tags: Optional[list[str]]
):
    """
    Start a task with the given project, description, and optional tags.
    """
    timesheet_path = get_current_timesheet_path()
    print(f"Timesheet path: {timesheet_path}")
    reader = TimesheetReader(timesheet_path)

    if project is None and description is None and (tags is None or tags == []):
        print("No arguments provided, using last task's values")
        project, description, tags_string = reader.get_last_row()[:3]
        print(project, description, tags_string)
        tags = tags_string.split(", ")

    date = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
    start_time = datetime.fromtimestamp(time.time()).strftime("%H:%M")
    print(f"Starting task: {project}, {description}, {tags} @ {date}:{start_time}")
    new_task = [project, description, ", ".join(tags), date, start_time, "", ""]

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
    start_parser.add_argument(
        "project",
        nargs="?",
        default=None,
        help="Project name (if not specified, last task's project will be used)",
    )
    start_parser.add_argument(
        "description",
        nargs="?",
        default=None,
        help="Task description (if not specified, last task's description will be used)",
    )
    start_parser.add_argument(
        "tags",
        nargs="*",
        default=None,
        help="Tags for the task (if not specified, last task's tags will be used)",
    )

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
