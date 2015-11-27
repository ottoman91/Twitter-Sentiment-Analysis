# Twitter-Sentiment-Analysis
This project was completed as part of the "Data Manipulation at Scale: Systems and Algorithms" MOOC on Coursera. 
The following were the objectives of this project:

1. Accessing the Twitter Application Programming Interface(API) using Python to download a live stream of Tweets.

2. Estimating the public's perception (the sentiment) of a particular term or phrase in a tweet.

3. Analyzing the relationship between location and mood based on a  sample of twitter data 

##Scripts in this Project
The following is a list of the Scripts in this project, along with a brief explanation of what they do.

* **AFINN-111.txt**. AFINN is a list of English words rated for valence with an integer between minus five (negative) and plus five (positive). The words have been manually labeled by Finn Arup Nielsen in 2009-2011. The file is tab-separated. We use the AFINN-111.txt file to find out the initial sentiment of tweets. 

* **twitterstream.py**. This python script downloads the tweets from a Twitter account via using the Twitter API. To use this script, do the following:
a. Enter the api_key, the api_secret, the access_token_key and the access_token_secret values for the Twitter application that you have created from your account. 
b. Output the Twitter stream into a text file via running the following:
**python twitterstream.py > output.txt** 

* **tweet_sentiment.py**. This python script reads through all of the tweets downloaded, and based on the occurance of words from the AFINN-111 file in the tweets, it assigns a sentiment score to every tweet. Run the script in the following way:
**python tweet_sentiment.py AFINN-111.txt output.txt** 

* **term_sentiment.py**. This script is used to figure out the sentiments of words in the tweets that are not included in the AFINN-111 file. The following is the logic I used for developing a sentiment metric:
1. For every tweet, compute the positive as well as the negative scores of any words present whose sentiments are listed in the AFINN text file. Also, note down the number of positive and negative sentiments present in every tweet.
2. For every tweet, find out the list of words whose sentiments are not calculated. To each of these words, assign the positive and negative sentiment scores,as well as the number of positive and negative words that it is in close proximity to.
3. After running through all of the tweets,for every word whose sentiments need to be calculated, multiply its total positive sentiment value by the total number of positive words it is in close proximity to and divide this by the total number of tweets in which the word is present. Lets call this number a. Then, multiply the total negative sentiment value by the total number of negative words the word is in close proximity to,and divide this by the total number of tweets in which the word is present. Lets call this number b. The sentiment of every new term would be equal to a - b. 
Run the script in the following way: **python term_sentiment.py AFINN-111.txt output.txt**

* **frequency.py** This script is used to compute the term frequency of the livestream twitter data that we have downloaded. 
Run the script in the following way: **python frequency.py output.txt** 

* **happiest_state.py** This script uses the user field in every Tweet to determine the state from which the Tweet originated. By using the AFINN-111.txt file to determine the sentiment of every tweet, this script displays the initials of the state that has the highest average positive sentiment.Run the script in the following way: **python happiest_state.py AFINN-111.txt output.py**

* **top_ten.py** This script prints the top ten hashtags from the twitter data downloaded. Run the script in the following way:
**python top_ten.py output.txt**
