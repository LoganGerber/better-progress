from __future__ import annotations

from typing import Tuple, TypeVar

from _IPrefixSuffix import IPrefixSuffix


_S = TypeVar('S', bound='Spinner')


class Spinner(IPrefixSuffix):
    def __init__(self):
        super().__init__()

        self._stages: Tuple[str] = ('-', '\\', '|', '/')
        self._current_stage: int = 0

    def __str__(self):
        prefix = self.formatted_prefix()
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix()
        if suffix != '':
            suffix = ' ' + suffix

        return prefix + self._stages[self._current_stage] + suffix

    def get_stages(self) -> Tuple[str]:
        return self._stages

    def set_stages(self: _S, val: Tuple[str]) -> _S:
        self._stages = val
        return self

    def get_current_stage(self) -> int:
        return self._current_stage

    def set_current_stage(self: _S, val: int) -> _S:
        self._current_stage = val
        return self

    def next(self):
        self._current_stage = (self._current_stage + 1) % len(self._stages)


class PieSpinner(Spinner):
    def __init__(self):
        super().__init__()

        self._stages = ('◷', '◶', '◵', '◴')


class MoonSpinner(Spinner):
    def __init__(self):
        super().__init__()

        self._stages = ('◑', '◒', '◐', '◓')


class LineSpinner(Spinner):
    def __init__(self):
        super().__init__()

        self._stages = ('⎺', '⎻', '⎼', '⎽', '⎼', '⎻')


class PixelSpinner(Spinner):
    def __init__(self):
        super().__init__()

        self._stages = ('⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽')
