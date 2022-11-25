import socket

HOST = "127.0.0.1" # server IP address
PORT = 65432 # server port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall((b"Hello, World!"))
    data = s.recv(1024)

print(f"Received {data!r}")
