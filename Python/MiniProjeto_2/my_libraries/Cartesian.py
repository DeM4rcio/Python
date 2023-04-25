from . import Coordenadas


class CartesianBoard():
    
    
    
    def __init__(self):
        
        self.shapes= {}
        
        
    def inserShape(self, shape):
        
        self.shapes[shape.getType() + str(shape.getNumber())]= shape
        
        
    def removeShape(self, shape):
        
        del self.shapes[shape.getType() + str(shape.getNumber())]
        
        
    def showShapes(self):
        
        print('\nEste plano cartesiano possui as seguintes formas:\n')
        for shape in self.shapes.keys():
            print(shape)
    
    
    def printDetails(self):
        
        for key in self.shapes.keys():
            print(self.shapes[key].Show())
                                                                                                           
        
    def getShape(self,key):
        return self.shapes[key]
