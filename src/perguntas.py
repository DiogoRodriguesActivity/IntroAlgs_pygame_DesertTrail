import json
from pathlib import Path


CAMINHO_PERGUNTAS = Path(__file__).with_name("perguntas.json")


def _carregar_perguntas():
    """Carrega e valida o banco de perguntas separado por fase."""
    with CAMINHO_PERGUNTAS.open(encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    perguntas_por_fase = {}
    for fase in (1, 2, 3):
        perguntas = dados.get(str(fase), [])
        if not perguntas:
            raise ValueError(f"Nao ha perguntas cadastradas para a fase {fase}.")

        for indice, pergunta in enumerate(perguntas, start=1):
            campos = {"pergunta", "opcoes", "resposta_correta"}
            if not campos.issubset(pergunta):
                raise ValueError(f"Pergunta {indice} da fase {fase} esta incompleta.")
            if len(pergunta["opcoes"]) != 4:
                raise ValueError(f"Pergunta {indice} da fase {fase} precisa de 4 opcoes.")
            if pergunta["resposta_correta"] not in ("a", "b", "c", "d"):
                raise ValueError(f"Resposta invalida na pergunta {indice} da fase {fase}.")

        perguntas_por_fase[fase] = perguntas

    return perguntas_por_fase


PERGUNTAS_POR_FASE = _carregar_perguntas()

# Mantem compatibilidade com qualquer modulo que ainda importe a lista completa.
PERGUNTAS = [
    pergunta
    for perguntas_da_fase in PERGUNTAS_POR_FASE.values()
    for pergunta in perguntas_da_fase
]
