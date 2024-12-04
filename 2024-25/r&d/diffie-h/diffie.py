import random

minumum=5
maxumum=20
# to fix, p has to be a prime,
# and for g to be a root, p has to be 2, 4, other prime **k k>1, or 2*other prime**k k>1
# g**x % p hits all numbers 1 to p-1

class diffie():
    def __init__(self):
        self.secret = random.randint(minumum, maxumum)
        self.base = None
        self.mod = None
        self.key = None

    def test(self):
        print(self.secret,self.base,self.mod,self.key)



    def gcd(self,a,b):
        while b != 0:
            a, b = b, a % b
        return a

    def roots(self,mod):
        ans=[]
        hits={hit for hit in range(1,mod) if self.gcd(hit,mod)==1} # all numbers up to mod and have a divisor of 1 (coprime)

        for i in range(2,mod):

            if not self.isPrime(i): # also has to be prime for other req
                continue

            # actual_set = set( i** power % mod for power in range (1, mod))
            # if actual_set == hits:
            #     ans.append(i)  

            # or 

            if hits == {pow(i, powers, mod) for powers in range(1, mod)}:
                ans.append(i)

        return ans

    def isPrime(self,n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False        
        return True

    def nthPrime(self,n):

        count =0 
        i=0
        while count<n:
            i+=1
            if self.isPrime(i):
                count+=1
        return i



    def createPublicKey(self):
        return self.base**self.secret % self.mod
    
    def receivePublicKey(self, publicKey):
        self.key=publicKey**self.secret % self.mod
        print("key:",self.key)


    def send(self): #send the public power
        # self.base = random.randint(minumum, maxumum)
        self.base = 20
        self.base= self.nthPrime(self.base)
        return self.base
    
    def reply(self, base): # recive public power and send mod
        self.base = base
        # self.mod = random.randint(minumum, maxumum)

        mods = self.roots(base)
        print(mods)

        self.mod = mods[random.randint(0,len(mods)-1)]
        # self.mod = 23

        return self.mod, self.createPublicKey()

    
    def receive(self, modulus, publicKey):
        self.mod = modulus
        temp = self.createPublicKey()

        self.key = publicKey**self.secret % self.mod
        print("Key: ", self.key)

        return temp
    
    


    # def dataIn
    # def dataOut

if __name__ =="__main__":
    alice = diffie()
    bob = diffie()

    p=alice.send() 
    print("Alice sent (base): ", p )

    g,B=bob.reply(p)
    print("Bob replied (mod, bob's public): ", g, B)

    A=alice.receive(g,B) 
    #received the public key, so she knows the whole key
    print("Alice received (alice's public): ", A)

    bob.receivePublicKey(A)

    alice.test()
    bob.test()

    

    


