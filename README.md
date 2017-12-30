# WaveGenerator
A Python wave generator with plugin system.

```python

from.WaveGenerator.WaveGenerator import WaveGenerator
from WaveGenerator.Plugins.WaveGeneratorPlugin import WaveGeneratorPlugin
from WaveGenerator.Plugins.ADSRPlugin import ADSRPlugin
from WaveGenerator.Plugins.TremoloPlugin import TremoloPlugin
from WaveGenerator.Plugins.WavePlugin import WavePlugin

w = WaveGenerator()
w.setSamplingRate(10)

p = WavePlugin( WavePlugin.WF_SINUS, 3 )

wg.addPlugin( p )

data = w.generate( 1000 )

```