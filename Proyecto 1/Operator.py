class Operator():
    def __init__(self,joint,relation):
        # joint = conjunto
        self.joint = joint
        # relation = relacion
        self.relation = relation
        self.isValid = True
        self.validateRelation(relation)

    # PRUEBA PARA VER SI LA RELACION CONINCIDE CON EL CONJUNTO
    def validateRelation(self,relation):
        for relationship in relation:
            num1 = relationship[0]
            num2 = relationship[1]
            if num1 not in self.joint:
                self.isValid = False
                print(str(num1) + " not in joint!")
            elif num2 not in self.joint:
                self.isValid = False
                print(str(num2) + " not in joint!")
                
    # Funcion para primer parte
    def closedTransitiveRel(self):
        self.matriz = list(list(1 if (y+1,x+1) in self.relation else 0 for x in range(len(self.joint))) for y in range(len(self.joint)))
        3dmatriz = [self.matriz]
        for x in range(2, len(self.joint)):
            3dmatriz.append(multi)
        
    # Funcion para segunda parte 
    def warshallAlgorithm():
        if self.isValid:
            #matrix = self.matriz[:]
            matrix = [[0,1],
                      [1,0]]
            submatrix = matrix[:]
            for num in range(len(submatrix)):
                submatrix = self.calculateMatrix(submatrix,num+1)
            print(submatrix)

    def calculateMatrix(submatrix,num):
        print("Hola")
