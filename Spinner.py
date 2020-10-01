from typing import Tuple

from _IPrefixSuffix import IPrefixSuffix


class Spinner(IPrefixSuffix):
    def __init__(self):
        self._stages: Tuple[str] = ('-', '\\', ' | ', ' / ')
        self._current_stage: int = 0

    def __str__(self):
        prefix = self.formatted_prefix
        if prefix != '':
            prefix = prefix + ' '
        suffix = self.formatted_suffix
        if suffix != '':
            suffix = ' ' + suffix

        return prefix + self._stages[self._current_stage] + suffix

    def stages(self, val: Optional[Tuple[str]] = None) -> Union[Tuple[str], Spinner]:
        if val != None:
            self._stages = val
            return self
        return self._stages

    def current_stage(self, val: Optional[int] = None) -> Union[int, Spinner]:
        if val != None:
            self._current_stage = val
            return self
        return self._current_stage

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
