"""
In order for a quadratic of the form f(x)=x^2+ax+b (a,b integers) to produce a set of infinitely many primes,
f(n) must output an infinitely large set with at least half of the elements within the set to be odd.
The statement "at least half of the elements within the set to be odd" is rationalized by the acknowledgement of f(n)
to alternate between even/odd outputs for specific a,b. Therefore, the only case where the set of the values of f(n)
does not produce a set of infinitely many primes is where the output of f(n) is even for a given a,b.
Therefore, we now consider 4 cases of a,b where a =/= b =/= 0

For convenience, let A = {f(n)}

1. Even a, Even b:
Even input(n)
  f(n) = even + even + even = even
Odd input(n)
  f(n) = odd + even + even = odd
A is alternating between even and odd which means A has infinitely many odd values
and hence, infinitely many primes.

2. Even a, Odd b:
Even input(n)
  f(n) = even + even + even = even
Odd input(n)
  f(n) = odd + even + odd = even
A does not contain infinitely many odd and therefore, does not contain infinitely many primes

3. Odd a, Even b:
Even input(n)
  f(n) = even + even + even = even
Odd input(n)
  f(n) = odd + odd + even = even
A does not contain infinitely many odd and therefore, does not contain infinitely many primes

4. Odd a, Odd b:
Even input(n)
  f(n) = even + even + odd = odd
Odd input(n)
  f(n) = odd + odd + odd = odd
A is alternating between even and odd which means A has infinitely many odd values
and hence, infinitely many primes.

Now we must consider if a and/or b = 0 which results in 3 cases:

1. a=b=0:
f(x) = x^2
x is a factor of x^2 and hence, for all x, f(x) is factorable and therefore, not prime.

2. a=0, b =/= 0:
f(x) = x^2 + b
We must consider two cases for b (even/odd):
  1. Even b:
    Even input(n)
     f(n) = even + even = even
    Odd input(n)
      f(n) = odd + even = odd
    A is alternating
  2. Odd b:
    Even input(n)
      f(n) = even + odd = odd
    Odd input(n)
      f(n) = odd + odd = even
    A is alternating
Therefore, if b is any integer, A will result with infinitely many odds and hence, infinitely many primes.

3. a =/= 0, b=0:
f(x) = x^2 + ax
We must consider two cases for a (even/odd):
  1. Even a:
    Even input:
      f(n) = even + even = even
    Odd input:
      f(n) = odd + even = odd
  A is alternating
  2. Odd a:
    Even input:
      f(n) = even + even = even
    Odd input:
      f(n) = odd + odd = even
  A contains a finite number of odds
Therefore, if b = 0 and a =/= 0, we must restrict a to be even in order to produce a set, A, with infinitely many primes.

In conclusion:
Conjecture:
If a =/= b =/= 0:
  a and b must be odd or
  a and b must be even
If a=0, b =/= 0:
  b can be any integer
If a =/= 0, b=0:
  a must be restricted to even integers 

