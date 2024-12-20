import matplotlib.pyplot as plt
import numpy as np

def pie(x,y,z) : 


    plt.figure(figsize = (8, 8))
    T = np.array([x,y])
    plt.pie(T, labels=["Énergie fossile","Énergie renouvelable"], normalize=True)
    plt.legend()
    plt.title(z)
    plt.show()