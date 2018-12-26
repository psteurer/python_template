msg = "Hello, World!"
print(msg)

def doPlayAndLearn():
    # create a list called my_list
    my_list = [1, 2, 3, "python", 67,  [4, 5]]

    # go through my_list and print every item
    for item in my_list:
        print(item)

    # create a dictionary
    person = {
                "name": "Amos",
                "age": 23,
                "hobbies": ["Travelling", "Swimming", "Coding", "Music"]
            }

    # iterate through the dict and print the keys
    for key in person:
        print(key)

    # iterate through the dict's keys and print their values
    for key in person:
        print(person[key])  