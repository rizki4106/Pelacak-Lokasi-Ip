import json
import requests

class Deteksi:

    def start(self):
        ip = str(input('Masukan alamat ip > '))
        url = "https://ipapi.co/"+ ip +"/json/"
        req = requests.get(url)
        data = req.json()
        try:
            if req.status_code == 200:

                negara = data['country_name']
                kab = data['region']
                kota = data['city']
                bendera = data['postal']
                latitude = data['latitude']
                longitude = data['longitude']
                print('\nNegara : {} \nProvinsi : {} \nKota : {}\nPostal : {}\nLatitude : {}\nLongitude : {}'.format(negara, kab, kota, bendera, latitude, longitude))
            else:
                print('Gagal mengambil data')
        except IOError:
            print('Data gagal di ambil')
            print(IOError)


if __name__ != '__main__':
    Scanner = Deteksi()