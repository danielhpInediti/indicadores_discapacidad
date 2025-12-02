import pandas as pd
import json
import csv

# Cargar el archivo CSV sin encabezado para tratar todo como datos
df = pd.read_excel('encabezado_preguntas.xlsx', header=None)

# Extraer las filas correspondientes
# Fila 0 = ID, Fila 1 = Pregunta, Fila 2 = Opciones (respuestas)
ids = df.iloc[0, 1:]  # Omitimos la primera columna que es el título de la fila
preguntas = df.iloc[1, 1:]
opciones = df.iloc[2, 1:]  # Asumimos que la fila 3 tiene las respuestas

html_output = ""
respuestas = [
    # 1 Usa lentes
    [6863, 5069],
    # 2. Dificultad para ver
    [3968, 2693, 185, 17],
    # 3 Esta dificultad es ...
    [1320, 1637],
    # 4 ¿Tiene dificultad para ver con claridad la cara de una persona que está al otro lado del aula aún usando lentes?
    [5013, 1655, 166, 29],
    # 5 ¿Tiene dificultad para ver con claridad el texto de un libro aún usando lentes?
    [5560, 1220, 72, 11],
    # 6 ¿Utiliza un implante coclear o aparato auditivo?
    [57, 11875],
    # 7 ¿Tiene dificultad para oír aún usando implante coclear o aparato auditivo?
    [10, 27, 18, 2],
    # 8 Esta dificultad es:
    [5, 42],
    # 9 ¿Tiene dificultad para oír lo que se dice en una conversación con otra persona en un salón sin ruido aún usando implante coclear o aparato auditivo?
    [14, 28, 11, 4],
    # 10  ¿Tiene dificultad para oír lo que se dice en una conversación con otra persona en un salón con ruido aún usando implante coclear o aparato auditivo?
    [12, 16, 25, 4],
    # 11 ¿Tiene dificultad para caminar o subir escalones?
    [11485, 447],
    # 12 ¿Utiliza algún dispositivo o recibe ayuda para desplazarse?
    [11789, 143],
    # 13 ¿Utiliza alguna de las siguientes ayudas técnicas? (puede marcar más de una)
    [11789, 80, 15, 21, 31, 3, 15, 53, 26],
    # 14 Esta dificultad es:
    [19, 124],
    # 15 ¿Tiene dificultad para desplazarse dentro del plantel?
    [162, 216, 64, 5],
    # 16 ¿Tiene usted dificultad para levantar su mochila?
    [262, 143, 34, 8],
    # 17 ¿Tiene usted dificultad para usar sus manos y dedos? Por ejemplo, al recoger objetos pequeños como un botón o un lápiz, o al abrir y cerrar recipientes o botellas.
    [316, 88, 34, 9],
    # 18 ¿Cuándo emplea su lenguaje habitual, tiene dificultad para comunicarse, por ejemplo, para entender a los demás o para que lo entiendan?
    [10166, 1631, 125, 10],
    # 19 Esta dificultad es:
    [1518, 424],
    # 20 ¿Utiliza usted Lengua de Señas?
    [11877, 55],
    # 21 ¿Tiene dificultad para recordar?
    [6887, 4569, 461, 15],
    # 22 Esta dificultad es:
    [4351, 832],
    # 23 ¿Tiene dificultad para concentrarse?
    [5493, 5532, 848, 59],
    # 24 Esta dificultad es:
    [5101, 1453],
    # 25 ¿Tiene dificultad para valerse por sí mismo, como lavarse el cuerpo?
    [11728, 161, 32, 11],
    # 26 Esta dificultad es:
    [191, 202],
    # 27 ¿Tiene usted dificultad para valerse por sí mismo, como vestirse por sí mismo?
    [11772, 122, 29, 9],
    # 28 Esta dificultad es:
    [165, 186],
    # 29 ¿Con qué frecuencia se siente preocupado/a?
    [1161, 5463, 1567, 2133, 1608],
    # 30 ¿Con qué frecuencia se siente nervioso/a?
    [940, 5070, 1713, 2379, 1830],
    # 31 ¿Con qué frecuencia se siente ansioso/a?
    [1693, 4442, 1519, 2248, 2030],
    # 32 ¿Toma medicamentos para tratar sus estados de ánimo?
    [347, 28, 31, 584, 10586, 356],
    # 33 Escriba los medicamentos que toma
    [],
    # 34  La toma de medicamentos es:
    [787, 383],
    # 35 ¿Por qué no?
    [9524, 885],
    # 36 ¿Con qué frecuencia se siente deprimido/a?
    [4330, 4861, 1177, 1065, 499],
    # 37 ¿Toma medicamentos para la depresión?
    [159, 15, 15, 464, 10990, 289],
    # 38 Escriba los medicamentos que toma
    [],
    # 39 La toma de medicamentos es:
    [541, 296],
    # 40 ¿Por qué no?
    [9969, 839],
    # 41 En el último año, ¿con qué frecuencia la condición de salud le impidió ir a la escuela, tomar clases y/o realizar actividades de ocio?
    [7292, 3892, 380, 261, 107],
    # 42 ¿Su condición de salud mental influye para que deje de realizar las siguientes acciones como?: (Puede marcar más de una)
    [6364, 1243, 1292, 1105, 782, 505, 421, 220],
    # 43 ¿En los últimos 3 meses, con qué frecuencia sintió dolor?
    [4731, 4831, 1300, 771, 299],
    # 44 En los últimos 3 meses, ¿con qué frecuencia se ha sentido muy cansado/a o exhausto/a ?
    [2268, 4614, 1701, 2183, 1166],
    # 45 ¿Qué tipo de apoyos pueden favorecer su desempeño académico? (Puede marcar más de una)
    [1099, 1285, 1539, 1603, 1535, 1302, 1025, 800, 577, 404, 278, 165, 112, 77, 34, 32, 18, 11, 8, 5, 19, 4],
    # 46 ¿Usa tecnología de apoyo (lector de pantalla, transcriptor de audio a texto, app?
    [9553, 2379],
    # 47
    [],
    # 48 ¿Por qué no?
    [3243, 138, 6019, 153],
    # 49 ¿Ha sido diagnosticado con alguna discapacidad?
    [11139, 793],
    # 50 ¿Cuál?
    [162, 181, 126, 15, 87, 68, 63, 91],
    # 51 ¿De qué tipo de institución?
    [608, 185]
]
with open('resultados_encuesta.csv', mode='r', newline='', encoding="utf-8") as file:
    # Create a csv.writer object
    reader = csv.reader(file)
    # Write data to the CSV file
    for row in reader:
        respuestas.append(row)
