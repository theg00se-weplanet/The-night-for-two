init:
    #same text
    #Add "cleft", "cright"
    transform cleft:
        xalign .4 yalign 1.0
    transform cright:
        xalign .6 yalign 1.0
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
    $ speedrun = Character (u'Anonymous', color="#ff9221", what_color="#ffffff", who_drop_shadow=[ (2, 1) ])
    #Mana's sprites
    image imn = "images/mn/mn.png"
    image imnhappy = "images/mn/mn(happy).png"
    image imnsad = "images/mn/mn(sad).png"
    image imnSHOck = "images/mn/mn(shock).png"
    image imnshadow = "images/mn/mn(shadow).png"
    #Planya's sprites
    image ipn = "images/pn/pn(cute).png"
    image ipnshock = "images/pn/pn(shock).png"
    image ipnsad = "images/pn/pn(sad).png"
    image ipnsleep = "images/pn/pn(sleep).png"
    image ipndark = "images/pn/pn(dark).png"
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

label start:
    show text "{b} Я не буду искать оправданий (рабочее название, не бейте) {/b}\n Пролог" at truecenter with dissolve
    ""
    hide text with dissolve
    play music streamEnd fadein 2
    scene streamEndScreen with dissolve
    "По экрану монитора заиграла заставка, а знакомая тысячам мелодия ознаменовала окончание стрима."
    "Чат запестрел сообщениями, чередуя комплименты, благодарность и самые разнообразные смайлики, в особенности с сердечками. {w}Но именно этим вечером сердечки были двух цветов – синие и желтые."
    scene mnRoomNight with dissolve
    show screen eggs(_layer = "easter_layer")
    $ renpy.pause(2)
    show imn at cleft with dissolve
    "Устало потянувшись и мило някнув, Мана встала из-за компьютера и, поправив кофточку, обернулась в сторону Плани."
    "Сегодня был совместный стрим по просмотру фильма вместе с подписчиками. {w}В этот раз стрим растянулся на добрых три часа."
    "Сам фильм оказался интересным, чатик был только рад продолжительности трансляции, но сама Мана могла сказать точно – она устала и хотела расслабиться, но вряд ли бы она призналась в этом перед своей любимой подругой."
    show ipn at cright with dissolve
    "Сама же Планя в этот момент с интересом вчитывалась в сообщения прощающегося чатика и лишь посмеивалась над завязавшейся борьбой между желающими «посчитать манулов» и фанатиками «циркумфлекса»."
    "В конце концов, щелчком оборвав последние мгновения стрима и шутливой перепалки, она со смешком сказала: "
    stop music
    hide imn with dissolve
    pn "Даже модеры в конце концов присоединились к хаосу в чатике и..."
    play music SHOwer fadein 3
    "Обернувшись вслед за своими словами, Планя увидела лишь пустую комнату. {w}Окинув взглядом углы и и кровать, она настороженно встала с кресла, но шум воды из коридора подсказал ей, что Мана в данный момент принимает душ."
    "Хитро улыбнувшись, Планя на цыпочках прокралась к двери ванной комнаты и слегка приоткрыла дверь."
    $ renpy.hide_screen("eggs", layer="easter_layer")
    scene SHtOra with dissolve
    play music predator fadein 3
    show imnshadow at left with dissolve
    "Сквозь лёгкую завесу пара угадывался стройный силуэт, омываемый упругими водными струями."
    "На секунду, невольно залюбовавшись этой картиной, Планя поддалась вспыхнувшим искрам своей фантазии и даже чуточку покраснела.{w} На ум невольно пришли воспоминания ночи со времен предыдущего коллаба, унося девушку всё дальше от реальности..."
    "Прикрыв глаза и успокоив себя коротким вздохом, Планя внезапно хитро улыбнулась пришедшей на ум шалости."
    "Возникшая идиллия умиротворения прервалась внезапным:"
    stop music fadeout 1
    play music madhouse fadein 2
    pn "МАНА!!! Как водичка?!"  with vpunch
    show imnshadow at leap with move
    "Силуэт покачнулся и вместо ответа то ли мявкнул, то ли чертыхнулся."
    "Не дождавшись продолжения, нарушительница спокойствия крикнула:"
    pn "Подожди! Сейчас приду и сама проверю!"
    stop music fadeout 1
    play sound door_close
    scene mnRoomNight with dissolve
    hide mnshadow with dissolve
    "Планя громко хлопнула дверью, прокрутилась на пятках и направилась обратно в комнату, мурлыча себе под нос незатейливый мотивчик."
    scene blink with dissolve
    show text "Сцена недоступна в демо-версии \n Ценители хорни, приносим свои временные извинения >_<" at truecenter with dissolve
    play music maiden fadein 2
    "Девушка подобралась к кровати и в считанные секунды избавилась от одежды, явив миру прелестное юное тело."
    "Её бледная чистая кожа, казалось, излучала лёгкое сияние, румянец расцветал прекрасными цветками от едва заметной прохлады после теплых оков одежды."
    "Cлегка учащенное дыхание заставляло грудь колыхаться, а два розоватых соска уже затвердели от фантазий, которые девушке уже не терпелось воплотить."
    hide text with dissolve
    scene mnRoomNight with dissolve
    pn "Ах, точно, носки же ещё, блин!"
    stop music fadeout 1
    scene blink
    "С этой мыслью Планя присела на краешек кровати и только собралась избавиться от «последнего препятствия на пути к Мане», как внезапно мир вокруг словно потемнел, а голова заполнилась звоном."
    play sound bump
    "Тело девушки мягко завалилось набок, уронив голову прямиком на подушку. {w}Комната погрузилась в тишину..."
    $ renpy.pause(3)
    play music doubts fadein 3
    scene mnRoomNight with dissolve
    show imnsad at left with dissolve
    "Спустя какое-то время в комнату вернулась Мана в своей обыкновенной кофте и с обиженным выражением на личике."
    mn "Планя, ну что за шутки? Сначала напугала - я думала, прямо в душе коней двину, а теперь заставила прождать почти цел…"
    hide imnsad with dissolve
    show imnSHOck at left with dissolve
    "Девушка осеклась, увидев свою подругу на кровати."
    hide imnSHOck with dissolve
    show imn at left with dissolve
    "Она наклонилась к лицу Плани и замерла, но, услышав спокойное глубокое дыхание, мягко улыбнулась, а её глаза наполнились теплом."
    mn "Пусть ты и утверждаешь обратное, но ты очень устала, и тебе действительно стоит как можно чаще отдыхать."
    show imn at offscreenleft with move
    "C этими словами, произнесенными полушепотом, Мана ненадолго вышла из комнаты, дабы вернуться с теплым пушистым пледиком."
    $ renpy.pause(1)
    show imn at left with move
    "Сначала она помогла подруге улечься поудобнее, подняв её ноги на кровать, но не спешила убрать с них свои руки. "
    "Тихонько, кончиками пальцев поглаживая шелковистую кожу ног, Maна вдруг обратила внимание на носочки."
    mn "Странно, не припомню, чтобы Планя когда-либо ложилась спать в носках. Если она раздевается, то обычно полностью и…"
    hide imn with dissolve
    show imnSHOck at left with dissolve
    "Hа этих мыслях лицо синеволосой стремительно покраснело, а взгляд заметался по сторонам, словно ища укрытие от нахлынувших мыслей."
    "Как бы Мана не устала, но чего ей хотелось больше всего в данный момент – так это почувствовать жар и дрожь по своему телу от ласковых прикосновений, горячего дыхания обжигающего кожу, умелых поцелуев и… {w}и…"
    $ renpy.pause(2)
    hide imnSHOck with dissolve
    show imn at left with dissolve
    "Успокоившись спустя некоторое время и даже разок икнув, Мана наконец-то вновь сумела взять себя в руки и аккуратно с нежностью накрыла пледом спящую подругу."
    hide imn with dissolve
    stop music fadeout 4
    scene blink with dissolve
    "Скользнув взглядом по телу ещё раз, Мана обошла кровать и аккуратно, стараясь не потревожить спящую соседку, улеглась на кровать и медленно прикрыла глаза."
    $ renpy.pause(2)
    play sound skrip
    "Усталость взяла своё и вскоре девушка спокойно засопела. {w}В полусонном состоянии она даже не обратила внимания на легкий скрип с другой стороны кровати."
    play music water fadein 2
    "Во сне она плавала в реке, а её тело омывали тугие струи воды, ласково огибая её тело и расслабляя не хуже любого массажа.{w} Мана полностью расслабилась, отдалась течению и лишь глубже погружалась в эти ощущения..."
    scene heat with Dissolve(5.0)
    "Несмотря на казавшуюся прохладу реки, в её теле медленно пробуждался жар, создавая сводящий с ума контраст."
    stop music fadeout 1
    "Внезапно она почувствовала лёгкий укус в районе шеи."
    "Легкое замешательство сменилось испугом, когда она почувствовала укус на плече и чью-то хватку на нежной груди." with vpunch
    "На тело внезапно навалилась тяжесть, а дыхание перехватило…"
    $ renpy.pause(3)
    "Дернувшись всем телом, Мана попробовала вскочить и открыть глаза, но удалось ей только второе." with vpunch
    scene mnRoomNight with dissolve
    show ipndark at center with dissolve:
        zoom 2.0
    "Она увидела Планю, что с комфортом оседлала спящую подругу и её неожиданно равнодушное лицо нависло прямо над лицом Маны, холодно её разглядывая."
    "Её взгляд с легким оттенком надменности изучающе рассматривал девушку, ничуть не рассеивая её замешательство."
    "Ночную тишину комнаты, разбавляемую лишь шумным дыханием девушек, прервал тихий голос:"
    dpn "Я хочу узнать о тебе больше… {w}Мана..."
    #End
    scene blink with dissolve
    stop music fadeout 3
    $ renpy.pause(3)
    gs "Спасибо за прохождение нашей с Sho демо-версии предстоящей новеллы!"
    gs "Авторы: \n{w}Текст: Sho, laborant killer{w}\nКод: гусиный посол, Ghostly Angel"
    speedrun "Если это читает Планя или Мана, то авторы пожелали сохранить анонимность =Р"
    gs "Музыка и некоторые фоны {s}спизж{/s} взяты из Бесконечного Лета"
    gs "Это был всего лишь пролог, дальше - больше!"
    gs "Также я хочу выразить огромную благодарность людям, участвующим в проекте, за то, что они смогли найти время для создания этой игры."
    gs "Ждать осталось недолго!"
    return
