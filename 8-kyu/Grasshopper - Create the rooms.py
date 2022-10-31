"""
@File    : Grasshopper - Create the rooms.py 
@Author  : Richie Black
@Time    : 31.10.2022 18:49

I have been learning Python since August 2022.
"""

rooms = {'1st': {1: 'name', 2: "description", 3: "completed"},
         '2nd': {1: 'name', 2: "description", 3: "completed"},
         '3rd': {1: 'name', 2: "description", 3: "completed"}
         }

"""Best practices
-----------------

rooms = { "Room_1":{"Guest_Name":"Hardik","Room_Number":"69","Hotel":"Royal Inn"},
          "Room_2":{"Guest_Name":"Hridhik","Room_Number":"369","Hotel":"Sandesh The Prince"},
          "Room_3":{"Guest_Name":"Pratham","Room_Number":"96","Hotel":"The Quorum"},
          "Room_4":{"Guest_Name":"Ruturaj","Room_Number":"14","Hotel":"Radisson Blu"}}

-----------------

room1 = {"name": "", "description": "", "completed": False}
room2 = {"name": "", "description": "", "completed": False}
room3 = {"name": "", "description": "", "completed": False}

rooms = {0: room1, 1: room2, 2: room3}

-----------------

rooms = {'room1': {'name': 'name1', 'description': 'description1', 'completed': 'no'},
         'room2': {'name': 'name2', 'description': 'description2', 'completed': 'no'},
         'room3': {'name': 'name3', 'description': 'description3', 'completed': 'no'}
         }

-----------------
"""

# https://www.codewars.com/kata/reviews/5ee3b0e84580980001fd1604/groups/634f3387cd7c5c0001592539
