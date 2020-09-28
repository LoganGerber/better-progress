import abc

import _Base as base


class BaseProgress(base.Base):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        self._max_value = max_value
        self._cap_value = cap_value

        super().__init__(current_value, increment_by)

    @abc.abstractmethod
    def __str__(self):
        return '{} / {}'.format(self._current_value, self._max_value)

    @property
    def max_value(self) -> float:
        return self._max_value

    @max_value.setter
    def max_value(self, val: float) -> None:
        self._max_value = val

    @property
    def current_value(self) -> float:
        return self._current_value

    @current_value.setter
    def current_value(self, val: float) -> None:
        if self._cap_value:
            self._current_value = min(self._max_value, val)
        else:
            self._current_value = val

    @property
    def increment_by(self) -> float:
        return self._increment_by

    @increment_by.setter
    def increment_by(self, val: float) -> None:
        self._increment_by = val

    @property
    def cap_value(self) -> bool:
        return self._cap_value

    @cap_value.setter
    def cap_value(self, cap: bool) -> None:
        if cap == self._cap_value:
            return

        self._cap_value = cap

        # Cap the current value if necessary
        self.current_value = self.current_value

    @property
    def progress(self) -> float:
        return self._current_value / self._max_value

    @property
    def remaining(self) -> float:
        return self._max_value - self._current_value

    def next(self):
        if super().next() > self._max_value and self._cap_value:
            self._current_value = self._max_value
