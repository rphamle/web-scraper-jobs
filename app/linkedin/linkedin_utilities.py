import json

def writeResultToFile(result, filename, indent_level):
    with open(filename, 'w') as f:
        f.write(json.dumps(result, indent = indent_level))

def getResultInJson(**kwargs):
    return {key:value for key, value in kwargs.items()}
