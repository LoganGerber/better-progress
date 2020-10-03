from __future__ import annotations

import sys
import math

from typing import Union, List, Optional

from _BaseProgress import BaseProgress


class Bar(BaseProgress):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by)

        self._bar_width: int = 32
        self._fill_character: str = '#'
        self._empty_character: str = ' '
        self._bar_prefix: str = '|'
        self._bar_prefix_kwargs: dict = {}
        self._bar_suffix: str = '|'
        self._bar_suffix_kwargs: dict = {}

    def __str__(self):
        filled = math.floor(self._bar_width * self.percent)
        empty = self._bar_width - filled
        prefix = self.formatted_prefix
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix
        if suffix != '':
            suffix = ' ' + suffix
        bar_prefix = self.formatted_bar_prefix
        bar_suffix = self.formatted_bar_suffix

        return prefix + bar_prefix + (self._fill_character * filled) + (self._empty_character * empty) + bar_suffix + suffix

    def bar_width(self, val: Optional[int] = None) -> Union[int, Bar]:
        if val != None:
            self._bar_width = val
            return self
        return self._bar_width

    def fill_character(self, val: Optional[str]) -> Union[str, Bar]:
        if val != None:
            self._fill_character = val
            return self
        return self._fill_character

    def empty_character(self, val: Optional[str]) -> Union[str, Bar]:
        if val != None:
            self._empty_character = val
            return self
        return self._empty_character

    def bar_prefix(self, val: Optional[str]) -> Union[str, Bar]:
        if val != None:
            self._bar_prefix = val
            return self
        return self._bar_prefix

    def bar_prefix_kwargs(self, val: Optional[dict]) -> Union[dict, Bar]:
        if val != None:
            self._bar_prefix_kwargs = val
            return self
        return self._bar_prefix_kwargs

    def bar_suffix(self, val: Optional[str]) -> Union[str, Bar]:
        if val != None:
            self._bar_suffix = val
            return self
        return self._bar_suffix

    def bar_suffix_kwargs(self, val: Optional[dict]) -> Union[dict, Bar]:
        if val != None:
            self._bar_suffix_kwargs = val
            return self
        return self._bar_suffix_kwargs

    @property
    def formatted_bar_prefix(self) -> str:
        return self._custom_format(self._bar_prefix, self._bar_prefix_kwargs)

    @property
    def formatted_bar_suffix(self) -> str:
        return self._custom_format(self._bar_suffix, self._bar_suffix_kwargs)


class IncrementalBar(Bar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        if sys.platform.startswith('win'):
            self._fill_stages: List[str] = [u' ', u'▌']
        else:
            self._fill_stages: List[str] = [
                u' ', u'▏', u'▎', u'▍', u'▌', u'▋', u'▊', u'▉']

        self._fill_character = '█'

    def __str__(self):
        filled = self._bar_width * self.percent
        has_partial = math.modf(filled)[0] != 0
        full_filled = math.floor(filled)
        stage_index = math.floor(math.modf(filled)[0] * len(self._fill_stages))
        empty = self._bar_width - full_filled - (1 if has_partial else 0)

        bar_prefix = self.formatted_bar_prefix
        bar_suffix = self.formatted_bar_suffix

        prefix = self.formatted_prefix
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix
        if suffix != '':
            suffix = ' ' + suffix

        return prefix + bar_prefix + (self._fill_character * full_filled) + (self._fill_stages[stage_index] if has_partial else '') + (self._empty_character * empty) + bar_suffix + suffix

    def fill_stages(self, stages: Optional[List[str]]) -> Union[List[str], IncrementalBar]:
        if stages != None:
            self._fill_stages = stages
            return self
        return self._fill_stages


class RaisingIncrementalBar(IncrementalBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages = [
            u' ', u'▁', u'▂', u'▃', u'▄', u'▅', u'▆', u'▇']
        self._fill_character = '█'


class PixelBar(IncrementalBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages = [' ', '⡀', '⡄', '⡆', '⡇', '⣇', '⣧', '⣷']
        self._fill_character = '⣿'


class ShadyBar(IncrementalBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages = [' ', '░', '▒', '▓']
        self._fill_character = '█'


class ChargingBar(Bar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_character = '█'
        self._empty_character = '.'
        self._bar_prefix = ' '
        self._bar_suffix = ' '


class FillingSquaresBar(ChargingBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._empty_character = '▢'
        self._fill_character = '▣'


class FillingCirclesBar(ChargingBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = False):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._empty_character = '◯'
        self._fill_character = '◉'
