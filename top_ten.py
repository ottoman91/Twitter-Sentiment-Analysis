import sys
import json 
import operator
def main(): 
    # Extract all tweets from the tweet file
    tweet_file = open(sys.argv[1])  
    tweets = []
    for line in tweet_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass 
    
    #generate the frequency of all hashtags in the tweet file
    hashtag_frequency = {} 
    for tweet in tweets:
        try:
            hashtags = tweet['entities']['hashtags']  
            for hashtag in hashtags:
                if not hashtag['text'] in hashtag_frequency:
                    hashtag_frequency[hashtag['text']] = 1
                else: 
                    hashtag_frequency[hashtag['text']] += 1
        except:
            pass 
    
    #sort and print the top ten hashtags
    sorted_hashtags = sorted(hashtag_frequency.items(),key=operator.itemgetter(1),reverse=True)
    top_ten_hashtags = sorted_hashtags[:10]
    for hashtag in top_ten_hashtags:
        print hashtag[0], hashtag[1] 
     
if __name__ == '__main__':
    main()
