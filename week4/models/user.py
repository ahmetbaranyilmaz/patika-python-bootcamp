from itertools import count


class User:
    def __init__(
        self,
        name:str,
        username:str,
        email:str,
        emailuserlk:int,
        usernamelk:int,
        birthYear:int,
        birthMonth:int,
        birthDay:int,
        country:str,
        activeStatus:int = 1
    ):
        self.name = name
        self.username = username
        self.email = email
        self.emailuserlk = emailuserlk
        self.usernamelk = usernamelk
        self.birthYear = birthYear
        self.birthMonth = birthMonth
        self.birthDay = birthDay
        self.country = country
        self.activeStatus = activeStatus