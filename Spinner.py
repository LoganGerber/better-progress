from typing import Tuple

from _IPrefixSuffix import IPrefixSuffix


class Spinner(IPrefixSuffix):
    def __init__(self):
        self._stages: Tuple[str] = ('-', '\\', ' | ', ' / ')
        self._current_stage: int = 0

    def __str__(self):
        prefix = self.formatted_prefix
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix
        if suffix != '':
            suffix = ' ' + suffix

        return prefix + self._stages[self._current_stage] + suffix

    def next(self):
        self._current_stage = (self._current_stage + 1) % len(self._stages)
