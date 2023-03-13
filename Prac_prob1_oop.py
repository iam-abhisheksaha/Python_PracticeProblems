
class Line:
    
    def __init__(self,coor1,coor2):

        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        dist=((x2-x1)**2+(y2-y1)**2)**0.5
        return dist
    
    def slope(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        slo=(y2-y1)/(x2-x1)
        return slo



my_line = Line((3,2),(8,10))
print(my_line.distance())
print(my_line.slope())