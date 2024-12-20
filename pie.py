import matplotlib.pyplot as plt

def pie(t) : 

    plt.show()
    plt.pie(t, labels=["Énergie renouvelable","Énergie fossile"], normalize=True)
    plt.colors("green","green")
    plt.lengend()