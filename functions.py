#coding=utf-8
import random
import classes as cl




####### INTERATION FUNCTIONS #############

def create_group_list(group,points):
   list =[]
   for p in points:
      if p.get_group() == group: list.append(p)
   return list

def kmeans_interation(list_of_points,list_centroids):
   #Faz o agrupamento dos pontos 
   for point in list_of_points:
      point.point_set_group(list_centroids)
   #Importa para os centroids a lista com os pontos e move o centroid 
   for centroid in list_centroids:
      list = create_group_list(centroid.get_group(),list_of_points)
      centroid.centroid_move(list)




###### CREATION FUNCTIONS ###############

def create_centroids(list_of_points):
   list_centroids = []
   n_centroids = int(input('How many Centroids?: '))
   for i in range(n_centroids):
      list_centroids.append(cl.centroid(list_of_points))
      list_centroids[i].set_group(i) 
   return list_centroids

def create_points():
   import_fim = 'Nao' 
   list_points = []
   while import_fim not in ('s','sim','SIM'):
      x = int(input('Digite a coordenada X: '))
      y = int(input('Digite a coordenada Y: '))
      import_fim = input('Import Finalizado? :')
      list_points.append(cl.ponto(x,y))
   return list_points

####### VISUALIZATION FUNCTIONS ############
#todo: Create Functions for visualization