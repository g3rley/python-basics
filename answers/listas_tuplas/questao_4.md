## Solução da Questão 4

A questão pede para criar uma função chamada `ordenar_tripulacao` que recebe uma lista de tuplas, onde cada tupla representa um membro da tripulação e contém o nome e a função do membro. A função deve retornar uma nova lista de tuplas ordenadas em ordem alfabética pelo nome dos membros.

Primeiro, vamos definir a função `ordenar_tripulacao`:

```python
def ordenar_tripulacao(tripulacao):
    tripulacao_ordenada = sorted(tripulacao, key=lambda x: x[0])
    return tripulacao_ordenada

```

A função `ordenar_tripulacao` recebe a lista de tuplas como parâmetro. Em seguida, usamos a função `sorted` para ordenar a lista `tripulacao` em ordem alfabética pelo nome dos membros. A função `sorted` recebe dois parâmetros: a lista a ser ordenada e uma função `key` que especifica o critério de ordenação. Neste caso, usamos uma função `lambda` para especificar que o critério de ordenação é o primeiro elemento de cada tupla, que é o nome do membro.

Por fim, retornamos a lista `tripulacao_ordenada` com os membros ordenados em ordem alfabética pelo nome.

Agora, vamos testar a função com a lista de tuplas fornecida:

```python
tripulacao = [('Han Solo', 'Piloto'), ('Chewbacca', 'Copiloto'), ('Leia Organa', 'Comandante'), ('Luke Skywalker', 'Jedi')]
resultado = ordenar_tripulacao(tripulacao)
print(resultado)

```

Executando o código acima, obtemos o resultado:

```
[('Chewbacca', 'Copiloto'), ('Han Solo', 'Piloto'), ('Leia Organa', 'Comandante'), ('Luke Skywalker', 'Jedi')]

```

Isso significa que os membros da tripulação foram ordenados corretamente em ordem alfabética pelo nome.

A função `ordenar_tripulacao` retorna corretamente os membros da tripulação ordenados em ordem alfabética pelo nome.

Parabéns! Você concluiu a solução da Questão 4.