from SineWavePlugin import SineWavePlugin

class WavePlugin(SineWavePlugin):

    def getValue( self, cSample, value ):
        angle = self._getAngle(cSample)
        if math.sin(angle)>0:
            return value
        else:
            return -value
