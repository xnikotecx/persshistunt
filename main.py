import subprocess
import signal
import time
import sys
import re
import os

def main():
	args = " ".join(sys.argv[1:])
	payload = None
	if re.match(r'^from-his\s([^:]+:)?([^:]+)\sto-my\s([^:]+:)?([^:]+)\s[^\s]+$', args):
		payload = payload_local_ssh(args)
	elif re.match(r'^from-my\s([^:]+:)?([^:]+)\sto-his\s([^:]+:)?([^:]+)\s[^\s]+$', args):
		payload = payload_remote_ssh(args)
	else:
		payload = payload_legacy_ssh(args)
	payload = payload.replace('*','\\*')
	code = shellx('timeout 1 '+payload)
	if code == 255 or code == 1:
		return sys.exit(code)
	elif code == 124 or code == 0:
		return persist_ssh_tunnel(payload)
	return sys.exit(1)

def persist_ssh_tunnel(cmd):
	s = cmd.lower().strip().replace(' ','').replace('|','')
	o = shello('ps ux | grep ssh')
	o = o.lower().strip().replace(' ','|')
	pid = -1
	for l in o.splitlines():
		if s in l.replace('|',''):
			l = re.sub(r'\|{1,}','|',l)
			ps = l.split('|')
			pid = int(ps[1])
			break
	if pid == -1:
		out = shellx(cmd)
		if out == 255:
			time.sleep(15)
			return persist_ssh_tunnel(cmd)
		return persist_ssh_tunnel(cmd)
	try:
		while True:
			if not os.path.exists('/proc/'+str(pid)):
				return persist_ssh_tunnel(cmd)
			time.sleep(3)
	except KeyboardInterrupt:
		os.kill(pid, signal.SIGKILL)
		return sys.exit(221)

def payload_local_ssh(args):
	return payload_common('L', args)

def payload_remote_ssh(args):
	return payload_common('R', args)

def payload_common(option, args):
	ps = args.strip().split()
	opt1 = ps[1]
	opt2 = ps[3]
	if not ':' in opt1:
		opt1 = '127.0.0.1:'+opt1
	return payload_legacy_ssh('-{} {}:{} {}'.format(option, opt2, opt1, " ".join(ps[4:])))

def payload_legacy_ssh(args):
	return 'ssh -fCN {} -o ServerAliveInterval=1 -o ServerAliveCountMax=1'.format(args)

def shello(cmd):
	try:
		return subprocess.check_output(cmd, shell=True).decode('utf8','ignore').strip()
	except Exception as e:
		print(str(e))
		return None

def shellx(cmd):
	print('[X] '+cmd)
	return subprocess.run(cmd, shell=True).returncode

if __name__ == '__main__':
	main()
