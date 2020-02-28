import random

def max_coordinates_x(object_point_list):
   max_x = 0 
   for i in object_point_list:
      x = i.get_coordenates_x()
      if x > max_x:
         max_x = x
   return max_x         

def max_coordinates_y(object_point_list):
   max_y = 0
   for i in object_point_list:
      y = i.get_coordenates_y()
      if y > max_y:
         max_y = y
   return max_y
