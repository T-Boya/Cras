from decouple import config
import twitter
twitterapi = twitter.Api()

twitterapi = twitter.Api(consumer_key=config('Tconsumer_key'),
                  consumer_secret=config('Tconsumer_secret'),
                  access_token_key=config('Taccess_token_key'),
                  access_token_secret=config('Taccess_token_secret'))
