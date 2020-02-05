#!/usr/bin/env python
# coding: utf-8

# In[53]:


import re
import requests                
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# url address to request web page
URL = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
try:
    r = requests.get(URL).text
except Exception as e:
    r = open('List_of_presidents_of_the_United_States.html', 'r').read()
    print(e)


soup = BeautifulSoup(r, 'lxml')

table = soup.find('table', {'class': 'wikitable'})


def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row       
    return rows

headers = ['Number', 'Presidency', 'Image', 'Presidents', 'Prior Office',
           'black', 'Party', 'Election', 'Vice President']

list_table = tableDataText(table)
dataframe = pd.DataFrame(list_table[2:], columns=headers)

def first_names_tot_presidents():
    names = []
    for name in dataframe['Presidents']:
        if name:
            names.append(name.split()[0])
    return names, len(names)


# In[54]:


# show the dataframe remove Nan Values
dataframe


# In[ ]:


# How many presidents on the page
number = first_names_tot_presidents()[1]
print(f"How many presidents on the page : {number}")


# In[56]:


# Which presidents were assasinated
assassination_pattern = re.compile(r'''Assassinated''')
assassinated = []
for index in range(len(dataframe['Presidency'])):
    if dataframe['Presidency'][index]:
        if assassination_pattern.search(dataframe['Presidency'][index]):
            assassinated.append(dataframe['Presidents'][index])
print(assassinated)


# In[62]:


# presidents selected after serving as senators
senators = []
for senator in filter(None, dataframe['Prior Office']):
    if "U.S Senator" in senator:
        senators.append(senator)
print("------------------------")
print(senators)


# In[80]:


# presidents selected after serving as vice presidents
vices = []
vp_pattern = re.compile(r'vice president')
for index in range(len(dataframe['Prior Office'])):
    if dataframe['Prior Office'][index]:
        if vp_pattern.search(dataframe['Prior Office'][index]):
            vices.append(dataframe['Presidents'][index])
print(vices)


# In[61]:


# which president had one VP for duration of term
def with_one_vp_on_term():
    pass


# In[46]:



# which president was in office for long time and when he left
year_pattern = re.compile(r'\d\d\d\d')
term_in_office = []
for i in filter(None, dataframe['Presidency']):
    if year_pattern.search(i):
        term_in_office.append((int(year_pattern.search(i).group(0))))
odd = [i for i in range(1, 59, 2)]
even = [i for i in range(0, 59, 2)]
# odd - even
# print(odd)

# print(term_in_office)
y1 = [term_in_office[o] for o in odd]
y2 = [term_in_office[e] for e in even]
# print(len(y1))
# print(len(y2))
years = list(map(lambda x, y: x - y, y1, y2))
presidents = ["George Washington","John Adams","Thomas Jefferson","James Madison",
              "James Monroe", "John Quincy Adams","Andrew Jackson", "Martin Van Buren",
             "William Henry Harrison", "John Tyler", "James K. Polk", "Zachary Taylor",
             "Millard Fillmore", "Franklin Pierce", "James Buchanan", "Abraham Lincoln",
             "Andrew Johnson", "Ulysses S. Grant","Rutherford B. Hayes", "James A. Garfield",
             "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison",
             "Grover Cleveland", "William McKinley", "Theodore Roosevelt", "William Howard Taft",
             "Woodrow Wilson", "Warren G. Harding", "Calvin Coolidge", "Herbert Hoover", "Franklin D. Roosevelt",
             "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy", "Lyndon B. Johnson", "Richard Nixon",
             "Gerald Ford", "Jimmy Carter", "Ronald Reagan", "George H. W. Bush", "Bill Clinton",
             "George W. Bush", "Barack Obama"]
print(len(presidents))
# print(len(presidents))
# print(years)
        

       





# In[43]:



# How many presidents with same forenames? 
forenames = {name:0 for name in first_names_tot_presidents()[0]}
for key, value in forenames.items():
    for name in filter(None, dataframe['Presidents']):
        if key == name.split()[0]:
            forenames[key] += 1
        continue

# This prints the names and the total for that name
# print(forenames)
total = 0
for key in forenames.keys():
    if forenames[key] > 1:
        total += 1

# Total number of presidents with similar forenames
print(f'Total Number of presidents with similar forename is : {total}')
        




# In[64]:



# oldest president ever elected
def oldest_president_ever_elected():
    pass


# In[65]:



# youngest president elected
def youngest_president_elect():
    pass


# In[66]:



# president who lived to an old age after leaving office
def president_who_lived_to_old_age_after_office():
    pass


# In[49]:


# Graph that shows no. of presidents and their respective political parties and party with many presidents
parties = {"Democratic":0 , "Republican":0, "National Union":0, "Federalist":0, "Whig":0, "Unaffiliated":0}
for key,value in parties.items():
    for party in filter(None, dataframe['Party']):
        if party.startswith(key):
            parties[key] += 1
        continue
        
print(parties)

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 10,
        }

plt.title('Graph shows no of presidents and political parties and party with many presidents', fontdict=font)
plt.bar(*zip(*parties.items()), align='edge', width=0.3)
plt.show()
    
                
                
        
        


# In[ ]:





# In[ ]:





# In[ ]:




