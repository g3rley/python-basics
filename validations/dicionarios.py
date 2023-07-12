def verificar_resposta_1(resultado):
    resultado_esperado = {
        'nome': 'Tatooine',
        'clima': 'Árido',
        'terreno': 'Deserto'
    }
    if resultado == resultado_esperado:
        print("Sua resposta está correta!")
    else:
        print("Sua resposta está incorreta.")

def verificar_resposta_2(resultado):
    resultado_esperado = {
        'Millennium Falcon': 4,
        'X-Wing': 1,
        'Star Destroyer': 1000
    }
    if resultado == resultado_esperado:
        print("Sua resposta está correta!")
    else:
        print("Sua resposta está incorreta.")

def verificar_resposta_3(resultado):
    resultado_esperado = {
        'localização': 'Desconhecida',
        'tamanho': 'Grande',
        'defesas': 'Escudos de energia'
    }
    if resultado == resultado_esperado:
        print("Sua resposta está correta!")
    else:
        print("Sua resposta está incorreta.")
