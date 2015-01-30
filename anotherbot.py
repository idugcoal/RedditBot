import praw
r = praw.Reddit('praw test bot')

for i in xrange(0,10):
	comments = r.get_comments('sportsbook')
	for comment in comments:
		body = comment.body.lower()
		if body.find("warriors") != 1 or body.find("GSW") != 1:
			print body