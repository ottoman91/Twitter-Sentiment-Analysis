import sys
import json 
from decimal import *  
import operator
getcontext().prec = 6

def main(): 
    #store the term scores 
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

    #dictionary of US state abbreviations and state names
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
} 
    #list of US state abbreviations
    state_abbreviations = states.keys()
    
    #dictionary of states and their total sentiment score
    states_sentiment_scores = {}  

    #dictionary of states and number of tweets
    states_number_of_tweets = {} 

    #dictionary of states and average sentiment scores
    states_average_sentiment_scores = {}

    
    for tweet in tweets: 
        score = 0
        try: 
            location_info = tweet['user']['location']
            location = location_info.split(" ")
            state_matches = set(state_abbreviations) & set(location)

            if len(state_matches) > 0:  
                text = tweet['text']
                words = text.split(" ")
                term_matches = set(words) & set(terms)

                for match in term_matches:
                    score = score + scores[match] 

                for state_match in state_matches:
                    if not state_match in states_number_of_tweets:
                        states_number_of_tweets[state_match] = 1 
                    else:
                        states_number_of_tweets[state_match] += 1

                    if not state_match in states_sentiment_scores:
                        states_sentiment_scores[state_match] = score 
                    else:
                        states_sentiment_scores[state_match] += score 

                    
        except:
            pass  
    
    for key in states_number_of_tweets:
        states_average_sentiment_scores[key] = Decimal(states_sentiment_scores[key]) / Decimal(states_number_of_tweets[key]) 
     
    sorted_state_sentiment_scores = sorted(states_average_sentiment_scores.items(),key=operator.itemgetter(1),reverse=True) 
    #print sorted_state_sentiment_scores
    print sorted_state_sentiment_scores[0][0]

        
if __name__ == '__main__':
    main()
