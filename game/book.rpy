init -3 python:
    paging1 = 'audio/book/paging1.mp3'
    paging2 = 'audio/book/paging2.mp3'
    paging3 = 'audio/book/paging3.mp3'
    paging4 = 'audio/book/paging4.mp3'
    close_book = 'audio/book/close_book.mp3'


    def Go_to_Label(label_name):
        renpy.call_in_new_context(label_name)
    go_to_label = renpy.curry(Go_to_Label)


    def Play_Sound(sound_name):
        renpy.play(sound_name)
    play_sound = renpy.curry(Play_Sound)


    def Showscreen_Action(screen):
        renpy.show_screen (screen)
        renpy.restart_interaction()
    showscreen_action = renpy.curry(Showscreen_Action)


    def Hidescreen_Action(screen, close=False):
        if close is True:
            renpy.play(close_book)
        renpy.hide_screen (screen)
        renpy.restart_interaction()
    hidescreen_action = renpy.curry(Hidescreen_Action)

    def Get_Triggered(number):
        global trigger_book_3, trigger_book_4
        if number == 3:
            trigger_book_3 = True
        if number == 4:
            trigger_book_4 = True
    get_triggered = renpy.curry(Get_Triggered)


style book_frame is frame:
    modal True
    background None

style book_hbox is hbox:
    xalign 0.5
    ypos -430

screen open_book():
    tag page
    vbox:
        frame:
            style "book_frame"
            image "book/opened_book.png"
        hbox:
            style "book_hbox"
            image "book/arrow_back.png" xoffset -80 alpha 0.0
            imagebutton idle "book/close.png" action Hide("open_book"), play_sound(close_book)
            imagebutton idle "book/arrow_next.png" xoffset 80 action showscreen_action("page2"), play_sound(paging1)


screen page2:
        tag page
        vbox:
            frame:
                style "book_frame"
                image "book/page2.png"
            hbox:
                style "book_hbox"
                imagebutton idle "book/arrow_back.png" xoffset -80 action showscreen_action("open_book"), play_sound(paging2)
                imagebutton idle "book/close.png" action Hide("page2"), play_sound(close_book)
                imagebutton idle "book/arrow_next.png" xoffset 80 action showscreen_action("page3"), play_sound(paging3), get_triggered(4)


screen page3:
        tag page
        vbox:
            frame:
                style "book_frame"
                image "book/page3.png"
            hbox:
                style "book_hbox"
                imagebutton idle "book/arrow_back.png" xoffset -80 action showscreen_action("page2"), play_sound(paging2)
                imagebutton idle "book/close.png" action Hide("page3"), play_sound(close_book)
                imagebutton idle "book/arrow_next.png" xoffset 80 action showscreen_action("page4"), play_sound(paging4)


screen page4:
        tag page
        vbox:
            frame:
                style "book_frame"
                image "book/page4.png"
            hbox:
                style "book_hbox"
                imagebutton idle "book/arrow_back.png" xoffset -80 action showscreen_action("page3"), play_sound(paging2)
                imagebutton idle "book/close.png" action Hide("page4"), play_sound(close_book)
                image "book/arrow_next.png" xoffset 80 alpha 0.0
