import snscrape.modules.twitter as sntwitter

for tweet in sntwitter.TwitterSearchScraper("Python").get_items():
    print(tweet.content)
    break
