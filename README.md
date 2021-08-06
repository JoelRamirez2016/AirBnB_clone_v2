![HBNB](https://i.imgur.com/knu0CXq.png)

<h1 align="center">0x02. AirBnB clone - MySQL</h1>
<p align="center"></p>

---

## Description

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks                         | Files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 0: Authors/README File        | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Project authors                                                                                     |
| 1: Pep8                       | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | All code is pep8 compliant                                                                          |
| 2: Unit Testing               | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | All class-defining modules are unittested                                                           |
| 3. Make BaseModel             | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Defines a parent class to be inherited by all model classes                                         |
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Add functionality to recreate an instance of a class from a dictionary representation               |
| 5. Create FileStorage class   | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/\_ _init_ \_.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py)                                                                                                                                                                                                                                       | Defines a class to manage persistent file storage system                                            |
| 6. Console 0.0.1              | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D          |
| 7. Console 0.1                | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Update the console with methods allowing the user to create, destroy, show, and update stored data  |
| 8. Create User class          | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py)                                                                                                                                                                                                                                                                        | Dynamically implements a user class                                                                 |
| 9. More Classes               | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes                                                                 |
| 10. Console 1.0               | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py)                                                                                                                                                                                                                                                                                                                                                                  | Update the console and file storage system to work dynamically with all classes update file storage |

---

## How to install it:

```
git clone https://github.com/Orcha02/AirBnB_clone.git
cd AirBnB_clone
```

## Usage

#### Interactive Mode

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```

#### Non-Interactive Mode

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

#### Commands Sintax with Respective Usage

| Command | Syntax                                                                                                                      | Output                                                                                                  |
| ------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| help    | `help [option]`                                                                                                             | Displays all available commands                                                                         |
| quit    | `quit`                                                                                                                      | Exit command interpreter                                                                                |
| EOF     | `EOF`                                                                                                                       | Exit command interpreter                                                                                |
| create  | `create [class_name]` or `[class_name].create()`                                                                            | Creates an instance of class_name                                                                       |
| update  | `update [class_name] [object_id] [update_key] [update_value]` or `[class].update([object_id] [update_key] [update_value]()` | Updates the key:value of class_name.object_id instance                                                  |
| show    | `show [class_name] [object_id]` or `[class_name].show([object_id])()`                                                       | Displays all attributes of class_name.object_id                                                         |
| all     | `all [class_name]`, `[class_name].all()`                                                                                    | Displays every instance of class_name, if used without option displays every instance saved to the file |
| destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()`                                                 | Deletes all attributes of class_name.object_id                                                          |
| count   | `count [class_name]` or `[class_name].count()`                                                                              | Counts all the instances with class name specified)                                                     |

<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object

Usage: create <class_name>

```
(hbnb) create BaseModel
```

```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)
```

###### Example 1: Show an object

Usage: show <class_name> <\_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959),
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)
```

###### Example 2: Destroy an object

Usage: destroy <class_name> <\_id>

```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)
```

###### Example 3: Update an object

Usage: update <class_name> <\_id>

```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889),
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```

<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects

Usage: <class_name>.all()

```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User

Usage: <class_name>.destroy(<\_id>)

```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 2: Update User (by attribute)

Usage: <class_name>.update(<\_id>, <attribute_name>, <attribute_value>)

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 3: Update User (by dictionary)

Usage: <class_name>.update(<\_id>, <dictionary>)

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

# Authors

## Initial Authors (V1):

👤 **Justin Majetich**

- Github: [@justinmajetich](https://github.com/Orcha02)

## Authors (V2):

👤 **Daniel Ortega**

- Github: [@Orcha02](https://github.com/Orcha02)

👤 **Joel Ramirez**

- Github: [@JoelRamirez2016](https://github.com/JoelRamirez2016)
