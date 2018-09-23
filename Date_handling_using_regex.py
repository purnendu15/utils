"""
Given multiple format of dates, the code below is able to determine the appropriate
regex and extract date information
"""


date_field_token_values = ['17/02/2009','February 17, 2009','2009/2/17','2009Feb17']


# In[8]:


def extract_mm_slash_dd_slash_yyyy(val):
    """ Extract  from mm/dd/yyyy """
    print("=========="+val)
    print("Month:{}".format(val.split('/')[0]))
    print("Day:{}".format(val.split('/')[1]))
    print("Year:{}".format(val.split('/')[2]))
    print("==========")


# In[9]:


def extract_month_space_dd_comma_space_yyyy(val):
    """ Extract  from mm/dd/yyyy """
    print("=========="+val)
    print("Month:{}".format(val.split(' ')[0]))
    temp_day = val.split(' ')[1]
    print("Day:{}".format(temp_day.split(',')[0]))
    print("Year:{}".format(val.split(' ')[2]))
    print("==========")


# In[10]:



date_field_regex_list = {'^\d{2}\/\d{2}\/\d{4}$':extract_mm_slash_dd_slash_yyyy,'^[A-z]{8} \d{2}':extract_month_space_dd_comma_space_yyyy}


# In[11]:


# month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
#               'August', 'September', 'October', 'November', 'December']


# In[12]:


import re
for data in date_field_token_values:
    for  regex_key in date_field_regex_list.keys():
        if re.search(regex_key,data):
            date_field_regex_list[regex_key](data)
#             print(regex_type,data)
            print("Found")
        

