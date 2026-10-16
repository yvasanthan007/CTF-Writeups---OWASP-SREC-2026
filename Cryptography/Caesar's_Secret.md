# Caesar's Secret

- **Event:** OWASP CTF
- **Category:** Cryptography
- **Tool Used:** CyberChef
- **Technique:** Caesar Cipher (ROT13)

## Objective

The objective was to decode the hidden message provided in the *Caesar's Secret* challenge and recover the readable plaintext.

## Approach and Methodology

Based on the challenge name, I suspected that the message was encrypted using a Caesar cipher.The encrypted message was in encrypted.txt I chose CyberChef to analyze and decode the message.

I used the **ROT13** recipe in CyberChef, which rotates each letter of the alphabet by 13 positions. I entered the provided ciphertext into the input field and applied the recipe to obtain the decoded output.

## Result

The ROT13 operation was used to decode the message. The resulting plaintext could then be checked to determine whether it contained the expected flag or challenge answer.

**Flag / Answer:** OWASP{c43s4r_c1ph3r_1s_34sy_t0_cr4ck}

## Learning Outcome

This challenge helped me understand how a Caesar cipher can be recognized from contextual clues and how CyberChef can be used to decode ROT13-encoded text. It also reinforced the importance of identifying suitable cryptographic techniques when solving CTF challenges.

## Tool Reference

- [CyberChef](https://gchq.github.io/CyberChef/)

