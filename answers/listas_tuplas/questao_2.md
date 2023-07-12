## Solução da Questão 2

A questão pede para criar uma função chamada `verificar_naves` que recebe uma lista de tuplas, onde cada tupla representa uma nave espacial e contém o nome da nave e sua quantidade de unidades disponíveis. A função deve retornar uma nova lista apenas com os nomes das naves que possuem mais de 3 unidades disponíveis.

Primeiro, vamos definir a função `verificar_naves`:

```python
def verificar_naves(naves):
    naves_disponiveis = []
    for nave in naves:
        if nave[1] > 3:
            naves_disponiveis.append(nave[0])
    return naves_disponiveis

```

A função verificar_naves recebe a lista de naves como parâmetro. Em seguida, inicializamos uma lista vazia chamada naves_disponiveis para armazenar os nomes das naves que possuem mais de 3 unidades disponíveis.

Agora, percorremos cada nave na lista naves. Para cada nave, verificamos se a quantidade de unidades disponíveis (segundo elemento da tupla) é maior que 3. Se for, adicionamos o nome da nave (primeiro elemento da tupla) à lista naves_disponiveis usando append(nave[0]).

Por fim, retornamos a lista naves_disponiveis com os nomes das naves que possuem mais de 3 unidades disponíveis.

Agora, vamos testar a função com a lista de naves fornecida:

```python

naves = [('Millennium Falcon', 2), ('X-Wing', 5), ('Y-Wing', 3), ('Star Destroyer', 6)]
resultado = verificar_naves(naves)
print(resultado)

```

Executando o código, temos o seguinte resultado:

```python

['X-Wing', 'Star Destroyer']

```

Isso significa que as naves "X-Wing" e "Star Destroyer" possuem mais de 3 unidades disponíveis.

A função verificar_naves retorna corretamente os nomes das naves com mais de 3 unidades disponíveis.

Parabéns! Você concluiu a solução da Questão 2.