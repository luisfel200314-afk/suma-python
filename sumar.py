import sys
import os
import re

# 1. Leer números ingresados por consola o commit
if len(sys.argv) >= 3:
    n1_raw, n2_raw = sys.argv[1], sys.argv[2]
    origen = f"Ingresados manualmente ({n1_raw} y {n2_raw})"
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

# 2. Imprimir en los logs de GitHub Actions
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

# 3. Guardar en el Summary de GitHub Actions
github_summary = os.getenv('GITHUB_STEP_SUMMARY')
if github_summary:
    with open(github_summary, 'a', encoding='utf-8') as f:
        f.write("### 🐍 Resultado Dinámico de la Suma\n")
        f.write(f"**Origen:** {origen}\n\n")
        f.write(f"```text\n{banner}\n```\n")
        f.write(f"**Operación:** `{num1_fmt} + {num2_fmt} = {resultado_fmt}` ✨\n")

# 4. Generar la página HTML con la tabla de resultados
html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Resultado de la Suma</title>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #0d1117;
      color: #c9d1d9;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }}
    .card {{
      background-color: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 30px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
      width: 360px;
      text-align: center;
    }}
    h2 {{ color: #58a6ff; margin-bottom: 10px; }}
    .origen {{ color: #8b949e; font-size: 14px; margin-bottom: 20px; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 15px;
    }}
    th, td {{
      border: 1px solid #30363d;
      padding: 12px;
      text-align: center;
    }}
    th {{ background-color: #21262d; color: #58a6ff; }}
    td {{ background-color: #0d1117; font-size: 18px; }}
    .total {{ color: #7ee787; font-weight: bold; font-size: 22px; }}
  </style>
</head>
<body>
  <div class="card">
    <h2>🧮 Resultado de la Suma</h2>
    <div class="origen">{origen}</div>
    <table>
      <thead>
        <tr>
          <th>Número 1</th>
          <th>Número 2</th>
          <th>Resultado</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{num1_fmt}</td>
          <td>{num2_fmt}</td>
          <td class="total">{resultado_fmt} 🔥</td>
        </tr>
      </tbody>
    </table>
  </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)