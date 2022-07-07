#É basicamente um objeto proprio para garantir integridade dos dados

tupla1 = ("Geografia1",23,"Elefante")
print(tupla1)
print(tupla1[0])
print(tupla1[1:])
print(tupla1.index("Elefante"))
del tupla1

t2 = ('A','B','C')
print(t2)
#para auterar um item dentro da tupla, tem q converter para uma lista
lista_t2 = list(t2)
print(lista_t2)
lista_t2.append('D')
#Depois é so converter para tupla dnv
t2 = tuple(lista_t2)
print(t2)

