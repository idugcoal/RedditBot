import praw

r = praw.Reddit(user_agent = "TutorialBot by /u/idugcoal")
r.login()

words_to_match = ['defiantly', 'definitly', 'definately', 'definatly']

def run_bot():
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit=25)
	for comment in comments:
		comment_text = comment.body
		