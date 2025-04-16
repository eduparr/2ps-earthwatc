
import json
from datetime import datetime
import random

def gerar_json_diario():
    frequencias = {
        "7.83 Hz": random.randint(78, 88),
        "14 Hz": random.randint(70, 80),
        "20 Hz": random.randint(72, 82),
        "26 Hz": random.randint(65, 75),
        "32 Hz": random.randint(55, 65),
        "38 Hz": random.randint(78, 90),
        "44 Hz": random.randint(85, 95)
    }

    kp_valores = [random.randint(2, 6) for _ in range(4)]
    kp_atual = kp_valores[-1]

    sismos = [
        {"local": "México", "magnitude": round(random.uniform(4.5, 6.0), 1), "lat": 19.43, "lon": -99.13},
        {"local": "Chile", "magnitude": round(random.uniform(4.5, 5.8), 1), "lat": -33.45, "lon": -70.66},
        {"local": "Indonésia", "magnitude": round(random.uniform(5.0, 6.3), 1), "lat": -6.2, "lon": 106.8}
    ]

    media_frequencia = sum(frequencias.values()) / len(frequencias)
    risco_nivel = 0
    if kp_atual >= 5 or media_frequencia >= 85:
        risco_nivel = 2
    if kp_atual >= 6 and media_frequencia >= 90:
        risco_nivel = 3

    classificacao = ["Baixo", "Moderado", "Elevado"][risco_nivel]
    recomendacoes = {
        0: ["Respiração consciente", "Contato com natureza", "Boa hidratação"],
        1: ["Evitar telas e luzes artificiais", "Pausas ao ar livre", "Apoio sensorial em escolas"],
        2: ["Reduzir estímulos urbanos", "Recolhimento em ambientes naturais", "Alerta em zonas hospitalares"]
    }

    resultado = {
        "data": datetime.utcnow().strftime("%Y-%m-%d"),
        "frequencias_schumann": frequencias,
        "indice_kp": {
            "ultimas_72h": kp_valores,
            "atual": kp_atual
        },
        "eventos_sismicos": sismos,
        "risco_biologico": {
            "nivel": risco_nivel,
            "classificacao": classificacao,
            "recomendacoes": recomendacoes[risco_nivel],
            "base_cientifica": [
                "Geesink & Meijer (2020)",
                "Persinger (1995)",
                "Cherry (2002)"
            ]
        }
    }

    with open("2ps_earthwatch_diario.json", "w") as f:
        json.dump(resultado, f, indent=2)

gerar_json_diario()
