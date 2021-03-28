#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


# base URL for the SEC EDGAR browser
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"

# define the parameters dictionary
param_dict = {'action':'getcompany',
              'CIK':'1719406',
              'type':'S-1',
              'dateb':'20210219',
              'owner':'exclude',
              'start':'',
              'output':'',
              'count':'100'}

# request the url, and then parse the response.
response = requests.get(url = endpoint, params = param_dict)
soup = BeautifulSoup(response.content, 'html.parser')

print('Request Successful')
print(response.url)


# In[3]:


# find the document table with the data
doc_table = soup.find_all('table', class_='tableFile2')

# define a base url that will be used for link building.
base_url_sec = r"https://www.sec.gov"

master_list = []

# loop through each row in the table.
for row in doc_table[0].find_all('tr')[0:9]:
    
    # find all the columns
    cols = row.find_all('td')
    
    # if there are no columns move on to the next row.
    if len(cols) != 0:        
        
        # grab the text
        filing_type = cols[0].text.strip()                 
        filing_date = cols[3].text.strip()
        filing_numb = cols[4].text.strip()
        
        # find the file links
        filing_doc_href = cols[1].find('a', {'href':True, 'id':'documentsbutton'})       
        filing_int_href = cols[1].find('a', {'href':True, 'id':'interactiveDataBtn'})
        filing_num_href = cols[4].find('a')
        
        # grab the the first href
        if filing_doc_href != None:
            filing_doc_link = base_url_sec + filing_doc_href['href'] 
        else:
            filing_doc_link = 'no link'
        
        # grab the second href
        if filing_int_href != None:
            filing_int_link = base_url_sec + filing_int_href['href'] 
        else:
            filing_int_link = 'no link'
        
        # grab the third href
        if filing_num_href != None:
            filing_num_link = base_url_sec + filing_num_href['href'] 
        else:
            filing_num_link = 'no link'
        
        # create and store data in the dictionary
        file_dict = {}
        file_dict['file_type'] = filing_type
        file_dict['file_number'] = filing_numb
        file_dict['file_date'] = filing_date
        file_dict['links'] = {}
        file_dict['links']['documents'] = filing_doc_link
        file_dict['links']['interactive_data'] = filing_int_link
        file_dict['links']['filing_number'] = filing_num_link
    
        # test to see if scrape is working
        print('-'*100)        
        print("Filing Type: " + filing_type)
        print("Filing Date: " + filing_date)
        print("Filing Number: " + filing_numb)
        print("Document Link: " + filing_doc_link)
        print("Filing Number Link: " + filing_num_link)
        print("Interactive Data Link: " + filing_int_link)
        
        # append dictionary to master list
        master_list.append(file_dict)


# In[4]:


# loop through to get the links from the dict
for report in master_list[0:10]:
    
    print('-'*100)
    print(report['links']['documents'])
    print(report['links']['filing_number'])
    print(report['links']['interactive_data'])


# In[5]:


# set base URL for the SEC EDGAR browser
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"

# define our parameters dictionary
param_dict = {'action':'getcompany',
              'CIK':'1719406',
              'type':'S-1',
              'dateb':'20210219',
              'owner':'exclude',
              'start':'',
              'output':'atom',
              'count':'100'}

# request the url, and then parse the response
response = requests.get(url = endpoint, params = param_dict)
soup = BeautifulSoup(response.content, 'lxml')

# check if successful
print('Request Successful')
print(response.url)


# In[6]:


# find all the entry tags using beatiful soup
entries = soup.find_all('entry')

# initalize the list for storage
master_list_xml = []

# loop through each found entry for up to 10 entries
for entry in entries[0:10]:
    
    # grab the accession number to create a key value for the filing
    accession_num = entry.find('accession-number').text
    
    # create a new dictionary
    entry_dict = {}
    entry_dict[accession_num] = {}
    
    # store the category info
    category_info = entry.find('category')    
    entry_dict[accession_num]['category'] = {}
    entry_dict[accession_num]['category']['label'] = category_info['label']
    entry_dict[accession_num]['category']['scheme'] = category_info['scheme']
    entry_dict[accession_num]['category']['term'] =  category_info['term']

    # store the file info
    entry_dict[accession_num]['file_info'] = {}
    entry_dict[accession_num]['file_info']['act'] = entry.find('act').text
    entry_dict[accession_num]['file_info']['file_number'] = entry.find('file-number').text
    entry_dict[accession_num]['file_info']['file_number_href'] = entry.find('file-number-href').text
    entry_dict[accession_num]['file_info']['filing_date'] =  entry.find('filing-date').text
    entry_dict[accession_num]['file_info']['filing_href'] = entry.find('filing-href').text
    entry_dict[accession_num]['file_info']['filing_type'] =  entry.find('filing-type').text
    entry_dict[accession_num]['file_info']['form_number'] =  entry.find('film-number').text
    entry_dict[accession_num]['file_info']['form_name'] =  entry.find('form-name').text
    entry_dict[accession_num]['file_info']['file_size'] =  entry.find('size').text
    
    # store extra info
    entry_dict[accession_num]['request_info'] = {}
    entry_dict[accession_num]['request_info']['link'] =  entry.find('link')['href']
    entry_dict[accession_num]['request_info']['title'] =  entry.find('title').text
    entry_dict[accession_num]['request_info']['last_updated'] =  entry.find('updated').text
    
    # store in the master list
    master_list_xml.append(entry_dict)
    
    #print file data and accession number to append to SPAC data list
    
    print('-'*100)
    print(entry.find('form-name').text)
    print(entry.find('file-number').text)
    print(entry.find('file-number-href').text)
    print(entry.find('link')['href'])
    print(accession_num)
    


# In[ ]:




