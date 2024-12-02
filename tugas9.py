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
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

#soal no 1
print ('No.1\n')
for i,j in data_panen.items():
     print(f"{i} ")
     print (f"Nama Lokasi : {j['nama_lokasi']}")
     print(f"Hasil Panen Padi: {j['hasil_panen']['padi']}")
     print(f"Hasil Panen Jagung: {j['hasil_panen']['jagung']}")
     print(f"Hasil Panen Kedelai: {j['hasil_panen']['kedelai']}")
     print()
     
#soal no 2
print ('No. 2\n')
l2= data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil Panen Jagung di Lokasi 2: {l2}\n")

#soal no 3
print ('No. 3\n')
l3=data_panen['lokasi3']['nama_lokasi']
print(f"Nama Lokasi 3: {l3}\n")

#soal no 4 dan 5
print ("NO. 4 dan 5\n")
padi=[]
kedelai=[]

for i,j in data_panen.items():
     padi.append(j['hasil_panen']['padi'])
     kedelai.append(j['hasil_panen']['kedelai'])

print (f"Hasil Panen Padi: {padi}")
print (f"Hasil Panen Kedelai: {kedelai}\n")

#soal no 6
print ("NO. 6\n")

for i,j in data_panen.items():
     if j['hasil_panen']['padi'] > 1300 or j['hasil_panen']['jagung'] > 800:
          print (f"Pada {i} memerlukan perhatian khusus\n")
     else :
          print (f"Pada{i} tidak memerlukan perhatian khusus\n")



