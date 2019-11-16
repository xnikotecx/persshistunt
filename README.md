## PerSSHisTUNt !

Persist an SSH tunnel!

This is what the script does. It will persist a SSH tunnel issuing a simple command
using simple wrappers:

`ssh -R ` equivalent:<br>
`python3 main.py from-my 8080 to-his 8081 user@myremoteserver`<br>

`ssh -L ` equivalent:<br>
`python3 main.py from-his 8081 to-my 8080 user@myremoteserver`<br>

Or... use the legacy ssh syntax for custom options:<br>
`python3 main -R *:8081:127.0.0.1:8080 -o IdentityFile=~/myssh.key root@remotesrv`
