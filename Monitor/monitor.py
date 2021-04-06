import time
import subprocess
import threading
import datetime

date = datetime.datetime.now()
r = open('host.cfg')
w = open('report-monitor.csv','w+')
if w.mode == "r":
    log = w.read()
    print(log)
hosts = []
password = r.readlines()
for line in password:
    line = line.strip()
    size = len(line)
    hosts.append(line)

def do_something():
    status, result = subprocess.getstatusoutput("ping -c1 " + ip)
    if(status == 0):
        result = f'{ip};UP'              
    else:
        result = f'{ip};DOWN'
    print(dates+result)
    w.write(dates+result+"\n")
    
Thread = []
while True:
    gedungA = time.perf_counter()
    mulai = "mulai monitor."    
    print(mulai)
    time.sleep(1)
    for x in range(len(hosts)):
        dates = date.strftime("%Y-%m-%d %X;")
        ip = hosts[x]
        P = threading.Thread(target=do_something)      
        P.start()
        Thread.append(P)

    for t in Thread:
        t.join()
    gedungB = time.perf_counter()
        #w.close()
    akhir = f"Selesai dalam … {round(gedungB-gedungA,2)} detik\n"
    print(akhir)
    time.sleep(15)

w.close()