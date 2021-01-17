import csv
from itertools import zip_longest
from requests import get
from bs4 import BeautifulSoup
import os
import time
import re
from datetime import datetime
import datetime
from pynput import keyboard


l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []
l10 = []
l11 = []
s = float(0)
m = float(0)
h = float(0)
def ho(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11):
    l1.clear()
    l2.clear()
    l3.clear()
    l4.clear()
    l5.clear()
    l6.clear()
    l7.clear()
    l8.clear()
    l9.clear()
    l10.clear()
    l11.clear()
def sd(p):
  with open(re.sub('[^a-zA-Z]', '', p)+'.csv', 'a', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("date","time","PM2.5", "PM10","O3","NO2","SO2","CO","Temp","Pressure","Humidity","wind","rain"))

      
  myfile.close()

def dataw1(p):
  try:
  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_pm25'})
    a=re.findall("\d+", str(v[0]))[2]
  except:
      a="n"
  return a
def dataw2(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_pm10'})
    a=re.findall("\d+", str(v[0]))[2]
  except:
      a="n"  
  return a
def dataw3(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_o3'})
    a=re.findall("\d+", str(v[0]))[2]
  except:
      a="n"  
  return a
def dataw4(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_no2'})
    a=re.findall("\d+", str(v[0]))[2]
  except:
      a="n"  
  return a
def dataw5(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_so2'})
    a=re.findall("\d+", str(v[0]))[2]
  except:
      a="n"  
  return a
def dataw6(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_co'})
    a=re.findall("\d+", str(v[0]))[1]
  except:
      a="n"  
  return a
def dataw7(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_t'})
    a=re.findall("\d+", str(v[0]))[1]
  except:
      a="n"  
  return a
def dataw8(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_p'})
    a=re.findall("\d+", str(v[0]))[1]
  except:
      a="n"  
  return a
def dataw9(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_h'})
    a=re.findall("\d+", str(v[0]))[1]
  except:
      a="n"  
  return a
def dataw10(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_w'})
    a=re.findall("\d+", str(v[0]))[1]
  except:
      a="n"  
  return a
def dataw11(p):
  try:  
    url = 'https://aqicn.org/city/'+str(p)+"/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    v = html_soup.find_all('td', {'id':'cur_r'})
    a=re.findall("\d+", str(v[0]))[1]
  except:
      a="n"  
  return a



def data(p,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,n):
    c = str(n.strftime("%H:%M:%S"))
    c1 = str(n.strftime("%D"))
    d = [[c1],[c],l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11]
    export_data = zip_longest(*d, fillvalue = '')
    with open(re.sub('[^a-zA-Z]', '', p)+'.csv', 'a', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      
      wr.writerows(export_data)
    myfile.close()
    
def ad(p,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11):
    l1.append(dataw1(p)) 
    l2.append(dataw2(p))
    l3.append(dataw3(p))
    l4.append(dataw4(p))
    l5.append(dataw5(p))
    l6.append(dataw6(p))
    l7.append(dataw7(p))
    l8.append(dataw8(p))
    l9.append(dataw9(p))
    l10.append(dataw10(p))
    l11.append(dataw11(p))

def op(p,n):
     ad(p,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)
     data(p,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,n)

def list(now):
       op("bangkok",now)
       ho(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)
       op("nonthaburi",now)
       ho(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)
       op("thailand/samut-prakan/south-bangkok-power-plant",now)
       ho(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)
      
r = "r"
sd("bangkok")
sd("nonthaburi")
sd("thailand/samut-prakan/south-bangkok-power-plant")
 
while r.lower()=="r":
    format(key)
    now = datetime.datetime.now()
    if s > 59:
       s = 0
       m = m+1
       list(now)
    if key == keyboard.Key.esc:
        break
    if m > 59:
       m = 0
       h = h+1
       
    os.system('cls')
    s = (s + 1)
    print(h,":",m,":",s)
    time.sleep(1)


    

    
