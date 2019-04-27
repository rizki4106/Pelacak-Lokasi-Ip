import json
import requests

class Deteksi:

	def __init__(self):
		self.ip = raw_input('masukan alamat ip : ')
		hasil = self.getData()
		print(hasil)
	
	# mengambil data

	def getData(self):

		url = "https://ipapi.co/"+ self.ip +"/json/"
		req = requests.get(url)
		
		if req.status_code == 200:

			negara = str(req.json()['country_name'])
			kab = str(req.json()['region'])
			kota = str(req.json()['city'])
			bendera = str(req.json()['postal'])
			latitude = str(req.json()['latitude'])
			longitude = str(req.json()['longitude'])
			print('Negara : {} \nProvinsi : {} \nKota : {}\nPostal : {}\nLatitude : {}\nLongitude : {}'.format(negara, kab, kota, bendera, latitude, longitude))
		else:

			print('Gagal mengambil data')

obj = Deteksi()