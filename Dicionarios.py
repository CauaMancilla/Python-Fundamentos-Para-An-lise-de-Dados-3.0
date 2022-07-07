#***DICIONÁRIOS***       (é criado com chaves)
"""
estudantes_list = ["Mateus", 24, "Fernanda", 22, "Tamires", 26,"Cristiano", 25]
print(estudantes_list)
#dicionario:
estudantes_dict = {"Mateus":24, "Fernanda":22, "Tamires":26,"Cristiano":25}
print(estudantes_dict["Mateus"])
estudantes_dict["Pedro"] = 23       #Criou outro item altomaticamente para o icionario
print(estudantes_dict["Pedro"])
print(estudantes_dict)
print(estudantes_dict["Tamires"])
estudantes_dict.clear()     #Limpou todas as informaçoes do dicionario
print(estudantes_dict)
del estudantes_dict     #Deletou o Dicionario
print(estudantes_dict)
"""
"""
#funções no dicionario:
estudantes = {"Mateus":24, "Fernanda":22, "Tamires":26,"Cristiano":25}
print(estudantes)
print(len(estudantes))      #Vai contar as combinaçoes como se fosse um só
print(estudantes.keys())        #Extrair somente as chaves do Dicionario
print(estudantes.values())      #Extrair apenas os valores das chaves
print(estudantes.items())       #Vai retornar todos os items do Dicionario
print()
print()
estudantes2 = {"Maria":27, "Erika":28, "Milton":26}
print(estudantes2)
estudantes.update(estudantes2)      #É como se tivesse feito uma concatenação (Juntou os valores)
print(estudantes)
#Pode criar um dicionario vazio e ir adicionando valores.
dict1 = {}
dict1["key_one"] = 2
print(dict1)
dict1[10] = 5
print(dict1)
dict1[8.2] = "Python"
print(dict1)
dict1["teste"] = 5
print(dict1)
print()
print()
dict1 = {}
print(dict1)
dict1["teste"] = 10
dict1["key"] = "teste"
print(dict1)
print()
print()
dict2 = {}
dict2["key1"] = "Big Data"
dict2["key2"] = 10
dict2["key3"] = 5.6
print(dict2)
#Extrair o valor de cada chave e atribuir a uma variavel
a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]
print(a,b,c)
print()
print()

#Diconario de listas:
dict3 = {"key1":1230,"key2":[22,453,73.4], "key3":["leite","maça","batata"]}
print(dict3)
print(dict3["key2"])
#Selecionar um elemento, dentro da lista, dentro da chave e deichar tudo maiusculo:
print(dict3["key3"][0].upper())
#Extrair um elemento, dentro de uma lista, dentro de um valor no dicionario e fazer operações:
var1 = dict3['key2'][0] - 2
print(var1)
#Se usar o "-=" da para fazer a operação e subistituir o valor
dict3["key2"][0] -= 2
print(dict3)
print()
print()
#DICIONARIOS ANINHADOS:
#***dicionario dentro de outro dicionario***
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhada em python'}}}
print(dict_aninhado)
print(dict_aninhado['key1']['key2_aninhada']['key3_aninhada'])
"""