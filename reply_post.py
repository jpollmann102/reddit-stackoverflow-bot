import praw
import os
from search import searchStack
from search import searchOther
from search import searchStretch
from formatReply import formatResponse

reddit = praw.Reddit('bot1')

# retrieve tracking
if not os.path.isfile("postsRepliedTo.txt"):
    postsRepliedTo = []
else:
    with open("postsRepliedTo.txt", "r") as f:
        postsRepliedTo = f.read()
        postsRepliedTo = postsRepliedTo.split("\n")
        postsRepliedTo = list(filter(None, postsRepliedTo))

# reply to posts
subreddit = reddit.subreddit('learnprogramming')
for submission in subreddit.new(limit=5):
    id = submission.id
    if id not in postsRepliedTo:
        # do the stuff here
        title = submission.title
        stackPosts = searchStack(title)
        otherPosts = searchOther(title, id)
        stretchPosts = searchStretch(title)
        response = formatResponse(stackPosts, otherPosts, stretchPosts)
        try:
            submission.reply(response)
            postsRepliedTo.append(id)
            print("Bot replied to ", title)
        except NameError:
            print("Something was not defined?")
        except:
            print("Error occurred, you are doing that too much")
            break


# update tracking
with open("postsRepliedTo.txt", "w") as f:
    for postId in postsRepliedTo:
        f.write(postId + "\n")
