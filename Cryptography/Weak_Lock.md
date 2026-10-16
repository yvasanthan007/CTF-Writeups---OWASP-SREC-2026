# Weak Lock

- **Event:** OWASP CTF
- **Category:** Cryptography
- **Tool Used:** XOR Cipher Encoder & Decoder
- **Technique:** XOR Cipher Decryption

## Objective

The objective was to decrypt a message encrypted using an XOR cipher. The challenge description indicated that the encryption key was 4 bytes long.

## Approach and Methodology

Based on the challenge description, I identified that the message was encrypted using an XOR cipher with a 4-byte key. I used an online tool called XOR Cipher Encoder & Decoder to solve the challenge.

I used the provided key bytes in the specified hexadecimal format, such as `0x41`, in the XOR cipher tool to decrypt the encrypted message. This process helped me recover the flag.

## Result

The XOR cipher decryption successfully revealed the flag.

**Flag / Answer:** `OWASP{w34k_k3y_m4k3s_34sy_w0rk}`

## Learning Outcome

This challenge helped me understand how XOR encryption works and how the key length affects the decryption process. I learned to use an online XOR cipher tool and represent key bytes in hexadecimal format to decrypt an encrypted message and retrieve the flag.

## Tool Reference

- [XOR Cipher Encoder & Decoder](https://www.thehackerwire.com/hacking-tools/xor-cipher)