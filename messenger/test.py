import interact
import messages
import main
from os import path

FILE_NAME = path.join(path.dirname(path.abspath(__file__)), "messages.txt")


def run():
    new_message = "Blah Blah Blah"
    new_date = "12/3/2022"
    password = 'password'
    messages_ = messages.Messages(FILE_NAME)
    username1 = 'AdmiralAbe'
    username2 = 'SeamanSam'
    username3 = 'CaptainCharlie'
    username4 = 'JimBob'
    # Confidential
    message_id1 = 100
    message_id2 = 102
    message_id3 = 105

    # Secret
    message_id4 = 106
    message_id5 = 109

    # Privileged
    message_id6 = 107
    message_id7 = 108

    # Public
    message_id8 = 101
    message_id9 = 103
    message_id10 = 104

    # Test Read-Up Restricted
    print("Test 1: ")
    interact_ = interact.Interact(username2, password, messages_)
    interact_.auto_show(message_id4)
    main.close_session()
    print("Test 2: ")
    interact_ = interact.Interact(username4, password, messages_)
    interact_.auto_show(message_id1)
    main.close_session()
    print("Test 3: ")
    interact_ = interact.Interact(username1, password, messages_)
    interact_.auto_show(message_id5)
    main.close_session()
    print("Test 4: ")
    interact_ = interact.Interact(username3, password, messages_)
    interact_.auto_show(message_id8)
    main.close_session()
    print("Test 5: ")
    interact_ = interact.Interact(username1, password, messages_)
    interact_.auto_add(new_message, new_date)
    main.close_session()
    interact_ = interact.Interact(username4, password, messages_)
    interact_.auto_show(110)
    print("Test 6: ")
    interact_ = interact.Interact(username3, password, messages_)
    interact_.auto_add(new_message, new_date)
    main.close_session()
    interact_ = interact.Interact(username1, password, messages_)
    interact_.auto_show(111)


