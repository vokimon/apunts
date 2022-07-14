## Units

Absolute lengths:

- cm: centimeters
- mm: milimeters 0.1cm
- Q: quarter milimeters 0.025cm
- in: inches 2.54cm
- px: pixels 1/96in 1/243.8cm (cannonical unit)
  - Not a device pixel! At the time of the standard, monitors where 96 DPI in 1024x798
  - Distance to the screen also counts.
    - Reference pixel, defined by the angle at arm length distance 71cmi s .26mm
    - Thus, closer screens (mobiles) have smaller px and further screens (tv's, projectors) have wider px
  - in screens also the distance to the screen counts, so it is the angle compared to that size at the arm distance
- pt: points 1/72in 1/182.88cm 1.333px
  - often used for absolute font sizes
- pc: picas 1/6in 16px 4.2mm

Font relatives:

- ch: advance measure of a '0' zero of the current typeface. The advance measure of the font is the spacing with the next letter (text orientation is taken into account)
- ex: height of an 'x' of the current typeface (or the parent if it is used to change font-size).  Used to compute interline spacings and margins
- em: width of an 'm' of the current typeface  (or the parent if it is used to change font-size)
  - being m the wider letter, ensures that at least those letters will be in
  - matches the font size (a 10pt font size, 1em is 3.5mm)
- rem: root em, em of the root element, not the current or the parent (Takes into account user's and system preferences)

Parent relative lengths:

- %: percent relative to the parent's size

Viewport relative lengths:

- vw: percent relative to the view port width
- vh: percent relative to the view port height
- vmin: percent relative to the view port min axis (height or width)
- vmax: percent relative to the view port max axis (height or width)

Angles:

- turn: full turn
- deg: degrees 360 per turn (canonical unit)
- grad: gradians 400 per turn
- rad: radians 2pi per turn

Rotations are clockwise

When stating a direction 0 is north and 90deg is right/east

Time

- s: seconds
- ms: miliseconds

Frequency

- Hz: 1/s
- kHz: 1000/s


Resolution:

The size of a real pixel (dot) in the device

dpi: dots per inch
dpcm: dots per cm
dppx: dots per pixel unit



