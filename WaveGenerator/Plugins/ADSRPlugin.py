from ..WaveGenerator import WaveGenerator
from WaveGeneratorPlugin import WaveGeneratorPlugin
import random
import math

## Generates an ADSR-Envelope
#
class ADSRPlugin(WaveGeneratorPlugin):

    PH_ATTACK  = 0
    PH_DECAY   = 1
    PH_SUSTAIN = 2
    PH_RELEASE = 3
    
    def __init__(self):
        self.__attackTime = 0
        self.__decayTime = 0
        self.__releaseTime = 0
        self.__sustainAmplitude = 0

    ## Sets the attack time in milli seconds.
    #  
    def setAttackTime(self, value):
        self.__attackTime = value

    ## Sets the decay time in milli seconds.
    #  
    def setDecayTime(self, value):
        self.__decayTime = value

    ## Sets the release time in milli seconds.
    #  
    def setReleaseTime(self, value):
        self.__releaseTime = value

    ## Sets the sustain level as a factor(0.0-1.0)
    #  
    def setSustainAmplitude(self, value):
        self.__sustainAmplitude = value

    ## Calclates the total length of the wave
    #  including the release time.
    #  
    def getLength( self, wg, length ):
        return length+self.__releaseTime

    def begin( self, wg, length, qtySamples ):
        self.__wg = wg
        self.__length = length
        self.__qtySamples = qtySamples

    def getValue( self, cSample, value ):

        # current pos in milli sec.
        cPos = self.__length / self.__qtySamples * cSample
        if cPos == 0: cPos = 1

        # ATTACK PHASE
        if cPos < self.__attackTime:
            f = cPos/self.__attackTime
            return value*f

        # DECAY PHASE
        if cPos < self.__attackTime+self.__decayTime :
            f = (cPos-self.__attackTime)/self.__decayTime
            return value*self.__sustainAmplitude+(value*(1-self.__sustainAmplitude))*(1-f)

        # RELEASE PHASE
        if self.__length-cPos < self.__releaseTime:
            f = (self.__length-cPos)/self.__releaseTime
            return value*self.__sustainAmplitude*f

        # SUSTAIN PHASE
        return value * self.__sustainAmplitude
