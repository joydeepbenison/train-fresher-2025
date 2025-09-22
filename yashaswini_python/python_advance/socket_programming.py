# server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(1)
print("Server listening...")

conn, addr = server.accept()
print("Connected by", addr)
conn.sendall(b"Hello Client")
conn.close()

