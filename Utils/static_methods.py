import numpy as np
import struct

def on_off_bit(i :int, current_byte: bytearray):
    logo_byte = current_byte
    byte_index = (i - 1) // 8
    bit_index = (i - 1) % 8
    logo_byte[byte_index] ^= (1<< bit_index)
    return logo_byte

def ushort_to_hexa(value: str):
    if value == "":
        value = 0
    return bytearray(struct.pack('>H', int(value)))


def time_to_hexa(time: str) -> bytearray:
    time_str = time.replace(':', '')
    time_len = len(time_str)
    if time_len == 3:
        time_str = '0' + time_str
    elif time_len == 2:
        time_str = time_str + '00'
    elif time_len == 1:
        time_str = '0' + time_str + '00'
    elif time_len == 0:
        time_str = "0000"
    print(bytearray.fromhex(time_str))
    return bytearray.fromhex(time_str)

def dict_to_bytearray(dictionary) -> bytearray:
    bits = np.array([int(dictionary[i]) for i in range(1, len(dictionary) + 1)])
    chunks = np.split(bits, len(bits) // 8)
    bytes_list = [np.packbits(chunk)[0] for chunk in chunks]

    return bytearray(bytes_list)
