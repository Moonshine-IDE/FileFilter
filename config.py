from pathlib import Path

CONFIG = {
    "directory_separator": "/",
    "path_require_any": [
        r"\.as$",
        r"\.mxml$",
        # r"\.java$",
        # r"\.js$",
        # r"\.ts$",
    ],
    "path_deny_all": [
        r"/obj/",
        r"/ApacheFlexSDKInstallerLib/",
    ],
    "content_require_any": [
        r"http://www\.apache\.org/licenses/LICENSE-2\.0",
    ],
    "content_deny_all": [
        r"http://www\.mongodb\.com/licensing/server-side-public-license",
        r"Copyright \(c\) 2009 H. Paul Robertson",
        r"Ported from",
        r"Copyright \(c\) 2007 Henri Torgemane",
        r"Copyright \(C\) 2012 Jean-Philippe Auclair",
    ],
    "remove_pattern": r"^\/\*\s+Licensed[\s\S]+(?:http://www\.apache\.org/licenses/LICENSE-2\.0)[\s\S]+License\.\s+\*\/$",
    "new_license": Path("./in/sspl.txt").read_text()
}

# r"^/////[\s\S]+(?:Prominic)[\s\S]+(?:http://www\.apache\.org/licenses/LICENSE-2\.0)[\s\S]+/////$" # Prominic Apache License
# r"^/////[\s\S]+(?:http://www\.apache\.org/licenses/LICENSE-2\.0)[\s\S]+/////$", # Any Apache License with //
# r"^<!--\s+Licensed[\s\S]+(?:http://www\.apache\.org/licenses/LICENSE-2\.0)[\s\S]+License\.\s+-->$", # Any Apache License with <!--
# r"^\/\*\s+Licensed[\s\S]+(?:http://www\.apache\.org/licenses/LICENSE-2\.0)[\s\S]+License\.\s+\*\/$", # Any Apache License with /*
# r"\/\*[\s\S]+(?:http://www.apache.org/licenses/LICENSE-2.0)[\s\S]+\*\/$", # Any Apache License with block /*
# r"http://www\.mongodb\.com/licensing/server-side-public-license", # SSPL License