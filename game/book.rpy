init -3 python:
    paging1 = 'audio/book/paging1.mp3'
    paging2 = 'audio/book/paging2.mp3'
    paging3 = 'audio/book/paging3.mp3'
    paging4 = 'audio/book/paging4.mp3'
    close_book = 'audio/book/close_book.mp3'

    def Showscreen_Action(screen, page=None):
        if page == 1:
            renpy.play(paging1)
        if page == 2:
            renpy.play(paging2)
        if page == 3:
            renpy.play(paging3)
        if page == 4:
            renpy.play(paging4)
        renpy.show_screen (screen)
        renpy.restart_interaction()
    showscreen_action = renpy.curry(Showscreen_Action)


    def Hidescreen_Action(screen, close=False):
        if close is True:
            renpy.play(close_book)
        renpy.hide_screen (screen)
        renpy.restart_interaction()
    hidescreen_action = renpy.curry(Hidescreen_Action)


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
            imagebutton idle "book/close.png" action hidescreen_action("open_book", close=True)
            imagebutton idle "book/arrow_next.png" xoffset 80 action showscreen_action("page2", page=1)


screen page2:
        tag page
        vbox:
            frame:
                style "book_frame"
                image "book/page2.png"
            hbox:
                style "book_hbox"
                imagebutton idle "book/arrow_back.png" xoffset -80 action showscreen_action("open_book", page=2)
                imagebutton idle "book/close.png" action hidescreen_action("page2", close=True)
                imagebutton idle "book/arrow_next.png" xoffset 80 action showscreen_action("page3", page=3)


screen page3:
        tag page
        vbox:
            frame:
                style "book_frame"
                image "book/page3.png"
            hbox:
                style "book_hbox"
                imagebutton idle "book/arrow_back.png" xoffset -80 action showscreen_action("page2", page=2)
                imagebutton idle "book/close.png" action hidescreen_action("page3", close=True)
                imagebutton idle "book/arrow_next.png" xoffset 80 action showscreen_action("page4", page=4)


screen page4:
        tag page
        vbox:
            frame:
                style "book_frame"
                image "book/page4.png"
            hbox:
                style "book_hbox"
                imagebutton idle "book/arrow_back.png" xoffset -80 action showscreen_action("page3", page=2)
                imagebutton idle "book/close.png" action hidescreen_action("page4", close=True)
                image "book/arrow_next.png" xoffset 80 alpha 0.0
