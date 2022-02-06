
def processing(lst):
    lstT = []
    lstU = []

    for i in lst:
        if i:
            if '_' in i:
                l = i.split('_')
                lstT.append(l[0])
                l.pop(0)
                for i in l:
                    lstU.append(i)
            else:
                lstT.append(i)
    return lstT, lstU
