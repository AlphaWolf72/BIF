class BitArray:
    def __init__(self, size):
        self.size = size
        self.size_in_bytes = (size + 7) // 8
        self.array = bytearray(self.size_in_bytes)

    def get_byte_offset(self, i):
        if i < 0 or i > self.size:
            raise ValueError("Index out of range")
        return i // 8

    def get_bit_position(self, i):
        if i < 0 or i > self.size:
            raise ValueError("Index out of range")
        return i % 8

    def set_bit(self, i):
        if i < 0 or i > self.size:
            raise ValueError("Index out of range")
        byte_offset = self.get_byte_offset(i)
        bit_position = self.get_bit_position(i)
        self.array[byte_offset] = self.array[byte_offset] | (1 << bit_position)  # Ajout du bit dans l'octet

    def get_bit(self, i):
        if i < 0 or i > self.size:
            raise ValueError("Index out of range")
        byte_offset = self.get_byte_offset(i)
        bit_position = self.get_bit_position(i)
        return (self.array[byte_offset] >> bit_position) & 1

    def visualize_byte(self, byte):
        return '{:08b}'.format(byte)

    def visualize_array(self):
        return ' '.join(self.visualize_byte(byte) for byte in self.array)



try:
    # Exemple d'utilisation
    bit_array = BitArray(10)
    # Exemple d'utilisation get_byte_offset
    print(bit_array.get_byte_offset(10))  # Output: 1 (car le bit 10 se trouve dans le deuxième octet)

    # Exemple d'utilisation get_bit_position
    bit_array = BitArray(10)
    print(bit_array.get_bit_position(3))  # Output: 3 (car le bit 3 se trouve à la position 3 dans son octet)
    print(bit_array.get_bit_position(10))  # Output: 2 (car le bit 10 se trouve à la position 2 dans son octet)

    # Exemple d'utilisation set_bit
    bit_array = BitArray(10)
    print(bit_array.visualize_array())  # Output: bytearray(b'\x00\x00') (avant l'appel à set_bit)
    bit_array.set_bit(8)
    print(bit_array.visualize_array())  # Output: bytearray(b'\x08\x00') (après l'appel à set_bit, le 4ème bit est maintenant à 1)

    # Exemple d'utilisation get_bit
    bit_array = BitArray(10)
    print(bit_array.visualize_array())  # Output: bytearray(b'\x00\x00') (avant l'appel à set_bit)
    bit_array.set_bit(3)
    print(bit_array.get_bit(3))  # Output: 1 (le 4ème bit est maintenant à 1)

    # Exemple d'utilisation visualize_byte
    # Test des méthodes
    bit_array = BitArray(10)

    # Test de set_bit et get_bit
    print("Initial array:", bit_array.visualize_array())
    bit_array.set_bit(5)
    print("Array after setting bit 3:", bit_array.visualize_array())
    print("Bit at position 3:", bit_array.get_bit(3))
    print(bit_array.get_bit(11))  # Index hors limites
except ValueError as e:
    print(e)