import math

class vec3:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,x):
        if isinstance(x, vec3):
            return vec3(self.x+x.x,self.y+x.y,self.z+x.z)
        else:
            return vec3(self.x+x,slef.y+x,self.z+x)

    def __sub__(self,x):
        if isinstance(x, vec3):
            return vec3(self.x-x.x,self.y-x.y,self.z-x.z)
        else:
            return vec3(self.x-x,slef.y-x,self.z-x)

    def __mul__(self,x):
        if isinstance(x, vec3):
            return vec3(self.x*x.x,self.y*x.y,self.z*x.z)
        else:
            return vec3(self.x*x,slef.y*x,self.z*x)

    def __truediv__(self,x):
        if isinstance(x, vec3):
            return vec3(self.x/x.x,self.y/x.y,self.z/x.z)
        else:
            return vec3(self.x/x,self.y/x,self.z/x)

    def length_squared(self):
        return self.x*self.x+self.y*self.y+self.z*self.z

    def length(self):
        return math.sqrt(self.length_squared())

    @staticmethod
    def dot(a,b):
        return a.x*b.x+a.y*b.y+a.z*b.z

    @staticmethod
    def cross(a,b):
        return vec3(
        a.y*b.z-a.z*b.y,
        a.z*b.x-a.x*b.z,
        a.x*b.y-a.y*b.x
        )

    def normalised(self):
        return self/self.length()
    def display(self):
        print("x: ",self.x,",y: ",self.y,",z: ",self.z)
