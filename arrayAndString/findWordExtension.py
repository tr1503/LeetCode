def findWordExtension(s):
	i = 0
	res = []
	while i < len(s):
		j = i + 1
		while j < len(s) and s[j] == s[i]:
			j += 1
		if j - i >= 3:
			res.append([i, j-1])
		i = j
	return res
