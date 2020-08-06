import os
import time
path = 'dataBase.txt'
f = open("cpu_bound_data.txt", "a")
def fatores_primos(numero):
    start = time.time()
    fator = 2
    lista_multiplicidade_fator = []
    
    while numero > 1:
        mult = 0
        while (numero%fator) == 0:
            mult += 1
            numero = numero//fator
        if mult != 0:
            lista_multiplicidade_fator.append((mult,fator))
        fator += 1
    
    end = time.time()
    f.write('{:10f} '.format(end - start))
    
    return lista_multiplicidade_fator

def printa_tabela(valor):
    lista_multiplicidade_fator = fatores_primos(valor)
    print("/-------------------------------------------------------------------------------\\")
    print("|\t\tTabela de multiplicidade para o numero  %-15d \t|"%valor)
    print("|-------------------------------------------------------------------------------|")
    print("|\t      Fator\t\t\t|\t\tMultiplicidade\t\t|")
    for multiplicidade,fator in lista_multiplicidade_fator:
        print("|-------------------------------------------------------------------------------|")
        print("|\t\t%-15d\t\t|\t\t%-15d\t\t|"%(fator,multiplicidade))
        
    print("\\-------------------------------------------------------------------------------/")


path = 'dataBase.txt'    
confirm_path = 'confirmation.txt'
try:
	while True:
		start = time.time()
		if os.path.isfile(confirm_path):
			with open(path,'r') as reader:
				for line in reader.readlines():
					printa_tabela(int(line))
			os.remove(path)
			os.remove(confirm_path)
			end = time.time()
	
		else:
			end = time.time()
		    
except KeyboardInterrupt:
	f.close()