# Iterar sobre las columnas
num_pregunta = 0
for col_idx in ids.index:
    if len(respuestas[num_pregunta]) == 0:
        num_pregunta += 1
        continue
    # Limpieza de datos
    p_id = str(ids[col_idx]).replace('.0', '').strip()  # Quitar decimales si existen
    p_pregunta = str(preguntas[col_idx]).strip()
    p_opciones_raw = str(opciones[col_idx])

    # Manejo de valores vacíos (NaN)
    if p_pregunta == "nan": continue

    # Inicio del bloque HTML
    html_output += f'\n'
    html_output += ' <div class="col-12 col-md-6 col-lg-4 mb-4"> <div class="card h-100"> <div class="card-body">'
    html_output += f'<label>{p_pregunta}</label>\n'
    # html_output += f'<select id="pregunta{p_id}">\n'

    # Procesar opciones (separadas por coma)

    opciones_text = []
    if p_opciones_raw != "nan" and p_opciones_raw.strip() != "":
        lista_opciones = p_opciones_raw.split(',')
        for opt in lista_opciones:
            opt_limpia = opt.strip()
            if opt_limpia:
                #  html_output += f'    <option value="{num_pregunta}">{opt_limpia}</option>\n'
                opciones_text.append(opt_limpia)
    else:
        pass
        # Opción por defecto si no hay respuestas en el renglón 2
    # html_output += f'    <option value="0">Seleccione una opción</option>\n'

    html_output += (
        f'\n <div class="chart-placeholder" style="height:350px" id="chart-pregunta{p_id}"></div></div></div></div><script>\n\n')

    JS_CHART_TEMPLATE = """
    // Initialize the echarts instance based on the prepared dom
    var myChart = echarts.init(document.getElementById('{chart_id}'));

    // Specify the configuration items and data for the chart
    var option = {{
        title: {{
            text: '{chart_title}' 
        }},
        tooltip: {{}},
        xAxis: {{
            data: {xAxis_data}
        }},
        yAxis: {{}},
        series: [
            {{
                type: 'bar',
                data: {series_data}
            }}
        ]
    }};

    // Display the chart using the configuration items and data just specified.
    myChart.setOption(option);
    """

    # --- New Data from Step 2 ---
    chart_id = 'chart-pregunta' + str(p_id)
    new_title = p_pregunta
    # new_legend_data = [p_pregunta]
    new_categories = opciones_text
    # new_series_name = p_pregunta
    new_series_values = respuestas[num_pregunta]

    # Format Python lists into valid JavaScript array strings using json.dumps
    # legend_js = json.dumps(new_legend_data)
    categories_js = json.dumps(opciones_text)
    values_js = json.dumps(new_series_values)

    # --- Injection from Step 3 ---
    final_js_code = JS_CHART_TEMPLATE.format(
        chart_id=chart_id,
        chart_title=new_title,
        # legend_data=legend_js,
        xAxis_data=categories_js,
        # series_name=new_series_name,
        series_data=values_js
    )

    html_output += final_js_code + '</script>'
    num_pregunta += 1

print(html_output)
