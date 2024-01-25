


choice = input("")

def read_fail(f):
    fail=open(f,'r',encoding="utf-8")
    list=[] 
    for row in fail:
        list.append(row.strip())
    fail.close()
    return list

rus:list=read_fail("rus.txt")
est:list=read_fail("est.txt")