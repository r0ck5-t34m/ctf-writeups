from Crypto.Util.number import long_to_bytes
import gmpy2

f = open("encryption.txt")

e = int(f.readline().split()[-1])
n = int(f.readline().split()[-1])
c = int(f.readline().split()[-1])

m, _ = gmpy2.iroot(c, e)
print(f"The Flag: {long_to_bytes(m).decode()}")