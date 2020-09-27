# coding=utf-8
import random as rd
import numpy as np

class ponto:
   def __init__ (self,x,y):
      self.x = x
      self.y = y
  
   def set_group(self,group):
      self._group = group 

   def get_group(self):
      return self._group

   def calculate_distance_to_centroid(self,centroid):
      delta_x = (self.x - centroid.x)
      delta_y = (self.y - centroid.y)
      return (delta_x**2+delta_y**2)**(1/2)

   def point_set_group(self,centroids_list):
      i = 0 
      for centroid in centroids_list:
         dist = self.calculate_distance_to_centroid(centroid)
         if i == 0:
            min_dist = dist
            self.set_group(centroid.get_group())
            i=+1
         if dist < min_dist:
            min_dist = dist
            self.set_group(centroid.get_group())




class centroid(ponto):
   def __init__(self,points_list):
      self.points_list = points_list
      super(centroid,self).__init__(self.create_centroid_x(),self.create_centroid_y())


   def create_centroid_x(self):
      list = [i.x for i in self.points_list]
      list = sorted(list)
      return rd.uniform(list[0],list[-1])

   def create_centroid_y(self):
      list = [i.y for i in self.points_list]
      list = sorted(list)
      return rd.uniform(list[0],list[-1])

   def centroid_move(self,list_of_points):
      self.x =np.mean([i.x for i in list_of_points])
      self.y =np.mean([i.y for i in list_of_points])
