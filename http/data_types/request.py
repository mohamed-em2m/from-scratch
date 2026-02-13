from dataclasses import dataclass


@dataclass
class HTTPRequest:
    method: str
    path: str
    protocol: str
    headers: dict
    body: str | dict
