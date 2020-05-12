import json
import requests

class Deteksi:

    def start(self):
        ip = str(input('Masukan alamat ip > '))
        url = "https://ipapi.co/"+ ip +"/json/"
        req = requests.get(url)
        try:
            if req.status_code == 200:

                negara = str(req.json()['country_name'])
                kab = str(req.json()['region'])
                kota = str(req.json()['city'])
                bendera = str(req.json()['postal'])
                latitude = str(req.json()['latitude'])
                longitude = str(req.json()['longitude'])
                print('\nNegara : {} \nProvinsi : {} \nKota : {}\nPostal : {}\nLatitude : {}\nLongitude : {}'.format(negara, kab, kota, bendera, latitude, longitude))
            else:
                print('Gagal mengambil data')
        except:
            print('Data gagal di ambil')


if __name__ != '__main__':
    Scanner = Deteksi()