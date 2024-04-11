def encode(kmer):
    encoding = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    binary_representation = ''.join(encoding[base] for base in kmer)
    return int(binary_representation, 2)

# Exemple d'utilisation
kmer = "ATCGG"
encoded_value = encode(kmer)
print(encoded_value)  # Output: 218

def xorshift64(value):
    value ^= value >> 21
    value ^= value << 35
    value ^= value >> 4
    return value

def kmer_to_hash(kmer, seed):
    encoded_value = encode(kmer)
    hashed_value = xorshift64(encoded_value * seed)
    return hashed_value

# Exemple d'utilisation
kmer = "ATCGG"
seed = 123  # Valeur de la seed
hashed_value = kmer_to_hash(kmer, seed)
print(hashed_value)