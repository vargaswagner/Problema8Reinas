import random
import tkinter as tk

# ventana = tk.Tk()
# ventana.title('Problema de las 8 Reynas')


# # Inicializacion de una lista
# tablero = [['_' for _ in range(8)] for _ in range(8)]

# # Función para ver tablero
# def verTablero():
#     for celdas in tablero:
#         print(celdas)

# def ataqueCruz(x, y):
#     # Ataque de la fila reyna
#     for f in range(8):
#         tablero[x][f]='X'
                
#     # Ataque de la columna de la Reyna
#     for f in range(8):
#         tablero[f][y]='X'
    
#     # Ataque en diagonales
#     for f in range(8):
#         tablero[f][y]='X'      

# # Inicializamos el tablero de 8x8
# def ataqueDiagonal(x, y):
#     for i in range(8):
#         for j in range(8):
#             if i+j==x+y:
#                 tablero[i][j]="X"
#             elif i-j==x-y:
#                 tablero[i][j]="X"
                
# reynas_colocadas = 0

# # En esta lista guardaremos las posiciones de las reynas colocadas
# posiciones = []
    
# for _ in range(500):
#     # Generamos una posición aleatoria "X" e "Y"
#     posicion_x = random.randint(0,7) #Filas
#     posicion_y = random.randint(0,7) #Columnas

#     # print("posicion_x", posicion_x)
#     # print("posicion_y", posicion_y)

#     if tablero[posicion_x][posicion_y] == '_':
#         # Colocamos una Reyna
#         print('Reyna colocada en ', posicion_x, '',posicion_y)
#         reynas_colocadas += 1
        
#         posiciones.append((posicion_x, posicion_y))
#         # Ataque en Cruz
#         ataqueCruz(posicion_x, posicion_y)
        
#         # Ataque en Diagonal
#         ataqueDiagonal(posicion_x, posicion_y)

#         tablero[posicion_x][posicion_y] = 'R'

# verTablero()
# print('reynas colocadas: ', reynas_colocadas)


# # casilla = tk.Canvas(
# #     ventana, 
# #     width=50,
# #     height=50,
# #     bg='gray'
# # )

# # casilla.grid(row=1, column=1)

# # ventana.mainloop()

# for row in range(8):
#     for col in range(8):
#         color = 'white' if (row + col) % 2 == 0 else 'black'
#         casilla = tk.Canvas(ventana, width=50, height=50, bg=color)
#         casilla.grid(row=row, column=col)

# # Cargamos una imagen de una Reyna
# imagen_reyna = tk.PhotoImage(file='queen.png')
# imagen_reyna = imagen_reyna.subsample(40,40)

# # Iteramos las posiciones
# for pos in posiciones:
#     x,y = pos
#     reyna_colocada = tk.Label(
#         ventana,
#         image = imagen_reyna
#     )
#     reyna_colocada.grid(row=x, column=y)

# ventana.mainloop()



import random
#inicializamos el tablero
tablero=[]

n=8

for _ in range(n):
        fila = [" "]*n
        tablero.append(fila)  


def tablero_view():
    for tabler in tablero:
        print(tabler)


#agregamos las posiciones de los ataques de la reina
def ataque_cruz(x,y):
    #ataque en la misma fila
    for i in range(n):
        if i!=y:
            tablero[x][i]="X" #ataque en la misma fila

    #ataque en la misma columna
    for i in range(n):
        if i!=x:
            tablero[i][y]="X" #ataque en la misma columna

def ataques_diagonales(x,y):
     for fila in range(n):
          for columna in range(n):
               if fila==x and columna==y:
                    tablero[fila][columna]="Q"
               elif fila+columna==x+y:
                    tablero[fila][columna]="X"
               elif fila-columna==x-y:
                    tablero[fila][columna]="X"

#colocamos todos los ataques en el tablero

def ataques(x,y):
    ataque_cruz(x,y)
    ataques_diagonales(x,y)

reinas=0
posiciones=[]

#en esta lista se guardan las listas de las posiciones de las reinas


def poner_posiciones():
     global reinas
     for _ in range(500):
        #agregamos una posocion aleatoria de la reina x e y
        position_x=random.randint(0,7) #fila
        position_y=random.randint(0,7) #columnas

        if tablero[position_x][position_y]==" ": #si la posicion esta vacia
            tablero[position_x][position_y]="Q"
            ataques(position_x,position_y)
            reinas+=1
            posiciones.append([position_x,position_y])
poner_posiciones()
print(reinas)

while reinas != 8:
    tablero = [[" "] * n for _ in range(n)]
    posiciones = []
    poner_posiciones()
    reinas = len(posiciones)
    if reinas == 8:
        for fila in tablero:
            print(fila)
        print("Se ha colocado 8 reinas correctamente.")
                  
tablero_view()


#visualizamos el tablero en un ventana con tkinter
import tkinter as tk
ventana=tk.Tk()
ventana.title("8 Reinas")

#dibujamos el tablero
for i in range(8):
    for j in range(8):
         color="black" if (i+j)%2==0 else "white"
         casilla=tk.Label(ventana,bg=color,width=14,height=7)
         casilla.grid(row=i,column=j)



imagen=tk.PhotoImage(file="queen.png")
imagen=imagen.subsample(21,22)
#colocar la imagen de la lista de posiciones que se guardo
for posicion in posiciones:
    reyna_colocada=tk.Label(ventana,image=imagen)
    reyna_colocada.grid(row=posicion[0],column=posicion[1])


#colocando u cuadro  de detalles al lado de la tabla, donde vemos en que posiciones se colocaron las y reinas y el nombre del autor "Gian Grobert Mamani Mamani"
# frame=tk.Frame(ventana)
# frame.grid(row=0,column=8,rowspan=8)
# #colocndo los detalles de las posiciones de la reinas
# for i in range(8):
#     tk.Label(frame,text=f"Reina {i+1} en la posicion: {posiciones[i]}").grid(row=i,column=0)



# frame2=tk.Frame(ventana)
# frame2.grid(row=0,column=8,columnspan=8)
# #agregando la foto del autor
# imagen_autor=tk.PhotoImage(file="queen.png")
# imagen_autor=imagen_autor.subsample(20,20)
# tk.Label(frame2,image=imagen_autor).grid(row=9,column=0)

# #colocando el nombre del autor
# tk.Label(frame2,text=" Autor:  Gian Grobert Mamani Mamani").grid(row=8,column=0)



ventana.mainloop()