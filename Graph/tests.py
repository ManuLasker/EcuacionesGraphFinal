import unittest
from bokeh.plotting import figure
from Graph.views import views
from Graph.CampoDireccional import CampoDirecciones
from Graph.Funcion import FuncionDiff
from Graph.MetodoEuler import MetodoEuler
from Graph.EulerMejorado import eulerMejorado
from Graph.RungeKutta import rungeKutta
import Funcion as fun


# Create your tests here.


class TestWebData(unittest.TestCase):

    @classmethod
    def setUp(self):
        v = views()
        self.parametros = {'xMin': 0, 'xMax': 3,
                'yMin': -1, 'yMax': 1, 'x0': 0.1, 'y0': 0.1, 'delta': 0.1,
                'fd_str': '2*y/tan(2*x)'}
        self.trans = v.getWebData()
        print (self.trans)
        print (self.parametros)
        self.assertDictEqual(self.parametros,self.trans,'error with webParameter')

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

class TestFuncion(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.funcion = FuncionDiff('')


    def testValidFunction(self):
        r = self.funcion.ObtenerFuncionDiferencial('sin(2+pi)*e^(1.2) + 1/2 - sqrt(2)')
        self.assertEqual(r(1, 1), -3.933187336977838)
        r = self.funcion.ObtenerFuncionDiferencial('x+y/2')
        self.assertEqual(r(1, 1), 1.5, 'x=1,y=1')
        self.assertEqual(r(-1, 4), 1, 'x=-1,y=1')

    def testInvalidWord(self):
        self.assertRaises(fun.Error, self.funcion.ObtenerFuncionDiferencial, '3 + int(1.2)')

    def testSyntaxError(self):
        self.assertRaises(fun.Error, self.funcion.ObtenerFuncionDiferencial, '3+*2')

    def testNameError(self):
        self.assertRaises(fun.Error, self.funcion.ObtenerFuncionDiferencial, 'sin.t')

    def testSanityError(self):
        self.assertRaises(fun.Error, self.funcion.ObtenerFuncionDiferencial, 'sin + t')

class TestCampoDireccional(unittest.TestCase):
    def setUp(self):
        self.args = {'xMin': 1, 'xMax': 0,
                       'yMin': 0, 'yMax': 2, 'x0': 0.1, 'y0': 0.1, 'delta': 0.1,
                       'fd_str': lambda t,y:1}
        self.TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

    def TestHallarCampo(self):

        figura = figure(title="f'(x,y) = {}".format(self.args['fd_str']), plot_width=800,
                        plot_height=500, tools=self.TOOLS, x_range=(self.args['xMin'] - 0.05, self.args['xMax']),
                        y_range=(self.args['yMin'], self.args['yMax']))
        campo = CampoDirecciones(self.args,figura)
        self.assertRaises(ArithmeticError,campo.hallarCampoDirecciones())
        r = campo.hallarCampoDirecciones()
        self.assertAlmostEqual(r.sum(), 3)

class TestMetodoEuler(unittest.TestCase):

    args = {'xMin': 0, 'xMax': 3,
            'yMin': -1, 'yMax': 1, 'x0': 0.1, 'y0': 0.1, 'delta': 0.1,
            'fd_str': '2*y/tan(2*x)'}

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

    def TestHallarSolucion(self):
        figura = figure(title="f'(x,y) = {}".format(self.args['fd_str']), plot_width=800,
                        plot_height=500, tools=self.TOOLS, x_range=(self.args['xMin'] - 0.05, self.args['xMax']),
                        y_range=(self.args['yMin'], self.args['yMax']))
        metodo = MetodoEuler(self.args,figura)
        self.assertRaises(ArithmeticError, metodo.hallarSolucion())

class TestEulerMejorado(unittest.TestCase):
    args = {'xMin': 0, 'xMax': 3,
            'yMin': -1, 'yMax': 1, 'x0': 0.1, 'y0': 0.1, 'delta': 0.1,
            'fd_str': '2*y/tan(2*x)'}

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

    def sumaSlope(self):
        self.assertEqual(1 + 1, 2)

    def TestHallarSolucion(self):
        figura = figure(title="f'(x,y) = {}".format(self.args['fd_str']), plot_width=800,
                        plot_height=500, tools=self.TOOLS, x_range=(self.args['xMin'] - 0.05, self.args['xMax']),
                        y_range=(self.args['yMin'], self.args['yMax']))

        metodo = eulerMejorado(self.args,figura)
        self.assertRaises(ArithmeticError, metodo.hallarSolucion())
        self.assertEqual(self.args,metodo.getParametros())

class TestRungeKuta(unittest.TestCase):
    args = {'xMin': 0, 'xMax': 3,
            'yMin': -1, 'yMax': 1, 'x0': 0.1, 'y0': 0.1, 'delta': 0.1,
            'fd_str': '2*y/tan(2*x)'}

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

    def TestHallarSolucion(self):
        figura = figure(title="f'(x,y) = {}".format(self.args['fd_str']), plot_width=800,
                        plot_height=500, tools=self.TOOLS, x_range=(self.args['xMin'] - 0.05, self.args['xMax']),
                        y_range=(self.args['yMin'], self.args['yMax']))

        metodo = rungeKutta(self.args, figura)
        self.assertRaises(ArithmeticError, metodo.hallarSolucion())
        self.assertEqual(self.args, metodo.getParametros())

if __name__ == "__main__":
    unittest.main()