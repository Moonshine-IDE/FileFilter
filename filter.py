import sys
import os
import re

import config
CONFIG = config.CONFIG

def make_pattern(array, flags=0):
    if array:
        return re.compile(
        "(?:" + 
        "|".join(array) + 
        ")", flags)
    else:
        return None

def allow_if(path, pattern):
    if not path: 
        return None
    
    if not pattern:
        return path
    
    if pattern.search(path):
        return path
    else:
        return None


def deny_if(path, pattern):
    if not path: 
        return None
    
    if not pattern:
        return path
    
    if pattern.search(path):
        return None
    else:
        return path


def allow_content_if(path, pattern):
    if not path: 
        return None
    
    if not pattern:
        return path
    
    content = open(path, mode="r", encoding="utf-8").read()
    if pattern.search(content):
        return path
    else:
        return None

def deny_content_if(path, pattern):
    if not path: 
        return None
    
    if not pattern:
        return path
    
    content = open(path, mode="r", encoding="utf-8").read()
    if pattern.search(content):
        return None
    else:
        return path


def main():
    rootDir = sys.argv[1]

    allow_path = make_pattern(CONFIG['path_require_any'], flags = 0)
    deny_path = make_pattern(CONFIG['path_deny_all'], flags = 0)
    allow_content = make_pattern(CONFIG['content_require_any'], re.MULTILINE)
    deny_content = make_pattern(CONFIG['content_deny_all'], re.MULTILINE)

    for root, subdirs, files in os.walk(rootDir):
        for f in files:
            path = os.path.join(root, f)
            match CONFIG['directory_separator']:
                case "/":
                    path = path.replace("\\", "/")
                case "\\":
                    path = path.replace("/", "\\")

            path = allow_if(path, allow_path)
            path = deny_if(path, deny_path)
            path = allow_content_if(path, allow_content)
            path = deny_content_if(path, deny_content)

            if path:
                print(path)


if __name__ == "__main__":
    main()