from ..WaveGenerator import WaveGenerator
from WaveGeneratorPlugin import WaveGeneratorPlugin
import math

class SineWavePlugin(WaveGeneratorPlugin):

    ## 
    #  @param   frequency   Frequency of the tremolo effect.
    #
    def __init__(self, frequency):
        self._frequency = frequency

    ## Sets the frequency of the wave.
    #
    def setFrequency(self, value):
        self._frequency = value

    ## Returns the frequency of the wave.
    #
    def getFrequency(self):
        return self._frequency

    def _getAngle(self, cSample):
        return cSample * math.pi/180.0 * 360.0 * self._frequency / self._qtySamples * self._length/1000

    def begin( self, wg, length, qtySamples ):
        self._wg = wg
        self._length = length
        self._qtySamples = qtySamples

    def getValue( self, cSample, value ):
        angle = self._getAngle(cSample)
        return value * math.sin(angle)
