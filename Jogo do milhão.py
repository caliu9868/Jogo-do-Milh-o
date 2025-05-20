
import json
import random

def carregar_perguntas(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def escolher_arquivo():
    arquivos = {
        "A": "perguntas_A.json",
        "B": "perguntas_B.json",
        "C": "perguntas_C.json",
        "D": "perguntas_D.json"
    }
    letra = random.choice(list(arquivos.keys()))
    return arquivos[letra], letra

def escolher_pergunta(lista):
    return random.choice(lista)

def eliminar_alternativa_incorreta(pergunta):
    incorretas = [alt for alt in pergunta["alternativas"] if not alt.startswith(pergunta["resposta_correta"])]
    eliminada = random.choice(incorretas)
    novas_alternativas = [alt for alt in pergunta["alternativas"] if alt != eliminada]
    return novas_alternativas, eliminada

def mostrar_pergunta(pergunta):
    usou_dica = False
    alternativas = pergunta["alternativas"]

    while True:
        print("\nPergunta:")
        print(pergunta["pergunta"])
        for alt in alternativas:
            print(alt)

        print("\nDigite A, B, C ou D para responder.")
        print("Digite DICA para eliminar uma alternativa incorreta.")
        print("Digite PARAR para encerrar o jogo.")
        resposta = input("Sua escolha: ").strip().upper()

        if resposta == "PARAR":
            return "PARAR"
        elif resposta == "DICA":
            if usou_dica:
                print("Você já usou a dica nessa pergunta.")
            else:
                alternativas, eliminada = eliminar_alternativa_incorreta(pergunta)
                print(f"Dica: a alternativa '{eliminada}' foi eliminada.")
                usou_dica = True
        elif resposta in ["A", "B", "C", "D"]:
            return resposta == pergunta["resposta_correta"]
        else:
            print("Opção inválida. Tente novamente.")

def iniciar_jogo():
    print("Bem-vindo ao Jogo do Milhão!")
    iniciar = input("Deseja iniciar o jogo? (S/N): ").strip().upper()

    if iniciar != 'S':
        print("Tudo bem! Até a próxima.")
        return

    pontos = 0
    while True:
        arquivo, letra_certa = escolher_arquivo()
        perguntas = carregar_perguntas(arquivo)
        pergunta = escolher_pergunta(perguntas)

        resultado = mostrar_pergunta(pergunta)

        if resultado == "PARAR":
            print("Você escolheu parar o jogo.")
            break
        elif resultado:
            print("Parabéns! Você acertou.")
            pontos += 1
        else:
            print(f"Que pena! A resposta correta era: {pergunta['resposta_correta']}")
            break

    print(f"\nFim de jogo! Você acertou {pontos} pergunta(s).")

# Iniciar o jogo
iniciar_jogo()