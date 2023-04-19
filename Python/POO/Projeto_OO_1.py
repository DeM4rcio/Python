class Plano():
    def __init__(self, vertices):
        self.vertices = vertices;
        
    def formaGeometrica (self):
        switch = {3:"Triangulo", 4:"Quadrilatero"}
        return switch.get(self.vertices)

quadrado = Plano(4)
print(quadrado.formaGeometrica())

class FormaGeometrica(Plano):
    def __init__(self, vertices) :
        super().__init__(vertices);
        self.vetores = []
        
    def Show(self):
        return f"{self.formaGeometrica()}";

    def Area(self, vetores):
        self.vetores = vetores;
        print(self.vetores)
    
    def Perimetro(self):
        return f"{self.lado * 4}  m";
tri = FormaGeometrica(3)
print(tri.Area([1,2,3,4]))



class Triangulo():
    def __init__(self, base, altura) :
        self.base = base;
        self.altura = altura; 
    
    def Area(self):
        return f"{self.base * self.altura/2} m²";
    
    def Perimetro(self):
        return f"{self.base * 3 } m";
        
class Circulo():
    def __init__(self, raio) :
        self.raio = raio;
        
    def Area(self):
        return f"{self.raio **2 * 3.14} m²";
    
    def Perimetro(self):
        return f"{2*3.14*self.raio} m";
        