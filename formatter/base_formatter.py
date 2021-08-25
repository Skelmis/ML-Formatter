import logging

log = logging.getLogger(__name__)


class BaseFormatter:
    def __init__(
        self,
        media_dir,
        transcript_dir,
        output_dir,
        media_type,
        transcript_type,
    ):
        self.media_dir = media_dir
        self.transcript_dir = transcript_dir
        self.output_dir = output_dir
        self.media_type = media_type
        self.transcript_type = transcript_type
        log.debug("Initialized %s", self.__class__.__name__)

    def run(self):
        raise NotImplementedError
