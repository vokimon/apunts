a x^2 + b x + c = 0

Instead of solving it by the formula, here there is a rememberable procedure:

1. Divide the equation by `a`
   - this will lead to  `x² + b' x + c' = 0` where `b' = b/a` and `c' = c/a`
2. Consider the roots are equidistant to a central point m: (m+d) and (m-d) m+-d
   - Then `x² + b' x  + c = 0 = (x -m -d)(x -m +d) = x² -2mx + (m² - d²)`
   - Then `m = -b'/2` and `d² = m²-c`

Other way:
`m` is also the `x` for the maxima/minima of the cuadratic,
so `f'(x) = 2x + b'; f'(m) = 0; m = -b'/2`

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
  = m +- sqrt(m²-c')                 # d²=m²-c'
  = -b'/2 +- sqrt(b'²/4 - c')        # m = -b/2
  = -b/2a +- sqrt(b²/4a² - c/a)      # b' = b/a; c'=c/a
  = -b/2a +- sqrt(b²/4a² - 4ac/4a²)  # multipy and divide c/a by 4a
  = -b/2a +- sqrt(b² - 4ac)/2a       # extract 1/4a² out of the sqrt as 1/2a
  = (-b +- sqrt(b² - 4ac))/2a        # common divisor 2a
```




