from typing import Any, Optional
import json
from _enum import log, mis




class Bank:

    def __init__(self, file_name: str, defolt_money: float = None) -> None:

        if defolt_money:
            self.defolt_money = defolt_money
        else:
            self.defolt_money = 0
        
        self.file_name = file_name
        self.data = {}

        

    def _read_json(self):

        with open(f"{self.file_name}.json", 'a', encoding="utf-8") as f:
            try:
                self.data = json.load(f)
            except:
                pass
        
        


    def _write_json(self):
        with open(f"{self.file_name}.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, separators=(",", ":"))


    def new_user(self, user_name: str, money:float = None): 
        self.data[user_name] = money
        print(f"person with name {user_name} has been create")
        Bank._write_json(Bank)


    def transers(self, from_who_name:str, to_whom_name: str, money: float):

        Bank._read_json(Bank)
        self.data[from_who_name] -= money
        self.data[to_whom_name] += money
        print(f"{from_who_name} transfer {money} to {to_whom_name}")
        Bank._write_json(Bank)


    def add_money(self, user_name: str, money: float):
        Bank._read_json(Bank)
        self.data[user_name] += money
        Bank._write_json(Bank)


    def get_money(self, user_name: str, money:float):

        Bank._read_json(Bank)
        if (self.data[user_name] - money) < 0:
            print("dont have enough money")
            return
        
        self.data[user_name] -= money
        Bank._write_json(Bank)


    def ban(self, user_name:str):
        Bank._read_json(Bank)
        self.data[f"{user_name}_ban"] = self.data[user_name]
        del self.data[user_name]
        Bank._write_json(Bank)
        print("user has been ban")
        
    
    
    def unban(self, user_name:str):
        Bank._read_json(Bank)
        self.data[user_name] = self.data[f"{user_name}_ban"]
        del self.data[f"{user_name}_ban"]
        Bank._read_json(Bank)
        print("user has been unbun")
    

    
    def set(self, money:str):
        self.defolt_money = money

    
    def _check_user_name(self, user_name:str):
        Bank._read_json(Bank)
        if user_name not in self.data:
            return 1
        

file_name = input("input file name you would like: ").strip()
defolt_money = int(input("input defolt amount of money. if you skip it, defolt will be 0 ").strip())
new_bank = Bank(file_name, defolt_money)
new_bank._read_json()

def doit():

    print(f"\n print s to start\n print help to see all comands\n print exit to leave the program ")
    inp = input("~").strip()

    if inp == log.start.value:
        start()

    else:
        print("error")

def start():

    while True:
        inp = input("~").strip()

        if inp == log.exit.value:
            break

        elif inp == log.help.value:
            print(f"you can:\n add new person\n transfer\n add money\n get money\n ban\n unban\n ")

        elif inp == log.add_user.value:

            user_name = input("input user name: ").strip()
            money = int(input("input amount of money: ").strip())
            new_bank.new_user(user_name, money)
            

        elif inp == log.transfer.value:
            
            from_who_name = input("input from who you would like make transfer: ").strip()
            if new_bank._check_user_name(from_who_name) == mis.err.value:
                start()

            to_whom_name = input("input to whom name you would like make transfer: ").strip()
            if new_bank._check_user_name(to_whom_name) == mis.err.value:
                start()

            money = int(input("input amount of money: ").strip())
            new_bank.transers(from_who_name= from_who_name, to_whom_name= to_whom_name, money= money)
            
            
        elif inp == log.add_money.value:
           
            user_name = input("input user name: ").strip()
            money = int(input("input amount of money: ").strip())
            new_bank.add_money(user_name= user_name, money= money)
           

        elif inp == log.get_money.value:
           
            user_name = input("input user name: ").strip()
            money = int(input("input amount of money: ").strip())
            new_bank.get_money(user_name= user_name, money=money)
           

    

       





        
        
       





        
        




        
        
        
