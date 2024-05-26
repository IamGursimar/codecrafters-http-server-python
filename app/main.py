import socket

"""
run ./your_server.sh in one terminal session, and nc -vz 127.0.0.1 4221 in another.
"""


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()  # wait for client
    with conn:
        while True:
            data = conn.recv(1024)
            request_data = data.decode().split("\r\n")
            # TODO: Content length should have dynamic length.
            # TODO: Add echo return value instead of abc.
            response = b"HTTP/1.1 404 Not Found\r\n\r\n"
            request_path = request_data[0].split(" ")[1]
            #  ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
            if not data:
                break

            if request_path == "/":
                response = b"HTTP/1.1 200 OK\r\n\r\n"
            elif "echo" in request_path:
                echo_val = request_path.split("/")[-1]
                response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(echo_val)}\r\n\r\n{echo_val}".encode()
            conn.sendall(response)


if __name__ == "__main__":
    main()
