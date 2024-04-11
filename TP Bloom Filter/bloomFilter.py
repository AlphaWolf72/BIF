import mmh3  # Import de la fonction de hachage MurmurHash3
import byteArray as BA
import encode as EN
class BloomFilter:
    def __init__(self, size, nb_hash, hash_size, hash_func=None):
        self.size = size
        self.nb_hash = nb_hash
        self.hash_size = hash_size
        self.array = BA.BitArray(size)
        self.hash_func = hash_func if hash_func else mmh3.hash

    # Méthode pour ajouter un élément au filtre de Bloom
    def add(self, kmer):
        for i in range(self.nb_hash):
            hash_value = self.hash_func(kmer, i) % self.size
            self.array.set_bit(hash_value)

    # Méthode spéciale pour l'opérateur "in"
    def __contains__(self, kmer):
        for i in range(self.nb_hash):
            hash_value = self.hash_func(kmer, i) % self.size
            if self.array.get_bit(hash_value) == 0:
                return False
        return True

    # Méthode pour obtenir les valeurs de hachage pour un élément
    def get_hash_values(self, kmer):
        hash_values = []
        for i in range(self.nb_hash):
            hash_value = self.hash_func(kmer, i) % self.size
            hash_values.append(hash_value)
        return hash_values


# Exemple d'utilisation avec la fonction MurmurHash3 par défaut
bloom_filter = BloomFilter(size=100, nb_hash=3, hash_size=32)
bloom_filter.add("ATCGG")
bloom_filter.add("ATCGC")
print("ATCGG" in bloom_filter)  # Output: True
print("ATCCG" in bloom_filter)  # Output: False

bloom_filter = BloomFilter(size=100, nb_hash=3, hash_size=32, hash_func=EN.kmer_to_hash)
hash_values = bloom_filter.get_hash_values("ATCGG")
print(hash_values)
hash_values = bloom_filter.get_hash_values("ATCCG")
print(hash_values)

