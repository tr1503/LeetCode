# get the index difference of first number after this element that is larger than this element
# if there is no number larger than this element, return -1
def indexDiff(nums):
	if len(nums) == 0:
		return []
	res = [-1 for _ in range(len(nums))]
	stack = [] # add [number, index]

	for i, num in enumerate(nums):
		while len(stack) != 0 and num > stack[-1][0]:
			smallIndex = stack[-1][1]
			res[smallIndex] = i - smallIndex
			stack.pop()
		stack.append([num,i])
	return res

def main():
	nums = [10, 8, 6, 8, 8, 11, 9]
	print(indexDiff(nums))

if __name__ == '__main__':
	main()
