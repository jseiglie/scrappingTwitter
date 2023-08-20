from snscrape.modules.twitter import TwitterSearchScraper
scraper = TwitterSearchScraper('omicron variant')

result = []

for i, item in enumerate(scraper.get_items()):
        result.append(item)
        if i == 100:
                break