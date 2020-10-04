from __future__ import annotations

import abc
import string

from typing import TypeVar


class _EndStringFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            if len(args) > key:
                return args[key]
            else:
                return '{{}}'
        return kwargs[key] if key in kwargs else '{{{}}}'.format(key)


S = TypeVar('S', bound='IPrefixSuffix')


class IPrefixSuffix(abc.ABC):
    _FORMATTER = _EndStringFormatter()

    def __init__(self: S):
        self._prefix: str = ''
        self._prefix_replacement_fields: dict = {}
        self._suffix: str = ''
        self._suffix_replacement_fields: dict = {}

    def get_prefix(self) -> str:
        return self._prefix

    def set_prefix(self: S, val: str, **kwargs) -> S:
        self._prefix = val
        if len(kwargs) > 0:
            self._prefix_replacement_fields = kwargs
        return self

    def get_prefix_replacement_fields(self) -> dict:
        return self._prefix_replacement_fields

    def set_prefix_replacement_fields(self: S, val: dict) -> S:
        self._prefix_replacement_fields = val
        return self

    def get_suffix(self) -> str:
        return self._suffix

    def set_suffix(self: S, val: str, **kwargs) -> S:
        self._suffix = val
        if len(kwargs) > 0:
            self._suffix_replacement_fields = kwargs
        return self

    def get_suffix_replacement_fields(self) -> dict:
        return self._suffix_replacement_fields

    def set_suffix_replacement_fields(self: S, val: dict) -> S:
        self._suffix_replacement_fields = val
        return self

    def formatted_prefix(self) -> str:
        return self._custom_format(self._prefix, self._prefix_replacement_fields)

    def formatted_suffix(self) -> str:
        return self._custom_format(self._suffix, self._suffix_replacement_fields)

    def _custom_format(self, text: str, relevant_kwargs: dict = {}) -> str:
        return IPrefixSuffix._FORMATTER.format(text, **relevant_kwargs)
