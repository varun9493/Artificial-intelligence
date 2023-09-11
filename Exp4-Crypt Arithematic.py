from itertools import permutations

def solve_cryptarithmetic(puzzle):
    words = puzzle.split()  # Split puzzle into words
    unique_chars = set("".join(words))  # Get unique characters
    if len(unique_chars) > 10:
        return "Too many unique characters (more than 10)"

    for perm in permutations(range(10), len(unique_chars)):
        char_to_digit = {char: digit for char, digit in zip(unique_chars, perm)}
        if all(char_to_digit[word[0]] != 0 for word in words):
            numbers = [int("".join(str(char_to_digit[char]) for char in word)) for word in words[:-1]]
            result = sum(numbers)
            if result == int("".join(str(char_to_digit[char]) for char in words[-1])):
                return char_to_digit

    return "No solution found"

# Example usage
puzzle = "SEND + MORE = MONEY"
solution = solve_cryptarithmetic(puzzle)
print(solution)
