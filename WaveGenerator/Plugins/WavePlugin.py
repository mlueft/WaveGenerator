from ..WaveGenerator import WaveGenerator
from WaveGeneratorPlugin import WaveGeneratorPlugin
import random
import math

class WavePlugin(WaveGeneratorPlugin):

    WF_SINUS    = 0
    WF_SAW_UP   = 1
    WF_SAW_DOWN = 2
    WF_TRIANGLE = 3
    WF_SQUARE   = 4

    ## 
    #  @param   type        Type the the generated wave.
    #                       Use one of the WavePlugin's static WF_ constants.
    #  @param   frequency   Frequency of the tremolo effect.
    #
    def __init__(self, type, frequency):
        self.__type = type
        self.__frequency = frequency

    ## Sets the frequency of the wave.
    #
    def setFrequency(self, value):
        self.__frequency = value

    ## Returns the frequency of the wave.
    #
    def getFrequency(self):
        return self.__frequency

    ## Sets the type of the wave.
    #
    def setType(self, value):
        self.__type = value

    ## Returns the type of the wave.
    #
    def getType(self):
        return self.__type

    def begin( self, wg, length, qtySamples ):
        self.__wg = wg
        self.__length = length
        self.__qtySamples = qtySamples

    def getValue( self, cSample, value ):

        angle = cSample * math.pi/180.0 * 360.0 * self.__frequency / self.__qtySamples * self.__length/1000

        if self.__type == WavePlugin.WF_SINUS:
            return value * math.sin(angle)

        if self.__type == WavePlugin.WF_TRIANGLE:
            return value * (2/math.pi)*math.asin(math.sin(angle))

        if self.__type == WavePlugin.WF_SAW_DOWN:
            return value * -(2/math.pi)*math.atan(math.tan(angle/2))

        if self.__type == WavePlugin.WF_SAW_UP:
            return value * (2/math.pi)*math.atan(math.tan(angle/2))

        if self.__type == WavePlugin.WF_SQUARE:
            if math.sin(angle)>0:
                return value
            else:
                return -value

        raise BaseException( "Wave form('" + str(self.__type) + "') not implemented." )
