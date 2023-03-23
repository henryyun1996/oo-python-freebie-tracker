from .freebie import Freebie

class Company:
    all = []
    def __init__(self, name, year):
        if type(name) == str:
            self.name = name
        else:
            print("Please input a string for name.")
        if type(year) == int:
            self.year = year
        else:
            print("Please input a number for founding year.")
        Company.all.append(self)
        
    @property
    def freebies(self):
        all_freebies = []
        for freebie in Freebie.all:
            if freebie.company == self:
                all_freebies.append(freebie)
        return all_freebies

    #   return [ f for f in Freebie.all if f.company == self ]

    @property
    def devs(self):
        devs_list = []
        for f in self.freebies:
            devs_list.append(f.dev)
        return devs_list

    #   return [ f.dev for f in self.freebies ]

    def give_freebie(self, dev_instance, item_name, value):
        Freebie(dev_instance, self, item_name, value)
    
    @classmethod
    def oldest_company(cls):
        earliest_year = 3000
        found_instane = ''

        for company in cls.all:
            if company.year < earliest_year:
                earliest_year = company.year
                found_instance = company
        return found_instance


