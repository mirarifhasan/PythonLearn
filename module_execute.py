import datetime
import module
# import module as m
# from module import greeting

print(module.greeting("Arif"))

name = module.person['name']
print('\n' + name)

print()
x = datetime.datetime.now()
# x = datetime.datetime(2020, 5, 17)
print(x)
print(x.year)
print(type(x.year))
print(x.strftime("%A"))
