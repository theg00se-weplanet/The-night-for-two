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
    define trigger_globe = False 
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
    image mnRoomBlur = "images/mnRoomNight Blur2.jpg"
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
    
label part1_2:
    hide screen interactive
    stop music fadeout 2
    scene blink with dissolve
    show text "Воспоминания" at truecenter with dissolve
    ""
    hide text with dissolve
    play music moar fadein 2
    scene mnRoomNight with dissolve
    show mnlaugh at center with dissolve
    show pnlaugh at right with dissolve:
        xoffset -90
    "Вот Мана со смехом тянется к Плане, они крепко обнимаются и звонко смеются."
    mn "Это было круто, Плань!"
    pn "Мана! Я от смеха чуть не умерла!"
    hide mnlaugh with dissolve
    show mntricky at center with dissolve
    "Мана легонько чмокает подругу в щечку, Планя взвизгивает и тоже пытается чмокнуть в ответ, но Мана слегка отводит голову назад (то ли случайно, то ли намеренно), и их губы вроде бы невзначай касаются друг друга."
    stop music fadeout 1
    $ renpy.pause(1)
    play music bittersweet fadein 2
    hide pnlaugh with dissolve
    show pnemb at right behind mntricky with dissolve:
        xoffset -90
    "Планя краснеет и смущенно отворачивается."
    pn "Мана…"
    "Она выдыхает, не зная, куда девать свои глаза, но при этом не отпускает ее из своих объятий. "
    "А Мана вдруг касается носом ее щеки, и слегка ведет по ней, обжигая своим горячим дыханием."
    "Планя замирает, прислушиваясь к своим ощущениям, и начинает слегка дрожать, одновременно боясь и желая продолжения."
    $ renpy.pause(2)
    show mntricky at center with move:
        linear 0.5 yoffset 50
    "А Мана опускает голову ниже, говорит шепотом: «Планюш, а ты знаешь, что ты очень красивая?..», и слегка кусает ту за ухо."
    "Планя часто-часто дышит, закрывает глаза и начинает все глубже погружаться в сладостный туман, постепенно окутывающий все ее тело."
    show mntricky at center with move:
        linear 0.4 yoffset 80
    "А Мана тем временем спускается все ниже, доходит до шеи и легонько ее целует."
    mn "Твой талисман… Ты сама, как яркая звездочка…"
    "Планя лишь крепче прижимает ее к себе, по телу идут волны томной дрожи вперемешку с мурашками, а место, где лизнула подруга, вдруг начинает приятно покалывать."
    $ renpy.pause(2)
    show mntricky at center with move:
        linear 0.4 yoffset 110
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
    "Планя закрывает глаза и крепче сжимает дрожащими руками голову Маны, ее рот открыт и она не может удержать сладостный стон."
    $ renpy.pause(1)
    "А Мана тем временем доводит влажную дорожку до соска и лижет его, чувствуя, как тело подруги дрожит и отзывается на каждое прикосновение."
    "И вот сосок уже полностью у нее во рту, Мана слегка прикусывает его зубами, и тут же отпускает, вслушиваясь в прерывистое дыхание Плани, а потом продолжает свое движение дальше вниз, попутно стягивая так мешающую одежду вниз."
    show mntricky at center with move:
        linear 0.5 yoffset 220
    "И вот она оказывается возле живота, поднимающегося и опускающегося в такт дыханию, задерживается и медленно проводит кончиками ногтей по нежной коже, которая тут же покрывается мурашками, мягко целует белую кожу."
    "И вдруг одним махом стягивает кофту с лифчиком через верх. Планя только и успевает поднять руки, одежда улетает куда-то в сторону, а их раскрасневшиеся губы вновь встречаются во влажном и жгучем поцелуе."
    "{size=-5}Обе девушки уже закипают от наполняющего их желания, Планя ногтями впивается Мане в спину и прижимает к себе, та же глубоко зарывается ладонями в золотистую гриву и, сжав кулаки, за волосы тянет ее голову на себя, языки переплетаются и обволакивают друг друга, словно сражаясь за то, кто глубже проникнет в чей рот. {/size}"
    $ renpy.pause(1)
    "Мана резко прекращает затянувшийся засос, с тихим чмоканьем отлепившись от Плани."
    "Ее щеки горят алым, дыхание тяжелое и прерывистое, а пламенеющие широко раскрытые глаза кажется могут поглотить не только Планю, но и вообще весь мир."
    show mntricky at center with move:
        linear 0.2 yoffset 400
    "Она в один миг спускается на колени и стягивает с подруги шорты вместе с трусиками."
    pn "Мана, Маночка…"
    "Планя шепчет, руками обхватив голову Маны."
    "А та, раздвинув ее колени и слегка притянув бедра к себе, зарывается языком между ног, в кипящую и влажную бездну…"
    $ renpy.pause(1)
    "Планя стонет и чуть ли не кричит, руками вжимая Ману в себя как можно сильнее, а та языком проникает все глубже…"
    $ renpy.pause(3)
    hide mntricky with dissolve
    hide pnemb with dissolve
    scene blink with dissolve
    stop music fadeout 2
    show text "Настоящее время" at truecenter with dissolve
    ""
    hide text with dissolve
    play music reflective fadein 2
    scene mnRoomNight with dissolve
    show pnshock at center with dissolve:
        yoffset 300
    "Планя открыла глаза и поняла, что лежит на кровати, одна ее рука зажата между стиснутых ног, а вторая залезла под лифчик и сжимает уже сильно набухший левый сосок."
    hide pnshock with dissolve
    show pnemb at center with dissolve:
        yoffset 300
    show pnemb at center with move:
        yoffset 120
    "Она густо покраснела, отдернула руку от груди и села."
    "Они ведь о том случае даже парой слов не обмолвились… {w}Но, видимо, этот локомотив из любви и вожделения уже было не остановить…"
    "Планя прислушалась к звуку льющейся воды: Мана плескалась от души и что-то пела, и ей вдруг показалось, что она так громко плещется намеренно, словно завлекает ее поскорее к себе."
    "А может, она все неправильно поняла?.."
    "Под трусиками приятно заныло, вгоняя Планю в краску еще сильнее."
    "Да что тут можно неправильно понять!?"
    show pnemb at center with move:
        linear 0.2 yoffset 0
    hide pnemb with dissolve
    show pn with dissolve
    "Планя резко вскочила с кровати, стянула с себя шорты и бросила их в общую кучу, где уже лежал Манин топ и ее кофта."
    menu:
        "Снять трусики":
            hide pn with dissolve
            show pnthink at center with dissolve:
                linear 0.2 yoffset 70
            "Планя наклонилась и начала стягивать с себя черные трусики, которые, как это ни удивительно, оказались насквозь мокрые."
            "Ох уж эта Мана…"
            stop music fadeout 1
            $ renpy.pause(1)
            play music bittersweet_anthem fadein 2
            hide pnthink with dissolve
            show pnshock at center with dissolve
            show pnshock at center with move:
                linear 0.1 xoffset 40
            show pnshock at center with move:
                linear 0.2 xoffset -40
            show pnshock at center with move:
                linear 0.1 xoffset 0
            "Планя задумчиво тянула их вниз и вдруг потеряла равновесие, запутавшись ногой в непослушном белье."
            show pnshock at leap with move 
            "Пытаясь не упасть, она  попыталась выставить одну ногу вперед, но трусы зацепились крепко, и она запрыгала на другой ноге, расставив локти в стороны."
            show pnshock at center with move:
                linear 0.1 yoffset 400
            hide pnshock with dissolve
            play sound bump
            show pnpain at center with dissolve:
                 yoffset 400
            if trigger_globe == True:
                "Эти акробатические упражнения не помогли, и в итоге Планя плашмя рухнула вперед, больно ударившись об пол коленом, причем тем же самым, которое она больно ушибла о шкаф 5 минут назад, а через секунду еще и ощутимо приложившись лбом."
            else:
                "Эти акробатические упражнения не помогли, и в итоге Планя плашмя рухнула вперед, больно ударившись об пол коленом, а через секунду еще и ощутимо приложившись лбом."
            "И так и застыла на некоторое время, являя миру соблазнительно торчащие бедра и теперь уже свободно сползающие по ноге трусики."
            "Спустя мгновение Планя вышла из ступора, застонала и обессилено завалилась на бок."
            pn "Ну ты дала, Плань…"
            "Она растирала ушибленное колено."
            if trigger_globe == True:
                pn "И опять этой же коленкой! Просто 10 из 10! Даже трусы снять нормально не можешь!"
                "Она стукнула по ноющему месту ладошкой, вскрикнула от боли, сморщилась и поднялась на ноги."
            else:
                pn "Как обычно, на ровном месте – и синяк."
                "Она внимательно осмотрела ноющее колено, еще немного его потерла, зашипев от боли, и с трудом поднялась."
            show pnpain at center with move:
                linear 0.4 yoffset 0
            hide pnpain with dissolve
            show pn at center with dissolve
            "Покрутив в руках коварные трусы, Планя кинула их во все увеличивающуюся кучу с одеждой и повернулась к двери, намереваясь все-таки дойти до Маны."
        "Снять лифчик":
            "Планя привычным движением занесла руку за спину и попыталась расстегнуть застежку лифчика."
            stop music fadeout 1
            $ renpy.pause(1)
            play music bittersweet_anthem fadein 2
            "Но не тут-то было – металлический замок не поддавался."
            hide pn with dissolve
            show pnserious at center with dissolve
            pn "Да ладно!"
            "Она продолжала и так, и эдак пытаться его расстегнуть."
            "Планя закрутилась на месте, подсовывая под лямку пальцы, в ход уже пошла и вторая рука, но все было тщетно – намертво заклинившая застежка отказывалась подчиняться."
            "Зубцы замка словно приварило друг к другу, и казалось, что этот чудовищный лифчик мерзко хихикает и про себя думает: «Не дойдешь ты сегодня до Маны, маленькая извращенка! Ох, не дойдешь!»"
            pn "Да чтоб тебя!"
            "Разозлившись, Планя с силой потащила взбунтовавшееся белье наверх и стянула его через голову."
            hide pnserious with dissolve
            show pnpain at center with dissolve
            "И тут внезапно кожа на спине взорвалась острой болью – перекрученный замок напоследок отомстил своей хозяйке и на пути наверх одним из своих зубьев оставил глубокую и по ощущениям кровоточащую царапину."
            pn "Ах ты ж твою Господи зараза!"
            "Планя зашипела, пытаясь заглянуть через плечо и оценить повреждения."
            "Но, конечно, ничего не вышло - как ни старайся, а свою спину можно увидеть только в зеркале."
            "Планя застонала от бессилия и топнула ногой по полу."
            if trigger_globe == True:
                pn "Да что за день сегодня такой!"
                pn "Сначала колено, теперь лифан этот долбанный…"
            else:
                pn "Вот знала же, что не стоит покупать это коварное китайское говно!"
            "Она в сердцах швырнула вероломное белье во все увеличивающуюся кучу с одеждой и повернулась к двери, намереваясь все-таки дойти до Маны."
            hide pnpain with dissolve
            show pn at center with dissolve
    $ renpy.pause(1)
    hide pn with dissolve
    show pnshock at center with dissolve
    scene mnRoomNightDark with dissolve
    stop music fadeout 1
    $ renpy.pause(1)
    play music otome fadein 2
    "И тут – мир вокруг начал резко темнеть, на границе видимости поплыли белые пятна, а вестибулярный аппарат вдруг отказался определять, где верх, а где низ."
    show pnshock at center with move:
        linear 0.1 xoffset 40
    show pnshock at center with move:
        linear 0.2 xoffset -40
    show pnshock at center with move:
        linear 0.1 xoffset 0
    scene blink with dissolve
    scene mnRoomNightDark with dissolve
    "Планю зашатало, она сделала неуверенный шаг вперед, зажмурилась и с силой потерла глаза."
    pn "Это еще что такое?.."
    scene mnRoomBlur with dissolve
    "Пятен в поле зрения становилось все больше, комната начала кружиться, а ноги отказывались слушаться и превратились в ватные колонны, которые были не в силах удержать такое враз потяжелевшее тело…"
    scene blink with dissolve
    play sound bump
    "Планя только и успела, что шагнуть назад, к кровати, и тут словно пьяный электрик отрубил все электричество – свет в ее глазах померк окончательно, а сознание безо всякого предупреждения покинуло это тело, тут же неловко рухнувшее на кровать."
    scene blink with dissolve

    #This text is useless, but I want this file to contain at least 500 lines xD
    stop music fadeout 2
    scene blink with dissolve
    $ renpy.pause(2)
    gs "тут должен быть текст-поздравление с тем, что ты прошёл игру и преисполнился в своём хорни-познании, но я не умею писать такие речи"
    gs "поэтому просто сделай вид, что ты тронут конечной речью, пожалуйста"
    gs "и да, спасибо, что прошёл! :3"
    return