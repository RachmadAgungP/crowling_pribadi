def baca_file():
    tgl_r = open("E:/Belajar/www.disnakerja.com/Data/tanggal.txt", "r", encoding='utf-8-sig')
    tgl = tgl_r.read()
    tgl_r.close()
    return tgl

def data_proses(tgl):
    import os
    x = os.listdir("hasil\%s"%tgl)
    list_data = []
    list_nama_data = []
    for y in x:
        w = y.split(".")
        if w[0].isnumeric():
            list_data.append(int(w[0]))
            list_nama_data.append(w[1])
        else:
            continue
    print (float(len(list_data))/2)
    return(list_data)

def data_proses_foto(tgl):
    import os
    x = os.listdir("hasil\%s"%tgl)
    list_data = []
    for y in x:
        w = y.split(".")
        if w[0].isnumeric():
            list_data.append(y)
        else:
            continue
    data_foto = []
    for u in list_data:
        oi = os.listdir("hasil\%s\%s"%(tgl,u))
        data_foto.append(oi)
    # print (data_foto)
    return(list_data,data_foto)

def data_proses_text(tgl):
    import os
    x = os.listdir("hasil/%s/text"%tgl)
    list_data = []
    for y in x:
        list_data.append(y)
    data_foto = []
    for u in list_data:
        print (u)
        # oi = os.listdir("hasil/%s/text/%s"%(tgl,u))
        data_foto.append(u)
    print (data_foto)
    return(list_data,data_foto)

# tgl = baca_file()
# # data_proses(tgl)
# data_proses_text(tgl)