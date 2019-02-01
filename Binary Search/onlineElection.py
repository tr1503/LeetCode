class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.leads = []
        self.times = times
        count = {}
        lead = -1
        for p, t in zip(persons, times):
            count[p] = count.get(p, 0) + 1
            if count.get(lead, 0) <= count[p]:
                lead = p
            self.leads.append(lead)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        left = 0
        right = len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] == t:
                return self.leads[mid]
            elif self.times[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
        return self.leads[left - 1]
