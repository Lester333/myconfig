import subprocess

def menu(options, prompt="Select: "):
    result = subprocess.run(
        ["fuzzel", "--dmenu", "--prompt", prompt],
        input="\n".join(options),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    return result.stdout.strip()


# Retrieve running processes.
# -e: show all processes
# -o: select the columns we want
processes = subprocess.run(
    ["ps", "-eo", "pid,comm"],
    capture_output=True,
    text=True
)

# Remove the header and empty lines.
process_list = processes.stdout.splitlines()[1:]

# Display the process list.
choice = menu(process_list, prompt="Processes: ")

if choice:

    # Extract the PID from the selected line.
    pid = choice.split()[0]

    print("Selected PID:", pid)
