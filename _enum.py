import enum

class log(enum.Enum):

    help = "help"
    exit = "exit"
    start = "s"

    add_user = "add new person"
    transfer = "transfer"
    add_money = "add money"
    get_money = "get money"
    ban = "ban"
    unban = "unban"

class mis(enum.Enum):
    err = 1
    ok = 0