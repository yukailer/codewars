def accum(s):
    res=""
    s_list=(list(s.strip()))
    for index,x in list(enumerate(s_list,start=1)):
        x=x.capitalize()
        res=res+x.capitalize()
        x=x.lower()
        res=res+((index-1)*x)+"-"
    return res.rstrip("-")
