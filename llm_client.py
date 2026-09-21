import os
from dotenv import load_dotenv

load_dotenv()

backend = os.getenv('LLM_BACKEND')

def chamar_llm(mensagens, temperatura=0.7):
    if backend == 'mock':
        return 'Resposta simulada.'

    raise ValueError('Backend não suportado')


print(chamar_llm("Olá"))

