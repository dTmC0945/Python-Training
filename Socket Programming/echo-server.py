import socket  # importing all the necessary netowk modules

HOST = "127.0.0.1"  # allows the machine to communicate with itself (i.e., localhost)
PORT = 65432  # port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # AF_INET is an address family to tell
    # what type of address the socket can communicate with
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

