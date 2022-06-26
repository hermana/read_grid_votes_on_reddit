from sys import base_exec_prefix
import personal_config
import grid_vote_regex
import votes
import re
import praw

votes = {}

reddit = praw.Reddit(client_id=personal_config.CLIENT_ID, client_secret=personal_config.CLIENT_SECRET, user_agent=personal_config.AGENT)

# TODO: Make an interface to customize this using a url instead.
post_with_grid_votes = reddit.submission("v2l22i")
comments = post_with_grid_votes.comments
# FIXME: does this throw some comments away? 
comments.replace_more(limit=0)

def flip(word):
    first = word[0]
    last = word[1]
    return last + first

def preprocess(comment):
    #replace punctuation with spaces
    comment = re.sub(r"[,.;@#?!&$]+\ *", " ", comment)
    #make all upper case
    return comment.upper()

def add_vote(vote:str):
    if vote in votes:
        votes.update({vote: votes[vote]+1})
    else:
        votes[vote] = 1

for comment in comments:
    processed_comment = preprocess(comment.body)
    comment_text = processed_comment.split()
    for word in comment_text:
        if grid_vote_regex.forwards.match(word):
            # add the item to the dictionary and increment its count.
            # TOD0: trim any commas or punctuation
            add_vote(word)
        elif grid_vote_regex.backwards.match(word):
            # flip it and do the same thing. 
            word = flip(word)
            add_vote(word)
            
print(votes)