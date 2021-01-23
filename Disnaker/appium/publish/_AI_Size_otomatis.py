import win32com.client as win32

adobe_app = win32.GetActiveObject("Illustrator.Application")
adobe_document = adobe_app.ActiveDocument
# layer2 = adobe_document.Layers("Layer2")
# layer2.Visible = True
import re 

# def layer_sama(nama_layer, layer_ke, isi, ukuran_font, visibley):
#     var = layer_ke.TextFrames(nama_layer)
#     var.TextRange.Contents = str(isi)
#     tR = var.TextRange
#     tR.CharacterAttributes.Size = ukuran_font
#     var.Hidden = visibley
#     return (var)
def reduceSizeOfOversetText(t):
    ru = 0
    bolll = True
    while bolll:
        d = t.Duplicate()
        d.Name = 'temp_%s'%ru
        d.convertAreaObjectToPointObject
        d = t.Parent.TextFrames('temp_%s'%ru)
        std = d.Contents.replace("\x03","")
        print (std)
        stt = t.Contents
        print (stt)
        if len(re.split("/[\x03\r]/g", std)[0]) != len(re.split("/[\x03\r]/g", stt)[0]):
            fon = t.TextRange
            fon.CharacterAttributes.Size -= 0.5
            # print ("->",layer2)
            d.Delete()
            ru+=1
        else:
            d.Delete()
            bolll = False
            break

def contentnya(nama_layer,layer_ke,isi,ukuran_font,visible,object_list):
    # layer_ke = layer2
    var = layer_ke.TextFrames(nama_layer)
    tR = var.TextRange
    if object_list == True:
        isi = isi.expandtabs(3)
        var.TextRange.Contents = str(isi)
        # tR.ParagraphAttributes.justification
        tR.ParagraphAttributes.leftIndent = 20
        tR.ParagraphAttributes.firstLineIndent = -18
    else:
        isi = isi
        var.TextRange.Contents = str(isi)
        # tR.ParagraphAttributes.justification = 2
        tR.ParagraphAttributes.leftIndent = 0
        tR.ParagraphAttributes.firstLineIndent = 0
    if len(isi) == 0:
        tR.CharacterAttributes.Size = 1
        pass
    else:
        tR.CharacterAttributes.Size = ukuran_font
        var.Hidden = visible
        reduceSizeOfOversetText(var)
    # print (tR.CharacterAttributes.Size)
    return (tR.CharacterAttributes.Size)

# isi = "-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!-\tMatahari menyelinap dibalik bukit,\n-\tmenyembunyikan kenangan hidup,\n-\tmenyimpan lembaran usang,\n-\tmenyambut hari-hari muda yang sebentar lagi akan menjelang.\n-\tSelamat tahun baru 2021!"
# contentnya("P1",layer2,isi,23,False,True)
