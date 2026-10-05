import sys
import os
import re

# 1. Leer números ingresados por consola o commit
if len(sys.argv) >= 3:
    n1_raw, n2_raw = sys.argv[1], sys.argv[2]
    origen = f"Ingresados manualmente desde GitHub UI ({n1_raw} y {n2_raw})"
else:
    commit_msg = os.getenv('COMMIT_MESSAGE', '')
    numeros = re.findall(r'-?\d+(?:\.\d+)?', commit_msg)
    if len(numeros) >= 2:
        n1_raw, n2_raw = numeros[0], numeros[1]
        origen = f"Extraídos del commit: '{commit_msg}'"
    else:
        n1_raw, n2_raw = "10", "20"
        origen = "Valores por defecto (no se enviaron números)"

# Convertir a flotante/entero
num1 = float(n1_raw)
num2 = float(n2_raw)
num1_fmt = int(num1) if num1.is_integer() else num1
num2_fmt = int(num2) if num2.is_integer() else num2

resultado = num1 + num2
resultado_fmt = int(resultado) if resultado.is_integer() else resultado

# 2. Generar Banner Visual
banner = f"""
┌──────────────────────────────────────────┐
│          🧮 SUMA DINÁMICA EN PYTHON 🧮   │
├──────────────────────────────────────────┤
│  Número 1 : {str(num1_fmt):>10}                   │
│  Número 2 : {str(num2_fmt):>10}                   │
│  ──────────────────────────────────────  │
│  TOTAL    : {str(resultado_fmt):>10} 🔥               │
└──────────────────────────────────────────┘
"""

print(banner)

# 3. Guardar en el Summary de GitHub
github_summary = os.getenv('GITHUB_STEP_SUMMARY')
if github_summary:
    with open(github_summary, 'a', encoding='utf-8') as f:
        f.write("### 🐍 Resultado Dinámico de la Suma\n")
        f.write(f"**Origen:** {origen}\n\n")
        f.write(f"```text\n{banner}\n```\n")
        f.write(f"**Operación:** `{num1_fmt} + {num2_fmt} = {resultado_fmt}` ✨\n")