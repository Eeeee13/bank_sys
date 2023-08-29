a ={}
a["eee"] = 100
a["rrr"] = 80
a["eee_ban"] = a ["eee"]
del a["eee"]

def ban(user_name, dict):
    print(dict[f"{user_name}_ban"])

ban("rrr", a)
# print(a)