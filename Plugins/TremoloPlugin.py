from ..WaveGenerator import WaveGenerator
from WaveGeneratorPlugin import WaveGeneratorPlugin
from WaveGenerator.Plugins.WavePlugin import WavePlugin

import random
import math

class TremoloPlugin(WaveGeneratorPlugin):

    def __init__( self, frequency, amplitude ):
        self.__frequency = frequency
        self.__amplitude = amplitude

    def begin( self, wg, length, qtySamples ):
        self.__wg = WaveGenerator()
        self.__wg.setSamplingRate(wg.getSamplingRate())
        self.__wg.setAmplitude(self.__wg.getAmplitude()*self.__amplitude)

        p = WavePlugin( WavePlugin.WF_SINUS, self.__frequency)
        self.__wg.addPlugin("p0",p)
        self.__data = self.__wg.generate( length )

    def getValue( self, cSample, value ):
        return value*(1-self.__amplitude)+self.__data[cSample]

