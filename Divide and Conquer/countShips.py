# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', tr: 'Point', bl: 'Point') -> int:
        if tr.x == bl.x and tr.y == bl.y:
            return 1 if sea.hasShips(tr, bl) else 0
        mx = (tr.x + bl.x) // 2
        my = (tr.y + bl.y) // 2
        res = 0
        if mx >= bl.x and my >= bl.y and sea.hasShips(Point(mx, my), bl):
            res += self.countShips(sea, Point(mx, my), bl)
        if mx >= bl.x and tr.y >= my + 1 and my + 1 <= 1000 and sea.hasShips(Point(mx, tr.y), Point(bl.x, my+1)):
            res += self.countShips(sea, Point(mx, tr.y), Point(bl.x, my + 1))
        if tr.x >= mx + 1 and my >= bl.y and my + 1 <= 1000 and sea.hasShips(Point(tr.x, my), Point(mx+1, bl.y)):
            res += self.countShips(sea, Point(tr.x, my), Point(mx + 1, bl.y))
        if tr.x >= mx + 1 and tr.y >= my + 1 and mx + 1 <= 1000 and my + 1 <= 1000 and sea.hasShips(tr, Point(mx+1, my+1)):
            res += self.countShips(sea, tr, Point(mx + 1, my + 1))
        return res
