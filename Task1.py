#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np


# In[25]:


import pandas as pd


# In[6]:


#Task-1
nos = np.arange(10)
sum_nos = 0
for i in nos:
    sum_nos = sum_nos + i
    print("Number =",str(i),"\t","Cumulative sum =",str(sum_nos))


# In[5]:


#Task-2
char_ls = ['A','B','C','D','E']
for i in range(len(char_ls)):
    print((char_ls[i]+"\t")*(i+1))


# In[58]:


#Task-3
contact_dict = {"Name":["person1","person2"],"age":[23,34],"height":[5.8,6.1],"Address":["address1","address2"],"cell number":[1234567890,9876543210]}
df_t3 = pd.DataFrame(contact_dict)
print(dt)


# In[16]:


#Task-4
num_t4 = int(input("Enter number : ")) #Enter number 2345667
for i in str(num_t4):
    print(i)


# In[20]:


#Task-5
letters = ["a","b","c","d"]
letters.insert(0,"z")
print(letters)


# In[27]:


# Task-6
nos_t6 = np.arange(10)
print(nos_t6[ nos_t6 % 2 != 0])


# In[29]:


# Task-7
stringname = "Hello, All!"
for i in stringname:
    print(i)


# In[30]:


# Task-8
Input_list = [2,4,6,8,10,13,12,14,16,18]
for i in Input_list:
    if i%2 != 0:
        break
    else:
        print(i)


# In[40]:


# Task-9
my_list1 = [1,3,5,7]
my_list2 = [2,4,6,8]
for i in range(len(my_list1)):
    print(my_list1[i],my_list2[i])


# In[41]:


# Task-10
def product(num1,num2):
    print(num1*num2)
    
product(2,3)


# In[48]:


# Task-11
def fibonacci_series(num):
    first_num = 0
    second_num = 1
    for i in range(num):
        if  i==0:
            print(first_num,end=",")
        elif i==1:
            print(second_num,end=",")
        else:
            sum=first_num + second_num
            print(sum,end=",")
            first_num = second_num
            second_num = sum

fibonacci_series(8)


# In[53]:


# Task-12
sample_data = pd.read_csv("train.csv") #imported a file "train.csv"
sample_data.head()


# In[57]:


# Task-13
def remove_duplicates(lis):
    create_set = set(lis)
    return list(create_set)
    
lis_t13 = [1,2,2,5,6,6,4,5]
print(remove_duplicates(lis_t13))


# In[67]:


# Task-14
df_t14 = pd.read_json("task_14.json")
df_t14.head()


# In[76]:


# Task-15
def remove_duplicates_intersection(lis1,lis2):
    set1 = set(lis1)
    set2 = set(lis2)
    return(list(set1.intersection(set2)))
lis1 = [1,1,2,3,5,8,13,21,34,55,89]
lis2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(remove_duplicates_intersection(lis1,lis2))


# In[51]:


# Task-16
def reverse_string(string):
    ls = string.split(" ")
    for i in range(len(ls)):
        print(ls[-(i+1)],end=" ")
            
str_t16 = "My name is Mike"
reverse_string(str_t16)


# In[3]:


# Task-17
def first_last_num(lis):
    return [lis[0],lis[-1]]

lis_t17 = [10,20,30,40,50,60]
print(first_last_num(lis_t17))


# In[22]:


# Task-18
def verify_prime(num):
    flag=0
    for i in range(2,(num//2)+1):
        if num%i == 0:
            flag+=1
    if flag>0:
        print("{} is composite".format(num))
    else:
        print("{} is prime".format(num))

num_t18 = int(input("Enter a number : "))#Enter a number to check for prime or composite
verify_prime(num_t18)


# In[67]:


# Task-19
def search_number(ls,num):
    mid = len(ls)//2
    if num > ls[-1] or num < ls[0]:
        return False
    elif num == ls[mid]:
        return True
    else:
        if num > ls[mid]:
            return search_number(ls[mid+1:],num)
        else:
            return search_number(ls[:mid],num)
    
ls_t19 = np.arange(26)
print(search_number(ls_t19,3))


# In[ ]:


# Task-20


# In[68]:


from bs4 import BeautifulSoup
import requests


# In[135]:


url = "https://www.nytimes.com"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
html = requests.get(url, headers = header).content
soup = BeautifulSoup(html, "lxml")

for i in soup.select(".story-wrapper"):
    try:
        print(i.find('h3').get_text())
    except:
        print("")


# In[ ]:




