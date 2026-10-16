# XOR Riddle

- **Event:** OWASP CTF
- **Category:** Cryptography
- **Tool Used:** XOR Cipher Encoder & Decoder
- **Technique:** XOR Cipher Decryption and Key Identification

## Objective

The objective was to decrypt an XOR-encrypted message. The challenge description provided hints that the encryption used a short key and that the key was a common English word.

## Approach and Methodology

Based on the challenge description, I investigated the expected key length and identified that it was 6 characters long. Using this clue, I determined that the word `secret` was a suitable match for the encryption key.

After identifying the key, I used the XOR Cipher Encoder & Decoder tool to decrypt the encrypted message. The decryption process successfully revealed the flag.

## Result

The XOR cipher decryption successfully revealed the flag.

**Flag / Answer:** `OWASP{x0r_1s_symm3tr1c_c1ph3r}`

## Learning Outcome

This challenge helped me understand how clues about key length and common English words can assist in identifying an XOR encryption key. I also learned how to use an XOR cipher tool to decrypt a message when the correct key is identified.

## Tool Reference

[Add the URL of the XOR Cipher Encoder & Decoder tool used.]