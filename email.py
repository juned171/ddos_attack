import smtplib
from kmean import ddos





# In[8]:


server=smtplib.SMTP_SSL("smtp.gmail.com",465)


# In[10]:


server.login("junedansari771@gmail.com","password")


# In[11]:


message = "Blocked IP is  {0}".format(ddos)


# In[12]:


server.sendmail("junedansari771@gmail.com","junedansari771@gmail.com",message)


# In[13]:


server.quit()

