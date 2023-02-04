from packaging import version

with open('version.txt') as file:
    currentVersion = file.read()

    if isinstance(version.parse(currentVersion), version.Version): # version not invalid
        ...
    else:
        raise version.InvalidVersion()