def cutTable(cuts, n):
	m = len(cuts)
	cuts.insert(0,0)
	cuts.append(n)
	dp = [[0 for _ in range(m + 2)] for _ in range(m + 2)]
	for i in range(m + 1):
		dp[i][i+1] = 0
	for k in range(1, m + 2):
		for i in range(m + 2 - k):
			j = i + k
			if k == 1:
				dp[i][j] = 0
				continue
			dp[i][j] = float('inf')
			for p in range(i+1,j):
				dp[i][j] = min(dp[i][j],dp[i][p]+dp[p][j]+cuts[j]-cuts[i])
	return dp[0][m+1]
