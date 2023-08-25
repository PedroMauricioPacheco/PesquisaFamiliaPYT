salario = [] * 20
numfilho = [] * 20
def funcao1():
  salario.append(int(input("Valor do salario: ")))
  numfilho.append(int(input("Número de filhos: ")))

def funcao2():
  print(sum(salario)/len(salario))

def funcao3():
  print(max(salario))

def funcao4(salario):
  i = 0
  for j in range(len(salario)):
    if salario[j] <500:
      i+=1
  print(i / len(salario)*100)
for i in range(20):
  funcao1()
funcao2()
funcao3()
funcao4(salario)
  