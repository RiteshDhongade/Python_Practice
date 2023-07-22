menu = {'Breakfast':['Egg Sandwich','Bagel','Coffee'],'Lunch':['BLT','PB&J','Turkey Sandwich'],'Dinner':['Soup','Salad','Spaghetti','Taco']}
# print('Brakefast Menu:\t', menu['Breakfast'])
# print('Lunch Menu:\t',menu['Lunch'])
# print('Dinner Menu:\t',menu['Dinner'])
for name, menu in menu.items():
    print(name,'$', menu)
