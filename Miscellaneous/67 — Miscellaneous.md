# 67 — Miscellaneous

- **Challenge:** 67
- **Category:** Miscellaneous
- **Points:** 67
- **Author:** kira07
- **Objective:** Decode the provided sequence to recover the flag.

## Steps to Solve

### 1. Read the Challenge File

Used Kali Linux to inspect the provided text file.

```bash
cat "chall (1).txt"
```

The file contained a long sequence consisting entirely of the digits `6` and `7`.

### 2. Identify the Encoding

Recognized that the sequence could represent binary data by mapping:

- `6` → `0`
- `7` → `1`

The resulting binary sequence could then be split into groups of 8 bits to represent ASCII characters.

### 3. Decode the Binary

Used Python 3 to convert the digits into binary and decode each 8-bit group into text.

```bash
python3 -c "s=open('chall (1).txt').read().strip(); b=''.join('0' if c=='6' else '1' for c in s); print(bytes(int(b[i:i+8],2) for i in range(0,len(b),8)).decode())"
```

The command converted the sequence into binary, grouped the bits into bytes, and decoded the bytes into readable ASCII text.

### 4. Retrieve the Flag

The decoded output revealed the flag directly.

## Tools Used

- **Kali Linux** — Operating environment.
- **Linux Terminal** — Executed commands.
- **`cat`** — Displayed the challenge file.
- **Python 3** — Converted the digit sequence into binary and decoded the ASCII text.

## Flag

```text
OWASP{c0mpu73r5_d0n7_5p34k_b1n4ry_7h3y_5p34k_67}
```

## Key Takeaway

This challenge demonstrated how a sequence containing only two distinct digits can encode binary data. By mapping `6` to `0` and `7` to `1`, then decoding the bits in 8-bit groups, the original message and flag were recovered.