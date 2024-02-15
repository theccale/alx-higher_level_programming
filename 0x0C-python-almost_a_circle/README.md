0x0C. Python - Almost a circle
Python
OOP
Tasks
0. If it's not tested it doesn't work
mandatory
. Base class
mandatory
2. First Rectangle
mandatory
0x0C. Python - Almost a circle
Python
OOP
Tasks
0. If it's not tested it doesn't work
mandatory
. Base class
mandatory
2. First Rectangle
mandatory
3. Validate attributes
mandatory
4. Area first
mandatory
5. Display #0
mandatory
6. __str__
mandatory
7. Display #1
mandatory
8. Update #0
mandatory
9. Update #1
mandatory
10. And now, the Square!
mandatory
11. Square size
mandatory
12. Square update
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

133. Rectangle instance to dictionary representation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:
14. Square instance to dictionary representation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:

This dictionary must contain:

id
15. Dictionary to JSON string
mandatory
Score: 0.0% (Checks completed: 0.0%)
JSON is one of the standard formats for sharing data representation.

Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:
16. JSON string to file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:
17. JSON string to dictionary
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:
18. Dictionary to Instance
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:

**dictionary can be thought of as a double pointer to a dictionary
To use the update method to assign all attributes, you must create a “dummy” instance before:
Create a Rectangle or Square instance with “dummy” mandatory attributes (width, height, size, etc.)
Call update instance method to this “dummy” instance to apply your real values
You must use the method def update(self, *args, **kwargs)
**dictionary must be used as **kwargs of the method update
You are not allowed to use eval
19. File to instances
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:

The filename must be: <Class name>.json - example: Rectangle.json
If the file doesn’t exist, return an empty list
Otherwise, return a list of instances - the type of these instances depends on cls (current class using this method)
You must use the from_json_string and create methods (implemented previously)
20. JSON ok, but CSV?
#advanced
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by21. Let's draw it
#advanced
Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:
O[O
~
~
~
~
~
~
~
~
~
~
~
README.md[+] [unix] (00:59 01/01/1970)                                  11,1 All
-- INSERT --

