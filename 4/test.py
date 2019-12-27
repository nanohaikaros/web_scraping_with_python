from twitter import *

t = Twitter(auth=OAuth())

pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)

statusUpdate = t.statuses.update(status='Hello,world!')
print(statusUpdate)

pythonStatuses = t.statuses.user_timeline(screen_name='montypython', count=5)
python(pythonStatuses)