import matplotlib.pyplot as plt 
#%matplotlib inline 

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 

RedCircle = Circle(10, 'red')

dir (RedCircle)

print (RedCircle.color)
RedCircle.color="grey"
print (RedCircle.color)
RedCircle.drawCircle()