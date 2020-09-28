import abc


class Base(abc.ABC):
    def __init__(self, current_value: float = 0, increment_by: float = 1):
        self._current_value = current_value
        self._increment_by = increment_by

    def next(self):
        self._current_value += self._increment_by
        return self._current_value
