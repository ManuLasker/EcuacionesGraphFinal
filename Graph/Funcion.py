from __future__ import division

import re
import numpy as np
from numpy import sin, cos, tan, sqrt, e, pi, log, \
    cosh, sinh, tanh, arccos, arcsin, arctan, abs
from ErrorException import Error


# Valid Mathematical functions
ln, asin, acos, atan = log, arcsin, arccos, arctan

# Ignored divided by zero
np.seterr(divide='ignore',invalid="ignore")


class FuncionDiff:
    np.seterr(divide='ignore', invalid="ignore")
    """
    Turns the users input into a valid mathematical function.
    """
    # Define INPUT_VALID
    VALID_INPUT = ['', 'sin', 'cos', 'tan', 'x', 'y', 'abs', 'sqrt', 'e',
                   'pi', 'log', 'ln', 'acos', 'asin', 'atan', 'cosh', 'sinh', 'tanh',
                   'arcsin', 'arctan', 'arccos']

    __fn_str = ""
    __error = ""

    def __init__(self, fn_str):
        """
        Class Constructor
        """
        self.__fn_str = fn_str

    def getError(self):
        """
        Returns the value of __error
        """
        return self.__error

    def setError(self, input):
        """
        Sets the value of __error
        """
        e = Error(input)
        self.__error = e
        return self.__error

    def ObtenerFuncionDiferencial(self, fn_str):
        """
        Returns the diferential function
        input is taken and turned into a mathematical function.
        """
        w_input = re.split(r'[0-9.+\-*/^ ()]+',fn_str)

        for w_input in w_input:
            if w_input not in self.VALID_INPUT:
                # Possible error when user input is unnexpected
                raise self.setError('Expresion no valida, %s' %w_input)
        # Replace ^ for **
        s = fn_str.replace('^', '**')
        # Replace int for float
        s = re.sub(r'[0-9.]+', r'float(\g<0>)', s)
        # print s

        try:
            # Receives input and turns it into a mathematical function.
            fn = eval("lambda x,y: "+s)
        except SyntaxError:
            raise self.setError('Error de sintaxis, errores comunes 3x en vez de '
                            '3*x, asegurese de escribir los parentesis y cada operador')
        except NameError as S:
            raise self.setError('Algo esta mal con la funcion que digito')
        except Exception as S:
            raise self.setError('Algo esta mal con la funcion que digito')

        try:
            fn(1.25,0.75)
        except(ValueError,ZeroDivisionError, OverflowError):
            pass
        except TypeError as S:
            if S.message == "'float' object is not callable":
                raise self.setError('Sintaxis invalida. Aseguro que uso multiplicacion explicita'
                                    'malo : 5y, bueno: 5*y')
            else:
                raise self.setError('algo esta mal con la funcion que digito')

        except Exception as S:
            raise self.setError('Algo esta mal con la funcion que digito')

        return fn

    def getFn(self):
        """
        Returns the value of __fn_str.
        """
        return self.__fn_str

    def convertir_Fn_str_enFuncionMatematica(self, fn_str):
        """
        Turns input into a mathematical function.
        """
        self.__fn_str = self.ObtenerFuncionDiferencial(fn_str)
