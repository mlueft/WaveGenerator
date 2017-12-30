import math

class WaveGenerator:

    def __init__(self):
        self.__samplingRate = 8000
        self.__amplitude = 1.0
        self.__plugins = {}

    ## Adds the given plugin to the list of plugins used
    #  during the wave generation process.
    #
    #  @param      plugin      A instance of the WaveGeneratorPlugin
    #  @return                 A unique id of the plugin. It can be 
    #                           used to remove a plugin  with the
    #                           removePlugin function.
    def addPlugin(self, plugin):
        id = str(len(self.__plugins))
        self.__plugins[id] = plugin
        return id

    ## Removes a Plugin of the list of plugins used
    #  during the wave generation process.
    #
    #  @param      id  A ID returned by addPlugin.
    #
    def removePlugin(self, id):
        del self.__plugins[id]


    ## Sets the rampling rate of the generated wave.
    #
    def setSamplingRate(self, value):
        self.__samplingRate = value

    ## Returns the sampling rate of the generated wave.
    #
    def getSamplingRate(self):
        return self.__samplingRate

    ## Sets the amplitude of the generated Wave.
    #
    def setAmplitude(self, value):
        self.__amplitude = value

    ## Returns the amplitude of the generated wave.
    #
    def getAmplitude(self):
        return self.__amplitude

    ## Generates the wave data.
    #
    #  @param   length      Lengh of the wave in milli seconds
    #  @return              A list with wave data.
    #
    def generate(self, length = 1000):

        length    = float(length)

        # Let plugins manipulate the length of the sound
        for p in self.__plugins:
            length = max(
                length,
                self.__plugins[p].getLength( self, length )
            )

        # total number of samples
        qtySamples = int(length*self.__samplingRate/1000)

        # send plugins the signal to begin
        for p in self.__plugins:
            self.__plugins[p].begin( self, length, qtySamples )

        # Let plugins calculate the value of the current sample
        data = []
        for i in range( 0, qtySamples ):
            value = self.__amplitude
            for p in self.__plugins:
                value = self.__plugins[p].getValue(i,value)

            data.append( value )

        # send plugins the signal to end
        for p in self.__plugins:
            self.__plugins[p].end()

        return data
