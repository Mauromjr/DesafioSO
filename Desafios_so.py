import os
import sys
import platform
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent

PASTA = BASE / "desafio_so"
ARQUIVO = PASTA / "exemplo.txt"
ARQUIVO_RENOMEADO = PASTA / "exemplo_renomeado.txt"


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


# ---------------------------------------------------------
# 1. ARQUIVOS - Criar arquivo
# ---------------------------------------------------------
titulo("1. CRIAR ARQUIVO")

PASTA.mkdir(exist_ok=True)
ARQUIVO.touch(exist_ok=True)

print(f"Arquivo criado: {ARQUIVO}")


# ---------------------------------------------------------
# 2. ARQUIVOS - Escrever e ler dados
# ---------------------------------------------------------
titulo("2. ESCREVER E LER DADOS")

ARQUIVO.write_text(
    "Olá! Este arquivo foi criado pelo programa python de desafios SO.\n",
    encoding="utf-8"
)

conteudo = ARQUIVO.read_text(encoding="utf-8")

print("Conteúdo do arquivo:")
print(conteudo)


# ---------------------------------------------------------
# 3. ARQUIVOS - Renomear arquivo
# ---------------------------------------------------------
titulo("3. RENOMEAR ARQUIVO")

if ARQUIVO_RENOMEADO.exists():
    ARQUIVO_RENOMEADO.unlink()

ARQUIVO.rename(ARQUIVO_RENOMEADO)

print(f"Arquivo renomeado para: {ARQUIVO_RENOMEADO}")


# ---------------------------------------------------------
# 4. DIRETÓRIOS - Criar e listar diretório
# ---------------------------------------------------------
titulo("4. CRIAR E LISTAR DIRETÓRIO")

SUBPASTA = PASTA / "subpasta"

SUBPASTA.mkdir(exist_ok=True)

print(f"Diretório criado: {SUBPASTA}")

print("\nItens encontrados dentro da pasta:")

for item in PASTA.iterdir():
    print(" -", item.name)


# ---------------------------------------------------------
# 5. PROCESSOS - Obter o próprio PID
# ---------------------------------------------------------
titulo("5. OBTER O PRÓPRIO PID")

meu_pid = os.getpid()

print(f"PID deste programa: {meu_pid}")


# ---------------------------------------------------------
# 6 e 7. PROCESSOS - Criar processo e obter PID
# ---------------------------------------------------------
titulo("6 E 7. CRIAR OUTRO PROCESSO E OBTER SEU PID")

processo = subprocess.Popen([
    sys.executable,
    "-c",
    "import os, time; "
    "print(f'Processo filho executando. PID = {os.getpid()}'); "
    "time.sleep(2)"
])

print(f"Processo filho criado.")
print(f"PID do processo filho: {processo.pid}")


# ---------------------------------------------------------
# 8. PROCESSOS - Aguardar processo terminar
# ---------------------------------------------------------
titulo("8. AGUARDAR FINALIZAÇÃO DO PROCESSO")

codigo_saida = processo.wait()

print("Processo filho terminou.")
print(f"Código de saída: {codigo_saida}")


# ---------------------------------------------------------
# 10. SISTEMA - Informações do sistema operacional
# ---------------------------------------------------------
titulo("10. INFORMAÇÕES DO SISTEMA OPERACIONAL")

print(f"Sistema operacional: {platform.system()}")
print(f"Versão: {platform.version()}")
print(f"Arquitetura: {platform.machine()}")
