import subprocess

subprocess.run(
        ["nmcli","dev","wifi","rescan"]
        )
wifilist = subprocess.run(
    ["nmcli","dev","wifi","list"],
    capture_output=True,
    text=True,
    )
print(wifilist.stdout.strip())
