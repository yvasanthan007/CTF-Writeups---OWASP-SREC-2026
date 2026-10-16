┌──(vasanthan㉿Kali)-[~]
└─$ ls
base64  Desktop  Documents  Downloads  Music  Pictures  Projects  Public  Templates  test_pickle.py  Videos  whisker_exploit.py  wifi-lab

┌──(vasanthan㉿Kali)-[~]
└─$ cd Downloads

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ ls
ap-south-1-yvasanthan007-regular.ovpn  audit_report.txt  bg.jpg  blackeye-1  Certifications  chall.txt  check_steg.py  obfuscated.py  Overthewire  payload.bin  solve.py  Solving  zlib  zphisher

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ cat audit_report.txt
Project Documentation - Confidential 
==================================================
 
Executive Summary 
--------------------------------------------------
This document outlines the security audit findings for the
quarterly review. All recommendations have been implemented.

Section 1: Network Security 
--------------------------------------------------
Firewall rules have been updated to block unauthorized access. 
VPN connections are now enforced for all remote workers.
Intrusion detection systems are monitoring all traffic. 

Section 2: Access Control
--------------------------------------------------
Multi-factor authentication is now mandatory for all users. 
Password policies have been strengthened significantly.
Regular access reviews are scheduled monthly. 
 
Section 3: Data Protection 
-------------------------------------------------- 
All sensitive data is encrypted at rest and in transit. 
Backup procedures have been automated and tested.
Data retention policies comply with regulations. 

Section 4: Incident Response 
--------------------------------------------------                                                                                                                                                                    
Incident response plan has been updated and tested.                                                                                                                                                                   
All team members have completed security training.                                                                                                                                                                    
Quarterly tabletop exercises are now mandatory.                                                                                                                                                                       
                                                                                                                                                                                                                      
==================================================                                                                                                                                                                    
End of Document                                                                                                                                                                                                       
                                                                                                                                                                                                                      
                                                                                                                             
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                    
 
