'''Configuration'''

dataType = "26?"
delay = 0.05
HOST = "192.168.0.11"
PORT = 65432

''' словарь '''

index = 1

keyboard = {
    "w": index,   #move_forward
    "s": index + 1,   #move_backward
    "a": index + 2,   #tank_turn_left
    "d": index + 3,   #tanl_turn_right
    "q": index + 4,   #wheel_turn_left
    "e": index + 5,   #wheel_turn_right
    "1": index + 6,   #cam_down
    "2": index + 7,   #cam_up
    "u": index + 8,   #man1_up
    "h": index + 9,   #man1_down
    "i": index + 10,  #man2_up
    "j": index + 11,  #man2_down
    "o": index + 12,  #man3_up
    "k": index + 13,  #man3_down
    "p": index + 14,  #man4_up
    "l": index + 15,  #man4_down
    "g": index + 16,  #man5_up
    "y": index + 17,  #man5_down
    "x": index + 18,  #speed_increase
    "z": index + 19,  #speed_deacrease
    "r": index + 20,  #reset
    "v": index + 21,  #lamp_on
    "b": index + 22,  #lamp_off
    "t": index + 23  #romb_wheel
}