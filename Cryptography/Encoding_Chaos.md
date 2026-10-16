# Encoding Chaos

- **Event:** OWASP CTF
- **Category:** Cryptography
- **Tool Used:** CyberChef
- **Technique:** Repeated Base64 Decoding

## Objective

The objective was to decode a message that had been encoded multiple times and recover the hidden flag.

## Approach and Methodology

The challenge provided a file named `encoded.txt` containing an encoded message. I used CyberChef to analyze the contents of the file and identify a suitable decoding technique.

I applied the **From Base64** recipe repeatedly to decode the message layer by layer. By continuing the decoding process, I eventually recovered the flag.

## Result

The repeated Base64 decoding operation successfully revealed the hidden flag.

**Flag / Answer:** `OWASP{b4s364_1s_n0t_3ncrypt10n}`

## Learning Outcome

This challenge helped me understand how data can be encoded multiple times using Base64 and how repeated decoding can reveal the original message. It also improved my ability to use CyberChef for analyzing and decoding encoded data.

## Tool Reference

- [CyberChef](https://gchq.github.io/CyberChef/)