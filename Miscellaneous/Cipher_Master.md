# Cipher Master — Miscellaneous

- **Challenge:** Cipher Master
- **Category:** Miscellaneous
- **Points:** 150
- **Author:** Mr-IR0k-oo1svg
- **Objective:** Decode four encoding layers to recover the flag.

## Steps to Solve

### 1. Read the Provided File

Used Kali Linux to inspect the attached `encoded.txt` file.

```bash
cat encoded.txt
```

The file specified four encoding layers: Base64, ROT13, Base64, and Reverse.

### 2. Reverse the Encoded String

Used Python to reverse the encoded message.

```bash
python3 -c "s='=0TPENXbXNjW1UUUvNXc692aERlW3VjMaNXQR9maTFVcrh0SvdzTxg0TxFzR'; print(s[::-1])"
```

### 3. Decode the First Base64 Layer

After reversing the string, decoded the Base64 data.

```bash
echo 'REVERSED_STRING' | base64 -d
```

Replaced `REVERSED_STRING` with the output from Step 2.

### 4. Apply ROT13

Decoded the ROT13 layer using Python.

```bash
python3 -c "import codecs; print(codecs.decode('BASE64_DECODED_TEXT', 'rot_13'))"
```

Replaced `BASE64_DECODED_TEXT` with the output from Step 3.

### 5. Decode the Final Base64 Layer

Decoded the resulting Base64 string to reveal the flag.

```bash
echo 'FINAL_BASE64_TEXT' | base64 -d
```

Replaced `FINAL_BASE64_TEXT` with the output from Step 4.

### Tools Used

- **Kali Linux** — Operating environment.
- **Linux Terminal** — Executed decoding commands.
- **`cat`** — Read the challenge file.
- **Python 3** — Reversed the string and applied ROT13.
- **`base64`** — Decoded the Base64 layers.

### Final Flag

```text
OWASP{mu1t1pl3_3nc0d1ng_l4y3rs}
```

### Key Takeaway

This challenge demonstrated how multiple encoding methods can be combined to hide a message. The key was to reverse the order of the encoding layers and decode them in the opposite sequence: Reverse → Base64 → ROT13 → Base64.