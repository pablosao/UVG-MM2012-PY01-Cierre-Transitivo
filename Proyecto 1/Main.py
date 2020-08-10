# LOGICA MATEMATICA PROYECTO 1
# INTEGRANTES:
# - 18332, ANDRE SEBASTIAN RODRIGUEZ OVALLE
# - 11530, PABLO ANDRES SAO ALONZO
# - 18099, JAVIER ALEJANDRO RAMIREZ COSPIN 

from Operator import *

# DEFINIR JOINT (CONJUNTO)
joint = (1,2,3,4)
# DEFINIR RELATION (RELACION)
relation = [(1,3),(1,4),(2,1),(3,2)]

ops = Operator(joint,relation)

print("Opcion 1")
print(ops.closedTransitiveRel())
print("\nWarshall")
ops.warshallAlgorithm()
# PARTE 1
# PARTE 2
