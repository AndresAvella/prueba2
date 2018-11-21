# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("hola mundo cruel , muy cruel ")
i=1
while i <200:
    if(i==1):
        print ( i, " mundo muy ")
    if(i>2):
        print("muuuuuyy")
    if(i==199):
                print("cruel")
        
    i=i+1
    
plt.figure()
x=np.linspace(0,100)
y=np.linspace(0,100)
plt.plot(x,y)
plt.savefig("mundo cruel")
