########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class allows one user to interact with the system
########################################################################

import messages, control

###############################################################
# USER
# User has a name and a password and a control
###############################################################
class User:
    def __init__(self, name, password, user_control):
        self.name = name
        self.password = password
        self.user_control = user_control

#if user isn't valid sign in as a public user
userlist = [
   [ "AdmiralAbe",     "password", control.Control.SECRET ],  
   [ "CaptainCharlie", "password", control.Control.PRIVILEGED ], 
   [ "SeamanSam",      "password", control.Control.CONFIDENTIAL ],
   [ "SeamanSue",      "password", control.Control.CONFIDENTIAL ],
   [ "SeamanSly",      "password", control.Control.CONFIDENTIAL ]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, password, messages):
      if (self._authenticate(username, password)):
         self._username = username
         self._p_messages = messages
         #partially hard coded, would require partial rewrite if user fields are changed
         self._user_control = userlist[self._id_from_user(username)][2]
      else:
         self._username = username
         self._p_messages = messages
         self._user_control = control.Control.PUBLIC

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self):
        id_ = self._prompt_for_id("display")
        if control.securityConditionRead(self._p_messages.get_control(id_), self._user_control):
            if not self._p_messages.show(id_):
                print(f"ERROR! Message ID \'{id_}\' does not exist")
        else:
            print(f"ERROR! Message ID \'{id_}\' does not exist or you do not have rights")
        print()

    def auto_show(self, id):
        id_ = id
        if control.securityConditionRead(self._p_messages.get_control(id_), self._user_control):
            if not self._p_messages.show(id_):
                print(f"ERROR! Message ID \'{id_}\' does not exist")
        else:
            print(f"ERROR! Message ID \'{id_}\' does not exist or you do not have rights")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self):
        print("Messages:")
        self._p_messages.display()
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self):
        self._p_messages.add(self._prompt_for_line("message"),
                             self._username,
                             self._prompt_for_line("date"),
                             self._user_control.name)

    def auto_add(self, message, date):
        self._p_messages.add(message,
                             self._username,
                             date,
                             self._user_control.name)

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self):
      id_ = self._prompt_for_id("update")
      if control.securityConditionRead(self._p_messages.get_control(id_), self._user_control):
         if not self._p_messages.show(id_):
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
            return
         self._p_messages.update(id_, self._prompt_for_line("message"))
         print()
      else:
         print(f"ERROR! Message ID \'{id_}\' does not exist or you do not have rights")
      print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self):
      id_ = self._prompt_for_id("delete")
      if control.securityConditionRead(self._p_messages.get_control(id_), self._user_control):
         self._p_messages.remove(id_)
         print()
      else:
         print("You Do Not Have The Required Rights")
         print()

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: AUTHENTICATE
    # Authenticate the user: find their control level
    ################################################## 
    def _authenticate(self, username, password):
        id_ = self._id_from_user(username)
        return ID_INVALID != id_ and password == users[id_].password

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID

#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")
