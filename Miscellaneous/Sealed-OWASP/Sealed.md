## Sealed — Miscellaneous

- **Challenge:** Sealed
- **Category:** Miscellaneous
- **Points:** 195
- **Author:** kira07
- **Objective:** Recover the secret from an encrypted file using the service source code and network capture.

### Steps to Solve

1. **Inspect the challenge files**
   - Examined `app.py`, `capture.pcapng`, and `flag.enc` to understand the encryption process and identify potential sources of the secret key.

2. **Analyze the service source code**
   - Reviewed the Python application to understand how the secret was encrypted and what information was needed for decryption.

   ```bash
   cat app.py
   ```

3. **Analyze the network capture**
   - Opened the packet capture in Wireshark to inspect the network communication and identify useful data related to the encryption process.
   - Used `tshark` to inspect packets from the terminal when needed.

   ```bash
   tshark -r capture.pcapng
   ```

4. **Recover the required information**
   - Correlated information from the source code and network capture to recover the information needed to decrypt the encrypted file.

5. **Decrypt the secret**
   - Used the recovered information and the encryption method identified in the source code to decrypt `flag.enc` and retrieve the flag.

### Tools Used

- **Kali Linux** — Analysis environment.
- **Python 3** — Inspected the service implementation and assisted with decryption.
- **Wireshark** — Analyzed network traffic.
- **`tshark`** — Inspected packet captures from the terminal.
- **Linux Terminal** — Executed analysis commands.
- **`cat`** — Read the application source code.

### Flag

```text
OESAP{3v3ry_s3c0nd_c0unts}
```

### Key Takeaway

This challenge demonstrated the importance of combining source-code analysis, network forensics, and cryptographic analysis. Information exposed through network communication can undermine the security of encrypted data when the encryption implementation or key-handling process is vulnerable.