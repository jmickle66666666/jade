import math
def dist(x1,y1,x2,y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Sect(object):
		def __init__(self,verts):
			self.verts = verts
	