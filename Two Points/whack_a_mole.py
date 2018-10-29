def whackMole(mole, k):
	res = 0
	window = 0
	for i in range(k):
		window += mole[i]
	i = 0
	j = k - 1
	while j < len(mole):
		i += 1
		j += 1
		if j < len(mole):
			window = window - mole[i-1] + mole[j]
			res = max(res, window)
	return res
