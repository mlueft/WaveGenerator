from WaveGenerator import WaveGenerator

class WaveGeneratorPlugin:

    ## Returns the length of the generated wave in milliseconds.
    #  The wave generator takes the max length returned by each plugin
    #  and used the max value.
    #  This function enables a plugin to increase the length.
    #
    #  @param   wg          Instance of the wave generator
    #  @param   length      Lengh of the sound in milli seconds
    #
    def getLength( self, wg, length ):
        return length

    ## This function is called by the wave generator after all 
    #  start up calls are done and before the generation itself
    #  begins. So here is the place to start sub systems in needed.
    #
    #  @param   wg          Instance of the wave generator
    #  @param   length      Lengh of the sound in milli seconds
    #  @param   qtySamples  Total number of samples for the sound
    #
    def begin( self, wg, length, qtySamples ):
        pass

    ## This function is called by the wave generator after the 
    #  generation itself. So here is the place to stop sub systems
    #  in needed.
    #
    def end( self ):
        pass

    ## This function is called by the wave generator and allows
    #  the plugin to manipulate the value of the current sample.
    #
    #  @param   cSample     Number of the current sample
    #  @param   value       The value of the current Sample
    #
    def getValue( self, cSample, value ):
        return value
