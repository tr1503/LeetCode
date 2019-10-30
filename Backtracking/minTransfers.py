class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # compute net profit for every person
        personNetProfit = dict()
        for lender, borrower, amount in transactions:
            personNetProfit[lender] = personNetProfit.get(lender, 0) - amount
            personNetProfit[borrower] = personNetProfit.get(borrower, 0) + amount
        # Preserved non-zero people only
        netProfit = []
        for amount in personNetProfit.values():
            if amount != 0:
                netProfit.append(amount)
        return self.traverse(netProfit, 0, 0)
    
    def traverse(self, netProfit, start, numTrans):
        # skip zero people
        while start < len(netProfit) and netProfit[start] == 0:
            start += 1
        if start + 1 >= len(netProfit):
            return numTrans
        else:
            for i in range(start + 1, len(netProfit)):
                # greedy condition, put every pair (exp. -5 and 5) together
                if netProfit[start] + netProfit[i] == 0:
                    netProfit[i] += netProfit[start]
                    minNumTrans = self.traverse(netProfit, start + 1, numTrans + 1)
                    netProfit[i] -= netProfit[start]
                    return minNumTrans
            minNumTrans = float('inf')
            for i in range(start + 1, len(netProfit)):
                # non-greedy condition for possible closing out in the future
                if netProfit[start] * netProfit[i] < 0:
                    netProfit[i] += netProfit[start]
                    minNumTrans = min(minNumTrans, self.traverse(netProfit, start + 1, numTrans + 1))
                    netProfit[i] -= netProfit[start]
            return minNumTrans
