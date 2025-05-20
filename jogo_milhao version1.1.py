
import json
import random

ajudas = {
    "pulo": 3,
    "cartas": 3,
    "placas": 3,
    "universitario": 3
}

valores = {
    1: 1000, 2: 1000, 3: 1000,
    4: 2000, 5: 5000,
    6: 10000, 7: 10000, 8: 10000, 9: 10000,
    10: 50000,
    11: 50000, 12: 50000,
    13: 100000, 14: 200000, 15: 500000
}

def escolher_arquivo_resposta():
    arquivos = {
        "A": "perguntas_A.json",
        "B": "perguntas_B.json",
        "C": "perguntas_C.json",
        "D": "perguntas_D.json"
    }
    letra = random.choice(list(arquivos.keys()))
    return arquivos[letra], letra

def carregar_pergunta():
    arquivo, resposta_certa = escolher_arquivo_resposta()
    with open(arquivo, 'r', encoding='utf-8') as f:
        perguntas = json.load(f)
    pergunta = random.choice(perguntas)
    pergunta['resposta_correta'] = resposta_certa
    return pergunta

def controle_pontuacao(num):
    return valores.get(num, 0)

def embaralhar_alternativas(pergunta):
    alternativas = pergunta['alternativas'].copy()
    random.shuffle(alternativas)
    return alternativas

def usar_cartas(alternativas, correta):
    incorretas = [a for a in alternativas if not a.startswith(correta)]
    qnt = random.randint(1, min(3, len(incorretas)))
    eliminar = random.sample(incorretas, qnt)
    novas = [a for a in alternativas if a not in eliminar]
    return novas

def usar_placas(alternativas, correta):
    incorretas = [a for a in alternativas if not a.startswith(correta)]
    escolhida = random.choice(incorretas)
    opcoes = [a for a in alternativas if a.startswith(correta) or a.startswith(escolhida)]
    random.shuffle(opcoes)
    return opcoes

def usar_universitario(pergunta):
    return f"Dica: Pensa com carinho na alternativa '{pergunta['resposta_correta']}'..."

def mostrar_ajudas():
    print("\nAjudas disponíveis:")
    for k, v in ajudas.items():
        print(f"- {k.capitalize()}: {v} uso(s)")

def mostrar_pergunta(pergunta, numero):
    print(f"\nPergunta {numero}: {pergunta['pergunta']}")
    alternativas = embaralhar_alternativas(pergunta)
    correta = pergunta["resposta_correta"]

    while True:
        for alt in alternativas:
            print(alt)
        mostrar_ajudas()
        print("Digite a letra da resposta (A/B/C/D), ou uma ajuda: pulo, cartas, placas, universitario, ou 'parar'.")

        escolha = input("Sua escolha: ").strip().lower()

        if escolha == "parar":
            return "parar"
        elif escolha == "pulo" and ajudas["pulo"] > 0:
            ajudas["pulo"] -= 1
            return "pulo"
        elif escolha == "cartas" and ajudas["cartas"] > 0:
            ajudas["cartas"] -= 1
            alternativas = usar_cartas(alternativas, correta)
        elif escolha == "placas" and ajudas["placas"] > 0:
            ajudas["placas"] -= 1
            alternativas = usar_placas(alternativas, correta)
        elif escolha == "universitario" and ajudas["universitario"] > 0:
            ajudas["universitario"] -= 1
            print(usar_universitario(pergunta))
        elif escolha.upper() in ["A", "B", "C", "D"]:
            return escolha.upper()
        else:
            print("Opção inválida ou ajuda indisponível.")

def verificar_resposta(resposta, correta):
    return resposta == correta

def iniciar_jogo():
    print("Bem-vindo ao Jogo do Milhão!")
    acumulado = 0
    rodada_anterior = 0

    for i in range(15):
        numero = i + 1
        pergunta = carregar_pergunta()
        valor = controle_pontuacao(numero)

        resposta = mostrar_pergunta(pergunta, numero)

        if resposta == "parar":
            print(f"\nVocê parou o jogo e levou R$ {acumulado:,.2f}")
            break
        elif resposta == "pulo":
            print("Você pulou a pergunta.")
            continue
        elif verificar_resposta(resposta, pergunta["resposta_correta"]):
            acumulado += valor
            rodada_anterior = acumulado
            print(f"Correto! Você ganhou R$ {valor:,.2f}. Total acumulado: R$ {acumulado:,.2f}")
        else:
            print(f"Resposta incorreta. A resposta certa era '{pergunta['resposta_correta']}'.")
            if numero == 1:
                acumulado = 0
            else:
                acumulado = rodada_anterior // 2
            print(f"Você perdeu! Prêmio final: R$ {acumulado:,.2f}")
            break
    else:
        print("\nParabéns! Você venceu o Jogo do Milhão e ganhou R$ 1.000.000!")

iniciar_jogo()
