# Python Basics

<p align="center">
  <img src="./img/main.jpg" width="411">
</p>
<p align="center"><i>Um Jedi usa a Força para o conhecimento e defesa, nunca para o ataque.”</i></p>
<p align="center"><i>- Mestre Yoda -</i></p>

Tendo como base a disciplina "Lógica de Programação II (PY)" do Santander Coders, este repositório tem como objetivo reunir exercícios essenciais de python para iniciantes. 

## 📚 Sumário

- [Listas](#listas)
- [Tuplas](#tuplas)
- [Dicionários](#dicionários)
- [Sobre os exercícios](#sobre-os-exercícios)
- [Contribuição](#contribuição)
- [Referências](#referências)
- [Licença](#licença)

## 📝 Listas

Listas são coleções de itens em uma ordem em particular. Você pode criar uma lista que inclua as letras do alfabeto, os dígitos de 0 a 9 ou os nomes de todas as pessoas em sua família. Você pode colocar qualquer informação que quiser em uma lista e acessar os itens individuais por meio de uma indexação.

### 📌 Sintaxe

```python

# Criando uma lista
lista = ['item1', 'item2', 'item3']

# Acessando um item da lista
print(lista[0]) # item1

# Acessando o último item da lista
print(lista[-1]) # item3

# Percorrendo uma lista

for item in lista:
    print(item)

# Adicionando um item na lista
lista.append('item4')

# Inserindo um item na lista
lista.insert(0, 'item0')

# Removendo um item da lista
del lista[0]

# Removendo um item da lista e armazenando em uma variável
item = lista.pop(0)

# Removendo um item da lista pelo valor
lista.remove('item1')

# Ordenando uma lista
lista.sort()

# Ordenando uma lista em ordem decrescente
lista.sort(reverse=True)

```

## 📝 Tuplas

Uma tupla é uma coleção de itens que não pode mudar durante a execução do seu programa. A principal diferença entre listas e tuplas é que as tuplas não podem ser modificadas, enquanto as listas podem.

### 📌 Sintaxe

```python

# Criando uma tupla
tupla = ('item1', 'item2', 'item3')

# Acessando um item da tupla
print(tupla[0]) # item1

# Acessando o último item da tupla
print(tupla[-1]) # item3

# Percorrendo uma tupla

for item in tupla:
    print(item)

```

## 📝 Dicionários

Um dicionário em Python é uma coleção de pares chave-valor. Cada chave é conectada a um valor e você pode usar uma chave para acessar o valor associado a ela. Um valor pode ser qualquer objeto Python, como uma string, lista ou até mesmo outro dicionário. Em Python, um dicionário é colocado entre chaves, {}.

### 📌 Sintaxe

```python

# Criando um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

# Acessando um valor do dicionário
print(dicionario['chave1']) # valor1

# Percorrendo um dicionário

for chave, valor in dicionario.items():
    print(chave, valor)

# Adicionando um item no dicionário
dicionario['chave4'] = 'valor4'

# Removendo um item do dicionário
del dicionario['chave4']

# Ordenando um dicionário
dicionario = sorted(dicionario.items(), key=lambda x: x[1])

```

## Sobre os exercícios

Os exercícios são contextualizados com o universo Star Wars, onde você é um Padawan e precisa passar por alguns desafios para se tornar um Jedi. 

As questões estão localizadas no diretório [exercises](./exercises) e as respostas no diretório [answers](./answers). 

## 📝 Contribuição

Contribuições são sempre bem-vindas! Por favor, leia o [guia de contribuição](./CONTRIBUTING.md) para obter mais detalhes sobre como você pode contribuir para este projeto.


## 📚 Referências

- [Python.org](https://www.python.org/)
- [Python Brasil](https://python.org.br/)

## 📝 Licença

Distribuído sob a licença BSD-2. Veja `LICENSE` para mais informações.