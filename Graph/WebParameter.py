from Funcion import FuncionDiff
import re


class webParameter:

    __parametros = ""

    def __init__(self, parametros):
        """
        Class constructor.
        """
        self.__parametros = parametros

    def getParametros(self):
        """
        Returns the value of __parametros
        """
        return self.__parametros

    def obteniendoDatos(self):
        """
        Obtains the parameters and adds them to the dictionary.
        """
        parametros = self.getParametros()
        xmin = float(parametros['xMin'])
        xmax = float(parametros['xMax'])

        ymin = float(parametros['yMin'])
        ymax = float(parametros['yMax'])

        x0 = float(parametros['x0'])
        y0 = float(parametros['y0'])
        delta = float(parametros['delta'])
        metodo = ""

        if 'euler' in parametros:
            metodo = 'euler'

        if 'eulerMejor' in parametros:
            metodo = 'eulerMejor'

        if 'rungeKutta' in parametros:
            metodo = 'rungeKutta'

        fd_str = parametros['fd_str']

        return {'xMin': xmin, 'xMax': xmax, 'yMin': ymin, 'yMax': ymax, 'delta': delta, 'x0': x0, 'y0': y0,
                'fd_str': fd_str, 'metodo': metodo}
