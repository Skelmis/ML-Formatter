import logging

from formatter.base_formatter import BaseFormatter

log = logging.getLogger(__name__)


class DeepSpeech(BaseFormatter):
    def run(self):
        """The runner for DeepSpeech formatting"""
