

label d2a1:
    $ renpy.block_rollback()
    call save_file_name_update (2, "d2a1")
    $ show_side_player = True
    $ fadein_sideimage = True
    scene bg black with dissolveslow
    I "....."
    X "{size=-15}...mm...{/size}"
    $ renpy.music.set_volume(0.1, 0, channel="loop_sfx")
    $ renpy.music.set_pan(0.75, 0, channel='loop_sfx')
    play loop_sfx sfx_showerloop fadein 2.0
    X "[u_music_note]~ ...Hmm~ [u_music_note]" with hpunch
    I "....... ...Nrgh..." with shakeonce
    I "I hear...singing?"
    $ renpy.music.set_volume(0.3, 2, channel="loop_sfx")
    $ renpy.music.set_pan(0.65, 2, channel='loop_sfx')
    scene bg masterbedroom:
        blur 20.0
        linear 10.0 blur 0.0
    with dissolveslow
    X "Hmmmmmmm~ [u_music_note]" with hpunch
    X "[u_music_note] Hmhmmm~ [u_music_note] Heehee~ [u_music_note][u_music_note]" with hpunch
    Y wince "Nrgh....."
    $ fadein_sideimage = False
    Y thinking "...?"
    $ fadein_sideimage = True
    I "Someone's...in the shower...?"
    window auto hide
    pause 1.0
    play sound ["<silence 0.5>", sfx_showeroff]
    pause 1.0
    stop loop_sfx fadeout 1.0
    scene bg white with dissolvemed
    pause 1.5
    play sound sfx_dooropen
    pause 1.0
    scene cg shower2:
        xalign 0.3 yalign 1.0 zoom 1.5
        easein 20.0 xalign 0.7
    with dissolvemed
    play music bgm_relaxed
    $ show_music_info_timer = music_info_pop_out_time()
    pause 1.0
    $ show_side_cecilia = True
    C towel sad "Haaaaanghh... Not having my hair dryer is the worst..."
    $ fadein_sideimage = False
    C "How am I gonna dry all this floof with just a couple of towels..."
    Y surprised "....."
    $ fadein_sideimage = True
    scene cg shower2:
        xalign 0.5 yalign 1.0 zoom 1.4
        easein 5.0 zoom 1.0
    with dissolvequick
    pause 1.0
    C towel surprised "Oh! [name_player], you're awake!{nw}"
    $ fadein_sideimage = False
    $ d2a1_shower_reaction = ""

    menu:
        extend ""
        "Be flustered":
            $ d2a1_shower_reaction = "A"
            Y panicked "Wha-- Cece?! Wh-what are you doing?!" with shakeshort
            C towel surprised "Huh? I mean, I took a shower, and my clothes are out here..."
            $ fadein_sideimage = True
            scene cg shower with dissolvequick
            C towel smile "...Wait, are you getting worked up from seeing me in a towel?"
            $ fadein_sideimage = False
            Y sad "N-no, I... Uh, tha-that is to say..." with shakeonce
            play ctc_sfx sfx_emotehappy
            C towel happy "Oh. Em. GEE! Your face is priceless right now! [u_heart]" with hpunch
            $ fadein_sideimage = True
            scene cg shower:
                xalign 0.2 yalign 0.0 zoom 1.1
                easein 10.0 zoom 1.5
            with dissolve
            C towel smile "If you want, I could give you a closer look...?"
            $ fadein_sideimage = False
            Y panicked "I-I'll pass, thanks! Wh-where's Ria? Downstairs? I'll go check on her!" with shakeonce
            play ctc_sfx sfx_whooshlow
            show bg black with custom_flashquick()
            C towel surprised "Ah! [name_player], wait!" with shakeshort
            C "[t_clue]Holding it in isn't good for you[t_cluee], you know!"
            play ctc_sfx sfx_emoteshout
            Y scream "JUST GET DRESSED ALREADY!" with shakelong
            $ fadein_sideimage = True
            play ctc_sfx sfx_running
            play sound ["<silence 0.3>", sfx_dooropenloud]
        "Be unfazed":
            $ d2a1_shower_reaction = "B"
            Y default "...Yeah, your humming woke me up."
            C "Oh... You heard that...?"
            $ fadein_sideimage = True
            scene cg shower with dissolvequick
            C towel smile "Hee hee, better than an annoying alarm clock, right?"
            $ fadein_sideimage = False
            Y "I guess, yeah..."
            C "....."
            Y "......."
            C "........."
            show cg shower2
            C towel surprised "Wait, is that all you have to say?" with hpunch
            Y thinking "...What do you mean? I just woke up."
            C "Wha-- I mean, you have a beautiful young lady almost NUDE and dripping WET before your bare eyes!" with shakeonce
            C towel pout "This is like, the quintessential fanservice scene! Possibly the [t_clue]only one[t_cluee] you'll get!" with shakeonce
            Y worried "...I have no idea what you're talking about..."
            play ctc_sfx sfx_emotesigh
            C towel sad "Mrgh... Okay, I guess you're allowed to not be into girls..." with hpunch
            $ fadein_sideimage = True
            scene cg shower2:
                xalign 0.5 yalign 1.0 zoom 1.4
                easein 5.0 zoom 1.6
            with dissolvequick
            C towel pout "...Wait, unless the problem is my assets? If it were Ria coming out of the shower, would you have a better reaction?"
            $ fadein_sideimage = False
            Y surprised "Oh yeah, where's Ria? If she's already awake, I better go check on her."
            $ fadein_sideimage = True
            play ctc_sfx sfx_steps
            scene bg black with dissolvemed
            play sound sfx_dooropen
            C towel pout "AHA, SO IT'S TRUE! Only someone with Ria's curvatures will do it for you, huh, [name_player]?!" with shakeshort
            $ fadein_sideimage = False
            Y worried "Can you stop your hijinks and get dressed already? We're still trapped in a killing game, you know."
            play ctc_sfx sfx_emoteshout
            C "[t_clue]\"Flat is justice\"[t_cluee], [name_player]! Remember that!" with shakeshort
            $ fadein_sideimage = True
            play ctc_sfx sfx_steps
        "Be angry" if seen_ending_despair or seen_ending_judgement:
            $ d2a1_shower_reaction = "C"
            stop music fadeout 3.0
            Y shouting "Cece! Just WHAT do you think you're doing?!" with shakeshort
            C towel surprised "Huh? I mean, I took a shower, and my clothes are out here..."
            $ fadein_sideimage = True
            scene cg shower with dissolvequick
            C towel smile "...Wait, are you getting worked up from seeing me in a tow--"
            play ctc_sfx sfx_emoteshout
            play music bgm_comedy
            $ show_music_info_timer = music_info_pop_out_time()
            $ fadein_sideimage = False
            show cg shower2
            Y shouting "As a young lady, how could you be strutting around half-naked like that?!" with shakeshort
            Y "Don't you have any shame?!" with shakeshort
            C towel surprised "Wh-what? Are... A-are you mad?" with shakeonce
            play ctc_sfx sfx_whoosh
            $ fadein_sideimage = True
            window auto hide
            play sound sfx_fallsoft
            scene bg black with shakeshort
            window auto show None
            C towel pout "MMPH! Ah! H-hey, don't throw my clothes around!" with shakeshort
            $ fadein_sideimage = False
            Y angry "Pick those up, get back in the bathroom, and get dressed!" with shakeshort
            Y leering "Meet us downstairs in 2 minutes, understood?!"
            C towel surprised "YES, MOMMY! Er, [name_player]!" with shakeshort
            C "...I did not foresee this sequence of events...{w=1.0} {size=-10}But it felt kinda nice...{/size} [u_heart]"
            play ctc_sfx sfx_steps
    $ persistent.unlock_cg_shower = True
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    $ renpy.music.set_volume(1.0, 2, channel="loop_sfx")
    $ renpy.music.set_pan(0.0, 2, channel='loop_sfx')
    stop music fadeout 2
    scene bg black with dissolveslow
    scene bg foyer with dissolvemed
    pause 2.0
    I "....."
    I "...There she is."
    scene bg foyer
    $ _last_say_who = "O"
    show oriana thinking at mycenter with dissolvemed
    pause 0.5
    play music bgm_awakening
    $ show_music_info_timer = music_info_pop_out_time()
    pause 0.5
    O "....."
    Y "Good morning, Ria."
    $ fadein_sideimage = False
    Y surprised "Er... It IS morning, right...?"
    $ fadein_sideimage = True
    I "The clock says 6:35... But is it A.M. or P.M.?"
    O stunned "...Oh. ...[name_player].{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend thinking " Sorry, I was lost in thought."
    O blink "You're correct, it's been about 8 hours since you went to sleep. Are you feeling better now?"
    Y default "I think so. My head isn't aching anymore."
    O default "Good. We won't have the luxury of sleeping another night, so you'll have to make today count."
    play ctc_sfx sfx_heartbeat_single
    O irritated "If we don't find a way out in the next few hours, it'll be {color=#ff0000}the end for all of us{/color}." with hpunch
    Y sad "....."
    scene bg frontdoor with fade
    pause 1.5
    scene bg frontdoor:
        xalign 0.5 yalign 1.0 zoom 1.2
        easein 6.0 zoom 1.3 yalign 0.1
    with dissolve
    I "...It still says 20 hours..."
    I "Subtracting the couple hours I spent explaining things to Ria and Cece, then the 8 hours I was asleep..."
    play ctc_sfx sfx_emotequestion
    I "...Yeah, it's possible the time limit is [t_clue]before the next time the clock chimes[t_cluee]."
    I "After all, it's 20 hours, but starting from when? When this message appeared? Or when the first of us woke up...?"
    I "Ugh, we really need more information..." with hpunch
    scene bg black with dissolvemed
    $ _last_say_who = "O"
    scene bg foyer
    show oriana thinking at mycenter
    with dissolvemed
    O "....."
    Y thinking "...You keep staring at that door over there. Did you notice something?"
    $ fadein_sideimage = False
    Y surprised "Wait... Did you find the [t_clue]key[t_cluee] for it?"
    $ fadein_sideimage = True
    O "No, but... A thought came to my mind when I remembered how we met [name_dog]."
    O default "How does he move around the house while the doors are closed?"
    Y thinking "Huh... I never thought about that."
    O blink "Considering the pet bowl in the kitchen, we can assume [name_dog] used to live here with the family."
    O sideeye "So following that train of thought... Right here, take a look."
    scene bg foyer:
        zoom 1.3 xalign 0.25 yalign 1.0
        easein 5.0 zoom 1.6
    with dissolve
    pause 1.0
    Y default "{cps=6}.....{/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend thinking " ...! At the bottom of this door..." with shakeonce
    play ctc_sfx sfx_emotequestion
    Y panicked "There's a secret little flap!"
    $ show_side_oriana = True
    O "A [t_clue]pet door[t_cluee], yes."
    O blink "I think out of the three of us, only Cecilia could fit through a passageway this small."
    Y leering "Makes sense. Now we can finally check out what's behind this door."
    $ show_side_oriana = False
    $ fadein_sideimage = True
    $ _last_say_who = "O"
    scene bg foyer at reset
    show oriana blink at mycenter
    with dissolve
    O "Cecilia said she was going to take a shower. And the only working one is in the master bedroom's bathroom."
    O default "Was she still in the shower when you left your bedroom?"
    if d2a1_shower_reaction is "C":
        Y blink "Yeah, but she still needs to dry her hair and get dressed."
        O thinking "All right, so it should only be a little longer now."
    else:
        Y "No, she had already come out."
        O confused "...Then why didn't she come down with you?"
        Y sad "She, uh... She still needs to get dressed."
        O ".....{w=0.5} ...Wait."
        O leering2 "So she'd come out, but she still hasn't gotten dressed? Doesn't that mean she was..."
        Y panicked "Uh... Ria?"
        play ctc_sfx "<silence 1.0>"
        O annoyed "Tsk..." with shakeonce
        O irritated "[name_player]. Tell me you [t_clue]scolded her[t_cluee] for acting so shamelessly."
        I "...That was an option?"
    $ show_side_cecilia = True
    C happy "[name_player]! Ria!" with vpunch
    $ show_side_cecilia = False
    window auto hide
    show oriana_raw as oriana at myleft, backedaway_on with move
    show cecilia happy at myright with dissolve
    C "Sorry to keep you waiting!"
    if d2a1_shower_reaction is "C":
        show oriana confused at backedaway_off
        O "Hm? Isn't your hair still a little wet?"
        C thinking "Yeah, but I was ordered to come down here in 2 minutes so..."
        C smug "....."
        I "...She's giving me a weird look..."
        O disappointed "...?"
    else:
        play ctc_sfx sfx_punch
        show oriana_raw irritated2 as oriana at mycenter, hop, backedaway_on
        show cecilia sobbing:
            ypos 1.2
            easein 0.2 ypos 1.4
        with custom_flashquick()
        C "ACK!" with shakeshort
        show oriana_raw irritated2 as oriana at mycenter_to_myleft, backedaway_on
        show cecilia pout at myright, doublehop
        C "OYY! Whaddaya whackin' me for, hah?!"
        show oriana angry at myleft, backedaway_off
        O "You know what you did! Don't you have any shame?!" with shakeonce
        show oriana shouting
        Y worried "Ria, we really don't have time for this..."
        O "....."
        O annoyed2 "...Yes, I suppose you're right."
        if d2a1_shower_reaction is "B":
            play ctc_sfx sfx_emotesob
            show cecilia sobbing at shrink
            C "First my heart, and now my head... Why must I suffer so much pain...?" with hpunch
        else:
            C wink "Heh. You're such a sore loser, Ria..."

    show cecilia default at myright
    C "Oh yeah, there's something I forgot to mention to you both! You know that--"
    O sideeyeblink "Cecilia. Do you see this little flap at the bottom of the door here?"
    C surprised "Huh? Oh, well look at that! Anyway, so you know that--"
    O sideeye "Crawl through it."
    C sweatdrop "Hweh? Okay, I know I'm not as curvy as you two, but even MY assets would get stuck trying to--"
    Y thinking "No, from what I saw earlier, I think your body will fit."
    play ctc_sfx sfx_emotesob
    C sobbing "[name_player]! You realize you crushed my heart into a million tiny pieces, right?!" with hpunch
    O confused "Look, set aside what fla-- ...Little pride you have already. Objectively, you have the best shot at getting through."
    C determined "Hey. You were about to say \"flat\", weren't you."
    Y leering "There must be a reason the culprit blocked this room from us. Our only shot at escaping this place alive could be in there."
    C sad "....."
    O disappointed "...You know you're not getting out of this."
    C "Mrgh...{w=0.5}{nw}" with hpunch
    play ctc_sfx "<silence 1.0>"
    extend pout " Ugh, fiiiine, I'll do it."
    show cecilia shouting at hop
    C "But I WILL struggle, okay?! This won't be an easy fit for me!"
    stop music fadeout 3.0
    window auto hide
    hide cecilia with dissolve
    pause 0.5
    scene bg black with dissolvemed
    play sound sfx_clothrustle
    $ show_side_cecilia = True
    C pout "..... Mrgh..." with hpunch
    $ fadein_sideimage = False
    C "Nrgh..." with hpunch
    C happy "Okay, I made it!"
    $ fadein_sideimage = True
    I "She didn't get even remotely stuck..."
    C thinking "Huh, looks like this little cabinet was [t_clue]blocking the door[t_cluee] at its hinges."
    $ fadein_sideimage = False
    Y surprised "There was never any lock?"
    $ show_side_oriana = True
    O confused "It {i}does{/i} make sense... After all, why would a living room door need a lock?"
    $ show_side_oriana = False
    C blink "Okay, little cabinet, let's pull you out of there, and..."
    play ctc_sfx sfx_furnituredrag
    scene bg black
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    pause 2.0
    play sound sfx_dooropen
    pause 1.0
    show cecilia happy at mycenter with dissolve
    play sound sfx_emotehappy
    C "Okay, come on in, guys!"
    play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
    play sound sfx_steps
    scene bg black with fade
    pause 1.0
    scene bg lounge:
        zoom 1.5 xalign 0.6 yalign 0.0
        linear 6.0 xalign 1.0
    with dissolvemed
    pause 2.0
    scene bg lounge:
        zoom 1.5 xalign 0.4 yalign 1.0
        linear 6.0 xalign 0.0
    with dissolvemed
    pause 2.0
    scene bg lounge:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 3.0 zoom 1.0
    with dissolvemed
    show screen notify_location("1 этаж - Гостиная", persistent.unlock_bg_lounge)
    $ persistent.unlock_bg_lounge = True
    pause 2.5
    Y surprised "Looks like you were right, Ria. It's a living room...or maybe more like a [t_clue]lounge[t_cluee]...?"
    I "There's a lot of damage around here... I wonder what could've happened?"
    $ _last_say_who = "O"
    show oriana confused at mycenter with dissolve
    O "....."
    window auto hide
    show oriana thinking at myright with move
    pause 1.0
    show oriana sideeye at myleft with move
    pause 1.0
    show oriana annoyed2 at mycenter with move
    O "There doesn't seem to be any place the culprit could be hiding..."
    Y thinking "I wonder why this room was blocked off from us, then...?"
    O blink "We'd better take a good look around."
    play ctc_sfx sfx_whooshlow
    show oriana blink at myleft
    show cecilia pout at mycenter_closeup:
        zoom 1.1
        easein 0.3 zoom 1.0
    with custom_flashquick()
    C "HEY! Can I get a \"thank you\" for crawling through that little flap?!{w=0.5}{nw}" with shakeonce
    show cecilia pout at mycenter_closeup:
        zoom 1.1
        easein 0.3 zoom 1.0
    play ctc_sfx sfx_emoteshout
    extend " My hair's all dirty again!" with shakeshort
    show cecilia pout at myright
    Y surprised "R-right. Thanks, Cece. Your tiny frame really came in handy."
    play ctc_sfx sfx_emotesob
    show cecilia sobbing at shrink
    C "You could've stopped at \"Thanks, Cece\"..."
    play sound sfx_emoteshout2
    show cecilia pout at doublehop
    C "ANYWAY! Can you two finally listen to what I have to say now?!" with shakeshort
    O disappointed "Hmm? Were you trying to say something?"
    play sound sfx_emoteangry
    show cecilia angry at mycenter_zoom
    hide oriana
    with custom_flashquick()
    C "YOU JERKS KEEP CUTTING ME OFF!!" with shakelong
    show cecilia pout at mycenter_return
    Y confused "Okay okay, what did you want to say?" with hpunch
    play music bgm_discussion
    $ show_music_info_timer = music_info_pop_out_time()
    C default "You remember that [t_clue]key[t_cluee] you said Ria would always find in the master bedroom?"
    Y surprised "Yeah, the one that doesn't open any new doors for us."
    C smug "Ohohoho~ That's where you're wrong, my dear sweet [name_player]~"
    C blink "Y'see, just a couple hours ago, I was watching you sleep for a while when something interesting caught my eye."
    play sound sfx_flashback
    scene bg masterbedroom at grayscale_on with custom_flashbulblong()
    $ show_side_cecilia = True
    C smile "On the frame of the bed, next to the wardrobe...was the tiniest little [t_clue]keyhole[t_cluee]."
    scene bg masterbedroom at grayscale_on:
        xalign 0.6 yalign 0.8 zoom 1.5
    with dissolvemed
    C thinking "So I figured that since Ria said she found the key inside the wardrobe, I gave it a shot and..."
    $ fadein_sideimage = False
    play ctc_sfx [sfx_unlock, sfx_emotehappy]
    C happy "Presto! Inside the bed frame was a [t_clue]secret compartment[t_cluee]! Neat, right?" with vpunch
    Y worried "...Did you just say you were watching me sleep?"
    C blink "It was a pretty large compartment, but all that was in there were some trinkets and a [t_clue]long pole[t_cluee]."
    play ctc_sfx sfx_emotesigh
    $ fadein_sideimage = True
    I "She ignored me..." with hpunch
    C thinking "The pole had a hook on it, so I thought \"Hmm, I wonder what this could be used for...?\""
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O confused "A long pole... A hook..."
    O surprised "...Wait. Was it for...?" with shakeonce
    C smug "I expected nothing less from our Ria! Yep, you guessed it!"
    $ fadein_sideimage = True
    scene bg hallway at grayscale_on
    show cecilia_raw thinking at mycenter, grayscale_on
    with dissolvemed
    C blink "I carried the pole to the dead end at the second floor's hallway, and took a look up at the ceiling."
    scene bg hallwayend at grayscale_on with dissolvemed
    C default "It's a little hard to see in the dark, but there's a tiny hoop stuck up there."
    scene bg hallwayend at grayscale_on:
        xalign 0.5 yalign 0.0 zoom 1.5
        easein 3.0 zoom 2.0
    with dissolvemed
    C smile "You can guess the rest. I raised the pole, put the hook into that hoop, and with just a yank..."
    scene bg black with dissolvemed
    pause 1.0
    play sound sfx_atticopen
    pause 0.6
    with shakeshort
    pause 0.4
    scene bg hallwayend withladder at grayscale_on with dissolvemed
    play ctc_sfx sfx_emotequestion
    pause 2.0
    Y surprised "{cps=6}...An...{/cps} An [t_clue]attic[t_cluee]...?"
    $ show_side_oriana = False
    $ show_side_cecilia = False
    scene bg black with dissolvemed
    scene bg lounge
    show oriana blink at myleft_fadein
    show cecilia happy at myright_fadein
    with dissolvemed
    C "Precisely, my precious little [name_player]~ And that's not even the best part!"
    C blink "When I reached the top of the ladder, I poked my head into the hatch."
    C "And what did my eyes bear witness to in the attic?"
    C smile "Only...a plethora of [t_clue]occult materials[t_cluee]!"
    O leering2 "...!" with shakeonce
    I "\"Occult\"... There's that word again..."
    play ctc_sfx sfx_emotehappy
    show cecilia overjoyed at hop
    C "Weeeell? What do you think? Suspicious, right? Intriguing, riiiight?"
    O confused "....."
    O sideeyeblink "...Maybe for you. But investigating this lounge should be our number one priority right now."
    C surprised "Wha--{w=0.5}{nw}"
    play ctc_sfx sfx_emotesob
    show cecilia sobbing at shrink
    extend " WHAAAAT?! You guys don't want to check it out?! [name_player]?!" with vpunch
    Y thinking "I don't know... How important can a bunch of occult stuff be?"
    show cecilia pout at hop
    C "But you guys were saying it before! If a room was blocked off from us..." with hpunch
    play ctc_sfx sfx_emotequestion
    C "There must be a [t_clue]reason[t_cluee] why the culprit doesn't want us in there!"
    Y surprised "...That's a good point."
    $ fadein_sideimage = False
    Y thinking "Ria, you have to admit that the attic sounds just as suspicious as this lounge now, if not more."
    $ fadein_sideimage = True
    O thinking "....."
    C grin "Oh! That's right, Ria, you're not too good with the spooky stuff, aren't you?"
    O annoyed2 "It doesn't scare me, if that's what you're implying. I just find it annoying how people buy into such illogical nonsense."
    I "...I still don't understand why Ria joined the Occult Club..."
    O irritated "We have no time to waste on chasing fairy tales. We're better off staying here and learning more about the culprit."
    C blink "Okay, okay, you can go ahead and investigate your boring little lounge. {i}I{/i}, however, cannot resist the allure of the occult."
    show cecilia happy at hop
    C "[name_player], come with me!"
    Y surprised "Huh? Me?"
    C blush "Yeah, it'll be fun!"
    C smile "Just you...and me...alone...in a dark little attic..."
    O thinking "....."
    Y thinking "Hrm..."
    I "...I guess there's nowhere else worth checking besides the [t_clue]attic[t_cluee] or the [t_clue]lounge[t_cluee]..."
    I "And if these two are going to split up, I have to make a choice to go with one of them..."

