from sys import base_exec_prefix
import personal_config
import grid_vote_regex
import votes
import re
import praw


def flip(word):
    first = word[0]
    last = word[1]
    return last + first


def preprocess(comment):
    comment = re.sub(r"[,.;@#?!&$-/]+\ *", " ", comment)
    return comment.upper()

def get_url():
    return input('Please enter the url of the grid on reddit: ')

grid_votes = votes.Votes()
reddit = praw.Reddit(client_id=personal_config.CLIENT_ID, client_secret=personal_config.CLIENT_SECRET, user_agent=personal_config.AGENT)
url = get_url()
post_with_grid_votes = reddit.submission(url=url)
comments = post_with_grid_votes.comments
comments.replace_more(limit=None)


# FIXME: lambda?
for comment in comments:
    processed_comment = preprocess(comment.body)
    comment_text = processed_comment.split()
    for word in comment_text:
        if grid_vote_regex.forwards.match(word):
            grid_votes.add_vote(word)
        elif grid_vote_regex.backwards.match(word):
            word = flip(word)
            grid_votes.add_vote(word)
            
print(grid_votes.votes)