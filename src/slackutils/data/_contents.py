from __future__ import annotations

from collections.abc import Sequence
from enum import Enum
from typing import Any, NamedTuple, Optional, TypedDict, Union


class Color(Enum):
    GOOD = "#2EB886"
    WARNING = "#DAA038"
    DANGER = "#A30100"

    @classmethod
    def get_code(cls, name: str) -> str:
        return cls[name.upper()].value


class Text(TypedDict):
    type: str
    text: str


class SimpleSection(TypedDict):
    type: str
    text: Text


class FieldsSection(TypedDict):
    type: str
    fields: Sequence[Text]


class Attachments(NamedTuple):
    color: Optional[str]
    header: Optional[str]
    message: Optional[str]
    fields: Sequence[str]
    footer: Optional[str]

    @staticmethod
    def _convert_to_mrkdwn_section(val: str) -> SimpleSection:
        return SimpleSection(
            type="section",
            text=Text(
                type="mrkdwn",
                text=val,
            ),
        )

    def _header_to_dict(self) -> Optional[SimpleSection]:
        if self.header:
            return SimpleSection(
                type="header",
                text=Text(
                    type="plain_text",
                    text=self.header,
                ),
            )
        return None

    def _message_to_dict(self) -> Optional[SimpleSection]:
        if self.message:
            return self._convert_to_mrkdwn_section(self.message)
        return None

    def _fields_to_dict(self) -> Optional[FieldsSection]:
        if self.fields:
            return FieldsSection(
                type="section",
                fields=[Text(type="mrkdwn", text=field) for field in self.fields],
            )
        return None

    def _footer_to_dict(self) -> Optional[SimpleSection]:
        if self.footer:
            return self._convert_to_mrkdwn_section(self.footer)
        return None

    def _build_block(self) -> list[Union[SimpleSection, FieldsSection]]:
        ret: list[Union[SimpleSection, FieldsSection]] = []
        if header := self._header_to_dict():
            ret.append(header)
        if message := self._message_to_dict():
            ret.append(message)
        if fields := self._fields_to_dict():
            ret.append(fields)
        if footer := self._footer_to_dict():
            ret.append(footer)
        return ret

    def to_payload(self) -> list[dict[str, Any]]:
        ret: dict[str, Any] = {}
        if self.color:
            ret["color"] = Color.get_code(self.color)
        if block := self._build_block():
            ret["blocks"] = block
        return [ret]
