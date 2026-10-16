### Riddle — Reverse Engineering (200 Points)

- **Step 1: Identify the binary**
  - Tool: `file`
  - Command: `file riddle`
  - Identified the executable as a 64-bit, statically linked, stripped ELF binary.

- **Step 2: Inspect strings**
  - Tool: `strings`
  - Command: `strings riddle`
  - Found game messages and useful markers such as `riddle-v1` and `riddle`.

- **Step 3: Analyze the binary**
  - Tool: `GDB` and `objdump`
  - Commands: `gdb -q ./riddle` and `objdump -d ./riddle`
  - Examined the validation function and discovered that the door statements were misleading.

- **Step 4: Recover the correct values**
  - Tool: Python 3 - python used here
  - Reimplemented the validation algorithm and recovered the correct values for all 10 rounds.

- **Step 5: Bypass validation**
  - Tool: `GDB`
  - Command: `gdb -q -batch -x g.gdb ./riddle`
  - Used a breakpoint and register modification to supply the correct values for each round.

- **Step 6: Retrieve the flag**
  - Successfully passed all 10 rounds and triggered the flag decryption.

**Final Flag:**
`OWASP{wh3n_r1ddl35_f41l_w3_h4ck_0ur_w4y_0ut}`

**Key Tools:** `file`, `strings`, `objdump`, Python 3, and GDB.

#OWASP #CTF #CyberSecurity #ReverseEngineering #GDB