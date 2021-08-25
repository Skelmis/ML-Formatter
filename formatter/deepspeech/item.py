from pathlib import Path

import attr


@attr.s
class Item:
    """Represents a set of files"""

    media_file: str = attr.ib()  # Path to media file
    transcript_file: str = attr.ib()  # Path to transcript file

    def get_media_file_size(self):
        """
        Returns
        -------
        bytes
            The size of the file in bytes
        """
        return Path(self.transcript_file).stat().st_size

    def get_transcription(self):
        """
        Returns
        -------
        str
            The transcription of this media file
        """
        return Path(self.transcript_file).read_text()
