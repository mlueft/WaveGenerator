from SineWavePlugin import SineWavePlugin

class WavePlugin(SineWavePlugin):

    def getValue( self, cSample, value ):
        angle = self._getAngle(cSample)
        return value * (2/math.pi)*math.asin(math.sin(angle))
