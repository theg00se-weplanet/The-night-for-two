init:
    #Add "cleft", "cright", "pleft"
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
    image pnhug = "images/pn_koikatsu/pn(hug).png"
    image pnthink = "images/pn_koikatsu/pn(think).png"
    image pnemb = "images/pn_koikatsu/pn(embarassed).png"
    image pnserious = "images/pn_koikatsu/pn(serious).png"
    image pnscared = "images/pn_koikatsu/pn(scared2).png"
    image pn = "images/pn_koikatsu/pn.png"
    image pnhappy = "images/pn_koikatsu/pn(happy).png"
    #Scenes
    image streamEndScreen = "images/streamEndScreen.png"
    image blink = "images/blackScreen.png"
    image mnRoomDay = "images/mnRoomDay.jpg"
    image mnRoomNight = "images/mnRoomNight.jpg"
    image SHtOra = "images/SHtOra.png"
    image heat = "images/heat.png"
    #Music
    $ streamEnd = "audio/music/mnStreamEnd.mp3"
    $ SHOwer = "audio/music/shower.mp3"
    $ water = "audio/music/water.mp3"
    $ predator = "audio/music/gentle_predator.mp3"
    $ madhouse = "audio/music/that_s_our_madhouse.mp3"
    $ darkness = "audio/music/sweet_darkness.mp3"
    $ doubts = "audio/music/waltz_of_doubts.mp3"
    $ maiden = "audio/music/forest_maiden.mp3"
    #Sounds
    $ zvon = "audio/zvon.mp3"
    $ bump = "audio/bump.mp3"
    $ door_close = "audio/door_close.mp3"
    #00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 STOP
