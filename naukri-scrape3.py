import csv
import time
from selenium import webdriver
import pandas as pd
import bs4
from bs4 import BeautifulSoup
import math
import urllib 
import numpy as np
from urllib.request import Request, urlopen
import requests
from time import sleep
from random import randint
from selenium.common.exceptions import *
import datetime
from selenium.webdriver.support import expected_conditions as EC


# driver=webdriver.Chrome('/home/ashok/chromedrv/chromedriver')
jobs={"ROLES":[],
     "COMPANIES":[],
     "LOCATIONS":[],
     "EXPERIENCE":[],
     "SKILLS":[],
     "DATES":[],
     "PRESENTDATE":[],
     "SALARY":[],
     "LINKS":[],
     "SPECIALITY":[],
     "DESCRIPTION":[]}


MAX_PAGE_NUM = 40
MAX_PAGE_DIG = 3
driver=webdriver.Chrome('/home/ashok/chromedrv/chromedriver')

for i in range(1, MAX_PAGE_NUM+1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    print('Page_num------',page_num)
    # url = "https://www.naukri.com/python-graphql-mongodb-docker-with-linux-jobs-"+page_num
    # url = "https://www.naukri.com/python-developer-python-docker-git-mongodb-sql-linux-api-development-jobs-in-chennai-"+page_num+"?k=python%20developer%2C%20python%2C%20docker%2C%20git%2C%20mongodb%2C%20sql%2C%20linux%2C%20api%20development&l=chennai%2C%20bangalore%2C%20hyderabad%2Fsecunderabad&experience=2"
    url = "https://www.naukri.com/python-developer-python-docker-git-mongodb-sql-linux-api-development-jobs-"+page_num
    # https://www.naukri.com/python-developer-python-docker-git-mongodb-sql-linux-api-development-jobs-in-chennai-2?k=python%20developer%2C%20python%2C%20docker%2C%20git%2C%20mongodb%2C%20sql%2C%20linux%2C%20api%20development&l=chennai%2C%20bangalore%2C%20hyderabad%2Fsecunderabad&experience=2
    # url="https://www.naukri.com/data-scientist-jobs-"+page_num+"?k=data%20scientist"
    driver.get(url)
    time.sleep(3)
    lst=driver.find_elements_by_css_selector(".jobTuple.bgWhite.br4.mb-8")
    
    for job in lst:
        driver.implicitly_wait(10)


        try:
            role=job.find_element_by_css_selector("a.title.fw500.ellipsis").text
            # print('role----',role)

        except:
            role = "NULL"


        
        try:
            company=job.find_element_by_css_selector("a.subTitle.ellipsis.fleft").text
            # print('company----',company)
        except:
            company = "NULL"


        try:
            location=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.location").text
            # print('location----',location)
        except:
            location = "NULL"


        try:
            salaries=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.salary").text
            # print(salaries)
        except:
            salaries = "NULL"

        try:
            # link = job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.salary").text
            link=job.find_element_by_css_selector("a.title.fw500.ellipsis").get_attribute('href')

            # print(link)
        except:
            link = "NULL"
        
        try:
            exp=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.experience").text
            # print(exp)

        except:
            exp = "NULL"

# job-description fs12 grey-text
        try:
            desc = job.find_element_by_css_selector(".job-description.fs12.grey-text").text
        except:
            desc = "NULL"
        try:
            date=job.find_element_by_css_selector(".type.br2.fleft.grey").text
            # print(date)

        except:
            date = "NULL"

        try:
            skills=job.find_element_by_css_selector(".tags.has-description").text 
            # skills = list(skills)
            skills = skills.split('\n')
            skills = tuple(skills)

            # print(skills)

        except:
            skills = "NULL"

        try:
            speciality = job.find_element_by_css_selector(".jobType.type.fleft.br2.mr-8").text
            # print(speciality)
        except:
            speciality = "NULL"

        # try:

       
        today=datetime.datetime.today().strftime('%Y-%m-%d')
        
        jobs["ROLES"].append(role)
        jobs["COMPANIES"].append(company)
        jobs["LOCATIONS"].append(location)
        jobs["EXPERIENCE"].append(exp)
        jobs["LINKS"].append(link)
        jobs["SALARY"].append(salaries)
        jobs["DATES"].append(date)
        jobs["PRESENTDATE"].append(today)
        jobs["SKILLS"].append(skills)
        jobs["SPECIALITY"].append(speciality)
        jobs["DESCRIPTION"].append(desc)

        # jobs["location"].append(lo)
                    
driver.close()
        
df=pd.DataFrame.from_dict(jobs)
df.to_csv('naukri.csv')