# Frequency count

def count_char_frequencies(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

# Example usage:
s = "hello world"
print(count_char_frequencies(s))
