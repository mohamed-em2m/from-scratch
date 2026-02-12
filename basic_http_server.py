import socket
import json
port=3001
s=socket.socket()
s.bind(("",port))
s.listen()
while True:
    c,addr=s.accept()
    response = c.recv(4096)
    print("recive request",response)
    body=json.dumps({"message":"hello emam greet you"}).encode()
    respones=("HTTP/1.1 200 OK\r\n"
              "Content-Type: application/json\r\n"
              f"Content-Length: {len(body)}\r\n"
              "\r\n"
              ).encode() + body
    c.send(respones)
    c.close()
