def formatResponse(stackPosts, otherPosts, stretchPosts):
    footerString = "------------------------------------\n^I ^am ^a ^bot, ^contact ^/u/thatoneguy102 ^for ^questions"
    responseString = "Hi, I'm a bot and I found some links that may be useful for you!\n\n{}{}{}{}".format(
                        stackFound(stackPosts),
                        otherFound(otherPosts),
                        stretchFound(stretchPosts),
                        footerString)
    return responseString

def stackFound(stackPosts):
    if len(stackPosts) is not 0:
        stackString = "**StackOverflow posts:**\n\n"
        i = 1
        for post in otherPosts:
            postString = "* [Link {}]({})\n\n".format(i, post)
            i = i + 1
            stackString = stackString + postString
    else:
        stackString = "**No StackOverflow posts found :(**\n\n"

    return stackString

def otherFound(otherPosts):
    if len(otherPosts) is not 0:
        otherString = "**Other posts that may be helpful:**\n\n"
        i = 1
        for post in otherPosts:
            postString = "* [Link {}]({})\n\n".format(i, post)
            i = i + 1
            otherString = otherString + postString
        return otherString
    return "\n"

def stretchFound(stretchPosts):
    stretchString = "**These links may be a stretch:**\n\n"
    i = 1
    for post in stretchPosts:
        postString = "* [Link {}]({})\n\n".format(i, post)
        i = i + 1
        stretchString = stretchString + postString
    return stretchString
