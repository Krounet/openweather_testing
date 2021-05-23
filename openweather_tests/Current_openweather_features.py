
class Current_openweather_features :
	


	def __init__(self,api_key,units,lang,citydefname={},citydefid={},citydefzip={},citydefcoord={},boxdef={},circledef={}):
		self.api_key=api_key
		self.units=units
		self.lang=lang
		self.citydefname=citydefname
		self.citydefzip=citydefzip
		self.citydefid=citydefzip
		self.citydefcoord=citydefcoord
		self.boxdef=boxdef
		self.circledef=circledef

	def create_citydefname(self):
		
		citydefname_construct=""
		for keys_inter in list(self.citydefname.keys()):
			if self.citydefname[keys_inter]!="" and list(self.citydefname.keys()).index(keys_inter)!=len(list(self.citydefname.keys()))-1:
				citydefname_construct=citydefname_construct+self.citydefname[keys_inter]+","
			elif self.citydefname[keys_inter]!="" and list(self.citydefname.keys()).index(keys_inter)==len(list(self.citydefname.keys()))-1:
				citydefname_construct=citydefname_construct+self.citydefname[keys_inter]				
		return "https://api.openweathermap.org/data/2.5/weather?q="+citydefname_construct+"&appid="+self.api_key+"&units="+self.units+"&lang="+self.lang

	def create_citydefid(self):		
		return "https://api.openweathermap.org/data/2.5/weather?id="+self.citydefid["id"]+"&appid="+self.api_key+"&units="+self.units+"&lang="+self.lang

	
	def create_citydefcoord(self):
		return "https://api.openweathermap.org/data/2.5/weather?lat="+self.citydefcoord["lat"]+"&lon="+self.citydefcoord["lon"]+"&appid="+self.api_key+"&units="+self.units+"&lang="+self.lang

	def create_citydefzip(self):
		return "https://api.openweathermap.org/data/2.5/weather?zip="+self.citydefzip["zip"]+","+self.citydefzip["country_code"]+"&appid="+self.api_key+"&units="+self.units+"&lang="+self.lang

	def create_boxdef(self):
		return "https://api.openweathermap.org/data/2.5/box/city?bbox="+self.boxdef["lon-left"]+","+self.boxdef["lat-bottom"]+","+self.boxdef["lon-right"]+","+self.boxdef["lat-top"]+","+self.boxdef["zoom"]+"&appid="+self.api_key+"&units="+self.units+"&lang="+self.lang
		

	def create_circledef(self):
		return "https://api.openweathermap.org/data/2.5/find?lat="+self.circledef["lat"]+"&lon="+self.circledef["lon"]+"&cnt="+self.circledef["cnt"]+"&appid="+self.api_key+"&units="+self.units+"&lang="+self.lang
		
	
