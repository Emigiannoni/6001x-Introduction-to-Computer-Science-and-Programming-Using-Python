ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

s = 'azcbobobegghakl'

indexes = []

for i in range(len(s)):

	indexes.append(ABC.index(s[i]))

partial_indexed_substring = []

final_indexed_substring = []

for i in range(len(indexes) - 1):

	partial_indexed_substring = []

	partial_indexed_substring.append(indexes[i])

	j = i

	while (j + 1) < len(indexes) and indexes[j] <= indexes[j + 1]:

		partial_indexed_substring.append(indexes[j + 1])

		j += 1

	if len(partial_indexed_substring) > len(final_indexed_substring):

		final_indexed_substring = partial_indexed_substring

substring_list = []

for i in range(len(final_indexed_substring)):

	pos = int(final_indexed_substring[i])

	letter = ABC[pos]

	substring_list.append(letter)

substring = "".join(substring_list)

print(substring)