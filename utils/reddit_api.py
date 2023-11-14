import praw
import config

reddit = praw.Reddit(
    client_id= config.reddit_client_id,
    client_secret= config.reddit_client_secret,
    user_agent= config.reddit_user_agent,
    username= config.reddit_username,
    password= config.reddit_password
)

subreddit_name = 'CryptoCurrency'  # Example subreddit

# Access the subreddit
subreddit = reddit.subreddit(subreddit_name)

# Fetch and print the titles of the latest posts
for post in subreddit.new(limit=10):  # Fetches the 10 latest posts
    print(post.title)  # Prints the title of each post