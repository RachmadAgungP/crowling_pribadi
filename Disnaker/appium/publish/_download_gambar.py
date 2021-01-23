import requests

def maine(urlss,direc):
    headers = {
    'Referer': 'https://www.disnakerja.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'DNT': '1',
    }
    r = requests.post(urlss, headers=headers)
   
    data_img = r.content
    filename = direc  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(data_img)