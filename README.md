# WaveGenerator
A Python wave generator with plugin system.

# Example 1 - Simple sine wave
```python
from WaveGenerator.WaveGenerator import WaveGenerator
from WaveGenerator.Plugins.SineWavePlugin import SineWavePlugin

# Instantiate the WaveGenerator class.
w = WaveGenerator()

# Sets the sampling rate.
# 10 Samples per second.
w.setSamplingRate(10)

# Instantiates a Wave plugin to generate a sine wave
# with 3 Hz.
p = SineWavePlugin( 3 )

# Adds the plugin to the wave generator
w.addPlugin( p )

# Generates the wave data for 1000 milliseconds.
# It returns a List with 10(sampling rate * length/1000) values
data = w.generate( 1000 )

# Prints values between -1 and 1 because standart amplitude
# is 1
print len(data)
print max(data)
print min(data)
```

# Example 2 - Adding an envelope 
In this example we change some parameters. We use a sampling rate of 22000 samples
and a resolution of 8 bits. At the end we raise all values by 127 to generate data
that can be used in an wave file.

```python
from WaveGenerator.WaveGenerator import WaveGenerator
from WaveGenerator.Plugins.SineWavePlugin import SineWavePlugin
from WaveGenerator.Plugins.ADSRPlugin import ADSRPlugin

samplingRate = 22000
resolution   = 8        # 8 bit resolution for a simple wave file
channels     = 1
duration     = 800      # milli sec
frequency    = 440.0

# for 8 bit amplitude is 125
amplitude    = (2**(resolution-1)-1)

# offset is 128
# generate returnes values between -127/127
# we raise all values be 128 to get values
# between 0/255.
offset       = 2**(resolution-1)

# Instantiate the WaveGenerator class.
w = WaveGenerator()

# Sets the sampling rate.
# 10 Samples per second.
w.setSamplingRate(samplingRate)

# Sets the amplitude.
w.setAmplitude(amplitude)

# Instantiates a Wave plugin to generate a sine wave
# with 440 Hz.
p = SineWavePlugin(  440 )

# Adds the plugin to the wave generator
w.addPlugin( p )

# see https://en.wikipedia.org/wiki/Synthesizer#Attack_Decay_Sustain_Release_(ADSR)_envelope

# Instantiates a Wave plugin to generate a sine wave
# with 3 Hz.
p = ADSRPlugin()
p.setAttackTime(50)
p.setDecayTime(20)
p.setReleaseTime(50)
p.setSustainAmplitude(0.8)

# Adds the plugin to the wave generator
w.addPlugin( p )


# Generates the wave data for 1000 milliseconds.
# It returns a List with 10000(sampling rate * length) values
data = w.generate( 1000 )

# Raise all values by offset to have values between 0/255
for i in range(0,len(data)):
    data[i] = data[i]+offset

# Prints values between 0 and 255
print max(data)
print min(data)
```

# Example 3 - Writing a wave file 
In this example we write a wave file containing the generates wave.
So we can visualize the wave in an wave editor.(e.g. audacity)
see https://github.com/mlueft/WaveFile

