#!/usr/bin/python3
<<<<<<< HEAD
""" 15-main """
=======
""" 16-main """
>>>>>>> f7db8bd98551ca608569109f21914d0989b581ff
from models.rectangle import Rectangle

if __name__ == "__main__":

<<<<<<< HEAD
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
=======
    list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))
>>>>>>> f7db8bd98551ca608569109f21914d0989b581ff
