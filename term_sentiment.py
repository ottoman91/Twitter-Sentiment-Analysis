import sys
import json
from decimal import *  
import operator
getcontext().prec = 6

def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]
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
    #dictionary for storing values for new terms
    new_terms = {}
    new_positive_scores = {}
    new_negative_scores = {}
    new_num_positives = {}
    new_num_negatives = {}

    #obtain all terms from the AFINN-111 File
    terms = scores.keys()
    
    #loop through every tweet to find out its score
    for tweet in tweets:
        score = 0 
        positive_score = 0
        negative_score = 0
        num_positive = 0
        num_negative = 0
        try:
            text = tweet['text'] 
            words = text.split(" ")  
            matches = set(words) & set(terms)  
            for match in matches:
                score = score + scores[match]
                if scores[match] > 0:
                    positive_score += scores[match]
                    num_positive += 1
                else:
                    negative_score += scores[match]
                    num_negative += 1
            new_words = diff(words, matches)
            if len(new_words) > 0:
                for new_word in new_words:
                    if not new_word in new_terms:
                        new_terms[new_word] = new_word
                        new_positive_scores[new_word] = positive_score
                        new_negative_scores[new_word] = negative_score
                        new_num_positives[new_word] = num_positive
                        new_num_negatives[new_word] = num_negative 
                    else:
                        new_positive_scores[new_word] += positive_score
                        new_negative_scores[new_word] += negative_score
                        new_num_positives[new_word] += num_positive
                        new_num_negatives[new_word] += num_negative 
        

            

            
            
        except:
            pass 
    for new_term in new_terms: 
        n = Decimal(new_num_negatives[new_term]) + Decimal(new_num_positives[new_term])
        try:
            a = Decimal(new_positive_scores[new_term]) * Decimal(new_num_positives[new_term]) / Decimal(n)
        except:
            pass
        try:
            b = Decimal(new_negative_scores[new_term]) * Decimal(new_num_negatives[new_term]) / Decimal(n)
        except:
            pass
        score = a + b 
        print new_term, score 
        
if __name__ == '__main__':
    main()
