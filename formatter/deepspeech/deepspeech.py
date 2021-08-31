import logging
import os
from pathlib import Path
import csv

from formatter.base_formatter import BaseFormatter
from formatter.deepspeech.item import Item
from formatter.exceptions import NoMedia, MissingTranscription, NonEmptyDir

log = logging.getLogger(__name__)


class DeepSpeech(BaseFormatter):
    """
    Designed to have a lot of file read/writes to save on
    needing to store everything in memory. This also means
    the process is essentially O(2) in terms of overall passes
    as we store everything initially before splitting up into
    train/test/dev.
    """

    def run(self):
        """The runner for DeepSpeech formatting"""
        self.create_initial_files()
        with open(
            os.path.join(self.output_dir, "initial_runs.csv"),
            newline="",
            mode="a",
            encoding="utf-8",
        ) as f:
            writer = csv.writer(f)

            found_file = False
            with os.scandir(self.media_dir) as it:
                entry: os.DirEntry
                for entry in it:
                    if not entry.is_file():
                        continue

                    filename: str = entry.name
                    if not filename.endswith(self.media_type):
                        continue

                    # Strip filetype to use as a generic pointer
                    filename = filename[: (len(filename) - (len(self.media_type) + 1))]

                    found_file = True
                    # Okay its a valid media file, lets try find its transcription
                    transcript_path: str = os.path.join(
                        self.transcript_dir, f"{filename}.{self.transcript_type}"
                    )
                    transcript = Path(transcript_path)
                    if not transcript.is_file():
                        log.warning(
                            "%s.%s is missing a transcript", filename, self.media_type
                        )

                    item = Item(media_file=entry.path, transcript_file=transcript_path)

                    self.process_item(writer, item)

        if not found_file:
            raise NoMedia()

    def create_initial_files(self) -> None:
        """Creates the initial files and sets up directories"""
        output_dir = Path(self.output_dir)
        if any(output_dir.iterdir()):
            raise NonEmptyDir

        # Setup our csv files
        self._create_csv("initial_runs")  # we delete this afterwards
        self._create_csv("train")
        self._create_csv("test")
        self._create_csv("dev")
        self._create_csv("all")

    def process_item(self, writer, item: Item) -> None:  # noqa
        """Process's an item and outputs it to a generic 'all' file"""
        writer.writerow(
            [
                item.get_absolute_media_path(),
                item.get_media_file_size(),
                item.get_transcription(),
            ]
        )

    def split_into_runs(self) -> None:
        """Splits the 'initial_runs' file into runs using the provided split ratio"""

    def _create_csv(self, csv_name: str) -> None:
        """Creates and injects headers to the given csv file"""
        headers = ["wav_filename", "wav_filesize", "transcript"]
        with open(
            os.path.join(self.output_dir, f"{csv_name}.csv"), newline="", mode="w"
        ) as f:
            writer = csv.writer(f)
            writer.writerow(headers)
