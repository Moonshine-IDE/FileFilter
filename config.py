from pathlib import Path

CONFIG = {
    "directory_separator": "/",
    "path_require_any": [
        r"\.as$",
        r"\.mxml$",
        r"\.java$",
        r"\.js$",
        r"\.ts$",
    ],
    "path_deny_all": [
        r"/\.",
        r"/bin-debug/",
        r"/node_modules/",
        r"/nativeExtension/",
        r"/MoonshineSharedCore/src/elements/",
        r"/extResources/",
        r"/ericfeminella/",
        r"/src/no/doomsday/",
        r"/html-template/",
        r"/library/ApacheFlexSDKInstallerLib/",
        r"/org/as3commons/asblocks/",
        r"/tourDeFlex/",
    ],
    "content_require_any": [
    ],
    "content_deny_all": [
        r"Copyright 2007 Adobe Systems Incorporated",
        r"Copyright \(c\) 2006 Darron Schall <darron@darronschall\.com>",
        r"Author: Victor Dramba",
        r"Copyright \(c\) 2016-2021 Vegard IT GmbH",
        r"@author Michael Schmalle",
        r"@author Chris Callendar",
        r"Copyright 2010 Michael Schmalle - Teoti Graphix, LLC",
        r"Copyright \(c\) Mike Stead 2009, All rights reserved\.",
        r"Code written by Doug McCune",
        r"http://www\.mongodb\.com/licensing/server-side-public-license", # SSPL License
    ],
    "remove_pattern": r"(?<=\<\?xml version=\"1.0\" encoding=\"utf-8\"\?>)\n",
    "new_license": Path("./in/sspl-xml.txt").read_text()
}

# r"^/////[\s\S]+(?:Prominic)[\s\S]+(?:http://www\.apache\.org/licenses/LICENSE-2\.0)[\s\S]+/////$" # Prominic Apache License
# r"^/////[\s\S]+(?:http://www\.apache\.org/licenses/LICENSE-2\.0)[\s\S]+/////$", # Any Apache License with //
# r"^<!--\s+Licensed[\s\S]+(?:http://www\.apache\.org/licenses/LICENSE-2\.0)[\s\S]+License\.\s+-->$", # Any Apache License with <!--
# r"http://www\.mongodb\.com/licensing/server-side-public-license", # SSPL License