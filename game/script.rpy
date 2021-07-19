init:
    #Add "cleft", "cright", "halfcright", "pleft"
    transform cleft:
        xalign .4 yalign 1.0
    transform cright:
        xalign .6 yalign 1.0
    transform pleft:
        xalign .1 yalign 1.0
    #Fix left, right
    transform left:
        xalign .3 yalign 1.0
    transform right:
        xalign .7 yalign 1.0
    #Add jumps
    transform leap(dyz=0.01, dxz=0.005, dt=.4):
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
    #Characters
    $ mn = Character (u'Мана', color="#57b0ff", what_color="#ffffff", who_drop_shadow=[ (2, 1) ] )
    $ pn = Character (u'Планя', color="#fced3f", what_color="#ffffff", who_drop_shadow=[ (2, 1) ] )
    $ dpn = Character (u'Планя', color="#d4c204", what_color="#ffffff", who_drop_shadow=[ (2, 1) ] )
    $ gs = Character (u'гусиный посол', color="#ff9221", what_color="#ffffff", who_drop_shadow=[ (2, 1) ])
    #Some triggers
    define hug_trigger = -1
    define i = False
    define trigger_globe = False
    $ trigger_dino = trigger_globe = trigger_book_3 = trigger_book_4 = False
    #Mana's sprites
    image mnlaugh = "images/mn_koikatsu/mn(laugh).png"
    image mnconc = "images/mn_koikatsu/mn(concentrated).png"
    image mncalmsleep = "images/mn_koikatsu/mn(calmsleep).png"
    image mn = "images/mn_koikatsu/mn.png"
    image mngo = "images/mn_koikatsu/mn(go).png" #mango xDDD (check images/mn_koikatsu/mngo.jpg)
    image mntricky = "images/mn_koikatsu/mn(tricky).png"
    image mntrickynude = "images/mn_koikatsu/mn(trickynude).png"
    image mnhappy = "images/mn_koikatsu/mn(happy).png"
    image mnhug = "images/mn_koikatsu/mn(hug).png"
    image mnpained = "images/mn_koikatsu/mn(pained).png"

    #Planya's sprites
    image pnlaugh = "images/pn_koikatsu/pn(laugh).png"
    image pnshock = "images/pn_koikatsu/pn(shock).png"
    image pnpain = "images/pn_koikatsu/pn(shock2).png"
    image pnhug = "images/pn_koikatsu/pn(hug).png"
    image pnthink = "images/pn_koikatsu/pn(think).png"
    image pnemb = "images/pn_koikatsu/pn(embarassed).png"
    image pnserious = "images/pn_koikatsu/pn(serious).png"
    image pnscared = "images/pn_koikatsu/pn(scared2).png"
    image pn = "images/pn_koikatsu/pn.png"
    image pnhappy = "images/pn_koikatsu/pn(happy).png"
    #Scenes
    image mnRoomNightDark = "images/mnRoomNightDark.jpg"
    image mnRoomNight = "images/mnRoomNight.jpg"
    image mnRoomBlur = "images/mnRoomNightBlur2.jpg"
    image blink = "images/blackScreen.png"
    #Music $  = "audio/music//.mp3" #
    $ SHOwer = "audio/music/shower.mp3"
    $ calm = "audio/music/calm.mp3"
    $ erotic_lovers = "audio/music/erotic_lovers.mp3" #For erotic scenes

    $ vntrack01 = "audio/music/ternox/vntrack01.mp3" #Calm, and i love it!
    $ vntrack03 = "audio/music/ternox/vntrack03.mp3" #Sad
    $ vntrack12 = "audio/music/ternox/vntrack12.mp3" #Sad, dynamic
    $ vntrack18 = "audio/music/ternox/vntrack18.mp3" #Horror
    $ vntrack19 = "audio/music/ternox/vntrack19.mp3" #Very calm
    $ vntrack21 = "audio/music/ternox/vntrack21.mp3" #Very sad, but the beats...

    $ bittersweet_anthem = "audio/music/lunaLucid/Bittersweet_Anthem.mp3" #Anxious, dymamic
    $ calamity = "audio/music/lunaLucid/Calamity.mp3" #Mystery, sad
    $ change = "audio/music/lunaLucid/cc_bgm_change.mp3" #Calm, sad, dynamic
    $ destiny = "audio/music/lunaLucid/Destiny.mp3" #Dynamic, anxious
    $ dubious = "audio/music/lunaLucid/Dubious.mp3" #Sad, dynamic
    $ mission = "audio/music/lunaLucid/Mission.mp3" #Some electro
    $ moar = "audio/music/lunaLucid/Moar_BGM.mp3" #Happy, dynamic
    $ otome = "audio/music/lunaLucid/Otome90.mp3" #Mystery, dancing
    #$ risen = "audio/music/lunaLucid/Risen.wav" #Some mystery

    $ romantic = "audio/music/green_bear_music/romanticbgm.mp3"
    $ reflective = "audio/music/green_bear_music/reflectivebgm.mp3" #Lovely
    $ bittersweet = "audio/music/green_bear_music/bittersweetbgm.mp3" #Erotic
    $ theme = "audio/music/green_bear_music/themebgm.mp3" #Sad, mystery - I love it!
    $ cheerful = "audio/music/green_bear_music/cheerfulbgm.mp3"
    $ cheerful2 = "audio/music/green_bear_music/cheerfulbgm2.mp3"
    $ daily = "audio/music/green_bear_music/dailybgm.mp3"
    $ daily2 = "audio/music/green_bear_music/dailybgm2.mp3"
    $ happy = "audio/music/green_bear_music/happybgm.mp3"
    $ mysterious = "audio/music/green_bear_music/mysteriousbgm.mp3"
    $ rock = "audio/music/green_bear_music/rockbgm.mp3"
    $ sleep = "audio/music/green_bear_music/sleepbgm.mp3"
    #Sounds
    $ zvon = "audio/zvon.mp3"
    $ bump = "audio/bump.mp3"
    $ door_close = "audio/door_close.mp3"

