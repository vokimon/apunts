import sys

def collatz_single_branch_factor(n):
    while n!=1:
        yield n
        ok = n&1
        n = (n + (2*n+1)*ok)//2

def collatz_single_branch_exp(n):
    while n!=1:
        yield n
        ok = n&1
        n = (3**ok*n + ok)//2

def collatz_additive(n):
    while n!=1:
        yield n
        if n&1:
            n += (n+1)//2
        else:
            n -= n//2

def collatz_skip(n):
    while n!=1:
        yield n
        if n&1:
            n = (n*3+1)//2
        else:
            n = n//2

def collatz_binary(n):
    while n!=1:
        yield n
        jump = (n>>1) + (n&1)
        if n&1:
            n += jump
        else:
            n -= jump


n = int(sys.argv[1])
for collatz in [
    collatz_single_branch_factor,
    collatz_single_branch_exp,
    collatz_skip,
    collatz_additive,
    collatz_binary,
]:
    print(list(collatz(n)))

def collatz_rhythm(n):
    series = list(collatz(n))
    return ''.join(('1' if a>b else '·' for a,b in zip(series[1:],series) ))

def bits(n):
    return ''.join(('1' if n &(1<<k) else '0' for k in range(0,32)))

print(collatz_rhythm(n))
print(bits(n))
print(collatz_rhythm(n+(1<<20)))
print(bits(n+(1<<20)))



