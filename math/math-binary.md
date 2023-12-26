# Binary base

https://www.youtube.com/watch?v=rDDaEVcwIJM

## Divisibility

Given n represented in base b, shares a factor with:

- b: if the final digit shares a factor with b (considering 0 as b)
	- ie In Base10, numbers ending with 
		- 0, 2, 4, 6, 8 are divisible by 2
		- 0, 5 are divisible by 5
- b-1 if the digit sum shares a factor with b-1
	- ie In Base10, b-1 is 9, which has double 3 factors. if the sum of factors is divisible by 3, n is divisible by 3
- b+1 if the digit alternated sum (+-) shares a factor with b+1 (considering 0 has common factor)
	- ie In Base10, b+1 is 11, 539 is 5-3+9 = 11 wich has 11 factor 4664

- Grouping k digits you can do the trick with b^k
	- ie 19998 is 1:99:98 in 100b, 1-99+98=0 so is divisible by 101
	- ie 19998 is 1:99:98 in 100b, 1+99+98=189=2*99 so is divisible by 99

In binary:

- div 2: last bit 0
- div 3: sum of duets of bits (b^2-1)  or alternating sums of bits (b+1)
- div 4 (b 2^2): last two digit is 0
- div 5 (b^2+1): alternating sum of pairs of bits
- div 7 (b^3-1): sum of triplets of bits 
- div 8 (b^3): last 3 triplet is 000

Extending divisibility ops for arbitrary number k

- Compute  b^a mod k until the result repeats
	- ie. for 11: 1 2 4 8 5(16) 10(32) 9(64) 7(128) 3(256) 6(512) 1(1024) ...
- Bind each mod to each digit as weight
- Multiply each digit of the number by its weight
- If the result is itself divisible by k is divisible

Rationale:

	X = sum(xi*b^i)
	X mod k = sum(xi*b^i) mod k
	X mod k = sum((xi*b^i) mod k) mod k
	X mod k = sum(xi*(b^i mod k)) mod k

- At the end, each digit 1 contributes to the divisibility as much as the mod of its weight
- TODO: Why mod cycles on powers?
	- a^k % n = a%n a^k-1%n = 
- Former tests are specifics of this one (-1 is b-1)



## Division

1101 0101 / 100


Decimal:

- Find the upper digits which are greater than the divisor, group them as target
- The next result digit is the greater factor that multiplies the divisor below the grouped digits
- Multiply the digit by the divident and substract to the grouped digits
- Append to the substraction the next dividend digit and let be that the next target, repeat

Binary

Same but because the factor is always 1 or 0,
each step is just a matter of whether we can substract or not the divider

- Pull down one digit from the divisor to the reminder
- Can we substract the divider from it?
	- If we can substract it, do it, 1 to the output
	- If we cannot substract, don't, 0 to the output
- In any case pull down the next digit, and loop
- When we came out of digits, the reminder is the integer reminder
- To get decimals, pulldown zeroes and continue until you get a reminder you got before after running out of ones
	- The results between repetitions stablishes the decimal (binarial?) period
	- A zero reminder is a direct stop, because without ones, then next one will be zero as well.

Example:

	 11001101010 (1642) / 10010 (18) = 1011011.r001110
	-10010
	 0011110
	  -10010
	   011001
	   -10010
	    0011101
	     -10010
	      010110
	      -10010
	       00100  <- integer remainder 100
	       00100000
	         -10010
	          011100
	          -10010
	           010100
	           -10010
	            000100 <-Repeated

## Square root

	Xk = sum[i=0..k] (xi b^i)
	Xk² = sum[i=0..k] (xi b^i)^2
	Xk² = xk²*bk² + 2*xi*bk*Xk-1 + Xk-1²
	Xk² = xk²*bk² + 2*xi*bk*Xk-1 + Xk-1²

	Given that k-j terms have been computed

	Xk² = 
	

Decimal:

- Group radicant digits in pairs from less significant to most, now, proceed from pairs from most significant
- Find digit whose square is less or equal the pair
- Substract the square pair
- pull the next pair to the right side of the substraction
- Annotate the obtained digits multipled by 2
- Guess digit that appended to the annotated number and multiplying (s*10+d)*d is just bellow the substraction
- This will be next digit of the result
- Substract the

Example

	2  6  8  9  0
	7.23.45.26
	4   (2*2)
	3 23
	2 76 (2*20 +9)*9 = 276
	  47 45
	  42 24  (20*26+8)*8 = 4224
	   5 21 26
	   4 83 21 (20*268+9)*9 = 48321
	     38 05 00
		 37 65 09 = (2689*20+7)*7
	        39 81 00
            00 00 00 = (26897*20+0)*0
			39 81 00 00
            00 00 00 00 = (268970*20+0)*0

	2689,707419032...

Binary

- Group bits in pairs from the decimal point (complement pairs with zeros at extremes)
- initialize the remainder to zero
- from most significant, pull down two digits from the radicand to the reminder right hand of the reminder
- build the substraction, by appending 01 on the right to the already computed digits
- if the substraction is over the reminder, next digit is 0, keep the reminder for the next iteration
- if the substraction fits the reminder, next digit is 1, substract to get the reminder for the next iteration

Example

	01 10 00 11 10 01 01.00 00 00  (6373)
	01
	01 -> 1
	00 10
	01 01 -> 0
	00 10 00
	   10 01 -> 0
	   10 00 11
		1 00 01 -> 1
		1 00 10 10
		  10 01 01 -> 1
		  10 01 01 01
		  01 00 11 01 -> 1
		  01 00 10 00 01
			 10 01 11 01 -> 1.
			 10 00 01 00 00
			  1 00 11 11 01 -> .1
				11 01 00 11 00
				10 01 11 11 01 -> 1
				00 11 00 11 11 00
				 1 00 11 11 11 01 -> 0
				   11 00 11 11 00 00
					1 00 11 11 10 01 -> 1
					1 11 11 11 01 11 00
	1 00 11 11.11 01 (79.8125<79.83107164506812)


