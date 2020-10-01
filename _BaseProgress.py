import abc
import string

from typing import Union, Optional


class _EndStringFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            return super().get_value(key, args, kwargs)
        return kwargs[key] if key in kwargs else ''


class BaseProgress(abc.ABC):
    _FORMATTER = _EndStringFormatter()

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

    def max_value(self, val: Union[float, None] = None) -> Union[float, BaseProgress]:
        if val:
            self._max_value = val
            return self
        return self._max_value

    def current_value(self, val: Union[float, None] = None) -> Union[BaseProgress, None]:
        if val:
            if self._cap_value:
                self._current_value = min(self._max_value, val)
            else:
                self._current_value = val
            return self
        return self._current_value

    def increment_by(self, val: Union[float, None] = None) -> Union[BaseProgress, None]:
        if val:
            self._increment_by = val
            return self
        return self._increment_by

    def cap_value(self, cap: Union[bool, None]) -> Union[BaseProgress, None]:
        if cap == self._cap_value:
            return

        self._cap_value = cap

        # Cap the current value if necessary
        self.current_value(self.current_value())
        return self

    def prefix(self, val: Optional[str] = None, **kwargs) -> Union[BaseProgress, str]:
        if val:
            self._prefix = str(val)
            self._prefix_kwargs = kwargs
            return self
        return self._prefix

    def prefix_kwargs(self, val: Optional[dict] = None) -> Union[BaseProgress, dict]:
        if val:
            self._prefix_kwargs = dict(val)
            return self
        return self._prefix_kwargs

    def suffix(self, val: Optional[str] = None, **kwargs) -> Union[BaseProgress, str]:
        if val:
            self._suffix = str(val)
            self._suffix_kwargs = kwargs
            return self
        return self._suffix

    def suffix_kwargs(self, val: Optional[dict] = None) -> Union[BaseProgress, dict]:
        if val:
            self._suffix_kwargs = dict(val)
            return self
        return self._suffix_kwargs

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

    def _format_prefix(self) -> str:
        return self._custom_format(self._prefix, self._prefix_kwargs) + ' '

    def _format_suffix(self) -> str:
        return ' ' + self._custom_format(self._suffix, self._suffix_kwargs)

    def _custom_format(self, end, relevant_kwargs: dict) -> str:
        return BaseProgress._FORMATTER.format(end,
                                              percent=(
                                                  str(self.progress * 100) + '%'),
                                              current_value=self.current_value,
                                              max_value=self.max_value,
                                              remaining=self.remaining,
                                              **relevant_kwargs)
