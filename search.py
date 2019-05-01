try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def searchStack(query):
    print("Searching for stackoverlow")
    ret = []
    for j in search(query, tld="co.in", num=6, stop=6, pause=2):
        if "stackoverflow" in j:
            ret.append(j)

    return ret

def searchOther(query, id):
    print("Searching for other links")
    ret = []
    for j in search(query, tld="co.in", num=6, stop=6, pause=2):
        if "github" in j:
            ret.append(j)
        elif "reddit" in j:
            if id not in j:
                ret.append(j)

    return ret

def searchStretch(query):
    print("Searching for stretch links")
    ret = []
    for j in search(query, tld="co.in", num=3, stop=3, pause=2):
        if "github" not in j and "stackoverflow" not in j and "reddit" not in j:
            ret.append(j)

    return ret
