from dataclasses import dataclass
import json


@dataclass
class HTTPResponse:
    status_code: int
    reason: str
    headers: str | dict
    body: str | dict

    def to_bytes(self):
        if isinstance(self.body, dict):
            response_body = json.dumps(self.body)
        elif isinstance(self.body, str):
            response_body = self.body

        encoded_body = response_body.encode()
        status_line = f"HTTP/1.1 {self.status_code} {self.reason}\r\n"

        if isinstance(self.headers, dict):
            self.headers["Content-Length"] = len(encoded_body)
            header_lines = "\r\n".join(
                [f"{key}: {value}" for key, value in self.headers.items()]
            )
        else:
            header_lines = self.headers
        response_header = status_line + header_lines
        response = response_header.encode() + b"\r\n\r\n" + encoded_body
        return response
