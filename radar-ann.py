import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
from matplotlib import cm
from matplotlib.colors import ListedColormap 
import numpy as np
import serial

# Trieda vizualizacie merani radaru
class Radar:
    # private variable
    # __xzy = 5
    
    # konstanta snimaca (zorny uhol 55st)
    __angel = 55.0 * np.math.pi / 180.0    # (v radianoch!!!)
    
    # constructor 
    def __init__(self):
        # Add labels
        #plt.title('TMP102 Temperature over Time')
        #plt.xlabel('Samples')
        #plt.ylabel('Temperature (deg C)')

        self.__fig = pyplot.figure()
        self.__fig.suptitle('Ultrasonic radar system', fontsize=18, fontweight='bold', fontstyle='oblique', color='red')

        ax = self.__fig.add_subplot(111, projection='polar')
        ax.set_thetagrids(range(0, 360, 30), size=8)
        ax.set_yticklabels(range(100, 600, 100), size=6)
        
        # priprava vstupu
        pos = [270 * np.math.pi / 180.0, 0, 180 * np.math.pi / 180.0]                   # poloha prekazky (v radianoch!!!)
        radii = 600 * np.random.rand(3)                # vzdialenost od prekazky (centimeters)

        top = cm.get_cmap('Reds', 128)
        bottom = cm.get_cmap('Greens', 128)
        newcolors = np.vstack((top(np.linspace(0.25, 0.75, 128)), bottom(np.linspace(0.25, 0.75, 128))))
        self.__newcmp = ListedColormap(newcolors, name='RedGreen')

        colors = self.__newcmp(radii / 600.) # pyplot.cm.viridis(radii / 600.)           # farebny ton podla vzdialenosti

        self.__barcollection = pyplot.bar(pos, radii, width=self.__angel, bottom=0.0, color=colors, alpha=0.5)

    def __animate(self, i):
        # priprava vstupu
        pos = np.random.rand(5) * 2 * np.math.pi   # poloha prekazky (v radianoch!!!)
        radii = 600 * np.random.rand(5)            # vzdialenost od prekazky (centimeters)
        colors = self.__newcmp(radii / 600.)      # farebny ton podla vzdialenosti

        self.__barcollection.remove()
        self.__barcollection = pyplot.bar(pos, radii, width=self.__angel, bottom=0.0, color=colors, alpha=0.5)

    def show(self):   
        # Set up plot to call animate() function periodically
        self.__animator = animation.FuncAnimation(self.__fig, self.__animate, blit=False, interval=100)
        pyplot.show()


r1 = Radar()

r1.show()
