import subprocess
import getpass
try:
    while True: 
        func=input("ls or cava?\n>")
        if func == "ls":
            subprocess.run(["ls"])
            break
        if func == "cava":
            subprocess.run(["cava"])
            break
        else:
            subprocess.run(["echo", "I don't understand you. Type either ls or cava."])
except KeyboardInterrupt:
    print("\nsubp.py interrupted by",getpass.getuser())
