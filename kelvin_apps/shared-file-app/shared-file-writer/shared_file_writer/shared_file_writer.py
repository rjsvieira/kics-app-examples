"""
Data Application.
"""

import random

from kelvin.app import DataApplication
from typing.io import TextIO


class App(DataApplication):
    """Application."""

    file: TextIO

    def init(self) -> None:
        mode = "w+"
        buffering = 1
        self.file = open(self.config.file_name, mode=mode, buffering=buffering)

    def process(self) -> None:
        """Process data."""

        # Generate a random value
        value = random.randint(0, 5000)
        self.logger.info("Writing to shared file the following value", value=value)
        try:
            self.file.write(f"{value}\n")
        except Exception as exc:
            self.logger.error(f"Error writing to file", exc=exc)