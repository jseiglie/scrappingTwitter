import snscrape.modules.twitter as sntwitter
import pandas as pd

#query = "(from:GirlsInTech) until:2022-11-07 since:2021-01-01"
#query = "#python"
#query = "JavierSeiglie"
query = "#covid19 -filter:retweets"
tweets = []
limit = 500


for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
#df.to_csv('tweets.csv')