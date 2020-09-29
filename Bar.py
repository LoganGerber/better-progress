import abc
import math
import string

import _BaseProgress as base


class _EndStringFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            return super().get_value(key, args, kwargs)
        return kwargs[key] if key in kwargs else ''


class Bar(base.BaseProgress):
    _FORMATTER = _EndStringFormatter()

    def __init__(self, max_value: int = 100, current_value: int = 0, increment_by: float = 1, prefix: str = '', suffix: str = '', bar_width: int = 32, fill: str = '#', empty_fill: str = ' ', bar_prefix: str = '|', bar_suffix: str = '|'):
        self._prefix = prefix if prefix else ''
        self._suffix = suffix if suffix else ''
        self._bar_width = bar_width
        self._fill = fill
        self._empty_fill = empty_fill
        self._bar_prefix = bar_prefix
        self._bar_suffix = bar_suffix

        super().__init__(max_value, current_value, increment_by)

    def __str__(self):
        filled = math.floor(self._bar_width * self.progress)
        empty = self._bar_width - filled
        prefix = self._formatEnd(
            self._prefix + ' ') if self._prefix != '' else ''
        suffix = self._formatEnd(
            ' ' + self._suffix) if self._suffix != '' else ''
        return prefix + self._bar_prefix + (self._fill * filled) + (self._empty_fill * empty) + self._bar_suffix + suffix

    @property
    def prefix(self) -> str:
        return self._prefix

    @prefix.setter
    def prefix(self, val: str) -> None:
        self._prefix = val if val else ''

    @property
    def suffix(self) -> str:
        return self._suffix

    @suffix.setter
    def suffix(self, val: str) -> None:
        self._suffix = val if val else ''

    @property
    def bar_width(self) -> int:
        return self._bar_width

    @bar_width.setter
    def bar_width(self, val: int) -> None:
        self._bar_width = val

    @property
    def fill(self) -> str:
        return self._fill

    @fill.setter
    def fill(self, val: str) -> None:
        self._fill = val

    @property
    def empty_fill(self) -> str:
        return self._empty_fill

    @empty_fill.setter
    def empty_fill(self, val: str) -> None:
        self._empty_fill = val

    @property
    def bar_prefix(self) -> str:
        return self._bar_prefix

    @bar_prefix.setter
    def bar_prefix(self, val: str) -> None:
        self._bar_prefix = val

    @property
    def bar_suffix(self) -> str:
        return self._bar_suffix

    @bar_suffix.setter
    def bar_suffix(self, val: str) -> None:
        self._bar_suffix = val

    def _formatEnd(self, end: str) -> str:
        return Bar._FORMATTER.format(end, percent=(str(self.progress * 100) + '%'), current_value=self.current_value, max_value=self.max_value, remaining=self.remaining)
