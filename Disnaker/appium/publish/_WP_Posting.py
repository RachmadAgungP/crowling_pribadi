
import requests
import json
import unidecode
def post_media(url,nama_image,headers):
    image_urls = 'images/%s'%nama_image
    urls = '%smedia'%url
    media = {'file': open(image_urls, 'rb'), 'caption': 'HappyFace'}
    image = requests.post(urls, headers=headers, files=media)
    # print('Your image is published on ' + json.loads(image.content)['source_url'])
    # print(json.loads(image.content)['id'])
    return json.loads(image.content)['id']

def post_artikel(url,user,password,title,artikel,token,id_image,id_category,tgl,index,headers):
    post = {
    'title'    : title,
    'status'   : 'publish', 
    'content'  : '''%s'''%artikel,
    'categories': id_category, 
    'date'   : tgl+'T10:00:00',
    'featured_media': id_image,
    }
    r = requests.post(url + 'posts', headers=headers, json=post)
    # print("ini ID POST ",json.loads(r.content)["id"])
    return r

def search_img(title,nama_image,url,jss,headers):
    list_id = [] 
    id_img = ''
    title = unidecode.unidecode(title)
    for i in range(len(json.loads(jss.content))):
        # for key in json.loads(jss.content)[i]:
        title_db = json.loads(jss.content)[i]["title"]['rendered']
        if title_db[-1].isnumeric():
            title_db = title_db.replace("-%s"%title_db[-1],"") 
        if title == title_db:
            id_img = json.loads(jss.content)[i]["id"]
        list_id.append(title_db)
    if title in list_id:
        print ("ada")
        id_image = id_img
    else:
        print ("tidak ada")
        print (title)
        print (list_id)
        id_image = post_media(url,nama_image,headers)
    return (id_image)   