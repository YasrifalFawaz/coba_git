data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi':1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi':1400,
            'jagung':950,
            'kedelai':480
        }
    }
}

#no 1
for i, j in data_panen.items():
    print(f"lokasi: {i}")
    print(f"nama lokasi: {j['nama_lokasi']}")
    print(f"hasil panen padi: {j['hasil_panen']["padi"]}")
    print(f"hasil panen jagung: {j['hasil_panen']["jagung"]}")
    print(f"hasil panen kedelai: {j['hasil_panen']["kedelai"]}")

#no 2
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"hasil panen jagung di lokasi2: {jagung_lokasi2}")

#no 3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"nama lokasi dari lokasi3 adalah {nama_lokasi3}")

#no 4
padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']

kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

print(f"hasil panen padi:\nlokasi1: {padi_lokasi1}\nlokasi2: {padi_lokasi2}\nlokasi3: {padi_lokasi3}\nlokasi4: {padi_lokasi4}\nlokasi5: {padi_lokasi5}")
print(f"hasil panen kedelai:\nlokasi1: {kedelai_lokasi1}\nlokasi2: {kedelai_lokasi2}\nlokasi3: {kedelai_lokasi3}\nlokasi4: {kedelai_lokasi4}\nlokasi5: {kedelai_lokasi5}")

#no 5
jumlah_padi = padi_lokasi1 + padi_lokasi2 + padi_lokasi3 + padi_lokasi4 + padi_lokasi5
jumlah_kedelai = kedelai_lokasi1 + kedelai_lokasi2 + kedelai_lokasi3 + kedelai_lokasi4 + kedelai_lokasi5

print(f"jumlah hasil panen padi: {jumlah_padi}")
print(f"jumlah hasil panen kedelai: {jumlah_kedelai}")

#no 6
for i, j in data_panen.items():
    maks_padi = j['hasil_panen']['padi']
    maks_jagung = j['hasil_panen']['jagung']

    if maks_padi > 1300 or maks_jagung > 800:
        print(f"{i} memerlukan perhatian khusus")
    else:
        print(f"{i} dalam kondisi baik")