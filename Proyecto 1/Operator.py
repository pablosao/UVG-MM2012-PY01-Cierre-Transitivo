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

    # Funcion para segunda parte 
