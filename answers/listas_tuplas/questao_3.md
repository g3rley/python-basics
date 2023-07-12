## Solução da Questão 3

A questão pede para criar uma função chamada `dobrar_numeros` que recebe uma lista de números inteiros e retorna uma nova lista contendo o dobro de cada número.

Primeiro, vamos definir a função `dobrar_numeros`:

```python
def dobrar_numeros(numeros):
    numeros_dobrados = [numero * 2 for numero in numeros]
    return numeros_dobrados

```

A função `dobrar_numeros` recebe a lista de números como parâmetro. Em seguida, usamos uma *list comprehension* para criar uma nova lista chamada `numeros_dobrados` contendo o dobro de cada número da lista `numeros`.

Por fim, retornamos a lista `numeros_dobrados` com o dobro de cada número.

Agora, vamos testar a função com a lista de números fornecida:

```python
numeros = [2, 3, 4, 5]
resultado = dobrar_numeros(numeros)
print(resultado)
  
```

Executando o código acima, obtemos o resultado:

```
[4, 6, 8, 10]

```

Isso significa que os números 2, 3, 4 e 5 foram dobrados corretamente.

A função `dobrar_numeros` retorna corretamente o dobro de cada número.

Parabéns! Você concluiu a solução da Questão 3.