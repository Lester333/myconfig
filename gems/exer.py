#So that's kinda how they created ls...

import getpass
import pathlib
from pathlib import Path

# \/ To remove all the eyesore when u KeyboardInterrupt a python script
def ctrl_c(func):
    def wrapper(*args, **kwargs):
        try: return func(*args, **kwargs)
        except KeyboardInterrupt: print("\nInterrupted by user.")
    return wrapper

@ctrl_c
def scanner():
    
    username = getpass.getuser()

    while True:
        chosendir_str = str(input(f"Select a dir: "))
        chosendir_str = chosendir_str.replace("~/", f"/home/{username}/")
        chdir = Path(chosendir_str)
        if chdir.is_dir() and chdir.exists(): break
        else: print("\nThat dir doesn't exist. Perhaps you made a typo or forgot to create it?\n"
                    "Or it's so locked and secret that this script cannot even read it...\n") 

    Imagesarr = [".png",".jpg",
              ".jpeg",".webp",
              ".svg",".avif"]
    Videosarr = [".mp4",".m4v",
              ".mov",".qt",
              ".mkv",".webm"]
    Archivesarr = [".zip",".rar"]
    Codearr = [".py",".lua",".c",".rs"] #etc
    Configarr = [".json",".ini",
              ".toml",".yaml",".yml",
              ".env",".xml",".conf",
              ".cfg",".properties",".hcl",
              ".jsonc",".json5",]
    Docsarr = [".doc",".docx",".pdf",".txt"]

    #  \/ These are to be filled up with filenames later
    Images=[]
    Videos=[]
    Archives=[]
    Code=[]
    Config=[]
    Docs=[]
    
    try:
        for file in chdir.iterdir():
            if file.is_file() and file.suffix.lower() in Imagesarr:
                Images.append(file)
            elif file.is_file() and file.suffix.lower() in Videosarr:
                Videos.append(file)
            elif file.is_file() and file.suffix.lower() in Archivesarr:
                Archives.append(file)
            elif file.is_file() and file.suffix.lower() in Codearr:
                Code.append(file)
            elif file.is_file() and file.suffix.lower() in Configarr:
                Config.append(file)
            elif file.is_file() and file.suffix.lower() in Docsarr:
                Docs.append(file)
            else: pass
    except PermissionError: print("\nPermission denied for this dir.\nTry using sudo.")

    if len(Images)>0: print("\n____IMAGES____")
    print(", ".join([f.name for f in Images]))
    if len(Videos)>0: print("\n____VIDEOS____")
    print(", ".join([f.name for f in Videos]))
    if len(Archives)>0: print("\n____ARCHIVES____")
    print(", ".join([f.name for f in Archives]))
    if len(Code)>0: print("\n____CODE____")
    print(", ".join([f.name for f in Code]))
    if len(Config)>0: print("\n____CONFIG____")
    print(", ".join([f.name for f in Config]))
    if len(Docs)>0: print("\n____DOCS____")
    print(", ".join([f.name for f in Docs]))

if __name__ == "__main__":
    scanner()

