def verificar_resposta_1(resultado):
    resposta_esperada = ['Naboo', 'Kashyyyk']
    assert resultado == resposta_esperada, 'Sua resposta está incorreta.'
    print('Sua resposta está correta!')

def verificar_resposta_2(resultado):
    resposta_esperada = ['X-Wing', 'Star Destroyer']
    assert resultado == resposta_esperada, 'Sua resposta está incorreta.'
    print('Sua resposta está correta!')

def verificar_resposta_3(resultado):
    resposta_esperada = [4, 6, 8, 10]
    assert resultado == resposta_esperada, 'Sua resposta está incorreta.'
    print('Sua resposta está correta!')

def verificar_resposta_4(resposta_usuario):
    resposta_esperada = [('Chewbacca', 'Copiloto'), ('Han Solo', 'Piloto'), ('Leia Organa', 'Comandante'), ('Luke Skywalker', 'Jedi')]    
    if resposta_usuario == resposta_esperada:
        print("Parabéns! Sua resposta está correta.")
    else:
        print("Ops! Sua resposta está incorreta. Tente novamente.")

