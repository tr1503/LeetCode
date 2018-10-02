class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        '''Brute Force Way: iter the time after giving time.
        The first value has all numbers from the original time (right now is a set) is the result.'''
        s = set(time)
        hour = int(time[0:2])
        minute = int(time[3:5])
        while True:
            minute += 1
            if minute == 60:
                minute = 0
                if hour == 23:
                    hour = 0
                else:
                    hour += 1
            time = "%02d:%02d" % (hour, minute)
            if set(time) <= s:
                return time
        return time
