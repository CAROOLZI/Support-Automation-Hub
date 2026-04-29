import pandas as pd

def classificar_prioridade(texto):
    urgentes = ['erro', 'crítico', 'pagamento', 'urgente', 'parado']
    if any(palavra in texto.lower() for palavra in urgentes):
        return 'ALTA 🔴'
    return 'NORMAL 🟢'

# Simulação de chamados
chamados = [
    "Dúvida sobre o horário de entrega",
    "Erro crítico no sistema de login",
    "Preciso de ajuda com o pagamento"
]

print("--- Classificador Inteligente de Chamados ---")
for msg in chamados:
    prioridade = classificar_prioridade(msg)
    print(f"Chamado: '{msg}' | Prioridade: {prioridade}")
