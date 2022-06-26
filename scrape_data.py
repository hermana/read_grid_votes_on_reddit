import personal_config
import praw

reddit = praw.Reddit(client_id=personal_config.CLIENT_ID, client_secret=personal_config.CLIENT_SECRET, user_agent=personal_config.AGENT)
