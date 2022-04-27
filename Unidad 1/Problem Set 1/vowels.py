ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

s = 'azcbobobegghakl'

provisory_substring = []

selected_substring = []


for i in range(len(s)):

	provisory_substring.append(s[i])

	current_index = ABC.index(s[i])

	next_letter = 1

	for j in range(len(s) - i):

		next_index = ABC.index(s[i + j])

		if next_index >= current_index:

			provisory_substring.append(s[i + j])

		else:

			break

	if len(provisory_substring) > len(selected_substring):

		selected_substring = provisory_substring

print(selected_substring)

