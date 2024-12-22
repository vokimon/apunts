def step(msg):
	print(f"\033]33;1m{msg}\033]0m")


def edge(n, nbits, carry):
	origin = f"{n:0{nbits}b}"
	shifted = f"{n>>1:0{nbits}b}"
	result = f"{n + (n>>1) + carry:0{nbits+1}b}"
	up = result[0] == "1"
	target = result[:nbits] if up else result[-nbits:]
	print(f"# {origin} + {shifted} + {carry} = {result}")
	print(f"{origin} -> {target} [label=\"{carry}\"{'color="red"' if up else ''} ]")
	

#step("What happens to the upper bits when odd")
for nbits in range(2,8):
	for a in range(1<<(nbits-1),1<<(nbits)):
		edge(a, nbits, carry=0)
		edge(a, nbits, carry=1)


