import subprocess
import sys



if(len(sys.argv) <= 1):
    print("Gagal: IP address belum diberikan")
else:
    ip = str(sys.argv[1])
    status, result = subprocess.getstatusoutput("ping " + ip)
    if(status == 0):
        print(f'Host {ip} is UP')
    else:
        print(f'Host {ip} is DOWN'