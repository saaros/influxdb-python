

import socket
import time


def get_free_port(ip='127.0.0.1'):
    sock = socket.socket()
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((ip, 0))
        return sock.getsockname()[1]
    finally:
        sock.close()

        # Is there a better way than a sleep?
        # There were issues on Travis where the port was not yet free.
        time.sleep(0.1)


def is_port_open(port, ip='127.0.0.1'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex((ip, port))
        if not result:
            sock.shutdown(socket.SHUT_RDWR)
        return result == 0
    finally:
        sock.close()
