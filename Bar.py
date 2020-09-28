import abc
import math

import _BaseProgress as base


class Bar(base.BaseProgress):
    def __init__(self, max_value: int = 100, current_value: int = 0, increment_by: float = 1, prefix: str = '', suffix: str = '', bar_width: int = 32, fill: str = '#', empty_fill: str = ' ', bar_prefix='|', bar_suffix='|'):
        self._prefix = prefix
        self._suffix = suffix
        self._bar_width = bar_width
        self._fill = fill
        self._empty_fill = empty_fill
        self._bar_prefix = bar_prefix
        self._bar_suffix = bar_suffix

        super().__init__(max_value, current_value, increment_by)

    def __str__(self):
        filled = math.floor(self._bar_width * self.progress)
        empty = self._bar_width - filled
        return self._prefix + ' ' + self._bar_prefix + (self._fill * filled) + (self._empty_fill * empty) + self._bar_suffix + ' ' + self._suffix

    @property
    def prefix(self) -> str:
        return self._prefix

    @prefix.setter
    def prefix(self, val: str) -> None:
        self._prefix = val

    @property
    def suffix(self) -> str:
        return self._suffix

    @suffix.setter
    def suffix(self, val: str) -> None:
        self._suffix = val

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
