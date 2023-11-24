# Operadores Aritméticos e Compostos em Python:

Em Python, os operadores aritméticos básicos são os mesmos que em C/C++. Eles incluem adição (+), subtração (-), multiplicação (*), divisão (/), resto da divisão (%) e exponenciação (**).
Operadores compostos, como +=, -=, *=, /=, também existem em Python, funcionando de maneira semelhante ao C/C++. Por exemplo:
```python
x = 5
x += 3  # Isso é equivalente a x = x + 3

```
# Representação de Números Inteiros Grandes em Python:

Em Python, os inteiros não têm um limite fixo de tamanho, como em C/C++. Isso significa que você pode representar números inteiros muito grandes sem se preocupar com estouro. Por exemplo, calcular o fatorial de 30 é fácil em Python:
```python
import math
result = math.factorial(30)
print(result)
```
Comparando isso com o maior valor inteiro que pode ser representado em C/C++ (2^31 - 1 ou 2^63 - 1 em sistemas de 32 ou 64 bits, respectivamente), a diferença é significativa.

# Imutabilidade de Variáveis Numéricas em Python:

Em Python, as variáveis numéricas são imutáveis, o que significa que, ao modificar o valor de uma variável, uma nova instância é criada em vez de modificar diretamente a variável existente. Por exemplo:
```python
x = 10
y = x  # y agora refere-se ao mesmo valor que x
y += 5  # y é atualizado, mas x permanece inalterado
print(x)  # A saída será 10

```

# Métodos Disponíveis para Variáveis Inteiras em Python:

Em Python, os inteiros são objetos, e eles têm métodos associados. Alguns métodos úteis incluem bit_length() para obter o número mínimo de bits necessário para representar o número e __abs__() para obter o valor absoluto. Exemplo:
```python
num = -42
print(num.bit_length())  # Saída: 6 (porque 42 em binário é '101010' e requer 6 bits)
print(abs(num))  # Saída: 42
```
