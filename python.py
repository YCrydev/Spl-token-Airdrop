
# a_file = open("test.txt",'r+')
# number_of_lines = 3
# for i in range(number_of_lines):
#     line = a_file.readline()
#     a_file.write(line+ ' SENT')
#     print(line)
import subprocess
with open('mint.txt', 'r+') as f: #r+ does the work of rw
    lines = f.readlines()
    for i, line in enumerate(lines):
        list_files = subprocess.Popen(["spl-token", "transfer", "BiJyWQr1Gpke3ouevgGCjtd9sSwSiUxdpnpGvJaoGQNL", "300000",lines[i].strip()])
        list_files.wait()
    f.seek(0)
    for line in lines:
        
        f.write(line)
        print(line)
    