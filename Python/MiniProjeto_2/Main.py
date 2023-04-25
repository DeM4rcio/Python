from my_libraries.Cartesian import *
from my_libraries.Coordenadas import *



def workspace():
    
   
    pt1= Pontos(12,54,1)
    print(pt1.Show())
    
    
    circ2= Circulo(2, 13, 15,1)
    print(circ2.Show())
    
     
    
    dashboard= CartesianBoard()
    dashboard.inserShape(pt1)
    dashboard.inserShape(circ2)

    dashboard.showShapes()

    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()
    
    
    
    print('\nRemoção de uma das formas!')
    
    dashboard.removeShape(pt1)
    dashboard.showShapes() 
    
    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()
    
    
    print('\nVamos pegar uma das formas e atualizar:')
    
    my_copy_of_circ2= dashboard.getShape('Circle_1')
    my_copy_of_circ2.updateCoord(17,22,5)
    print(my_copy_of_circ2.Show())
    
    print('\nO objeto original:')
    print(circ2.Show())
    
    print('\nNote que a atualização da cópia alterou o objeto original!')    

    print('\nPodemos ver se ao inserir um ponto qualquer, o mesmo está dentro do ciruclo!')
    print(circ2.PointIn(1,2))
    
    print('\nCriando um quadrado!')
    quadr1 = Quadrado([4,-1,-1,4],[2,2,-3,-3], 1)
    print('\nDetalhes do quadrado')
    print(quadr1.Show())

    print('\nÁrea do quadrado')
    print(quadr1.AreaEPerimetro())
    print('\nCriando um Triangulo!')
    tri1 = Triangulo([2,5,2],[1,1,4],1)
    print('\nDetalhes do triangulo')
    print(tri1.Show())

    print('\nÁrea do triangulo')
    print(tri1.Area())

    print("\nSuccessful exit")
    
    
    
    
    
    
    



if __name__ == "__main__":

    workspace()
