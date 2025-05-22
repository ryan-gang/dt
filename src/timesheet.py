import csv
from typing import Any, Dict, List


class CSVTimesheetReader:
    def __init__(self, path: str):
        """
        Initialize CSV timesheet reader with file path.
        """
        self.path = path

    def read(self) -> List[Dict[str, Any]]:
        """
        Read CSV file and return list of dictionaries.
        """
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file, delimiter=",")
            headers = next(reader)
            return [dict(zip(headers, row)) for row in reader]

    def write(self, data: List[Dict[str, Any]]) -> None:
        """
        Write list of dictionaries to CSV file.
        """
        if not data:
            return

        fieldnames = data[0].keys()
        with open(self.path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
