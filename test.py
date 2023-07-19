def sort_on(d):
    return d["num"]

dict_list = [{"character":'a',"num":200},{"character":'b',"num":500}]


dict_list.sort(reverse=True, key=sort_on)

print(dict_list)