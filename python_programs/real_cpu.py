# python -m pip install psutil
import psutil
# print(psutil.cpu_times())
# print(psutil.cpu_percent(interval=1))
# print(dir(psutil))
# print(psutil.subprocess.__doc__)

# for i in range(5):
#     print(psutil.cpu_percent(interval=1))

#check cpu usage for 5 sec and take a threshold from user and check if cpu is healthy or not

threshold= float(input("Enter the threshold: "))

for i in range(5):
    if psutil.cpu_percent(interval=1) > threshold:
        print("CPU is not healthy")
    else:
        print("CPU is healthy")