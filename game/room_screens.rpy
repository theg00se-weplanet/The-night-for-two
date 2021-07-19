screen interactive():
    frame:
        background None
        hbox:
            imagebutton: # книга
                auto "book/book_%s.png"
                action showscreen_action("open_book"), play_sound(paging2), get_triggered(3)
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
            imagebutton: # пони
                auto "pony/pony_button_%s.png"
                focus_mask True
                action go_to_label("pony")
            imagebutton: # динозвар
                auto "dino/dino_button_%s.png"
                focus_mask True
                action go_to_label("dino")
            imagebutton: # глобус
                auto "globe/globe_button_%s.png"
                focus_mask True
                action go_to_label("globe")
            imagebutton: # шкаф
                auto "cupboard/cupboard_button_%s.png"
                focus_mask True
                action go_to_label("cupboard")
            imagebutton: # скетчбук
                auto "sketch/sketch_button_%s.png"
                focus_mask True
                action go_to_label("sketch")
