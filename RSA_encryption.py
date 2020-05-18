import math
import time 

start_time = time.time()
print("RSA encryption algorithm")

#getting user input for p and q as primes
print("Enter two prime numbers below: ")
p = int(input("1st number: "))
q = int(input("2nd number: "))

#Check user input for p and q

def is_prime(number):
    if (number > 1):
        for i in range (2, number//2):
            if (number % i == 0):
                return False
            else:
                return True
    else:
        return False

check_p = is_prime(p)
check_q = is_prime(q)

while ((check_p == False) or (check_q) == False):
    p = int(input("Please choose a prime number for p: "))
    q = int(input("Please choose a prime number for q: "))
    check_p = is_prime(p)
    check_q = is_prime(q)

#first part of the public key
n = p*q
#Euler's totient function
phi = (p-1)*(q-1)

#Euclid's alg for determining greatest common divisor
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

#the public key d determined with extended Euclid's algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#and the multiplicative modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#calculate e such as e is coprime with phi and it's the biggest value in loop
for i in range (1,1000):
    if (gcd(i, phi) == 1):
        e = i
d = modinv(e,phi)
public = (e, n)
private = (d, n)
print("The public key is: ", public)
print("The private key is: ", private)

def encrypt_msg(n, e, some_text):
    #n, e = pub_key
    x = []
    for i in some_text:
        if (i.isupper()):
            m = ord(i)-65
            c = (m**e)%n
            x.append(c)
        elif (i.islower()):
            m = ord(i)-97
            c = (m**e)%n
            x.append(c)
    return x

def decrypt_msg(pv_key, encrypted_text):
    d, n = pv_key
    txt=encrypted_text.split(',')
    print(txt)
    x = ''
    for i in txt:
        m = (int(i)**d)%n+65
        decr = chr(m)
        x += decr
    return x
user_message = input("What do you want to encrypt/decrypt? Please use values separated by comma for decryption: ")
rsa_option = input("Choose 1 for encryption or 2 for decryption: ")
if (rsa_option) == '1':
    encrypted = encrypt_msg(n, e, user_message)
    print("RSA encryption of your message is: ", encrypted)
elif (rsa_option) == '2':
    decrypted = decrypt_msg(private, user_message)
    print("RSA decryption of your message is: ", decrypted)

print("--- %s seconds ---" % (time.time() - start_time))
