from pathlib import Path
import base64

lines = Path("audit_report.txt").read_bytes().splitlines()

bits = ""
for line in lines:
    trailing = line[len(line.rstrip(b" \t")):]
    if trailing == b" ":
        bits += "0"
    elif trailing == b"\t":
        bits += "1"

print(f"[+] Extracted {len(bits)} bits")
print(f"[+] Hex: {bytes(int(bits[i:i+8], 2) for i in range(0, len(bits)-7, 8)).hex()}")

for name, stream in [
    ("normal", bits),
    ("reversed bits", "".join(
        bits[i:i+8][::-1] for i in range(0, len(bits), 8)
    )),
    ("reversed stream", bits[::-1]),
]:
    print(f"\n--- {name} ---")
    usable = stream[:len(stream) // 8 * 8]
    raw = bytes(int(usable[i:i+8], 2)
                for i in range(0, len(usable), 8))
    print("ASCII:", repr(raw.decode("utf-8", errors="replace")))
    print("Hex:  ", raw.hex())
    print("Base64:", base64.b64encode(raw).decode())
