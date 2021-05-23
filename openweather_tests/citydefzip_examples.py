import json
import urllib.request
import re
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
	init=Current_openweather_features(api_key,units,lang,citydefzip={"zip":"94040","country_code":"us"})
	define=init.create_citydefzip()
	print(define)
	openweather_call=urllib.request.urlopen(define)
	datas=json.loads(openweather_call.read())
	print(datas)