import sys
import json

def main(): 
    #get the term scores stored
    scores = {}
    afinnfile = open(sys.argv[1]) 
    for line in afinnfile:
        term, score = line.split("\t")
	scores[term] = int(score)
    
    # Extract text of all tweets 
    tweet_file = open(sys.argv[2])  
    tweets = []
    for line in tweet_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass 
    
    #obtain all terms from the AFINN-111 File
    terms = scores.keys()
    
    #loop through every tweet to find out its score
    for tweet in tweets:
        score = 0
        try:
            text = tweet['text'] 
            words = text.split(" ")  
            matches = set(words) & set(terms)  
            for match in matches:
                score = score + scores[match] 
            print score
        except:
            pass
        
if __name__ == '__main__':
    main()
