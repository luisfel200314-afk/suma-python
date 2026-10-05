import os
import re
import random

# 1. Obtenemos el mensaje del commit desde GitHub
commit_msg = os.getenv('COMMIT_MESSAGE', '')

# 2. Buscamos números dentro del mensaje con una expresión regular
numeros = re.findall(r'\b\d+\b', commit_msg)

if len(numeros) >= 2:
    num1 = int(numeros[0])
    num2 = int(numeros[1])
    origen = f"Extraídos del commit: '{commit_msg}'"
else:
    # Si no pones números en el commit, genera 2 números aleatorios entre 1 y 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    origen = "Números aleatorios (no se pasaron números en el commit)"

resultado = num1 + num2

# 3. Banner dinámico
banner = f"""
┌──────────────────────────────────────────┐
│          🧮 SUMA DINÁMICA EN PYTHON 🧮   │
├──────────────────────────────────────────┤
│  Número 1 : {num1:>6}                       │
│  Número 2 : {num2:>6}                       │
│  ──────────────────────────────────────  │
│  TOTAL    : {resultado:>6} 🔥                   │
└──────────────────────────────────────────┘
"""

print(banner)

# 4. Escribir resumen en GitHub Actions
github_summary = os.getenv('GITHUB_STEP_SUMMARY')
if github_summary:
    with open(github_summary, 'a', encoding='utf-8') as f:
        f.write("### 🐍 Resultado Dinámico de la Suma\n")
        f.write(f"**Origen de los datos:** {origen}\n\n")
        f.write(f"```text\n{banner}\n```\n")
        f.write(f"**Operación ejecutada con éxito:** `{num1} + {num2} = {resultado}` ✨\n")