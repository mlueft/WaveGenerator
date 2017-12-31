from ..WaveGenerator import WaveGenerator
from WaveGeneratorPlugin import WaveGeneratorPlugin
import random
import math

## Generates an Envelope
#
class EnvelopPlugin(WaveGeneratorPlugin):

    def __init__(self):
        self.__wg = None
        self.__length = 0
        self.__qtySamples = 0
        self.__values = []

    ## 
    #   @param  time    Time in milli seconds.
    #   @param  value   Factor for amplitude
    #                   0.0 = 0%
    #                   0.4 = 40%
    #                   1.0 = 100%
    def addValue(self, time, level):
        self.__values.append( [time, float(level)] )
        self.__values.sort()

    def getLength( self, wg, length ):
        return length

    def begin( self, wg, length, qtySamples ):
        self.__wg = wg
        self.__length = length
        self.__qtySamples = qtySamples

    def getValue( self, cSample, value ):

        # current pos in milli sec.
        cPos = self.__length / self.__qtySamples * cSample

        if len(self.__values) == 0:
            return value

        if cPos == 0:
            return self.__values[0][1]

        if cPos >= self.__values[len(self.__values)-1][0]:
            return value * self.__values[len(self.__values)-1][1]
        
        for i in range(0,len(self.__values)):
            if self.__values[i][0] >= cPos:
                v0 = self.__values[i-1]
                v1 = self.__values[i]
            
                deltaV = v1[1]-v0[1]
                deltaT = v1[0]-v0[0]
                
                f = v0[1]+deltaV*(cPos-v0[0])/deltaT
                return value * f
