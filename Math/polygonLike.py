def polygonLike(nums):
	m = {}
	res = len(nums) * (len(nums) - 1) / 2.0
	for num in nums:
		if num not in m:
			m[num] = 1
		else:
			m[num] += 1
	for key in m:
		if m[key] == 1:
			continue
		res -= m[key] * (m[key] - 1) / 2.0
	return res / len(nums)
