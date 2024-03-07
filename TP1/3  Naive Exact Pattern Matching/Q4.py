import time
def naive_pattern_matching(P, T):
    m = len(P)  # Length of the pattern
    n = len(T)  # Length of the text

    # Iterate through all possible starting positions of the pattern in the text
    for i in range(n - m + 1):
        # Check if the substring of length m starting at position i matches the pattern P
        if T[i:i+m] == P:
            print(f"Pattern found at position {i}")


def naive_pattern_matching2(P, T):
    m = len(P)  # Length of the pattern
    n = len(T)  # Length of the text

    # Iterate through all possible starting positions of the pattern in the text
    for i in range(n - m + 1):
        j = 0
        # Check if the substring of length m starting at position i matches the pattern P
        while j < m:
            if T[i+j] != P[j]:
                break
            j += 1
        if j == m:
            print(f"Pattern found at position {i}")



# Example usage:
pattern = "ACGT"
text = "ACGTAACGTACGTA"


time1 = time.time()
naive_pattern_matching(pattern, text)
time2 = time.time()

print("V1 : ", time2 - time1)

time1 = time.time()
naive_pattern_matching2(pattern, text)
time2 = time.time()

print("V2 : ", time2 - time1)