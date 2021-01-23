def baca_file():
    tgl_r = open("E:/Belajar/www.disnakerja.com/Data/tanggal.txt", "r")
    tgl = tgl_r.read()
    tgl_r.close()
    return tgl

def data_proses(tgl):
    import os
    x = os.listdir("hasil\%s"%tgl)
    list_data = []
    for y in x:
        if y[0].isnumeric():
            list_data.append(int(y[0]))
        else:
            continue
    return(list_data)