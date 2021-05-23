import re
import json
import urllib.request
from Current_openweather_features import Current_openweather_features
def lect_infos(fich):

	lect=open(fich,'r')
	datas=lect.readlines()
	api_key=re.split('=',re.split('\n',datas[0])[0])[1]
	lang=re.split('=',re.split('\n',datas[1])[0])[1]
	units=re.split('=',re.split('\n',datas[2])[0])[1]
	return api_key,lang,units

	
if __name__ == '__main__':
	
	
	api_key,lang,units=lect_infos("infos.txt")	
	init=Current_openweather_features(api_key,units,lang,citydefname={"name":"Baud","country":"fr"})
	define=init.create_citydefname()
	print(define)
	openweather_call=urllib.request.urlopen(define)
	datas=json.loads(openweather_call.read())
	print(datas)
	# print("City : %" %datas["name"])
	# print("lon : %" %datas["coord"]["lon"] + "lat : %" %datas["coord"]["lat"])
	# print("Country : %" %datas["country"])
	# print("Weather : % " %datas["weather"]["main"] + "%" %datas["weather"]["description"])
	# print("Temperature : % °C" %datas["main"]["temp"])
	# print("Pressure : % hPa" %datas["main"]["pressure"])
	# print("Humidity : %%" %datas["main"]["humidity"])
	
	
	
	