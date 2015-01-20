import praw
import time

r = praw.Reddit(user_agent = "TutorialBot by /u/idugcoal")
print("Logging in...")
r.login()

words_to_match = ['defiantly', 'definitly', 'definately', 'definatly', 'definantly']
cache = []

def run_bot():
	print("Grabbing subreddit...")
	subreddit = r.get_subreddit("test")
	print("Grabbing comments...")
	comments = subreddit.get_comments(limit=25)
	for comment in comments:
		comment_text = comment.body
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch:
			print("Match found! Comment ID: " + comment.id)
			comment.reply("I think you meant to say 'definitely.'")
			print("Reply successful!")
			cache.append(comment.id)
	print("Comments loop finished. Time to sleep")

while True:
	run_bot()
	time.sleep(10)