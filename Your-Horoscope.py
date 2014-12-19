import urllib2
from bs4 import BeautifulSoup
import re

def horoscope(sunsign,duration,language):
  if language == "hindi":
    url = "http://www.ganeshaspeaks.com/hindi/" + sunsign + "/" + sunsign + "-"+duration+"-horoscope.action"
  else:
    url = "http://www.ganeshaspeaks.com/" + sunsign + "/" + sunsign + "-"+duration+"-horoscope.action"

  html_doc = urllib2.urlopen(url)
  soup = BeautifulSoup(html_doc.read())

  raw_data = str (soup.find_all(id="predData"))

  soup = BeautifulSoup (raw_data)
  date = soup.find_all('strong')[0].get_text ()

  soup = BeautifulSoup (raw_data)
  horoscope = soup.find_all(id="predData")[0].get_text ()
  horoscope = re.sub(r'\d+-\d+-\d+', r'', horoscope)

  print "Date : " + date
  print "Your horscope says..." + horoscope

sunsign = raw_input ("Enter Your Sunsign : ")
duration = raw_input ("Daily, weekly, Monthly or yearly? : ")
language = raw_input("English or hindi? : ")
horoscope(sunsign,duration,language)
