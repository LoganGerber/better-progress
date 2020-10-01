import abc
import math
import string

from typing import Union, List

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

    def prefix(self, val: Optional[str] = None, **kwargs) -> Union[Bar, str]:
        if val:
            self._prefix = str(val)
            self._prefix_kwargs = kwargs
            return self
        return self._prefix

    def prefix_kwargs(self, val: Optional[dict] = None) -> Union[Bar, dict]:
        if val:
            self._prefix_kwargs = dict(val)
            return self
        return self._prefix_kwargs

    def suffix(self, val: Optional[str] = None, **kwargs) -> Union[Bar, str]:
        if val:
            self._suffix = str(val)
            self._suffix_kwargs = kwargs
            return self
        return self._suffix

    def suffix_kwargs(self, val: Optional[dict] = None) -> Union[Bar, dict]:
        if val:
            self._suffix_kwargs = dict(val)
            return self
        return self._suffix_kwargs

    def bar_width(self, val: Optional[int] = None) -> Union[None, Bar]:
        if val:
            self._bar_width = val
            return self
        return self._bar_width

    def fill_character(self, val: Optional[str]) -> Union[None, Bar]:
        if val:
            self._fill_character = val
            return self
        return self._fill_character

    def empty_character(self, val: Union[str, None]) -> Union[None, Bar]:
        if val:
            self._empty_character = val
            return self
        return self._empty_character

    def bar_prefix(self, val: Union[str, None]) -> Union[None, Bar]:
        if val:
            self._bar_prefix = val
            return self
        return self._bar_prefix

    def bar_suffix(self, val: Union[str, None]) -> Union[None, Bar]:
        if val:
            self._bar_suffix = val
            return self
        return self._bar_suffix

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
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages: List[str] = [
            ' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
        self._fill_character = '█'

    def __str__(self):
        filled = self._bar_width * self.progress
        full_filled = math.floor(filled)
        stage_index = math.floor(math.modf(filled)[0] * len(self._fill_stages))
        empty = self._bar_width - full_filled - 1

        return self._prefix + ' ' + self._bar_prefix + (self._fill * full_filled) + (self._fill_stages[stage_index]) + (self._empty_fill * empty) + self._bar_suffix + ' ' + self._suffix

    def fill_stages(self, stages: Union[List[str], None]) -> Union[None, IncrementalBar]:
        if stages:
            self._fill_stages = stages
            return self
        return self._fill_stages
