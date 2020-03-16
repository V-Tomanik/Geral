#coding=utf-8
import functions as fc
import matplotlib.pyplot as  plt

#Cria os pontos
list_of_points = fc.create_points()
#Cria os centroids 
list_centroids=fc.create_centroids(list_of_points)
 

x=[]
y=[]
for i in list_centroids:
   x.append(i.x)
   y.append(i.y)
plt.plot(x,y)
plt.show()

#Aloca os pontos aos centroids mais próximos
fc.kmeans_interation(list_of_points,list_centroids)
pronto = 'sim'
while pronto != 'nao':
   x=[]
   y=[]
   for i in list_centroids:
      x.append(i.x)
      y.append(i.y)
   plt.plot(x,y)
   plt.show()

   fc.kmeans_interation(list_of_points,list_centroids)
   pronto = input('Termino:')