vasanthan㉿Kali)-[~/Downloads]
└─$ file audit_report.txt                                                                                                                                                                                             
audit_report.txt: ASCII text

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ xxd -g 1 audit_report.txt | less                                                                                                                                                                                  

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ nano solve_DF.py                                                                                                                                                                                               

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ python3 solve_DF.py                                                                                                                                                                                               
[+] File size: 1785
[+] Trailing whitespace per line:
Line   1: spaces=1, tabs=0, total=1
Line   2: spaces=0, tabs=1, total=1
Line   3: spaces=1, tabs=0, total=1
Line   4: spaces=1, tabs=0, total=1
Line   5: spaces=0, tabs=1, total=1
Line   6: spaces=0, tabs=1, total=1
Line   7: spaces=0, tabs=1, total=1
Line   8: spaces=0, tabs=1, total=1
Line   9: spaces=1, tabs=0, total=1
Line  10: spaces=0, tabs=1, total=1
Line  11: spaces=1, tabs=0, total=1
Line  12: spaces=0, tabs=1, total=1
Line  13: spaces=1, tabs=0, total=1
Line  14: spaces=0, tabs=1, total=1
Line  15: spaces=0, tabs=1, total=1
Line  16: spaces=0, tabs=1, total=1
Line  17: spaces=1, tabs=0, total=1
Line  18: spaces=0, tabs=1, total=1
Line  19: spaces=1, tabs=0, total=1
Line  20: spaces=1, tabs=0, total=1
Line  21: spaces=1, tabs=0, total=1
Line  22: spaces=1, tabs=0, total=1
Line  23: spaces=1, tabs=0, total=1
Line  24: spaces=0, tabs=1, total=1
Line  25: spaces=1, tabs=0, total=1
Line  26: spaces=0, tabs=1, total=1
Line  27: spaces=1, tabs=0, total=1
Line  28: spaces=0, tabs=1, total=1
Line  29: spaces=1, tabs=0, total=1
Line  30: spaces=1, tabs=0, total=1
Line  31: spaces=0, tabs=1, total=1
Line  32: spaces=0, tabs=1, total=1
Line  33: spaces=1, tabs=0, total=1
Line  34: spaces=0, tabs=1, total=1
Line  35: spaces=1, tabs=0, total=1
Line  36: spaces=0, tabs=1, total=1
Line  37: spaces=1, tabs=0, total=1
Line  38: spaces=1, tabs=0, total=1
Line  39: spaces=1, tabs=0, total=1
Line  40: spaces=1, tabs=0, total=1
Line  41: spaces=1, tabs=0, total=1
Line  42: spaces=0, tabs=1, total=1
Line  43: spaces=0, tabs=1, total=1
Line  44: spaces=0, tabs=1, total=1
Line  45: spaces=0, tabs=1, total=1
Line  46: spaces=1, tabs=0, total=1
Line  47: spaces=0, tabs=1, total=1
Line  48: spaces=0, tabs=1, total=1
Line  49: spaces=1, tabs=0, total=1
Line  50: spaces=0, tabs=1, total=1
Line  51: spaces=0, tabs=1, total=1
Line  52: spaces=0, tabs=1, total=1
Line  53: spaces=1, tabs=0, total=1
Line  54: spaces=0, tabs=1, total=1
Line  55: spaces=0, tabs=1, total=1
Line  56: spaces=0, tabs=1, total=1
Line  57: spaces=1, tabs=0, total=1
Line  58: spaces=0, tabs=1, total=1
Line  59: spaces=0, tabs=1, total=1
Line  60: spaces=1, tabs=0, total=1
Line  61: spaces=0, tabs=1, total=1
Line  62: spaces=1, tabs=0, total=1
Line  63: spaces=1, tabs=0, total=1
Line  64: spaces=1, tabs=0, total=1
Line  65: spaces=1, tabs=0, total=1
Line  66: spaces=1, tabs=0, total=1
Line  67: spaces=0, tabs=1, total=1
Line  68: spaces=0, tabs=1, total=1
Line  69: spaces=1, tabs=0, total=1
Line  70: spaces=1, tabs=0, total=1
Line  71: spaces=1, tabs=0, total=1
Line  72: spaces=0, tabs=1, total=1
Line  73: spaces=1, tabs=0, total=1
Line  74: spaces=0, tabs=1, total=1
Line  75: spaces=0, tabs=1, total=1
Line  76: spaces=0, tabs=1, total=1
Line  77: spaces=1, tabs=0, total=1
Line  78: spaces=0, tabs=1, total=1
Line  79: spaces=1, tabs=0, total=1
Line  80: spaces=1, tabs=0, total=1
Line  81: spaces=1, tabs=0, total=1
Line  82: spaces=1, tabs=0, total=1
Line  83: spaces=0, tabs=1, total=1
Line  84: spaces=0, tabs=1, total=1
Line  85: spaces=1, tabs=0, total=1
Line  86: spaces=1, tabs=0, total=1
Line  87: spaces=0, tabs=1, total=1
Line  88: spaces=0, tabs=1, total=1
Line  89: spaces=1, tabs=0, total=1
Line  90: spaces=0, tabs=1, total=1
Line  91: spaces=0, tabs=1, total=1
Line  92: spaces=0, tabs=1, total=1
Line  93: spaces=1, tabs=0, total=1
Line  94: spaces=1, tabs=0, total=1
Line  95: spaces=0, tabs=1, total=1
Line  96: spaces=0, tabs=1, total=1
Line  97: spaces=1, tabs=0, total=1
Line  98: spaces=0, tabs=1, total=1
Line  99: spaces=0, tabs=1, total=1
Line 100: spaces=0, tabs=1, total=1
Line 101: spaces=1, tabs=0, total=1
Line 102: spaces=1, tabs=0, total=1
Line 103: spaces=1, tabs=0, total=1
Line 104: spaces=1, tabs=0, total=1
Line 105: spaces=1, tabs=0, total=1
Line 106: spaces=1, tabs=0, total=1
Line 107: spaces=0, tabs=1, total=1
Line 108: spaces=0, tabs=1, total=1
Line 109: spaces=1, tabs=0, total=1
Line 110: spaces=0, tabs=1, total=1
Line 111: spaces=1, tabs=0, total=1
Line 112: spaces=1, tabs=0, total=1
Line 113: spaces=1, tabs=0, total=1
Line 114: spaces=0, tabs=1, total=1
Line 115: spaces=0, tabs=1, total=1
Line 116: spaces=1, tabs=0, total=1
Line 117: spaces=1, tabs=0, total=1
Line 118: spaces=1, tabs=0, total=1
Line 119: spaces=0, tabs=1, total=1
Line 120: spaces=0, tabs=1, total=1
Line 121: spaces=1, tabs=0, total=1
Line 122: spaces=1, tabs=0, total=1
Line 123: spaces=0, tabs=1, total=1
Line 124: spaces=0, tabs=1, total=1
Line 125: spaces=1, tabs=0, total=1
Line 126: spaces=1, tabs=0, total=1
Line 127: spaces=0, tabs=1, total=1
Line 128: spaces=0, tabs=1, total=1
Line 129: spaces=1, tabs=0, total=1
Line 130: spaces=0, tabs=1, total=1
Line 131: spaces=1, tabs=0, total=1
Line 132: spaces=0, tabs=1, total=1
Line 133: spaces=0, tabs=1, total=1
Line 134: spaces=0, tabs=1, total=1
Line 135: spaces=0, tabs=1, total=1
Line 136: spaces=0, tabs=1, total=1
Line 137: spaces=1, tabs=0, total=1
Line 138: spaces=0, tabs=1, total=1
Line 139: spaces=0, tabs=1, total=1
Line 140: spaces=0, tabs=1, total=1
Line 141: spaces=1, tabs=0, total=1
Line 142: spaces=0, tabs=1, total=1
Line 143: spaces=1, tabs=0, total=1
Line 144: spaces=1, tabs=0, total=1
Line 145: spaces=1, tabs=0, total=1
Line 146: spaces=1, tabs=0, total=1
Line 147: spaces=0, tabs=1, total=1
Line 148: spaces=0, tabs=1, total=1
Line 149: spaces=1, tabs=0, total=1
Line 150: spaces=1, tabs=0, total=1
Line 151: spaces=0, tabs=1, total=1
Line 152: spaces=0, tabs=1, total=1
Line 153: spaces=1, tabs=0, total=1
Line 154: spaces=0, tabs=1, total=1
Line 155: spaces=0, tabs=1, total=1
Line 156: spaces=1, tabs=0, total=1
Line 157: spaces=0, tabs=1, total=1
Line 158: spaces=0, tabs=1, total=1
Line 159: spaces=1, tabs=0, total=1
Line 160: spaces=1, tabs=0, total=1
Line 161: spaces=1, tabs=0, total=1
Line 162: spaces=0, tabs=1, total=1
Line 163: spaces=0, tabs=1, total=1
Line 164: spaces=1, tabs=0, total=1
Line 165: spaces=0, tabs=1, total=1
Line 166: spaces=0, tabs=1, total=1
Line 167: spaces=1, tabs=0, total=1
Line 168: spaces=1, tabs=0, total=1
Line 169: spaces=1, tabs=0, total=1
Line 170: spaces=1, tabs=0, total=1
Line 171: spaces=0, tabs=1, total=1
Line 172: spaces=0, tabs=1, total=1
Line 173: spaces=1, tabs=0, total=1
Line 174: spaces=1, tabs=0, total=1
Line 175: spaces=0, tabs=1, total=1
Line 176: spaces=0, tabs=1, total=1
Line 177: spaces=1, tabs=0, total=1
Line 178: spaces=0, tabs=1, total=1
Line 179: spaces=0, tabs=1, total=1
Line 180: spaces=0, tabs=1, total=1
Line 181: spaces=1, tabs=0, total=1
Line 182: spaces=1, tabs=0, total=1
Line 183: spaces=0, tabs=1, total=1
Line 184: spaces=0, tabs=1, total=1
Line 185: spaces=1, tabs=0, total=1
Line 186: spaces=0, tabs=1, total=1
Line 187: spaces=1, tabs=0, total=1
Line 188: spaces=0, tabs=1, total=1
Line 189: spaces=0, tabs=1, total=1
Line 190: spaces=0, tabs=1, total=1
Line 191: spaces=0, tabs=1, total=1
Line 192: spaces=0, tabs=1, total=1
Line 193: spaces=1, tabs=0, total=1
Line 194: spaces=0, tabs=1, total=1
Line 195: spaces=0, tabs=1, total=1
Line 196: spaces=0, tabs=1, total=1
Line 197: spaces=1, tabs=0, total=1
Line 198: spaces=1, tabs=0, total=1
Line 199: spaces=0, tabs=1, total=1
Line 200: spaces=0, tabs=1, total=1
Line 201: spaces=1, tabs=0, total=1
Line 202: spaces=1, tabs=0, total=1
Line 203: spaces=0, tabs=1, total=1
Line 204: spaces=0, tabs=1, total=1
Line 205: spaces=1, tabs=0, total=1
Line 206: spaces=1, tabs=0, total=1
Line 207: spaces=0, tabs=1, total=1
Line 208: spaces=0, tabs=1, total=1
Line 209: spaces=1, tabs=0, total=1
Line 210: spaces=0, tabs=1, total=1
Line 211: spaces=0, tabs=1, total=1
Line 212: spaces=1, tabs=0, total=1
Line 213: spaces=1, tabs=0, total=1
Line 214: spaces=1, tabs=0, total=1
Line 215: spaces=0, tabs=1, total=1
Line 216: spaces=0, tabs=1, total=1
Line 217: spaces=1, tabs=0, total=1
Line 218: spaces=0, tabs=1, total=1
Line 219: spaces=0, tabs=1, total=1
Line 220: spaces=0, tabs=1, total=1
Line 221: spaces=1, tabs=0, total=1
Line 222: spaces=1, tabs=0, total=1
Line 223: spaces=0, tabs=1, total=1
Line 224: spaces=1, tabs=0, total=1
Line 225: spaces=1, tabs=0, total=1
Line 226: spaces=1, tabs=0, total=1
Line 227: spaces=0, tabs=1, total=1
Line 228: spaces=0, tabs=1, total=1
Line 229: spaces=1, tabs=0, total=1
Line 230: spaces=1, tabs=0, total=1
Line 231: spaces=0, tabs=1, total=1
Line 232: spaces=0, tabs=1, total=1
Line 233: spaces=1, tabs=0, total=1
Line 234: spaces=0, tabs=1, total=1
Line 235: spaces=0, tabs=1, total=1
Line 236: spaces=0, tabs=1, total=1
Line 237: spaces=1, tabs=0, total=1
Line 238: spaces=0, tabs=1, total=1
Line 239: spaces=1, tabs=0, total=1
Line 240: spaces=1, tabs=0, total=1
Line 241: spaces=1, tabs=0, total=1
Line 242: spaces=1, tabs=0, total=1
Line 243: spaces=0, tabs=1, total=1
Line 244: spaces=0, tabs=1, total=1
Line 245: spaces=1, tabs=0, total=1
Line 246: spaces=0, tabs=1, total=1
Line 247: spaces=1, tabs=0, total=1
Line 248: spaces=0, tabs=1, total=1
Line 249: spaces=1, tabs=0, total=1
Line 250: spaces=0, tabs=1, total=1
Line 251: spaces=0, tabs=1, total=1
Line 252: spaces=0, tabs=1, total=1
Line 253: spaces=0, tabs=1, total=1
Line 254: spaces=0, tabs=1, total=1
Line 255: spaces=1, tabs=0, total=1
Line 256: spaces=0, tabs=1, total=1

