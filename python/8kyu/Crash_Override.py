def alias_gen(f_name, l_name):
    if f_name[0].isalpha() == True and l_name[0].isalpha() == True:
        alias = FIRST_NAME[f_name[0].upper()] + ' ' + SURNAME[l_name[0].upper()]
        return alias
    else: return "Your name must start with a letter from A - Z."
    pass
