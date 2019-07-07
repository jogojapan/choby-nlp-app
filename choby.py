from choby_init import ChobyInit

class Choby:
    def __init__(self):
        init = ChobyInit()
        self.api = init.api

def strNone(string):
    if string is None:
        return 'None'
    else:
        return string
        
if __name__ == '__main__':
    choby = Choby()
    stream = choby.api.GetStreamFilter(track=['amazon.co.jp'], languages=['ja','und'])
    num = 0
    for tweet in stream:
        #print(tweet)
        print(
            '  '+strNone(tweet['created_at']),
            '  '+strNone(tweet['user']['screen_name']),
            '  '+strNone(tweet['geo']),
            '  '+strNone(tweet['coordinates']),
            '  '+strNone(tweet['lang'])
        )
        print(tweet['text'].replace('\n',' '))
        print(tweet['entities']['hashtags'])
        print()
        num += 1
        if num > 100:
            break