[+] Non-ASCII characters:

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ python3 - <<'PY'                                                                                                                                                                                                  
from pathlib import Path

lines = Path("audit_report.txt").read_bytes().splitlines()

for i, line in enumerate(lines, 1):
    trailing = line[len(line.rstrip(b" \t")):]
    if trailing:
        bits = ''.join('1' if b == 9 else '0' for b in trailing)
        print(f"{i:3}: {len(trailing):4} chars | {bits}")
PY
  1:    1 chars | 0
  2:    1 chars | 1
  3:    1 chars | 0
  4:    1 chars | 0
  5:    1 chars | 1
  6:    1 chars | 1
  7:    1 chars | 1
  8:    1 chars | 1
  9:    1 chars | 0
 10:    1 chars | 1
 11:    1 chars | 0
 12:    1 chars | 1
 13:    1 chars | 0
 14:    1 chars | 1
 15:    1 chars | 1
 16:    1 chars | 1
 17:    1 chars | 0
 18:    1 chars | 1
 19:    1 chars | 0
 20:    1 chars | 0
 21:    1 chars | 0
 22:    1 chars | 0
 23:    1 chars | 0
 24:    1 chars | 1
 25:    1 chars | 0
 26:    1 chars | 1
 27:    1 chars | 0
 28:    1 chars | 1
 29:    1 chars | 0
 30:    1 chars | 0
 31:    1 chars | 1
 32:    1 chars | 1
 33:    1 chars | 0
 34:    1 chars | 1
 35:    1 chars | 0
 36:    1 chars | 1
 37:    1 chars | 0
 38:    1 chars | 0
 39:    1 chars | 0
 40:    1 chars | 0
 41:    1 chars | 0
 42:    1 chars | 1
 43:    1 chars | 1
 44:    1 chars | 1
 45:    1 chars | 1
 46:    1 chars | 0
 47:    1 chars | 1
 48:    1 chars | 1
 49:    1 chars | 0
 50:    1 chars | 1
 51:    1 chars | 1
 52:    1 chars | 1
 53:    1 chars | 0
 54:    1 chars | 1
 55:    1 chars | 1
 56:    1 chars | 1
 57:    1 chars | 0
 58:    1 chars | 1
 59:    1 chars | 1
 60:    1 chars | 0
 61:    1 chars | 1
 62:    1 chars | 0
 63:    1 chars | 0
 64:    1 chars | 0
 65:    1 chars | 0
 66:    1 chars | 0
 67:    1 chars | 1
 68:    1 chars | 1
 69:    1 chars | 0
 70:    1 chars | 0
 71:    1 chars | 0
 72:    1 chars | 1
 73:    1 chars | 0
 74:    1 chars | 1
 75:    1 chars | 1
 76:    1 chars | 1
 77:    1 chars | 0
 78:    1 chars | 1
 79:    1 chars | 0
 80:    1 chars | 0
 81:    1 chars | 0
 82:    1 chars | 0
 83:    1 chars | 1
 84:    1 chars | 1
 85:    1 chars | 0
 86:    1 chars | 0
 87:    1 chars | 1
 88:    1 chars | 1
 89:    1 chars | 0
 90:    1 chars | 1
 91:    1 chars | 1
 92:    1 chars | 1
 93:    1 chars | 0
 94:    1 chars | 0
 95:    1 chars | 1
 96:    1 chars | 1
 97:    1 chars | 0
 98:    1 chars | 1
 99:    1 chars | 1
