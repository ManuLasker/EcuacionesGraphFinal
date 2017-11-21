import numpy as np

class Metodo:
    np.seterr(divide='ignore', invalid="ignore")
    _Parametros = {}
    _figura = ""

    def __init__(self, Parametros, figura):
        """
        Class Constructor.
        """
        self._Parametros = Parametros
        self._figura = figura

    def getParametros(self):
        """
        Returns the value of _Parametros.
        """
        return self._Parametros

    def getFigura(self):
        """
        Returns the value of _figura.
        """
        return self._figura