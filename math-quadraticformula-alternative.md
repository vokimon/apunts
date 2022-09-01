a x^2 + b x + c = 0

Instead of solving it by the formula, here there is a rememberable procedure:

1. Divide the equation by a
   - this will lead to  `x² + b' x + c' = 0` where `b' = b/a` and `c' = c/a`
2. Consider the roots are equidistant to a central point m: (m+d) and (m-d) m+-d
   - Then `x² + b' x  + c = 0 = (x -m -d)(x -m +d) = x² -2mx + (m² - d²)
   - Then `m = -b'/2` and `d² = m²-c`

Example with two real solutions:
```
2x² - 22x - 28 = 0
x² - 11x - 14 = 0
m = -b'/2 = 11/2
d² = m²-c' = 11²/4 - 28 = (121 - 112) / 4 = 9 / 4
d = 3 / 2
x = 11/2 +- 3/2 = 4, 7
```

Example with imaginary solutions

```
3x² -5x +4 = 0
x² - 5/3 + 4/3 = 0
m = 5/6
d² = 25/36 - 4/3 = 25/36 - 48/36 = -23/36
d = +- i sqrt(23) / 6
x =  5/6 +- i sqrt(23)/6
```

Example with single solution (d=0)

```
4x² + 20x + 25 = 0
x² + 5x + 25/4 = 0
m = -5/2
d² = m² -c = 25/4 - 25/4 = 0
x = d +-c = -5/2
```

Deducing the classic formula

```
x = m +- d
  = -b'/2 +-sqrt(m²-c`)
  = (-b' +-2*sqrt(m²-c`)/2
  = (-b' +-2*sqrt((-b'/2)²-c`)/2
  = (-b' +-2*sqrt((b'²/4 -c`)/2
  = (-b' +-sqrt((b'² -4c`)/2
  = (-b/a +-sqrt((b'²/a² -4c/a)/2

```




