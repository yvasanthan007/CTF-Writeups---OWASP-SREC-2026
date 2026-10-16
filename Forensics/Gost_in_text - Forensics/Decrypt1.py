
import random

receipt_target = "1e7a4f25daa1ca3b"

with open("flag.enc", "rb") as f:
    ciphertext = f.read()

# Candidate seeds derived from the packet capture.
for seed in range(1749926550, 1749926565):
    rng = random.Random(seed)

    # Reproduce the service's receipt.
    receipt = rng.randbytes(8).hex()

    if receipt != receipt_target:
        continue

    print("[+] Receipt matched!")
    print("[+] Seed:", seed)

    # Reproduce the encryption mask.
    mask = rng.randbytes(len(ciphertext))

    # Reverse XOR encryption.
    plaintext = bytes(
        encrypted_byte ^ mask_byte
        for encrypted_byte, mask_byte in zip(ciphertext, mask)
    )

    print("[+] Recovered plaintext:", plaintext.decode())
    break
else:
    print("[-] No matching seed found.")

