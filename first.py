import snscrape.modules.twitter as sntwitter
for tweet in sntwitter.TwitterSearchScraper("elon musk").get_items():
    print(vars(tweet))