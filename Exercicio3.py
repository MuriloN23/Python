#Exercício 3: Manipulação de variáveis de tipo string e explorando o uso de print.


# Imprime cada caractere numérico e seu código numérico
print("Imprimindo caracteres numéricos e seus códigos:")
for i in range(10):
    print(f"'{chr(ord('0') + i)}' - {ord(chr(ord('0') + i))}")

# Modifica a saída para incluir códigos numéricos em octal e hexadecimal
print("\nImprimindo caracteres numéricos e seus códigos em octal e hexadecimal:")
for i in range(10):
    print(f"'{chr(ord('0') + i)}' - Decimal: {ord(chr(ord('0') + i))}, Octal: {oct(ord(chr(ord('0') + i)))}, Hexadecimal: {hex(ord(chr(ord('0') + i)))}")

# Lê um caractere da entrada padrão e imprime no mesmo formato
user_char = input("\nDigite um caractere: ")
print(f"'{user_char}' - Decimal: {ord(user_char)}, Octal: {oct(ord(user_char))}, Hexadecimal: {hex(ord(user_char))}")

# Demonstra o uso de caracteres especiais
special_char = 'ç'
print(f"\nExemplo de caractere especial '{special_char}': Decimal: {ord(special_char)}, Octal: {oct(ord(special_char))}, Hexadecimal: {hex(ord(special_char))}")

special_char = 'ã'
print(f"Exemplo de caractere especial '{special_char}': Decimal: {ord(special_char)}, Octal: {oct(ord(special_char))}, Hexadecimal: {hex(ord(special_char))}")
