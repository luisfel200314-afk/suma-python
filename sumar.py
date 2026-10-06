import os
import django
from django.conf import settings
from django.template import Template, Context

# 1. Configuración de Django Templates
if not settings.configured:
    settings.configure(
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': False,
        }]
    )
    django.setup()

# 2. Plantilla con Menú de Navegación procesada por Django
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
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
      padding: 20px;
      box-sizing: border-box;
    }

    .badge-django {
      background-color: #092e20;
      color: #2ba977;
      border: 1px solid #2ba977;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: bold;
      margin-bottom: 20px;
    }

    .card {
      background-color: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 30px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
      width: 100%;
      max-width: 420px;
      text-align: center;
      box-sizing: border-box;
    }

    h1, h2 { color: #58a6ff; margin-top: 0; }

    /* Estilos del Menú */
    .menu-buttons {
      display: flex;
      flex-direction: column;
      gap: 15px;
      margin-top: 20px;
    }

    .btn-menu {
      padding: 15px;
      border-radius: 8px;
      border: 1px solid #30363d;
      background-color: #21262d;
      color: #58a6ff;
      font-size: 18px;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }

    .btn-menu:hover {
      background-color: #30363d;
      border-color: #58a6ff;
      transform: translateY(-2px);
    }

    /* Secciones Ocultas/Visibles */
    .view-section {
      display: none;
    }

    .view-section.active {
      display: block;
    }

    .btn-back {
      background-color: transparent;
      border: 1px solid #30363d;
      color: #8b949e;
      padding: 8px 16px;
      border-radius: 6px;
      cursor: pointer;
      margin-bottom: 20px;
      font-weight: bold;
    }

    .btn-back:hover {
      color: #ffffff;
      border-color: #8b949e;
    }

    /* Formulario y Tablas */
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
    .btn-action {
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
    .btn-action:hover { background-color: #2ea043; }
    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    th, td { border: 1px solid #30363d; padding: 10px; text-align: center; }
    th { background-color: #21262d; color: #58a6ff; }
    td { background-color: #0d1117; font-size: 16px; }
    .total { color: #7ee787; font-weight: bold; font-size: 20px; }
    .resta-box {
      background-color: #0d1117;
      border: 1px dashed #2ba977;
      border-radius: 8px;
      padding: 15px;
      font-size: 16px;
      margin-top: 15px;
    }
  </style>
</head>
<body>

  <div class="badge-django">⚡ Motor Django v{{ django_version }}</div>

  <!-- VISTA 1: MENÚ PRINCIPAL -->
  <div id="view-menu" class="card view-section active">
    <h1>📌 Menú Principal</h1>
    <p style="color: #8b949e;">Selecciona la operación que deseas realizar:</p>
    
    <div class="menu-buttons">
      <button class="btn-menu" onclick="showView('view-suma')">
        ➕ Operación Suma
      </button>
      <button class="btn-menu" onclick="showView('view-resta')">
        ➖ Operación Resta
      </button>
    </div>
  </div>

  <!-- VISTA 2: SECCIÓN SUMA -->
  <div id="view-suma" class="card view-section">
    <button class="btn-back" onclick="showView('view-menu')">⬅ Volver al Menú</button>
    <h2>🧮 Calculadora de Suma</h2>
    
    <div class="inputs">
      <input type="number" id="n1" placeholder="Número 1">
      <input type="number" id="n2" placeholder="Número 2">
    </div>

    <button class="btn-action" onclick="realizarSuma()">Calcular Suma 🔥</button>

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

  <!-- VISTA 3: SECCIÓN RESTA -->
  <div id="view-resta" class="card view-section">
    <button class="btn-back" onclick="showView('view-menu')">⬅ Volver al Menú</button>
    <h2>➖ Módulo de Resta</h2>
    
    <div class="resta-box">
      Renderizado desde Django:
      <br><br>
      <strong>{{ r_val1 }} - {{ r_val2 }} = <span class="total">{{ r_resultado }}</span></strong>
    </div>
  </div>

  <script>
    // Navegación entre vistas
    function showView(viewId) {
      document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
      document.getElementById(viewId).classList.add('active');
    }

    // Lógica de Suma
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

# 3. Renderizado con Contexto de Django
template = Template(template_django)
contexto = Context({
    'titulo': 'Plataforma de Operaciones - Django',
    'django_version': django.get_version(),
    'r_val1': 50,
    'r_val2': 18,
    'r_resultado': 50 - 18
})

html_generado = template.render(contexto)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_generado)

print("Página principal con menú interactivo creada con éxito.")