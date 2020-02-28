import random as rd
class ponto:
   def __init__ (self,x,y):
      self._x = x
      self._y = y
   
   def get_coordenates_x(self):
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
   def __init__(self,points_list):
      #todo: Fazer a criação através dos pontos importados, e através do init da classe mãe   
      self.point_list = points_list


   def create_centroid_x(self):
      iterations = 0
      for point in self.point_list:
         x = point.get_coordenates_x()
         if iterations == 0:
            min_x = x 
            max_x  = x
         if x >= max_x:
            max_x = x
         if x <= min_x:
            min_x = x
         iterations +=1
      print(min_x,max_x)   
      return rd.uniform(min_x,max_x)
   
   def create_centroid_y(self):
      iterations = 0
      for point in self.point_list:
         y = point.get_coordenates_y()
         if iterations == 0:
            min_y = y 
            max_y  = y
         if y > max_y:
            max_y = y
         if y < min_y:
            min_y = y
      return rd.uniform(min_y,max_y)    
   