label d2a1_start_investigation:
    Y default "Okay, I'll..."
    menu:
        "Go with Cece to the [t_clue]Attic[t_cluee]":
            if not seen_ending_despair:
                Y "...I'll go to the attic with Cece."
                play ctc_sfx sfx_emotehappy
                show cecilia happy at hop
                C "YAYYY~ [u_heart] We're gonna have so much fun up there, [name_player]!"
                Y sad "Ria, will you be okay on your own?"
                O surprised "I--{w=1.0}{nw}"
                play ctc_sfx "<silence 1.0>"
                extend irritated " *ahem* ...Don't underestimate me. I've already looked around this house on my own a couple times before." with hpunch
                C grin "Yeah, but this is a new room. And the crazy culprit could be aaaaanywheeeere~"
                Y worried "C-come on, Cece, don't do that..."
                show oriana
                $ _last_say_who = "O"
                window auto hide
                hide cecilia
                show oriana at mycenter
                with dissolve
                O "....."
                Y surprised "...Ria?"
                O thinking "..... [name_player]."
                O leering2 "...I don't imagine an attic being very big."
                Y thinking "Y-yeah, probably not..."
                O embarrassed "....."
                O irritated "So... Um..." with shakeonce
                O thinking "{cps=6}.....{/cps} ...Don't waste any time coming back, okay?"
                play ctc_sfx sfx_heartbeat_single
                Y surprised "...!" with shakeshort
                $ fadein_sideimage = False
                Y happy "Y-yeah, of course!" with vpunch
                $ fadein_sideimage = True
                O "....."
                I "Ria's hands are shaking..."
                I "...Maybe I should--"
                play ctc_sfx sfx_whooshlow
                show bg black
                hide oriana
                with custom_flashquick()
                Y panicked "WHOA!" with shakeshort
                $ fadein_sideimage = False
                $ show_side_cecilia = True
                play ctc_sfx sfx_emotehappy
                C overjoyed "Come on, [name_player], the attic awaits us!" with vpunch
                $ show_side_cecilia = False
                $ fadein_sideimage = True
                play ctc_sfx [ "<silence 0.2>", sfx_running ]
                play sound sfx_runninglong
                window auto hide
                pause 1.0
                play ctc_sfx [ sfx_doorcloseloud, sfx_running ]
                show bg black with shakeshort
                pause 1.0
                jump d2a1_attic
            else:
                Y thinking "...I'll go to the... Um..."
                play ctc_sfx sfx_heartbeat_single
                window auto hide None
                $ renpy.music.set_volume(0.0, 0.0, channel="music")
                show bg black with shakeshort
                pause 1.0
                $ renpy.music.set_volume(1.0, 2.0, channel="music")
                I "...Huh?"
                I "...Something feels off. Somewhere in the back of my mind, I have a feeling that..."
                play ctc_sfx "<silence 1.0>"
                I "...if I go to the attic with Cece, [t_clue]something will happen to Ria[t_cluee]..."
                O sideeye "...?"
                I "...I guess there's only one choice, then."
                show bg lounge with dissolve
                jump d2a1_start_investigation
        "Stay with Ria in the [t_clue]Lounge[t_cluee]":

            if not seen_ending_judgement:
                Y blink "...Sorry, Cece. I think I'll stay here and help Ria."
                O blink "....."
                O default "...Thank you, [name_player]. I appreciate it."
                if d2a1_shower_reaction is "A":
                    C surprised "Wait, really?! Earlier, you were blushing so hard, I thought for sure I had you captivated!"
                    C thinking "...Oh, you must be the type to get bored of a girl real quick and move on to your next conquest, is that it?"
                    Y worried "What in the world are you talking abo--"
                    $ _last_say_who = "C"
                    play ctc_sfx sfx_whooshlow
                    show oriana_raw stunned as oriana at backedaway_on
                    show cecilia pout at mycenter_closeup
                    with hpunch
                    C "Well, you can't have Ria! She's mine, okay?!"
                    I "I'm not-- ...Ugh, I can't keep up with these antics, never mind." with hpunch
                    show cecilia pout at mycenter
                    show oriana_raw irritated2 as oriana
                    show cecilia_raw pout as cecilia at myright, backedaway_on with ease
                    show oriana irritated2 at backedaway_off
                else:
                    play ctc_sfx sfx_emotesob
                    show cecilia sobbing at shrink
                    C "Aww... [name_player] rejected me yet again..."
                    show cecilia pout at myright
                    C "Guess there really is no competing with Ria's goods, huh...?"
                    Y worried "That's not the reason why I'm staying here."
                O irritated2 "Cecilia. Stop wasting time and go find some clues in the attic."
                O sideeye "...I may not believe in supernatural phenomena, but... If anyone can find something relevant, it'd be you."
                show cecilia surprised at backedaway_off
                C "....."
                C "...Ria... Are you... Are you saying you have [t_clue]faith[t_cluee] in me?"
                O sideeyeblink "...If it'll motivate you to believe that, then sure."
                play ctc_sfx sfx_emotehappy
                show oriana sideeyeblink at myleft
                show cecilia happy at mycenter, shudder
                with custom_flashquick()
                C "RIA, I LOVE YOUUUUUU~ [u_heart]"
                hide cecilia
                show oriana irritated at mycenter
                with custom_flashquick()
                play ctc_sfx sfx_whooshlow
                $ show_side_cecilia = True
                C surprised "WAHHH!!{cps=2} {/cps}{nw}"
                $ fadein_sideimage = False
                play sound sfx_fallhard
                extend sobbing "OUCHIES!" with shakeshort
                O shouting "Get going already!" with shakeonce
                $ fadein_sideimage = True
                C smug "Oh, I will! Watch out, [name_player]!"
                $ fadein_sideimage = False
                C happy "I'm gonna find us the [t_clue]most important clue[t_cluee] you'll ever see!"
                $ fadein_sideimage = True
                $ show_side_cecilia = False
                play ctc_sfx sfx_running
                stop music fadeout 3.0
                scene bg black with dissolve
                pause 0.2
                play sound sfx_doorclose_quick
                pause 1.8
                jump d2a1_lounge
            else:
                Y thinking "...I'll go to... Um..."
                play ctc_sfx sfx_heartbeat_single
                window auto hide None
                $ renpy.music.set_volume(0.0, 0.0, channel="music")
                show bg black with shakeshort
                pause 1.0
                $ renpy.music.set_volume(1.0, 2.0, channel="music")
                I "...Huh?"
                I "...Something feels off. Somewhere in the back of my mind, I have a feeling that..."
                play ctc_sfx "<silence 1.0>"
                I "...if I stay here with Ria, [t_clue]something will happen to Cece[t_cluee]..."
                C default "...?"
                I "...I guess there's only one choice, then."
                show bg lounge with dissolve
                jump d2a1_start_investigation


label d2a1_attic:
    call save_file_name_update (2, "d2a1_attic")
    stop music fadeout 2
    scene bg black
    pause 3.0
    play sound sfx_steps fadein 1
    Y worried "Cece... You can stop tugging my arm now..."
    $ fadein_sideimage = False
    $ show_side_cecilia = True
    C smile "Oh psh, don't act like you don't love it~ [u_heart]"
    C happy "And here we are!"
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene bg hallwayend withladder:
        xalign 0.5 yalign 0.0 zoom 1.2
        easein 5.0 zoom 1.0
    with dissolvemed
    $ persistent.unlock_bg_hallwayend_withladder = True
    pause 2.0
    Y surprised "Huh, there really {i}is{/i} an attic here. No wonder this corner felt a little odd."
    $ _last_say_who = "C"
    show bg hallwayend withladder at reset
    show cecilia happy at mycenter
    with dissolve
    C "I'll go up first!"
    C wink "...Ah. Don't stare too hard at my buttcheeks though, okay?"
    play ctc_sfx sfx_emotesigh
    Y worried "You never miss an opportunity to joke, don't you..." with hpunch
    play ctc_sfx "<silence 1.0>"
    $ renpy.music.set_pan(0.0, 0, channel='sound')
    play sound sfx_steps_ladderfast
    $ renpy.music.set_pan(0.75, 2, channel='sound')
    scene bg hallwayend withladder with dissolve
    pause 1.0
    I "Okay, let's try to make this quick..."
    scene bg hallwayend withladder:
        xalign 0.6 yalign 0.6 zoom 1.0
        easein 1.0 zoom 1.5
    pause 1.0
    I "The sooner we can get back to Ria, the better..."
    play ctc_sfx "<silence 1.0>"
    $ renpy.music.set_pan(0.0, 0, channel='sound')
    play sound sfx_steps_ladder
    scene bg black with dissolve
    pause 2.0
    scene bg attic:
        zoom 1.5 xalign 0.6 yalign 0.0
        linear 6.0 xalign 1.0
    with dissolvemed
    pause 2.0
    scene bg attic:
        zoom 1.5 xalign 0.4 yalign 1.0
        linear 6.0 xalign 0.0
    with dissolvemed
    pause 2.0
    scene bg attic:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 3.0 zoom 1.0
    with dissolvemed
    show screen notify_location("Чердак", persistent.unlock_bg_attic)
    $ persistent.unlock_bg_attic = True
    pause 1.5
    $ show_music_info_timer = music_info_pop_out_time()
    play music bgm_chaos
    pause 2.0
    I "Whoa... This is...surreal..."
    stop sound
    $ _last_say_who = "C"
    show cecilia smile at mycenter with dissolve
    C "That's a good face you're making, [name_player]~ Admit it! Occult stuff is pretty cool, right?"
    Y surprised "I mean... It certainly leaves an impression."
    C happy "Yeah! You so totally get it!"
    Y thinking "Still... I wonder if anything here will actually be useful to us..."
    I "It's not like we can magic our way out of this killing game..."
    C blink "Well, you've already made your choice to come up here. Can't hurt to take a look, right? Besides..."
    play ctc_sfx sfx_emotequestion
    C smile "We might learn something about whatever's causing your [t_clue]time traveling[t_cluee] here."
    Y surprised "...! That's true..." with shakeonce
    C happy "C'mon, go and check out whatever looks interesting! I'll be right behind you, ready to provide commentary!"
    play ctc_sfx sfx_emotesigh
    I "Or you could...you know, do your own investigating?" with hpunch

    $ d2a1_attic_clue1 = False
    $ d2a1_attic_clue2 = False
    $ d2a1_attic_clue3 = False
    $ d2a1_attic_clue4 = False
    $ d2a1_attic_clue5 = False
    $ d2a1_attic_clue6 = False
    $ d2a1_attic_clue7 = False
    $ d2a1_attic_clue8 = False
    $ d2a1_attic_clue9 = False
    $ d2a1_attic_clue10 = False
    $ d2a1_attic_clue11 = False
    $ d2a1_attic_clue12 = False
    $ d2a1_attic_clue13 = False
    $ d2a1_attic_clue14 = False
    $ d2a1_attic_clue15 = False

    $ investigation_location = "d2a1_attic"
    $ investigation_complete = False
    $ investigation_perfect = False
    $ investigation_clues_required = 5
    $ investigation_clues_required_found = 0
    $ investigation_clues_optional = 10
    $ investigation_clues_optional_found = 0

    $ music_info = False
    scene bg attic with dissolve
    call screen pac_investigation_start(_("The Attic of Dark Secrets"), _("What weird, supernatural discoveries await you in this eerie attic?\nPerhaps one of the many items here will lead you to the truth..."))
    $ music_info = True

label d2a1_attic_investigation:
    $ renpy.choice_for_skipping()
    scene bg attic with dissolvequick
    if not investigation_complete:
        if investigation_clues_required_found >= investigation_clues_required:
            $ investigation_complete = True
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d2a1_attic_perfect
            else:
                call d2a1_attic_complete
    elif not investigation_perfect:
        if investigation_clues_optional_found >= investigation_clues_optional:
            $ investigation_perfect = True
            call d2a1_attic_perfect
    call screen pac_d2a1_attic with dissolvequick
    if investigation_location != None:
        jump d2a1_attic_investigation
    else:
        jump d2a1_attic_end

