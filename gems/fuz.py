import subprocess
from pathlib import Path
import pyperclip
from time import sleep
#FUZZELMENU
def menu(options, prompt=""):
    result = subprocess.run(
        ["fuzzel", "--dmenu", "--prompt", prompt],
        input="\n".join(options),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    return result.stdout.strip()

def fuzzel_input(prompt="Input"):
    result = subprocess.run(
        ["fuzzel","--dmenu", "--prompt-only", prompt, "--width","80"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    return result.stdout.strip()

def wificli():
    subprocess.run(["nmcli","radio","wifi","on"])
    subprocess.run(["nmcli","dev","wifi","rescan"])
    wificon = subprocess.run(
            ["foot","--hold","nmcli","dev","wifi","connect","TP-Link_6F4D_5G","password","75420277"],
            capture_output = True,
            text = True,
            )
    print(wificon.stdout.strip())
    if "Error" in wificon.stdout.strip():
        wificon2 = subprocess.run(
                ["nmcli","dev","wifi","connect","TP-Link_6F4D","password","75420277"],
                capture_output = True,
                text = True,
                )
    if "Error" in wificon2.stdout.strip():
        fuzzel_input("Oopsie! My wifi seems unavailable.")
    
categories = {
        "Imgs":   [".png",".jpg",".jpeg",".webp",".svg",".avif"],
        "Vids":   [".mp4",".m4v",".mov",".qt",".mkv",".webm"],
        "Docs":   [".pdf",".txt",".doc",".docx"],
        "Confs":  [".json",".ini",".toml",".yaml",".yml",".env",".xml",
                   ".conf",".cfg",".properties",".hcl",".jsonc",".json5",".lua"],
        "Archvs": [".zip",".rar",".tar",".gz"],
        "Code":   [".py",".lua",".c",".rs"],
        "Other":  []
        }

# For some reason, fuzzel menus written in python
# are 10x faster than the ones written in bash.
# I always thought it would be vice-versa
def main():
    while True: # I also was struggling so much in the beginning because I didn't wanna use
                # a lot of them while Trues. It turns out it's the only choice
                # for my coding skills yet.

        choice = menu(
            ["Wifi","List files", "Pacman", "Gems", "Exit"], "> "
        )

        if choice == "List files":
            dirinpt="Select a dir: "
            while True:
                try:
                    results = {name: [] for name in categories}
                    dir = fuzzel_input(dirinpt)
                    if dir is None:
                        break
                    chdir = Path(dir.rstrip("\n")).expanduser()
                    if not chdir.is_dir():
                        dirinpt="That dir doesn't exist. Select a real dir: "
                        continue
                    
                    for file in chdir.iterdir():
                        if not file.is_file():
                            continue
                        extension = file.suffix.lower()
                        for category, extensions in categories.items():
                            if extension in extensions:
                                results[category].append(file.name)
                                break
                        else:
                            results["Other"].append(file.name)
                        
                    for k in list(results.keys()):
                        if len(results[k]) == 0:
                            del results[k]

                    dirinpt="Select a dir: " # Returns dirinpt back to normal
                                             # for user to esc back and see a normal prompt
                                             # instead of "Select a REAL dir! >:("
                except PermissionError:
                    pass # This allows you to access locked dirs.
                         # I wanted to add a sudo password confirmation,
                         # but since it's just an abslute-path copying tool,
                         # I decided not to.
                while True:
                    options = {
                        f"{key} ({len(value)})": key
                        for key, value in results.items()
                    }
                    cat = menu(list(options.keys()),"Categories: ")
                    if cat is None:
                        break
                    else:
                        while True:
                            file = menu(results[options[cat]],"Copy file path to clipboard: ")
                            if file is not None:
                                filepath = (chdir / Path(file)).resolve()
                                pyperclip.copy(str(filepath))
                            else: break
        
        elif choice == "Pacman":
            method = menu(["Install","Update"],"> ")
            if method == "Install":
                pkgs = fuzzel_input("Pkgs: ").split()
                subprocess.Popen(
                        ["foot","sudo","pacman","-S",*pkgs]
                        )
                break

            elif method == "Update":
                subprocess.Popen(
                        ["foot","sudo","pacman","-Syu"]
                        )
                break
        elif choice == "Gems":
            gemlist = []
            gems = Path("~/gems").expanduser()
            for gem in gems.iterdir():
                if gem.is_file():
                    gemlist.append(gem.name)
            chgem = menu(gemlist,">")
            if chgem is not None:
                subprocess.run(
                    ["foot","nvim",f"/home/stock/gems/{str(chgem)}"]
                    )
                break
            else: break
            
        elif choice == "Wifi":
            wificli()
            
            
            
        elif choice == "Exit" or not choice:
            break

if __name__ == "__main__":
    main()
