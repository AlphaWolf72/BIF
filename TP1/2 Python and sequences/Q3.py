def whereIsA(S):
    # Initialize an empty list to store positions of 'A'
    positions = []

    # Iterate through the string and find positions of 'A'
    for i in range(len(S)):
        if S[i] in "Aa":
            positions.append(i)

    # Return the list of positions
    return positions

# Example usage:
string_input = "ATCGATAGCTAA"
result = whereIsA(string_input)
print(f"Positions of 'A': {result}")