label start:
    show text "{b} Я не буду искать оправданий{/b}\n Пролог" at truecenter with dissolve
    ""
    hide text with dissolve
    scene mnRoomNight with dissolve
    play music vntrack01 fadein 2
    "Стоял теплый весенний вечер."
    "{size=-5}Закатные лучи солнца, робко светящие из приоткрытого окна и будто бы провожающие знойный день, освещали небольшую, явно девичью комнату, и словно из последних сил выхватывали из полутьмы то стоящее под столом мусорное ведерко, полное смятых листов бумаги, то старый и всеми забытый глобус, пылящийся высоко на шкафу.{/size}"
    "Однако шлем виртуальной реальности, графический планшет и альбом для рисования явно намекали: тут живет художник."
    "Точнее, художница, это можно было понять по маленьким пластиковым фигуркам из My Little Pony, хаотично расставленным везде, где только можно."
    "Также на это намекал плюшевый динозавр, вольготно раскинувшийся на громадной двуспальной кровати, и небольшой пушистый манул, одиноко стоящий на полке с книгами и с удивлением взирающий на весь этот хаос."
    $ renpy.pause(2)
    show mnhappy at center with dissolve
    show pnhappy at right with dissolve
    "У окна, за широким компьютерным столом, где стоял большой, наверное, 30-и дюймовый монитор, сидели Мана и Планя."
    "Они махали руками и прощались со зрителями, придвинувшись поближе друг к другу."
    stop music fadeout 1
    $ renpy.pause(1)
    play music moar fadein 2
    "И вот наконец стрим закончился и пошла финальная заставка."
    "Чат, как обычно, заполнился тоннами решеток с циркумфлексами, а Мана с Планей облегченно откинулись на спинки своих кресел, выдохнули и посмотрели друг на друга."
    mn "Плань, а ты сегодня молодец!"
    "Планя сцепила руки над головой и, как кошка, мягко потянулась."
    pn "Ман, ты тоже жгла!{w} А как их разорвало, когда мы устроили обнимашки, а?"
    hide mnhappy with dissolve
    show mnlaugh at center with dissolve
    "Мана рассмеялась и взъерошила свои голубые волосы. Ответила:"
    mn "Ну! Хорни-хорни-циркумфлекс!"
    hide pnhappy with dissolve
    show pnlaugh at right with dissolve
    "Обе вновь рассмеялись, звонкий смех яркими колокольчиками пронесся по небольшой комнате и звенящим ветерком затих в дальнем углу."
    $ renpy.pause(1)
    hide mnlaugh with dissolve
    show mnconc at center with dissolve
    stop music fadeout 1
    $ renpy.pause(1)
    play music reflective fadein 2
    "Вдруг Мана что-то заметила на экране монитора, придвинулась к клавиатуре, нахмурилась и начала быстро печатать."
    hide pnlaugh with dissolve
    show pnhug at right with dissolve
    "А Планя залюбовалась своей лучшей подругой."
    "Ей нравилось вот так исподтишка за ней наблюдать, когда та чем-то недовольна или злится."
    "Ее брови мило сходятся к переносице, губы вытягиваются в тонкую струну, а миниатюрный носик смешно морщится."
    "Планя осторожно придвинулась поближе, рассматривая и вбирая в себя в каждую черточку (такого уже родного) лица, небольшие, слегка оттопыренные уши, стройная и изящная шея, будто созданная для того, чтобы ее целовали, ..."
    "...ярко-алые, горящие изнутри глаза, пара непослушных голубых прядей, которые Мана уже который раз безуспешно пыталась откинуть рукой, а те упрямыми пружинами возвращались на место и продолжали маячить перед глазами."
    hide mnconc with dissolve
    show mncalmsleep at center with dissolve:
        linear 0.4 yoffset 100
    "Тут Мана закончила печатать, откинулась назад, вздохнула и расслабленно закрыла глаза."
    "А Планя замерла на месте, не зная, что делать: то ли с криком: «Обнимашки!» наброситься на подругу, то ли отвести взгляд и ничего не делать…"
    menu:
        "Крикнуть «Обнимашки!» и обнять Ману":
            $ hug_trigger = 1
            stop music fadeout 1
            $ renpy.pause(1)
            play music cheerful fadein 2
            hide pnhug with dissolve
            show pnlaugh at cright with dissolve
            "Планя набрала побольше воздуха в легкие, расставила руки в стороны и с криком: «Ман, обнимашки!» прыгнула на подругу."
            stop music fadeout 1
            $ renpy.pause(1)
            play music theme fadein 2
            hide mncalmsleep with dissolve
            show mngo at center with dissolve
            show mngo at left with move
            "Но та вдруг резко открыла глаза, ловко увернулась от объятий, встала и сделала шаг назад."
            hide pnlaugh with dissolve
            show pnshock at cright with dissolve
            "А Планя, обняв воздух, удивленно мяукнула и растерянно посмотрела на подругу."
            "Ее сердце вдруг заухало, гулко отдаваясь в уши, а ладони мгновенно вспотели."
            "Что тут происходит?.."
            show mngo at pleft with move
            "Тем временем Мана повернулась к ней спиной и направилась к выходу из комнаты."
            "Планя, замерев, проводила взглядом уходящую подругу. Неужели обиделась? {w}Она что-то сделала не так?.."
            stop music fadeout 1
            $ renpy.pause(1)
            play music cheerful2 fadein 2
            "Но тут Мана, уже стоя в дверях, повернула голову и, сверкнув своими громадными огненными глазами, хитро подмигнула:"
            hide mngo with dissolve
            show mntricky at pleft with dissolve
            mn "А я в ванную!"
            hide mntricky with dissolve
            show mntrickynude at pleft with dissolve
            "После чего стянула с себя топ, еще раз внимательно посмотрела на Планю, бросила его на середину комнаты и убежала."
            gs "НАШ ТОПИК (удали это перед выпуском)"
            show mntrickynude at offscreenleft with move
            hide mntrickynude
            hide pnshock with dissolve
            show pnthink at cright with dissolve
            stop music fadeout 1
            $ renpy.pause(1)
            play music romantic fadein 2
            "Планя облегченно выдохнула и опустила голову."
            "И почему ей все время чудится, будто она в чем-то виновата?.. {w}И вот сейчас тоже – ну надо же было подумать, будто Мана на нее за что-то дуется…"
            "Она медленно поднялась с кресла, с хрустом размяла затекшую спину и принялась задумчиво накручивать желтый локон на указательный палец, блуждая взглядом по творческому беспорядку Маниной комнаты-студии, а по совместительству еще и спальни."
            stop music fadeout 1
            $ renpy.pause(1)
            play music shower fadein 2 volume 0.4
            "Из коридора донесся шум включаемой воды и гулкие всплески – Мана принимала душ."
            hide pnthink with dissolve
            stop music fadeout 2
        "Остаться на месте и ничего не делать":
            $ hug_trigger = 0
            stop music fadeout 1
            $ renpy.pause(1)
            play music vntrack12 fadein 2
            hide pnhug with dissolve
            show pnemb at right with dissolve
            "Планя смущенно отвела взгляд и застыла на месте, не зная, что ей делать со своими не совсем дружескими мыслями."
            "Шея, созданная для поцелуев, и как такое в голову-то пришло?.."
            "Они конечно уже давние и лучшие подруги, но после прошлого раза, когда ночью, у них… {w}Они тогда, после стрима…"
            hide mncalmsleep with dissolve
            show mnhappy at center with dissolve
            mn "Плань!"
            hide pnemb with dissolve
            show pnshock at right with dissolve:
                yoffset 20
            show pnshock at right with move:
                linear 0.1 yoffset 0
            show pnshock at right with move:
                linear 0.1 yoffset 20
            "Она вздрогнула и испуганно посмотрела на Ману."
            hide pnshock with dissolve
            show pnserious at right with dissolve
            "Планя напустила на себя самый серьезный вид, какой только сумела изобразить, но не смогла и секунды выдержать этого смеющегося взгляда."
            hide mnhappy with dissolve
            show mnlaugh at center with dissolve
            hide pnserious with dissolve
            show pnlaugh at right with dissolve
            "Сначала хрюкнула и прыснула Мана, а за ней и Планя залилась звонким, заразительным смехом."
            mn "Плань, обнимашки!"
            "Мана стремительно покатилась в ее сторону на кресле."
            show pnlaugh at right with move:
                linear 0.2 xoffset 130
            show mnlaugh at right with move
            "Планя шутливо отшатнулась назад, но конечно не смогла избежать широко расставленных рук, и стремительная кресловая атака закончилась взаимными, крепкими и может не совсем дружескими объятиями."
            hide pnlaugh with dissolve
            show pnhug at right with dissolve:
                xoffset 130
            hide mnlaugh with dissolve
            show mnhug at right with dissolve
            $ renpy.pause(2)
            #Art?
            "Планя целиком зарылась в голубые, приятно пахнущие волосы, вдыхала их запах и все крепче прижимала к себе Ману."
            "А та, носом растормошив ярко-желтые непослушные вихры, вдруг отстранилась и прильнула теплыми губами к ее щеке."
            hide pnhug with dissolve
            show pnemb at right with dissolve:
                xoffset 130
            "Тук-тук-тук… Почему сердце так стучит каждый раз, когда Мана ее целует, пусть даже и в щеку?.. "
            show pnemb at right with move:
                linear 0.3 xoffset 40
            hide mnhug with dissolve
            show mngo at right with dissolve
            show mngo at center with move
            "Планя выдохнула и тоже попыталась поцеловать подругу в ответ, но та уже отодвинулась и поднялась с кресла."
            stop music fadeout 1
            $ renpy.pause(1)
            play music theme fadein 2
            hide pnemb with dissolve
            show pnshock at right with dissolve:
                yoffset 30
            show mngo at pleft with move
            "Планя, застыв в нелепой позе, с губами, свернутыми в трубочку, недоуменно наблюдала, как та повернулась к ней спиной и направилась к двери."
            "Сердце забилось тревожнее, а ладони предательски вспотели. Обиделась на что-то?.."
            hide mngo with dissolve
            stop music fadeout 1
            $ renpy.pause(1)
            play music cheerful2 fadein 2
            show mntricky at pleft with dissolve
            "Но тут Мана, уже стоя в дверях, повернула голову и, сверкнув своими громадными огненными глазами, хитро подмигнула:"
            mn "А я в ванную!"
            hide mntricky with dissolve
            show mntrickynude at pleft with dissolve
            show mntrickynude at offscreenleft with move
            hide mntrickynude with dissolve
            "После чего стянула с себя топ, бросила его на середину комнаты, еще раз подмигнула и убежала."
            gs "НАШ ТОПИК (удали это перед выпуском)"
            stop music fadeout 1
            $ renpy.pause(1)
            play music romantic fadein 2
            "Планя некоторое время с удивлением смотрела на медленно оседающий на полу топ, а в голове ее был только одинокий перекати-поле, мечущийся туда-сюда под порывами ветра. А вокруг – бескрайняя пустыня, и ни деревца, ни озерца…"
            $ renpy.pause(1)
            "Что Мана имела в виду?.."
            "Она осторожно поднялась с кресла, сцепила руки над головой и принялась разминать затекшие мышцы, наклоняясь то вправо, то влево, а взгляд ее блуждал по творческому беспорядку Маниной комнаты-студии, а по совместительству еще и спальни."
            show pnshock at cright with move
            stop music fadeout 1
            $ renpy.pause(1)
            play music shower fadein 2 volume 0.4
            "Из коридора донесся шум включаемой воды, за ним последовал мощный всплеск-плюх, а потом по квартире разлилось тихое мелодичное пение – Мана в своем стиле принимала душ."
            hide pnshock with dissolve
            stop music fadeout 2
    $ renpy.pause(2)
    play music daily fadein 2
    show screen interactive
    while i == False:
        ""
        $ renpy.pause(100)
