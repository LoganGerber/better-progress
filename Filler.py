from __future__ import annotations

import math

from typing import Tuple, TypeVar

import _BaseProgress as base


_S = TypeVar('S', bound='Filler')


class Filler(base.BaseProgress):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages: Tuple[str] = (u' ', u'▁',
                                         u'▂', u'▃', u'▄', u'▅', u'▆', u'▇', u'█')

    def __str__(self):
        prefix = self.formatted_prefix()
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix()
        if suffix != '':
            suffix = ' ' + suffix

        stage_index = math.floor(
            max(0, min((len(self._fill_stages) - 1) * self.percent(), self._max_value)))

        return prefix + self._fill_stages[stage_index] + suffix

    def get_fill_stages(self) -> Tuple[str]:
        return self._fill_stages

    def set_fill_stages(self: _S, val: Tuple[str]) -> _S:
        self._fill_stages = val
        return self


class Pie(Filler):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages = ('○', '◔', '◑', '◕', '●')
