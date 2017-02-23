import os, requests, bs4, time											#import necessary library 

temprature = None													#global veriable
location = None

def main():
	weather()													#will get temprature and location
	notify(temprature, location)								#notify you
	time.sleep(60*5)											#sleep for 5 mins

def notify(location, temprature):

    os.system("""
              osascript -e 'display notification "{}" with title "{}"'						
              """.format(location, temprature))

def weather():

	req  = requests.get("https://www.google.co.in/search?q=weather")					
	req.raise_for_status()
	
	soup = bs4.BeautifulSoup(req.text, 'lxml')											#parse html

	with open("weather.html", "w") as file:												#saves html code in a file(directly parsing google was not working)
		file.write(str(soup))
	
	global temprature, location
	temprature = soup.find('div', {'class' : 'e'}).get_text().split("|")[0][-5:]		
	location = soup.find('div', {'class' : 'e'}).get_text().split("|")[0][11:-5]

	return(location)
	return(temprature)

while True:
	main()