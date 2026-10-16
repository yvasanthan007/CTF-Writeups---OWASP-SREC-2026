I found the chall content

676677776767677767666667676766776767666667777677677666776677666667767767677766666777676766776777667766776777667666776767676777776776676666776666677677766677677767677777667767676777666666776677667767666776767767677777677666766677666767767776667767666777667667777667676777776677677767767666667766776777766767677777667767676777666666776677667767666776767767677777667767766677677767777767

#commands 

wc -c chall.txt
head -c 100 chall.txt
file chall.txt


# rev — Reverse Engineering

- **Challenge:** rev
- **Category:** Reverse Engineering
- **Author:** kira07svg
- **Points:** 79

### Solution

- **Step 1: Inspect the challenge file**

  ```bash
  cat chall
  ```

  The file contains a long sequence consisting only of the digits `6` and `7`.

- **Step 2: Identify the encoding**

  The sequence can be interpreted as binary by replacing:
  - `6` with `0`
  - `7` with `1`

- **Step 3: Decode the binary data**

  Each group of 8 bits represents one ASCII character. I used Python 3 to convert the sequence into readable text.

  ```bash
  python3 - <<'PY'
  data = open("chall", "r").read().strip()
  bits = data.translate(str.maketrans("67", "01"))
  flag = bytes(
      int(bits[i:i+8], 2)
      for i in range(0, len(bits), 8)
  ).decode()
  print(flag)
  PY
  ```

- **Step 4: Retrieve the flag**

  The decoded output revealed the flag.

### Final Flag

```text
OWASP{c0mpu73r5_d0n7_5p34k_b1n4ry_7h3y_5p34k_b1n4ry_7h3y_5p34k_b1n4r}
```

### Tools Used

- Kali Linux terminal
- Python 3
- ASCII and binary decoding
