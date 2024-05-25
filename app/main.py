import socket

"""
run ./your_server.sh in one terminal session, and nc -vz 127.0.0.1 4221 in another.
"""


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()  # wait for client


if __name__ == "__main__":
    main()
