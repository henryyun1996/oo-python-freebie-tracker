
class Freebie:

    all = []

    def __init__(self, dev_instance, company_instance, item_name, value):
        self.dev = dev_instance
        self.company = company_instance
        self.item = item_name
        self.value = value
        Freebie.all.append(self)

# `{dev name} owns a {freebie item_name} from {company name}`.

    @property
    def print_details(self):
        return (f"{self.dev.name} owns a {self.item} from {self.company.name}.")
