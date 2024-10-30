"""
Choose two large prime numbers p and q.
To make factoring harder, p and q should be chosen at random, be both large and have a large difference.[1] For choosing them the standard method is to choose random integers and use a primality test until two primes are found.
p and q should be kept secret.
Compute n = pq.
n is used as the modulus for both the public and private keys. Its length, usually expressed in bits, is the key length.
n is released as part of the public key.
Compute λ(n), where λ is Carmichael's totient function. Since n = pq, λ(n) = lcm(λ(p), λ(q)), and since p and q are prime, λ(p) = φ(p) = p − 1, and likewise λ(q) = q − 1. Hence λ(n) = lcm(p − 1, q − 1).
The lcm may be calculated through the Euclidean algorithm, since lcm(a, b) = ⁠
|ab|
/
gcd(a, b)
⁠.
λ(n) is kept secret.
Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime.
e having a short bit-length and small Hamming weight results in more efficient encryption – the most commonly chosen value for e is 216 + 1 = 65537. The smallest (and fastest) possible value for e is 3, but such a small value for e has been shown to be less secure in some settings.[15]
e is released as part of the public key.
Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n).
This means: solve for d the equation de ≡ 1 (mod λ(n)); d can be computed efficiently by using the extended Euclidean algorithm, since, thanks to e and λ(n) being coprime, said equation is a form of Bézout's identity, where d is one of the coefficients.
d is kept secret as the private key exponent.


"""
from functools import cache

@cache
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a


    while b != 0:
        a, b = b, a % b
    return a

@cache
def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False        
    return True



def nthPrime(n):

    count =0 
    i=0
    while count<n:
        i+=1
        if isPrime(i):
            count+=1
    return i

# print(nthPrime(10))

def roots(mod):
    ans=[]
    hits={hit for hit in range(1,mod) if gcd2(hit,mod)==1} # all numbers up to mod and have a divisor of 1 (coprime)

    for i in range(2,mod):

        if not isPrime(i): # also has to be prime for other req
            continue

        # actual_set = set( i** power % mod for power in range (1, mod))
        # if actual_set == hits:
        #     ans.append(i)  

        # or 

        if hits == {pow(i, powers, mod) for powers in range(1, mod)}:
            ans.append(i)

    return ans


# def primRoots(modulo):
#     coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
#     return [g for g in range(1, modulo) if isPrime2(g) and coprime_set == {pow(g, powers, modulo)
#             for powers in range(1, modulo)}]



# import time

# start = time.time()
# prime=nthPrime(200)
# print(time.time()-start)
# print(prime)

# start = time.time()
# root=roots(prime)
# print(time.time()-start)
# print(root)

# start = time.time()
# root=primRoots(prime)
# print(time.time()-start)
# print(root)

def lcm(a,b):
    return abs(a*b) // gcd(a,b)

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1



import random

minumum=100
maxumum=1000

class host():
    def __init__(self):
        # self.p = nthPrime(random.randint(minumum,maxumum)) #secret
        # self.q = nthPrime(random.randint(minumum,maxumum)) #secret
        self.p = nthPrime(100) #secret
        self.q = nthPrime(101) #secret
        # self.p = 61 #secret
        # self.q = 53 #secret

        self.n = self.p * self.q #public
        # print(self.n)

        self.lam = lcm(self.p-1,self.q-1) # = lamda(n) secret
        # print(self.lam)

        # self.e = 65537 # public
        self.e = 17 # public
        # print(self.e)

        # self.d = pow(self.e, -1, self.lam) # private key exponent
        self.d = modinv(self.e,self.lam)
        # this is not e**-1 %lam it is the "modular multiplicative inverse"
        
        print(self.d)


        self.public_key = (self.n,self.e)
        self.private_key = self.d

    def getPublic(self):
        return self.public_key

    def decrypt(self,enc):
        """
        Decryption
        Alice can recover m from c by using her private key exponent d by computing

        c**d = (m**e)**d = m %n

        Given m, she can recover the original message M by reversing the padding scheme.

        """
        # # print(enc,self.d)
        # m=enc ** self.d
        # print("pow int", m)
        # m = m % self.n
        # print("decrypted int",m)

        # print(self.d,self.e,self.n)
        # print(2790**413 %3233)
        # print(2790**self.d %self.n)

        decoded=enc**self.d %self.n
        # breaks on n, because it will loop

        print("out",decoded)
        return decoded

        # m=pow(enc, self.d,self.e)
        # # print("pow int", m)
        # # m = m % self.n
        # print("decrypted int",m)

        # b=m.to_bytes((m.bit_length() + 7) // 8, 'big')
        # message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()

        # print("decrypted bytes", b)
        # print("decoded bytes",b.decode())
        # print( c ** self.d % self.n )

if __name__ == "__main__":

    host1 = host()
    
    n,e=host1.getPublic()
    print(n,e)
    #encryption
    message = 'Ab' #

    byte_message = bytes(message, 'utf-8')
    print("bytes",byte_message)

    int_message=int.from_bytes(byte_message, 'big')

    ##### the int of the message has to be less than n

    if int_message > n:
        print("message too large",int_message,n)
        exit()


    # for int_message in range(1000,10000):
    
    print("int",int_message)


    c = (int_message **e) % n
    # print("encrypted int",c)


    out=host1.decrypt(c)
    if int_message != out:
        print("error")
        # break
    



