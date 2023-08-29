from typing import Any, Optional
import json




class Bank:

    def __init__(self, file_name) -> None:
        self.defolt_money = 0
        self.file_name = file_name
        self.data = {}

        

    def _read_json(self):

        with open(f"{self.file_name}.json", 'a', encoding="utf-8") as f:
            self.data = json.load(f)
        
        return self.data


    def _write_json(self):
        with open(f"{self.file_name}.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, separators=(",", ":"))


    def new_user(self, user_name, money = None): 
        self.data[user_name] = money

        return self.data
    

    def transers(self, from_who_name, to_whom_name, money):

        self.data[from_who_name] -= money
        self.data[to_whom_name] += money

    def add_money(self, user_name, money):

        self.data[user_name] += money

    def get_money(self, user_name, money):

        if (self.data[user_name] - money) < 0:
            return "dont have enough money"

        self.data[user_name] -= money

    def ban(self, user_name):
        self.data[f"{user_name}_ban"] = self.data[user_name]
        del self.data[user_name]
        return "user has been ban"
    
    def set(self, money):
        self.defolt_money = money

    
    

def doit():
    while True:
        ...




        
        
        
