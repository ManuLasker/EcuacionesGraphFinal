from WebParameter import webParameter
from Funcion import FuncionDiff
from ErrorException import Error

import re


class Graficador:

    __error = ""
    __webData = ""
    __funcion = ""
    __Pd = ""

    def __init__(self, dataWeb):
        """
        Sets in the constructor the web parameters from views.
        """
        self.__webData = webParameter(dataWeb)

    def getFuncion(self):
        """
        Returns the value of __funcion
        """
        return self.__funcion

    def ValidacionParametrosDeLaGraficadora(self):
        """
        Turns the user input into a mathematical function.
        """
        # Creating params dictionary
        Pd = self.__webData.obteniendoDatos()

        # Verifies if the current limits are maximum and minimum
        if Pd['xMax'] <= Pd['xMin']:
            Pd['xMax'] = Pd['xMin'] + 1
        if Pd['yMax'] <= Pd['yMin']:
            Pd['yMax'] = Pd['yMin'] + 1

        # According to the limits validate the initial data
        if Pd['x0'] < Pd['xMin'] or Pd['x0'] >= Pd['xMax']:
            Pd['x0'] = 0.5 * (Pd['xMin'] + Pd['xMax'])
        if Pd['y0'] < Pd['yMin'] or Pd['y0'] > Pd['yMax']:
            Pd['y0'] = 0.5 * (Pd['yMin'] + Pd['yMax'])

        # Obtains the mathematical function
        if Pd['fd_str']:
            Pd['fd_str'] = re.sub(r'\bt\b', 'x', Pd['fd_str'])  # replace t por x
            # Creates the function
            self.__funcion = FuncionDiff(Pd['fd_str'])
            # Turns __funcion into a mathematical function
            self.__funcion.convertir_Fn_str_enFuncionMatematica(Pd['fd_str'])
            # Adds __funcion into the dictionary
            Pd['fn'] = self.__funcion.getFn()

        self.__Pd = Pd
        return Pd

    def getWebData(self):
        """
        returns the value of __webData
        """
        return self.__webData

    def getPd(self):
        """
        returns the value of __Pd
        """
        try:
            self.ValidacionParametrosDeLaGraficadora()
        except Error as str:
            args = {'error': 'Warning!! {}'.format(str)}
            return args
        return self.__Pd
