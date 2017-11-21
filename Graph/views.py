from django.shortcuts import render, HttpResponse, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from django.http.request import HttpRequest

from RungeKutta import rungeKutta
from WebParameter import webParameter
from Graficador import Graficador
from EulerMejorado import eulerMejorado
from MetodoEuler import MetodoEuler
from CampoDireccional import CampoDirecciones


class views:

    __webData = ""
    __Graficador = ""

    def __init__(self):
        pass

    def getWebData(self):
        """
        Returns the value of __webData
        """
        return self.__webData

    # Create your views here.
    def home(self, request):
        """
        Sends the neccesary data to show in web app.
        """
        parametros = request.GET.dict()
        figura = ""
        # print parametros
        args = {'xMin': 0, 'xMax': 3,
                'yMin': -1, 'yMax': 1, 'x0': 0.1, 'y0': 0.1, 'delta': 0.1,
                'fd_str': '2*y/tan(2*x)'}

        if bool(parametros):

            # Creates webData with its parameters
            self.__webData = webParameter(parametros)
            # Obtains data
            dataWeb = self.__webData.obteniendoDatos()
            # print(self.__webData.obteniendoDatos())
            self.__Graficador = Graficador(parametros)
            # Args gets the dictionary 
            args = self.__Graficador.getPd()
            # print(args)

            if('error' not in args.keys()):
                # create TOOLS for the plugin
                TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
                # create figure fot the plot
                figura = figure(title="f'(x,y) = {}".format(args['fd_str']), plot_width=800,
                                plot_height=500, tools=TOOLS, x_range=(args['xMin']-0.05, args['xMax']),
                                y_range=(args['yMin'], args['yMax']))
                # plot with differents methods
                if(args['metodo'] == 'euler'):
                    eulerMethod = MetodoEuler(args,figura)
                    eulerMethod.hallarSolucion()
                    figura = eulerMethod.getFigura()
                if (args['metodo'] == 'eulerMejor'):
                    eulerBest = eulerMejorado(args,figura)
                    eulerBest.hallarSolucion()
                    figura = eulerBest.getFigura()
                if (args['metodo'] == 'rungeKutta'):
                    rungeSolve = rungeKutta(args,figura)
                    rungeSolve.hallarSolucion()
                    figura = rungeSolve.getFigura()
                # obtained figure

                campoGrafica = CampoDirecciones(args,figura)
                campoGrafica.hallarCampoDirecciones()
                # adding the html form of the plotting to the args
                args['divCampo'] = campoGrafica.getDiv()
                args['scripCampo'] = campoGrafica.getScript()

        return render(request,'Graph/page.html', args)
