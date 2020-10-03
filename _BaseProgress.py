from __future__ import annotations

import abc
import string

from typing import Union, Optional

from _IPrefixSuffix import IPrefixSuffix


class BaseProgress(IPrefixSuffix):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        self._max_value = max_value
        self._current_value = current_value
        self._increment_by = increment_by
        self._cap_value = cap_value
        self._prefix: str = ''
        self._prefix_kwargs: dict = {}
        self._suffix: str = ''
        self._suffix_kwargs: dict = {}

    @abc.abstractmethod
    def __str__(self):
        return '{} / {}'.format(self._current_value, self._max_value)

    def max_value(self, val: Optional[float] = None) -> Union[BaseProgress, float]:
        if val != None:
            self._max_value = val
            # Cap the current value if necessary
            self.current_value(self.current_value())
            return self
        return self._max_value

    def current_value(self, val: Optional[float] = None) -> Union[BaseProgress, float]:
        if val != None:
            if self._cap_value:
                self._current_value = min(self._max_value, val)
            else:
                self._current_value = val
            return self
        return self._current_value

    def increment_by(self, val: Optional[float] = None) -> Union[BaseProgress, float]:
        if val != None:
            self._increment_by = val
            return self
        return self._increment_by

    def cap_value(self, cap: Optional[bool]) -> Union[BaseProgress, bool]:
        if cap != None:
            if cap == self._cap_value:
                return

            self._cap_value = cap

            # Cap the current value if necessary
            self.current_value(self.current_value())
            return self
        return self._cap_value

    @property
    def progress(self) -> float:
        return self._current_value / self._max_value

    @property
    def remaining(self) -> float:
        return self._max_value - self._current_value

    def next(self):
        self._current_value += self._increment_by
        if self._cap_value and self._current_value > self._max_value:
            self._current_value = self._max_value

    def _custom_format(self, text: str, relevant_kwargs: dict = {}) -> str:
        kwargs = {
            **relevant_kwargs,
            'percent': str(self.progress * 100) + '%',
            'current_value': self.current_value,
            'max_value': self.max_value,
            'remaining': self.remaining
        }
        return super()._custom_format(text, kwargs)
