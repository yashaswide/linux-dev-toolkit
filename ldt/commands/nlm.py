import re

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")

except Exception:
    spacy = None
    nlp = None


def extract_location(text):

    locations = [
        "desktop",
        "downloads",
        "documents"
    ]

    for loc in locations:
        if loc in text:
            return loc

    return None


def understand(sentence):

    # spaCy unavailable
    if nlp is None:
        print("spaCy model not available.")

        return {
            "intent": None,
            "file": None,
            "folder": None,
            "number": None,
            "location": None
        }

    # preprocess
    text = sentence.lower()

    print("DEBUG text:", text)

    # create spaCy document
    doc = nlp(text)

    # result object
    result = {
        "intent": None,
        "file": None,
        "folder": None,
        "number": None,
        "location": None
    }

    # -------------------------
    # INTENT DETECTION
    # -------------------------

    verbs = [token.lemma_ for token in doc]

    print("DEBUG verbs:", verbs)

    # CREATE
    if any(v in verbs for v in [
        "create",
        "make",
        "build",
        "generate"
    ]):
        result["intent"] = "create"

    # DELETE
    elif any(v in verbs for v in [
        "delete",
        "remove",
        "erase"
    ]):
        result["intent"] = "delete"

    # RENAME
    elif any(v in verbs for v in [
        "rename",
        "change"
    ]):
        result["intent"] = "rename"

    # SHOW / DISPLAY
    elif any(v in verbs for v in [
        "show",
        "display",
        "list"
    ]):

        if "last" in text:
            result["intent"] = "tail"

        elif "first" in text:
            result["intent"] = "head"

        else:
            result["intent"] = "show"

    # GOTO
    elif any(v in verbs for v in [
        "go",
        "open",
        "move"
    ]):
        result["intent"] = "goto"

    # -------------------------
    # NUMBER EXTRACTION
    # -------------------------

    for token in doc:
        if token.like_num:
            try:
                result["number"] = int(token.text)
            except ValueError:
                pass

    # -------------------------
    # FILE DETECTION
    # -------------------------

    file_match = re.search(
        r"\b[\w\-]+\.[a-zA-Z0-9]+\b",
        text
    )

    if file_match:
        result["file"] = file_match.group()

    # -------------------------
    # FOLDER DETECTION
    # -------------------------

    folder_match = re.search(
        r"(folder (named )?|called )(\w+)",
        text
    )

    if folder_match:
        result["folder"] = folder_match.group(3)

    # -------------------------
    # LOCATION DETECTION
    # -------------------------

    result["location"] = extract_location(text)

    return result