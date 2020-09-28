import typing
import math

import Bar


class ChargingBar(Bar.Bar):
    def __init__(self, max_value: int = 100, current_value: int = 0, increment_by: float = 1, prefix: str = '', suffix: str = '', bar_width: int = 32, fill: str = '█', fill_stages: typing.List[str] = [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'], empty_fill: str = ' ', bar_prefix: str = '|', bar_suffix: str = '|'):
        self._fill_stages = fill_stages

        super().__init__(max_value, current_value, increment_by, prefix,
                         suffix, bar_width, fill, empty_fill, bar_prefix, bar_suffix)

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
