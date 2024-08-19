def compress_string(s):
    compressed = []  # Initialize an empty list for the compressed characters
    count = 1  # Initialize the count for consecutive characters

    # Iterate through the string (except the last character)
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # If the current character is the same as the previous one
            count += 1  # Increment the count
        else:
            # Append the character and its count to the result list
            compressed.append(s[i - 1] + str(count))
            count = 1  # Reset the count for the next character

    # Append the last character and its count
    compressed.append(s[-1] + str(count))

    # Join the list elements to form the final compressed string
    return ''.join(compressed)

# Example usage
input_string = "aabcccccaaa"
compressed_result = compress_string(input_string)
print("Compressed result:", compressed_result)  # Output: 'a2b1c5a3'
