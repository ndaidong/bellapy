#!/usr/bin/env python3

import socket
from uuid import getnode


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ipaddr = s.getsockname()[0]
        s.close()
        return ipaddr
    except Exception:
        pass
    return ''


def get_mac():
    try:
        return (':'.join(['{:02x}'.format(
            (getnode() >> i) & 0xff) for i in range(
                0, 8*6, 8
            )][::-1]
        ))
    except Exception:
        pass
    return ''
