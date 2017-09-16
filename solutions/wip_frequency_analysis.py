text = str(input())

freq = {}
for char in 'abcdefghijklmnopqrstuvwxyz':
    freq[char] = 0

n_char = 0
for char in text:
    if char.isalpha():
        c = char.lower()
        freq[c] += 1
        n_char += 1

# Normalize frequencies so they sum to 1.
# for char in freq.keys():
#     freq[char] = freq[char] / n_char

for char in 'abcdefghijklmnopqrstuvwxyz':
    print(char + ' ' + str(freq[char]))