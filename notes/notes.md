# Helpful notes for development


[mp4-container](https://www.ramugedia.com/mp4-container)

[hex editor](https://www.sweetscape.com/010editor/)

[file reverse engineering tutorial](https://www.youtube.com/playlist?list=PLCJoIC7hiEqY0_2pnJnbEirf780dgeiT-)


GP.. tag possibilities

more common

b'\x47\x50\x04\x00'
b'\x47\x50\x10\x03'
b'\x47\x50\x00\x03'
b'\x47\x50\x1B\x00'



b'\x47\x50\x00\x02'
b'\x47\x50\x10\x02'

SI encoding
As the SIUN is declared as an ASCII the character for degrees, squared, cubed and micro use the single byte values: 0xB0 (°), 0xB2 (²), 0xB3 (³) and 0xB5 (µ).