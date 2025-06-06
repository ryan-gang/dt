import csv
from typing import List

ROWS = ["Project", "Description", "Tags", "Date", "StartTime", "EndTime", "Duration"]


class TimesheetReader:
    def __init__(self, path: str):
        """
        Initialize CSV timesheet reader with file path.
        """
        self.path = path
        # Don't create unnecessary state which is bound to go out of sync
        self._data = self._read()

    def _read(self) -> List[list[str]]:
        """
        Read CSV file and return list of rows.
        """
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            return [row for row in reader]

    def _write(self):
        """
        Write all `data` rows to CSV file, along with `header`.
        """
        with open(self.path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerows(self._data)
        print(f"Written {len(self._data)} rows to {self.path}")

    def append_row(self, row: list[str]):
        """
        Append a row to the CSV file.
        """
        print(f"Appending row: {row}")
        self._data.append(row)
        print(f"Data: {self._data}")
        self._write()

    def edit_last_row(self, row: list[str]):
        """
        Append a row to the CSV file.
        """
        self._data.pop()
        self._data.append(row)
        self._write()

    def get_last_row(self) -> list[str]:
        """
        Get the last row of the CSV file.
        """
        if not self._data:
            raise ValueError("No rows found in the CSV file.")
        return self._data[-1]
