# RSA Decryption with Small Public Exponent \( e = 3 \)

## Problem Statement

We are given the following values:

- Public exponent \( e = 3 \)
- RSA modulus \( n \)
- Ciphertext \( c \)

The goal is to decrypt the ciphertext \( c \) and retrieve the original message \( m \).

## Approach

When using RSA with a small public exponent (e.g., \( e = 3 \)) and when the message \( m \) is small enough such that \( m^e < n \), the ciphertext \( c \) can be directly decrypted by computing the integer \( e \)-th root of \( c \). This is because in such cases, the ciphertext \( c \) is simply \( m^e \) without any modular reduction by \( n \).

## Decryption Steps

1. **Compute the Integer Cube Root**:
   We compute the cube root of \( c \) using the `gmpy2` library's `iroot` function, which returns the integer root and a boolean indicating if the root is exact.

2. **Verify the Result**:
   We verify that raising the computed root \( m \) to the power of \( e \) modulo \( n \) gives back the original ciphertext \( c \). This ensures the correctness of the decryption.

3. **Convert the Integer to Bytes**:
   If the verification is successful, we convert the decrypted integer message \( m \) to bytes to retrieve the original plaintext message.

## Code

Below is the Python code to perform the decryption:

```python
from Crypto.Util.number import long_to_bytes
import gmpy2

# Given values
e = 3
n = 135112325288715136727832177735512070625083219670480717841817583343851445454356579794543601926517886432778754079508684454122465776544049537510760149616899986522216930847357907483054348419798542025184280105958211364798924985051999921354369017984140216806642244876998054533895072842602131552047667500910960834243
c = 13037717184940851534440408074902031173938827302834506159512256813794613267487160058287930781080450199371859916605839773796744179698270340378901298046506802163106509143441799583051647999737073025726173300915916758770511497524353491642840238968166849681827669150543335788616727518429916536945395813

# Compute the cube root of c
m, _ = gmpy2.iroot(c, e)

print(f"The Flag: {long_to_bytes(m).decode()}")```
