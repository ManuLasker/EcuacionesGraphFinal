from __future__ import division
from Metodo import Metodo
import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file, save
from bokeh.models import Range1d
from bokeh.embed import components
from numpy import sin, cos, tan, sqrt, e, pi, log, \
    cosh, sinh, tanh, arccos, arcsin, abs, arctan
np.seterr(divide="ignore",invalid="ignore")


class eulerMejorado (Metodo):
    """
    Finds the solution of diferential ecuation and creates an x,y vector.
    """
    __div = ""
    __script = ""
    __p1 = ""

    def __init__(self, Parametros, figura):
        """
        Class constructor
        """
        Metodo.__init__(self,Parametros,figura)

    def getDiv(self):
        """
        Returns the value of __div
        """
        return self.__div

    def getScript(self):
        """
        Returns the value of __script
        """
        return self.__script

    def hallarSolucion(self):
        """
        Generates lines for Euler's method plot.
        """
        form = self.getParametros()
        TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
        # Step size, the smaller the better, however it may take longer to compute
        f = form['fn']
        x = []
        y = []
        delta = form['delta']
        new_x = form['x0']
        new_y = form['y0']
        ymargin = 0.5 * (form['yMax'] - form['yMin'])

        while (new_x < form['xMax'] - delta and
               form['yMin'] - ymargin < new_y < form['yMax'] + ymargin):
            # Plots the given values until the xMax and yMax are satisfied

            old_x = new_x
            old_y = new_y
            """
            Compute derivative.  Could be bad, so abort with results so far if
            division by zero or NaN occurs.
            """

            try:
                yp = f(old_x, old_y)
            except ArithmeticError:
                break

            if np.isnan(yp):
                break
            new_x = old_x + delta
            # print "new_t = " + str(new_t)
            new_y = old_y + yp * delta

            try:
                ypp = (f(old_x, old_y) + f(new_x, new_y))/2
            except ArithmeticError:
                break
            if np.isnan(ypp):
                # When ypp is NaN breaks the while
                break

            new_y = old_y + delta * ypp
            # plt.plot(old_t,yp)
            x.append(old_x)
            y.append(old_y)

            if old_x + delta > form['xMax']:
                break

        p1 = self.getFigura()
        # Draws the starting point
        p1.circle(form['x0'], form['y0'], size=15, fill_color="green",
                  line_color="red", line_width=2)
        p1.line(x, y)  # Draws the line obtained by the function
        script, div = components(p1)  # obtains components
        self.__p1 = p1
        self.__div = div
        self.__script = script
