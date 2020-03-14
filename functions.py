#coding=utf-8
import random

def import_points_to_group(group,points):
   list =[]
   for p in points:
      if p.get_group() == group: list.append(p)
   return list
 