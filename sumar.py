import os
import django
from django.conf import settings
from django.template import Template, Context

# 1. Configuración del entorno de Django
if not settings.configured:
    settings.configure(
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': False,
        }]
    )
    django.setup()

# 2. Operación de Resta calculada en el backend con Python/Django
resta_val1 = 50
resta_val2 = 18
resultado_resta = resta_val1 - resta_val2

# 3. Plantilla usando sintaxis y variables nativas de Django Templates ({% %}, {{ }})
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
      min-height: 100vh;
      margin: 0;
      padding: 20px;
      box-sizing: border-box;
    }
    .container {
      display: flex;
      flex-direction: column;
      gap: 20px;
      width: 100%;
      max-width: 420px;
    }
    .card {
      background-color: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 25px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
      text-align: center;
    }
    .badge-django {
      background-color: #092e20;
      color: #2ba977;
      border: 1px solid #2ba977;
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: bold;
      display: inline-block;
      margin-bottom: 15px;
    }
    h2 { color: #58a6ff; margin-top: 5px; margin-bottom: 20px; font-size: 20px; }
    .inputs { display: flex; gap: 10px; margin-bottom: 15px; }
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
    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    th, td { border: 1px solid #30363d; padding: 10px; text-align: center; }
    th { background-color: #21262d; color: #58a6ff; }
    td { background-color: #0d1117; font-size: 16px; }
    .total { color: #7ee787; font-weight: bold; font-size: 18px; }
    .resta-box {
      background-color: #0d1117;
      border: 1px dashed #2ba977;
      border-radius: 8px;
      padding: 15px;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <div class="container">
    
    <!-- Bloque 1: Generado directamente por el contexto de Django -->
    <div class="card">
      <span class="badge-django">⚡ Procesado por Django v{{ django_version }}</span>
      <h2>➖ Resta en Backend (Django)</h2>
      <div class="resta-box">
        Operación: <strong>{{ r_val1 }} - {{ r_val2 }}</strong> = <span class="total">{{ r_resultado }}</span>
      </div>
    </div>

    <!-- Bloque 2: Calculadora interactiva en Frontend -->
    <div class="card">
      <h2>🧮 {{ titulo }} (Frontend)</h2>
      
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

# 4. Inyección de variables de Python/Django al Contexto de la Plantilla
template = Template(template_django)
contexto = Context({
    'titulo': 'Calculadora de Suma',
    'django_version': django.get_version(),
    'r_val1': resta_val1,
    'r_val2': resta_val2,
    'r_resultado': resultado_resta
})

# 5. Renderizado del HTML final
html_generado = template.render(contexto)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_generado)

print(f"Index HTML generado con Django v{django.get_version()}")