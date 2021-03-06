# Stubs for email.parser (Python 3.4)

import email.feedparser
from email.message import Message
from typing import Callable, Optional, TextIO, BinaryIO
from email.policy import Policy

FeedParser = email.feedparser.FeedParser
BytesFeedParser = email.feedparser.BytesFeedParser

class Parser:
    def __init__(self, _class: Callable[[], Message] = ..., *,
                 policy: Policy = ...) -> None: ...
    def parse(self, fp: TextIO, headersonly: bool = ...) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...

class HeaderParser(Parser):
    def __init__(self, _class: Callable[[], Message] = ..., *,
                 policy: Policy = ...) -> None: ...
    def parse(self, fp: TextIO, headersonly: bool = ...) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...

class BytesHeaderParser(BytesParser):
    def __init__(self, _class: Callable[[], Message] = ..., *,
                 policy: Policy = ...) -> None: ...
    def parse(self, fp: BinaryIO, headersonly: bool = ...) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...

class BytesParser:
    def __init__(self, _class: Callable[[], Message] = ..., *,
                 policy: Policy = ...) -> None: ...
    def parse(self, fp: BinaryIO, headersonly: bool = ...) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...
