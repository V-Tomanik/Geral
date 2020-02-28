import classes as cl
import functions as fc
import pandas as pd


list_of_points = []
k=0
import_points_finalizado = 'Não'

#todo: Fazer via read_csv do pandas
print('Importe os pontos')
while import_points_finalizado != 'sim':
   x = float(input('Coordenada X: '))
   y = float(input('Coordenada Y: '))
   list_of_points.append(cl.ponto(x,y))
   import_points_finalizado = input('Todos os pontos importados?')


print(list_of_points)
print(list_of_points[0].get_coordenate_y())
cd = cl.centroid(list_of_points)
print(cd.create_centroid_x())
#todo:criar a iteração dos centroides

