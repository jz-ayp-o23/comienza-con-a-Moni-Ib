"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
CONSTANTE = "AÁ"

# Entradas
entrada = input("Escribe una palabra: ")

# Proceso
entrada = entrada.upper()
if entrada[0] in CONSTANTE:
    print(f"'{entrada}' comienza con '{CONSTANTE}'")
else:
    print(f"'{entrada}' no comienza con 'A'")

