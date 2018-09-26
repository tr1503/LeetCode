class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domains = collections.Counter()
        for cp in cpdomains:
            num = cp.split()[0]
            domain = cp.split()[1].split('.')
            for i in range(len(domain)):
                domains[".".join(domain[i:])] += int(num)
        return [" ".join((str(v),k)) for k,v in domains.items()]
