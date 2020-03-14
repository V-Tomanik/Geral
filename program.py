#coding=utf-8
import classes as cl
import functions as fc
import pandas as pd
import matplotlib.pyplot as  plt

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

#Cria os centroids 
list_centroids=[]
for i in range(int(input('Numero de Centroids: '))):
   list_centroids.append(cl.centroid(list_of_points))
   list_centroids[i].set_group(i) 
#todo:criar a iteração dos centroides

x=[]
y=[]
for i in list_centroids:
   x.append(i.x)
   y.append(i.y)
plt.plot(x,y)
plt.show()

#Aloca os pontos aos centroids mais próximos
for point in list_of_points:
   point.point_interation(list_centroids)
   
for centroid in list_centroids:
   list = fc.import_points_to_group(centroid.get_group(),list_of_points)
   centroid.centroid_move(list)

x=[]
y=[]
for i in list_centroids:
   x.append(i.x)
   y.append(i.y)
plt.plot(x,y)
plt.show()