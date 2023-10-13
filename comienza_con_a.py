"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
CONSTANTE = "A"
CONSTANTE_2 = "Á"

# Entradas
entrada = input("Escribe una palabra: ")

# Proceso
entrada = entrada.upper()
if entrada[0] in CONSTANTE:
    print(f"'{entrada}' comienza con '{CONSTANTE}'")
elif entrada[0] in CONSTANTE_2:
    print(f"'{entrada}' comienza con '{CONSTANTE_2}'")
else:
     print(f"'{entrada}' no comienza con 'A'")

