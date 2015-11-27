import sys
import json 
from decimal import * 
getcontext().prec = 4
def main(): 
    # Extract all tweets from the tweet file
    tweet_file = open(sys.argv[1])  
    tweets = []
    for line in tweet_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass 
    
    #generate the frequency of all words in the tweet file
    words_frequency = {}
    for tweet in tweets:
        try:
            text = tweet['text'] 
            words = text.split(" ")  
            for word in words:
                if not word in words_frequency:
                    words_frequency[word] = 1
                else:
                    words_frequency[word] += 1  
             
            
        except:
            pass
    #print words_frequency 

    #calculate the term frequency of every word
    total_words = 0 
    for words in words_frequency:
    	total_words += words_frequency[words] 
    #print total_words 
    for word in words_frequency:
    	term_frequency = Decimal(words_frequency[word]) / Decimal((total_words)) 
        #print term_frequency
        print word, term_frequency
        
if __name__ == '__main__':
    main()
