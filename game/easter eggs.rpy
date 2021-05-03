init -3 python:
    sss = 'audio/police2.mp3'
    renpy.add_layer("easter_layer", below = "transient") #transient
    num = 0
    def Sock_Count():
        global num
        num += 1
        #renpy.restart_interaction()
        if num == 10:
            renpy.play(sss)
            num = 0
    sock_count = renpy.curry(Sock_Count)

screen eggs():
    imagebutton idle "sock.png" xalign 0.45 yalign 0.6 xoffset 48 yoffset 85 action sock_count()
