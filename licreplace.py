import sys
import re

import config
CONFIG = config.CONFIG

paths = sys.stdin
pattern = re.compile(CONFIG['remove_pattern'], re.MULTILINE)

for path in paths:
    stripped = path.strip()

    with open(stripped, "r") as file:
        oldContent = file.read()
        match = pattern.search(oldContent)
        if match:
            oldLicense = match.group(0)        
            newContent = oldContent.replace(oldLicense, CONFIG['new_license'], 1)
            with open(stripped, "w") as file:
                file.write(newContent)
        else:
            print("NO MATCH: " + stripped)
