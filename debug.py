import ipdb
from lib import *

#code here

apple = Company("Apple Inc", 1976)
ibm = Company("IBM computers", 1911)
google = Company("Google Search", 1998)

henry = Dev("Henry")
joy = Dev("Joy")
eric = Dev("Eric")

c1 = Freebie(henry, apple, "Hat", 10)
c2 = Freebie(joy, google, "Jacket", 30)
c3 = Freebie(eric, apple, "Laptop", 800)

ipdb.set_trace()