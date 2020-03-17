#coding=utf-8
import functions as fc

#Cria os pontos
list_of_points = fc.create_points()
#Cria os centroids 
list_centroids=fc.create_centroids(list_of_points)
 
fc.visualization(list_of_points,list_centroids)

#Aloca os pontos aos centroids mais próximos
fc.kmeans_interation(list_of_points,list_centroids)
pronto = 'nao'
while pronto != 'sim':
   fc.visualization(list_of_points,list_centroids)
   fc.kmeans_interation(list_of_points,list_centroids)
   pronto = input('Termino:')