import os as os
import subprocess as sp
def main():
#	os.system("cd /home/nishant/django/DevOps/index/docker-shellinabox")
#	os.system("docker build -t guestshellinabox .")
	os.system("docker run -d shellinabox ")
#	container_id=sp.check_output("docker ps -q",shell=True).split()[8]
	return
