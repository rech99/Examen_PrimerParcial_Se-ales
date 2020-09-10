import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import play_wave
from thinkdsp import read_wave



frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia941 = SinSignal(freq=941, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=941, amp=1, offset=0)


wave_852 = frecuencia852.make_wave(duration=0.5, start=0, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0, framerate=44100)

wave_770 = frecuencia770.make_wave(duration=0.5, start=.5, framerate=44100)
wave_1209_1 = frecuencia1209.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_1477 = frecuencia1477.make_wave(duration=0.5, start=1, framerate=44100)
wave_852_1 = frecuencia852.make_wave(duration=0.5, start=1, framerate=44100)

wave_941 = frecuencia941.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido_7 = wave_852 + wave_1209 

wave_sonido_4 = wave_770 + wave_1209_1

wave_sonido_9 = wave_852_1 + wave_1477

wave_sonido_0 = wave_941 + wave_1336

wave_sonido_final = wave_sonido_7 + wave_sonido_4 + wave_sonido_9 + wave_sonido_0

wave_sonido_final.write("output.wav")
