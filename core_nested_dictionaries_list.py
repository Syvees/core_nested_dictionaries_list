#1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
#1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students[0])
#1.3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])
#1.4 Change the value 20 in z to 30
z[0]["y"] = 30
print(z)

#2 Iterate Through a List of Dictionaries
writers = [
        {"first_name": "CS", "last_name": "Lewis"},
        {"first_name": "Katherine", "last_name": "Paterson"},
        {"first_name": "JK", "last_name": "Rowling"},
        {"first_name": "Roald", "last_name": "Dahl"}
]
def iterate_dictionary(writers):
        for i in writers:
                print("first_name - " + i["first_name"] +", last_name - " + i["last_name"])

iterate_dictionary(writers)

#3 Get Values From a List of Dictionaries
def iterate_dictionary2(writers):
        for i in writers:
                print(i["first_name"])

def iterate_dictionary3(writers):
        for i in writers:
                print(i["last_name"])

iterate_dictionary2(writers)
iterate_dictionary3(writers)


#4 Iterate Through a Dictionary with List Values

dojo = {
        'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
        for key, val in dojo.items():
                print(str(len(val)) + " " + key.upper())
                for i in val:
                        print(i)
printInfo(dojo)
