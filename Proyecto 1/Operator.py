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
                
    def matrixOperations(self, matrixres, matrix1 = [], matrix2 = [], multi = True):
        for x in range(len(self.joint if multi else self.matriz3d)):
              for y in range(len(self.joint)):
                  for z in range(len(self.joint)):
                      if multi:
                          matrixres[x][y] = matrixres[x][y] or (matrix1[x][z] and matrix2[z][y])
                      else:
                          matrixres[y][z] = matrixres[y][z] or self.matriz3d[x][y][z]          
        return matrixres
        
    # Funcion para las operaciones de matrices
    def boolOperations(self,matrixres, pot = 0, multi = True):
        return self.matrixOperations(matrixres,multi=False) if not multi else self.matriz if pot == 1 else self.matrixOperations(matrixres, self.matriz, self.matriz) if pot == 2 else self.matrixOperations(matrixres, self.boolOperations(matrixres, pot-1), self.matriz)  


    # Funcion para primer parte
    def closedTransitiveRel(self):
        matrixres = list(list(False for x in range(len(self.joint))) for y in range(len(self.joint)))
        self.matriz = list(list(1 if (y+1,x+1) in self.relation else 0 for x in range(len(self.joint))) for y in range(len(self.joint)))    
        self.matriz3d = list(self.boolOperations(matrixres, x + 1) for x in range(len(self.joint)))
        return self.boolOperations(matrixres, multi=False)
        
    # Funcion para segunda parte 
    def warshallAlgorithm(self):
        if self.isValid:
            #matrix = self.matriz[:]
            matrix = [[0,1],
                      [1,0]]
            submatrix = matrix[:]
            for num in range(len(submatrix)):
                submatrix = self.calculateMatrix(submatrix,num+1)
            self.printMatrix(submatrix)
            

    # Funcion para mostrar matrices
    def printMatrix(self,submatrix):
        print(submatrix)
        mLength = len(submatrix)
        for elem in submatrix:
            for x in range(mLength):
                print("| " + str(elem[x]),end=' ')
            print('|')

    def calculateMatrix(self,submatrix,num):
        row = submatrix[num - 1]
        column = []
        for m in submatrix:
            column.append(m[num - 1])
        nMatrix = []
        for x in range(len(submatrix)):
            if x == num - 1:
                nMatrix.append(row)
            else:
                nRow = []
                numRow = submatrix[num - 1]
                for y in range(len(submatrix)):
                    if y == num - 1:
                        nRow.append(column[x])
                    else:
                        numa = numRow[y]
                        numb = column[x]
                        if numa == 1 and numb == 1:
                            nRow.append(1)
                        else:
                            nRow.append(0)
                nMatrix.append(nRow)
        return nMatrix
