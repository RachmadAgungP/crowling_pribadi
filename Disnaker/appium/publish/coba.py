data = [[1, 2], [3,4,10,8], [8, 11, 12], [5, 6, 7]]

# bagi(Input)
def tt(lst, n):
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            # print (lst[i:i + n])
        
            yield lst[i:i + n]

    asw = list(chunks(lst, n))
    print (asw)
    po = []
    for t in asw:
        wew = []
        for u in t:
            for y in u:
                if y not in wew:
                    wew.append(y)
        po.append(wew)
    return (po)
# print(tt(data, 2))

import itertools


# data=[['Sarah', '12', 'Chocolate'],
#        ['Anders', '11', 'Vanilla'],
#        ['Sarah', '13', 'Strawberry'],
#        ['John', '11', 'None']]
def grouping(sequence):
    datas = []
    for y in sequence:
        ti = []
        print (set(y))
        for u in y:
            if u == '':
                pass
            else:
                ti.append(u)
        datas.append(ti)
    def grouper(sequence):
        result = []  # will hold (members, group) tuples

        for item in sequence:
            for members, group in result:
                if members.intersection(item):  # overlap
                    members.update(item)
                    group.append(item)
                    break
            else:  # no group found, add new
                result.append((set(item), [item]))

        return [group for members, group in result]

    # for group in grouper(data):
        # print (grouper(data))
    asw = grouper(datas)
    po = []
    for t in asw:
        wew = []
        for u in t:
            for y in u:
                if y not in wew:
                    wew.append(y)
        po.append(wew)
    return (po)
data =[['', 'Fresh Graduate, Diploma or Bachelor Degree with following major:', '', 'Mining Engineering', 'Geology Engineering', 'Civil Engineering', 'Mechanical Engineering', 'Electrical Engineering', 'Law', 'Psychology', 'Finance & Accounting', 'Business Management', 'Public Health', 'Industrial Engineering', '', '', ''], ['', 'Mining Engineering', 'Geology Engineering', 'Civil Engineering', 'Mechanical Engineering', 'Electrical Engineering', 'Law', 'Psychology', 'Finance & Accounting', 'Business Management', 'Public Health', 'Industrial Engineering', ''], ['', 'GPA > 2.75', 'Max 25 years old', 'Good Health', 'Ready for work at remote area', '']]

print (grouping(data))