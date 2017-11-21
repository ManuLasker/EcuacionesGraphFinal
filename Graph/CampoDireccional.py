from __future__ import division
from Metodo import Metodo
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
from numpy import sin, cos, tan, sqrt, e, pi, log, \
    cosh, sinh, tanh, arccos, arcsin, abs, arctan
np.seterr(divide="ignore", invalid="ignore")


class CampoDirecciones(Metodo):
    """
    Generates the direction of the fields.
    """
    np.seterr(divide='ignore', invalid="ignore")
    __div = ""
    __script = ""
    __p1 = ""

    def __init__(self, parametros, figura):
        """
        Class constructor
        """
        Metodo.__init__(self, parametros, figura)

    def hallarCampoDirecciones(self):
        """
        Finds the direction fields.
        """
        form = self.getParametros()
        fig = self.getFigura()
        TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
        # coordinate initialization:
        x = np.arange(form['xMin'], form['xMax'], 0.1)
        y = np.arange(form['yMin'], form['yMax'], 0.1)
        coord = np.meshgrid(x, y)
        x = coord[0]
        y = coord[1]
        r = 0.2  # length of arrows

        # Differential function
        fn = form['fn']
        v = sqrt((r**2)/(1+1/fn(x, y)**2))   # length of arrow in y-dir
        u = v/fn(x, y)                       # length of arrow in x-dir
        mag = np.sqrt(u ** 2 + v ** 2)/3
        angle = (np.pi / 2.) - np.arctan2(u / mag, v / mag)
        # plotting:
        i = 1

        while (i <= len(y) - 1):
            """
            Draws each vector with its corresponding mag and angle
            mag means magnitude.
            """
            if np.isscalar(mag) is False:
                fig.ray(x[i], y[i], length=mag[i], angle=angle[i],
                        color="#FB8072",
                        line_width=2)

            else:
                fig.ray(x[i], y[i], length=mag, angle=angle, color="#FB8072",
                        line_width=2)

            i = i + 1
        script, div = components(fig)  # obtains components
        self.__div = div
        self.__script = script
        self.__p1 = fig

    def getDiv(self):
        """
        Returns the value of __div.
        """
        return self.__div

    def getScript(self):
        """
        Returns the value of __script.
        """
        return self.__script

    def getP1(self):
        """
        Returns the value of __p1
        """
        return self.__p1