```python
from WaveGenerator.WaveGenerator import WaveGenerator
from WaveGenerator.Plugins.SineWavePlugin import SineWavePlugin
from WaveGenerator.Plugins.ADSRPlugin import ADSRPlugin

from WaveFile import WaveFile

samplingRate = 22000
resolution   = 8        # 8 bit resolution for a simple wave file
channels     = 1
duration     = 800      # milli sec
frequency    = 440.0

# for 8 bit amplitude is 125
amplitude    = (2**(resolution-1)-1)

# offset is 128
# generate returnes values between -127/127
# we raise all values be 128 to get values
# between 0/255.
offset       = 2**(resolution-1)

# Instantiate the WaveGenerator class.
w = WaveGenerator()

# Sets the sampling rate.
# 10 Samples per second.
w.setSamplingRate(samplingRate)

# Sets the amplitude.
w.setAmplitude(amplitude)

# Instantiates a Wave plugin to generate a sine wave
# with 440 Hz.
p = SineWavePlugin( 440 )

# Adds the plugin to the wave generator
w.addPlugin( p )

# see https://en.wikipedia.org/wiki/Synthesizer#Attack_Decay_Sustain_Release_(ADSR)_envelope

# Instantiates a Wave plugin to generate a sine wave
# with 3 Hz.
p = ADSRPlugin()
p.setAttackTime(50)
p.setDecayTime(20)
p.setReleaseTime(50)
p.setSustainAmplitude(0.8)

# Adds the plugin to the wave generator
w.addPlugin( p )


# Generates the wave data for 1000 milliseconds.
# It returns a List with 10000(sampling rate * length) values
data = w.generate( 1000 )

# Raise all values by offset to have values between 0/255
for i in range(0,len(data)):
    data[i] = data[i]+offset

# see https://github.com/mlueft/WaveFile
#     project WaveFile
file = WaveFile.WaveFile(samplingRate,resolution,channels)
file.save( "sound.wav", data )
```

# Example 4 - Adding Tremolo
In this example we add tremolo to the wave using the tremolo plugin

```python
from WaveGenerator.WaveGenerator import WaveGenerator
from WaveGenerator.Plugins.SineWavePlugin import SineWavePlugin
from WaveGenerator.Plugins.ADSRPlugin import ADSRPlugin
from WaveGenerator.Plugins.TremoloPlugin import TremoloPlugin
from WaveFile import WaveFile

samplingRate = 22000
resolution   = 8        # 8 bit resolution for a simple wave file
channels     = 1
duration     = 800      # milli sec
frequency    = 440.0

# for 8 bit amplitude is 125
amplitude    = (2**(resolution-1)-1)

# offset is 128
# generate returnes values between -127/127
# we raise all values be 128 to get values
# between 0/255.
offset       = 2**(resolution-1)

# Instantiate the WaveGenerator class.
w = WaveGenerator()

# Sets the sampling rate.
# 10 Samples per second.
w.setSamplingRate(samplingRate)

# Sets the amplitude.
w.setAmplitude(amplitude)

# Instantiates a Wave plugin to generate a sine wave
# with 440 Hz.
p = SineWavePlugin( 440 )

# Adds the plugin to the wave generator
w.addPlugin( p )

# see https://de.wikipedia.org/wiki/Tremolo
# The first parameter is the frequency of the tremolo
# the second is the amplitude of the tremolo.
# In this case 15% of the total amplitude.
p = TremoloPlugin(4.2,0.15)
w.addPlugin( p )

# see https://en.wikipedia.org/wiki/Synthesizer#Attack_Decay_Sustain_Release_(ADSR)_envelope

# Instantiates a Wave plugin to generate a sine wave
# with 3 Hz.
p = ADSRPlugin()
p.setAttackTime(50)
p.setDecayTime(20)
p.setReleaseTime(50)
p.setSustainAmplitude(0.8)

# Adds the plugin to the wave generator
w.addPlugin( p )


# Generates the wave data for 1000 milliseconds.
# It returns a List with 10000(sampling rate * length) values
data = w.generate( 1000 )

# Raise all values by offset to have values between 0/255
for i in range(0,len(data)):
    data[i] = data[i]+offset

# see https://github.com/mlueft?tab=repositories
#     project WaveFile
file = WaveFile.WaveFile(samplingRate,resolution,channels)
file.save( "sound.wav", data )
```

# Waveforms
The WaveGenerator comes with plugins for the most common wave forms:
* SineWavePlugin
* TriangleWavePlugin
* SquareWavePlugin
* SawUpWavePlugin
* SawDownWavePlugin

Try to use TriangleWavePlugin instead of SineWavePlugin and watch the wave in your sound editor.
