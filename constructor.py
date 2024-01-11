import configparser
import json

"""
Para deshabilitar una funcion de notificacion, introduzca 1

Ejemplo, quiero deshabilitar la notificacion del docstring obligatorio

Entonces:
DOCSTRING_OBLIGATORIO = 1
"""



#Descripcion al principio del documento
DOCSTRING_OBLIGATORIO = 1


#Una descripción para cada función o método
DESCRIPCION_FUNCIONES = 1


#Bibliotecas importadas sin uso
IMPORTACION_NO_UTILIZADA = 1

#Variables importadas sin uso
VARIABLE_NO_UTILIZADA = 0

#Pass no utilizados
PASS_NO_UTILIZADO=0


# Por ejemplo, camelCase, snake_case, UPPER_CASE. Si no se cumple será notificado.
NOMBRES_FORMATO = 'snake_case'









# Cargar el mapeo desde el archivo JSON
with open('map.json', 'r') as json_file:
    mapping = json.load(json_file)




def verifica_obligaciones(nombre_variable):
    

    # Obtener el valor de la variable
    valor_de_variable = globals().get(nombre_variable)

    if valor_de_variable == 1:
        valor_resultante = mapping.get(nombre_variable)
        
        return valor_resultante
    else:
        return ""




def verifica_formato(nombre_variable):
        

    # Obtener el valor de la variable
        valor_de_variable = globals().get(nombre_variable)

    
        valor_resultante = mapping.get(valor_de_variable)
        
        return valor_resultante
  

#Logramos la equivalencia




#On y Off
DOCSTRING_OBLIGATORIO_RESULTANTE=verifica_obligaciones("DOCSTRING_OBLIGATORIO")
DESCRIPCION_FUNCIONES_RESULTANTE=verifica_obligaciones("DESCRIPCION_FUNCIONES")
IMPORTACION_NO_UTILIZADA_RESULTANTE=verifica_obligaciones("IMPORTACION_NO_UTILIZADA")
VARIABLE_NO_UTILIZADA_RESULTANTE=verifica_obligaciones("VARIABLE_NO_UTILIZADA")
PASS_NO_UTILIZADO_RESULTANTE=verifica_obligaciones("PASS_NO_UTILIZADO")
#Formatos
NOMBRES_FORMATO_RESULTANTE=verifica_formato("NOMBRES_FORMATO")



string_constructor= f'{DOCSTRING_OBLIGATORIO_RESULTANTE}{DESCRIPCION_FUNCIONES_RESULTANTE}{IMPORTACION_NO_UTILIZADA_RESULTANTE}{VARIABLE_NO_UTILIZADA_RESULTANTE}{PASS_NO_UTILIZADO_RESULTANTE}'
# Verificar si la cadena termina con una coma y eliminarla si es necesario
string_constructor = string_constructor[:-1] if string_constructor.endswith(',') else string_constructor

# Crear un objeto ConfigParser
config = configparser.ConfigParser()

# Establecer algunas configuraciones personalizadas (puedes modificar según tus necesidades)
config['MESSAGES CONTROL'] = {
    'disable': f'{string_constructor} '  # Ejemplo de desactivar algunos mensajes
}

config['FORMAT'] = {
    'max-line-length': '120',
    'indent-string': "'    '",  # Utiliza una tabulación para la indentación
    'good-names=':f"{NOMBRES_FORMATO_RESULTANTE}"
}

# Escribir la configuración en un archivo custom.pylintrc
ruta_archivo = 'custom.pylintrc'

try:
    with open(ruta_archivo, 'w') as archivo:
        config.write(archivo)
        print(f'Se ha creado y guardado el archivo {ruta_archivo} con configuraciones personalizadas.')
except FileNotFoundError:
    print(f'Error: el archivo {ruta_archivo} no pudo ser encontrado.')
except IOError as e:
    print(f'Error al guardar el archivo {ruta_archivo}: {e}')




