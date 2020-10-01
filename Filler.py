import math

from typing import List

import _BaseProgress as base


class Filler(base.BaseProgress):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages: Tuple[str] = (u' ', u'▁',
                                         u'▂', u'▃', u'▄', u'▅', u'▆', u'▇', u'█')

    def __str__(self):
        prefix = self.formatted_prefix
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix
        if suffix != '':
            suffix = ' ' + suffix

        stage_index = math.floor(
            max(0, min((len(self._fill_stages) - 1) * self.progress)))

        return prefix + self._fill_stages[stage_index] + suffix

    def fill_stages(self, val: Optional[Tuple[str]] = None) -> Union[Filler, Tuple[str]]:
        if val != None:
            self._fill_stages = val
            return self
        return self._fill_stages

