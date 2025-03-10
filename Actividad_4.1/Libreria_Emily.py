def cargar_dataset (archivo):
    import pandas as pd
    import numpy as np
    import os
    import matplotlib.pyplot as plt

    extension = os.path.splitext(archivo)[1].lower()
    if extension == '.csv':
        df = pd.read_csv (archivo)
        return (df)
    elif extension == '.xlsx':
         df = pd.read_excel (archivo)
         return (df)
    elif extension == '.json':
        df = pd.read_json (archivo)
        return (df)
    elif extension == '.html':
        df = pd.read_html (archivo)
        return (df)
    else : 
        raise ValueError (f"Formato de archivo no soportado: {extension}")
    
        
def sustituir(df, metodo, valor = None):
    if metodo == 'ffill':
        return df.fillna(method='ffill')
    elif metodo == 'bfill':
        return df.fillna(method='bfill').fillna(method = "ffill")
    elif metodo == 'string' and isinstance(valor, str):
        return df.fillna(valor)
    elif metodo == 'promedio':
        return df.fillna(df.mean(numeric_only=True))
    elif metodo == 'mediana':
        return df.fillna(df.median(numeric_only=True))
    elif metodo == 'constante' and valor is not None:
        return df.fillna(valor)
    else:
        raise ValueError("Método no válido o falta el valor requerido.")
    
