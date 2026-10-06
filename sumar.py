import os
import django
from django.conf import settings
from django.template import Template, Context

# 1. Configuración básica de Django sin requerir el proyecto completo
if not settings.configured:
    settings.configure(
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': False,
        }]
    )
    django.setup()

# 2. Plantilla HTML adaptada para el motor de Django Templates
template_django = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ titulo }}</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #0d1117;
      color: #c9d1d9;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      background-color: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 30px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
      width: 380px;
      text-align: center;
    }
    h2 { color: #58a6ff; margin-bottom: 20px; }
    .inputs {
      display: flex;
      gap: 10px;
      margin-bottom: 15px;
    }
    input {
      width: 50%;
      padding: 10px;
      border-radius: 6px;
      border: 1px solid #30363d;
      background-color: #0d1117;
      color: #fff;
      font-size: 16px;
      text-align: center;
      box-sizing: border-box;
    }
    button {
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
    }
    button:hover { background-color: #2ea043; }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }
    th, td {
      border: 1px solid #30363d;
      padding: 12px;
      text-align: center;
    }
    th { background-color: #21262d; color: #58a6ff; }
    td { background-color: #0d1117; font-size: 18px; }
    .total { color: #7ee787; font-weight: bold; font-size: 22px; }
  </style>
</head>
<body>
  <div class="card">
    <h2>🧮 {{ titulo }}</h2>
    
    <div class="inputs">
      <input type="number" id="n1" placeholder="Número 1">
      <input type="number" id="n2" placeholder="Número 2">
    </div>

    <button onclick="realizarSuma()">Calcular Suma 🔥</button>

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
          <td id="res-n1">-</td>
          <td id="res-n2">-</td>
          <td class="total" id="res-total">-</td>
        </tr>
      </tbody>
    </table>
  </div>

  <script>
    function realizarSuma() {
      const val1 = document.getElementById('n1').value;
      const val2 = document.getElementById('n2').value;

      if (val1 === '' || val2 === '') {
        alert('Por favor ingresa ambos números');
        return;
      }

      const num1 = parseFloat(val1);
      const num2 = parseFloat(val2);
      const suma = num1 + num2;

      document.getElementById('res-n1').innerText = num1;
      document.getElementById('res-n2').innerText = num2;
      document.getElementById('res-total').innerText = suma + " 🔥";
    }
  </script>
</body>
</html>
"""

# 3. Procesar y renderizar usando la librería de Django
template = Template(template_django)
contexto = Context({'titulo': 'Calculadora de Suma'})
html_generado = template.render(contexto)

# 4. Guardar la salida en index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_generado)

print("Página generada exitosamente usando django.template.")