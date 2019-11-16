## PerSSHisTUNt !

Persist an SSH tunnel!

This is what this script does. It will persist a SSH tunnel issuing a simple command
using our wrappers:

`ssh -R ` equivalent:
`python3 main.py from-my 8080 to-his 8081 user@myremoteserver`

`ssh -L ` equivalent:
`python3 main.py from-his 8081 to-my 8080 user@myremoteserver`
