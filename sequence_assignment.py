import random

# Homework on Comments included
# I used the random integer function to pull a number for the coefficients 'a' and 'b' then assigned those random integers to 'c' and 'd' respectively. The answer requires the products of variable pairs so I assigned 'u' and 'v' accordingly.

# A sequence of assignments to generate a random problem :
a = random.randint(1, 10)	# Return a random integer N such that 1 <= N <= 10.
b = random.randint(2, 6)	# Return a random integer N such that 2 <= N <= 12.
c = a	# The middle term must cancel for the answer to be correct.
d = b	# Same reason
u = a * c	# For the answer to be correct for every version of the problem, the product of 'a' and 'c' must be the coefficient 'u'.
v = b * d	# Same reason

print ('Problem : ({a}x + {b}) * ({c}x - {d}) = ?'. format (a = a , b = b , c = c , d = d))
print ('Answer : {u}x^2 + {v}'. format (u = u , v = v))