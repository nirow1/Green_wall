import struct

def _on_off_bit(i :int, current_byte: bytearray):
    logo_byte = current_byte
    byte_index = (i - 1) // 8
    bit_index = (i - 1) % 8
    logo_byte[byte_index] ^= (1<< bit_index)
    return logo_byte

def ushort_to_hexa(value: str):
    if value == "":
        value = 0
    return bytearray(struct.pack('>H', int(value)))

def time_to_hexa(time: str):
    if time == "":
        time = "0000"
    return bytearray.fromhex(time.replace(':', ''))


def dict_to_bytearray(dictionary) -> bytearray:
            byte1 = 0
            byte2 = 0
            for i in range(1, 9):
                byte1 |= (1 if dictionary[i] else 0) << (i - 1)
            for i in range(9, 17):
                byte2 |= (1 if dictionary[i] else 0) << (i - 9)
            return bytearray([byte1,byte2])