label d2a1_attic_end:
    scene bg black
    scene bg attic with dissolvemed
    $ fadein_sideimage = True
    Y thinking "I guess that's about everything we're gonna find here."
    I "Sucks that there was nothing about time travel..."
    $ _last_say_who = 'C'
    show cecilia smile at mycenter with dissolve
    C "So? Any insights come to mind? Please share with the class~"
    Y blink "Well, everything in this attic appears to be related to [t_clue]demons[t_cluee] and [t_clue]the dead[t_cluee]."
    $ fadein_sideimage = False
    Y default "Which leads me to believe that whoever collected all this stuff was trying to [t_clue]accomplish a specific goal[t_cluee] related to those."
    $ fadein_sideimage = True
    C smug "An astute observation, [name_player]! You get an A plus!"
    Y annoyed "...How about you, Miss Occult Club President? Anything come to mind?"
    C surprised "Oh, I pretty much landed on the same conclusion you did."
    C thinking "If the owner of these books was an occult enthusiast like myself, there would be a wider variety of topics."
    C "Magic circles, for example, are often used for blessing objects or summoning demons, and yet, no books on either."
    Y surprised "Huh? I could've sworn I saw one book about summoning demons..."
    scene bg attic:
        xalign 0.5 yalign 0.6 zoom 1.5
    with dissolve
    Y thinking "Somewhere around here..."
    $ fadein_sideimage = False
    $ show_side_cecilia = True
    C thinking "Really? Maybe over--{w=1.0}{nw}"
    stop music fadeout 3.0
    play ctc_sfx sfx_trip
    extend surprised " AHH!" with shakeonce
    play ctc_sfx sfx_trip_furniture
    $ fadein_sideimage = True
    window auto hide
    play sound sfx_bloodsquish
    $ persistent.unlock_bg_attic_nobottle = True
    show bg attic nobottle with shakeshort
    pause 1.0
    Y panicked "What happened?!" with shakeonce
    play ctc_sfx sfx_emotesob
    $ fadein_sideimage = False
    C sobbing "Aww... I knocked over this bottle of [t_clue]red ink[t_cluee], and now this book behind the trunk is ruined..." with hpunch
    if seen_ending_judgement:
        I "...Huh, why does that book look familiar...?"
    else:
        Y sad "Ah... Crap, I missed that one..."
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    $ _last_say_who = "C"
    scene bg attic nobottle
    show cecilia sad at mycenter
    with dissolve
    C "Welp, I guess we just weren't fated to read this book."
    Y thinking "Fate..."
    I "...Actually, come to think of it..."
    Y default "Predicting or changing fate is part of the occult, right?"
    C smug "Oh, psh, totally! Those are the most popular types, especially with dreamy maidens like myself."
    Y "Do you know any rituals we could use to see the future? Even if it's just a little ways ahead?"
    C surprised "You mean like fortune telling? Hmm..."
    C thinking "...Truth be told, those tend to be more for entertainment purposes than for actual life saving..."
    Y leering "But anything helps, right?"
    C sweatdrop "Sorry, [name_player], but even if we wanted to do some fortune telling..."
    C sad "...the ones I know how to do off the top of my head, we don't have the materials for them."
    C "And as you know, none of these books here are related to anything except dead people."
    Y sad "Darn..."
    C smile "But wait, don't forget, [name_player], you're a [t_clue]time traveler[t_cluee], aren't you?"
    show cecilia happy at hop
    C "Coming back to the past with knowledge of the future is, like, the ultimate form of fortune telling!"
    Y wince "I suppose so... I just wish my memories of the future were clearer..."
    I "If I could just get a proper handle on this power of mine, then..."
    window auto hide None
    play ctc_sfx "<silence 1.0>"
    play sound sfx_frontdoor
    show bg attic with shakeshort
    show cecilia surprised at hop
    pause 3.0
    Y panicked "...Wha... Wait, was that the sound of...?" with shakeonce
    C thinking "[name_player], we should go downstairs and check."
    Y leering "Yeah, let's go."
    play ctc_sfx sfx_steps_ladder
    call save_file_name_update (2, "d2a1_despair")
    scene bg black with dissolvemed
    I "...As we made our way down the ladder, and again down the stairs..."
    play ctc_sfx sfx_steps
    I "So too did my spirits go down and down until..."
    window auto hide
    pause 1.0
    $ persistent.unlock_bg_frontdoor_open = True
    scene bg frontdoor open:
        xalign 0.5 yalign 1.0 zoom 1.2
        easein 10.0 zoom 1.0
    with dissolveslow
    pause 2.0
    Y shocked "{cps=6}.........{/cps}"
    $ fadein_sideimage = False
    Y "...The front door..."
    Y "It's...open..."
    Y "...Then...that means..." with shakeonce
    $ fadein_sideimage = True
    scene bg black with dissolveslow
    $ _last_say_who = 'C'
    scene bg foyer
    show cecilia surprised at mycenter
    with dissolveslow
    C surprised "....."
    C thinking "[name_player]... Should we just...leave now?"
    C "We can finally escape..."
    play ctc_sfx sfx_whooshlow
    show bg black
    hide cecilia
    with custom_flashquick()
    $ show_side_cecilia = True
    C surprised "Ah! [name_player]!" with shakeonce
    $ show_side_cecilia = False
    play ctc_sfx sfx_running
    I "I took too long... I wasted too much time talking about nonsense like fortune telling..." with shakeshort
    I "...Please... Not like this..." with shakeshort
    play ctc_sfx sfx_dooropenloud
    Y scream "RIA!!" with shakeshort
    window auto hide
    pause 1.0
    scene bg lounge dark:
        xalign 0.5 yalign 0.5 zoom 1.2 matrixcolor BrightnessMatrix(-1.0)
        parallel:
            easein 5.0 matrixcolor BrightnessMatrix(0.0)
        parallel:
            easein 10.0 zoom 1.0
    with dissolveslow
    $ persistent.unlock_bg_lounge_dark = True
    pause 2.0
    Y shocked "...Ria...?"
    I "...! She's... She's just on the couch..." with shakeonce
    Y surprised "Ah..."
    $ fadein_sideimage = False
    Y happy "Ahaha... Thank goodness..." with hpunch
    Y "Ria, the front door's open. We can escape now."
    $ fadein_sideimage = True
    O "......."
    Y surprised "...Ria?"
    $ fadein_sideimage = False
    Y "Come on, are you sleeping or..."
    show bg lounge dark at wobble, blurring:
        xalign 0.5 yalign 0.6 zoom 1.5
    play ctc_sfx "<silence 1.0>"
    Y afraid "!!!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    scene bg black with custom_flashbulbred()
    scene cg despair:
        parallel:
            zoom 2.0 xalign 0.54 yalign 0.8
            pause 2.0
            easeout 3.5 yalign 0.45
            easein 3.5 yalign 0.1
        parallel:
            xoffset 0 yoffset 0 matrixcolor BrightnessMatrix(0.0)
            choice:
                pause 2.5
            choice:
                pause 3.5
            linear 0.05 xoffset 10 yoffset 10 matrixcolor BrightnessMatrix(-0.25)
            linear 0.05 xoffset -10 yoffset -10 matrixcolor BrightnessMatrix(0.0)
            linear 0.05 xoffset 10 yoffset 0 matrixcolor BrightnessMatrix(-0.5)
            linear 0.05 xoffset 0 yoffset -10 matrixcolor BrightnessMatrix(0.0)
            repeat
    with dissolveslow
    pause 6.0
    scene cg despair:
        zoom 1.2 xalign 0.5 yalign 0.3
        easein 3.0 zoom 1.0
    with dissolvemed
    pause 3.0
    play music bgm_murder_chaos
    $ show_music_info_timer = music_info_pop_out_time()
    pause 2.0
    Y shocked "....."
    $ fadein_sideimage = False
    Y "...Ria...?"
    Y afraid "H-hey... Ria, are you tired? Can't you...see...me..." with shakeonce
    $ fadein_sideimage = True
    window auto hide
    pause 2.0
    Y depressed "{cps=5}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    Y pained2 "{cps=5}.......{/cps}" with shakeonce
    $ show_side_cecilia = True
    C blink "...So it really happened."
    $ _last_say_who = None
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene bg black with dissolvemed
    pause 1.0
    scene bg lounge dark with dissolvemed
    show cecilia blink at mycenter_fadein
    Y shadow "...Cece... Ria's..."
    show cecilia thinking at mycenter
    C "Yeah. I know."
    C "Ria's [t_clue]dead[t_cluee]."
    Y troubled "Agh..." with shakeonce
    $ fadein_sideimage = False
    Y scream "Agggghhhhh.... AAGHH--" with shakeshort
    $ fadein_sideimage = True
    C blink "[name_player]. I want you to stay calm and listen to me."
    Y afraid "Wh-what? \"Stay calm\"...? How could I possibly do that?!" with shakeonce
    $ fadein_sideimage = False
    Y pained "Ria was alive just less than an hour ago!" with shakeonce
    Y pained2 "We left her alone! She died with no one around to save her!" with shakeonce
    $ fadein_sideimage = True
    C blink "Exactly. Think about it."
    C "She should've been alone. So then..."
    play ctc_sfx sfx_emotequestion
    C thinking "[t_clue]Who killed her?[t_cluee]"
    Y shocked "Wh-wha... \"Who\"...?"
    C "You and I were in the attic together the entire time. Neither of us could've done it."
    C default "So...what does that mean?{nw}"

    menu:
        extend ""
        "She killed herself":
            Y troubled "She...killed herself...right? Because all of this was too..."
            C sad "[name_player]. You and I both know she would never do that."
            C thinking "Come on, it's not too complicated. Think about it."
            Y "....."
            $ fadein_sideimage = False
            Y wince "...It was...the culprit." with hpunch
            $ fadein_sideimage = True
        "The culprit killed her":
            Y shadow "...The culprit. They must have killed her."
    C blink "Yes. The culprit must've ambushed her."
    Y troubled "The...culprit..." with shakeonce
    C thinking "The weapon that killed Ria is nowhere to be found."
    C "And there's a faint trail of blood drops leading to the [t_clue]corner[t_cluee] over there, AWAY from the door we entered."
    Y depressed "....."
    C "In other words, [name_player], the culprit probably didn't escape through the foyer."
    C determined "They could still be hiding around here, waiting to kill us too."
    Y "...No..."
    $ fadein_sideimage = False
    Y angry "...No... Not if I kill them first. Where's your knife? Let me--" with shakeonce
    $ fadein_sideimage = True
    C sad "[name_player]. Come to your senses already."
    C determined "We need to run. Go get help. There's no way we can handle a murderer alone."
    play ctc_sfx "<silence 1.0>"
    $ renpy.music.set_volume(0.0, 0.0, channel="music")
    $ renpy.music.set_volume(1.0, 2.0, channel="music")
    Y scream "STOP BEING THE RATIONAL ONE!!" with shakeshort
    C surprised "[name_player]..."
    Y pained "Ria... Ria was your friend, wasn't she...?" with shakeonce
    $ fadein_sideimage = False
    Y "How can you be so cold about her death...?"
    $ fadein_sideimage = True
    C "....."
    C blink "......."
    Y shocked "Unless... You... Did you..."
    play ctc_sfx "<silence 1.0>"
    play loop_sfx sfx_heartbeat
    show bg black
    show cecilia blink at blurring, wobble
    with custom_flashquick()
    $ fadein_sideimage = False
    Y pained2 "Ngh! ...My head..." with shakeonce
    $ fadein_sideimage = True
    KI "[t_ghost]...can't...[t_ghoste]"
    I "This voice again...?" with shakeonce
    C surprised "[name_player]? Are you okay?"
    Y pained "I'm... It's happening again..." with shakeonce
    C thinking "What's...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend surprised " Oh! Your [t_clue]time travel power[t_cluee]?!"
    KI "[t_ghost]...like this... Can't...[t_ghoste]" with shakeonce
    Y shadow "It's...for the best..."
    $ fadein_sideimage = False
    Y depressed "...Ria... We can't leave...Ria..."
    $ fadein_sideimage = True
    KI "[t_ghost]...I can't let Ria...die like this... It...[t_ghoste]" with shakeonce
    C determined "[name_player], quick! Before you go, just try your hardest to remember this sentence!"
    Y "Wha... Remember a..."
    play ctc_sfx sfx_emotequestion
    C default "[t_clue]Serena killed the clownfish.[t_cluee]"
    Y "What are you..."
    C smile "Just remember it, okay?! I--{w=0.2}{nw}"
    play ctc_sfx "<silence 1.0>"
    stop loop_sfx
    $ renpy.music.set_volume(0.0, 0, channel="music")
    hide cecilia with custom_flashquick()
    KI "[t_ghost]{size=+5}IT CAN'T END LIKE THIIIIIIIS!!{/size}[t_ghoste]" with shakelong
    play ctc_sfx "<silence 1.0>"
    play sound sfx_wail
    window auto hide dissolveslow
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#ff0000}ПЛОХАЯ КОНЦОВКА{/color}{/size}\nКонцвка отчаяния{/font}" with dissolve
    pause 2.0
    $ _skipping = True
    pause 3.0
    hide text with dissolveslow
    $ seen_ending_despair = True
    $ persistent.unlock_cg_despair = True
    $ shard_string = "Despair"
    $ renpy.music.set_volume(1.0, 0, channel="music")
    stop music
    jump gameover_day2

label d2a1_lounge:
    call save_file_name_update (2, "d2a1_lounge")
    $ _last_say_who = "O"
    scene bg lounge
    show oriana irritated2 at mycenter
    with dissolvemed
    O "...She really needs a volume knob..."
    Y confused "Ahaha... Does she always get this excited over the occult?"
    O leering "Yes. Her enthusiasm for all things creepy and otherworldly is unrivaled."
    O sideeyeblink "Honestly, no matter how much you love something, you should at least try to act mature about it."
    Y surprised "Oh. It's [name_dog]."
    play music bgm_comedy
    show oriana panicked at doublehop
    play sound sfx_emoteshout
    O panicked "WHAT?! WHERE?! AHH!!" with shakeshort
    scene bg lounge:
        xalign 1.0 yalign 1.0 zoom 1.5
    show dog_raw at mycenter
    with wipeleft
    pause 0.5
    $ show_side_oriana = True
    window auto show
    play sound sfx_emotehappy
    O overjoyed "THERE YOU AAAARE!! I've been looking EVERYWHERE for you, little [name_dog]!" with hpunch
    $ fadein_sideimage = False
    O "Don't just disappear on me like that! I was super duper worried!" with hpunch
    $ fadein_sideimage = True
    I "{cps=6}.....{/cps} ...I don't think it's wrong to be enthusiastic about things you love."
    scene bg lounge:
        xalign 1.0 yalign 1.0 zoom 1.5
    show dog_raw at mycenter, shudder
    pause 1.5
    play sound sfx_dogsteps
    hide dog_raw with dissolve
    O panicked "Ah! Wait! [name_dog], come baaaaack!" with shakeonce
    stop music fadeout 3.0
    scene bg lounge
    show oriana panicked at mycenter
    with wipeleft
    $ show_side_oriana = False
    O "....."
    Y thinking "As fast as ever..."
    play ctc_sfx sfx_emotesob
    show oriana sobbing2 at crouch
    O "[name_player]... [name_dog] left me again..." with hpunch
    Y confused "There, there... I'm sure he'll be back soon."
    $ fadein_sideimage = False
    Y relaxed "In the meantime, let's take a good look around this room like we planned. M'kay?"
    $ fadein_sideimage = True
    show oriana sobbing at standup
    O "...M'kay. You take the lead..."
    Y default "{cps=6}.....{/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend happy " Pft..." with vpunch
    $ fadein_sideimage = True
    I "...Ria's quite a character, isn't she."

    $ d2a1_lounge_clue1 = False
    $ d2a1_lounge_clue2 = False
    $ d2a1_lounge_clue3 = False
    $ d2a1_lounge_clue4 = False
    $ d2a1_lounge_clue5 = False
    $ d2a1_lounge_clue6 = False
    $ d2a1_lounge_clue7 = False
    $ d2a1_lounge_clue8 = False
    $ d2a1_lounge_clue9 = False
    $ d2a1_lounge_clue10 = False
    $ d2a1_lounge_clue11 = False
    $ d2a1_lounge_clue12 = False
    $ d2a1_lounge_clue13 = False
    $ d2a1_lounge_clue14 = False

    $ investigation_location = "d2a1_lounge"
    $ investigation_complete = False
    $ investigation_perfect = False
    $ investigation_clues_required = 5
    $ investigation_clues_required_found = 0
    $ investigation_clues_optional = 9
    $ investigation_clues_optional_found = 0

    $ music_info = False
    scene bg lounge with dissolve
    play sound sfx_pac_intro
    call screen pac_investigation_start(_("The Lounge, Unsealed"), _("You finally opened the final room in the first floor. Who is the culprit?\nWhy was this room sealed? The answers to these questions beckon you..."))
    $ music_info = True
    stop sound
    play music bgm_order
    $ show_music_info_timer = music_info_pop_out_time()

label d2a1_lounge_investigation:
    $ renpy.choice_for_skipping()
    scene bg lounge with dissolvequick
    if not investigation_complete:
        if investigation_clues_required_found >= investigation_clues_required:
            $ investigation_complete = True
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d2a1_lounge_perfect
            else:
                call d2a1_lounge_complete
    elif not investigation_perfect:
        if investigation_clues_optional_found >= investigation_clues_optional:
            $ investigation_perfect = True
            call d2a1_lounge_perfect
    call screen pac_d2a1_lounge with dissolvequick
    if investigation_location != None:
        jump d2a1_lounge_investigation
    else:
        jump d2a1_lounge_end

label d2a1_lounge_end:
    scene bg black
    scene bg lounge with dissolvemed
    $ fadein_sideimage = True
    Y "Okay, looks like that's everything covered."
    $ _last_say_who = 'O'
    show oriana thinking at mycenter with dissolve
    O "....."
    Y surprised "...Ria?"
    O "{cps=6}.....{/cps} {nw}"
    play ctc_sfx "<silence 1.0>"
    extend sobbing "...Where do you think [name_dog] went off to...?" with hpunch
    play ctc_sfx sfx_emotesigh
    I "She's still hung up on that dog ditching her..." with hpunch
    Y leering "Come on, Ria, focus! What did we learn from looking around here?" with shakeonce
    O "...Mngh..."
    Y "....."
    O "...There was a [t_clue]family[t_cluee] that used to live here. And an unfortunate tragedy tore them apart."
    Y relaxed "Very good! And what else?"
    O "...There's a door leading to the [t_clue]basement[t_cluee]... But we should get Cecilia back with us before we go check it out."
    play ctc_sfx sfx_emotehappy
    Y happy "Exactly! Very well done!" with vpunch
    O irritated "...You can stop treating me like a preschooler anytime now."
    Y worried "Right, sorry." with hpunch
    I "She's back."
    O sideeye "...[name_player]. Do you remember the state of the bedrooms upstairs?"
    Y surprised "Huh? Y-yeah?"
    O blink "We know that one of the bedrooms belonged to a little girl. Probably the young daughter of this family."
    O "The master bedroom only has men's clothes, and finally, the mysterious empty bedroom..."
    Y thinking "Uh huh...?"

