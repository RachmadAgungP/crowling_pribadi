import pandas as pd
import _tgl_
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
tgl = _tgl_.baca_file()
dataw = pd.read_csv("hasil\%s\data_namapekerjaan1.csv"%tgl, index_col=0)
datay = pd.read_csv("hasil\%s\data_namapekerjaan1_new.csv"%tgl, index_col=0)
# r = dataw.drop_duplicates()
# df.drop([0, 1])
namaa = dataw['Nama']
namaa2 = datay['Nama']
vel_same = []
# nltk.download('stopwords')
def simm(X,Y):
    X_list = word_tokenize(X)  
    Y_list = word_tokenize(Y) 
    
    # sw contains the list of stopwords 
    sw = stopwords.words('english')  
    l1 =[];l2 =[] 
    
    # remove stop words from the string 
    X_set = {w for w in X_list if not w in sw}  
    Y_set = {w for w in Y_list if not w in sw} 
    
    # form a set containing keywords of both strings  
    rvector = X_set.union(Y_set)  
    for w in rvector: 
        if w in X_set: l1.append(1) # create a vector 
        else: l1.append(0) 
        if w in Y_set: l2.append(1) 
        else: l2.append(0) 
    c = 0
    
    # cosine formula  
    for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5) 
    return cosine

ind = []
for index,row in dataw.iterrows():
    # if row['Nama'].split(" ")
    # jellyfish.jaro_distance(u'jellyfish', u'smellyfish')
    vel_same.append(row['Nama'])
    for ui in range(len(namaa2)):
        # print (row['Nama'], namaa2[ui])
        value_sim = simm(row['Nama'], namaa2[ui])
        if value_sim >= 0.80:
            ind.append(index)
update_data = dataw.drop(ind)
update_data_full = update_data.append(datay, ignore_index = True)
update_data_full.to_csv('E:/Belajar/www.disnakerja.com/hasil/%s/data_namapekerjaan1.csv'%tgl)

