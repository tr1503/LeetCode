class Solution:
    def binarySearch(self, arr, target):
        lo = 0
        hi = len(arr)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        search = ""
        
        for c in searchWord:
            temp = []
            search += c
            insert_index = self.binarySearch(products, search)
            for i in range(insert_index, min(len(products), insert_index + 3)):
                if products[i].startswith(search):
                    temp.append(products[i])
            res.append(temp)
        return res
