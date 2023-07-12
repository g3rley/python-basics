## Solução da Questão 1

A questão pede para criar uma função chamada `filtrar_planetas` que recebe uma lista de planetas e retorna uma nova lista apenas com os nomes dos planetas que possuem climas variados. Um planeta é considerado de clima variado se tiver mais de uma estação climática mencionada em sua descrição. A função deve ignorar maiúsculas e minúsculas.

Primeiro, vamos definir a função `filtrar_planetas`:

```python
def filtrar_planetas(planetas):
    planetas_filtrados = []
    for planeta in planetas:
        clima_planeta = planeta.split(':')[1].strip().lower()
        if clima_planeta.count(' e ') > 0:
            planetas_filtrados.append(planeta.split(':')[0].strip())
    return planetas_filtrados
```

A função `filtrar_planetas` recebe a lista de planetas como parâmetro. Em seguida, inicializamos uma lista vazia chamada planetas_filtrados para armazenar os nomes dos planetas que possuem climas variados.

Agora, percorremos cada planeta na lista `planetas`. Para cada planeta, dividimos a descrição em duas partes usando `split(':')`. A primeira parte é o nome do planeta e a segunda parte é a descrição do clima. Usamos `strip()` para remover os espaços em branco no início e no final da descrição. Também usamos `lower()` para converter o clima para letras minúsculas, ignorando maiúsculas e minúsculas.

Em seguida, usamos `count(' e ')` para verificar se o clima contém a expressão " e ", indicando a presença de mais de uma estação climática. Se o clima tiver mais de uma estação, adicionamos o nome do planeta à lista `planetas_filtrados` usando `append(planeta.split(':')[0].strip())`.

Por fim, retornamos a lista `planetas_filtrados` com os nomes dos planetas que possuem climas variados.

Agora, vamos testar a função com a lista de planetas fornecida:

```python

planetas = ['Tatooine: Planeta desértico.', 'Naboo: Planeta com climas tropicais e temperados.', 'Hoth: Planeta gelado.', 'Kashyyyk: Planeta com florestas tropicais e temperadas.']
resultado = filtrar_planetas(planetas)
print(resultado)

```

Executando o código acima, obtemos o resultado:

```
['Naboo', 'Kashyyyk']
```

Isso significa que os planetas "Naboo" e "Kashyyyk" possuem climas variados, pois têm mais de uma estação climática mencionada em suas descrições.

A função filtrar_planetas retorna corretamente os nomes dos planetas com climas variados.

Parabéns! Você concluiu a solução da Questão 1.