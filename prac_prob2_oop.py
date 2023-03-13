class Cylinder:
    
    pi=3.14
    def __init__(self,height=1,radius=1):
        self.radius=radius
        self.height=height
        
    def volume(self):
        vol=self.pi*self.radius*self.radius*self.height
        return vol
    
    def surface_area(self):
        surfaceArea=((2*self.pi*self.radius*self.height) + (2*self.pi*self.radius*self.radius))
        return surfaceArea


my_cylinder = Cylinder(2,3)
print(my_cylinder.volume())
print(my_cylinder.surface_area())