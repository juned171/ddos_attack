#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# In[18]:


df=pd.read_csv('weblog4.csv')


# In[19]:


df.head


# In[20]:


df


# In[21]:


df['IP'].value_counts()


# In[22]:


df['Status'].value_counts()


# In[23]:


train_data = df.drop(['IP'],axis=1)


# In[24]:


df


# In[25]:


train_data


# In[26]:


df


# In[27]:


data=df.groupby(['IP','Status']).size().reset_index(name='count')


# In[28]:


data


# In[29]:


data['IP'].value_counts()


# In[30]:


train_data = data.drop(['IP'],axis=1)


# In[31]:


train_data


# In[32]:


from sklearn.preprocessing import StandardScaler 
sc = StandardScaler()
data_scaled = sc.fit_transform(train_data)
print(data_scaled)


# In[33]:


import numpy as np


# In[34]:


from sklearn.cluster import KMeans


# In[35]:


model = KMeans(n_clusters=4)


# In[36]:


model.fit(data_scaled)


# In[37]:


pred=model.fit_predict(data_scaled)


# In[39]:


data_with_pred = pd.DataFrame(data_scaled, columns=['Status','Count'])


# In[40]:


data_with_pred['Cluster'] = pred


# In[41]:


final_data =pd.concat([data,data_with_pred],axis=1)


# In[42]:



final_data


# In[43]:


final_data.plot.bar(x='IP',y='count',rot=0)


# In[68]:


final_data=final_data[['IP','Count','Cluster']]


# In[69]:


final_data


# 

# In[ ]:





# In[107]:


def block_IP(counter, ip): 
  
    
    count = {} 
    for item in counter: 
        if (item in count): 
            count[item] += 1
        else: 
            count[item] = 1
    max_count = 0
    max_key = 0
    for key, value in count.items(): 
        if value > max_count:
            max_count = value
            max_key = key
    
    return ip[counter.index(max_key)]
ddos = block_IP(final_data['IP'].tolist(), final_data['IP'].tolist())


# In[ ]:





# In[ ]:





# In[108]:


ddos


# In[109]:


import os
os.system('sudo iptables -A INPUT -s {} -p -tcp --destination-port 80 -j DROP'.format(ddos))


# In[ ]:




