class point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return"points are ({0},{1})".format(self.x,self.y)
    
point1 = point(5,6)
print(point1)