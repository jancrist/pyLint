# Pylint

Su propósito principal es detectar posibles errores, anomalías y problemas de estilo
 en el código fuente de Python. PyLint examina el código en busca de errores
a las convenciones de estilo, errores sintácticos, problemas de seguridad, y otros
aspectos que podrían afectar la calidad y mantenibilidad del código.


## Diagrama de ejecucion

![Texto Alternativo](draw.png)




### El archivo **CONSTRUCTOR.PY** es el encargado de elaborar un arhivo .pylintrc  . Desde el se pueden definir ciertas notificaciones como:
##### Definir un formato de nombre y notificar cuando este no se cumpla, obligar a establecer un  Docstring en cada archivo, notificar de importaciones, variables o pass no utilizados.

#### - invalid-name (tipo de nombres, snake_case, UPPER_CASE) formato de nombre no admitido. 

#### - Docstring (descripcion de archivo) faltante en los archivos.

#### - Function Docstring (descripcion de funcion) faltante en las funciones.

#### - Unused-Import (Importacion no utilizada) en los archivos.

#### - Unused Constant ( Variable no utilizada) en los archivos.

#### - unnecessary-pass (Pass sin funcion) en los archivos.


