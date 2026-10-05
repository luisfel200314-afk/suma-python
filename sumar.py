import os
import re

# 1. Leer números del commit si existen, o usar valores iniciales (10 y 20)
commit_msg = os.getenv('COMMIT_MESSAGE', '')
numeros = re.findall(r'-?\d+(?:\.\d+)?', commit_msg)

if len(numeros) >= 2:
    num1, num2 = float(numeros[0]), float(numeros[1])
else:
    num1, num2 = 10.0, 20.0

num1_fmt = int(num1) if num1.is_integer() else num1
num2_fmt = int(num2) if num2.is_integer() else num2
resultado_fmt = int(num1 + num2) if (num1 + num2).is_integer() else (num1 + num2)

# 2. Generar página HTML Interactiva (Sin resumen en los logs de GitHub Actions)
html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculadora de Suma Interactiva</title>
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
      width: 380px;
      text-align: center;
    }}
    h2 {{ color: #58a6ff; margin-bottom: 20px; }}
    .inputs {{
      display: flex;
      gap: 10px;
      margin-bottom: 15px;
    }}
    input {{
      width: 50%;
      padding: 10px;
      border-radius: 6px;
      border: 1px solid #30363d;
      background-color: #0d1117;
      color: #fff;
      font-size: 16px;
      text-align: center;
      box-sizing: border-box;
    }}
    button {{
      width: 100%;
      padding: 12px;
      margin-bottom: 20px;
      border-radius: 6px;
      border: none;
      background-color: #238636;
      color: white;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
    }}
    button:hover {{ background-color: #2ea043; }}
    table {{
      width: 100%;
      border-collapse: collapse;
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
    <h2>🧮 Calculadora de Suma</h2>
    <div class="inputs">
      <input type="number" id="n1" value="{num1_fmt}" placeholder="Número 1" oninput="calcular()">
      <input type="number" id="n2" value="{num2_fmt}" placeholder="Número 2" oninput="calcular()">
    </div>
    <button onclick="calcular()">Calcular Suma 🔥</button>

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
          <td id="res-n1">{num1_fmt}</td>
          <td id="res-n2">{num2_fmt}</td>
          <td class="total" id="res-total">{resultado_fmt} 🔥</td>
        </tr>
      </tbody>
    </table>
  </div>

  <script>
    function calcular() {{
      const val1 = parseFloat(document.getElementById('n1').value) || 0;
      const val2 = parseFloat(document.getElementById('n2').value) || 0;
      const total = val1 + val2;

      document.getElementById('res-n1').innerText = val1;
      document.getElementById('res-n2').innerText = val2;
      document.getElementById('res-total').innerText = total + " 🔥";
    }}
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Página interactiva generada con éxito.")