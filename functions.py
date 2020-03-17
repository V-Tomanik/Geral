#coding=utf-8
import random
import classes as cl
import pandas as pd
import matplotlib.pyplot as plt



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
def create_points():
   df = pd.read_csv(r'C:\Users\Victor\Documents\pontos.csv')
   print('This is your list of points:', df)
   list_of_points =[cl.ponto(row.x,row.y) for index, row in df.iterrows()]
   return list_of_points


def create_centroids(list_of_points):
   list_centroids = []
   n_centroids = int(input('How many Centroids?: '))
   for i in range(n_centroids):
      list_centroids.append(cl.centroid(list_of_points))
      list_centroids[i].set_group(i) 
   return list_centroids

####### VISUALIZATION FUNCTIONS ############
#todo: Create Functions for visualization
def visualization(list_of_points,list_of_centroids):
      df_ponto = pd.DataFrame([vars(point) for point in list_of_points], columns=['x','y'])
      df_centroid = pd.DataFrame([vars(point) for point in list_of_centroids], columns=['x','y'])
      graph =  df_ponto.plot.scatter(x='x',y='y',color = 'DarkBlue',label ='Pontos')
      df_centroid.plot.scatter(x='x',y='y',color = 'Red', label = 'Centroid',ax=graph)
      plt.show()