import abc
import math
import string
import typing

import _BaseProgress as base


class _EndStringFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            return super().get_value(key, args, kwargs)
        return kwargs[key] if key in kwargs else ''


class Bar(base.BaseProgress):
    _FORMATTER = _EndStringFormatter()

    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        self._prefix: str = ''
        self._prefix_kwargs: dict = {}
        self._suffix: str = ''
        self._suffix_kwargs: dict = {}
        self._bar_width: int = 32
        self._fill_character: str = '#'
        self._empty_character: str = ' '
        self._bar_prefix: str = '|'
        self._bar_suffix: str = '|'

        super().__init__(max_value, current_value, increment_by)

    def __str__(self):
        filled = math.floor(self._bar_width * self.progress)
        empty = self._bar_width - filled
        prefix = self._format_prefix() if self._prefix != '' else ''
        suffix = self._format_suffix() if self._suffix != '' else ''
        return prefix + self._bar_prefix + (self._fill_character * filled) + (self._empty_character * empty) + self._bar_suffix + suffix

    @property
    def prefix(self) -> str:
        return self._prefix

    @prefix.setter
    def prefix(self, val: str) -> None:
        self._prefix = val if val else ''
        return self

    @property
    def suffix(self) -> str:
        return self._suffix

    @suffix.setter
    def suffix(self, val: str) -> None:
        self._suffix = val if val else ''
        return self

    @property
    def bar_width(self) -> int:
        return self._bar_width

    @bar_width.setter
    def bar_width(self, val: int) -> None:
        self._bar_width = val
        return self

    @property
    def fill(self) -> str:
        return self._fill

    @fill.setter
    def fill(self, val: str) -> None:
        self._fill = val
        return self

    @property
    def empty_fill(self) -> str:
        return self._empty_fill

    @empty_fill.setter
    def empty_fill(self, val: str) -> None:
        self._empty_fill = val
        return self

    @property
    def bar_prefix(self) -> str:
        return self._bar_prefix

    @bar_prefix.setter
    def bar_prefix(self, val: str) -> None:
        self._bar_prefix = val
        return self

    @property
    def bar_suffix(self) -> str:
        return self._bar_suffix

    @bar_suffix.setter
    def bar_suffix(self, val: str) -> None:
        self._bar_suffix = val
        return self

    def _format_prefix(self) -> str:
        return self._format_end(self._prefix, self._prefix_kwargs) + ' '

    def _format_suffix(self) -> str:
        return ' ' + self._format_end(self._suffix, self._suffix_kwargs)

    def _format_end(self, end, relevant_kwargs: dict) -> str:
        return Bar._FORMATTER.format(end,
                                     percent=(str(self.progress * 100) + '%'),
                                     current_value=self.current_value,
                                     max_value=self.max_value,
                                     remaining=self.remaining,
                                     **relevant_kwargs)


class IncrementalBar(Bar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False, prefix: str = '', prefix_kwargs: dict = {}, suffix: str = '', suffix_kwargs: dict = {}, bar_width: int = 32, fill: str = '█', fill_stages: typing.List[str] = [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'], empty_fill: str = ' ', bar_prefix: str = '|', bar_suffix: str = '|'):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages: typing.List[str] = [
            ' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
        self.prefix

    def __str__(self):
        filled = self._bar_width * self.progress
        full_filled = math.floor(filled)
        stage_index = math.floor(math.modf(filled)[0] * len(self._fill_stages))
        empty = self._bar_width - full_filled - 1

        return self._prefix + ' ' + self._bar_prefix + (self._fill * full_filled) + (self._fill_stages[stage_index]) + (self._empty_fill * empty) + self._bar_suffix + ' ' + self._suffix

    @property
    def fill_stages(self) -> typing.List[str]:
        return list(self._fill_stages)

    @fill_stages.setter
    def fill_stages(self, stages: typing.List[str]) -> None:
        self._fill_stages = stages
        return self
