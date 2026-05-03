import os
import re

# -----------------------------
# Location map
# -----------------------------
LOCATIONS = {
    "desktop": "~/Desktop",
    "downloads": "~/Downloads",
    "documents": "~/Documents"
}

# -----------------------------
# INTENT DETECTION
# -----------------------------
def detect_intent(text):
    text = text.lower()

    if re.search(r"\b(create|make|new)\b.*\bfile\b", text):
        return "create_file"

    return None


# -----------------------------
# ENTITY EXTRACTION
# -----------------------------
def extract_file(text):
    match = re.search(r"(\w+\.\w+)", text)
    return match.group(1) if match else None


def extract_folder(text):
    match = re.search(r"folder (\w+)", text)
    return match.group(1) if match else "default"


def extract_location(text):
    match = re.search(r"(desktop|downloads|documents)", text)
    return match.group(1) if match else "desktop"


# -----------------------------
# EXECUTION LAYER
# -----------------------------
def create_file(file_name, folder_name, location):
    base_path = os.path.expanduser(LOCATIONS[location])

    folder_path = os.path.join(base_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as f:
        pass

    print("\nCREATED file:", file_name)
    print("folder:", folder_name)
    print("path:", file_path)


# -----------------------------
# MAIN ENTRY
# -----------------------------
def run_sentence(sentence):
    text = sentence.lower()

    intent = detect_intent(text)

    if intent == "create_file":
        file_name = extract_file(text)
        folder_name = extract_folder(text)
        location = extract_location(text)

        if not file_name:
            print("❌ Could not find file name")
            return

        create_file(file_name, folder_name, location)

    else:
        print("❌ Unsupported command")