480HW4
======
#1)

m=list(primes(0,10^7))
n = []
for i in m:
    n.append(i%15)
stats.TimeSeries(n).plot_histogram()
#Gives a uniform distribution of numbers among (1, 2, 4, 7, 8, 11, 13, 14)



#2)

"""Conjecture: Primes up to 10^7 modulo n (where n is any number), gives a uniform distribution of the numbers
within the distribution"""



#3)

#primes mod 22 (I chose this number because it's different from 15 in the sense that it's even)
m=list(primes(0,10^7))
n = []
for i in m:
    n.append(i%22)
stats.TimeSeries(n).plot_histogram()
#Gives a uniform distribution of numbers among (1,3,5,7,9,13,15,17,19,21)


#primes mod 7 (I chose this number because it's different from both 15 and 22 in the sense that it's prime)
m=list(primes(0,10^7))
n = []
for i in m:
    n.append(i%7)
stats.TimeSeries(n).plot_histogram()
#Gives a uniform distribution of numbers among (1,2,3,4,5,6) with the exception of 0 occuring once (for the prime in the list "m" which equals 7).


#primes mod 193
m=list(primes(0,10^7))
n = []
for i in m:
    n.append(i%193)
stats.TimeSeries(n).plot_histogram()
#This does NOT output a uniform distribution. Therefore my conjecture in number 2 is incorrect.


#New conjecture (Taken from Dirichlet's Theorem): There are infinitely many primes which are congruent to a modulo b (where a,b are any co-prime positive integers)
