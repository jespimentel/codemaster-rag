import os
from dotenv import load_dotenv

load_dotenv()
backend = os.getenv('LLM_BACKEND')


def chamar_llm(mensagem, temperatura=0.7):
    if backend == 'mock':
        return "Olá, teste!"
    elif backend == 'ollama':
        return _chamar_ollama(mensagem, temperatura)
    else:
        raise ValueError('Backend não suportado')


def _chamar_ollama(mensagem, temperatura):
    pass