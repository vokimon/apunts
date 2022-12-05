import sympy as s

(
    N0,N1,N2,N3,N4,N5,N6,N7,N8,
    n0,n1,n2,n3,n4,n5,n6,n7,n8,
)=s.symbols(
    "N0,N1,N2,N3,N4,N5,N6,N7,N8," # Nk: N right shifted k times
    "n0,n1,n2,n3,n4,n5,n6,n7,n8," # nk: kth bit of N
)

def truth(f, symbols, values=[]):
    if not symbols:
        print(''.join((str(x) for x in values)), f.expand().simplify())
        return
    for val in (0,1):
        truth(f.subs(symbols[0], val), symbols[1:], values+[val])

def result(f, variables):
    print(f"f{len(variables)} results:")
    truth(f, variables)
    print()

def oddity(f, variables, factors=1, values=[]):
    if not variables:
        #print("oddity", values, f, f%2)
        return (factors if f%2 else s.Number(0))
    result = 0
    for val in (0,1):
        result += oddity(
            f.subs(variables[0], val),
            variables[1:],
            factors * (variables[0] if val else 1-variables[0]),
            values+[val],
        )
    return result

generations=6


Ns = s.symbols([f'N{i}' for i in range(generations+1)])
ns = s.symbols([f'n{i}' for i in range(generations+1)])
f = Ns[0]
[n0,n1,n2,n3,n4,n5,n6] = ns
fs = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    Ns[0] * 1
        + 0,
    Ns[1] * (2*n0 + 2)
        + 2*n0,
    Ns[2] * (4*n0*n1 + 2*n0 + 2*n1 + 1)
        + 5*n0*n1 + n0 + 2*n1,
    Ns[3] * (20*n0*n1*n2 - 2*n0*n1 - 8*n0*n2 + 8*n0 + 4*n1*n2 + 2*n1 + 2*n2 + 1)
        + 17*n0*n1*n2 + n0*n1 - 2*n0*n2 + 2*n0 + 5*n1*n2 + n1 + 2*n2,
    Ns[4] * (
        28*n0*n1*n2*n3 + 26*n0*n1*n2 + 8*n0*n1*n3 - 8*n0*n1 - 16*n0*n2*n3 - 8*n0*n2 + 16*n0*n3 + 8*n0 + 20*n1*n2*n3 - 2*n1*n2
        - 8*n1*n3 + 8*n1 + 4*n2*n3 + 2*n2 + 2*n3 + 1
    )   
        + 41*n0*n1*n2*n3 + 10*n0*n1*n2 + 4*n0*n1*n3 - n0*n1 - 14*n0*n2*n3 - n0*n2 + 14*n0*n3 + n0 + 17*n1*n2*n3 + n1*n2
        - 2*n1*n3 + 2*n1 + 5*n2*n3 + n2 + 2*n3,

    Ns[5] * (
        + 92*n0*n1*n2*n3*n4 + 10*n0*n1*n2*n3 - 92*n0*n1*n2*n4 + 98*n0*n1*n2 + 88*n0*n1*n3*n4 - 28*n0*n1*n3 + 20*n0*n1*n4
        - 26*n0*n1 + 40*n0*n2*n3*n4 - 52*n0*n2*n3 + 20*n0*n2*n4 - 26*n0*n2 - 40*n0*n3*n4 + 52*n0*n3 - 20*n0*n4 + 26*n0
        + 28*n1*n2*n3*n4 + 26*n1*n2*n3 + 8*n1*n2*n4 - 8*n1*n2 - 16*n1*n3*n4 - 8*n1*n3 + 16*n1*n4 + 8*n1 + 20*n2*n3*n4
        - 2*n2*n3 - 8*n2*n4 + 8*n2 + 4*n3*n4 + 2*n3 + 2*n4 + 1
        )
        + 87*n0*n1*n2*n3*n4 + 23*n0*n1*n2*n3 - 17*n0*n1*n2*n4 + 20*n0*n1*n2 + 66*n0*n1*n3*n4 - 14*n0*n1*n3 - n0*n1*n4
        - 2*n0*n1 + 12*n0*n2*n3*n4 - 23*n0*n2*n3 - n0*n2*n4 - 2*n0*n2 - 12*n0*n3*n4 + 23*n0*n3 + n0*n4 + 2*n0 + 41*n1*n2*n3*n4
        + 10*n1*n2*n3 + 4*n1*n2*n4 - n1*n2 - 14*n1*n3*n4 - n1*n3 + 14*n1*n4 + n1 + 17*n2*n3*n4 + n2*n3 - 2*n2*n4 + 2*n2
        + 5*n3*n4 + n3 + 2*n4,
    Ns[6] * (
        436*n0*n1*n2*n3*n4*n5 - 34*n0*n1*n2*n3*n4 + 128*n0*n1*n2*n3*n5 - 44*n0*n1*n2*n3 - 220*n0*n1*n2*n4*n5
        - 74*n0*n1*n2*n4 + 196*n0*n1*n2*n5 + 98*n0*n1*n2 - 184*n0*n1*n3*n4*n5 + 268*n0*n1*n3*n4 - 56*n0*n1*n3*n5
        - 28*n0*n1*n3 + 76*n0*n1*n4*n5 + 2*n0*n1*n4 - 52*n0*n1*n5 - 26*n0*n1 + 56*n0*n2*n3*n4*n5 + 52*n0*n2*n3*n4
        - 116*n0*n2*n3*n5 - 46*n0*n2*n3 + 76*n0*n2*n4*n5 + 2*n0*n2*n4 - 52*n0*n2*n5 - 26*n0*n2 - 56*n0*n3*n4*n5
        - 52*n0*n3*n4 + 116*n0*n3*n5 + 46*n0*n3 - 76*n0*n4*n5 - 2*n0*n4 + 52*n0*n5 + 26*n0 + 92*n1*n2*n3*n4*n5
        + 10*n1*n2*n3*n4 - 92*n1*n2*n3*n5 + 98*n1*n2*n3 + 88*n1*n2*n4*n5 - 28*n1*n2*n4 + 20*n1*n2*n5 - 26*n1*n2
        + 40*n1*n3*n4*n5 - 52*n1*n3*n4 + 20*n1*n3*n5 - 26*n1*n3 - 40*n1*n4*n5 + 52*n1*n4 - 20*n1*n5 + 26*n1
        + 28*n2*n3*n4*n5 + 26*n2*n3*n4 + 8*n2*n3*n5 - 8*n2*n3 - 16*n2*n4*n5 - 8*n2*n4 + 16*n2*n5 + 8*n2 
        + 20*n3*n4*n5 - 2*n3*n4 - 8*n3*n5 + 8*n3 + 4*n4*n5 + 2*n4 + 2*n5 + 1
    )
    + 415*n0*n1*n2*n3*n4*n5 - 20*n0*n1*n2*n3*n4 + 92*n0*n1*n2*n3*n5 - 2*n0*n1*n2*n3 - 175*n0*n1*n2*n4*n5
    - 3*n0*n1*n2*n4 + 167*n0*n1*n2*n5 + 10*n0*n1*n2 - 46*n0*n1*n3*n4*n5 + 110*n0*n1*n3*n4 - 56*n0*n1*n3*n5
    - 7*n0*n1*n3 + 49*n0*n1*n4*n5 - 6*n0*n1*n4 - 41*n0*n1*n5 - n0*n1 + 58*n0*n2*n3*n4*n5 + 10*n0*n2*n3*n4
    - 107*n0*n2*n3*n5 - 10*n0*n2*n3 + 49*n0*n2*n4*n5 - 6*n0*n2*n4 - 41*n0*n2*n5 - n0*n2 - 58*n0*n3*n4*n5
    - 10*n0*n3*n4 + 107*n0*n3*n5 + 10*n0*n3 - 49*n0*n4*n5 + 6*n0*n4 + 41*n0*n5 + n0 + 87*n1*n2*n3*n4*n5
    + 23*n1*n2*n3*n4 - 17*n1*n2*n3*n5 + 20*n1*n2*n3 + 66*n1*n2*n4*n5 - 14*n1*n2*n4 - n1*n2*n5 - 2*n1*n2
    + 12*n1*n3*n4*n5 - 23*n1*n3*n4 - n1*n3*n5 - 2*n1*n3 - 12*n1*n4*n5 + 23*n1*n4 + n1*n5 + 2*n1
    + 41*n2*n3*n4*n5 + 10*n2*n3*n4 + 4*n2*n3*n5 - n2*n3 - 14*n2*n4*n5 - n2*n4 + 14*n2*n5
    + n2 + 17*n3*n4*n5 + n3*n4 - 2*n3*n5 + 2*n3 + 5*n4*n5 + n4 + 2*n5,
    None,
    None,
]
print()
for i in range(generations):
    f = f.subs(Ns[i], 2*Ns[i+1] + ns[i])
    print(f"f{i}:", f.expand().simplify(), "   # Nk = 2*Nk+1 + nk")
    bits = ns[i::-1]
    oddityi = oddity(f.subs(Ns[i+1],0), bits)
    print(f"oddity:", oddityi)
    oddityi = oddityi.expand().simplify()
    print(f"oddity {i}:", oddityi)
    truth(oddityi, bits)
    print()

    f = (f*(1+2*oddityi) + oddityi)/2
    print(f"f{i+1}:", f.expand().simplify())
    #print(f.as_poly(Ns[i+1]))
    if fs[i+1] is not None:
        f = fs[i+1]
        print("Simplified")
        print(f"f{i+1}:", f.expand().simplify(), "    # Simplifying nk**2=nk")
        #print(f.as_poly(Ns[i+1]))
    result(f, bits)
    print()




result=0
bit = 1

def compose_trinomials(f, g):
    """
    f(x)=(a1x+b1)/c1.
    g(x)=(a2x+b2)/c2.
    f(g(x)) = (a1((a2x+b2)/c2)+b1)/c1.
    f(g(x)) = (a1*a2*x +a1*b2 + b1*c2)/(c1*c2)
    """
    a1,b1,c1 = f
    a2,b2,c2 = g
    return a1*a2, a1*b2 + c2*b1, c1*c2

def discardable(a, b, c):
    """
    (ax + b)/c<x
    ax +b < cx
    (c-a)x > b
    x > b/(c-a)
    """









