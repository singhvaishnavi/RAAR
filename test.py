tp={'Casual Dining': 0,
        'Cafe': 1,
        'Quick Bites': 2,
        'Delivery': 3,
        'Mess': 4,
        'Dessert Parlor': 5,
        'Bakery': 6,
        'Pub': 7,
        'Takeaway': 8,
        'Fine Dining': 9,
        'Beverage Shop': 10,
        'Sweet Shop': 11,
        'Bar': 12,
        'Confectionery': 13,
        'Kiosk': 14,
        'Food Truck': 15,
        'Microbrewery': 16,
        'Lounge': 17,
        'Food Court': 18,
        'Dhaba': 19,
        'Club': 20,
        'Bhojanalya': 21,
        'Pop Up': 22}
"""
print(sorted(tp))
dc={}
for key in sorted(tp):
    #print("%s: %s" % (key, tp[key]))
    dc[key]=tp[key]
print(dc)
#print(sorted(tp.items(), key = 
#             lambda kv:(kv[1], kv[0]))) 
"""
def sortdic(x):
    dc={}
    for key in sorted(x):
        dc[key]=x[key]
    return dc
y=sortdic(tp)
print(y)   
