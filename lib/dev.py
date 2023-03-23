from .freebie import Freebie

class Dev:
    all = []
    def __init__(self, name):
        if type(name) == str:
            self.name = name
        else:
            print("Please input a string for name.")
        Dev.all.append(self)

    @property
    def freebies(self):
        all_freebies = []
        for freebie in Freebie.all:
            if freebie.dev == self:
                all_freebies.append(freebie)
        return all_freebies

    #   return [ f for f in Freebie.all if f.dev == self ]

    @property
    def companies(self):
        company_list = []
        for f in self.freebies:
            company_list.append(f.company)
        return company_list

    # return [ f.company for f in self.freebies ]

    def received_one(self, item_name):
        for freebie in self.freebies:
            if freebie.item.lower() == item_name.lower():
                return True
            return False
        # freebie_list = [ f.item for f in self.freebies if f.item == item_name]
        # if len(freebie_list) > 0:
        #     return True
        # else:
        #     return False

    def give_away(self, dev_recipient, freebie):
        if freebie.dev == self:
            freebie.dev = dev_recipient
        else:
            print("Don't give away what's not yours.")