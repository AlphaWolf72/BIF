def stupid_function(S, a, b):
    # Print S[a, b], S[0, a], S[b, |S| − 1]
    print(f"S[{a}, {b}] = {S[a:b+1]}, S[0, {a}] = {S[0:a]}, S[{b}, {len(S)-1}] = {S[b:len(S)]}")

    # Print S[0, 2, ..., |S| − 1] if |S| is even, S[0, 2, ..., |S| − 2] else
    if len(S) % 2 == 0:
        print(f"S[0, 2, ..., {len(S)-1}] = {S[0:len(S):2]}")
    else:
        print(f"S[0, 2, ..., {len(S)-2}] = {S[0:len(S)-1:2]}")

    # Calculate and print the GC rate with a precision of two decimals
    gc_count = sum(1 for base in S if base in "GCgc")
    gc_rate = gc_count / len(S) * 100
    print(f"GC rate: {gc_rate:.2f}%")

# Example usage:
string_input = "ATCGATCGATCG"
a_value = 2
b_value = 8
stupid_function(string_input, a_value, b_value)
