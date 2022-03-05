from ctypes import *

from src.protocols import Protocol

class DNS(Protocol):
    _fields_ = [
        ("id", c_uint16),
        ("flags", c_uint16),
        ("qdcount", c_uint16),
        ("ancount", c_uint16),
        ("nscount", c_uint16),
        ("arcount", c_uint16),
        ("query", str)
    ]
    
    header_len = 12
    
    def __init__(self, packet: bytes):
        print("DNS BUILT")
        super().__init__(packet)