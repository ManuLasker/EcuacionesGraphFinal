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


class rungeKutta(Metodo):

    __div = ""
    __script = ""
    __p1 = ""

    def __init__(self, parametros, figura):
        """
        Class Constructor
        """
        Metodo.__init__(self, parametros, figura)

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

            old_x = new_x
            old_y = new_y
            # Compute derivative.  Could be bad, so abort with results so far if a
            # Division by zero or NaN occurs.
            try:
                k1 = f(old_x, old_y)
                k2 = f(old_x + (1/2)*delta, old_y + (1/2)*delta*k1)
                k3 = f(old_x + (1/2)*delta, old_y + (1/2)*delta*k2)
                k4 = f(old_x + delta, old_y + delta*k3)
            except ArithmeticError:
                break
            if np.isnan(k1) or np.isnan(k2) or np.isnan(k3) or np.isnan(k4):
                break

            new_x = old_x + delta
            # print "new_t = " + str(new_t)
            new_y = old_y + ((k1+2*k2+2*k3+k4)/6) * delta
            # plt.plot(old_t,yp)
            x.append(old_x)
            y.append(old_y)
            if old_x + delta > form['xMax']:
                break

        p1 = self.getFigura()
        p1.circle(form['x0'], form['y0'], size=15, fill_color="purple", line_color="red", line_width=2)
        p1.line(x, y)
        script, div = components(p1)
        self.__p1 = p1
        self.__div = div
        self.__script = script

    def getDiv(self):
        """
        Returns the valuf of __div
        """
        return self.__div

    def getScript(self):
        """
        returns the value of __script
        """
        return self.__script
