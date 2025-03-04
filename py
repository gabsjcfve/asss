import requests
import json

def perguntar_gemini(pergunta):
    api_key = "AIzaSyBzwbCvx_LMKbGu3OiVmJzveXmW25Hfuk0"
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    
    # Contexto com todas as informações dos benefícios da empresa
    contexto = """
    Você é um assistente virtual especializado em responder dúvidas sobre os benefícios da empresa. Aqui estão as informações principais:
    
    - Home Office: 3 dias presenciais e 2 dias remotos (mediante aprovação do gestor).
    - Plano Médico: Diferentes categorias com coparticipação para dependentes, reembolsos variáveis e isenção de coparticipação para internações.
    - Plano Odontológico: Opções Básico e Clássico, sem coparticipação.
    - Vale Transporte: Desconto de 6% no salário, incompatível com estacionamento.
    - Vale Alimentação: R$ 176,00 mensais sem desconto em folha.
    - Refeições: Café, almoço e janta fornecidos por Sodexo/Resov, com desconto fixo em folha.
    - Auxílio-Creche: Reembolso de até 30% do salário normativo para filhos de 0 a 18 meses.
    - Day Off: Folga no dia do aniversário, negociável se cair em feriado ou fim de semana.
    - Empréstimo Consignado: Disponível após 6 meses na empresa, sujeito à análise do Itaú.
    - Seguro de Vida: Cobertura de 24x o salário base, com assistência funeral de R$ 7.000,00.
    - Ponto Eletrônico e Banco de Horas: Apuração mensal, pagamento de extras aos sábados (50%) e domingos/feriados (100%).
    - Benefícios extras: Descontos em farmácias, lojas e serviços via SulaMais e Golden Farma.
    """
    
    dados = {
        "contents": [{"parts": [{"text": contexto + "\nPergunta: " + pergunta}]}]
    }
    
    resposta = requests.post(url, headers=headers, params={"key": api_key}, json=dados)
    
    if resposta.status_code == 200:
        resposta_json = resposta.json()
        return resposta_json["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Erro ao obter resposta do Gemini."

# Exemplo de uso
duvida = "Qual é o valor do vale alimentação?"
print(perguntar_gemini(duvida))
