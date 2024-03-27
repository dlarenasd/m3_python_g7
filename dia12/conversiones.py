import sys
""" 
a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.0013

"""


soles_peruanos = float(sys.argv[1])
pesos_argentinos = float(sys.argv[2])
dolares_americanos = float(sys.argv[3])
pesos_chilenos = float(sys.argv[4])

print(f"Los {pesos_chilenos} pesos equivalen a:") 
print(f"{soles_peruanos * pesos_chilenos} Soles")
print(f"{pesos_argentinos * pesos_chilenos} Pesos Argentinos") 
print(f"{dolares_americanos * pesos_chilenos} Dólares Americanos")