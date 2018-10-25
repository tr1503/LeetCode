class BashParser(object):
    def parse(self, string):
        bigParts = self.separateHighCommas(string)

        retList = list()
        for bigPart in bigParts:
            retList.extend(self.parsePart(bigPart))
        return retList

    def separateHighCommas(self, string):
        index = 0
        iStart = 0
        pCount = 0
        tokenList = list()
        while index < len(string):
            if string[index] == '(': pCount += 1
            if string[index] == ')': pCount -= 1
            if string[index] == ',' and pCount == 0:
                tokenList.append(string[iStart:index])
                iStart = index + 1
            index += 1
        if len(string) - iStart > 0:
            tokenList.append(string[iStart:])
        return tokenList

    def parsePart(self, string):
        tokens = self.separateTokens(string)
        if len(tokens) == 1 and tokens[0] == string:
            return tokens[0]
        else:
            return self.comb(*map(self.parse, tokens))

    def separateTokens(self, string):
        index = 0
        iStart = 0
        pCount = 0
        tokenList = list()
        while index < len(string):
            if string[index] == '(':
                if pCount == 0 and index - iStart > 0:
                    tokenList.append(string[iStart:index])
                    iStart = index
                pCount += 1
            if string[index] == ')':
                pCount -= 1
                if pCount == 0:
                    tokenList.append(string[iStart+1:index])
                    iStart = index + 1
            index += 1
        if iStart < index:
            tokenList.append(string[iStart:])
        return tokenList

    def comb(self, *lists):
        index = 0
        frontier = ['']
        while index < len(lists):
            next = list()
            for string in frontier:
                for elem in lists[index]:
                    next.append(string + elem)
            index += 1
            frontier = next
        return frontier

def main():

    bp = BashParser()
    print(bp.parse('a(b(c,d),a(p,q))'))

if __name__ == '__main__':
    main()
