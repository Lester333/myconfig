
from pathlib import Path

# Define our categories and their accepted extensions.
categories = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".txt", ".odt"],
    "Archives": [".zip", ".tar", ".gz"],
    "Other": []
}

# Initialize an empty list for every category.
results = {name: [] for name in categories}

# Ask the user for a directory.
directory = Path(input("Directory: ")).expanduser()

# Check whether the directory exists.
if not directory.is_dir():
    print("Error: Invalid directory.")
    exit(1)

# Iterate over directory contents.
for file in directory.iterdir():

    # Ignore subdirectories.
    if not file.is_file():
        continue

    # Extract the extension.
    extension = file.suffix.lower()

    # Find the appropriate category.
    for category, extensions in categories.items():

        if extension in extensions:
            results[category].append(file.name)
            break

    else:
        # The for-else executes if no break occurred.
        results["Other"].append(file.name)

# Display the results.
for category, files in results.items():

    print(f"\n{category}:")

    for filename in files:
        print(f"  {filename}")
    
