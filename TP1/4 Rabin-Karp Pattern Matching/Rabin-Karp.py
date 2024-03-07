# Q5
def equals(A, B):
    return A == B

# Example usage:
word1 = "hello"
word2 = "world"
result = equals(word1, word2)
print(result)  # This will print False


# Q6
p = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
def hash_value(S, p):
    return sum(p[S[i]] * 10 ** i for i in range(len(S)))

# Example usage:
string_example = "ACGT"
result = hash_value(string_example, p)
print(result)


# Q7
def update_hash_value(previous_hash, leaving, entering, p, m):
    previous_hash -= p[leaving]
    previous_hash //= 10
    previous_hash += p[entering] * 10 ** (m-1)
    return previous_hash

# Example usage:
prev_hash = hash_value("ACG", p)
print(prev_hash)
leaving = "A"
entering = "T"
pattern_length = 3
result = update_hash_value(prev_hash, leaving, entering, p, pattern_length)
print(result)


# Q8
# Validation:
text = "ACG"
pattern = "CGT"
pattern_length = len(pattern)
hash_pattern = hash_value(pattern, p)
print("Hash value of pattern:", hash_pattern)

# Initial hash for the first window in the text
initial_hash = hash_value(text[:pattern_length], p)
print("Initial hash value of the first window in the text:", initial_hash)

# Update hash for the next window
updated_hash = update_hash_value(initial_hash, "A", "G", p, pattern_length)
print("Updated hash value for the next window in the text:", updated_hash)



# Q9
def RabinKarp(P, T, p):
    m = len(P)
    n = len(T)

    # Calculate hash values
    hash_pattern = hash_value(P, p)
    hash_text = hash_value(T[:m], p)

    # Iterate through the text
    for i in range(n - m + 1):
        if hash_pattern == hash_text and equals(P, T[i:i+m]):
            print(f"Pattern found at position {i}")

        # Update hash value for the next window in the text
        if i < n - m:
            print(f"old {hash_text}")
            hash_text = update_hash_value(hash_text, T[i], T[i+m], p, m)
            print(f"new {hash_text}")

# Example usage:
pattern_to_find = "CGT"
text_to_search = "ACGTACGTACGT"
prime_number = 31
RabinKarp(pattern_to_find, text_to_search, p)
