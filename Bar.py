from __future__ import annotations

import sys
import math

from typing import TypeVar, List

from _BaseProgress import BaseProgress


_B = TypeVar('B', bound='Bar')


class Bar(BaseProgress):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by)

        self._bar_width: int = 32
        self._fill_character: str = '#'
        self._empty_character: str = ' '
        self._bar_prefix: str = '|'
        self._bar_prefix_replacement_fields: dict = {}
        self._bar_suffix: str = '|'
        self._bar_suffix_replacement_fields: dict = {}

    def __str__(self):
        filled = math.floor(self._bar_width * self.percent())
        empty = self._bar_width - filled
        prefix = self.formatted_prefix()
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix()
        if suffix != '':
            suffix = ' ' + suffix
        bar_prefix = self.formatted_bar_prefix()
        bar_suffix = self.formatted_bar_suffix()

        return prefix + bar_prefix + (self._fill_character * filled) + (self._empty_character * empty) + bar_suffix + suffix

    def get_bar_width(self) -> int:
        return self._bar_width

    def set_bar_width(self: _B, val: int) -> _B:
        self._bar_width = val
        return self

    def get_fill_character(self) -> str:
        return self._fill_character

    def set_fill_character(self: _B, val: str) -> _B:
        self._fill_character = val
        return self

    def get_empty_character(self) -> str:
        return self._empty_character

    def set_empty_character(self: _B, val: str) -> _B:
        self._empty_character = val
        return self

    def get_bar_prefix(self) -> str:
        return self._bar_prefix

    def set_bar_prefix(self: _B, val: str) -> _B:
        self._bar_prefix = val
        return self

    def get_bar_prefix_replacement_fields(self) -> dict:
        return self._bar_prefix_replacement_fields

    def set_bar_prefix_replacement_fields(self: _B, val: dict) -> _B:
        self._bar_prefix_replacement_fields = val
        return self

    def get_bar_suffix(self) -> str:
        return self._bar_suffix

    def set_bar_suffix(self: _B, val: str) -> _B:
        self._bar_suffix = val
        return self

    def get_bar_suffix_replacement_fields(self) -> dict:
        return self._bar_suffix_replacement_fields

    def set_bar_suffix_replacement_fields(self: _B, val: dict) -> _B:
        self._bar_suffix_replacement_fields = val
        return self

    def formatted_bar_prefix(self) -> str:
        return self._custom_format(self._bar_prefix, self._bar_prefix_replacement_fields)

    def formatted_bar_suffix(self) -> str:
        return self._custom_format(self._bar_suffix, self._bar_suffix_replacement_fields)


_I = TypeVar('I', bound='IncrementalBar')


class IncrementalBar(Bar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by, cap_value)

        if sys.platform.startswith('win'):
            self._fill_stages: List[str] = [u' ', u'▌']
        else:
            self._fill_stages: List[str] = [
                u' ', u'▏', u'▎', u'▍', u'▌', u'▋', u'▊', u'▉']

        self._fill_character = '█'

    def __str__(self):
        filled = self._bar_width * self.percent()
        has_partial = math.modf(filled)[0] != 0
        full_filled = math.floor(filled)
        stage_index = math.floor(math.modf(filled)[0] * len(self._fill_stages))
        empty = self._bar_width - full_filled - (1 if has_partial else 0)

        bar_prefix = self.formatted_bar_prefix()
        bar_suffix = self.formatted_bar_suffix()

        prefix = self.formatted_prefix()
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix()
        if suffix != '':
            suffix = ' ' + suffix

        return prefix + bar_prefix + (self._fill_character * full_filled) + (self._fill_stages[stage_index] if has_partial else '') + (self._empty_character * empty) + bar_suffix + suffix

    def get_fill_stages(self) -> List[str]:
        return self._fill_stages

    def set_fill_stages(self: _I, stages: List[str]) -> _I:
        self._fill_stages = stages
        return self


class RaisingIncrementalBar(IncrementalBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages = [
            u' ', u'▁', u'▂', u'▃', u'▄', u'▅', u'▆', u'▇']
        self._fill_character = '█'


class PixelBar(IncrementalBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages = [' ', '⡀', '⡄', '⡆', '⡇', '⣇', '⣧', '⣷']
        self._fill_character = '⣿'


class ShadyBar(IncrementalBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_stages = [' ', '░', '▒', '▓']
        self._fill_character = '█'


class ChargingBar(Bar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._fill_character = '█'
        self._empty_character = '.'
        self._bar_prefix = ''
        self._bar_suffix = ''


class FillingSquaresBar(ChargingBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._empty_character = '▢'
        self._fill_character = '▣'


class FillingCirclesBar(ChargingBar):
    def __init__(self, max_value: float = 100, current_value: float = 0, increment_by: float = 1, cap_value: bool = True):
        super().__init__(max_value, current_value, increment_by, cap_value)

        self._empty_character = '◯'
        self._fill_character = '◉'
