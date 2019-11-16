## PerSSHisTUNt !

Persist an SSH tunnel!

This is what the script does. It will persist a SSH tunnel issuing a simple command
using simple wrappers:

`ssh -R ` equivalent:

`python3 main.py from-my 8080 to-his 8081 user@myremoteserver`


`ssh -L ` equivalent:

`python3 main.py from-his 8081 to-my 8080 user@myremoteserver`


Or... use the legacy ssh syntax for custom options:

`python3 main -R *:8081:127.0.0.1:8080 -o IdentityFile=~/myssh.key root@remotesrv`


## Requirements

Any _python3_ installed on the machine

## Installation

Clone the repository wherever you want

`git clone https://github.com/xnikotecx/persshistunt.git`

Change directory to the cloned repo

`cd persshistunt/`

Run the commands using python3 or use our install script.

`./install.sh`
