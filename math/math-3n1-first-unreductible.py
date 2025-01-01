# To be demonstrated hypothesis for this script:
# Given a number n and their 
# If the kth lower bits of a number after fk(n
from dataclasses import dataclass, field
import sympy as sp
from collections import namedtuple
from functools import cached_property

n = sp.symbols("n", positive=True, integer=True)

def fk1_odd(fk):
	return (sp.Rational(1,2) * (3*fk + 1 )).simplify()

def fk1_even(fk):
	return (sp.Rational(1, 2) * fk).simplify()

@dataclass
class Solution:
	expression: sp.Expr = n
	lowerbits: int = 0
	ups: int = 0
	nbits: int = 0
	viability_condition: sp.Expr = field(init=False)
	is_viable: bool = field(init=False)

	def __post_init__(self):
		self.viability_condition = (self.expression >= n)
		complemented_viability = self.viability_condition & (n >= max(self.lowerbits, 2))
		self.is_viable = complemented_viability.simplify() is not sp.false

	def __str__(self):
		return (
			f"{'\033[32;1m' if self.is_viable else '\033[31;1m'}"
			f"{self.lowerbits:0{self.nbits or 1}b}: "
			f"{self.ups:0{self.nbits or 1}b} "
			f"f{self.nbits} = {self.expression} "
			f"viability: {self.viability_condition} --> {self.is_viable}"
			f"\033[0m"
		)

	def expand(self, bitValue):
		assert not (bitValue >> 1), "Bit value should be 0 or 1"

		lowerbits = self.lowerbits | (bitValue<<self.nbits)
		fk = int(round(self.expression.subs(n, lowerbits).evalf()))
		fk1 = fk1_odd if fk & 1 else fk1_even
		newExpression = fk1(self.expression)
		return Solution(
			nbits = self.nbits + 1,
			expression = fk1(self.expression),
			lowerbits = lowerbits,
			ups = self.ups | ((fk & 1) << self.nbits),
		)
"""
Para que n sea reducible:

fk(n) = (3^Ak *n + Rk) / 2^k >= n
Se da que (empiricamente, demostrar)
	Ak <= k
	0 <= Rk= < 3^Ak-1
Por construccion Rk hace que 3^Ak*n sea divisible por 2^k

2^k n <= 3^Ak * n + Rk
(3^Ak - 2^k) n + Rk >= 0

2 -> 1 for 0 bits
2 -> 2 for 1 bits
4 -> 3 for 2 bits
6 -> 5 for 3 bits
10 -> 6 for 4 bits
12 -> 12 for 5 bits
24 -> 18 for 6 bits
36 -> 26 for 7 bits
52 -> 50 for 8 bits
100 -> 82 for 9 bits
164 -> 163 for 10 bits
326 -> 285 for 11 bits
570 -> 458 for 12 bits
916 -> 915 for 13 bits
1830 -> 1607 for 14 bits
3214 -> 2608 for 15 bits

2 -> 1 for 0 bits
2 -> 1 for 1 bits
2 -> 2 for 2 bits
4 -> 3 for 3 bits
6 -> 4 for 4 bits
8 -> 8 for 5 bits
16 -> 13 for 6 bits
26 -> 19 for 7 bits
38 -> 38 for 8 bits
76 -> 64 for 9 bits
128 -> 128 for 10 bits
256 -> 226 for 11 bits
452 -> 367 for 12 bits
734 -> 734 for 13 bits
1468 -> 1295 for 14 bits
2590 -> 2114 for 15 bits




"""


print((
	fk1_odd(fk1_odd(n))
))

print("eval", (
	fk1_odd(fk1_odd(n))
).subs(n, 12))

print("solved:", (fk1_even(fk1_even(fk1_odd(fk1_odd(n)))) >= n).simplify())

print(type(fk1_odd(n)))

def printSolutions(solutions):
	for s in solutions:
		print(s)

solutions=[Solution()]
for bit in range(0, 32):
	print(f"## Bit {bit}")
	next_solutions = []
	for solution in solutions:
		next_solutions.append(solution.expand(1))
		next_solutions.append(solution.expand(0))
	printSolutions(next_solutions)
	solutions = list(filter(lambda s: s.is_viable, next_solutions))

	print(f"{len(next_solutions)} -> {len(solutions)} for {bit+1} bits ratio: x{2**(bit+1) /len(solutions):.2f}")


