"""
listaTeste = ["bala", "cola", "dolar"]
print(listaTeste)
listaTeste[2] = "suco"  #subistitur item da lista
print(listaTeste)
del listaTeste[2]   #deletar item da lista
print(listaTeste)
"""
"""
#LIISTAS ANINHADAS
ListaAninhada = [[1,2,3],[10,15,14], [10.1,8.7,2.3]]
print(ListaAninhada)
a = ListaAninhada[0]   #Mostrar somente um item da lista
print(a)
b = a[0]   #Mostrar somente um item da variavel 'a'
print(b)
#Fatiamento:
list1 = ListaAninhada[1]
print(list1)
valor_1_0 = list1[0]
valor_1_2 = list1[2]
print(valor_1_0)
print(valor_1_2)

list2 = ListaAninhada[2]
print(list2)
valor_2_0 = list2[0]
print(valor_2_0)
"""
"""
#Operaçoes com listas
OperaLista = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print(OperaLista)
a = OperaLista[0][0]  #selecionar valores dentro da lista
print(a)
b = OperaLista[1][2]  #selecionar valores dentro da lista
print(b)
c = OperaLista[0][2] + 10   #selecionar valores dentro da lista e somar
print(c)
d = 10
e = d * OperaLista[2][0]   #Pegando valor de variavel para multiplicar pelos valores da lista
print(e)
"""
"""
#Concatenando Listas
lista_s1 = [34, 32, 56]
lista_s2 = [21, 90, 51]
lista_total = lista_s2 + lista_s1   #Somando as listas
print(lista_total)
"""
"""
#Operador in   *BASICAMENTE PESQUISA SE TEM TAL ELEMENTO PROCUTADO*
lista_teste_op = [100, 2, -5, 3.4]
#print(10 in lista_teste_op)
#print(100 in lista_teste_op)

#Funções Built-in
print(len(lista_teste_op))  #Conta quantos elementos tem na lista
print(max(lista_teste_op))  #Retorna o MAIOR valor da lista
print(min(lista_teste_op))  #Retorna o MENOR valor da lista
"""
"""
#Adicionar um item à lista
listaMercado2 = ["ovos", "farinha", "leite", "maças"]
print(listaMercado2)
listaMercado2.append("carne")   #Adiciona o item na lista
print(listaMercado2)
listaMercado2.append("carne")   #Pode adicionar o mesmo elemento varias vezes
print(listaMercado2)
print(listaMercado2.count("carne")) #Conta quantas vezes o elemento se repete
"""

#****PODE CRIAR LISTA VAZIA*****
a = []
print(a)
print(type(a))
a.append(10)    #adicionando valores
print(a)
a.append(50)    #adicionando valores
print(a)
#Atribuindo os valores da lista com item a lista vazia
old_list = [1,2,5,10]
new_list = []
for item in old_list:
    new_list.append(item)
print(new_list)

"""
#Extend / Index / Remove
cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])     #Inserir mais de um valor na lista
print(cidades)

print(cidades.index("Salvador"))    #Saber o numero do item na lista

cidades.insert(2, 110)      #Inserir valor na posição desejada na lista
print(cidades)

cidades.remove(110) #Remover um item da lista
print(cidades)

cidades.reverse()       #Inverter a ordem da lista
print(cidades)

cidades.sort()
print(cidades)

#Ordenar a lista (Ordem alfabetica ou Numerica)
cidades.sort()
print(cidades) 

x = [3,4,2,1]
print(x)
x.sort()
print(x)
"""