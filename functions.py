#coding=utf-8
from random import randrange
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

def centroid_variation(df_points,list_centroids,list_centroids_past):
   delta=  (df_points.max() - df_points.min())
   variation_toleraded = (delta/len(list_centroids))/3

   for i in list_centroids:
      for j in list_centroids_past:
         if i.get_group() == j.get_group(): dist_between_same_centroid = i.calculate_distance_to_centroid(j)
         if dist_between_same_centroid > variation_toleraded: return False
   return True

def read_csv(url):
   return pd.read_csv(url)

###### CREATION FUNCTIONS ###############
def create_points(df_points):
   df = df_points 
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
def visualization(list_of_points,list_of_centroids):
      df_ponto = pd.DataFrame([vars(point) for point in list_of_points], columns=['x','y'])
      df_centroid = pd.DataFrame([vars(point) for point in list_of_centroids], columns=['x','y'])
      graph =  df_ponto.plot.scatter(x='x',y='y',color = 'DarkBlue',label ='Pontos')
      df_centroid.plot.scatter(x='x',y='y',color = 'Red', label = 'Centroid',ax=graph)
      plt.show()


####### CREATE DATA  ############
def create_data(num_points,num_groups):
    data=[]
    points_group = num_points//num_groups
    for i in range(num_groups):
        x_center = randrange(-200,200)
        y_center = randrange(-200,200)    
        for j in range(points_group):
            points={}
            points['x']= x_center + randrange(-20,20)
            points['y']= y_center + randrange(-20,20)
            data.append(points)
    df = pd.DataFrame(data)
    return df
