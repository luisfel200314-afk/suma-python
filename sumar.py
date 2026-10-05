import os

# 1. Definimos los números a sumar
num1 = 45
num2 = 55
resultado = num1 + num2

# 2. Generamos un banner creativo en ASCII / Bordes
banner = f"""
┌──────────────────────────────────────────┐
│          🧮 SUMA EN PYTHON 🧮             │
├──────────────────────────────────────────┤
│  Número 1 : {num1:>6}                       │
│  Número 2 : {num2:>6}                       │
│  ──────────────────────────────────────  │
│  TOTAL    : {resultado:>6} 🔥                   │
└──────────────────────────────────────────┘
"""

# Imprimir en consola (Logs de GitHub)
print(banner)

# 3. Escribir el resultado en el 'Job Summary' de GitHub Actions
github_summary = os.getenv('GITHUB_STEP_SUMMARY')
if github_summary:
    with open(github_summary, 'a', encoding='utf-8') as f:
        f.write("### 🐍 Resultado del Script de Python\n")
        f.write(f"```text\n{banner}\n```\n")
        f.write(f"**Operación ejecutada con éxito:** `{num1} + {num2} = {resultado}` ✨\n")