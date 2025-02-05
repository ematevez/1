import os
import pandas as pd



def modificar_nombre_excel(ruta_original, nuevo_nombre):
    # Cargar el archivo Excel
    try:
        # Leemos el archivo Excel
        excel_data = pd.read_excel(ruta_original, engine='openpyxl')
        print("Archivo leído con éxito.")
        
        # Mostrar las primeras filas para verificar el contenido (opcional)
        print(excel_data.head())

        # Renombrar el archivo
        nueva_ruta = os.path.join(os.path.dirname(ruta_original), nuevo_nombre)
        os.rename(ruta_original, nueva_ruta)

        print(f"El archivo ha sido renombrado a: {nuevo_nombre}")
        return nueva_ruta  # Retorna la nueva ruta del archivo renombrado

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Ejemplo de uso
ruta_excel = 'datos_aleatorios.xlsx'  # Ruta del archivo original
nuevo_nombre = 'documento_modificado.xlsx'  # Nuevo nombre para el archivo

# Llamamos a la función para modificar el nombre
nueva_ruta = modificar_nombre_excel(ruta_excel, nuevo_nombre)

# Opcional: guardar el archivo con algún cambio (por ejemplo, añadir una columna)
if nueva_ruta:
    # Aquí puedes realizar modificaciones sobre el contenido del archivo si es necesario
    excel_data['NuevaColumna'] = 'Valor por defecto'
    excel_data.to_excel(nueva_ruta, index=False)
    print("Archivo guardado con los cambios.")
