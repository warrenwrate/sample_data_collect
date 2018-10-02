import datetime
import re

class Player:
    def __init__(self):
        self.playerid = None
        self.gender= None
        self.title= None
        self.first= None
        self.last= None
        self.street= None
        self.city= None
        self.state= None
        self.postcode= None
        self.email= None
        self.dob= None
        self.registered= None
        self.phone= None
        self.cell= None
        self.id_name= None
        self.id_value= None
        self.large= None
        self.medium= None
        self.thumbnail= None
        self.nat= None

    def checkvalues(self):
        if type(self.playerid) is not int:
            return 'playerid of {} is not an int'.format(self.playerid)
        if type(self.registered) is not datetime.datetime:
            return 'registered of {} is not datetime'.format(self.registered)
        if type(self.dob) is not datetime.datetime:
            return 'dob of {} is not datetime'.format(self.dob)
        if not (re.match(r'\d{3}-\d{3}-\d{4}$',self.phone) or re.match(r'\(\d{3}\)-\d{3}-\d{4}$',self.phone)):
            return 'phone number of {} may be incorrect'.format(self.phone)
        if not (re.match(r'\d{3}-\d{3}-\d{4}$',self.cell) or re.match(r'\(\d{3}\)-\d{3}-\d{4}$',self.cell)):
            return 'cell number of {} may be incorrect'.format(self.cell)
        if not re.match(r'[a-z|0-9|\.]+@[a-z|0-9]+(.com|.net|.org)',self.email):
            return 'email of {} might be incorrect'.format(self.email)
        
            


