# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = [] #global "buffer"
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        while self.queue and n > 0:
            buf[index] = self.queue.pop(0)
            index += 1
            n -= 1
        while n > 0:
            buf4 = [""] * 4
            l = read4(buf4)
            
            #if no more char in file, return
            if not l:
                return index
            #if buff can't contain buf4, save to queue
            if l > n:
                self.queue += buf4[n:l]
            #write buf4 to buff directly
            for i in range(min(l,n)):
                buf[index] = buf4[i]
                index += 1
                n -= 1
        return index
