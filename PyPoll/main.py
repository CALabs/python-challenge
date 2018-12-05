#!/usr/bin/env python
# coding: utf-8

# In[70]:


#Pandas activation
import pandas as pd


# In[71]:


#Import the CSV file
PyPoll_file = 'Resources/election_data.csv'
#read the CSV file
PyPoll_df = pd.read_csv(PyPoll_file)

PyPoll_df.head()


# In[72]:


#The total number of votes
Vote_count = PyPoll_df["Voter ID"].count()
Vote_count


# In[73]:


#A complete list of candidates who received votes
Candidates_WV = PyPoll_df["Candidate"].unique().tolist()
Candidates_WV
#Candidates_df = pd.DataFrame(Candidates_WV)
#Candidates_df.columns = ['Candidates With Votes']
#Candidates_df


# In[74]:


#The percentage of votes each candidate won - Khan
Vote_khan = PyPoll_df.query("Candidate =='Khan'")["Candidate"].count()
#Vote_khan
# Percentage
Vote_khanp = round((Vote_khan / Vote_count)*100,3)
Vote_khanp


# In[75]:


#The percentage of votes each candidate won - Correy
Vote_Correy = PyPoll_df.query("Candidate =='Correy'")["Candidate"].count()
#Vote_khan
# Percentage
Vote_Correyp = round((Vote_Correy / Vote_count)*100,3)
Vote_Correyp


# In[76]:


#The percentage of votes each candidate won - LI
Vote_Li = PyPoll_df.query("Candidate =='Li'")["Candidate"].count()
#Vote_khan
# Percentage
Vote_Lip = round((Vote_Li / Vote_count)*100,3)
Vote_Lip


# In[77]:


#The percentage of votes each candidate won - O'Tooley
Vote_OTooley = (Vote_count - Vote_khan - Vote_Correy - Vote_Li)
#Vote_khan
# Percentage
Vote_OTooleyp = round((Vote_OTooley / Vote_count)*100,3)
Vote_OTooleyp


# In[79]:

print("Election Results")
print("-----------------")
print("Total Votes: " + str(Vote_count))
print("-----------------")
print("Khan: " + str(Vote_khanp) + "%  (" + str(Vote_khan) +")")
print("Correy: " + str(Vote_Correyp) + "%  (" + str(Vote_Correy) +")")
print("Li: " + str(Vote_Lip) + "%  (" + str(Vote_Li) +")")
print("O'Tooley: " + str(Vote_OTooleyp) + "%  (" + str(Vote_OTooley) +")")
print("-----------------")
print("Winner: Khan")

import sys
sys.stdout = open('Election Results.txt','wt')

print("Election Results")
print("-----------------")
print("Total Votes: " + str(Vote_count))
print("-----------------")
print("Khan: " + str(Vote_khanp) + "%  (" + str(Vote_khan) +")")
print("Correy: " + str(Vote_Correyp) + "%  (" + str(Vote_Correy) +")")
print("Li: " + str(Vote_Lip) + "%  (" + str(Vote_Li) +")")
print("O'Tooley: " + str(Vote_OTooleyp) + "%  (" + str(Vote_OTooley) +")")
print("-----------------")
print("Winner: Khan")


# In[ ]:





# In[ ]:




