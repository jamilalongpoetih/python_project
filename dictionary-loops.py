### looping a dictionary
birthday_months = {
    'adrian' : 'february' ,
    'bobby' : 'july' ,
    'nini' : 'april' ,
    'yusoff' : 'april' ,
}
person1_details = {
    'name' : 'adrian' ,
    'age' : 61 ,
    'sex' : 'male',
}
person2_details = {
    'name' :'bobby' ,
    'age': 87 ,
    'sex' : 'male'
}
person3_details = {
    'name' : 'nini' ,
    'age' : 69 ,
    'sex' : 'female' ,
}
person4_details = {
    'name' : 'yusoff',
    'age' : 70 ,
    'sex' : 'male' ,
}

### looping by keys in a list
print ("\nlooping by keys") 
for name in birthday_months.keys() :
    print(name)
    
### looping by values in a list
print("\nlooping by values")
for month in birthday_months.values() :
    print (month) 

### looping a set. Note that a set cannot contain duplicate values from the list
print("\nlooping a set no duplicates allowed")
for month in set(birthday_months.values())  :
    print (month) 

personal_details = [person1_details, person2_details, person3_details, person4_details] 
for details in personal_details :
    print("\n") 
    print(details)
