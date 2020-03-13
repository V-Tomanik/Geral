# coding=utf-8
import random as rd
class ponto:
   def __init__ (self,x,y):
      self._x = x
      self._y = y
   
   def get_coordenate_x(self):
      return self._x

   def get_coordenate_y(self):
      return self._y

   def set_group(self,group):
      self._group = group 

   def get_group(self,group):
      return self._group

   def calculate_distance_centroid_point(self,centroid):
      delta_x = (self._x - centroid.get_coordenates_x())**2
      delta_y = (self._y - centroid.get_coordenates_y())**2
      return (delta_x**2-delta_y**2)**2

   def point_interation(self,centroids_list):
      iterations = 0 
      for centroid in centroids_list:
         dist = self.calculate_distance_centroid_point(centroid)
         if iterations == 0:
            min_dist = dist
            self.set_group(centroid.get_group)
         if dist < min_dist:
            min_dist = dist
            self.set_group(centroid.get_group)
      

class centroid(ponto):
    def create_centroid_x(self):
       list = [i.get_coordenate_x() for i in self.points_list]
       list = sorted(self.point_list.get_coordenate_x())
       return rd.uniform(list[0],list[-1])

    def create_centroid_y(self):
       list = [i.get_coordenate_y() for i in self.points_list]
       list = sorted(self.point_list.get_coordenate_y())
       return rd.uniform(list[0],list[-1])


    def __init__(self,points_list):
#todo: Fazer a criação através dos pontos importados, e através do init da class    ...e mãe
    self.points_list = points_list
    super(centroid,self).__init__(self.create_centroid_x(),self.create_centroid_y(    ...))

