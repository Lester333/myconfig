import time 
import psutil
try:
    while True:
        ram = psutil.virtual_memory()
        used = float(ram.used / (1024 ** 3))
        print("\r",used,end="                     ")
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