label d2a1_lounge_tragedy:
    O default "[name_player]. Think about it. What tragedy happened to the family?{nw}"

    menu:
        extend ""
        "The parents divorced":
            Y thinking "The parents divorced, right? That explains why there are only men's clothes in the master bedroom."
            $ fadein_sideimage = False
            Y default "The mother must've left the house and took the son with her."
            $ fadein_sideimage = True
            O blink "...I suppose that's not the worst guess in the world."
            O thinking "Frankly, I wish the tragedy was as simple and bloodless as that..."
            Y worried "So...no?"
            O default "No. The mother certainly did leave the father, most likely taking the son with her..."
            O sideeyeblink "But there was another event that occurred before that. Something big."
            I "Why can't she just say what it is instead of hyping it up like this...?" with hpunch
            jump d2a1_lounge_tragedy
        "The son died":
            Y default "The son died, right? The empty bedroom must have belonged to him."
            $ fadein_sideimage = False
            Y sad "And then after he died, the family must've cleared his bedroom to move on from the pain of losing him."
            $ fadein_sideimage = True
            O sideeyeblink "...[name_player]. You're so close, yet so, SO very far."
            O sideeye "You recall the mother's letter mentioning that the son is with her, yes?"
            Y worried "Oh."
            O sideeyeblink "Also, if the son really had died, I don't think they would've cleared out his bedroom."
            O thinking "If anything, they would've [t_clue]preserved it[t_cluee], but it was instead scraped bare. Almost maliciously."
            Y thinking "Hmm..."
            O default "You're getting closer, though. It should be obvious now what happened."
            I "Then can't you just tell me the answer...?" with hpunch
            jump d2a1_lounge_tragedy
        "The daughter died":
            Y blink "The daughter died, right?"
    $ fadein_sideimage = False
    Y default "That's probably why the little girl's bedroom was kept neat and tidy."
    $ fadein_sideimage = True
    O blink "...I think so too, but obviously, that alone is insufficient as proof."
    O leering2 "What else did we learn that suggests the daughter died?{nw}"

    menu:
        extend ""
        "The timing of the son and mother's actions":
            Y thinking "This has been bothering me the whole time, but why did the son and mother wait so long before leaving?"
            $ fadein_sideimage = False
            Y leering "If it's true that the father was beating the son, then wouldn't they react sooner? In fact, why didn't they call the authorities?" with shakeonce
            $ fadein_sideimage = True
            O "....."
            O blink "......."
            O thinking "[name_player]. Domestic violence is always a complicated problem. Victims can't really be objective in those situations."
            O default "There could be any number of reasons why they stayed so long, and why they didn't call for help."
            Y sad "....."
            O blink "That's why their actions alone don't necessarily prove the daughter died."
            O "Just to clear your thoughts, let's start from the beginning."
            jump d2a1_lounge_tragedy
        "The daughter isn't mentioned in the letter":
            Y blink "There was something strange I noticed about the letter's contents."
            $ fadein_sideimage = False
            Y thinking "The mother mentions the addressee--most likely the father--was beating his son."
            Y "And the result of that is the son urging for the mother to leave the house..."
            Y leering "But there's [t_clue]no mention of the daughter[t_cluee] at all."
            Y sad "Nothing that suggests the mother took the daughter with her, or that the son rescued his sister himself..."
            $ fadein_sideimage = True
            O irritated "....." with shakeonce
        "\"I don't know...\"":
            Y worried "I, uh.... I dunno." with hpunch
            O disappointed "....."
            Y thinking "Maybe we're a little off with our assumptions here...?"
            O confused "...Fine, let's think this through from the beginning again."
            jump d2a1_lounge_tragedy
    O thinking "...Yes."
    O "Through some unknown means, the daughter must have died first. That has to be the tragedy that tore their family apart."
    stop music fadeout 3.0
    Y shadow2 "....."
    O "....."
    O default "...Well?"
    Y surprised "...Well...what?"
    O "Learning about the daughter's death, and how it affected her loved ones... Do you feel nothing about it?"
    Y sad "Do I feel...? I mean, it's tragic, for sure. My condolences to them."
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotequestion
    Y default "But [t_clue]I don't know these people[t_cluee]. Or at least...I don't think I do."
    $ fadein_sideimage = True
    O "....."
    O thinking "......."
    O blink "...I see. Then we'll leave it at that."
    Y thinking "...?"
    O confused "Back to our present situation..."
    play music bgm_order fadein 3.0
    O "Considering all of our deductions up to now, there's a good chance the father still lives here."
    O leering2 "In other words, the [t_clue]father is the mastermind[t_cluee] behind this killing game."
    Y thinking "Considering the type of man he was, I guess that's plausible..."
    $ fadein_sideimage = False
    Y sad "But... I don't know, there's plenty of proof to suggest that he was a good father before the tragedy happened."
    $ fadein_sideimage = True
    O surprised "....."
    O thinking "{cps=6}.......{/cps} {nw}"
    play ctc_sfx "<silence 1.0>"
    extend irritated "No." with shakeonce
    O annoyed2 "A criminal is a criminal, no matter what his circumstances were."
    O leering2 "No amount of suffering he's been through can justify what he did to his son. ...And what he's done to us."
    Y shadow2 "....." with hpunch
    O thinking "He's probably hiding in the [t_clue]basement[t_cluee]. We should go find Cecilia and get ourselves ready to bring him to justice."
    Y surprised "Oh yeah, Cece's still not back..."
    I "I guess she got really into whatever's in the attic. Wonder if she found any important clues..."
    stop music fadeout 3.0
    call save_file_name_update (2, "d2a1_judgement")
    scene bg black with dissolvemed
    play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
    play sound sfx_steps
    pause 1.0
    I "...Ria's clearly on autopilot, following my back while lost in her own thoughts..."
    I "I wonder what's got her so distracted...?"
    Y surprised "Oh!"
    scene bg hallwayend withladder:
        xalign 0.5 yalign 0.0 zoom 1.2
        easein 5.0 zoom 1.0
    with dissolvemed
    $ persistent.unlock_bg_hallwayend_withladder = True
    pause 2.0
    Y surprised "Huh, what do you know, there really was an attic here. No wonder this corner felt a little odd."
    scene bg hallwayend withladder:
        xalign 0.5 yalign 0.0 zoom 1.5
    with dissolve
    Y default "Hey! Cece! Are you done checking out the attic?"
    $ fadein_sideimage = False
    Y "....."
    Y thinking "......."
    play ctc_sfx sfx_emoteshout
    Y shouting "CECE! COME ON, WE HAVE ANOTHER PLACE TO CHECK OUT! GET DOWN HERE!" with shakelong
    Y leering "....."
    Y worried "......."
    $ fadein_sideimage = True
    $ _last_say_who = "O"
    scene bg hallwayend withladder
    show oriana blink at mycenter
    with dissolve
    O "...She must be completely absorbed in a book or something."
    Y annoyed "Guess there's no choice but to climb up."
    $ fadein_sideimage = False
    Y default "You can wait here, Ria. I'll go pull her down quickly."
    $ fadein_sideimage = True
    O "....."
    O surprised "...Huh?"
    O thinking "O-oh, okay, take your time..."
    Y worried "....."
    I "Everyone's so distracted today..."
    window auto hide
    hide oriana with dissolve
    play ctc_sfx sfx_steps_ladder
    scene bg black with dissolvemed
    pause 2.0
    Y shouting "Okay, Cece, playtime's over!" with shakeshort
    $ fadein_sideimage = False
    Y surprised "Let's...get... ...going...?"
    $ fadein_sideimage = True
    scene bg attic dark:
        xalign 0.4 yalign 0.3 zoom 2.0
        easein 10.0 zoom 1.8
    with dissolveslow
    Y surprised "...Cece?"
    $ fadein_sideimage = False
    scene bg attic dark:
        xalign 0.4 yalign 0.3 zoom 1.8
        easein 3.0 zoom 1.5
    with dissolve
    pause 1.0
    Y thinking "....."
    play ctc_sfx sfx_heartbeat_single
    scene bg attic dark:
        xalign 0.4 yalign 0.3 zoom 1.5
        easein 1.0 zoom 1.0
    with dissolve
    pause 1.0
    Y afraid "...!!" with shakeshort
    $ persistent.unlock_bg_attic_dark = True
    $ fadein_sideimage = True
    scene cg judgement:
        parallel:
            xalign 0.5 yalign 0.5 zoom 1.5
            easein 30.0 zoom 1.0
        parallel:
            matrixcolor BrightnessMatrix(-0.2)
            linear 10.0 matrixcolor BrightnessMatrix(0.0)
    with dissolveslow
    pause 3.0
    play loop_sfx sfx_introambiance_sequence4_loop fadein 3.0
    Y afraid "CECE!!" with shakeshort
    I "Cece's...been slashed...?"
    Y pained "Cece, wake up! Come on, this isn't funny!" with shakeonce
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O hidden "{size=-10}[name_player]! What's going on?!{/size}"
    $ fadein_sideimage = True
    C "....."
    Y scream "Cece, talk to me!" with shakeshort
    stop loop_sfx fadeout 3.0
    C "...I...messed up..."
    play sound sfx_steps_ladderfast
    I "...!! She's still alive!" with shakeonce
    O shouting "*pant* [name_player]! What's with all...the..." with shakeshort
    $ fadein_sideimage = False
    O afraid "...Wait... Wha-what is this...?"
    play music bgm_tension
    Y troubled "It's okay, Cece! You'll be fine! Just... Just focus on breathing!" with shakeonce
    Y "Something to stop the bleeding...! There's gotta be something... Anything!" with shakeonce
    $ fadein_sideimage = True
    C "No...need...[name_player]... I'm...not...bouncing back...from this..."
    Y pained "Stop joking around! This is... This is the one time you shouldn't be joking around!" with shakeshort
    C "I...know... It's...no joke..."
    Y angry "Who did this to you?! Cece! Did you see the culprit?!"
    C "...Sorry..."
    C "...I couldn't...see..."
    C "...It was...dark...and...fast..."
    play ctc_sfx sfx_heartbeat_single
    C "A...[t_clue]demon[t_cluee]..." with shakeonce
    Y shocked "A demon...? Cece, what are you--"
    stop music fadeout 3.0
    play ctc_sfx "<silence 1.0>"
    scene cg judgement:
        matrixcolor BrightnessMatrix(-0.1)
    with dissolve
    C "[t_clue]Behind[t_cluee]...[t_clue]trunk[t_cluee]..."
    play ctc_sfx "<silence 1.0>"
    scene cg judgement:
        matrixcolor BrightnessMatrix(-0.2)
    with dissolve
    C "[t_clue]Page[t_cluee]... [t_clue]Forty[t_cluee]... {size=-10}[t_clue]Fo[t_cluee]...{/size}"
    play ctc_sfx "<silence 1.0>"
    $ show_side_oriana = False
    scene bg black with dissolveslow
    Y shocked "{cps=6}.....{/cps} ...C-Cece...?"
    window auto hide None
    play ctc_sfx "<silence 1.0>"
    play sound sfx_frontdoor
    show bg black with shakeshort
    pause 3.0
    I "...That's...the front door..."
    scene bg attic dark with dissolvemed
    $ _last_say_who = 'O'
    show oriana injured at mycenter with dissolvemed
    O "....."
    Y depressed "......."
    O irritated "...[name_player]. She's gone."
    play ctc_sfx "<silence 1.0>"
    O "Cecilia is...{w=1.0}{cps=9}[t_clue]dead[t_cluee].{/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    play music bgm_decision_order
    $ show_music_info_timer = music_info_pop_out_time()
    extend "" with shakeonce
    play ctc_sfx sfx_heartbeat_single
    Y shadow "....." with shakeonce
    O thinking "She has two deep knife wounds, one on her stomach, one on her neck..."
    O sideeye "Her kitchen knife is on the floor next to her. No blood."
    O leering "This means someone used [t_clue]another knife[t_cluee] to kill her."
    Y "...Not \"someone\". A [t_clue]demon[t_cluee]."
    play sound sfx_dogsteps volume 0.15
    O surprised "...What? Come on, [name_player], she didn't mean a literal demon."
    Y shadow2 "But it's the only thing that makes sense..."
    $ fadein_sideimage = False
    Y "Cece's...practically a demon herself. Only another demon would be able to kill her."
    Y happy "...Heh... Heh heh... It makes perfect sense..." with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    O shouting "[name_player]! Forget about all that! We need to leave! NOW!" with shakeshort
    O leering "Cecilia's death means the front door is open. We could both hear it even all the way from up here!"
    Y troubled "Nrgh..." with shakeonce
    O annoyed2 "We don't know who killed her! Demon or not, they could still be hiding somewhere around here!"
    O shouting "We owe it to her to escape this place alive! Don't let her [t_clue]sacrifice[t_cluee] be in vain!" with shakeshort
    Y depressed "Demon... Sacrifice..."
    play ctc_sfx "<silence 1.0>"
    play loop_sfx sfx_heartbeat
    show bg black
    show oriana shouting at blurring, wobble
    with custom_flashquick()
    $ fadein_sideimage = False
    Y pained2 "Ngh! ...My head..." with shakeonce
    $ fadein_sideimage = True
    KI "[t_ghost]...can't...[t_ghoste]"
    I "This...voice again...?" with shakeonce
    O surprised "[name_player]! What's wrong?!"
    Y troubled "It's...happening...again..."
    O "What's...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " W-wait, you mean your [t_clue]time travel power[t_cluee]?!" with shakeonce
    KI "[t_ghost]...Cece can't...[t_ghoste]"
    O horrified "No! Stop! [name_player]! Don't turn back time!" with shakeonce
    O "Things are okay like this! W-we can escape now! Just the two of us..."
    O "DON'T THROW ALL THIS AWAY!" with shakeshort
    Y shadow "I... I can't... do that..."
    $ fadein_sideimage = False
    Y "...Cece... Cece...doesn't...deserve this..."
    $ fadein_sideimage = True
    I "...!! Wait, [t_clue]behind the trunk[t_cluee]!" with shakeshort
    window auto hide None
    play ctc_sfx sfx_fallsoft
    scene bg attic dark at blurring, wobble:
        xalign 0.5 yalign 0.8 zoom 1.3
    with custom_flashquick()
    window auto show None
    Y pained "NRGHHH!!" with shakeshort
    KI "[t_ghost]...We can't leave things...like this...[t_ghoste]"
    show bg attic dark at blurring, wobble:
        xalign 0.5 yalign 0.7 zoom 1.6
    with shakeshort
    $ show_side_oriana = True
    O horrified "[name_player]! Please! Don't go back!" with shakeonce
    $ fadein_sideimage = False
    O "Don't go back! DON'T GO BAAAACK!!" with shakelong
    $ show_side_oriana = False
    $ fadein_sideimage = True
    show bg attic dark at blurring, wobble:
        xalign 0.5 yalign 0.5 zoom 1.9
    with shakeshort
    I "Nrrrrrrghh... Got it!" with shakeonce
    Y "Page... Forty... Foooo--" with shakeonce
    play ctc_sfx "<silence 1.0>"
    stop loop_sfx
    $ renpy.music.set_volume(0.0, 0, channel="music")
    show bg black with custom_flashquick()
    KI "[t_ghost]{size=+5}GO BAAAAAAAAAAAAAACK!!!{/size}[t_ghoste]" with shakelong
    play ctc_sfx "<silence 1.0>"
    window auto hide dissolvemed
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}Страница 44{/size}\nОткрытие Врат в {color=#ff0000}АД{/color}{/font}" with dissolveslow
    pause 5.0
    $ ctc_timer = 0
    hide text with dissolveslow
    play sound sfx_wail
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#ff0000}ПЛОХАЯ КОНЦОВКА{/color}{/size}\nКонцвка правосудия{/font}" with dissolve
    pause 2.0
    $ _skipping = True
    pause 3.0
    hide text with dissolveslow
    $ seen_ending_judgement = True
    $ persistent.unlock_cg_judgement = True
    $ shard_string = "Judgement"
    $ renpy.music.set_volume(1.0, 0, channel="music")
    stop music
    jump gameover_day2
label d2a2:
    $ renpy.block_rollback()
    call save_file_name_update (2, "d2a2")
    $ fadein_sideimage = True
    scene bg black with dissolveslow
    I "....."
    X "{size=-15}...mm...{/size}"
    I "...Nrgh..."
    $ renpy.music.set_volume(0.1, 0, channel="loop_sfx")
    $ renpy.music.set_pan(0.75, 0, channel='loop_sfx')
    play loop_sfx sfx_showerloop fadein 2.0
    X "[u_music_note]~ ...Hmm~ [u_music_note]"
    Y troubled "Mrgh...! Ah..." with shakeonce
    $ renpy.music.set_volume(0.3, 0, channel="loop_sfx")
    $ renpy.music.set_pan(0.65, 0, channel='loop_sfx')
    show bg masterbedroom with custom_flashquick()
    $ fadein_sideimage = False
    Y scream "NGAAAAAAAAHHHH!!" with shakelong
    $ fadein_sideimage = True
    scene bg masterbedroom
    play sound sfx_showeroff
    stop loop_sfx fadeout 1.0
    pause 0.5
    with shakeonce
    pause 0.2
    with shakeonce
    pause 0.2
    with shakeonce
    play ctc_sfx sfx_dooropenloud
    scene cg shower2:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 1.0 zoom 1.0
    with custom_flashquick()
    $ show_side_cecilia = True
    C towel surprised "[name_player]! What's wrong?! Did you have a nightmare?!" with shakeshort
    $ fadein_sideimage = False
    Y afraid "No... That... That was no nightmare..." with shakeonce
    $ fadein_sideimage = True
    scene bg black with custom_flashquick()
    play ctc_sfx sfx_whooshlow
    show bg black with custom_flashquick()
    C towel surprised "Ah! [name_player], wait!"
    $ fadein_sideimage = False
    Y scream "Get dressed and come down! Hurry!" with shakeshort
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    window auto hide
    play ctc_sfx ["<silence 0.3>", sfx_dooropenloud]
    play sound sfx_running
    pause 0.3
    with shakeshort
    pause 1.5
    scene bg masterbedroom
    show cecilia towel surprised at mycenter
    with dissolvemed
    C "....."
    C "But... My fanservice scene..."
    scene bg black
    with dissolvemed
    $ renpy.music.set_volume(1.0, 2, channel="loop_sfx")
    $ renpy.music.set_pan(0.0, 2, channel='loop_sfx')
    pause 1.0
    play sound sfx_runninglong fadein 1.0
    scene bg foyer with dissolveslow
    Y scream "RIA!!" with shakelong
    stop sound
    $ _last_say_who = "O"
    show oriana panicked at mycenter, hop with shakeonce
    O "Ah! [name_player], you startled me!"
    show bg foyer at wobble, blurring
    play ctc_sfx "<silence 1.0>"
    play loop_sfx sfx_heartbeat
    Y afraid "Ria... I..." with shakeonce
    $ fadein_sideimage = False
    Y shocked "You... I'm..." with shakeonce
    $ fadein_sideimage = True
    O surprised "Huh...? [name_player], take a couple of deep breaths."
    O "It's okay. We're all safe right now."
    I "....."
    I "...Y-yeah..." with hpunch
    stop loop_sfx fadeout 2.0
    show bg foyer at reset:
        blur 0.0
    with dissolve
    I "Yeah... We're... We're all safe...for now..." with hpunch
    $ show_side_cecilia = True
    C surprised "[name_player]! Ria!"
    $ show_side_cecilia = False
    show oriana_raw thinking as oriana at myleft, backedaway_on with move
    show cecilia injured at myright with dissolve
    C "*pant* *pant* I've never gotten dressed so fast... My hair is still soaked..." with hpunch
    C pout "What's the big idea, [name_player]! Why all the screaming?!" with shakeonce
    Y troubled "I... That is, um..."
    show oriana blink at myleft, backedaway_off
    O "...Did you travel back in time again?"
    C surprised "...!" with shakeonce
    Y panicked "Y-yeah! And... Uh..." with shakeonce
    O thinking "...Did one of us die in front of you?"
    play ctc_sfx sfx_heartbeat_single
    Y pained2 "Nrgh..." with shakeshort
    C sad "[name_player]..."
    Y depressed "No matter...what I chose... Either you...{cps=2} {/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend pained2 "...or you..." with shakeonce
    Y pained "It's... It's my fault... It's because I left you alone, and..."
    $ fadein_sideimage = True
    O irritated "...[name_player]."
    O "We don't have time for you to be falling apart like this."
    play ctc_sfx "<silence 1.0>"
    Y shocked "{cps=6}.....{/cps}"
    C sweatdrop "Ria... That's going a bit too far, don't you think...?"
    O "....."
    show bg black with dissolve
    I "....."
    C surprised "See, look what you did! [name_player] is all frozen up now!"
    I "......."
    O thinking "....."
    O sideeyeblink "...Regardless of whatever happened in the future you came from, the fact is that you're here now."
    O sideeye "Both of us are still alive right NOW, and ready to hear the information you have for us, [name_player]."
    Y surprised "...!" with shakeonce
    C surprised "Ooh..."
    play ctc_sfx sfx_emotehappy
    show cecilia happy at hop
    C "Yeah, what {i}she{/i} said! We're counting on you, [name_player]!"
    O irritated2 "So please. Pull yourself together and tell us everything."
    O leering "It could very well [t_clue]save our lives[t_cluee]."
    I "....."
    I "....... I..." with shakeonce
    Y shadow "....."
    $ fadein_sideimage = False
    Y blink "......."
    Y sad "...I'm sorry. Let me start from the beginning."
    $ fadein_sideimage = True
    play music bgm_tension
    scene bg black with dissolveslow
    scene bg foyer
    show oriana irritated at myleft
    show cecilia thinking at myright
    with dissolveslow
    O "I see..."
    O "So whenever one of us chooses to investigate a place alone, we get killed by an [t_clue]unknown assailant[t_cluee]."
    Y sad "....."
    C default "I guess this means the culprit realized we're not playing their killing game anymore?"
    O thinking "Both the attic and the lounge are places the culprit never expected us to access."
    O default "There may have been important information that could expose the culprit in both of those places."
    C smug "Like that book [t_clue]behind the trunk[t_cluee], right? What did you say it said? \"Opening a Gate to {color=#ff0000}HELL{/color}\"...?"
    C smile "What else do you remember about that page, [name_player]?"
    Y thinking "Not much... I just remember the page title, how it was circled in red ink, and a lot of text and images I couldn't understand."
    C thinking "So it was probably a detailed guide to creating a \"Gate to Hell\", whatever that means..."
    play ctc_sfx sfx_heartbeat_single
    I "...Why does that term send a chill down my spine...?" with hpunch
    O sideeyeblink "In any case, our next step is clear."
    O sideeye "The three of us need to stick together and head to the [t_clue]basement[t_cluee]."
    C smile "Time for the {color=#ff0000}final boss{/color}, huh...? Think we stand a chance at winning?"
    O thinking "It's too soon to say for sure. We know that it's most likely the [t_clue]father of the family[t_cluee] that lived in this house."
    O default "Considering what we learned about him from the [t_clue]mother's letter[t_cluee], he's likely unstable and violent."
    play ctc_sfx sfx_knifebrandish
    C blink knife "Oh, psh, that's nothing me and my knife here can't handle!" with hpunch
    O leering "Have you already forgotten that [name_player] watched you die in the attic?"
    C sweatdrop "Geh-- I-I mean..." with hpunch
    C pout "I probably got distracted reading books! There's no way I can be taken down when I'm 100%% focused!" with shakeonce
    Y happy "Heh..."
    play ctc_sfx sfx_emotehappy
    show cecilia happy at hop
    C "Ah! There's that smile!"
    O default "Are you feeling better now, [name_player]?"
    Y relaxed "Yeah. Thanks, you two."
    $ fadein_sideimage = False
    Y thinking "I don't know for sure how things will go down in the basement, but..."
    Y default "If the worst happens, I can always go back in time, right?"
    $ fadein_sideimage = True
    C wink "Yeah, don't you just LOVE deus ex machina? We can't possibly lose!"
    O blink "Let's just hope you won't have to use it too many more times."
    O default "We'll get through this with [t_clue]all our efforts together[t_cluee], [name_player]."
    I "Yeah... Together..."
    O sideeye "Now then. Cecilia. The door."
    C surprised "...Oh. Right, I guess there's no arguing that I won't fit, huh?"
    C sobbing "Agh, my poor, wet hair..."
    $ _last_say_who = None
    scene bg black with dissolveslow
    I "This is it..."
    I "If the culprit is in the basement, everything will come to a climax."
    I "And yet... I can't help but wonder about all the [t_clue]remaining mysteries[t_cluee]..."
    I "....."
    play ctc_sfx sfx_heartbeat_single
    I "No. I'm not here to solve mysteries. I'm here to [t_clue]end the killing game[t_cluee]." with shakeonce
    I "Nothing else matters. We're getting out of here...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend "alive!" with shakeonce
    scene bg black
    stop music fadeout 3.0
    pause 3.0
    play ctc_sfx sfx_steps fadein 1.0
    play sound sfx_steps_heels fadein 1.0
    scene bg lounge with dissolveslow
    pause 1.0
    play sound sfx_dooropen
    scene bg basement entrance:
        xalign 0.5 yalign 0.5 zoom 1.2
        easein 3.0 zoom 1.0
    with dissolvemed
    pause 1.0
    $ show_side_oriana = True
    $ show_side_cecilia = True
    O leering "So this is it... The door to the basement..."
    I "It's so dark... We can't see anything from here..."
    O "Are both of you ready?"
    $ fadein_sideimage = False
    Y leering "Yeah."
    C happy "Come on, let's go!"
    play ctc_sfx sfx_steps
    play sound sfx_steps_heels
    $ show_side_oriana = False
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene bg black with dissolve
    play ctc_sfx sfx_emotequestion
    I "...?" with hpunch
    $ _last_say_who = "D"
    scene bg lounge
    show dog at mycenter
    with dissolvemed
    D "....."
    Y surprised "[name_dog]...?"
    $ _last_say_who = "D"
    window auto hide
    show dog at shudder
    pause 1.0
    play sound sfx_dogsteps
    scene bg lounge with dissolve
    Y surprised "....."
    I "...He ran off..."
    $ show_side_oriana = True
    O thinking "[name_player]? What are you doing?"
    $ show_side_oriana = False
    $ fadein_sideimage = False
    Y thinking "...I-it's nothing. Sorry, I'm coming!"
    $ fadein_sideimage = True
    I "What was that all about...?"
    play ctc_sfx sfx_steps


label d2a2_basement:
    call save_file_name_update (2, "d2a2_basement")
    scene bg black with dissolve
    pause 3.0
    play sound sfx_steps fadein 1
    $ show_side_player = False
    $ show_side_oriana = True
    $ show_side_cecilia = True
    show screen notify_location("-1 этаж - Подвал", persistent.unlock_bg_basement) 
    Y "....."
    $ fadein_sideimage = False
    Y "...Guys, I can't see anything." with hpunch
    O hidden "Yes, I think we're all aware of how dark it is."
    O "There're no windows in an underground room, after all."
    C hidden "Agh, if only we still had our phones! A flashlight would be great right now." with hpunch
    Y "Maybe there's something like that around here..."
    O "Wait... My eyes are getting adjusted to the dark... I think there's tools on the wall."
    C "Ooh! And where there are tools, there's...what exactly?"
    O "If it's anything like my father's basement, there should be various household items stored down here."
    O "The odds are high that there will be something that can illuminate this place, even if only slightly."
    $ fadein_sideimage = True
    I "...Something tells me the culprit's not here..."
    play ctc_sfx sfx_heartbeat_single
    I "If they were, we definitely would've gotten attacked by now..." with shakeonce
    C "Oh! Guys, I think I found something!"
    $ fadein_sideimage = False
    C "A tiny little room... Walls... Touchy touch..."
    C "Wait, I think this is a [t_clue]breaker panel[t_cluee]!" with hpunch
    play ctc_sfx sfx_lightswitch
    $ fadein_sideimage = True
    $ _last_say_who = None
    $ show_side_player = True
    $ show_side_oriana = False
    $ show_side_cecilia = False
    scene bg basement:
        xalign 0.0 yalign 0.6 zoom 1.5
    show oriana irritated at myleft_fadein
    show cecilia happy at myright_fadein
    with custom_flashbulb()
    Y worried "Ergh... A warning would be appreciated for next time..." with hpunch
    O surprised "....."
    C surprised "....."
    Y surprised "...Huh? What's wrong?"
    C "[name_player]. Um. Behind you, there's..."
    scene bg basement:
        xalign 0.0 yalign 0.6 zoom 1.4
        easeout 3.0 xalign 0.3
        easein 3.0 xalign 0.6
    with dissolvemed
    pause 2.0
    Y thinking "Huh?"
    scene bg basement:
        xalign 1.0 yalign 0.7 zoom 1.5
    with dissolve
    $ persistent.unlock_bg_basement = True
    window auto show
    play music bgm_criminal
    $ show_music_info_timer = music_info_pop_out_time()
    Y afraid "UWAAAAAHHHH!!" with shakelong
    $ fadein_sideimage = False
    Y "Wh-what is..." with shakeonce
    $ show_side_oriana = True
    $ show_side_cecilia = True
    C surprised "Looks like a dead man sitting. Wait, hang on..."
    C thinking "...Yep. [t_clue]No pulse[t_cluee]. Definitely dead."
    Y depressed "He's...dead...? Then... Is the culprit...?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O afraid "....."
    play ctc_sfx "<silence 1.0>"
    C sad "....."
    Y shocked "...Wh-what's wrong with you two?"
    C thinking "Um, well--"
    O annoyed "It's nothing!" with shakeshort
    C surprised "...!" with shakeonce
    O leering2 "[name_player]. I don't believe that corpse there is the culprit."
    O irritated "It's clearly been dead and rotting for a [t_clue]very long time[t_cluee]. If anything, it must've been one of the culprit's first victims."
    Y sad "Y-yeah... I guess that makes sense..."
    $ fadein_sideimage = True
    $ show_side_oriana = False
    $ show_side_cecilia = False
    scene bg black with dissolvemed
    scene bg basement
    show oriana irritated at myleft_fadein
    show cecilia thinking at myright_fadein
    with dissolvemed
    C "....."
    show cecilia sad at myright
    C "...So, uh... What now? Looks like the culprit's nowhere to be found after all."
    Y leering "No, there has to be someone here. It's the only explanation for how I couldn't find who killed Ria in the lounge."
    C surprised "So you think there's someone hiding somewhere around here?"
    Y sad "Yeah... Let's stay on our guard and take a good look around..."
    show oriana thinking at myleft
    O "....."
    Y surprised "...Ria?"
    O blink "Y-yes, I agree. There might be something of interest hidden around here..."
    O thinking "We should take some time looking around. But be careful."
    C smile "....."
    $ _last_say_who = None
    window auto hide
    stop music fadeout 3.0
    show bg black with dissolvemed
    I "...It's happening again..."
    play ctc_sfx "<silence 1.0>"
    I "They're hiding something from me again... Why...?"
    play ctc_sfx sfx_heartbeat_single
    I "How could they STILL be keeping secrets from me, even now, after everything we've been through?!" with shakeonce
    scene bg black with dissolvemed
    I "....."
    I "...No. That's not important right now."
    I "All that matters is that we escape safely. And to do that, we need to [t_clue]find the culprit[t_cluee]..."
    scene bg basement with dissolvemed
    Y blink "....."
    $ fadein_sideimage = False
    Y leering "Alright, let's all take a careful look around this place."
    $ fadein_sideimage = True
    I "I should try to get Cece and Ria to talk to me more too..."

    $ d2a2_basement_clue1 = False
    $ d2a2_basement_clue2 = False
    $ d2a2_basement_clue3 = False
    $ d2a2_basement_clue4 = False
    $ d2a2_basement_clue5 = False
    $ d2a2_basement_clue6 = False
    $ d2a2_basement_clue7 = False
    $ d2a2_basement_clue8 = False
    $ d2a2_basement_clue9 = False
    $ d2a2_basement_clue10 = False
    $ d2a2_basement_clue11 = False
    $ d2a2_basement_clue12 = False

    $ investigation_location = "d2a2_basement"
    $ investigation_complete = False
    $ investigation_perfect = False
    $ investigation_clues_required = 5
    $ investigation_clues_required_found = 0
    $ investigation_clues_optional = 7
    $ investigation_clues_optional_found = 0

    $ music_info = False
    scene bg basement with dissolve
    play sound sfx_pac_intro2
    call screen pac_investigation_start(_("Basements Are Scary"), _("You, Cecilia, and Oriana have finally pierced the heart of the killing game.\nWill you be able to find the light before the darkness consumes you...?"))
    $ music_info = True
    stop sound
    play music bgm_karma
    $ show_music_info_timer = music_info_pop_out_time()

label d2a2_basement_investigation:
    $ renpy.choice_for_skipping()
    scene bg basement with dissolvequick
    if not investigation_complete:
        if investigation_clues_required_found >= investigation_clues_required:
            $ investigation_complete = True
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d2a2_basement_perfect
            else:
                call d2a2_basement_complete
    elif not investigation_perfect:
        if investigation_clues_optional_found >= investigation_clues_optional:
            $ investigation_perfect = True
            call d2a2_basement_perfect
    call screen pac_d2a2_basement with dissolvequick
    if investigation_location != None:
        jump d2a2_basement_investigation
    else:
        jump d2a2_basement_end

label d2a2_basement_end:
    call save_file_name_update (2, "d2a2_basement_end")
    $ investigated_basement = True
    scene bg black
    scene bg basement
    show oriana thinking at myleft_fadein
    show cecilia thinking at myright_fadein
    with dissolveslow
    O "So... That's everything, then."
    Y thinking "I think it's safe to say that the only place the culprit could be hiding is the room behind that [t_clue]locked door[t_cluee]."
    C sad "Again with the locked doors..."
    O blink "We've searched the whole house pretty thoroughly now, and there aren't any more mysterious keys."
    Y leering "That means the key has to be somewhere around here. Let's check the floor a bit more carefully."
    $ _last_say_who = "C"
    show bg basement
    hide oriana
    show cecilia thinking at mycenter
    with dissolve
    C "Mrghhh... Keys are so easy to miss, though..."
    show cecilia thinking at mycenter_to_myright
    C "It's so dark that even if we keep our eyes glued to the floor, I don't think--{w=1.0}{nw}"
    stop music
    play ctc_sfx sfx_trip_furniture
    show cecilia surprised at mycenter_closeup with custom_flashquick()
    extend " ACK!!" with shakeshort
    window auto hide None
    play sound sfx_fallhard
    scene bg basement with shakeshort
    $ show_side_oriana = True
    O panicked "Hey!" with hpunch
    $ fadein_sideimage = False
    $ show_side_oriana = False
    Y panicked "Cece?!" with hpunch
    Y "{cps=6}.....{/cps}"
    $ fadein_sideimage = True
    window auto hide
    $ _last_say_who = "O"
    show oriana irritated2 at mycenter with dissolve
    show oriana irritated2 at crouch
    O shouting "Hey! Snap out of it!" with shakeonce
    O leering2 "....."
    O irritated "...Tsk. She's knocked out."
    O thinking "Looks like she tripped and hit her head on the foot of...whatever this is."
    I "She's actually pretty clumsy, huh...?"
    O surprised "...Hmm? There's something here."
    show oriana annoyed2 at standup
    O "[name_player], take this blue dwarf off my hands."
    Y worried "R-right."
    scene bg black with dissolvemed
    play sound sfx_clothrustle
    I "Cece's unconscious..."
    I "Heh. When she's asleep, she sorta looks like an angel..." with vpunch
    I "I'll just lean her against the table behind us right here..."
    $ show_side_oriana = True
    O surprised "...! [name_player], take a look." with shakeonce
    $ fadein_sideimage = False
    Y thinking "Huh? What's..."
    play ctc_sfx "<silence 1.0>"
    Y surprised "...!" with vpunch
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    scene bg basement hatch:
        xalign 0.6 yalign 0.5 zoom 1.1
        easein 4.0 zoom 1.0
    with dissolvemed
    $ persistent.unlock_bg_basement_hatch = True
    pause 2.0
    Y surprised "Wh-wha... Is this...?"
    $ fadein_sideimage = False
    O leering2 "A [t_clue]secret hatch[t_cluee]. And if we look inside, you can see it goes underground."
    play music bgm_discussion
    Y angry "This... This is a major find!" with shakeshort
    O blink "There are two possibilities here, [name_player]."
    O "This could be a secret [t_clue]alternative escape route[t_cluee] out of this house, or..."
    O leering2 "...it could be where the [t_clue]true culprit[t_cluee] is hiding, ready to ambush us the second we jump in."
    Y shocked "...! That's..." with shakeonce
    O irritated "I know. It's a big gamble."
    O "But we can't exactly ignore it, now can we?"
    Y thinking "Definitely not. Either way is progress, at least."
    Y sad "Looks like the darkness down there is ADVANCED darkness, though. I'm squinting as hard as I can, but..."
    Y leering "All I can see is that the ground is close enough that we can [t_clue]jump in[t_cluee], but nothing else."
    O thinking "...No choice then. One of us will just have to go in and see what happens."
    $ fadein_sideimage = True
    I "One of us..."
    O default "So who will it be, [name_player]? I don't mind jumping in."
    $ fadein_sideimage = False
    Y panicked "Huh? Y-you're letting me decide? Why?" with hpunch
    O blink "...No particular reason. Flip a coin if you need to."
    O leering2 "Just hurry up and make a choice."
    play ctc_sfx "<silence 1.0>"
    Y shadow2 "{cps=6}.....{/cps}"
    $ fadein_sideimage = True
    play ctc_sfx sfx_heartbeat_single
    I "...There's that [t_clue]uneasy feeling[t_cluee] again. But why...? " with shakeonce
    I "It's just jumping into a hatch. And I have my time travel power. Maybe there's no point in thinking too much about it?"
    Y blink "{cps=6}.....{/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend leering " ...Okay."
    $ fadein_sideimage = True
    I "It's time. Who should jump in...?"
    play ctc_sfx "<silence 1.0>"
    $ show_side_oriana = False

label d2a2_basement_choice:
    $ show_choicegrand = True
    play loop_sfx sfx_heartbeat
    show bg basement hatch:
        xalign 0.6 yalign 0.5 zoom 1.0
        easein 20.0 zoom 1.5
    menu:
        "Have Ria jump in":
            $ show_choicegrand = False
            stop loop_sfx fadeout 3.0
            scene bg basement hatch with dissolve
            Y default "Could you jump in, Ria?"
            $ show_side_oriana = True
            $ fadein_sideimage = False
            O surprised "....."
            Y surprised "...Ria?"
            O thinking "Y-yes, I can do that. No problem..." with shakeonce
            $ fadein_sideimage = True
            I "...She's afraid, isn't she?"
            Y sad "Okay never mind, you don't have to--" with hpunch
            $ fadein_sideimage = False
            O irritated "I said I can do it! Just give me a moment to mentally prepare..." with shakeonce
            $ fadein_sideimage = True
            I "...I kinda feel bad now..."
            $ show_side_oriana = False
            $ _last_say_who = "O"
            scene bg basement
            show oriana irritated at mycenter
            with dissolve
            stop music fadeout 3.0
            O "*deep inhale*{w=1.0}{nw}" with hpunch
            play ctc_sfx "<silence 1.0>"
            extend thinking " Wheeeeewww..." with shakeshort
            Y surprised "....."
            play ctc_sfx sfx_whooshlow
            show bg black
            show oriana leering at mycenter_closeup
            O "Mmph!" with vpunch
            play ctc_sfx "<silence 1.0>"
            scene bg black with custom_flashquick()
            pause 1.0
            play sound sfx_fallsoft
            with vpunch
            pause 2.0
            I "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            I "{cps=6}.......{/cps}"
            play ctc_sfx "<silence 1.0>"
            I "...Nothing happened."
            play ctc_sfx "<silence 1.0>"
            scene bg basement hatch with dissolvemed
            Y surprised "You okay down there, Ria?"
            $ show_side_oriana = True
            $ fadein_sideimage = False
            O hidden "...Yes, I'm fine. I seemed to have stepped on something, though."
            play ctc_sfx sfx_emotequestion
            O "...Hm. From the way it feels, I think it's a [t_clue]key[t_cluee]."
            Y panicked "A key...? Oh! That might be the key to that locked door up here!" with shakeonce
            O "I think so too. Wait, let me check this place a bit more first."
            O "It feels like I can walk down this path a little. I just can't see anything..."
            Y angry "Be careful, Ria!" with shakeonce
            O "{size=-10}...Rgh! What is this... A wall...? It doesn't seem like this path leads outside after all...{/size}" with shakeonce
            Y thinking "Seems like the culprit isn't hiding down there either, huh?"
            Y default "Okay, come on ba--{w=0.5}{nw}"
            window auto hide None
            play ctc_sfx sfx_knifestab
            scene bg basement hatch at blurring, wobble
            with custom_flashquickred()
            call save_file_name_update (2, "d2a2_darkness")
            window auto show None
            extend shocked " ...kKGH!!!" with shakelong
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            I "{cps=6}.....{/cps} ...What...?"
            O hidden "{size=-10}[name_player]? What happened?{/size}"
            $ fadein_sideimage = False
            play ctc_sfx "<silence 1.0>"
            Y depressed "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            Y depressed stabbed "{cps=6}.......{/cps}"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            I "Someone...[t_clue]stabbed me[t_cluee]...in the back..." with shakeonce
            play ctc_sfx "<silence 1.0>"
            show bg basement hatch at blurring, wobble:
                xalign 0.0
            I "{cps=12}I'm... I feel weak... This is...{/cps}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            scene bg black with dissolvemed
            play sound sfx_fallhard
            with shakelong
            pause 1.0
            scene bg bloodpool 1 with dissolveslow
            Y shadow stabbed "{cps=5}..........{/cps}"
            play ctc_sfx "<silence 1.0>"
            I "{cps=6}.....{/cps} ...Heh..."
            I "...After all that talk about staying on our guard..."
            I "I'm the one...who messed up..."
            scene bg bloodpool 2 with dissolvemed
            O hidden "{size=-20}[name_player]! Answer me!{/size}" with shakelong
            I "Weird though..."
            I "It's burning hot on my back, and...I can feel my consciousness fading, but..."
            I "Getting stabbed...doesn't hurt as much as I thought it would..."
            scene bg bloodpool 3 with dissolvemed
            I "...Huh. Wait. This is...[t_clue]good[t_cluee]..."
            I "If I die, then the other two can escape through the front door..."
            I "...Yeah, why didn't I consider this as an option before?"
            I "Now the killing games...can finally end..."
            play ctc_sfx "<silence 1.0>"
            I "Heh..." with shakeonce
            play ctc_sfx "<silence 1.0>"
            I "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            I "I wonder [t_clue]who stabbed me[t_cluee], though...?"
            play ctc_sfx "<silence 1.0>"
            show bg black with custom_flashquick()
            KI "[t_ghost]...no...can't...[t_ghoste]" with shakeonce
            I "...Huh? ...My head... It's..."
            play loop_sfx sfx_heartbeat fadein 5.0
            I "No..."
            I "No, just leave things like this..." with hpunch
            play ctc_sfx "<silence 1.0>"
            I "Let me die! Just... Just [t_clue]let me DIE[t_cluee] already!" with shakeonce
            KI "[t_ghost]...hurts... I don't...[t_ghoste]" with shakeonce
            I "No... I...can't escape...!" with shakeonce
            I "{size=+5}Don't do it...! Don't send me back!{/size}" with shakeshort
            I "{size=+10}I want out! LET IT ALL END! PLEASE!!{/size}" with shakeshort
            $ show_side_oriana = False
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            stop loop_sfx
            show bg black with custom_flashquick()
            KI "[t_ghost]{size=+10}I DON'T WANNA DIEEEEEEEEEEEEEE!!{/size}[t_ghoste]" with shakelong
            play ctc_sfx "<silence 1.0>"
            play sound sfx_wail
            window auto hide dissolveslow
            pause 2.0
            $ renpy.choice_for_skipping()
            $ _skipping = False
            show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#ff0000}ПЛОХАЯ КОНЦОВКА{/color}{/size}\nКонцовка тьмы{/font}" with dissolve
            pause 2.0
            $ _skipping = True
            pause 3.0
            hide text with dissolveslow
            $ persistent.unlock_bg_bloodpool = True
            $ seen_ending_darkness = True
            $ shard_string = "Darkness"
            $ renpy.music.set_volume(1.0, 0, channel="music")
            stop music
            jump gameover_day2
        "Have Cece jump in":

            $ show_choicegrand = False
            if seen_ending_light and seen_ending_darkness:
                stop music
                stop loop_sfx
                scene bg black with custom_flashbulb()
                pause 0.5
                Y blink "...Let's have Cece jump in."
                jump d2a3
            else:
                stop loop_sfx fadeout 3.0
                scene bg basement hatch with dissolve
                $ show_side_oriana = False
                Y blink "Cece, you'd probably have the best luck down there."
                $ fadein_sideimage = False
                $ show_side_oriana = True
                O disappointed "[name_player]. Have you forgotten that she's knocked out right now?"
                $ show_side_oriana = False
                Y panicked "Oh. Right."
                $ fadein_sideimage = True
                I "I guess she can't exactly jump in while she's unconscious..."
                play ctc_sfx sfx_emotequestion
                I "...Huh. Wonder why I thought of that as an option, then...?" with hpunch
                Y blink "Alright, let's try this again."
                I "Who should jump in?"
                play ctc_sfx "<silence 1.0>"
                jump d2a2_basement_choice
        "Jump in yourself":

            $ show_choicegrand = False
            stop loop_sfx fadeout 3.0
            scene bg basement hatch with dissolve
            Y blink "...I'll jump in."
            $ show_side_oriana = True
            $ fadein_sideimage = False
            O default "....."
            O blink "...If you're sure, then go for it."
            $ fadein_sideimage = True
            I "I think I saw her sigh in relief just now."
            O leering "Be careful, okay?"
            $ fadein_sideimage = False
            Y leering "Yeah, I'll check it out really quickly and come right back up."
            $ fadein_sideimage = True
            stop music fadeout 3.0
            scene bg basement with dissolve
            Y blink "....."
            I "Okay, deep breaths..." with hpunch
            I "The ground is right there, after all. Just focus on landing safely."
            Y angry "Here goes!"
            scene bg black with custom_flashquick()
            play ctc_sfx sfx_whooshlow
            show bg black
            with vpunch
            pause 1.0
            play sound sfx_flameburst
            play loop_sfx sfx_flameloop
            scene bg flamewall with custom_flashbulblongred()
            call save_file_name_update (2, "d2a2_light")
            Y scream "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAGGGGGGGGGGGGGHHHHHHHHHHH!!!" with shakelong
            $ fadein_sideimage = False
            O injured "NRGGHH!! F... [t_clue]Flames[t_cluee]?! Wh-what just..." with shakeshort
            play music bgm_tragedy
            O stabbed "A-ah... [name_player]!" with shakeshort
            $ fadein_sideimage = True
            window auto hide
            show pov_hand:
                xalign 0.0 yanchor 1.0 ypos 1.5 xoffset 0 zoom 1.2 blur 20
                parallel:
                    easein 3.0 xalign 0.2 ypos 1.2 zoom 1.0 blur 0
                parallel:
                    ease 0.05 xoffset -2
                    ease 0.15 xoffset 3
                    ease 0.05 xoffset -2
                    ease 0.05 xoffset 3
                    ease 0.15 xoffset -3
                    ease 0.05 xoffset 0
                    repeat
            with dissolve
            Y pained2 "UUUUUUUUUUUUUUUUUUAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAARRRRRGGGGGHHHHHH!!!" with shakelong
            $ fadein_sideimage = False
            O depressed "...No..."
            O horrified "NOOOOOOOOOOOOOOOOOO!!" with shakelong
            show pov_hand:
                xalign 0.2 yanchor 1.0 ypos 1.2 xoffset 0 blur 10 alpha 1.0 matrixcolor BrightnessMatrix(0.0)
                parallel:
                    linear 7.0 blur 30 xalign 0.3 matrixcolor BrightnessMatrix(-1.0)
                    linear 10.0 alpha 0.0
                parallel:
                    ease 0.15 xoffset -2
                    ease 0.45 xoffset 3
                    ease 0.15 xoffset -2
                    ease 0.15 xoffset 3
                    ease 0.45 xoffset -3
                    ease 0.15 xoffset 0
                    repeat
            Y whiteeyes "Aaaaghh... A-agh..." with shakeshort
            Y whiteeyes2 "...a... ...h..." with shakeshort
            $ fadein_sideimage = True
            I "...I... I can't see..." with shakeonce
            I "The flames..." with shakeonce
            I "Bright... Red..." with shakeonce
            I "My body's...burning...?"
            I "The pain..." with shakeonce
            I "It's...unbearable..." with shakeonce
            I "Everything...hurts..." with shakeshort
            I "Kill me."
            extend " Kill me."
            extend "{cps=36} Kill me, kill me, kill me, kill me, kill me, kill me, kill me, kill me, kill me...{/cps}"
            I "{cps=48}KILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLME\nKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLMEKILLME--{/cps}" with shakeshort
            I "GOD, I'M BEGGING YOU, PLEASE--" with shakelong
            hide pov_hand
            I "...! I..." with custom_flashquick()
            I "I...[t_clue]remember[t_cluee]..."

            if not seen_ending_light:
                call truename_entry

            if input_name_true == input_name:
                I "[name_player_true]...is in fact my true name..."
            else:
                I "My true name...is [name_player_true]... Not [name_player]..."
            I "And my life... I remember..."
            I "I'm..."
            play ctc_sfx sfx_heartbeat_single
            $ renpy.music.set_volume(0.0, 0, channel="music")
            $ renpy.music.set_volume(0.0, 0, channel="loop_sfx")
            show bg flamewall:
                matrixcolor BrightnessMatrix(-1.0)
                easein 10.0 matrixcolor BrightnessMatrix(0.0)
            with custom_flashquickred()
            I "I'm [t_clue]dead[t_cluee]." with shakeshort
            $ renpy.music.set_volume(1.0, 5, channel="music")
            $ renpy.music.set_volume(1.0, 5, channel="loop_sfx")

            if not seen_ending_light:
                I "{cps=6}I...{/cps}should be dead already.{w=1.0} I died...{nw}"

                menu:
                    extend ""
                    "With regrets":
                        $ died_with_regrets = True
                    "Without regrets":
                        $ died_with_regrets = False
            if died_with_regrets:
                I "I...didn't want to die..."
                I "But... I definitely did. Long before any of this."
            else:
                I "I died...satisfied..."
                I "I don't need any second chances at life, so..."
            I "...Why...? Why am I here...?" with shakeonce
            I "What even is [t_clue]this place[t_cluee]?! WHY WAS I BROUGHT HERE?!" with shakeshort
            I "The pain... Every part of my body..."
            I "Make it stop...{w=1.0}{nw}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            extend " PLEASE MAKE IT STOP!!" with shakelong
            O hidden "{size=-10}...You! What are you...{/size}" with shakeonce
            I "...R-Ria...?" with hpunch
            O "{size=-10}...ou [t_clue]tricked[t_cluee] us! ..... ...we... {/size}{size=-20}...[name_player] is...{/size}" with shakeshort
            with custom_flashquick()
            KI "[t_ghost]...can't...[t_ghoste]" with shakeonce
            I "Ria's...talking to...[t_clue]someone[t_cluee]...?" with shakeonce
            KI "[t_ghost]...hurts so bad... I don't...[t_ghoste]"
            I "Who is it?" with shakeonce
            extend "{cps=24} Who is it, who is it, who is it, who is it, who is it, who is it, who is it...{/cps}"
            I "{cps=32}WHOISITWHOISITWHOISITWHOISITWHOISITWHOISITWHOIS\nITWHOISITWHOISITWHOISITWHOISITWHOISITWHOISIT--{/cps}" with shakeshort
            play ctc_sfx "<silence 1.0>"
            show bg black with custom_flashquick()
            stop music
            KI "[t_ghost]{size=+5}I DON'T WANT TO DIIIIIIIEEEE!!{/size}[t_ghoste]" with shakelong
            play ctc_sfx "<silence 1.0>"
            $ show_side_oriana = False
            stop loop_sfx fadeout 10.0
            play sound sfx_wail
            window auto hide dissolveslow
            pause 2.0
            $ renpy.choice_for_skipping()
            $ _skipping = False
            show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#ff0000}ПЛОХАЯ КОНЦОВКА{/color}{/size}\nКонцовка света{/font}" with dissolve
            pause 2.0
            $ _skipping = True
            pause 3.0
            hide text with dissolveslow
            $ persistent.unlock_bg_flamewall = True
            $ seen_ending_light = True
            $ shard_string = "Light"
            jump gameover_day2

label truename_entry:
    I "My name... My [t_clue]true name[t_cluee]...{nw}"

    menu:
        extend ""
        "\"...is [name_player].\"":
            $ input_name_true = input_name
            $ name_player_true = "{color=#44b817}"+input_name_true+"{/color}"
            return
        "\"...is NOT [name_player].\"":
            I "...My...true name...is..."
    $ quick_menu = False
    $ music_info = False
    $ input_name_true = renpy.input("ВВЕДИТЕ ВАШЕ {size=+15}{color=#44b817}НАСТОЯЩЕЕ ИМЯ{/color}{/size}", exclude={'[', ']', '{', '}'}, pixel_width=250)
    $ quick_menu = True
    $ music_info = True


    $ input_name_true = input_name_true.strip()

    if input_name_true == "":
        I "...No... I remember my true name..."
        jump truename_entry
    else:
        $ name_player_true = "{color=#44b817}"+input_name_true+"{/color}"
        I "...[name_player_true]..."
        I "My true name is [name_player_true]...{nw}"

        menu:
            extend ""
            "\"Yes, it is.\"":
                return
            "\"No, that's wrong.\"":
                jump truename_entry
label d2a3:
    scene bg basement
    with dissolvemed
    $ _last_say_who = 'O'
    show oriana surprised at mycenter with dissolvemed
    O "Huh? What do you mean? Cecilia is--"
    Y leering "I have a strong feeling that she'll wake up in a couple of seconds." with hpunch
    I "Or maybe she's already awake..."
    O leering2 "...Did you travel through time again?"
    Y blink "...Yeah, more than once."
    $ fadein_sideimage = False
    Y leering "No matter which of us two jumps into the hatch, it all ends badly."
    Y thinking "We'd be better off waiting until Cece's awake."
    $ fadein_sideimage = True
    O thinking "....."
    Y surprised "...What's wrong?"
    O "...It's just...now that you've said that..."
    play ctc_sfx sfx_heartbeat_single
    O irritated "I have an [t_clue]uneasy feeling[t_cluee] about going in that hatch too." with shakeonce
    Y thinking "But...didn't you say it could be an escape route?"
    O confused "I did, but at the same time, I felt something strange... Maybe if..."
    O leering2 "...[name_player]. May I ask what happens if I jump in?{nw}"

    menu:
        extend ""
        "Tell her":
            Y blink "You find a key down there, but...someone [t_clue]stabs my back[t_cluee] and kills me."
            O surprised "...! That's..." with shakeonce
            O irritated "...Oh. I understand why you want to wait now."
            Y shadow2 "....."
        "Don't tell her":
            Y sad "...It's better if you don't know."
            O confused "....."

    O confused "...And what happens if {i}you{/i} jump in?{nw}"

    menu:
        extend ""
        "Tell her":
            Y troubled "...I..." with shakeonce
            I "...Can I say it...?"
        "Don't tell her":
            Y wince "I...don't want to say." with shakeonce

    O blink "...[name_player]. Your face gives it all away, you know."
    play ctc_sfx "<silence 1.0>"
    O thinking "[t_clue]I get killed again[t_cluee], don't I?"
    Y depressed "{cps=6}.....{/cps}{cps=1} {/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend panicked "...W-wait, what?! That's..." with shakeshort
    $ fadein_sideimage = True
    O sideeye "Again, there's no point trying to hide it."
    scene bg basement hatch with dissolvemed
    pause 1.0
    $ show_side_oriana = True
    O default "Looking at this hatch... It brings me a mysterious sense of foreboding."
    $ fadein_sideimage = False
    O thinking "As though this hatch will be the [t_clue]last thing[t_cluee] I look at before my life comes to an end."
    Y depressed "...W-wait. Does that mean..."
    play ctc_sfx sfx_heartbeat_single
    Y afraid2 "Do you...[t_clue]remember[t_cluee] getting killed here?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O blink "{cps=6}.....{/cps}"
    Y shocked "...Ria...?"
    play ctc_sfx sfx_emotequestion
    O confused "Hm. That's strange. As soon as you said that, the foreboding feeling [t_clue]suddenly vanished[t_cluee]."
    Y depressed "...What? How?" with shakeonce
    O "{cps=6}.....{/cps} ...Hmm..."
    O irritated "...No, it's no use. I'm sorry, I don't think there's anything more I can say about it." with hpunch
    play ctc_sfx "<silence 1.0>"
    Y shocked "{cps=6}.....{/cps} ...O-okay, then..." with hpunch
    $ fadein_sideimage = True
    I "...What could Ria's feelings mean? I mean...I [t_clue]never saw her die here[t_cluee]..."
    I "She can't possibly remember that!{w=0.5} Unless...{w=0.5} No..." with shakeonce
    play ctc_sfx sfx_heartbeat_single
    I "No... [t_clue]I'm the only time traveler here[t_cluee]...{w=1.0} ...Right?" with shakeonce
    $ show_side_cecilia = True
    C sad "Mrgh..." with hpunch
    $ fadein_sideimage = False
    O surprised "Oh, you were right. She's waking up."
    C "Just...five more minutes... Mom..."
    O disappointed "....."
    play ctc_sfx sfx_whoosh
    window auto hide None
    scene bg black
    with custom_flashquick()
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    $ show_side_oriana = False
    pause 0.2
    show bg basement
    show oriana irritated at myleft
    show cecilia sobbing at myright, crouchquick
    window auto show None
    play ctc_sfx sfx_punch
    C "BWAHHH!!" with shakelong
    O "If you're well enough to babble like that, then get up already."
    show cecilia sad at myright, standup
    C "Even my own mother's never hit me..."
    C thinking "...Hm? What's up? You guys look kinda tense. And sweaty."
    C surprised "*gasp* Wait, what did you do while I was knocked out? No way, did you raise the age rating of this ga--" with shakeshort
    O disappointed "[name_player] thinks you should jump into that hole there."
    play ctc_sfx sfx_emotesob
    C sobbing "What?! [name_player], how could you...?" with hpunch
    C "I thought what we had was SPECIAL!" with shakeonce
    Y worried "...Okay, settle down and let me explain from the beginning."
    play music bgm_discussion
    scene bg black with dissolveslow
    scene bg basement
    show oriana blink at myleft
    show cecilia thinking at myright
    with dissolveslow
    C "I see, and that's why you waited for me to wake up."
    Y "Yeah."
    C determined "And to be clear, no clothes were removed by anyo--{w=0.5}{nw}"
    play ctc_sfx sfx_punch
    show oriana irritated2
    show cecilia sobbing at crouchquick
    with custom_flashquick()
    extend "oOMAN ON WOMAN VIOLENCEE!!" with shakelong
    O annoyed "Enough with the tired gags and jump into that hole already."
    show cecilia pout at hop
    C "Wait wait wait wait, I do have a serious suggestion to give here!" with shakeonce
    C thinking "So from the sound of things, whoever does NOT jump into the hatch gets killed by something, right?"
    I "...Jumping into the hatch kills me too, but...{w=0.5} ...No, I'll tell them about that later." with hpunch
    C default "Then what we oughta do is have me stay up and [t_clue]stand guard[t_cluee] while one of you two jump in!"
    Y thinking "...Huh?"
    C thinking "I mean, if you're getting jumped by the culprit hiding somewhere around here, I'm the best chance you have at surviving, right?"
    O confused "{cps=6}.....{/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend irritated " ...Tsk. I can't refute your logic..." with hpunch
    Y shadow2 "....."
    C happy "Heehee~ Score one for Cece, finally!"
    C grin "...So! Which of you's gonna stay up here with me?"
    play ctc_sfx sfx_whooshlow
    Y shouting "I'll stay up here!" with shakeshort
    show oriana panicked at hop
    O "Eh?! [name_player]?!"
    C overjoyed "Oooh! What an eager beaver you are, [name_player]!"
    Y sad "Y-yeah, I...uh... I'm not too good with dark places..."
    O leering "....."
    I "Ria's leering daggers into me...{w=0.5} But it's better than burning to death again..." with hpunch
    Y panicked "S-sorry, Ria, I guess... I-I mean, you said you were fine with jumping in before, right?" with shakeonce
    O surprised "...! That's..." with shakeonce
    C blush "It's settled, then! Right this way, milady~"
    C wink "Watch your step...or, y'know, don't. [u_heart]"
    O annoyed "....." with shakeonce
    I "Sorry Ria..."
    stop music fadeout 3.0
    scene bg black with dissolvemed
    scene bg basement hatch with dissolvemed
    $ show_side_cecilia = True
    $ show_side_oriana = True
    O thinking "....."
    $ fadein_sideimage = False
    O irritated "......."
    C grin "Come on, enough stalling! Down you go, Ria~" with vpunch
    play ctc_sfx sfx_emoteshout
    O annoyed "DON'T push me!" with shakeshort
    O leering2 "....."
    $ fadein_sideimage = True
    I "Yep, she's still shooting me daggers..."
    Y worried "...Uh... Be careful, Ria." with hpunch
    $ fadein_sideimage = False
    O irritated "{cps=6}.......{/cps}{w=0.5} *sigh*{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend annoyed2 " {size=-10}I hope you get stabbed a little anyway.{/size}"
    Y panicked "Huh? What did you sa--" with shakeonce
    O shouting "HERE GOES!" with shakeshort
    play ctc_sfx sfx_whooshlow
    show bg black
    show oriana_raw leering at mycenter_closeup
    Y panicked "Whoa!" with shakelong
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    scene bg black with custom_flashquick()
    pause 1.0
    play sound sfx_fallhard
    with shakeshort
    pause 2.0
    I "{cps=6}.....{/cps}"
    scene bg basement hatch with dissolvemed
    I "...Nothing happened...?"
    Y shouting "Ria! Are you okay?!" with shakeshort
    $ fadein_sideimage = False
    O hidden "{cps=6}.......{/cps}{nw}"
    play ctc_sfx sfx_emotesigh
    extend " {size=-10}Ow...{/size}" with hpunch
    C smug "Sounds like she didn't stick the landing."
    $ fadein_sideimage = True
    I "She should've hopped down a little more carefully..."
    $ show_side_cecilia = False
    $ show_side_oriana = False
    scene bg basement
    show cecilia at mycenter
    with dissolvemed
    C smile "So, [name_player]! Guess it's just you and me now~ [u_heart]"
    Y sad "...! Y-yeah..." with shakeonce
    I "...Cece..."
    C surprised "Hm? Ooooh..."
    C grin "You look really worked up and excited right now, [name_player]."
    C blush "Are you...thinking about what happened earlier in the bedroom?"
    I "...I don't think she's gonna try anything funny..."
    Y blink "...You have your knife on hand, right?"
    play ctc_sfx sfx_knifebrandish
    C happy knife "Yep! All the better to protect you with, my dear~" with custom_flashquick()
    Y sad "G-good, that's... That's a relief..." with shakeonce
    play ctc_sfx sfx_knifeequip
    C surprised "...Seriously, are you okay, [name_player]? You don't have to be so on guard." with hpunch
    C sad "I said I'd protect you, didn't I?"
    play ctc_sfx sfx_heartbeat_single
    I "...She says all that, but... I bet the moment I show my back to her..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y shouting "...Ria! Everything going okay down there?!" with shakeshort
    $ show_side_oriana = True
    $ fadein_sideimage = False
    O hidden "{size=-10}It's exactly like how you described it!{/size}"
    O "{size=-10}There's a key here, but I don't think this passage leads anywhere!{/size}"
    Y leering "A-all right, hurry up and come back! I'll give you a hand!"
    $ fadein_sideimage = True
    C thinking "....."
    C surprised "...? You'll need to turn around if you want to help her up, you know."
    Y sad "Right, I'll just..." with hpunch
    $ fadein_sideimage = False
    Y panicked "W-wait, Cece, you're pretty strong! Why don't {i}you{/i} help her up, and I'll keep watch for a moment." with shakeonce
    $ fadein_sideimage = True
    C sad "Uh...sure?"
    C thinking "You're acting really strange right now, [name_player]. And that's coming from ME!"
    Y shadow2 "....."
    $ show_side_oriana = False
    scene bg black with dissolvemed
    scene bg basement
    show oriana blink at myleft
    show cecilia at myright
    with dissolvemed
    O "*ahem* So here's the key." with shakeonce
    window auto hide
    show oriana at shrink
    pause 0.5
    play sound sfx_knifeglint
    show oriana at myleft with move
    Y thinking "Hmm... It's a little heavier than it looks..."
    $ fadein_sideimage = False
    Y default "I wonder why the key was right under the hatch and not hidden further down that passageway."
    $ fadein_sideimage = True
    O thinking "Perhaps the culprit was in a rush and threw it in before covering up the hatch?"
    Y thinking "But we still haven't found the culprit. Wouldn't the safest way to hide a key be to just carry it aro--"
    $ _last_say_who = 'C'
    play ctc_sfx sfx_knifebrandish
    window auto hide None
    show bg basement nocorpse
    show oriana surprised
    show cecilia shadow knife at mycenter
    with custom_flashquick()
    Y afraid "WHA--{w=1.0}{nw}" with shakeshort
    play ctc_sfx sfx_whooshhigh
    scene bg black with custom_flashquick()
    play sound sfx_knifeswing
    with custom_flashquickred()
    O "EEEEEEK!!" with shakelong
    window auto hide None
    play sound sfx_knifeclash
    with shakeshort
    play ctc_sfx sfx_knifeslash
    scene bg black with custom_flashbulbred()
    pause 2.0
    window auto show
    call save_file_name_update (2, "d2a3")
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "What...just..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    I "...Cece... You..." with shakeonce
    $ show_side_cecilia = True
    C shouting "[name_player]! Snap out of it! OPEN YOUR EYES!!" with shakeshort
    $ fadein_sideimage = False
    Y wince "Huh...?" with hpunch
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    $ _last_say_who = 'V'
    scene bg basement nocorpse at blurred
    show villain at mycenter, blurred
    show eye frame
    with eyeopen_quick
    scene bg black with eyeclose
    hide eye frame
    scene bg basement nocorpse:
        blur 20.0
        linear 1.0 blur 0.0
    show villain at mycenter:
        blur 20.0
        linear 1.0 blur 0.0
    with eyeopen_quick
    play music bgm_chase
    pause 2.0
    show villain at mycenter:
        blur 0.0
    $ persistent.unlock_bg_basement_nocorpse = True
    V "{cps=6}.....{/cps}"
    show bg basement nocorpse at blurring
    Y afraid2 "!!! WHAT THE--" with shakeshort
    I "That's... That's the corpse from the chair!" with shakeonce
    show villain_raw shadow as villain at shudder, backedaway_on
    I "He's...MOVING?!" with shakeshort
    window auto hide None
    play ctc_sfx sfx_knifebrandish
    scene bg basement nocorpse:
        xalign 0.5 yalign 0.5 zoom 1.2
        easein 0.4 yalign 0.2 zoom 1.5
    show villain attacking at mycenter:
        xalign 0.5
        parallel:
            zoom 1.0 ypos 1.05
            easein 0.4 zoom 1.2 ypos 1.15
        parallel:
            linear 0.1 xalign 0.5
            linear 0.1 xalign 0.51
            linear 0.1 xalign 0.49
            linear 0.1 xalign 0.47
            linear 0.1 xalign 0.52
            linear 0.1 xalign 0.5
            linear 0.1 xalign 0.51
            linear 0.1 xalign 0.49
            linear 0.1 xalign 0.47
            linear 0.1 xalign 0.52
            linear 0.1 xalign 0.5
    show dagger glint at mycenter:
        zoom 1.0 ypos 1.05 alpha 0.0
        easein 0.4 zoom 1.2 ypos 1.15 alpha 1.0
        linear 0.2 zoom 1.15 ypos 1.1 alpha 0.0
    with custom_flashquick()
    pause 0.2
    window auto show None
    Y scream "{size=+10}AAAAAAAAHHHHHHHH!!{/size}" with shakeshort
    play ctc_sfx sfx_whooshhigh
    window auto hide None
    show bg basement nocorpse:
        xalign 0.5 yalign 0.2 zoom 1.5
        linear 0.2 yalign 0.0 zoom 2.0
    show villain attacking:
        zoom 1.2 ypos 1.15
        linear 0.3 zoom 2.5 ypos 2.4
    with custom_flashquick()
    pause 0.2
    window auto hide None
    play ctc_sfx sfx_knifeclash
    show bg basement nocorpse at reset:
        xalign 0.0 yalign 0.5 zoom 1.3
    with custom_flashquick()
    show villain shadow at reset:
        zoom 1.0
        xalign 0.5 yanchor 1.0 ypos 1.05
        easein 0.2 xalign 0.24
        linear 0.05 xalign 0.25
    show cecilia determined knife:
        xalign 0.5 yanchor 1.0 ypos 1.05
        easein 0.2 xalign 0.76
        linear 0.05 xalign 0.75
    with shakeshort
    C injured "Kgghh! For a rotting zombie, he sure is packing a lot of muscle..." with shakeonce
    I "{cps=12}He's...{/cps}using a knife...?" with shakeonce
    V shadow "....."
    I "...Wait. Could it be...?"
    I "The one who stabbed me in the back was--" with shakeonce
    play ctc_sfx sfx_whooshhigh
    window auto hide None
    show cecilia_raw surprised as cecilia
    show villain_raw attacking as villain
    with shakeonce
    play sound sfx_knifeclash
    scene bg basement nocorpse at reset:
        xalign 1.0 yalign 0.5 zoom 1.3
    show villain shadow:
        xalign 0.5 yanchor 1.0 ypos 1.05
        easein 0.2 xalign 0.76
        linear 0.05 xalign 0.75
    show cecilia determined knife:
        xalign 0.5 yanchor 1.0 ypos 1.05
        easein 0.2 xalign 0.24
        linear 0.05 xalign 0.25
    with custom_flashquick()
    with shakeshort
    C shouting "[name_player]! GET UP ALREADY!" with shakeshort
    C "Ria got cut! You need to help her up and RUN!" with shakeshort
    Y shocked "Wha... R-Ria?!" with shakeonce
    window auto hide
    hide cecilia
    hide villain
    with dissolvequick
    scene bg basement nocorpse:
        xalign 1.0 yalign 0.5 zoom 1.3
        easeout 0.5 xalign 0.5
        easein 0.5 xalign 0.0
    pause 1.0
    $ _last_say_who = "O"
    show oriana injured at mycenter
    with dissolvequick
    O "Mnnghh...!" with shakeshort
    I "...!! Her arm... It got cut really deep..." with shakeonce
    Y shouting "Ria! Give me your good arm! Hurry!" with shakeshort
    O "I'm...sorry..." with shakeonce
    window auto hide
    hide oriana with dissolve
    scene bg basement nocorpse at wobble
    with dissolve
    I "Okay, I have Ria leaning on my shoulder. Cece is still fighting off that...zombie thing..." with shakeonce
    I "I need to find an escape route!{nw}" with shakeonce

    menu:
        extend ""
        "Go up the stairs":
            scene bg basement nocorpse:
                xalign 0.0 yalign 0.0 zoom 1.3
            with dissolve
            I "The safest place would be back upstairs!" with vpunch
            I "We could also get some supplies to treat Ria's wound--"
            window auto hide None
            play ctc_sfx sfx_whooshlow
            play sound ["<silence 0.2>", sfx_fallhard]
            show bg basement nocorpse at reset
            show cecilia injured at mycenter:
                zoom 1.5
                easein 0.18 zoom 0.99
                linear 0.05 zoom 1.0
                linear 0.02 zoom 1.1
                linear 0.02 zoom 1.0
            with custom_flashquick()
            Y afraid2 "AHH!" with shakelong
            C sad "Aghh... Curse my dainty weight... Got flung like a softball there..."
            Y panicked "Cece, are you--" with shakeonce
            play ctc_sfx sfx_knifeclash
            show villain behind cecilia at mycenter
            show cecilia determined knife at myleft
            with custom_flashquick()
            C "COUNTERRRRRR!!" with shakelong
            show villain behind cecilia at myright
            show cecilia shouting at mycenter
            C "Ngh...! I'm fine! Just hurry to someplace safe!" with shakeonce
            I "They're fighting too close to the stairs... Guess there's only one place left to go!" with hpunch
            scene bg basement nocorpse:
                xalign 0.0 yalign 0.8 zoom 1.3
            with dissolvequick
        "Go into the locked room":
            scene bg basement nocorpse:
                xalign 0.0 yalign 0.8 zoom 1.3
            with dissolve
            I "If we go into that room, we can lock this zombie out!" with shakeonce
    I "Where's the... Right, I still have the [t_clue]key[t_cluee] in my hand!" with hpunch
    play sound sfx_unlock
    Y shouting "Cece! This way!" with shakeshort
    $ fadein_sideimage = False
    $ show_side_cecilia = True
    play ctc_sfx sfx_knifeclash
    C injured "ERGH!! H-hold the door!" with shakeshort
    play ctc_sfx sfx_runninglong
    play sound ["<silence 0.2>", sfx_running]
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene bg black with dissolve
    Y scream "LOCK IT!" with shakelong
    window auto hide custom_flashquick()
    play ctc_sfx sfx_doorcloseloud
    with shakelong


label d2a3_library:
    scene bg black
    show bg library right with dissolvemed
    show screen notify_location("-1 этаж - Библиотека", persistent.unlock_bg_library) 
    Y pained2 "Hrgh... *gasp* ...Ngh... *pant*" with shakeshort
    $ _last_say_who = "C"
    show cecilia injured at mycenter
    with dissolve
    C "Agh... Hooo boy... That was... That was something, huh...?" with shakeshort
    play ctc_sfx "<silence 1.0>"
    show cecilia surprised
    play sound sfx_slamwall3
    $ renpy.music.set_volume(0.5, 0, channel="music")
    $ renpy.music.set_volume(1.0, 1, channel="music")
    window auto hide shakeshort
    pause 0.2
    play sound ["<silence 0.5>", sfx_slamwall2]
    Y afraid2 "...! He's trying to break in!" with shakeshort
    hide cecilia with custom_flashquick()
    $ show_side_cecilia = True
    $ fadein_sideimage = False
    C shouting "Oh no he doesn't!" with shakeonce
    play ctc_sfx ["<silence 0.4>", sfx_slamwall]
    play sound sfx_slamwall3
    $ renpy.music.set_volume(0.5, 0, channel="music")
    $ renpy.music.set_volume(1.0, 1, channel="music")
    C injured "Mrgh! Wait, [name_player]! Hold this door for me! I'll drag that dresser over to block it off!" with shakeshort
    play ctc_sfx ["<silence 0.6>", sfx_slamwall2]
    play sound sfx_slamwall2
    Y shouting "A-all right!" with shakeshort
    $ fadein_sideimage = True
    window auto hide
    play sound sfx_slamwall3
    with shakeshort
    scene bg black with dissolve
    play ctc_sfx ["<silence 0.4>", sfx_slamwall2, sfx_slamwall]
    play sound sfx_furnituredrag
    Y wince "Mrgh...! Grgh..." with shakeshort
    $ fadein_sideimage = False
    play ctc_sfx ["<silence 0.4>", sfx_slamwall, sfx_slamwall3]
    play sound2 sfx_furnituredrag
    C pout "HNNNNGGGGHHHHH!!" with shakelong
    play sound sfx_slamwall3
    play ctc_sfx ["<silence 0.6>", sfx_slamwall2]
    Y panicked "We got it!" with shakeonce
    play sound sfx_slamwall2
    play ctc_sfx ["<silence 0.5>", sfx_slamwall3]
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene bg library right
    show cecilia determined at mycenter
    with dissolvemed
    play sound sfx_slamwall3
    C "Yeah... He's still pounding away though..." with shakeonce
    play ctc_sfx ["<silence 0.5>", sfx_slamwall]
    C "How's Ria doing?" with shakeonce
    Y thinking "Ria's..."
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O injured "....." with shakeonce
    $ show_side_oriana = False
    play sound sfx_slamwall2
    Y afraid "She's gone completely pale... We need to stop the bleeding..." with shakeshort
    $ fadein_sideimage = True
    C thinking "There might be something around here. [name_player], go and take a look around!"
    play ctc_sfx ["<silence 0.5>", sfx_slamwall2]
    play sound sfx_slamwall3
    Y panicked "Right! Okay, um..." with shakeonce
    I "This is... I think it's a [t_clue]library[t_cluee]...?"
    I "...Wait. What's...that..."
    hide cecilia with dissolve
    call save_file_name_update (2, "d2a3_library")
    scene bg library:
        xalign 1.0
        linear 3.0 xalign 0.0
    play sound sfx_slamwall
    with shakeshort
    pause 0.7
    play sound sfx_slamwall3
    with shakeshort
    pause 0.8
    play sound sfx_slamwall2
    with shakeshort
    pause 0.6
    play sound sfx_emotequestion
    pause 0.5
    play sound sfx_slamwall
    with shakeshort
    I "That's..."
    $ persistent.unlock_bg_library = True

    $ d2a3_library_clue1 = False
    $ d2a3_library_checkedcorpse = False
    $ d2a3_library_clue2 = False
    $ d2a3_library_clue3 = False
    $ d2a3_library_clue4 = False
    $ d2a3_library_clue5 = False
    $ d2a3_library_clue6 = False
    $ d2a3_library_clue7 = False
    $ d2a3_library_clue8 = False
    $ d2a3_library_clue9 = False
    $ d2a3_library_clue10 = False
    $ d2a3_library_clue11 = False
    $ d2a3_library_clue12 = False
    $ d2a3_library_clue13 = False
    $ d2a3_library_clue14 = False

    $ investigation_location = "d2a3_library_left"
    $ investigation_complete = False
    $ investigation_perfect = False
    $ investigation_clues_required = 3
    $ investigation_clues_required_found = 0
    $ investigation_clues_optional = 11
    $ investigation_clues_optional_found = 0

    $ music_info = False
    scene bg library left with dissolve
    call screen pac_investigation_start(_("KYAAA!! ZOMBIES!!"), _("A zombie is trying to kill you! Cecilia's holding the door up, and Oriana is...\nHurry and find something in this room to stop Oriana from bleeding out!"))
    $ music_info = True

label d2a3_library_investigation:
    $ renpy.choice_for_skipping()
    if investigation_location == "d2a3_library_right":
        scene bg library right with dissolvequick
        if not investigation_complete:
            if investigation_clues_required_found >= investigation_clues_required:
                $ investigation_complete = True
                if investigation_clues_optional_found >= investigation_clues_optional:
                    $ investigation_perfect = True
                    call d2a3_library_perfect
                else:
                    call d2a3_library_complete
        elif not investigation_perfect:
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d2a3_library_perfect
        call screen pac_d2a3_library_right with dissolvequick
    else:
        scene bg library left with dissolvequick
        if not investigation_complete:
            if investigation_clues_required_found >= investigation_clues_required:
                $ investigation_complete = True
                if investigation_clues_optional_found >= investigation_clues_optional:
                    $ investigation_perfect = True
                    call d2a3_library_perfect
                else:
                    call d2a3_library_complete
        elif not investigation_perfect:
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d2a3_library_perfect
        call screen pac_d2a3_library_left with dissolvequick
    if investigation_location != None:
        jump d2a3_library_investigation
    else:
        jump d2a3_library_end

label d2a3_library_end:
    scene bg black
    pause 1.0
    scene bg library right with dissolvemed
    play sound sfx_slamwall2
    $ renpy.music.set_volume(0.5, 0, channel="music")
    $ renpy.music.set_volume(1.0, 1, channel="music")
    with shakeshort
    pause 0.5
    play sound sfx_slamwall3
    $ renpy.music.set_volume(0.5, 0, channel="music")
    $ renpy.music.set_volume(1.0, 1, channel="music")
    Y pained "Agh... He's still pounding away, Ria's still bleeding..." with shakeshort
    play sound sfx_slamwall2
    $ fadein_sideimage = False
    Y pained2 "After all that looking around, I couldn't find anything we could use as a bandage..." with shakeshort
    $ show_side_cecilia = True
    play ctc_sfx sfx_emotehappy
    C happy "Hey, [name_player]! Don't worry, I got it covered!" with vpunch
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    scene bg library:
        xalign 1.0 yalign 1.0
        linear 1.0 xalign 0.0
    pause 1.0
    play sound sfx_slamwall2
    with shakeshort
    show cecilia happy at mycenter
    with dissolve
    C "Well? What do you think?"
    Y panicked "Huh? ...Ah! Yeah, you got her wound all wrapped up with that cloth..."
    $ fadein_sideimage = False
    Y annoyed "...Wait, where did you get that?"
    $ fadein_sideimage = True
    play sound sfx_slamwall3
    C default "Over there in that corner. You know, where that dead little girl is? I just cut a little bit of that sheet's corner." with shakeshort
    C thinking "Can't believe you missed something so obvious. Come on, were you really even trying?"
    play ctc_sfx sfx_emoteshout
    Y afraid2 "THAT SHEET WAS OBVIOUSLY A BURIAL SHROUD!!" with shakeshort
    C smug "Oh, psh, what's that dead girl gonna do, rise from the dead and try to kill us?"
    play ctc_sfx sfx_emoteshout
    Y scream "WHY DO YOU THINK WE'RE TRAPPED HERE IN THE FIRST PLACE?!" with shakeshort
    stop music fadeout 5.0
    play ctc_sfx sfx_emoteangry
    C shouting "STOP YELLING! Ria's finally starting to settle down!" with shakeshort
    $ show_side_oriana = True
    O shadow "....."
    $ fadein_sideimage = False
    Y shocked "Ah..." with shakeonce
    $ fadein_sideimage = True
    $ show_side_oriana = False
    I "She's right. I think she's just sleeping now..."
    I "....."
    I "...Huh?"
    Y panicked "...Wait. I think the zombie finally let up?"
    C surprised "Yeah... I don't think it's pounding anymore..."
    C sad "Let's wait for a little while, just to be safe."
    Y sad "Y-yeah... It doesn't seem like there's any other way out of this room..."
    play ctc_sfx "<silence 1.0>"
    I "But...what if it's just waiting for us to open the door ourselves...?" with shakeonce
    C smile "[name_player]. I can tell what you're thinking."
    Y surprised "...Huh?"
    C blink "That thing's definitely a mindless zombie. I don't think it's capable of advanced plans like that."
    Y wince "But it was using a knife... Could a mindless zombie really do that?" with shakeonce
    C thinking "....."
    C "A lot was happening earlier, so I can't blame you for missing this, but..."
    C determined "While we were fighting, I cut him a couple times with my knife. Some stabs too.{w=1.0} But he [t_clue]didn't even flinch[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    Y depressed "That's...impossible..." with shakeonce
    C "Exactly. That {i}thing{/i} isn't human."
    C thinking "It's gotta be some kind of science experiment gone wrong. Or an android designed for combat or security."
    play ctc_sfx "<silence 1.0>"
    C blink "Or maybe...it's some kind of [t_clue]demon summoned from Hell[t_cluee]..."
    Y shadow "....."
    $ fadein_sideimage = False
    Y "...Aren't you going to gush about it, then? It's the occult...but for real..."
    $ fadein_sideimage = True
    C sad "Normally, I would, but I don't think you have the energy to retort right now."
    window auto hide
    hide cecilia with dissolve
    scene bg library:
        xalign 0.0 yalign 1.0
        linear 1.0 xalign 1.0
    pause 1.0
    show bg library right:
        blur 0
        linear 10.0 blur 30
    show cecilia smile at mycenter
    with dissolve
    C "Come on, sit down next to me, [name_player]! Take a breather!"
    hide cecilia with dissolve
    Y shadow "{cps=12}...I'll sit, but I don't know how much...I can...{/cps}"
    play ctc_sfx sfx_heartbeat_single
    show bg black with custom_flashquick()
    I "....." with shakeshort
    play ctc_sfx "<silence 1.0>"
    I "...Crap... I'm so sleepy..." with hpunch
    play ctc_sfx "<silence 1.0>"
    I "I've been...time traveling...too much...again..."
    play ctc_sfx "<silence 1.0>"
    I "I... ....."
    play ctc_sfx "<silence 1.0>"
    I "......."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.........{/cps}"
    play ctc_sfx "<silence 1.0>"
    call save_file_name_update (2, "d2a3_library_cece_hearttoheart")
    scene bg black with dissolveslow
    pause 2.0
    I "....."
    play sound sfx_clothrustle volume 0.5
    Y wince "Mrgh..." with hpunch
    $ fadein_sideimage = False
    $ show_side_cecilia = True
    C smile "Oh! [name_player], you're awake?"
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    I "...What...happened...?" with hpunch
    scene bg library dark right
    show cecilia at mycenter
    with dissolveslow
    $ persistent.unlock_bg_library_dark = True
    Y wince "...Cece...? Where are... "
    $ fadein_sideimage = False
    Y surprised "...Oh yeah, the library..."
    $ fadein_sideimage = True
    C blink "There's no sign of the zombie anywhere, but maybe we should wait until you're rested up before we move out."
    Y sad "Okay..."
    C default "....."
    Y surprised "...Aren't you going to sleep?"
    C smile "Hmm? I'm fine. It's best if one of us stays awake to keep watch."
    C blush "And Ria's completely knocked out on your shoulder there."
    Y thinking "Ria...?"
    window auto hide
    hide cecilia with dissolve
    scene bg library dark:
        xalign 1.0 yalign 1.0
        linear 2.0 xalign 0.0
    pause 3.0
    $ show_side_oriana = True
    O blink "{cps=6}..........{/cps}"
    $ show_side_oriana = False
    I "...Oh, it's true. How did I not notice her head on my shoulder...?"
    $ _last_say_who = "C"
    show bg library dark left
    show cecilia thinking at mycenter
    with dissolve
    C "I'm guessing you're also tired from time traveling a ton?"
    Y surprised "Huh?"
    C default "Remember? You were out cold almost right after this whole thing started."
    C blink "The killing game starts, you suddenly say you're a time traveler, ask a bunch of questions, then nighty night!"
    Y sad "Right..." with hpunch
    I "That feels like such a long time ago now... But for her, it's only been a few hours..."
    C smile "Don't worry, just get some shut-eye~"
    C blush "I'll look out for the both of you. Promise."
    play ctc_sfx sfx_heartbeat_single
    Y shocked "...!" with shakeshort
    $ fadein_sideimage = False
    Y "....."
    Y depressed "...I..." with shakeonce
    Y "....."
    play ctc_sfx "<silence 1.0>"
    Y troubled "{cps=6}...I'm...{/cps} ...I'm sorry." with shakeonce
    $ fadein_sideimage = True
    C surprised "Huh? For what?"
    Y shadow2 "I was...suspicious of you..."
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    Y "When Ria jumped in the hatch...and I got stabbed in the back..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y pained2 "...I thought it was you." with shakeonce
    $ fadein_sideimage = True
    C "....."
    play ctc_sfx sfx_emotesigh
    C sweatdrop "Oooh, you're talking about {i}before{/i} you time traveled? Uhh... I'm not sure I fully get what you're saying." with hpunch
    C thinking "I mean, there were definitely many, MANY times I tried to kill you and Ria, weren't there?"
    Y wince "No-- Yeah, I mean...{cps=1} {/cps}I'm talking about here, in the basement." with hpunch
    scene bg foyer at grayscale_on
    show oriana_raw sideeye at myleft, grayscale_on, backedaway_on
    show cecilia_raw happy at myright, grayscale_on, backedaway_on
    with dissolvemed
    Y sad "Each time, the three of us would come down here. Each time, we would promise each other we'd escape this place together."
    scene bg basement hatch at grayscale_on
    with dissolvemed
    Y wince "But the moment I saw that hatch, I..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    show bg black with custom_flashquick()
    Y troubled "I suddenly remembered everything. Every time something went horribly wrong near that hatch." with shakeonce
    Y shocked "Like, if I jumped in, I...I would get swallowed up in flames.{cps=1} {/cps}And Ria would...confront someone for tricking us..."
    $ show_side_cecilia = True
    C surprised "Huh? [t_clue]Flames[t_cluee]?"
    Y pained2 "But if Ria jumped in, I would get stabbed in the back..." with shakeonce
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene bg library dark left
    show cecilia thinking at mycenter
    with dissolveslow
    C "....."
    Y wince "I didn't know that corpse could move yet, so..."
    $ fadein_sideimage = False
    Y "So I thought... Maybe..." with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    C blink "...That I was [t_clue]betraying[t_cluee] you and Ria, right?"
    Y shadow2 "....."
    C "For what it's worth, I don't think you were wrong to suspect me."
    C thinking "You know how I am, as well as what I've done in alternate futures."
    C sweatdrop "And also, there's no way anyone could've expected the corpse would stand up and try to kill us."
    Y sad "Even so, I... I should've trusted you..." with shakeonce
    $ fadein_sideimage = False
    Y default "You risked your life to save us from that...thing. So...thank you."
    Y happy "Thank you so much."
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    C surprised "...! ....." with shakeonce
    C "......."
    C thinking "I-I don't know how to respond to something like that..."
    C sweatdrop "Y-you're welcome...?" with shakeonce
    Y surprised "....."
    C sad "No, seriously, I can't, I-- I-I don't know how to handle a situation like this." with shakeonce
    Y relaxed "It's fine. I just needed to say that."
    C blush "O-okay, good! I heard you loud and clear! Ahaha..." with shakeonce
    C smile "You can go ahead and get some sleep now. Again, I can keep watch."
    I "...Yeah..."
    I "It might be good to get some rest..."
    I "...Unless...{w=0.5} Do I want to talk with Cece a little longer...?" with hpunch
    $ show_choicegrand = True
    menu:
        "Keep talking with Cece":
            $ show_choicegrand = False
            call d2a3_library_cece_hearttoheart
        "Stop talking with Cece":

            $ show_choicegrand = False
            I "...No. I think I've said all I need to say."
            Y relaxed "...All right. I think I'll get some more sleep."
            C blush "Sure. Good night, [name_player]~"

    scene bg black with dissolveslow
    I "Time's running out... I wonder what's supposed to happen when it does?"
    I "Is the culprit going to emerge and kill us all? Or..."
    I "...Maybe...whatever caused that fire in the underground passage..."
    I "...or some other thing related to the occult will happen and erase us all..."
    I "Anything is possible now. I mean, [t_clue]I'm dead[t_cluee]. I shouldn't even be around anymore, and yet here I am."
    I "...What's the purpose of this killing game? Why are we here?"
    I "....."
    play ctc_sfx "<silence 1.0>"
    I "...So tired..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}The answers...{/cps}{w=0.5} [t_clue]I'll find all of them[t_cluee]...{w=0.5} When I...wake...{size=-10}up...{/size}"
    play ctc_sfx "<silence 1.0>"
    stop music fadeout 5
    I "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolveslow
    jump day2_end

label d2a3_library_cece_hearttoheart:
    Y blink "...Actually, Cece, there's something I wanted to ask you about."
    C default "Hmm? What is it?"
    Y sad "The time I found Ria dead in the lounge, just before I was about to go back in time..."
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotequestion
    Y default "...You told me to remember a [t_clue]sentence[t_cluee]."
    $ fadein_sideimage = True
    C thinking "Huh? A sentence?"
    Y thinking "Yeah, the sentence was... Uh... How did it go...?{nw}"
    $ fadein_sideimage = False
    $ d2a3_library_cece_sentence = ""

    menu:
        extend ""
        "\"Selena...\"":
            Y "\"Selena...\"{nw}"
        "\"Serena...\"":
            $ d2a3_library_cece_sentence = d2a3_library_cece_sentence + "A"
            Y "\"Serena...\"{nw}"
        "\"Serene...\"":
            Y "\"Serene...\"{nw}"
        "\"Celene...\"":
            Y "\"Celene...\"{nw}"

    menu:
        extend ""
        "\"...killed...\"":
            $ d2a3_library_cece_sentence = d2a3_library_cece_sentence + "B"
            Y "\"...killed...\"{nw}"
        "\"...grilled...\"":
            Y "\"...grilled...\"{nw}"
        "\"...spilled...\"":
            Y "\"...spilled...\"{nw}"
        "\"...chilled...\"":
            Y "\"...chilled...\"{nw}"

    menu:
        extend ""
        "\"...the monkfish.\"":
            Y "\"...the monkfish.\""
        "\"...the koi fish.\"":
            Y "\"...the koi fish.\""
        "\"...the goldfish.\"":
            Y "\"...the goldfish.\""
        "\"...the clownfish.\"":
            $ d2a3_library_cece_sentence = d2a3_library_cece_sentence + "C"
            Y "\"...the clownfish.\""
    $ fadein_sideimage = True
    if d2a3_library_cece_sentence == "ABC":
        play ctc_sfx sfx_heartbeat_single
        C surprised "...! That's..." with shakeshort
        Y surprised "As promised, I memorized it, but I'm not sure what it means..."
    else:
        C sad "Hmm...? That sounds kinda familiar..."
        Y worried2 "Yeah, I might have gotten a part of it wrong. Or maybe all of it."
        C surprised "...Wait."
        play ctc_sfx sfx_emotequestion
        C "[t_clue]\"Serena killed the clownfish.\"[t_cluee] Was that the sentence?"
        Y panicked "Y-yeah, that was it!" with shakeonce

    C surprised "....."
    Y thinking "I guess this was something the Cece from another timeline just randomly came up with, huh?"
    C thinking "No. I know why that Cece told you that."
    Y surprised "Huh?"
    play ctc_sfx "<silence 1.0>"
    play music bgm_discussion
    $ show_music_info_timer = music_info_pop_out_time()
    C default "[name_player]. You were just about to travel back in time, right?"
    Y thinking "Y-yeah...?"
    C blink "\"Serena killed the clownfish.\"{w=1.0} That's a [t_clue]secret I've never told anyone[t_cluee], not even family."
    Y panicked "What?! Then..." with shakeonce
    C default "Yup. That Cece was trying to [t_clue]test something[t_cluee]. And I think I know what."
    Y leering "Wh-what is it?" with shakeonce
    C thinking "Um..."
    C sweatdrop "...Are you sure you wanna know? It might make things...tricky for you.{nw}"

    menu:
        extend ""
        "\"Yes, tell me.\"":
            Y leering "Cece, please tell me. What were you trying to test by telling me that secret?"
            C blink "Now, of course, I can't be 100%% sure, but I think that other Cece was trying to test two things."
            C default "First, she was testing [t_clue]me[t_cluee]. The current Cece."
            Y thinking "What? How?"
            C thinking "By having you tell me a secret no one could possibly know about, she's testing if I [t_clue]remember[t_cluee] telling you that secret."
            Y panicked "...Wait, what? But aren't you two different Ceces?" with shakeonce
            C "...No. It turns out her theory was correct."
            C default "It's very faint, but I do vaguely [t_clue]remember telling someone that secret[t_cluee]."
            C blink "Which then tested and confirmed the second thing."
            C smug "She was testing the [t_clue]nature[t_cluee] of your time travel power."
            Y worried "The...\"nature\" of my time traveling?" with hpunch
            C sweatdrop "Hmm... Your oblivious expression tells me you're not familiar with the time travel tropes so commonly explored in sci-fi stories."
            C default "Okay, think of it this way. Let's say you go back in time because Ria died, but I'm still alive."
            C "What do you think happens to the dead Ria and the still-alive me AFTER you travel back?{nw}"
            menu:
                extend ""
                "\"You continue on.\"":
                    Y sad "...Wouldn't you still live on? And Ria would still be dead..."
                    C blink "So I would escape through the front door, right?"
                    Y blink "I guess so, yeah."
                    C default "But then what about you?"
                    Y surprised "Me? Didn't I--"
                    C smile "Yes, \"you\" went back in time. But what about your body?"
                    Y thinking "{cps=6}.....{/cps} {nw}"
                    $ fadein_sideimage = False
                    play ctc_sfx "<silence 1.0>"
                    extend panicked "Oh! Wait, no, I guess only my [t_clue]mind[t_cluee] travels back, since I always wake up in my sleeping body." with hpunch
                    $ fadein_sideimage = True
                    C happy "Exactly! So what do you think happens to your old body, still stuck in the future?"
                    Y thinking "Uh... It either lives on without a mind, or..."
                    $ fadein_sideimage = False
                    Y surprised "Wait, does it become another \"me\"?"
                    $ fadein_sideimage = True
                    C smile "That would be the [t_clue]multiple timeline theory[t_cluee], yes."
                    C blink "If your time traveling was of this type, that would mean that every single time any of us died..."
                    C "...that person [t_clue]stayed dead[t_cluee] in that timeline, and all you're doing is jumping around until you find an optimal outcome."
                    Y thinking "...\"If\"? So... What I'm doing is NOT that?"
                "\"You get rewound.\"":
                    Y thinking "Wouldn't you...um...rewind? Like, your bodies and minds get pulled back to their original states?"
                    C surprised "Interesting... So it'd be like every single millisecond, our current states get saved to the universe's save cloud?"
                    play ctc_sfx sfx_emotehappy
                    show cecilia happy at hop
                    C "That'd be like we're living inside a [t_clue]video game[t_cluee] or something!"
                    Y worried "Uh... I think you lost me..."
                    C blink "That's not too far off, actually. The main distinction is that our minds seem to be retaining some of the information."
                "\"You get erased.\"":

                    Y thinking "...I mean, if that future no longer happened, then the two of you at that moment would vanish, right?"
                    C sweatdrop "That's a scary thought... I guess as long as at least one instance of us exists, huh...?"
                    C blink "But no, that can't be what's happening because I remember my other self telling you that secret."
                    Y surprised "Right... So what does that mean?"

            C default "Simply put, it's not fully accurate to call yourself a time \"traveler\"."
            C blink "What you're actually doing is...{w=1.0}{nw}"
            play ctc_sfx "<silence 1.0>"
            $ renpy.music.set_volume(0.0, 0, channel="music")
            extend smile "[t_clue]forcibly pulling the world backwards in time[t_cluee]." with shakeonce
            $ renpy.music.set_volume(1.0, 3, channel="music")
            C blink "And it's an imperfect power because information from the rewound future is [t_clue]leaking into the past[t_cluee]."
            Y shocked "Pulling...the world? Like, the \"world\" world? Including everything outside of this house?" with shakeonce
            C thinking "It's possible. We have no means of communicating with the outside world."
            C smug "For all we know, there's chaos and pandemonium from people suddenly being able to predict the future."
            C "Cheating the lottery, committing perfect murders, maybe even seeing visions of the apocalypse..."
            play ctc_sfx "<silence 1.0>"
            Y afraid "Then... Every time I \"went back in time\"... I..." with hpunch
            C sweatdrop "Yeah... See, this is why I wasn't sure if I should tell you."
            C thinking "But remember, nothing is confirmed. Not until we can go outside and see for ourselves."
            Y shadow "....."
            I "...No." with hpunch
            I "She's right... Nothing's confirmed..."
            C default "....."
        "\"Actually, never mind...\"":

            Y blink "...No. Never mind, I guess it's not important."
            $ fadein_sideimage = False
            Y sad "From the way you're describing it, it sounds like it won't be very useful information, huh?"
            $ fadein_sideimage = True
            C blink "Not at all. But... I sense that you'll eventually find out about it in due time regardless..."
            Y surprised "...?"

    stop music fadeout 3.0
    C happy "Anyway, wow, what a blabbermouth, spilling a girl's secrets like that!"
    Y sad "...Um..."
    C surprised "Oh wait, I guess that blabbermouth was me, huh?"
    Y default "What does it mean, though? Who's Serena? And what's a clownfish?"
    C sweatdrop "R-really? You really want to invade a girl's privacy even more?"
    Y thinking "I mean, if you really don't want to talk about it..."
    C default "....."
    C blink "Eh. It's fine. This story is over ten years old now anyway."
    play ctc_sfx "<silence 1.0>"
    play music bgm_origin_chaos
    scene bg black with dissolveslow
    C "When I was in the 3rd grade, our class had some pet fish. One clownfish, three goldfish, and a...guppy. I think."
    C "It was a way of teaching us kids how to take care of a living thing. You know, all the good reasons."
    C "The teacher had us take care of each fish in pairs. We'd rotate the pairs every week."
    scene cg origin cecilia:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 10.0 zoom 1.0
    with dissolveslow
    C "One week, it was my turn to take care of the clownfish with this girl named [t_clue]Serena[t_cluee]."
    C "Serena was popular. She was always surrounded by boys and girls alike. And she was great at handling them all."
    C "I didn't dislike her either. She didn't let her popularity inflate her ego or anything."
    window auto hide None
    play ctc_sfx sfx_heartbeat_single
    $ renpy.music.set_volume(0.25, 0, channel="music")
    show cg origin cecilia1:
        xalign 0.5 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.1
    with custom_flash()
    show cg origin cecilia:
        xalign 0.5 yalign 0.5 zoom 1.1
    with dissolve
    $ renpy.music.set_volume(1.0, 1, channel="music")
    pause 1.0
    scene cg origin cecilia at grayscale_on:
        matrixcolor BrightnessMatrix(-0.5)
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 20.0 zoom 1.0
    with dissolvemed
    C "Anyway, yeah, that week, [t_clue]Serena killed the clownfish[t_cluee]."
    C "Gave it the wrong food. Couldn't digest it. Went belly-up overnight."
    C "Of course, it was an accident, but..."
    scene cg origin cecilia2:
        xalign 0.5 yalign 0.0 zoom 1.25
        linear 20.0 zoom 1.0
    with dissolvemed
    C "The next day in class, there was an uproar. A lot of eyes were glaring at Serena, who was witnessed feeding it the previous day."
    C "Oh, I should explain that I wasn't the most conspicuous child. My hair was much shorter. And not dyed. Still fluffy, though!"
    C "Anyway, Serena was kind of in a pinch because of what happened the previous day."
    C "I don't think anyone noticed I was there, but a couple of the boys were fooling around with the food dispensers."
    C "That's probably how she ended up feeding the clownfish the wrong food. But what was she going to do, finger all of those boys?"
    C "She stayed completely silent while the teacher kept on asking her what happened."
    scene cg origin cecilia3:
        xalign 0.5 yalign 0.0 zoom 1.1
        easein 5.0 zoom 1.75
    with dissolvemed
    pause 1.0
    C "...And then, being the clueless child that I was, I walked up to the clownfish tank and said the following:"
    play ctc_sfx "<silence 1.0>"
    $ renpy.music.set_volume(0.0, 0, channel="music")
    show bg black with custom_flashquick()
    C "{cps=15}\"Whoa... Its eyes are all gray and blotchy! Dead things are pretty...\"{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ persistent.unlock_cg_origin_cecilia = True
    scene cg cece hearttoheart:
        xalign 1.0 yalign 0.0 zoom 1.4
        easein 20.0 zoom 1.0
    with dissolveslow
    $ renpy.music.set_volume(1.0, 3, channel="music")
    $ show_side_cecilia = True
    Y surprised "....."
    $ fadein_sideimage = False
    C blink "...It was my first time ever seeing a dead thing. My first encounter with death, and I was captivated by it."
    C default "As you may have predicted, everyone was grossed out, the teacher included."
    C blink "Some boy yelled out that I must have killed the clownfish, and then...that became the truth."
    Y shouting "Wha... But you were innocent!" with shakeonce
    C thinking "{i}Was{/i} I? I mean, for an eight-year-old, that was a pretty twisted thing to say."
    Y angry "No, I mean, you didn't kill the clownfish! Didn't you defend yourself?!" with shakeonce
    C happy "Nope. I didn't really care. I was more concerned with being able to take the dead clownfish home. Boy, the teacher got maaad~"
    Y default "....."
    play ctc_sfx "<silence 1.0>"
    Y blink "...You did it to protect Serena, didn't you? That's why you never told anyone until today."
    C thinking "Hmm... Sorry, that doesn't sound right. I liked Serena, but not enough to wanna protect her. We weren't really friends."
    Y sad "Then why didn't you say anything? Didn't the other kids hate you for the rest of the year?"
    C happy "For the rest of elementary school, yep!" with vpunch
    Y panicked "How are you able to say that so cheerfully? Wasn't it difficult for you?"
    C sweatdrop "Difficult... Mrgh... I don't know, [name_player], elementary school was the earliest years of my fascination with the occult."
    C happy "I can confidently say that I only have [t_clue]happy memories[t_cluee] of my time there as a result of that."
    Y sad "...Did you...not make any friends...?"
    C blink "....."
    C thinking "...Hmm?{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend surprised " Oooh. Wait, [name_player], I think maybe that was why I didn't say anything about Serena."
    C default "When she was almost forced to betray her friends, she was deep in despair."
    C "Even someone like me could tell that the opinions of other people meant the whole world to her."
    C sad "And somehow... It felt like it'd be a waste to see everything she'd built up crumble so easily. I...didn't want to see that."
    C smile "People should be allowed to hold on to the things they care about the most, you know?"
    Y surprised "....."
    play ctc_sfx sfx_emotesigh
    C sweatdrop "Gosh, I've never talked this much about myself before... [name_player], you're a real smooth operator, huh?" with hpunch
    Y default "{cps=6}.....{/cps} Cece...{w=0.5}{nw}"

    menu:
        extend ""
        "\"You're a good person after all.\"":
            Y relaxed "You're a good person after all."
            C surprised "Hm? Where's this coming from?"
            Y blink "The way you talk about yourself...and your past self..."
            Y default "It feels like you don't have the nicest things to say about either of them."
            C sweatdrop "Ahaha... I get what you mean, but it's not like I have low self-esteem or anything." with hpunch
            C blink "I'm just giving a description of how general society views someone like me."
            Y leering "But you protected Serena."
            C thinking "Maybe, but it wasn't out of heroism or friendship or some civic duty..."
            C sweatdrop "Frankly, it was just because it was the easiest choice to make. Imagine trying to convince a class of children that--"
            Y blink "You just said that you recognized Serena's friends were important to her."
            C surprised "....."
            Y "You kept this secret for so long because you wanted to protect something that some kid cared about."
            Y relaxed "Some kid who wasn't even your friend."
            Y happy "I think being able to even recognize the things that matter to other people proves your humanity."
        "\"You really are a weirdo.\"":
            Y confused "You really are a weirdo." with hpunch
            play ctc_sfx sfx_emotehappy
            C happy "Ahaha! Guilty as charged!" with vpunch
            Y relaxed "You still don't realize it, huh?"
            C surprised "Heh?"
            Y blink "You genuinely believe that you protected Serena on a whim. Like, it meant nothing to you."
            C thinking "I mean, again, it's not my strongest memory of elementary school, let alone my happiest."
            Y default "But you recognized what mattered the most to Serena, a girl who wasn't even your friend."
            Y thinking "And with that information in mind, what did you do? You chose to keep this secret for over ten years."
            C surprised "....."
            Y relaxed "Sure, maybe you don't consider those dots to be connected, but anyone with the slightest shred of humanity would tell you..."
            Y happy "...You did a really good thing. Regardless of your intentions, the outcome was that your actions saved that girl."

    play ctc_sfx "<silence 1.0>"
    C blink "{cps=6}.....{/cps} ...Heh..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    scene cg cece hearttoheart2 with dissolve
    C happy "Ahahahahahahaha~" with vpunch
    $ fadein_sideimage = False
    Y panicked "Wh-what's so funny?" with shakeonce
    C blink "Hee hee... It's nothing. It's just... \"Humanity\" was an interesting word for you to say right now..."
    Y worried "I...don't understand..." with hpunch
    C wink "You don't have to just yet, [name_player]."
    C blush "But thanks. I'm glad we were able to have this talk."
    Y relaxed "...Yeah."
    $ fadein_sideimage = True
    scene cg cece hearttoheart2:
        xalign 0.5 yalign 0.0 zoom 1.1
        easein 10.0 zoom 1.3
    with dissolve
    I "Cece... Maybe you don't have the greatest track record with forming human connections..."
    I "But your heart's in the right place. You have a lot to offer to the world..."
    I "...There's no way your story should end here." with shakeonce
    Y relaxed "I'm counting on you, Cece. Let's get out of here alive."
    $ fadein_sideimage = False
    Y happy "All of us, together."
    C smile "...\"Together\", huh?"
    C blush "Yeah, that sounds like fun!"
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    $ persistent.unlock_cg_cece_hearttoheart = True
    $ seen_cece_hearttoheart = True
    return

label day2_end:
    pause 3.0
    show screen lock_hotkeys
    $ quick_menu = False
    pause 3.0
    scene cg eyecatch oriana bloody:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 3.0 zoom 1.0
    with dissolvemed
    pause 1.0
    scene cg eyecatch oriana with dissolvemed
    show chaptertitle2_end_text:
        xpos 550 xanchor 0.5 yalign 0.5 alpha 0.0 zoom 1.0
        linear 1.0 alpha 1.0
    show chaptertitle2_end_subtext:
        xpos 550 xanchor 0.5 yalign 0.57 alpha 0.0
        linear 1.0 alpha 1.0
    pause 4.0
    scene bg black with dissolveslow
    pause 1.0
    hide screen lock_hotkeys
    $ quick_menu = True

    S "Continuing [name_player]'s [t_clue]killing game[t_cluee] to {color=#fff}Part III{/color}.{w=1.0}\nPlease remember to save your progress regularly.{nw}"

    menu:
        extend ""
        "Continue":
            window auto hide
            $ renpy.block_rollback()
            show screen lock_hotkeys
            $ quick_menu = False
            $ music_info = False
            pause 2.0
            scene cg eyecatch empty at wobble
            show chaptertitle3_text:
                xpos 960 xanchor 0.5 yalign 0.45 alpha 0.0 zoom 1.0
                pause 3.0
                parallel:
                    linear 1.0 alpha 1.0
                parallel:
                    linear 1.5 matrixcolor BrightnessMatrix(0.0)
                    linear 1.5 matrixcolor BrightnessMatrix(0.5)
                    repeat
            show chaptertitle3_subtext:
                xpos 960 xanchor 0.5 yalign 0.55 alpha 0.0
                pause 3.0
                parallel:
                    linear 1.0 alpha 1.0
                parallel:
                    linear 1.5 matrixcolor BrightnessMatrix(0.0)
                    linear 1.5 matrixcolor BrightnessMatrix(0.5)
                    repeat
            with blot_in_slow
            pause 4.0
            scene bg black with dissolveslow
            pause 1.0
            stop sound
            hide screen lock_hotkeys
            $ quick_menu = True
            $ music_info = True
            jump d3a1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
