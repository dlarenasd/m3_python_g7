import sys
""" 
a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.0013

"""

conversiones={
"sol_peruano": float(sys.argv[1]),
"peso_argentino" : float(sys.argv[2]),
"dolar_americano" : float(sys.argv[3]),
"peso_chileno" : int(sys.argv[4]),
}

print(f"Los {conversiones["peso_chileno"]} pesos equivalen a:") 
print(f"{conversiones["sol_peruano"] * conversiones["peso_chileno"]} Soles")
print(f"{conversiones["peso_argentino"] * conversiones['peso_chileno']} Pesos Argentinos") 
print(f"{conversiones["dolar_americano"] * conversiones['peso_chileno']} Dólares Americanos")