100:    1 chars | 1
101:    1 chars | 0
102:    1 chars | 0
103:    1 chars | 0
104:    1 chars | 0
105:    1 chars | 0
106:    1 chars | 0
107:    1 chars | 1
108:    1 chars | 1
109:    1 chars | 0
110:    1 chars | 1
111:    1 chars | 0
112:    1 chars | 0
113:    1 chars | 0
114:    1 chars | 1
115:    1 chars | 1
116:    1 chars | 0
117:    1 chars | 0
118:    1 chars | 0
119:    1 chars | 1
120:    1 chars | 1
121:    1 chars | 0
122:    1 chars | 0
123:    1 chars | 1
124:    1 chars | 1
125:    1 chars | 0
126:    1 chars | 0
127:    1 chars | 1
128:    1 chars | 1
129:    1 chars | 0
130:    1 chars | 1
131:    1 chars | 0
132:    1 chars | 1
133:    1 chars | 1
134:    1 chars | 1
135:    1 chars | 1
136:    1 chars | 1
137:    1 chars | 0
138:    1 chars | 1
139:    1 chars | 1
140:    1 chars | 1
141:    1 chars | 0
142:    1 chars | 1
143:    1 chars | 0
144:    1 chars | 0
145:    1 chars | 0
146:    1 chars | 0
147:    1 chars | 1
148:    1 chars | 1
149:    1 chars | 0
150:    1 chars | 0
151:    1 chars | 1
152:    1 chars | 1
153:    1 chars | 0
154:    1 chars | 1
155:    1 chars | 1
156:    1 chars | 0
157:    1 chars | 1
158:    1 chars | 1
159:    1 chars | 0
160:    1 chars | 0
161:    1 chars | 0
162:    1 chars | 1
163:    1 chars | 1
164:    1 chars | 0
165:    1 chars | 1
166:    1 chars | 1
167:    1 chars | 0
168:    1 chars | 0
169:    1 chars | 0
170:    1 chars | 0
171:    1 chars | 1
172:    1 chars | 1
173:    1 chars | 0
174:    1 chars | 0
175:    1 chars | 1
176:    1 chars | 1
177:    1 chars | 0
178:    1 chars | 1
179:    1 chars | 1
180:    1 chars | 1
181:    1 chars | 0
182:    1 chars | 0
183:    1 chars | 1
184:    1 chars | 1
185:    1 chars | 0
186:    1 chars | 1
187:    1 chars | 0
188:    1 chars | 1
189:    1 chars | 1
190:    1 chars | 1
191:    1 chars | 1
192:    1 chars | 1
193:    1 chars | 0
194:    1 chars | 1
195:    1 chars | 1
196:    1 chars | 1
197:    1 chars | 0
198:    1 chars | 0
199:    1 chars | 1
200:    1 chars | 1
201:    1 chars | 0
202:    1 chars | 0
203:    1 chars | 1
204:    1 chars | 1
205:    1 chars | 0
206:    1 chars | 0
207:    1 chars | 1
208:    1 chars | 1
209:    1 chars | 0
210:    1 chars | 1
211:    1 chars | 1
212:    1 chars | 0
213:    1 chars | 0
214:    1 chars | 0
215:    1 chars | 1
216:    1 chars | 1
217:    1 chars | 0
218:    1 chars | 1
219:    1 chars | 1
220:    1 chars | 1
221:    1 chars | 0
222:    1 chars | 0
223:    1 chars | 1
224:    1 chars | 0
225:    1 chars | 0
226:    1 chars | 0
227:    1 chars | 1
228:    1 chars | 1
229:    1 chars | 0
230:    1 chars | 0
231:    1 chars | 1
232:    1 chars | 1
233:    1 chars | 0
234:    1 chars | 1
235:    1 chars | 1
236:    1 chars | 1
237:    1 chars | 0
238:    1 chars | 1
239:    1 chars | 0
240:    1 chars | 0
241:    1 chars | 0
242:    1 chars | 0
243:    1 chars | 1
244:    1 chars | 1
245:    1 chars | 0
246:    1 chars | 1
247:    1 chars | 0
248:    1 chars | 1
249:    1 chars | 0
250:    1 chars | 1
251:    1 chars | 1
252:    1 chars | 1
253:    1 chars | 1
254:    1 chars | 1
255:    1 chars | 0
256:    1 chars | 1

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ nano decode.py                                                                                                                                                                                                    

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ python3 decode.py                                                                                                                                                                                                 
[+] Extracted 256 bits
[+] Hex: 4f574153507b776831743373703463335f74336c6c33735f733363723374357d

--- normal ---
ASCII: 'OWASP{wh1t3sp4c3_t3ll3s_s3cr3t5}'
Hex:   4f574153507b776831743373703463335f74336c6c33735f733363723374357d
Base64: T1dBU1B7d2gxdDNzcDRjM190M2xsM3NfczNjcjN0NX0=

--- reversed bits ---
ASCII: '   \n  \x16 .  \x0e,   . 66      N .  '
Hex:   f2ea82ca0adeee168c2eccce0e2cc6ccfa2ecc3636cccefaceccc64ecc2eacbe
Base64: 8uqCygre7haMLszODizGzPouzDY2zM76zszGTswurL4=

--- reversed stream ---
ASCII: '  . N      66 .   ,\x0e  . \x16  \nʂ  '
Hex:   beac2ecc4ec6cccefacecc3636cc2efaccc62c0ececc2e8c16eede0aca82eaf2
Base64: vqwuzE7GzM76zsw2Nswu+szGLA7OzC6MFu7eCsqC6vI=
