#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# **Loading the medical dataset**

# In[4]:


medical=pd.read_csv("medical.csv")
medical


# In[6]:


medical.head()


# **Dataset information**

# In[7]:


medical.info()


# **shape means it shows how many records and how many columnsin whole dataset**

# In[10]:


medical.shape


# **changing patientid column from significant value to normal integer**

# In[13]:


medical['PatientId'] = medical['PatientId'].apply(lambda x: '{:.0f}'.format(float(x)))
print(medical)


# In[14]:


medical


# **checking of null values**

# In[15]:


medical.isnull().sum()


# **checking the duplicate rows**

# In[18]:


duplicate_rows=medical.duplicated()
print(duplicate_rows)


# **changing the date and time format**

# In[24]:


medical['ScheduledDay'] = pd.to_datetime(medical['ScheduledDay'])
medical['AppointmentDay'] = pd.to_datetime(medical['AppointmentDay'])
medical


# In[ ]:




