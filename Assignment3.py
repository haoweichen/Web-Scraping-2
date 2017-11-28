
# coding: utf-8

# In[1]:


import string
from string import punctuation
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import json
import matplotlib.pyplot as plt

consumer_key = 'i2Eego1GgNga1ND3Oxpq2wwxm'
consumer_secret = '2bNZvOqlg7MvqQeCsqP7Ma64Gh77xCvdmlNI5Th6SmfxLELQQu'
access_token = '1373172530-UqKl5faRYzTWuYnC6TcocHMOgUhbzS2cjVZH59M'
access_secret = 'P9JV8cJl36RpA2MA7GEGz73kMO8kTApPyLXaFYcCMPVJi'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class Text_Analyzer(object):

    def __init__(self, input_file):
        # add code to initialize an instance
        self.input_file = input_file
        #self.output_file = output_file
          
    def analyze(self):
        tweets=[]
        with open(self.input_file, 'r') as f:
            tweettext_content=""
            for line in f: 
                tweet = json.loads(line)
                tweettext_content += tweet.get("text").rstrip("\n")
                tweets.append(tweet)
                #print tweet.get("text")
            #print tweettext_content
            tweettext_content_list = tweettext_content.split()
            #print tweettext_content_list
            json.dump(tweets, open("all_tweets.json",'w'))
            tweets=json.load(open("all_tweets.json",'r'))
        
    
            count_tweettext={}
            for x in tweettext_content_list:
                x = x.lower()
                x = x.strip(punctuation)
                if x == "":
                    continue
                if x in count_tweettext:
                    count_tweettext[x]+=1
                else:
                    count_tweettext[x]=1
            count_tweettext_list=count_tweettext.items()
            tweettext_result = sorted(count_tweettext_list , key=lambda item:-item[1])
    #print tweettext_result
    
            top_50_words=tweettext_result[0:50]
            words, counts=zip(*top_50_words)
            print(words, counts)
    #tweettext_count_list=tweettext_result.items()
    
    
    
            count_per_topic={}
            for t in tweets:
                if "entities" in t and "hashtags" in t["entities"]:
                    topics=set([hashtag["text"].lower() for hashtag in t["entities"]["hashtags"]])
        
                    for topic in topics:
                        topic=topic.lower()
                        if topic in count_per_topic:
                            count_per_topic[topic]+=1
                        else:
                            count_per_topic[topic]=1
      
            topic_count_list=count_per_topic.items()
            sorted_topics=sorted(topic_count_list, key=lambda item:-item[1])
            #print(sorted_topics)
    
            x_pos = range(len(words))
            plt.bar(x_pos, counts)
            plt.xticks(x_pos, words)
            plt.ylabel('Count of Text of Tweet')
            plt.title('Count of Text per Word')
            plt.xticks(rotation=90)
            plt.show()

            #top_50_topics=sorted_topics[0:50]

            topics, counts=zip(*sorted_topics)
            #print("\nTopics and counts in separated tuples:")
            print(topics, counts)
    
            # get a range as the horizontal position of each topic
            x_pos = range(len(topics))
    
            # plot the bar chat
            plt.bar(x_pos, counts)
    
            # add the legend of each bar
            plt.xticks(x_pos, topics)
    
            # add the label for Y-axis
            plt.ylabel('Count of Tweets')
    
            # add title
            plt.title('Count of Tweets per Topic')
    
            # vetically align the text of each topic
            plt.xticks(rotation=90)
    
            # display the plot
            plt.show()
        

if __name__ == "__main__":  
    
    analyzer=Text_Analyzer("python.txt")
    vocabulary=analyzer.analyze()



        
        
        
         









