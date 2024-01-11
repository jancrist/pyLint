# Pylint

Pylint es una herramienta poderosa diseñada para detectar posibles errores, anomalías y problemas de estilo en el código fuente de Python. Su objetivo principal es mejorar la calidad y mantenibilidad del código, asegurándose de que cumpla con las convenciones de estilo, evite errores sintácticos, aborde problemas de seguridad y más.

## Diagrama de Ejecución

![Diagrama de Ejecución](draw.png)

### Constructor.py - Configuración Personalizada

El archivo **constructor.py** es esencial para la configuración personalizada de Pylint. Desde este archivo, puedes definir notificaciones específicas, tales como:

- **invalid-name:** Detecta formatos de nombres no admitidos (snake_case, UPPER_CASE).
- **Docstring faltante:** Notifica cuando falta una descripción de archivo o función.
- **Unused-Import:** Advierte sobre importaciones no utilizadas en los archivos.
- **Unused Constant:** Identifica variables no utilizadas en los archivos.
- **unnecessary-pass:** Señala el uso de la declaración "pass" sin funcionalidad aparente.

### Uso de Constructor.py

1. Define requisitos y estructuras en el archivo constructor.py.
2. Mapea los requisitos con los códigos de Pylint.
3. Crea el archivo .pylintrc con los códigos y requisitos definidos.
4. Genera un nuevo archivo .pylintrc asociado a las necesidades especificadas.

Para ejecutar este archivo, utiliza el siguiente comando en la consola:

```bash
python constructor.py
```

### Ejecución de Pylint
Una vez obtenido el archivo .pylintrc personalizado, ejecútalo asociándolo con el nombre del archivo a analizar. Por ejemplo:
```bash
pylint --rcfile=custom.pylintrc archivo_a_analizar.py
```
#### La consola mostrará resultados detallados, como:
```
C0114: Missing module docstring (missing-module-docstring)
C0103: Module name "archivoErrores" doesn't conform to snake_case naming style (invalid-name)
C0116: Missing function or method docstring (missing-function-docstring)
Constant name "variable_no_cumple" doesn't conform to UPPER_CASE naming style (invalid-name)
W0611: Unused pandas imported as pd (unused-import)
W0611: Unused numpy imported as np (unused-import)
```
------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)

### Personalizaciones Admitidas
Hasta el momento, las personalizaciones admitidas incluyen:
```
- IMPORTACION_NO_UTILIZADA
- VARIABLE_NO_UTILIZADA
- METODO_NO_UTILIZADO
- LINEA_DEMASIADO_LARGA
- ESPACIOS_EN_BLANCO_NO_PERMITIDOS
- FIRMA_FUNCION_INCORRECTA
- PASS_NO_UTILIZADO
- DOCSTRING_OBLIGATORIO
- DESCRIPCION_FUNCIONES
```