label start:
    show text "{b} Я не буду искать оправданий{/b}\n Пролог" at truecenter with dissolve
    ""
    hide text with dissolve
    scene mnRoomNight with dissolve
    "Стоял теплый весенний вечер."
    "{size=-5}Закатные лучи солнца, робко светящие из приоткрытого окна и будто бы провожающие знойный день, освещали небольшую, явно девичью комнату, и словно из последних сил выхватывали из полутьмы то стоящее под столом мусорное ведерко, полное смятых листов бумаги, то старый и всеми забытый глобус, пылящийся высоко на шкафу.{/size}"
    "Однако шлем виртуальной реальности, графический планшет и альбом для рисования явно намекали: тут живет художник."
    "Точнее, художница, это можно было понять по маленьким пластиковым фигуркам из My Little Pony, хаотично расставленным везде, где только можно."
    "Также на это намекал плюшевый динозавр, вольготно раскинувшийся на громадной двуспальной кровати, и небольшой пушистый манул, одиноко стоящий на полке с книгами и с удивлением взирающий на весь этот хаос."
    $ renpy.pause(2)
    show mnhappy at center with dissolve
    show pnhappy at right with dissolve
    "У окна, за широким компьютерным столом, где стоял большой, наверное 30-и дюймовый монитор, сидели Мана и Планя."
    "Они махали руками и прощались со зрителями, придвинувшись поближе друг к другу."
    #play music streamEnd fadein 2
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
    stop music fadeout 2
    menu:
        "Крикнуть «Обнимашки!» и обнять Ману":
            $ hug_trigger = 1
            hide pnhug with dissolve
            show pnlaugh at cright with dissolve
            "Планя набрала побольше воздуха в легкие, расставила руки в стороны и с криком: «Ман, обнимашки!» прыгнула на подругу."
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
            "Планя облегченно выдохнула и опустила голову."
            "И почему ей все время чудится, будто она в чем-то виновата?.. {w}И вот сейчас тоже – ну надо же было подумать, будто Мана на нее за что-то дуется…"
            "Она медленно поднялась с кресла, с хрустом размяла затекшую спину и принялась задумчиво накручивать желтый локон на указательный палец, блуждая взглядом по творческому беспорядку Маниной комнаты-студии, а по совместительству еще и спальни."
            "Из коридора донесся шум включаемой воды и гулкие всплески – Мана принимала душ."
            hide pnthink with dissolve

        "Остаться на месте и ничего не делать":
            $ hug_trigger = 0
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
            hide pnemb with dissolve
            show pnshock at right with dissolve:
                yoffset 30
            show mngo at pleft with move
            "Планя, застыв в нелепой позе, с губами, свернутыми в трубочку, недоуменно наблюдала, как та повернулась к ней спиной и направилась к двери."
            "Сердце забилось тревожнее, а ладони предательски вспотели. Обиделась на что-то?.."
            hide mngo with dissolve
            show mntricky at pleft with dissolve
            "Но тут Мана, уже стоя в дверях, повернула голову и, сверкнув своими громадными огненными глазами, хитро подмигнула:"
            mn "А я в ванную!"
            hide mntricky with dissolve
            show mntrickynude at pleft with dissolve
            show mntrickynude at offscreenleft with move
            hide mntrickynude with dissolve
            "После чего стянула с себя топ, бросила его на середину комнаты, еще раз подмигнула и убежала."
            gs "НАШ ТОПИК (удали это перед выпуском)"
            "Планя некоторое время с удивлением смотрела на медленно оседающий на полу топ, а в голове ее был только одинокий перекати-поле, мечущийся туда-сюда под порывами ветра. А вокруг – бескрайняя пустыня, и ни деревца, ни озерца…"
            $ renpy.pause(1)
            "Что Мана имела в виду?.."
            "Она осторожно поднялась с кресла, сцепила руки над головой и принялась разминать затекшие мышцы, наклоняясь то вправо, то влево, а взгляд ее блуждал по творческому беспорядку Маниной комнаты-студии, а по совместительству еще и спальни."
            show pnshock at cright with move
            "Из коридора донесся шум включаемой воды, за ним последовал мощный всплеск-плюх, а потом по квартире разлилось тихое мелодичное пение – Мана в своем стиле принимала душ."
            hide pnshock with dissolve
    #Interactive part
    show screen interactive
    "здесь есть интерактив. \nможешь поиграться, я хз"
    "уже уходишь? ну ок, чё"
    "потом не жалуйся, если не всё посмотрел"
    hide screen interactive
    #End of interactive part :D
    scene blink with dissolve
    show text "Воспоминания" at truecenter with dissolve
    ""
    hide text with dissolve
    scene mnRoomNight with dissolve
    "Вот Мана со смехом тянется к Плане, они крепко обнимаются и звонко смеются."
    mn "Это было круто, Плань!"
    pn "Мана! Я от смеха чуть не умерла!"
    "Мана легонько чмокает подругу в щечку, Планя взвизгивает и тоже пытается чмокнуть в ответ, но Мана слегка отводит голову назад (то ли случайно, то ли намеренно), и их губы вроде бы невзначай касаются друг друга."
    "Планя краснеет и смущенно отворачивается."
    pn "Мана…"
    "Она выдыхает, не зная, куда девать свои глаза, но при этом не отпускает ее из своих объятий. "
    "А Мана вдруг касается носом ее щеки, и слегка ведет по ней, обжигая своим горячим дыханием."
    "Планя замирает, прислушиваясь к своим ощущениям, и начинает слегка дрожать, одновременно боясь и желая продолжения."
    $ renpy.pause(2)
    "А Мана опускает голову ниже, говорит шепотом: «Планюш, а ты знаешь, что ты очень красивая?..», и слегка кусает ту за ухо."
    "Планя часто-часто дышит, закрывает глаза и начинает все глубже погружаться в сладостный туман, постепенно окутывающий все ее тело."
    "А Мана тем временем спускается все ниже, доходит до шеи и легонько ее целует."
    mn "Твой талисман… Ты сама, как яркая звездочка…"
    "Планя лишь крепче прижимает ее к себе, по телу идут волны томной дрожи вперемешку с мурашками, а место, где лизнула подруга, вдруг начинает приятно покалывать."
    $ renpy.pause(2)
    "Мана спускается еще ниже, начинает стягивать с одного плеча лифчик вместе со свитером, постоянно целуя горящую кожу."
    "И тут накопившееся возбуждение вырывается наружу – Планя, слегка приоткрыв рот, издает хриплый стон."
    "Потом она открывает глаза, наклоняется  - и сразу же тонет в бездонном огненном взгляде, в котором смешалось все: и любовь, и вожделение, и страсть."
    "Их губы, будто на автопилоте, сами находят друг друга и сливаются в жарком и длинном поцелуе."
    "Планя, тяжело дыша носом, стонет и все никак не может остановиться, их языки сплетаются, сначала лишь нежно касаясь друг друга, а потом, словно поняв всю тщетность этих жалких попыток удержать кипящий водопад желания, сливаются в одно целое."
    "Мана тоже стонет, ее ладонь сначала бережно гладит подругу по шее, а спустя мгновение спускается вниз и залезает той под лифчик. "
    "Планя слегка дергается, ее красные щеки наливаются розовым румянцем еще сильнее."
    pn "Мана..."
    "Планя изгибается и гладит ее по волосам, чувствуя, как подруга пальцами осторожно сжимает набухший сосок."
    "Они прекращают целоваться, Мана смотрит Плане в глаза и слегка улыбается."
    "Потом она медленным движением стягивает вниз лифчик вместе со свитером, оголяя небольшие и упругие груди, и начинает медленно вести горячим языком по коже, от шеи – и дальше вниз, все ниже, и ниже…"
    

    #If Planya starts singing: 🌟⭐🌟⭐🌟⭐🌟⭐🌟
    $ renpy.pause(3)
    gs "тут должен быть текст-поздравление с тем, что ты прошёл игру и преисполнился в своём хорни-познании, но я не умею писать такие речи"
    gs "поэтому просто сделай вид, что ты тронут конечной речью, пожалуйста"
    gs "и да, спасибо, что прошёл! :3"
    return