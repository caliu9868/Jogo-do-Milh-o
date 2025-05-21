# Jogo-do-Milhão
JOGO DO MILHÃO - EXPLICAÇÃO COMPLETA DO CÓDIGO E REGRAS

=============================================
INFORMAÇÕES GERAIS
=============================================
Este projeto simula o famoso "Show do Milhão" com 15 perguntas divididas em 3 rodadas:
- Rodada Fácil (1 a 5)
- Rodada Média (6 a 10)
- Rodada Difícil (11 a 15)

Objetivo: acertar todas as perguntas e ganhar 1 MILHÃO de reais fictícios.

---------------------------------------------
COMO FUNCIONA O JOGO
---------------------------------------------
1. O jogador é perguntado se deseja iniciar o jogo.
2. São sorteadas perguntas de arquivos JSON:
   - perguntas_A.json
   - perguntas_B.json
   - perguntas_C.json
   - perguntas_D.json
3. Cada arquivo possui perguntas cuja resposta correta é A, B, C ou D.
4. O jogo embaralha as alternativas e mostra ao jogador.
5. O jogador responde e o código verifica se está correto.
6. Pontuação é acumulada conforme a rodada.
7. Ajuda pode ser usada (pulo, cartas, placas, universitário).
8. O jogo continua até o jogador errar, desistir ou vencer.

=============================================
ESTRUTURA DO CÓDIGO
=============================================

1. iniciar_jogo()
------------------
É a função principal. Controla o fluxo do jogo:
- Chama perguntas em sequência.
- Gerencia pontuação.
- Gerencia rodadas.
- Lê e mostra perguntas sorteadas.
- Controla desistência, ajuda e final de jogo.

2. carregar_perguntas_json(arquivo: str) -> list
--------------------------------------------------
Abre um arquivo JSON e carrega as perguntas disponíveis. Cada pergunta tem:
- "pergunta": Enunciado
- "alternativas": Lista de alternativas
- "correta": Letra correta

3. escolher_arquivo_pergunta() -> str
-------------------------------------
Sorteia um entre os 4 arquivos de pergunta (A, B, C, D) para garantir que a resposta correta da pergunta sorteada será a letra correspondente.

4. sortear_pergunta(arquivo: str) -> dict
-----------------------------------------
Dentro do arquivo sorteado, escolhe uma pergunta aleatória e a retorna.

5. embaralhar_alternativas(alternativas: list) -> list
------------------------------------------------------
Embaralha a ordem das alternativas (A, B, C, D), mas mantém a correta entre elas.

6. mostrar_pergunta(pergunta: dict)
-----------------------------------
Mostra a pergunta e as alternativas na tela.

7. verificar_resposta(resposta: str, correta: str) -> bool
-----------------------------------------------------------
Verifica se a resposta dada pelo jogador é igual à correta.

8. controle_pontuacao(pergunta_num: int) -> int
-----------------------------------------------
Calcula e retorna o valor da pergunta com base no número da rodada e da questão.

9. usar_cartas(alternativas: list, correta: str) -> list
---------------------------------------------------------
Sorteia de 1 a 3 alternativas incorretas para eliminar e mostra ao jogador apenas o que sobra.

10. usar_placas(alternativas: list, correta: str) -> list
----------------------------------------------------------
Mostra duas alternativas: a correta e uma incorreta aleatória.

11. usar_universitario(pergunta: dict) -> str
---------------------------------------------
Mostra uma dica simples sobre a alternativa correta (pré-definida).

=============================================
ARQUIVOS DE PERGUNTAS
=============================================

Os arquivos .json contêm listas de perguntas como este exemplo:

[
  {
    "pergunta": "Qual a capital do Brasil?",
    "alternativas": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
    "correta": "A"
  }
]

- As perguntas em perguntas_A.json têm sempre a letra A como correta.
- O mesmo vale para os outros arquivos.

=============================================
REGRAS DO JOGO
=============================================

Rodada 1 - Fácil (Perguntas 1 a 5)
- Q1, Q2, Q3 = R$ 1.000 cada
- Q4 = R$ 2.000
- Q5 = R$ 5.000
- Acumulado: R$ 10.000

Rodada 2 - Média (Perguntas 6 a 10)
- Q6 a Q9 = R$ 10.000 cada
- Q10 = R$ 50.000
- Acumulado: R$ 100.000

Rodada 3 - Difícil (Perguntas 11 a 15)
- Q11 e Q12 = R$ 50.000
- Q13 = R$ 100.000
- Q14 = R$ 200.000
- Q15 = R$ 500.000
- Acumulado: R$ 1.000.000

=============================================
COMANDOS DISPONÍVEIS DURANTE O JOGO
=============================================
Durante a pergunta, o jogador pode digitar:

- A, B, C ou D → Para responder
- ajuda → Para escolher entre os tipos de ajuda
- parar → Para encerrar o jogo e levar o valor atual

Ajudas possíveis:
- cartas → Elimina alternativas erradas (até 3 vezes)
- pulo → Pula a pergunta (até 3 vezes)
- placas → Mostra 2 alternativas (1 certa, 1 errada) (até 3 vezes)
- universitario → Dá uma dica simples (até 3 vezes)

=============================================
FINALIZAÇÃO DO JOGO
=============================================
- Resposta errada → jogador perde metade do valor acumulado da rodada anterior.
- Desistência → jogador leva o valor acumulado até aquele momento.
- Acerto das 15 perguntas → jogador ganha R$ 1.000.000 fictício.

Boa sorte no seu caminho rumo ao milhão!
