init -3 python:
    def Go_to_Label(label_name):
        renpy.call_in_new_context(label_name)
    go_to_label = renpy.curry(Go_to_Label)


screen interactive():
    frame:
        background None
        hbox:
            imagebutton: # книга
                auto "book/book_%s.png"
                action showscreen_action("open_book", page=2)
                mouse say
            imagebutton: # кот
                auto "cat/cat_button_%s.png"
                focus_mask True
                action go_to_label("minecraft_cat")
            imagebutton: # манул
                auto "manul/manul_button_%s.png"
                focus_mask True
                action go_to_label("manul")
            imagebutton: # бирка
                auto "tag/tag_button_%s.png"
                focus_mask True
                action go_to_label("tags")
