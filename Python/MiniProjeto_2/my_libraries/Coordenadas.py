class Pontos():
    def __init__(self, vetoresX, vetoresY, n) :
        self.n = n;
        self.vetoresX = vetoresX;
        self.vetoresY = vetoresY;

    def updateCoord(self,x,y):
        self.vetoresY = y;
        self.vetoresX = x;

    
    def add(self, x, y):
        self.vetoresX.append(x);
        self.vetoresY.append(y);
        return f"Adicionado com sucesso!"
    
    def Show(self):
        return f"Seus vetores são x:{self.vetoresX}, y:{self.vetoresY}"
    
    def Deletar(self, index):
        self.vetoresX.pop(index - 1);
        self.vetoresY.pop(index - 1);
        return f"Deletado com sucesso!"
    
    def getType(self):
        return 'Point_'
        
        
    def getNumber(self):
        return self.n
    


class Triangulo(Pontos):
    def __init__(self, vetoresX, vetoresY, n):
        self.retast = [];
        
        super().__init__(vetoresX, vetoresY,n)
    
    def Area(self):
        self.retast = []
        
        for i in range(3):
            calculo = ((self.vetoresX[-2 + i] - self.vetoresX[i] )**2 + (self.vetoresY[-2 + i]-self.vetoresY[i] )**2)**1/2
            self.retast.append(calculo)
        print(self.retast)        
        if self.retast[0] == self.retast[2]:
            return f"{(self.retast[0]**2)*(3**1/2)/4} metros quadrados";
        else:
            return "O programa não comporta outro tipo de triângulo"
        
        
    def getType(self):
        
        return 'Triangule_'

    def Perimetro(self):
        return f"{sum(self.retast)} metros";


    


class Circulo(Pontos):
    def __init__(self, vetoresX, vetoresY, raio,n):
        
        self.raio = raio;
        super().__init__(vetoresX, vetoresY,n)
    
    def getType(self):
        
        return 'Circle_'
        
    def updateCoord(self,radius,x,y): 
        self.raio= radius
        super().updateCoord(x,y)
    
    def Show(self):
        return f"{super().Show()} e com {self.raio} de raio"


    def Area(self):
        return f"{self.raio **2 * 3.14} m²";
    
    def Perimetro(self):
        return f"{2*3.14*self.raio} m";

    def PointIn(self,x,y):
        calculo = ((self.vetoresX - x)**2 + (self.vetoresY - y)**2)**1/2
        if self.raio >= calculo:
            return "O ponto está contido no circulo"
        else:
            return "o ponto está fora do circulo"



class Quadrado(Pontos):
    def __init__(self, vetoresX, vetoresY,n):
        super().__init__(vetoresX, vetoresY,n)

    def AreaEPerimetro(self):

        self.retas = []
        
        for i in range(4):
            calculo = ((self.vetoresX[i] - self.vetoresX[-3 + i])**2 + (self.vetoresY[i] - self.vetoresY[-3 + i])**2)**1/2
            self.retas.append(calculo)
        
   
        if self.retas[0] == self.retas[1] == self.retas[2] == self.retas[3]:
            return f"{(self.retas[0]**2)} metros quadrados e com {self.retas[0]*4} de perimetro";
        else:
            return "O programa não comporta outro tipo de quadrilátero"
        
    

    def getType(self):
        
        return 'quadrilateral_'
    
    