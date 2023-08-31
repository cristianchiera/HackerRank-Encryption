import math

def encryption(s):
    # Eliminar espacios en blanco y obtener la longitud del texto
    s = s.replace(" ", "")
    L = len(s)
    
    # Calcular las dimensiones del grid
    rows = math.isqrt(L)
    columns = rows if rows * rows >= L else rows + 1
    
    # Si las dimensiones no cumplen con la condicixn, ajustarlas
    if rows * columns < L:
        rows += 1
    
    # Crear el grid
    grid = [s[i:i+columns] for i in range(0, len(s), columns)]
    
   
    # Construir el mensaje cifrado
    encrypted_message = ""
    for col in range(columns):
        for row in range(rows):
            if col < len(grid[row]):
                encrypted_message += grid[row][col]
        encrypted_message += " "
    
    return  encrypted_message
