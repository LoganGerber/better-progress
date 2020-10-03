import abc
import string

from typing import Union, Optional


class _EndStringFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            return super().get_value(key, args, kwargs)
        return kwargs[key] if key in kwargs else ''


class IPrefixSuffix(abc.ABC):
    _FORMATTER = _EndStringFormatter()

    def __init__(self):
        self._prefix: str = ''
        self._prefix_kwargs: dict = {}
        self._suffix: str = ''
        self._suffix_kwargs: dict = {}

    def prefix(self, val: Optional[str] = None, **kwargs) -> Union[IPrefixSuffix, str]:
        if val != None:
            self._prefix = str(val)
            self._prefix_kwargs = kwargs
            return self
        return self._prefix

    def prefix_kwargs(self, val: Optional[dict] = None) -> Union[IPrefixSuffix, dict]:
        if val != None:
            self._prefix_kwargs = dict(val)
            return self
        return self._prefix_kwargs

    def suffix(self, val: Optional[str] = None, **kwargs) -> Union[IPrefixSuffix, str]:
        if val != None:
            self._suffix = str(val)
            self._suffix_kwargs = kwargs
            return self
        return self._suffix

    def suffix_kwargs(self, val: Optional[dict] = None) -> Union[IPrefixSuffix, dict]:
        if val != None:
            self._suffix_kwargs = dict(val)
            return self
        return self._suffix_kwargs

    @property
    def formatted_prefix(self) -> str:
        return self._custom_format(self._prefix, self._prefix_kwargs)

    @property
    def formatted_suffix(self) -> str:
        return self._custom_format(self._suffix, self._suffix_kwargs)

    def _custom_format(self, text: str, relevant_kwargs: dict = {}) -> str:
        return IPrefixSuffix._FORMATTER.format(text, **relevant_kwargs)
