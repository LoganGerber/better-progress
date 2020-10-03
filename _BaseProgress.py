from __future__ import annotations

import abc
import string

from typing import TypeVar

from _IPrefixSuffix import IPrefixSuffix


S = TypeVar('S', bound='BaseProgress')


class BaseProgress(IPrefixSuffix):
    def __init__(self: S, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__()

        self._max_value = max_value
        self._current_value = current_value
        self._increment_by = increment_by
        self._cap_value = cap_value

    @abc.abstractmethod
    def __str__(self):
        return '{} / {}'.format(self._current_value, self._max_value)

    def get_max_value(self) -> float:
        return self._max_value

    def set_max_value(self: S, val: float) -> S:
        self._max_value = val
        # Cap the current value if necessary
        self.set_current_value(self.get_current_value())
        return self

    def get_current_value(self) -> float:
        return self._current_value

    def set_current_value(self: S, val: float) -> S:
        if self._cap_value:
            self._current_value = min(self._max_value, val)
        else:
            self._current_value = val
        return self

    def get_increment_by(self) -> float:
        return self._increment_by

    def set_increment_by(self: S, val: float) -> S:
        self._increment_by = val
        return self

    def get_cap_value(self) -> bool:
        return self._cap_value

    def set_cap_value(self: S, cap: bool) -> S:
        self._cap_value = cap
        # Cap the current value if necessary
        self.set_current_value(self.get_current_value())
        return self

    def percent(self) -> float:
        return self._current_value / self._max_value

    def remaining(self) -> float:
        return self._max_value - self._current_value

    def complete(self) -> bool:
        return self._current_value >= self._max_value

    def next(self):
        self._current_value += self._increment_by
        if self._cap_value and self._current_value > self._max_value:
            self._current_value = self._max_value

    def _custom_format(self, text: str, relevant_kwargs: dict = {}) -> str:
        kwargs = {
            **relevant_kwargs,
            'percent': self.percent() * 100,
            'current_value': self.get_current_value(),
            'max_value': self.get_max_value(),
            'remaining': self.remaining()
        }
        return super()._custom_format(text, kwargs)
