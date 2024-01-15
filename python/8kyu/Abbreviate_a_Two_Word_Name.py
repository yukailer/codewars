def abbrev_name(name):
    name_list=name.split()
#    print(name_list[0][:1].capitalize()+"."+name_list[1][:1].capitalize())
    return "%s.%s" % (name_list[0][:1].capitalize(), name_list[1][:1].capitalize())

