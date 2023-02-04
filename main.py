from packaging import version
import requests

page = requests.get("https://raw.githubusercontent.com/Tomz3n/autoupdate/main/version.txt")
with open('version.txt') as file:
    currentVersion = version.parse(file.read())
    latestVersion = version.parse(page.text)

    if isinstance(currentVersion, version.Version) and isinstance(latestVersion, version.Version): # version not invalid
        if latestVersion > currentVersion: # not up to date
            print("Script is out of date")
            # perform script downloads and extraction here
        else:
            print("Script is up to date.")
    else:
        raise version.InvalidVersion()