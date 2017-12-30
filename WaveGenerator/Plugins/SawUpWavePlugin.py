from SineWavePlugin import SineWavePlugin
import math

class SawUpWavePlugin(SineWavePlugin):

    def getValue( self, cSample, value ):
        angle = self._getAngle(cSample)
        return value * (2/math.pi)*math.atan(math.tan(angle/2))
