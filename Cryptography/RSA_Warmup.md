# RSA Warmup

- **Event:** OWASP CTF
- **Category:** Cryptography
- **Tool Used:** dCode RSA Cipher
- **Technique:** RSA Decryption

## Objective

The challenge was based on the RSA encryption algorithm. The given information included the public key parameters `n` and `e`, along with an encoded message represented as an array of integers. The objective was to decrypt the message and retrieve the flag.

## Approach and Methodology

I first studied the RSA algorithm and its mathematical equations to understand how the decryption process works. I then used a search engine to find the values of the prime numbers `p` and `q` associated with the given modulus `n`. After understanding the required mathematical relationship, I entered the available RSA parameters into the online dCode RSA Cipher tool to decrypt the encoded message and obtain the plaintext.

## Result

Successfully decrypted the RSA-encrypted message and retrieved the flag.

**Flag:** `OWASP{rs4_s1mple_d3crypt10n}`

## Learning Outcome

This challenge helped me understand the fundamentals of RSA encryption and the mathematical principles behind decryption. I learned about the roles of the public key parameters `n` and `e`, the importance of the prime factors `p` and `q`, and how an online RSA tool can assist in recovering plaintext from an encrypted message.

## Tool Reference

[dCode RSA Cipher](https://www.dcode.fr/rsa-cipher)