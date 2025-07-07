

label d3a1:
    $ renpy.block_rollback()
    call save_file_name_update (3, "d3a1")
    $ show_side_player = True
    $ fadein_sideimage = True
    scene bg black with dissolveslow
    I "....."
    X "...mm..."
    X "[u_music_note]~ ...Hmm~ [u_music_note]" with hpunch
    I "....... ...Nrgh..." with shakeonce
    I "Singing...again...?"
    $ _last_say_who = "C"
    scene bg library right
    show cecilia blink at mycenter
    with dissolveslow
    C smile "Oh! [name_player], you're awake?"
    Y wince "...Cece? Where...?" with hpunch
    I "...Oh yeah. We were hiding from that zombie..."
    C grin "Pftft~" with vpunch
    Y thinking "...? What's so funny? Is there drool on my face?" with hpunch
    C blink "No no, it's just..."
    C smile "Have you noticed that every single time you woke up here..."
    C blush "...I'm always the first one to notice and greet you? It's a pretty funny coincidence."
    Y surprised "...Huh... I guess that's true..."
    C thinking "Anyway, I think the coast is clear now. I took a peek through the door, but I couldn't see the zombie."
    Y sad "You think he went upstairs?"
    C sad "Maybe... But there's also the chance that he's camped out next to the door, waiting for us to open it."
    Y troubled "....." with shakeonce
    C determined "What do you wanna do? Should we wait a little longer?"
    Y wince "W-wait... Where's Ria?" with hpunch
    scene bg library right with dissolve
    scene bg library:
        xalign 1.0 yalign 1.0
        linear 1.0 xalign 0.0
    pause 1.5
    $ show_side_oriana = True
    O shadow "{cps=6}..........{/cps}"
    $ show_side_oriana = False
    $ fadein_sideimage = False
    play ctc_sfx sfx_heartbeat_single
    Y shocked "W-wait, is she...?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    $ _last_say_who = "C"
    scene bg library left
    show cecilia surprised at mycenter
    with dissolvequick
    C "No no no, she's still breathing!" with hpunch
    Y depressed "Ah... G-good..." with shakeonce
    C sad "We probably want to [t_clue]get her wound cleaned[t_cluee] and into a [t_clue]proper bed[t_cluee] as soon as we can."
    C determined "Even if it's risky, we need to leave this room and get upstairs."
    I "....."
    I "She's right. There's no getting around it."
    Y blink "Okay. We'd better move."
    C thinking "Ria's still kinda conked out so one of us will have to [t_clue]carry her[t_cluee]."
    C default "You decide, [name_player]. Who should carry Ria?{nw}"

    menu:
        extend ""
        "\"I'll do it.\"":
            Y leering "We need you ready with your knife. The zombie could ambush us at any point on our way up."
            C smile "Sounds good. I won't let him get close to either of you."
        "\"You do it.\"":
            Y blink "I'll go up front and keep an eye out. I can always turn back time if things get bad, after all."
            C blink "Good point. Okay, you can leave Ria to me."
    window auto hide
    hide cecilia with dissolve
    I "Okay... First step is to move this dresser out of the way."
    scene bg black with dissolvemed
    play sound sfx_furnituredrag volume 0.5
    with hpunch
    I "Nrgh... Does this have to make so much noise...?" with shakeonce
    $ show_side_cecilia = True
    C determined "Are you ready for this, [name_player]?"
    $ fadein_sideimage = False
    Y wince "As ready as I'll ever be..."
    $ fadein_sideimage = True
    I "...Okay. Let's [t_clue]open the door[t_cluee]...{nw}"
    menu:
        extend ""
        "Open it now":
            I "No time to waste. Let's move out." with hpunch
        "Wait a moment first":
            I "{cps=6}.....{/cps}"
            C determined "{cps=6}.....{/cps}"
            I "{cps=6}.....{/cps}"
            I "Okay, I still don't hear anything. Let's try opening it now..."
    $ show_side_cecilia = False
    scene bg black with dissolveslow
    play sound sfx_dooropenslow_unlatch
    with shakeonce
    play sound2 ["<silence 2.0>", sfx_dooropenslow_move]
    pause 3.0
    scene bg basement nocorpse:
        xalign 0.0 yalign 0.5 zoom 1.15 matrixcolor BrightnessMatrix(-0.5)
        easein 10.0 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    with dissolvemed
    pause 5.0
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y surprised "...I don't see the zombie anywhere..."
    play ctc_sfx "<silence 1.0>"
    $ _last_say_who = "C"
    show cecilia thinking at mycenter with dissolve
    C "The chair's empty too... Guess that's not like his charging station or something..."
    Y thinking "Okay, let's take a look at the stairs."
    play ctc_sfx "<silence 1.0>"
    I "Carefully now..."
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolveslow
    pause 0.5
    scene bg basement stairway:
        xalign 0.5 yalign 0.0 zoom 1.15 matrixcolor BrightnessMatrix(-0.5)
        easein 10.0 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    with dissolveslow
    pause 2.5
    $ persistent.unlock_bg_basement_stairway = True
    I "The door to the lounge is upstairs..."
    I "Er, wait, did we close the door behind us when we came down here? I can't even remember anymore..." with hpunch
    $ show_side_cecilia = True
    C thinking "[name_player]. I don't hear any footsteps up there. It's possible he's in another room."
    $ fadein_sideimage = False
    C determined "We should [t_clue]move quickly[t_cluee] while we can. If he comes back now, then our only way up will be blocked off."
    $ fadein_sideimage = True
    $ show_side_cecilia = True
    I "She has a point... But I'm still nervous...{nw}"
    menu:
        extend ""
        "Move up quickly":
            Y leering "Yeah, we can't afford to get stalled here. Let's pick up the pace." with hpunch
            play ctc_sfx "<silence 1.0>"
            play sound sfx_steps_ladderfast
            scene bg basement stairway:
                xalign 0.5 yalign 0.0 zoom 1.0
                linear 5.0 zoom 2.0
            pause 1.0
            scene bg black with dissolve
            pause 1.0
            scene bg basement entrance light with dissolvemed
            pause 2.0
        "Move up slowly":
            Y blink "No, we can't risk making any noise. Let's climb up these steps carefully."
            play ctc_sfx "<silence 1.0>"
            play sound sfx_steps_ladder volume 0.5
            scene bg basement stairway:
                xalign 0.5 yalign 0.0 zoom 1.0
                linear 10.0 zoom 1.2
            pause 1.0
            scene bg black with dissolveslow
            pause 2.0
            scene bg basement entrance light with dissolvemed
            pause 2.0
    $ persistent.unlock_bg_basement_entrance_light = True
    $ show_side_cecilia = False
    scene bg lounge with dissolvemed
    pause 1.0
    I "{cps=6}.....{/cps}"
    Y blink "Looks like the coast is clear..."
    $ _last_say_who = "C"
    scene bg lounge
    show cecilia thinking at mycenter
    with dissolve
    C "Hmm... All these [t_clue]tears in the wallpaper[t_cluee]..."
    C grin "I wonder if that zombie is the culprit behind them. Probably thrashed around, chasing and clawing at its prey..."
    Y thinking "....."
    C surprised "Huh? Where's your retort, [name_player]?"
    Y "It's just...if that's true..."
    play ctc_sfx sfx_emotequestion
    $ fadein_sideimage = False
    Y "I wonder why the zombie would suddenly [t_clue]start using a knife[t_cluee]? These tears are clearly made by some other thing."
    $ fadein_sideimage = True
    C sad "It wasn't a serious theory, [name_player]..."
    C thinking "Hmm... But if I can board this train of thought anyway, maybe...the zombie learned how to use tools?"
    Y blink "No... I think there's more to that \"zombie\"..."
    play ctc_sfx "<silence 1.0>"
    C surprised "Ah...!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y afraid "...!! I-is it behind me...?!" with shakeshort
    play ctc_sfx sfx_whooshlow
    scene bg basement entrance light
    show dog at mycenter
    with custom_flashquick()
    with shakelong
    pause 1.5
    Y shocked "...Oh. It's just [name_dog]..."
    I "That scared the crap outta me..." with hpunch
    D "....."
    $ show_side_cecilia = True
    C thinking "...Huh?"
    $ fadein_sideimage = False
    C determined "[name_player]. Maybe you should take a step back from him."
    Y worried "What? Why? We already know he's friendly."
    C sad "I-I dunno, I can't explain it, but..."
    play ctc_sfx sfx_heartbeat_single
    C injured "I'm just...getting a [t_clue]really bad feeling[t_cluee] from him..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y shocked "....."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    I "...Wait a minute. What's this dog been up to this whole time anyway?"
    I "The last I saw him, he was hanging around in this lounge..."
    play ctc_sfx sfx_whoosh
    play sound sfx_dogsteps
    hide dog
    with custom_flashquick()
    Y afraid2 "AHH!! W-wha...?!" with shakeshort
    I "He ran off..."
    $ show_side_cecilia = False
    scene bg lounge
    with dissolvemed
    $ _last_say_who = "C"
    show cecilia determined knife at mycenter
    with dissolve
    pause 1.0
    C "{cps=6}.....{/cps}"
    Y panicked "C-Cece, why are you...?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    C "{cps=6}.......{/cps}"
    play ctc_sfx sfx_knifeequip
    C sad "...I just DON'T get it... What is this...?" with hpunch
    play ctc_sfx "<silence 1.0>"
    C thinking "Maybe...a [t_clue]memory[t_cluee]...?"
    Y shocked "...Cece?"
    C surprised "Oh! I-it's nothing, [name_player]!" with hpunch
    C determined "Let's get to the foyer. If the zombie comes back now, we'd have to backtrack into the basement."
    Y surprised "....."
    C pout "[name_player]! Come on!" with shakeonce
    Y sad "Y-yeah, let's move."
    scene bg black with dissolvemed
    I "{cps=6}.....{/cps}"
    I "The door is already slightly open. And I don't hear any sounds coming from the foyer."
    I "We need to [t_clue]open this door[t_cluee]...{nw}"
    menu:
        extend ""
        "Open it now":
            I "Wait, once we're in the foyer, we have some room to run around."
            I "As long as we're ready for an ambush, we should be fine..." with hpunch
        "Wait a moment first":
            I "{cps=6}.....{/cps}"
            $ show_side_cecilia = True
            C sad "{cps=6}.....{/cps}"
            $ show_side_cecilia = False
            I "{cps=6}.....{/cps}"
            I "Okay, I still don't hear anything. Guess the zombie isn't in the foyer..."
    Y leering "Okay, Cece, I'm pushing open the door."
    window auto hide
    pause 2.6
    play sound ["<silence 2.0>", sfx_dooropenslow_move]
    pause 3.0
    scene bg foyer:
        xalign 0.3 yalign 0.5 zoom 1.15 matrixcolor BrightnessMatrix(-0.5)
        easein 10.0 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    with dissolvemed
    pause 3.0
    I "{cps=6}.....{/cps}"
    stop sound
    I "Okay, we're almost there..."
    $ _last_say_who = "C"
    show cecilia sad at mycenter with dissolve
    C "How're you holding up, [name_player]? I say this with love, but you don't exactly have the sturdiest heart for this sorta thing."
    Y wince "I'm fine... We're almost to our goal anyway." with hpunch
    C thinking "Hmm... If you say so, then."
    C determined "Just don't let your guard down. Mistakes tend to happen the moment you get [t_clue]overconfident[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    Y shadow2 "....." with shakeonce
    I "Yeah, don't break focus... Just one last step..."
    scene bg foyer with dissolve
    $ day3_checked_kitchen = False
    $ day3_checked_bathroom = False

label d3a1_foyer_start:
    show bg foyer
    I "Let's see... Where should I go?"
    menu:
        "Go to the [t_clue]Kitchen[t_cluee]" if day3_checked_kitchen == False:
            I "I might as well join Cecilia in the kitchen."
            I "It'd be nice if I can find something to eat too..."
            $ show_side_cecilia = True
            C surprised "H-huh?! [name_player]?!" with shakeshort
            $ show_side_cecilia = False
            play ctc_sfx sfx_whooshlow
            show cecilia pout at mycenter with shakeshort
            C "Why are you going to the kitchen?!"
            Y panicked "I-I, uh..." with hpunch
            I "...Wait, what the heck am I doing?!" with shakeshort
            C sad "...What did I say about being overconfident?"
            Y wince "S-sorry, it's been a really long day." with hpunch
            C pout "This isn't the time to be [t_clue]fooling around on purpose[t_cluee], y'know!"
            Y worried "Right... Sorry..."
            scene bg foyer with dissolve
            I "Come on, don't go messing up now..." with hpunch
            $ day3_checked_kitchen = True
            jump d3a1_foyer_start
        "[u_check]Go to the [t_clue]Kitchen[t_cluee]" if day3_checked_kitchen == True:
            I "....."
            I "There's absolutely no reason for me to go to the kitchen right now..." with hpunch
            I "We need to [t_clue]get Ria's wound cleaned[t_cluee] and put her in a [t_clue]proper bed[t_cluee] as fast as we can."
            jump d3a1_foyer_start
        "Go to the [t_clue]Bathroom[t_cluee]" if day3_checked_bathroom == False:
            I "I guess I should go check out that bathroom."
            I "There probably isn't any way to escape there, but might as well see if there are any interesting clues."
            $ show_side_cecilia = True
            C surprised "W-wait! [name_player]!" with shakeshort
            $ show_side_cecilia = False
            play ctc_sfx sfx_whooshlow
            show cecilia pout at mycenter with shakeshort
            C "Why are you going to that bathroom?!"
            Y panicked "I-I, uh..." with hpunch
            C sad "I know we need Ria's wound cleaned, but if the zombie comes while we're in there, we'll be trapped."
            C determined "We should use one of the bathrooms [t_clue]upstairs[t_cluee]." with hpunch
            I "Right, that makes sense..."
            scene bg foyer with dissolve
            $ day3_checked_bathroom = True
            jump d3a1_foyer_start
        "[u_check]Go to the [t_clue]Bathroom[t_cluee]" if day3_checked_bathroom == True:
            I "....."
            I "...Cece's right, we should use one of the bathrooms [t_clue]upstairs[t_cluee]." with hpunch
            I "Besides, it'd probably be easier to use a [t_clue]shower[t_cluee] to clean Ria's wound while she's still unconscious..."
            jump d3a1_foyer_start
        "Go to the hallway [t_clue]Upstairs[t_cluee]":

            I "Right, going upstairs would be the best option."

    Y leering "Cece. We're going up."
    I "We should be in the clear now, as long as that zombie isn't on the second floor..."
    scene bg black with dissolveslow
    pause 1.5
    scene bg hallway:
        xalign 0.5 yalign 0.5 zoom 1.15 matrixcolor BrightnessMatrix(-0.5)
        easein 5.0 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    with dissolveslow
    pause 1.5
    I "{cps=6}.....{/cps}"
    play ctc_sfx sfx_heartbeat_single
    I "This is...going WAY too smoothly..." with shakeonce
    $ _last_say_who = "C"
    scene bg hallway
    show cecilia thinking at mycenter
    with dissolve
    C "Hmm... Ria's still unconscious, so if we're gonna clean her wound, it'd be best to use a [t_clue]showerhead[t_cluee]."
    C blink "And then if you need a good bed after... Yeah, you should take Ria to the [t_clue]master bedroom[t_cluee]."
    Y blink "Right, makes... {cps=6}.....{/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend panicked " ...W-wait, {i}I{/i} should take her? Where are {i}you{/i} going?" with shakeonce
    $ fadein_sideimage = True
    C thinking "I'm gonna check the [t_clue]attic[t_cluee] real quick. You said it was a blue book that had the page about the Gate to Hell, right?"
    Y surprised "...Y-yeah..." with hpunch
    I "That's right... I guess this version of Cece never got to check out the attic in detail..."
    Y sad "...Do you really need to go? What if the zombie corners you there?"
    C smile "Aww, [name_player]~ [u_heart] Are you worried about me...?"
    C happy "I'll be fine, I still have my knife with me."
    play ctc_sfx sfx_emotequestion
    C thinking "Besides, I have a [t_clue]theory[t_cluee] I wanna confirm about the strange things happening in this house."
    play ctc_sfx sfx_heartbeat_single
    C smug "And if I'm right, we'll know how to get out of here [t_clue]without killing anyone[t_cluee]." with shakeonce
    Y panicked "R-really?" with shakeonce
    C blink "Maybe. But I'll need to read through that book first to be sure."
    C default "Be sure to block the door with something, okay? I'll knock when I come back!"
    Y sad "Cece, I--" with hpunch
    play ctc_sfx sfx_steps
    scene bg hallway with dissolvemed
    Y shocked "Ah...!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    Y "....."
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "...I'd better hurry and clean Ria's wound..."
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolveslow
    call save_file_name_update (3, "d3a1_masterbedroom_alone")
    I "Okay, first, I gotta block the door."
    I "Let's see... This dresser should do the trick."
    window auto hide None
    play ctc_sfx "<silence 1.0>"
    play sound sfx_furnituredrag
    with shakeshort
    pause 5.0
    scene bg masterbedroom with dissolveslow
    I "...Okay, next is the wound..."
    play sound sfx_steps
    scene bg black with fade
    play sound2 sfx_dooropen
    pause 1.0
    scene bg masterbathroom with dissolvemed
    pause 1.0
    I "....."
    I "Let's get that cloth and her jacket off..."
    play sound sfx_clothrustle
    $ show_side_oriana = True
    O jacketless shadow "....." with shakeshort
    $ show_side_oriana = False
    I "Ugh... That's not a pretty cut..." with hpunch
    scene bg masterbathroom:
        xalign 0.2 yalign 0.5 zoom 1.2
        easein 0.5 zoom 1.4
    with dissolve
    pause 2.0
    play sound sfx_showeron
    with shakeonce
    scene bg black with dissolvemed
    $ renpy.music.set_volume(0.5, 0, channel="loop_sfx")
    play loop_sfx sfx_showerloop fadein 2.0
    pause 4.0
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "...It's no use... I can't help but worry about everything..." with hpunch
    I "Cece's alone in the attic again... Ria's still passed out..."
    I "And me... It's slow, but memories of my life are resurfacing."
    play ctc_sfx sfx_heartbeat_single
    I "I should be dead... So...[t_clue]am I a zombie too[t_cluee] or something...?" with shakeonce
    $ show_side_oriana = True
    O jacketless shadow "...gh..." with shakeonce
    $ show_side_oriana = False
    I "Ah-- Sh-she moved?" with shakeshort
    window auto hide
    play sound sfx_showeroff
    pause 0.5
    stop loop_sfx fadeout 1.0
    scene bg masterbathroom:
        xalign 0.2 yalign 0.5 zoom 1.4
    with dissolvemed
    pause 2.0
    $ renpy.music.set_volume(1.0, 1, channel="loop_sfx")
    I "{cps=6}.....{/cps}"
    I "No, she's still unconscious."
    Y sad "....."
    I "I hope this is enough to clean a wound. Now to dry her arm off and wrap it..."
    scene bg black with dissolveslow
    Y thinking "Hmm... What can I use here...?"
    $ fadein_sideimage = False
    Y surprised "Ah..."
    $ fadein_sideimage = True
    I "One of the towels Cece used after her shower."
    I "...I guess beggars can't be choosers. Sorry Ria, I'm gonna use this to dry and wrap up your wound..."
    play sound sfx_clothrustle volume 0.5
    I "....." with hpunch
    I "There... I think that should do it...?"
    play ctc_sfx "<silence 1.0>"
    I "....."
    play ctc_sfx "<silence 1.0>"
    Y shadow2 "....."
    play ctc_sfx "<silence 1.0>"
    I "...I haven't been alone like this for some time now..."
    play ctc_sfx "<silence 1.0>"
    I "I... I don't know what I'm doing..."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 2.0
    scene bg masterbedroom:
        xalign 0.0 yalign 0.25 zoom 2.0
        easein 10.0 zoom 1.75
    with dissolveslow
    pause 2.0
    I "{cps=6}.....{/cps}"
    I "All right, I got Ria into the bed, treated her wound, blocked the door..."
    I "...Guess there's nothing to do but wait until Cece gets back."
    I "....."
    scene bg masterbedroom:
        xalign 0.0 yalign 0.25 zoom 1.75
        easein 6.0 yalign 0.75
    with dissolve
    I "When will this end...?"
    I "Can we...really make this all end...?"
    play sound sfx_flashback
    scene bg diningroom dark at grayscale_on
    show cecilia blink at mycenter, grayscale_on
    with custom_flashbulblong()
    C blink "Another thing I noticed, in all your time travel tales, not a single one ends with {i}you{/i} being killed."
    C grin "Which begs the question: what happens if YOU die? Do you still go back in time?"
    I "....."
    C creepygrin "...Well, [name_player]? Aren't you just a teeny-tiny bit curious?"
    scene bg black with dissolvemed
    scene bg masterbedroom:
        xalign 0.0 yalign 0.75 zoom 2.0
        blur 0
        pause 2.0
        linear 10.0 blur 20.0
    with dissolvemed
    Y troubled "{cps=6}.....{/cps}"
    I "...I..." with shakeonce
    play ctc_sfx sfx_heartbeat_single
    I "...I'm in {color=#ff0000}Hell{/color}...aren't I...?" with shakeshort
    play ctc_sfx "<silence 1.0>"
    I "I'm already dead...{w=0.5} And yet, I can still experience the pain of being [t_clue]stabbed[t_cluee]...{w=0.5} Being [t_clue]burned alive[t_cluee]..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    I "And then... I get sent back in time to experience it all over again..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y pained2 "{cps=6}.....{/cps}" with shakeshort
    play ctc_sfx "<silence 1.0>"
    I "Someone... Anyone..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}Help me...{w=0.5} Please...{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ show_side_oriana = True
    O hidden "...[name_player]..."
    $ show_side_oriana = False
    $ fadein_sideimage = False
    show bg masterbedroom:
        xalign 0.0 yalign 0.75 zoom 2.0
        blur 0
    Y depressed "...!!" with shakeshort
    $ _last_say_who = "O"
    $ fadein_sideimage = True
    scene bg masterbedroom
    show oriana jacketless at mycenter
    with dissolveslow
    pause 2.0
    Y depressed "....."
    $ fadein_sideimage = False
    Y "...Ria..."
    $ fadein_sideimage = True
    O jacketless thinking "This is...the master bedroom... Did you bring me up here, [name_player]?"
    Y afraid2 "R-Ria? Ria, you're awake?" with shakeshort
    O jacketless surprised "Y-yes, I... I-I'm sorry I weighed you down earlier."
    Y shocked "....."
    O jacketless blink "...No. Scratch that."
    O jacketless thinking "You and Cece... You fought that monster and kept me safe, didn't you?"
    O jacketless relaxed "...Thank you. You saved my life."
    play ctc_sfx "<silence 1.0>"
    Y shadow "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    Y troubled "...Ri...a..." with shakeshort
    $ fadein_sideimage = True
    play ctc_sfx sfx_fallsoft
    scene bg black with vpunch
    $ show_side_oriana = True
    O jacketless panicked "Ah! [name_player]?!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    Y crying "I... I-I..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    play music bgm_relaxed
    Y "I'm...SO GLAD YOU'RE OKAY...!!" with shakeshort
    O jacketless surprised "....."
    Y "I can't... I couldn't..." with shakeonce
    $ fadein_sideimage = True
    I "...No good... My thoughts are just..." with shakeshort
    O jacketless relaxed "...Come on, is this really worth crying over?"
    $ fadein_sideimage = False
    O "Besides, it was only one cut on my arm. I can still move it too."
    Y troubled "I... I-I was..." with shakeshort
    O jacketless thinking "....."
    O jacketless default "[name_player]. Now that I think about it..."
    O "We never finished our conversation in the basement. The one we were having before Cecilia woke up."
    Y shadow "{cps=6}.....{/cps} ...Huh...?"
    O "....."
    O jacketless blink "...Your reaction tells me a lot must have happened since then."
    O jacketless default "I was asking you what happens if you or I jump into the basement hatch, [name_player]."
    $ fadein_sideimage = True
    I "...Right... I vaguely recall something like that..." with hpunch
    O jacketless thinking "You were hesitant about saying what happens if you jump in."
    $ fadein_sideimage = False
    O jacketless blink "I didn't want to push the issue any further, so I brought the topic back to myself, but..."
    play ctc_sfx sfx_heartbeat_single
    O jacketless irritated "Something terrible... Something [t_clue]worse than death[t_cluee] happened to you, didn't it...?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    I "{cps=6}.....{/cps}"
    O jacketless default "I won't ask you to say what happened. But if that's what is weighing heavy on your heart..."
    $ fadein_sideimage = False
    O jacketless thinking "...Then you should know that I finally remember.{w=1.0} The light... Your screams...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    show bg flamewall:
        matrixcolor BrightnessMatrix(0.0) * SaturationMatrix(0.0)
        linear 5.0 matrixcolor BrightnessMatrix(-1.0) * SaturationMatrix(0.0)
    with custom_flashquick()
    extend jacketless irritated " [t_clue]I remember it all[t_cluee]." with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y depressed "...!!!" with shakeshort
    O jacketless thinking "So...{w=0.5} If you feel like you're alone in your suffering... If you're about to go mad from the endless torture..."
    O jacketless default "Keep in mind that there are [t_clue]others[t_cluee] who know your pain. Others who are desperately seeking the solution."
    O "You don't have to feel like you're fighting alone."
    Y "....."
    Y troubled "I'm..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    I "{cps=12}I'm...not alone...{/cps}"
    play ctc_sfx "<silence 1.0>"
    O jacketless blink "....."
    $ fadein_sideimage = False
    O "Now... Whenever you're ready..."
    O jacketless default "Tell me everything that happened since we got attacked."
    $ fadein_sideimage = True
    I "....."
    I "Yeah... There's still work to be done..." with hpunch
    I "I need to get Ria caught up..."
    $ show_side_oriana = False
    scene bg black with dissolvemed
    stop music fadeout 5.0
    pause 5.0

    call save_file_name_update (3, "d3a1_masterbedroom_ria_hearttoheart")
    I "I shared everything I could remember, including any clues I found in the library."
    if seen_cece_hearttoheart:
        I "I skipped over what I talked with Cece about, though."
    scene bg masterbedroom
    show oriana jacketless blink at mycenter
    with dissolvemed
    Y sad "And now we're here, waiting for Cece to come back from the attic."
    O jacketless thinking "I see... I'm sorry to have weighed you down like that."
    Y panicked "No, you don't need to apologize. You were injured pretty badly." with hpunch
    $ fadein_sideimage = False
    Y sad "And there was no way we were gonna leave you alone when that zombie's still on the loose."
    $ fadein_sideimage = True
    O jacketless blink "....."
    Y surprised "...Ria?"
    O jacketless irritated "Is it a zombie, though? Maybe it was someone pretending to be dead to catch us by surprise."
    Y worried "Maybe, but...that doesn't change the fact that it tried to kill us."
    O jacketless thinking "Perhaps not, but..."
    play ctc_sfx sfx_emotequestion
    O jacketless leering "...[name_player]. What do you think is really going on around here?"
    Y surprised "What do you mean?"
    O jacketless thinking "Well, as far as Cecilia and I are concerned, we never fully explored the entirety of this house, but..."
    O jacketless default "According to you, the only place we hadn't checked was the basement."
    Y thinking "I guess so, yeah..." with hpunch
    O jacketless irritated "But after we checked out the basement and that underground passage, we got ambushed by that...monstrous attacker..."
    O jacketless thinking "...And then we were trapped in the library for a while, yes? No doors leading to other rooms in there?"
    play ctc_sfx "<silence 1.0>"
    Y depressed "....."
    play ctc_sfx "<silence 1.0>"
    O jacketless blink "...You've realized it, haven't you, [name_player]?"
    show bg black
    play ctc_sfx sfx_heartbeat_single
    O jacketless leering "With your own eyes, you checked [t_clue]every room[t_cluee] in this house now." with shakeonce
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    O jacketless irritated "All of those [t_clue]clues[t_cluee]... All of those [t_clue]deaths[t_cluee] you've experienced...{w=1.0} And yet, there's a critical question we still don't have the answer to."
    O "{cps=6}.....{/cps}{w=1.0} {nw}"
    play ctc_sfx "<silence 1.0>"
    extend jacketless leering "...Who is the [t_clue]mastermind[t_cluee] of this killing game?{nw}"
    play ctc_sfx "<silence 1.0>"
    play music bgm_tension
    extend "" with shakeshort
    Y depressed "...The...mastermind..."
    O jacketless irritated "There was no obvious \"culprit\" hiding anywhere. So what do you think this means?"
    I "....."
    play ctc_sfx "<silence 1.0>"
    I "Do I know who it is...? If I think back to everything I've experienced so far..."
    play ctc_sfx "<silence 1.0>"
    $ renpy.music.set_volume(0.5, 3, channel="music")
    scene cg karma2 at grayscale_on with custom_flash()
    pause 0.5
    scene cg wakeup at grayscale_on with dissolve
    pause 0.5
    scene bg bedroom dark at grayscale_on
    show oriana_raw deranged at mycenter, grayscale_on
    with dissolve
    pause 0.5
    scene cg judgement at grayscale_on with dissolve
    pause 0.5
    scene bg flamewall at grayscale_on
    show pov_hand at grayscale_on:
        xalign 0.2 yanchor 1.0 ypos 1.2
    with dissolve
    pause 0.5
    scene cg despair at grayscale_on with dissolve
    pause 0.5
    scene bg basement nocorpse at grayscale_on
    show villain_raw attacking at mycenter, grayscale_on
    with dissolve
    pause 0.5
    scene bg emptybedroom dark chaos at grayscale_on
    show cecilia_raw creepygrin at mycenter, grayscale_on
    with dissolve
    pause 0.5
    scene bg bloodpool 3 at grayscale_on
    with dissolve
    pause 0.5
    scene bg basement entrance light at grayscale_on
    show dog_raw at mycenter, grayscale_on
    with dissolve
    pause 0.5
    scene bg frontdoor at grayscale_on with dissolve
    pause 0.5
    play sound sfx_flashback
    scene bg black
    show oriana jacketless leering at mycenter
    with custom_flashbulblong()
    $ renpy.music.set_volume(1.0, 3, channel="music")
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"

label d3a1_choosesuspect:
    I "The one who orchestrated this whole killing game is...{nw}"

    menu:
        extend ""
        "The monstrous attacker":
            Y shadow "...It has to be that zombie. ...No, the...\"monstrous attacker\"."
            O jacketless default "....."
            Y thinking "If he really {i}is{/i} a mindless zombie, then why did he wait so long before killing you in the lounge?"
            $ fadein_sideimage = False
            Y "Why did he play dead before trying to attack us while our backs were turned?"
            Y leering "But most importantly... Where did he disappear to?" with shakeonce
            Y "He has to be hiding somewhere again, waiting for another chance to kill us."
            $ fadein_sideimage = True
            O jacketless thinking "....."
            Y surprised "...Huh? What is it?"
            O "It's just... Don't you remember what Cecilia said when she checked the corpse in the basement?"
            play ctc_sfx "<silence 1.0>"
            play sound sfx_flashback
            scene bg basement at grayscale_on:
                xalign 1.0 yalign 0.7 zoom 1.5
            with custom_flashbulblong()
            $ grayscale_sideimage = True
            Y afraid "Wh-what is..." with shakeonce
            $ fadein_sideimage = False
            $ show_side_cecilia = True
            C surprised "Looks like a dead man sitting. Wait, hang on..."
            C thinking "...Yep. [t_clue]No pulse[t_cluee]. Definitely dead."
            Y depressed "He's...dead...? Then... Is the culprit...?" with shakeonce
            $ fadein_sideimage = True
            $ show_side_cecilia = False
            $ grayscale_sideimage = False
            scene bg black with dissolvemed
            scene bg black
            show oriana jacketless thinking at mycenter
            with dissolvemed
            I "...That's right..."
            Y troubled "He...didn't have a pulse..." with shakeonce
            O jacketless blink "...Admittedly, only Cecilia touched his body directly."
            O jacketless thinking "But considering how she protected us from him later, it wouldn't make sense if she lied about that."
            O jacketless leering "And then both of us saw him move and attack us. That is a fact." with shakeonce
            Y thinking "Then... He must have been able to move despite not having a pulse...?"
            O jacketless blink "...Normally I would say that's preposterous, but..."
            O "...I suppose if time travel is possible, then reanimated corpses shouldn't come as a surprise."
            I "....."
            O jacketless thinking "That said, though... If he really is the mastermind, then his actions don't fully make sense."
            O "For instance, if he wanted us to kill each other in the killing game, why would he suddenly try to attack us now?"
            O "And now, he's gone missing... Why did he stop pursuing us?"
            jump d3a1_choosesuspect_end
        "The dog":
            Y wince "...Could it be... [name_dog]?" with hpunch
            O jacketless default "....."
            O jacketless blink "...We can't really rule that out, I suppose."
            Y panicked "H-huh? I was kinda expecting you to deny it..." with hpunch
            O jacketless thinking "As much as it would pain me if that were the case, considering what's happened so far, it wouldn't be the strangest thing."
            O jacketless irritated "[name_dog]'s appearances have been rare and sudden, to say the least."
            Y thinking "Yeah, even in my own memories, I can count the number of times I've ever seen [name_dog] on one hand..."
            play ctc_sfx "<silence 1.0>"
            $ renpy.music.set_volume(0.5, 3, channel="music")
            scene bg diningroom at grayscale_on
            show oriana_raw overjoyed at myleft, grayscale_on
            show cecilia_raw sweatdrop at myright, grayscale_on
            show dog_raw at mycenter, grayscale_on
            with custom_flash()
            pause 1.5
            scene bg lounge at grayscale_on
            show dog_raw at mycenter, grayscale_on
            with dissolve
            pause 1.5
            scene bg basement entrance light at grayscale_on
            show dog_raw at mycenter, grayscale_on
            with dissolve
            pause 1.5
            I "And all he ever does is watch us for a while, then run away..."
            $ show_side_oriana = True
            O jacketless thinking "There's just one issue with that possibility, [name_player]."
            $ fadein_sideimage = False
            O jacketless default "There's no way [name_dog] could have written the [t_clue]message on the front door[t_cluee]."
            Y surprised "The front door..."
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            play sound sfx_flashback
            scene bg frontdoor at grayscale_on
            with custom_flashbulblong()
            pause 1.0
            scene bg frontdoor at grayscale_on:
                xalign 0.5 yalign 1.0 zoom 1.2
                easein 6.0 zoom 1.3 yalign 0.1
            with dissolve
            I "...Yeah, she's right..." with hpunch
            I "It's written too high up and too well for a dog to have done it..."
            $ show_side_oriana = False
            $ renpy.music.set_volume(1.0, 3, channel="music")
            scene bg black with dissolvemed
            scene bg black
            show oriana jacketless thinking at mycenter
            with dissolvemed
            O "That message is the {color=#ff0000}sole reason{/color} this entire killing game began."
            O "I suppose [name_dog] could've had a human accomplice, but then we're back to suspecting everyone else again."
            jump d3a1_choosesuspect_end
        "One of us":
            Y shadow2 "....."
            $ fadein_sideimage = False
            Y "...It can only be one of us, right?"
            $ fadein_sideimage = True
            jump d3a1_choosesuspect2
        "Someone outside the house":
            Y blink "...It has to be someone [t_clue]outside the house[t_cluee]."
            O jacketless default "....."
            Y wince "No matter what angle I think from, it can't possibly be anyone {i}inside{/i} the house." with shakeonce
            $ fadein_sideimage = False
            Y thinking "The zombie's actions don't make sense for the killing game, we're the \"players\", and [name_dog] is...well, a DOG."
            Y surprised "And the front door... It always opens really loudly the MOMENT one of us dies."
            Y leering "That means...someone has to be watching this entire \"game\" as it unfolds. Hearing [t_clue]every word we speak[t_cluee], even now." with shakeonce
            $ fadein_sideimage = True
            O jacketless blink "[name_player]. I see where you're going with this."
            Y angry "...Yeah. We're in some [t_clue]maniac's crazy game[t_cluee]." with shakeonce
            $ fadein_sideimage = False
            Y pained "It's probably whoever was experimenting with the occult materials in the attic and the basement." with shakeonce
            Y pained2 "Or...some [t_clue]demon[t_cluee] they summoned through those experiments." with shakeonce
            $ renpy.music.set_volume(0.0, 3, channel="music")
            play ctc_sfx sfx_heartbeat_single
            Y depressed "...Wait. Is this not the real world? Are we not in our real bodies right now?" with shakeonce
            $ fadein_sideimage = True
            O jacketless leering "[name_player]. You're going too far with your theorizing."
            play ctc_sfx "<silence 1.0>"
            Y troubled "....." with shakeonce
            O jacketless irritated "...I won't deny the occult aspect of this situation. As loath as I am to accept."
            play ctc_sfx sfx_emotequestion
            O jacketless leering "But keep in mind that you have your time travel power. A power that is [t_clue]exclusively yours[t_cluee]."
            Y thinking "Huh? What does that have to do with anything...?"
            O jacketless irritated "Let's suppose for a moment that this whole house...this \"killing game\" is a fabrication designed to torture us."
            O jacketless leering "Do you think whatever monster responsible for this would've given you the power to constantly undo any of our deaths?"
            Y pained "But I can't even control it... I must've gotten it so that I would endlessly go through--" with shakeonce
            play ctc_sfx sfx_heartbeat_single
            O "Then why don't Cecilia and I have the same power?" with shakeshort
            Y shocked "Th-that's..." with shakeonce
            O jacketless thinking "It's true that I'm starting to remember faint details now, but..."
            O jacketless default "Whenever you would tell us about the future events you've experienced, Cecilia and I were genuinely surprised by them."
            O jacketless blink "From our point of view, we're in a \"normal\" killing game, as oxymoronic as that sounds."
            O "In other words, your time travel power has to be an unexpected variable. Something the culprit [t_clue]didn't anticipate[t_cluee]."
            play ctc_sfx "<silence 1.0>"
            I "....."
            O "...There's still hope, [name_player]. There's a way out of this."
            play ctc_sfx "<silence 1.0>"
            O jacketless leering "This place... It's NOT {color=#ff0000}Hell{/color}."
            play ctc_sfx "<silence 1.0>"
            Y depressed "....."
            $ fadein_sideimage = False
            Y sad "....." with shakeonce
            $ renpy.music.set_volume(1.0, 3, channel="music")
            Y blink "...You're right. Sorry." with hpunch
            $ fadein_sideimage = True
            O jacketless blink "....."
            O jacketless thinking "But getting back on track..."
            O jacketless default "...We're not dealing with some omniscient being. The culprit is a being with limits, like any of us."
            O "So I don't think they could be outside of the house. There's no surveillance cameras anywhere, and the windows are fogged up."
            jump d3a1_choosesuspect_end
        "\"I don't know...\"":
            Y sad "{cps=6}.....{/cps} ...I don't know."
            $ fadein_sideimage = False
            Y wince "I feel like I don't have enough information to even make a guess." with hpunch
            $ fadein_sideimage = True
            O jacketless default "....."
            O jacketless thinking "...I suppose I can't blame you for hesitating. It's generally unwise to base your theories on conjecture."
            I "....."
            O jacketless irritated "But there are moments where you have no choice but to do so."
            O "Even if all the facts haven't been laid out yet, you can still pick a direction and have faith it will lead you to the [t_clue]truth[t_cluee]."
            jump d3a1_choosesuspect_end
label d3a1_choosesuspect2:
    O jacketless blink "....."
    O "...And which of us do you suspect could be the [t_clue]mastermind[t_cluee]?"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps} The true villain behind the killing game is..."
    play ctc_sfx "<silence 1.0>"
    $ show_choicegrand = True
    menu:
        "Cecilia":
            $ renpy.music.set_volume(0.0, 3, channel="music")
            Y shadow2 "...You think it's Cece, don't you? You...probably always did."
            play ctc_sfx "<silence 1.0>"
            O jacketless default "....."
            Y troubled "...Even way back, when we were first investigating the second floor..."
            $ fadein_sideimage = False
            Y "You were keen to suspect a small girl. Maybe not the girl who lived here, but--" with hpunch
            $ fadein_sideimage = True
            O jacketless blink "I don't know what you're talking about. As far as I'm aware, we've never investigated the second floor together."
            O jacketless thinking "But... I can't deny I suspected Cecilia at first."
            Y wince "A-and now you don't?" with hpunch
            O jacketless blink "...As much as she comes across as a little less than sane..."
            play ctc_sfx sfx_emotequestion
            O "...It is a fact that she [t_clue]risked her life for us[t_cluee]."
            if d1a4_questioning_clue2AB:
                O jacketless thinking "She...followed through with her [t_clue]promise[t_cluee]."
                Y shadow "....."
                play ctc_sfx "<silence 1.0>"
                play sound sfx_flashback
                scene bg diningroom dark at grayscale_on
                show cecilia sad at mycenter, grayscale_on
                with custom_flashbulblong()
                C "*sigh* ...Fine, how about this?"
                C default "[name_player]."
                C blink "I swear to you here and now, with Ria as my witness..."
                C "I won't allow either of you to come into any harm."
                C smile "That's a promise."
                scene bg black with dissolvemed
                scene bg black
                show oriana jacketless irritated at mycenter
                with dissolvemed
                I "{cps=6}.....{/cps}"
                play ctc_sfx "<silence 1.0>"
                O "It sounded so hollow, so fake at the time. But after all that's happened since..."
                play ctc_sfx "<silence 1.0>"
                O jacketless thinking "...How could we possibly suspect her now?"
            else:
                O jacketless thinking "What choice do I have but to believe in her now?"
            play ctc_sfx "<silence 1.0>"
            $ chose_suspect = True
            if persistent.unlock_gameclear_cgs:
                show bg white
                show oriana jacketless thinking:
                    matrixcolor InvertMatrix(1.0)
                play loop_sfx sfx_introambiance_sequence4_loop
                S "ERROR: An exception has occurred. Please rollback your changes.{fast}" with custom_flashquickred()
                play ctc_sfx "<silence 1.0>"
                S "ERROR: An exception has occurred. Please rollback your changes.\nERROR: An exception has occurred. Please rollback your changes.{fast}" with shakeonce
                play ctc_sfx "<silence 1.0>"
                S "ERROR: An exception has occurred. Please rollback your changes.\nERROR: An exception has occurred. Please rollback your changes.\nERROR: An exception has occurred. Please rollback your changes.{fast}" with shakeshort
                play ctc_sfx "<silence 1.0>"
                stop loop_sfx
                show bg black
                show oriana jacketless thinking:
                    matrixcolor InvertMatrix(0.0)
                I "...?" with custom_flashquickred()
                achieve BUG_MASTERMIND
            $ renpy.music.set_volume(1.0, 3, channel="music")
            jump d3a1_choosesuspect_end
        "Oriana":
            $ renpy.music.set_volume(0.0, 3, channel="music")
            Y shadow "...Could it be...you?"
            play ctc_sfx "<silence 1.0>"
            O jacketless default "....."
            play ctc_sfx "<silence 1.0>"
            O "...Are you guessing blindly right now? Or did you pick the option you think would offer the biggest plot twist?"
            Y panicked "I... Uh..." with hpunch
            play ctc_sfx "<silence 1.0>"
            O jacketless irritated "If this is just a joke to you, then never mind. You're better off not trying to guess."
            $ renpy.music.set_volume(1.0, 3, channel="music")
            jump d3a1_choosesuspect_end
        "Me":
            $ renpy.music.set_volume(0.0, 3, channel="music")
            Y shadow2 "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = False
            Y "...It might have been me. I...still don't have all of my memories back..."
            Y "For all we know, I could have set this whole situation up and found a way to erase my memory about it."
            play ctc_sfx "<silence 1.0>"
            Y "Maybe on some level... I wanted to experience a killing game firsthand." with shakeonce
            $ fadein_sideimage = True
            O jacketless thinking "....."
            O jacketless blink "No. I have trouble imagining you to be someone like that, [name_player]."
            O "Even if you don't have all of your memories back, your personality is fixed."
            O jacketless default "And the fact that you cried just moments earlier at the sight of me waking up..."
            I "....."
            O jacketless blink "I don't need to say anything more, do I?"
            $ renpy.music.set_volume(1.0, 3, channel="music")
            jump d3a1_choosesuspect_end
        "The third club member" if d1a4_third_member_mentioned:
            $ renpy.music.set_volume(0.0, 3, channel="music")
            Y leering "...You mentioned before that there's a [t_clue]third member[t_cluee] of the Occult Club."
            O jacketless surprised "...!!" with shakeonce
            O jacketless thinking "W-we've told you already that she didn't come with us." with shakeonce
            Y thinking "But it doesn't make sense. Cece's feelings for you are a mystery, but {i}you{/i} clearly don't like her very much."
            play ctc_sfx sfx_emotequestion
            $ fadein_sideimage = False
            Y leering "At least... Not enough that you would agree to visit an abandoned house with her, just the two of you."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            O jacketless shadow "....." with shakeonce
            Y blink "The third member came to this house with you two, didn't she?"
            $ fadein_sideimage = False
            Y thinking "That would explain why {i}you're{/i} here. But I guess the question is where is she hiding now--"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            O "...You're wrong, [name_player]."
            Y surprised "....."
            play ctc_sfx "<silence 1.0>"
            O "The third member...is our [t_clue]friend[t_cluee]. She loves me and Cecilia too much to put us in a killing game." with shakeonce
            play ctc_sfx "<silence 1.0>"
            O "There's no way she could be the mastermind."
            play ctc_sfx sfx_heartbeat_single
            Y shadow "....." with shakeshort
            play ctc_sfx "<silence 1.0>"
            $ renpy.music.set_volume(1.0, 3, channel="music")
            jump d3a1_choosesuspect_end
        "Cancel your accusation":
            $ show_choicegrand = False
            Y wince "...Sorry, I think I might be wrong about this. Let me back up a bit." with hpunch
            O jacketless default "....."
            jump d3a1_choosesuspect

label d3a1_choosesuspect_end:
    $ show_choicegrand = False
    $ _last_say_who = None
    window auto hide
    show bg masterbedroom with dissolvemed
    I "She's got a point... I guess that wasn't the right answer...?" with shakeonce
    Y wince "Well then... Who do {i}you{/i} think is the mastermind, Ria?"
    O jacketless blink "....."
    Y surprised "...Ria?"
    stop music fadeout 3.0
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    O jacketless dejected "...I just don't know anymore..."
    O "Ever since we had our conversation in the basement, my head has been an absolute mess..."
    play ctc_sfx "<silence 1.0>"
    I "....."
    play ctc_sfx "<silence 1.0>"
    O jacketless irritated "It also doesn't help that I woke up from a horrible [t_clue]nightmare[t_cluee] just a moment ago..."
    Y thinking "A nightmare?"
    O jacketless shadow "Yes. A terrifying one where..."
    play ctc_sfx sfx_heartbeat_single
    O "...Where I kept [t_clue]getting killed over and over[t_cluee]..." with shakeonce
    Y shocked "....." with shakeonce
    O "...I wonder if this is anything like your time traveling, [name_player]?"
    Y shadow "....."
    I "...?{w=0.5} Wait... Come to think of it..." with hpunch
    I "When I was asleep in the basement, I didn't have a [t_clue]strange dream[t_cluee]..."
    show bg masterbedroom:
        matrixcolor BrightnessMatrix(0.0)
        linear 3.0 matrixcolor BrightnessMatrix(-1.0)
    play ctc_sfx "<silence 1.0>"
    Y blink "{cps=6}.........{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "Focus your mind, [name_player_true]..."
    play ctc_sfx "<silence 1.0>"
    scene bg white with custom_flashbulblong()
    scene cg allshards
    with dissolveslow
    pause 2.0
    I "{cps=6}.........{/cps}"
    play ctc_sfx sfx_emotequestion
    I "...Huh?"
    play ctc_sfx "<silence 1.0>"
    I "There's...no more...?!" with shakeonce
    play ctc_sfx sfx_heartbeat_single
    I "Could this mean... [t_clue]I don't turn back time anymore[t_cluee]?" with shakeshort
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolvemed
    scene bg masterbedroom
    show oriana jacketless surprised at mycenter
    with dissolvemed
    O "[name_player]...?"
    Y shadow "{cps=6}.....{/cps}"
    $ fadein_sideimage = False
    Y "...Ria. I think...{nw}"

    menu:
        extend ""
        "\"It'll be fine now.\"":
            Y leering "...We're nearly at the end of all this. Everything will be all right." with shakeonce
            $ fadein_sideimage = True
            O jacketless leering "...What makes you so sure?"
            Y blink "I even tried concentrating, but I couldn't see any more unusual memories."
            $ fadein_sideimage = False
            Y "I don't know what the future looks like going forward from here. In other words..."
        "\"We should be careful.\"":
            Y wince "...We'll need to be extra careful going forward." with shakeonce
            Y sad "I... I don't think time will rewind anymore. I don't know what's in the future this time."
            $ fadein_sideimage = True
            O jacketless surprised "...! A-are you sure?" with shakeonce
            Y wince "Yeah... I was trying to focus earlier, and no new memories come to mind."
            O jacketless leering "So you mean...the \"[name_player]\" in front of me right now didn't travel back in time at all?"
            Y sad "Exactly... That's why I think..."
            $ fadein_sideimage = False
    play ctc_sfx sfx_heartbeat_single
    Y leering "...This should be the {color=#ff0000}final killing game{/color}." with shakeonce
    $ fadein_sideimage = True
    O jacketless surprised "...!!" with shakeonce
    O "....."
    O jacketless thinking "I see... So the time loops have finally come to an end..."
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    O jacketless irritated "{cps=6}.......{/cps}"
    I "...She doesn't look relieved at all. In fact...I think she's even more troubled..." with shakeonce
    Y surprised "Ria, are you okay?"
    play ctc_sfx "<silence 1.0>"
    O "...Why...?"
    play ctc_sfx "<silence 1.0>"
    O jacketless irritated "...Why is it all ending {i}now{/i}? What changed...?" with shakeshort
    Y panicked "R-Ria?" with hpunch
    play ctc_sfx "<silence 1.0>"
    O jacketless panicked "Ah--{w=1.0} ...I-I..." with shakeshort
    O jacketless irritated "....."
    O jacketless thinking "I-I'm sorry. I suppose the thought of the killing game finally ending is...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend "[t_clue]frightening[t_cluee]." with shakeonce
    I "....."
    O jacketless blink "...You said that you don't know the future.{w=0.5} That means you also don't know HOW the killing game will end."
    O jacketless leering "Sure, we could all escape this nightmare safely, but...you know there's another possibility."
    Y wince "...Yeah. It could end because [t_clue]one of us finally dies[t_cluee].{cps=1} {/cps}{nw}"
    play ctc_sfx sfx_heartbeat_single
    $ fadein_sideimage = False
    show bg masterbedroom dark
    extend troubled "{color=#ff0000}Permanently{/color}." with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    O jacketless irritated "....." with shakeonce
    O "....."
    play ctc_sfx "<silence 1.0>"
    O jacketless shadow "{cps=6}.......{/cps}"
    I "....."
    I "...It might be because of her injury, but...I've never seen Ria look this drained..."
    I "What should I do? Should I change the topic? Or maybe it'd be better to leave her alone now..."
    $ show_choicegrand = True
    menu:
        "Keep talking with Ria":
            $ show_choicegrand = False
            call d3a1_masterbedroom_ria_hearttoheart
        "Stop talking with Ria":

            $ show_choicegrand = False
            I "...No. I should stop before I stress her out even more."
            Y sad "...Cece should be back soon, so let's try to get some rest while we can."
            O jacketless shadow "....."
            play ctc_sfx "<silence 1.0>"
            O jacketless dejected "...Okay."
            play ctc_sfx "<silence 1.0>"
            scene bg black with dissolveslow
            pause 6.7
            play sound sfx_knockhard
            show bg black with shakeshort
            pause 0.5
    jump d3a2

label d3a1_masterbedroom_ria_hearttoheart:
    show bg masterbedroom with dissolvemed
    Y panicked "...S-soooo, Ria? Why exactly did you join the Occult Club?" with hpunch
    O jacketless blink "....."
    O jacketless thinking "...You're asking that {i}now{/i}?"
    Y sad "I mean, you don't have to share if you don't want to, but..."
    $ fadein_sideimage = False
    Y worried "I dunno, I guess I'm curious?" with hpunch
    $ fadein_sideimage = True
    O "....."
    Y surprised "...Ria?"
    play ctc_sfx "<silence 1.0>"
    O jacketless blink "{cps=6}.......{/cps} ...I'm sorry, it's just..."
    O jacketless relaxed "The way you shrugged awkwardly just now reminded me of someone I know..."
    Y surprised "Really? Who?"
    O jacketless thinking "...Someone you've never met."
    if d1a4_third_member_mentioned:
        O jacketless default "Do you remember back in the dining room...when we talked about the third member in the Occult Club?{nw}"

        menu:
            extend ""
            "\"I remember.\"":
                Y thinking "Right... It didn't seem like you wanted to talk about that, though."
                O jacketless blink "...It's fine now. I think... No, you definitely deserve to know."
            "\"No...\"":
                Y worried "Uh... Sorry, I don't remember." with hpunch
                O jacketless thinking "That's fine. We barely talked about it, after all."
    else:
        Y thinking "...?"
    O jacketless blink "As of this year, the Occult Club currently consists of three members."
    O "There's Cecilia, the president. Then there's me. And finally, the third member."
    play ctc_sfx "<silence 1.0>"
    O jacketless thinking "Her name is... {w=1.0}[t_clue]Carol-Maria[t_cluee]."
    Y surprised "Carol...and Maria...?"
    O jacketless blink "It's both of those names put together. Her parents were whimsical. Not important right now."
    O jacketless default "Anyway, Carol-Maria and I were acquainted long before we joined the Occult Club. We met in our first semester of high school."
    O jacketless thinking "She and I have...opposite personalities. And back in the day, we were like oil and water."
    Y thinking "Huh? Oil and...?"
    O jacketless blink "As in, we didn't get along. In fact, our very first conversation began with me yelling at her."
    play music bgm_origin_order
    scene bg black with dissolveslow
    pause 1.0
    $ name_oriana = _("Young Oriana")
    $ name_npc = _("???")
    O "What... What in the world are you...{size=-10}all doing...?{/size}"
    $ name_npc = _("Student A")
    X "Huh? Who's this tiny little kid?"
    $ name_npc = _("Student B")
    X "I guess she's a first-year? Do you know this girl, Carol?"
    $ name_karma = _("{color=#fff}\"Carol\"{/color}")
    K "Nope, first time seeing her."
    O "Um... F-first period is already under way, and...and you're all here with...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " Wait, is that...?!" with shakeonce
    $ name_npc = _("Student A")
    X "Oh, lighten up, four-eyes. Come on, you can try one if you want~"
    scene cg origin oriana at wobble:
        xalign 0.5 yalign 0.75 zoom 1.5 blur 10.0
        easein 20.0 zoom 1.0 blur 0.0
    with dissolveslow
    O "You... Y-you shouldn't...{size=-10}be doing this...{/size}" with shakeonce
    $ name_npc = _("Student C")
    X "Ha! Check it out, the kid's trying to tell us what we can and can't do!" with vpunch
    K "Hey, keep your voice down! What if a teacher shows up?" with hpunch
    O "Th-this isn't about me... It's about...{size=-10}being proper members of society...{/size}"
    $ name_npc = _("Student B")
    X "Huh? What did you say? What's wrong with you; why do you keep mumbling like that?"
    $ name_npc = _("Student C")
    X "She said something about \"society\". Ha, we got a little Lady Justice here!"
    O "I'm... I-I'm not--" with shakeonce
    $ name_npc = _("Student A")
    X "Aren't you a first-year? You've only been in high school for like what, a week?"
    $ name_npc = _("Student B")
    X "Move along, kid. It's clearly too soon for you to join our fun."
    O "..... {size=-10}*sniff*{/size}"
    $ name_npc = _("Student C")
    X "Wha-- DUDE, you made her cry! You're so baaaad~" with shakeshort
    scene cg origin oriana:
        xalign 0.5 yalign 0.75 zoom 1.25
        easein 10.0 zoom 1.5
    with dissolve
    $ name_npc = _("Student A")
    X "Awww, I didn't mean to do that... Okay, come over here, kid, let me--{w=1.0}{nw}"
    play ctc_sfx sfx_slap
    show bg black with custom_flashquick()
    extend " OUCH!!" with shakeshort
    X "Wh-wha... Carol?!" with shakeonce
    K "...You already crossed a line, and were about to cross another one."
    K "It's been fun, I guess, but we're done here.{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " Never talk to me again." with shakeonce
    X "Carol... You--" with shakeshort
    $ name_npc = _("Student B")
    play sound sfx_runninglong
    X "Hey, four-eyes is running! Crap, we gotta clean this up before a teacher comes!" with shakeshort
    scene bg black
    pause 3.0
    play sound sfx_runninglong fadein 0.5
    O "*pant* *gasp* *wheeze*" with shakeshort
    play ctc_sfx sfx_running
    K "H-hey! Fellow first-year girl! Slow down!" with shakeshort
    scene cg origin oriana1:
        xalign 1.0 yalign 0.5 zoom 1.5 matrixcolor BrightnessMatrix(-1.0)
        parallel:
            easein 20.0 zoom 1.0
        parallel:
            linear 5.0 matrixcolor BrightnessMatrix(0.0)
    with dissolvemed
    O "*pant* ...Y-you're..." with shakeonce
    K "Whew! You run fast, um... Sorry, what was your name again? Mine's, uh...Carol-Maria." with vpunch
    $ name_karma = _("{color=#fff}Carol-Maria{/color}")
    O "Carol... *pant* ...Maria..."
    K "Eh... It's actually the names \"Carol\" and \"Maria\" stuck together with a hyphen. I know it's weird, but--"
    play ctc_sfx sfx_emoteshout
    O "SCREW YOU! AND SCREW THOSE GUYS!" with shakelong
    K "ACK! Wh-whoa, so you CAN speak louder..." with hpunch
    O "You're the same age as me, right?! You've only been here for a week too, RIGHT?!" with shakeonce
    play ctc_sfx sfx_emotesigh
    K "Y-yes, that's correct..." with hpunch
    play ctc_sfx sfx_emoteshout
    with custom_flashquick()
    O "WHAT WERE YOU THINKING?! Those guys were... They were--" with shakelong
    play ctc_sfx sfx_emotesob
    K "AHHHH, you don't have to say it! Look, yes, they were doing...something bad, but like... They're not..." with shakeonce
    O "{cps=6}.....{/cps} ...They're not...?"
    K "{cps=6}.....{/cps}{w=0.5} {nw}"
    play ctc_sfx "<silence 1.0>"
    extend "*sigh* No, you're right. I guess I could hang out with better people. I just kinda went with the flow, you see." with hpunch
    O "The \"flow\"? The \"flow\" led you to commit a cri--"
    K "I didn't try any of those, I swear! I was just hanging with them!" with shakeonce
    K "I mean, you know what it's like, right? First few days of high school, you wanna make friends right away so you can..."
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}.....{/cps}"
    K "Uh... You, uh... H-have friends, right?"
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}.....{/cps}{w=1.0} {size=-10}No.{/size}"
    K "...You know what? Tell me your name. Come on, quickly."
    O "...Oriana."
    play ctc_sfx sfx_emotehappy
    K "Oriana! From this day onwards, we're friends!" with vpunch
    O "Huh? No thanks."
    play ctc_sfx sfx_emoteshout
    K "Pft! AHAHA!! I got rejected instantly! You're actually pretty funny, huh, Oriana?" with shakeshort
    O "....."
    K "...Wait, you weren't joking?"
    O "I have no interest in befriending someone who is predisposed to physical violence."
    play ctc_sfx sfx_emotesob
    K "Physical vio-- Y-you mean that slap earlier?! That was because--" with shakeshort
    show bg black with custom_flashquick()
    $ name_npc = _("Teacher")
    X "HEY! What are you two doing in the hallway?! You should be in class right now!" with shakeshort
    K "Oh crap! Oriana, let's talk again at lunch, okay?!" with shakeonce
    $ persistent.unlock_cg_origin_oriana = True
    $ name_npc = _("???")
    $ name_karma = _("???")
    $ name_oriana = _("Ria")
    window auto hide
    pause 2.0
    scene cg ria hearttoheart:
        xalign 0.2 yalign 0.0 zoom 2.0
        easein 20.0 zoom 1.5
    with dissolveslow
    Y surprised "....."
    $ fadein_sideimage = False
    Y "That was...quite the story..."
    $ show_side_oriana = True
    O jacketless thinking "I remember the details vividly. It was an important day for me, after all."
    $ fadein_sideimage = True
    I "Yeah, it almost felt like I was there myself..."
    O jacketless blink "Looking back on it now, becoming friends with Carol-Maria shaped us both into better, stronger people."
    $ fadein_sideimage = False
    O jacketless thinking "She taught me how to assert myself more, and I taught her how to make better decisions in life."
    $ fadein_sideimage = True
    play ctc_sfx sfx_emotesigh
    I "That's...certainly a way to phrase it..." with hpunch
    Y blink "It sounds like even back in the day, you had a strong moral compass."
    $ fadein_sideimage = False
    Y default "Strong enough to push you into confronting a group of delinquents all by yourself."
    O "I suppose so, yes. I was certainly aware of how small and timid I was, and yet, I still charged ahead reflexively."
    $ fadein_sideimage = True
    scene cg ria hearttoheart:
        xalign 0.5 yalign 1.0 zoom 1.4
        easein 5.0 zoom 1.5
    with dissolvemed
    Y relaxed "And look at you now. You're definitely not small anymore.{w=1.0}{nw}"
    $ fadein_sideimage = False
    show cg ria hearttoheart:
        xalign 0.5 yalign 1.0 zoom 1.4
        easein 2.0 yalign 0.5
    play ctc_sfx "<silence 1.0>"
    extend panicked " ...Er, sorry, what I meant was--" with shakeonce
    O jacketless irritated "It's fine. I know what you mean."
    $ fadein_sideimage = True
    scene cg ria hearttoheart:
        xalign 0.5 yalign 0.5 zoom 1.4
        easein 20.0 zoom 1.0
    with dissolve
    O jacketless think "To this day, Carol-Maria likes to tease at how much I grew over the years."
    $ fadein_sideimage = False
    Y surprised "And what about her? Did Carol-Maria grow a lot too?"
    O jacketless default "Not much physically, but a lot mentally. When we first met, she didn't have the best grades."
    O jacketless thinking "But once it became nearly time for us to graduate high school, she was suddenly enthusiastic about studying."
    O jacketless blink "...I...found out that it was because she was keen to go to the same college I planned on enrolling in."
    $ fadein_sideimage = True
    I "....."
    O jacketless thinking "I told her she shouldn't aim for something so impossible for such a silly reason but..."
    $ fadein_sideimage = False
    O jacketless blink "...She refused to give up. She pushed herself through countless all-nighters."
    O "Not just studying, but working in order to afford tutoring."
    O jacketless irritated "She became a shell of herself, so I eventually begged her to slow down. Get some proper rest." with hpunch
    O "I even offered to go to a different college with lighter entry requirements."
    O "It didn't matter to me where I went for my education."
    O jacketless thinking "But that made her get upset with me. She said she would never forgive herself if..."
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}If...{/cps}her [t_clue]best friend[t_cluee] got pulled down by her own failure."
    play ctc_sfx sfx_heartbeat_single
    Y surprised "....." with shakeonce
    O jacketless relaxed "...So idiotic, right?"
    Y sad "N-no, I don't think she was wrong to try so hard..."
    $ renpy.music.set_volume(0.0, 0, channel="music")
    $ renpy.music.set_volume(1.0, 3, channel="music")
    play ctc_sfx "<silence 1.0>"
    O jacketless shadow "I'm talking about myself."
    Y shocked "Wh-what?" with shakeonce
    O "I know Carol-Maria very well."
    O "She's the type to [t_clue]never, EVER give up[t_cluee], no matter how hard things get."
    O jacketless dejected "That's why...I shouldn't have denied her efforts. I should have helped her the moment I learned what her goal was."
    O "It was the least I could do...after everything she had done for me..."
    Y sad "....."
    $ fadein_sideimage = True
    I "{cps=6}.....{/cps} ...Hm?{w=0.5} She's doing it again..."
    Y surprised "That ring hanging on your neck... I noticed you keep fiddling with it?"
    $ fadein_sideimage = False
    O jacketless thinking "....." with shakeonce
    O jacketless blink "...Yes. It's actually an earring, but I was too... ...I didn't want to get my ear pierced."
    O "It was a gift from Carol-Maria the day we both got successfully admitted to my first choice college."
    Y panicked "...! S-so... Carol-Maria... Her studies paid off?" with shakeonce
    O jacketless relaxed "Through some miracle, yes. The day we learned the news, she was so thrilled."
    O "All her vigour came back at once, and she tackled me, causing us both to fall to the floor."
    play ctc_sfx sfx_emotehappy
    O "And she gave me the biggest, shiniest smile I have ever seen in my whole life." with vpunch
    $ fadein_sideimage = True
    I "....."
    I "...I've never seen Ria glow like this before..."
    Y happy "That must be a good memory for you."
    $ fadein_sideimage = False
    O "It is..."
    O jacketless default "From a young age, I knew what I wanted to do. What kind of person I wanted to be."
    O jacketless thinking "But I was small. Weak. Unable to even speak my mind. And the thought of that being my identity forever haunted me."
    O jacketless blink "But then...Carol-Maria proved to me that people can grow and change."
    O "That even the lowest of people can do great things if they try."
    O jacketless thinking "I knew my path would be mired in darkness and uncertainty, but...{w=1.0} She became my [t_clue]light[t_cluee]."
    O jacketless blink "Without her, I wouldn't be even half the person I am today. ...Maybe even physically."
    Y default "{cps=6}.....{/cps} Ria...{w=0.5}{nw}"
    menu:
        extend ""
        "\"You're stronger than you think.\"":
            Y sad "I don't think you give yourself enough credit."
            O jacketless surprised "What do you mean? All I'm saying is it's thanks to Carol-Maria that I've grown out of being that timid little girl." with hpunch
            Y blink "Sure, but if I understand your story correctly, it went both ways."
            Y "Carol-Maria was a kid hanging out with a bad crowd, not knowing any better."
            Y default "Then you show up, and show her a better, brighter path to take by being {i}your{/i} friend instead."
            Y blink "And this isn't even the current-day Ria oozing with confidence and strength. The Ria that Carol-Maria went to chase after..."
            play ctc_sfx "<silence 1.0>"
            Y relaxed "...was the Ria who was [t_clue]small and quiet[t_cluee], yet stood up to a group of delinquents all the same."
            O jacketless panicked "...!" with shakeonce
            Y happy "You get what I'm saying, right?"
            O jacketless surprised "...I... I never thought about it that way..."
            O jacketless thinking "....."
            play ctc_sfx "<silence 1.0>"
            O jacketless irritated "......." with shakeonce
            Y surprised "...Ria...?"
            O jacketless shadow "Do you think... If Carol-Maria didn't chase after me that day..."
            O "Would I...still have grown? Would I still have become the person I always wanted to be?"
            Y blink "...It's hard to say."
            O jacketless dejected "Right..."
            Y leering "But there's no point in wondering about what-ifs like that." with shakeonce
            Y thinking "Maybe Carol-Maria was the key to your growth. Or maybe she wasn't."
            Y blink "Either way, {i}you{/i} were the one who pulled her into your life."
            Y default "The tiny little Oriana of the past had guts. And through those guts, she obtained other things essential to her growth."
            Y relaxed "And now, thanks to her, we're here. {i}You're{/i} here. I think that's worth easing up on her a bit, don't you?"
            O jacketless shadow "....."
            $ fadein_sideimage = True
            scene cg ria hearttoheart2:
                xalign 0.5 yalign 1.0 zoom 1.7 blur 20
                linear 5.0 blur 0
            with dissolve
            I "{cps=6}.....{/cps} ...I've been talking quite a bit. Getting kinda embarrassed..." with hpunch
            Y worried2 "O-or you know, maybe I'm misreading all this! After all, I've never met Carol-Ma...{cps=1} {/cps}{nw}" with hpunch
            $ fadein_sideimage = False
            play ctc_sfx "<silence 1.0>"
            extend surprised "Uh, Ria?"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            I "...!!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            scene cg ria hearttoheart2:
                xalign 0.5 yalign 1.0 zoom 1.7
                easein 4.0 yalign 0.0
            pause 5.0
            scene cg ria hearttoheart2 at reset with dissolvemed
            O jacketless crying2 "..... {size=-10}*sniff*{/size}" with hpunch
            $ fadein_sideimage = False
            play ctc_sfx sfx_heartbeat_single
            Y surprised "....." with shakeonce
            O jacketless crying "...Sorry, I... I need a moment."
            Y "....."
            Y relaxed "...Okay."
            O jacketless crying2 "{size=-10}*sniff*{/size} ......." with shakeonce
            O "....... ...{size=-10}*hic*{/size}" with shakeonce
            $ fadein_sideimage = True
        "\"You're being too harsh with yourself.\"":

            Y thinking "The way you describe your past self... It almost sounds like you resent her. Even now."
            O jacketless blink "....."
            Y leering "But I don't think it's healthy to think so negatively about yourself. After all--" with hpunch
            play ctc_sfx "<silence 1.0>"
            O jacketless shadow "[name_player]. I didn't tell you the whole truth earlier."
            Y panicked "H-huh?" with shakeonce
            O "I said I woke up from a nightmare where I kept getting killed over and over."
            play ctc_sfx sfx_heartbeat_single
            O "But...there were times where it was [t_clue]me doing the killing[t_cluee]." with shakeonce
            play ctc_sfx "<silence 1.0>"
            Y panicked "...! That's..." with shakeonce
            O "I talk big about how we shouldn't kill anyone, acting like some symbol of morality when..."
            O jacketless dejected "...I'm perfectly capable of losing myself in this madness as well."
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            $ renpy.music.set_volume(0.5, 0, channel="music")
            $ renpy.music.set_volume(1.0, 2, channel="music")
            window auto hide None
            show bg black
            show oriana_raw deranged at mycenter_closeup, grayscale_on
            with custom_flashquick()
            scene cg ria hearttoheart
            with dissolvemed
            pause 1.0
            I "....."
            O jacketless blink "...Hm. Maybe it was a bit arrogant of me to think I've changed. I'm still the same."
            $ fadein_sideimage = False
            O jacketless irritated "A weak, cowardly little girl who hides behind an air of superiority... Unable to take action where it counts..." with shakeonce
            Y angry "You need to stop." with shakeonce
            O jacketless dejected "....."
            Y leering "Did you already forget what you did just a few hours ago?"
            O "What I...did...?"
            Y "When I woke up from a nightmare and rushed down to the foyer to find you."
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            scene bg foyer at grayscale_on
            show oriana_raw irritated2 at myleft, grayscale_on
            show cecilia_raw happy at myright, grayscale_on, backedaway_on
            with custom_flashbulblong()
            pause 1.0
            Y sad "If it weren't for you, I might have just stayed frozen up."
            $ fadein_sideimage = False
            Y leering "We would never have gotten this far. Just a little bit away from reaching the end of this wretched game."
            O jacketless shadow "....."
            O "...What if..."
            O "What if this killing game finally comes to an end today because...{w=0.5}{nw} "
            play ctc_sfx "<silence 1.0>"
            show bg black
            hide oriana_raw
            hide cecilia_raw
            extend "I'm the one who kills someone?" with shakeonce
            play ctc_sfx "<silence 1.0>"
            Y wince "....." with shakeonce
            O jacketless dejected "...Your face says it all, [name_player]."
            O "Admit it. It's possible."
            O jacketless shadow "After all, you've seen me do it before..."
            Y blink "You won't do it."
            O "And how can you possibly know that?"
            play ctc_sfx "<silence 1.0>"
            Y default "Because you could never do that to Carol-Maria."
            show cg ria hearttoheart
            play ctc_sfx sfx_heartbeat_single
            O jacketless panicked "...!!!{w=1.0} A-are you..." with shakeshort
            Y thinking "Sure, maybe she's not here right now... Or maybe she doesn't hold you in regards as high as we think..."
            O jacketless surprised "....."
            Y default "But knowing what Carol-Maria saw in you...{w=0.5} Knowing how hard she worked to keep being with you..."
            Y blink "Surely you can't face such a person with blood staining your hands?"
            O jacketless shadow "...!" with shakeonce
            Y relaxed "You would never allow it.{w=0.5} Not when she's waiting for you to come back home."
            O jacketless blink "....."
            play ctc_sfx "<silence 1.0>"
            O "{cps=6}.......{/cps}"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            scene cg ria hearttoheart2 with dissolvemed
            pause 1.0
            O jacketless crying2 "{size=-10}*sniff*{/size}" with shakeonce
            $ fadein_sideimage = False
            Y panicked "R-Ria...?" with shakeonce
            O jacketless crying "...I'm sorry... *sniff* I just..." with hpunch
            Y surprised "....."
            Y relaxed "...It's fine. Take your time."
            O jacketless crying2 "*sob* Grk...! I..." with shakeonce
            O "Euugh... *hic* Aaaugh..." with shakeshort
            achieve RIA_H2H

    $ show_side_oriana = False
    $ fadein_sideimage = True
    scene cg ria hearttoheart2:
        xalign 0.5 yalign 0.0 zoom 1.1
        easein 10.0 zoom 1.3
    with dissolve
    I "Ria...{w=0.5} I don't know what it is, but something deep inside me wants to protect you at all costs..."
    I "...But I know you're strong. Any normal human being in this situation would've lost all hope by now."
    I "I think...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " No, I know for sure that I will be [t_clue]relying on you[t_cluee] for the challenges up ahead..." with shakeonce
    stop music fadeout 5.0
    scene bg black with dissolveslow
    pause 2.0
    $ persistent.unlock_cg_ria_hearttoheart = True
    $ seen_ria_hearttoheart = True
    scene bg masterbedroom

    show oriana jacketless blink at mycenter
    with dissolveslow
    O "{cps=6}..........{/cps}"
    I "...She's finally calmed down."
    Y surprised "Oh yeah, back to the original question... The reason you joined..."
    $ fadein_sideimage = False
    Y blink "...Actually, I think I can guess. You joined the Occult Club because Carol-Maria--"
    $ fadein_sideimage = True
    O jacketless thinking "Became enamoured with it, yes."
    O jacketless default "It was during a student club exhibition event where Cecilia ran up to the two of us and said--"
    play ctc_sfx sfx_knockhard
    window auto hide None
    show bg black
    hide oriana
    with custom_flashquick()
    pause 0.5
    I "...!!" with shakeshort
    return

label d3a2:
    show bg black
    $ show_side_cecilia = True
    $ show_side_oriana = True
    X "Pst! [name_player]! You there?" with hpunch
    I "Huh? Oh, looks like Cece's back..."
    Y blink "You can stay here, Ria. I'll go talk to her."
    $ fadein_sideimage = False
    O jacketless thinking "...Okay."
    $ fadein_sideimage = True
    play ctc_sfx sfx_steps
    scene bg black with dissolve
    pause 1.0
    Y surprised "...Cece?"
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotehappy
    C hidden "Yep, it's me, Cece! Can you open the door?" with vpunch
    Y thinking "The coast is clear, right?"
    C "Uh... You can say that. Actually, you should probably come take a look at this..."
    Y leering "What...? Okay, hang on, let me unblock the door..."
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    $ show_side_oriana = False
    window auto hide
    play sound sfx_furnituredrag
    with shakeshort
    pause 2.0
    play sound sfx_dooropen
    pause 2.0
    I "And upon opening the door out into the hall..."
    play ctc_sfx sfx_heartbeat_single
    I "A sick surprise was awaiting me, seemingly void of any purpose beyond the amusement of a [t_clue]maniac[t_cluee]..." with hpunch
    play ctc_sfx "<silence 1.0>"
    scene bg hallway
    show cecilia sad at mycenter
    with dissolveslow
    pause 1.0
    Y surprised "...What is it?"
    C thinking "...Look here. At the floor."
    Y thinking "Huh? {cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    Y depressed "...!! Th-that's..." with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolvemed
    call save_file_name_update (3, "d3a2")
    scene cg deaddog:
        parallel:
            xalign 1.0 yalign 0.8 zoom 1.5
            linear 10.0 yalign 0.0
        parallel:
            xoffset 0 yoffset 0 matrixcolor BrightnessMatrix(0.0)
            choice:
                pause 1.5
            choice:
                pause 2.5
            linear 0.05 xoffset 10 yoffset 10 matrixcolor BrightnessMatrix(-0.15)
            linear 0.05 xoffset -10 yoffset -10 matrixcolor BrightnessMatrix(0.0)
            linear 0.05 xoffset 10 yoffset 0 matrixcolor BrightnessMatrix(-0.3)
            linear 0.05 xoffset 0 yoffset -10 matrixcolor BrightnessMatrix(0.0)
            repeat
    with dissolveslow
    $ persistent.unlock_cg_deaddog = True
    pause 3.0
    scene cg deaddog:
        xalign 1.0 yalign 0.0 zoom 1.1
        easein 4.0 zoom 1.0
    with dissolvemed
    pause 5.0
    Y depressed "{cps=6}.....{/cps}{cps=1} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend "[name_dog]...?{nw}"
    play ctc_sfx "<silence 1.0>"
    play music bgm_criminal
    $ show_music_info_timer = music_info_pop_out_time()
    extend "" with shakeonce
    Y afraid2 "...Why? Why is [name_dog]...?"
    $ show_side_cecilia = True
    C thinking "I don't know. After I finished my business in the attic, I came down and found him already dead and lying there."
    Y afraid "Th-then... It could've only been...th-that zombie?" with hpunch
    C blink "Who knows? But considering the lack of blood, it's safe to say that [name_dog] was killed somewhere else and brought here after."
    Y pained "Wh-what? Why would anyone do that?" with shakeonce
    C determined "...It must be a warning."
    Y shocked "A warning? For what?"
    C thinking "After I found [name_dog] here, I checked the front door downstairs. It was still [t_clue]shut tight[t_cluee]."
    C "Which means that [name_dog] losing his life doesn't qualify for opening that door."
    play ctc_sfx "<silence 1.0>"
    Y troubled "...Then, that means..."
    play ctc_sfx sfx_heartbeat_single
    C determined "[t_clue]One of us humans HAS to die[t_cluee] in order for anyone to escape." with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    scene bg hallway
    show cecilia thinking at mycenter
    with dissolvemed
    Y angry "We can't go back to that! We're so close to the truth! Once we find the true mastermind--" with shakeonce
    C sad "But there was no such person in the basement, now was there?"
    Y shocked "That's..."
    C smug "Unless you want to claim that mindless, rotting zombie is somehow the cunning mastermind behind all this."
    Y pained "B-but he might be exactly that! Maybe he's pretending to be mindless? Or he lost his sanity just before he attacked..." with shakeshort
    C thinking "Either way, what do you propose we do, then?"
    C sad "It's not like we have any clue as to where that zombie went."
    C determined "And as you recall, we were given [t_clue]20 hours[t_cluee]. Time is running out."
    Y shocked "Cece... What are you doing?"
    $ fadein_sideimage = False
    Y "We're supposed to be a team now, right?"
    play ctc_sfx sfx_heartbeat_single
    Y "Why are you trying to [t_clue]restart the killing game[t_cluee]?" with shakeonce
    $ fadein_sideimage = True
    C surprised "Restart the... That's not what I'm trying to do! I'm just being realistic here!" with shakeonce
    C pout "We know from your time traveling that the door definitely opens if one of us dies! And if [name_dog] doesn't count..." with shakeshort
    C shouting "What other choices do we have?! There's no other way out!" with shakeshort
    I "....."
    I "...No. There's still one option."
    show cecilia thinking

label d3a2_escape_choice:
    I "...We can escape by...{nw}" with shakeonce

    menu:
        extend ""
        "Digging through the underground passage":
            Y wince "The hatch in the basement leads to an underground passage that stops short, right?"
            $ fadein_sideimage = False
            Y leering "If we can find a shovel or something similar, than we can--" with hpunch
            $ fadein_sideimage = True
            C sad "Didn't someone mention before that that passage gets [t_clue]engulfed in flames[t_cluee] when {i}you{/i} enter it, [name_player]...?"
            Y wince "Ah... Crap, that's right..." with hpunch
            C thinking "We won't get a lot of digging done if we're being burned alive while doing it. Any other ideas?"
            jump d3a2_escape_choice
        "Using what Cece learned in the attic":
            Y leering "...You said you were going to the attic to read that book about the Gate to {color=#ff0000}Hell{/color}, right?"
            $ fadein_sideimage = False
            Y "Did you find anything that can help us escape?"
            $ fadein_sideimage = True
            C surprised "Oh yeah, that! Uh..." with shakeonce
            C sad "No, it turns out I was wrong. That book only explains how to open and close a Gate to Hell."
            C thinking "This house...isn't exactly one of those."
            Y wince "Darn... Okay, different plan..." with hpunch
            jump d3a2_escape_choice
        "Killing the zombie":
            stop music fadeout 3.0
    Y thinking "...Wait. You said a \"human\" needs to die in order for that door to open..."
    $ fadein_sideimage = False
    Y "What if we just find and kill that zombie?"
    $ fadein_sideimage = True
    C sweatdrop "Um, [name_player]? By definition, zombies are already dead--"
    Y blink "No, let me rephrase that."
    $ fadein_sideimage = False
    Y leering "Let's find and kill that human being that's pretending to be a zombie."
    $ fadein_sideimage = True
    C surprised "Huh?{w=0.5} You think that killer zombie attack was all an act?{nw}" with hpunch

    menu:
        extend ""
        "\"Yes, I'm sure.\"":
            Y blink "I'm positive he was faking it."
            C determined "And what makes you so sure?"
            Y leering "Because of [name_dog]."
            C thinking "Huh? You mean this dead dog here?"
            Y thinking "It's like you said, if the dog was killed somewhere else and left here as a warning..."
            $ fadein_sideimage = False
            play ctc_sfx "<silence 1.0>"
            Y leering "...who could have possibly done something like that?" with hpunch
            $ fadein_sideimage = True
            C surprised "Ah!" with shakeonce
        "\"I don't know!\"":
            Y pained "I don't know, but we don't have any other choice!" with shakeonce
            $ fadein_sideimage = False
            Y pained2 "If that man isn't the mastermind, and is really just a walking corpse, then we're all good as dead!" with hpunch
            Y angry "We have to [t_clue]believe[t_cluee] that killing him will let us escape!" with shakeonce
            $ fadein_sideimage = True
            C thinking "{cps=6}.....{/cps} \"Believe\", huh...?"
    C blink "{cps=6}.....{/cps} ...Hmm! I guess that makes sense."
    C smile "Alright, I guess it's not like things will get any worse for us if it turns out killing that guy doesn't open the door."
    C thinking "Well... Other than a man's blood staining our hands for all eternity."
    Y blink "...I'm ready to bear that sin."
    C sad "Maybe {i}you{/i} are, but what about the rest of us?"
    C "You realize I'm the only one strong enough to take that man on in a fight?"
    C smug "What if he isn't the mastermind? An innocent man's blood will stain these maidenly hands of mine."
    Y leering "Don't worry about that. I... I'll take responsibility for it."
    I "I'm already dead, after all... What's another sin or two to stain {i}my{/i} hands?"
    play ctc_sfx sfx_emotehappy
    C happy "Ahaha~ That was quite a line you just used, [name_player]!" with vpunch
    play music bgm_tension
    $ show_music_info_timer = music_info_pop_out_time()
    C smile "Okay. Let's go find that zombie! I actually already checked [t_clue]all the rooms on the second floor[t_cluee] and didn't see him." with shakeonce
    C blink "He's probably somewhere in the lower floors. Wanna head down now?"
    Y leering "Yeah. We need to put an end to this."
    play ctc_sfx "<silence 1.0>"
    I "This might even be how the killing game finally comes to an end..." with hpunch
    $ show_side_oriana = True
    O hidden "[name_player]...?"
    play ctc_sfx sfx_dooropen
    play sound sfx_steps
    $ show_side_oriana = False
    window auto hide
    pause 0.7
    show cecilia_raw as cecilia at mycenter_to_myright, backedaway_on
    pause 0.3
    show oriana thinking at myleft with dissolvemed
    O surprised "What's...going on...?"
    Y panicked "Ah! R-Ria?! Y-you're okay to move?" with shakeshort
    play ctc_sfx "<silence 1.0>"
    I "Oh crap, she's gonna see--" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O depressed "{cps=6}.....{/cps} [name_dog]? ...What happened to [name_dog]?"
    play ctc_sfx "<silence 1.0>"
    Y troubled "....." with hpunch
    show cecilia sad at myright, backedaway_off
    C "....."
    O "Hey... Why won't you answer me...?" with shakeonce
    C thinking "Look, we don't have a lot of time left, [name_player]. Let's get moving."
    I "...Yeah, she's right. Except..."
    scene cg deaddog
    with dissolvemed
    I "Looking at [name_dog] again, this scene looks...unnatural..."
    play ctc_sfx "<silence 1.0>"
    I "Maybe I should actually take a closer look before moving on?{nw}"
    menu:
        extend ""
        "Investigate [name_dog]'s corpse":
            $ show_side_cecilia = True
            $ show_side_oriana = True
            Y sad "Sorry, Cece, could you give me a moment to inspect [name_dog]'s body really quick?" with hpunch
            $ fadein_sideimage = False
            C surprised "Wh-what? Why?" with shakeonce
            Y blink "There's just something bothering me about this scene..."
            C thinking "....."
            C blink "...Okay, I guess that zombie isn't going anywhere."
            C smile "Go ahead and take your time."
            Y default "Thanks, Cece."
            play ctc_sfx "<silence 1.0>"
            O dejected "....."
            $ fadein_sideimage = True
            I "The main thing bothering me is that it's not really clear [t_clue]{i}how{/i} he died[t_cluee]..."
            I "I can probably do this [t_clue]quickly[t_cluee]..."
            $ show_side_cecilia = False
            $ show_side_oriana = False
            $ d3a2_dog_clue1 = False
            $ d3a2_dog_clue2 = False
            $ d3a2_dog_clue3 = False
            $ d3a2_dog_clue4 = False
            $ d3a2_dog_clue5 = False
            $ d3a2_dog_clue6 = False
            $ d3a2_dog_clue7 = False

            $ investigation_location = "d3a2_dog"


            $ investigation_clues_required = 7
            $ investigation_clues_required_found = 0
            $ investigation_clues_optional = 0
            $ investigation_clues_optional_found = 0
            jump d3a2_dog_investigation
        "\"No, there's no need...\"":

            I "...No, I suppose finding that zombie is more important." with hpunch
            Y blink "Okay, let's get moving, Cece."
            jump d3a2_dog_end

label d3a2_dog_investigation:
    $ renpy.choice_for_skipping()
    if investigation_clues_required_found == investigation_clues_required:
        achieve 100_DOG
    scene cg deaddog with dissolvequick
    call screen pac_d3a2_dog with dissolvequick
    if investigation_location != None:
        jump d3a2_dog_investigation
    else:
        jump d3a2_dog_end

label d3a2_dog_end:
    scene bg black with dissolvemed
    scene bg hallway
    show oriana dejected at mycenter
    with dissolvemed
    O panicked "[name_player], wait! I--{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    show oriana injured at crouch with custom_flashquick()
    extend " ...Nrgh!" with shakelong
    Y panicked "R-Ria, you should probably get a little more rest..." with hpunch
    window auto hide
    $ _last_say_who = "O"
    show oriana irritated at standup
    pause 0.5
    O "I... I-I'm sorry, you're right..." with shakeonce
    O leering "...Listen to me, [name_player]."
    Y surprised "Y-yeah? I'm listening..."
    play ctc_sfx "<silence 1.0>"
    O "...Stay extremely vigilant. [t_clue]Don't let your guard down[t_cluee], even for a second." with shakeonce
    Y blink "...Okay, I will."
    $ fadein_sideimage = False
    Y default "But I should be fine if I'm with Cece."
    $ fadein_sideimage = True
    O irritated2 "....."
    stop music fadeout 5.0
    play ctc_sfx "<silence 1.0>"
    O "{cps=12}That's...what I mean...{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y surprised "Huh?"
    O "You said the killing game will end soon, right? And we're almost at the end of the time limit too..."
    O "If the two of you are alone together, and Cecilia decides that it's too risky to keep everyone alive..."
    play ctc_sfx "<silence 1.0>"
    Y "....."
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    show bg hallway:
        blur 20
        linear 5.0 blur 0
    Y depressed "{cps=6}.....{/cps}" with shakeonce
    $ fadein_sideimage = True
    O annoyed2 "You should go now, before she suspects us. ...Be careful, [name_player]."
    $ show_side_cecilia = True
    C happy "[name_player], come on~" with hpunch
    $ fadein_sideimage = False
    $ show_side_cecilia = False
    play ctc_sfx "<silence 1.0>"
    Y shadow "R-right..." with hpunch
    $ fadein_sideimage = True
    I "....."
    play ctc_sfx "<silence 1.0>"
    window auto hide None
    scene bg black with custom_flashquick()
    window auto show None
    I "No, I... I trust her..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    I "We're so close... It can't fall apart now...right...?"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 2.0
    call save_file_name_update (3, "d3a2_zombiehunt")
    play sound sfx_steps fadein 1.0
    scene bg foyer
    with dissolveslow
    pause 2.0
    scene bg frontdoor with dissolvemed
    pause 2.0
    I "The front door is still closed, just like Cece said..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    scene bg foyer with dissolvemed
    $ _last_say_who = "C"
    show cecilia thinking at mycenter
    with dissolve
    C "Looks like he's nowhere in sight from here. Guess we'll have to check one of the rooms."
    play ctc_sfx "<silence 1.0>"
    Y shadow "Right..." with hpunch
    C surprised "Huh? [name_player], what's wrong? You suddenly seem down."
    Y panicked "Ah-- N-no, I'm fine!" with shakeshort
    C sad "Come on... You need to focus here!"
    show cecilia pout at hop
    C "We can literally get ambushed at any point! Keep your ears peeled and your eyes on alert!"
    Y troubled "I-I know..." with hpunch
    I "I could...get ambushed..." with shakeonce
    C blink "We have the [t_clue]kitchen[t_cluee], the [t_clue]bathroom[t_cluee], and the [t_clue]lounge[t_cluee]. Which room do you want to check out, [name_player]?"
    Y wince "Uh... Let's see..." with vpunch
    $ day3_checked_kitchen = False
    $ day3_checked_bathroom = False
    $ day3_checked_lounge = False

label d3a2_start_investigation:
    scene bg foyer with dissolve
    I "Okay then...{w=0.5} Let's go to..."
    menu:
        "Investigate the [t_clue]Kitchen[t_cluee]" if not day3_checked_kitchen:
            Y thinking "Let's check out the kitchen. Maybe that's where he's been hiding this whole time."
            $ _last_say_who = "C"
            show cecilia blink at mycenter
            with dissolve
            C "Good idea. Plus, if you're right that he's just pretending to be a zombie, he might be eating something."
            C smile "Let's take a [t_clue]stealthy approach[t_cluee] and ambush him."
            scene bg foyer with dissolve
            I "Okay, opening the door to the dining room...{nw}"

            menu:
                extend ""
                "Open the door quickly":
                    window auto hide
                    play sound sfx_dooropenloud
                    scene bg diningroom with custom_flashquick()
                    window auto show None
                    Y shouting "GOTCHA!!" with shakelong
                    $ fadein_sideimage = False
                    $ show_side_cecilia = True
                    C surprised "Wha-- [name_player]?!" with shakeonce
                    $ fadein_sideimage = True
                    $ show_side_cecilia = False
                    scene bg diningroom
                    show cecilia determined knife at mycenter
                    with custom_flashquick()
                    play sound sfx_knifebrandish
                    with hpunch
                    pause 3.0
                    C "....."
                    play sound sfx_knifeequip
                    C sad "Whew... Guess we're in the clear."
                    play ctc_sfx sfx_emoteshout
                    C pout "[name_player]! I told you we should take a stealthy approach!" with shakeshort
                    Y wince "Nrgh... S-sorry, I'm kind of on edge..." with hpunch
                    show cecilia thinking
                "Open the door carefully":
                    scene bg black with dissolvemed
                    pause 0.5
                    with shakeonce
                    play sound [sfx_dooropenslow_unlatch, "<silence 1.5>", sfx_dooropenslow_move]
                    pause 3.0
                    scene bg diningroom:
                        matrixcolor BrightnessMatrix(-0.5)
                        easein 10.0 matrixcolor BrightnessMatrix(0.0)
                    with dissolvemed
                    pause 3.0
                    I "....."
                    I "No sign of him..."
                    $ _last_say_who = "C"
                    scene bg diningroom
                    show cecilia thinking at mycenter
                    with dissolve

            C "Hmm... I'm not hearing any sounds coming from the kitchen either."
            Y leering "We should still take a look."
            C determined knife "Yep. Just stay behind me."
            scene bg black with dissolveslow
            pause 1.0
            scene bg kitchen:
                matrixcolor BrightnessMatrix(-0.5)
                easein 10.0 matrixcolor BrightnessMatrix(0.0)
            with dissolvemed
            pause 3.0
            I "...He's not here either."
            $ _last_say_who = "C"
            scene bg kitchen
            show cecilia sad at mycenter
            with dissolve
            C "Hrm... Guess he wasn't here eating something after all. There goes our great ambush plan..."
            I "{cps=6}.....{/cps} ...Huh? Wait, eating...?"
            Y default "Are you hungry at all, Cecilia?"
            C thinking "Hmm? No, not really. How about you, [name_player]?"
            play ctc_sfx sfx_emotequestion
            Y thinking "No, but... Isn't that strange?"
            $ fadein_sideimage = False
            Y "The last time we ate anything was [t_clue]almost a day ago[t_cluee]. After we had that long discussion."
            play ctc_sfx "<silence 1.0>"
            Y panicked "How are we [t_clue]still not hungry[t_cluee]?" with shakeonce
            $ fadein_sideimage = True
            C surprised "Ah...!" with shakeonce
            C thinking "Y-you're right! That's...really weird..."
            I "....."
            C happy "Oh, you know what? It's probably just the [t_clue]adrenaline[t_cluee]!"
            C grin "I mean, we're in a really intense situation! We're trying to kill a man before he can kill us!"
            Y surprised "...Right..."
            play ctc_sfx "<silence 1.0>"
            I "Something feels wrong here..." with hpunch
            C thinking "Anyway, let's go back to the foyer, [name_player]."
            Y sad "Yeah, let's go..."
            play ctc_sfx "<silence 1.0>"
            scene bg black with dissolveslow
            play ctc_sfx sfx_steps
            pause 1.0
            scene bg foyer with dissolveslow
            $ day3_checked_kitchen = True

        "[u_check]Investigate the [t_clue]Kitchen[t_cluee]" if day3_checked_kitchen:
            I "We already checked the dining room and the kitchen. No sign of the zombie there."

        "Investigate the [t_clue]Bathroom[t_cluee]" if not day3_checked_bathroom:
            Y leering "Let's check out the bathroom. It's a little small, but he could be hiding in there."
            $ _last_say_who = "C"
            show cecilia thinking at mycenter
            with dissolve
            C "Yeah, maybe he's taking care of his business in there?"
            C smug "Considering how small that bathroom is, we could probably [t_clue]burst through the door[t_cluee] and catch him by surprise."
            play sound sfx_knifebrandish
            C blink knife "I'll have my knife at the ready." with hpunch
            scene bg foyer with dissolve
            I "Okay, let's open the bathroom door...{nw}"

            menu:
                extend ""
                "Open the door quickly":
                    window auto hide
                    play sound sfx_dooropenloud
                    scene bg bathroom with custom_flashquick()
                    window auto show None
                    Y shouting "GO, CECE!!" with shakelong
                    show cecilia shouting at mycenter_return
                    with custom_flashquick()
                    C "ATTAAAACK!!" with shakelong
                    C determined knife "....."
                    I "....."
                    C "....."
                    play ctc_sfx sfx_knifeequip
                    C sad "Darn. Looks like he's not in here."
                    Y wince "Dammit, where {i}is{/i} he...?" with hpunch
                "Open the door carefully":
                    scene bg black with dissolvemed
                    pause 0.5
                    with shakeonce
                    play sound [sfx_dooropenslow_unlatch, "<silence 1.5>", sfx_dooropenslow_move]
                    pause 3.0
                    scene bg bathroom:
                        matrixcolor BrightnessMatrix(-0.5)
                        easein 10.0 matrixcolor BrightnessMatrix(0.0)
                    with dissolvemed
                    pause 3.0
                    I "....."
                    I "Looks like nobody's in here..."
                    $ _last_say_who = "C"
                    scene bg bathroom
                    show cecilia sweatdrop at mycenter
                    with dissolve
                    C "...Uh... [name_player]? Weren't you listening to my suggestion?"
                    Y thinking "Yes, but it's still good to be careful. He could've been waiting for us to open it."
                    C surprised "Oh! Yeah, that's a good point."
                    I "....."

            C thinking "Hmm. Come to think of it, [name_player], have you ever checked this bathroom out before?"
            if investigated_bathroom:
                Y surprised "I...think so? There were some times I didn't get the chance to, though."
                C smile "Any...interesting events happen to you?"
                I "....."
                I "Right, I'd run into [name_dog] and..."
                play ctc_sfx "<silence 1.0>"
                play sound sfx_flashback
                scene bg bathroom at grayscale_on
                show dog at mycenter, grayscale_on
                with custom_flashbulblong()
                pause 2.0
                I "He'd suddenly run off, and look at me as though he wanted me to chase him..."
                I "Just what was he up to...?" with shakeonce
                scene bg black with dissolvemed
                $ _last_say_who = "C"
                scene bg bathroom
                show cecilia at mycenter
                with dissolvemed
                C surprised "[name_player]? What's up, did you remember something?"
                Y thinking "Yeah, but...I don't think it's important right now."
            else:

                Y thinking "{cps=6}.....{/cps} ...Wait, I...I don't think I ever did..."
                play ctc_sfx sfx_emotequestion
                I "That's weird... I wonder why? I doubt I [t_clue]intentionally avoided it[t_cluee] or something..." with hpunch
                C sad "Oh. Okay, never mind, then."
                achieve BATHROOM_LATE
                Y surprised "...?"
                C sweatdrop "...Uh... D-does anything come to mind NOW?"
                Y worried "You mean...in this bathroom? Not really..."

            C thinking "...You sure? The more clues we have, the better our chances at understanding the zombie's movements."
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "C'mon, even the tiniest details may help! Maybe you looked in the mirror and [t_clue]noticed something unusual[t_cluee]?"
            Y thinking "...Unusual?"
            scene cg mirror:
                xalign 0.4 yalign 0.4 zoom 1.3
                easein 6.0 xalign 0.5 yalign 0.5 zoom 1.0
            with dissolvemed
            pause 2.0
            Y surprised "....."
            I "{cps=6}.....{/cps} {nw}"
            play ctc_sfx sfx_emotequestion
            extend "...No?" with hpunch
            I "There's nothing unusual...except..."
            Y wince "....."
            $ fadein_sideimage = False
            Y "Is this...{i}really{/i} my own face...?" with hpunch
            $ fadein_sideimage = True
            I "I can't believe I'm still missing memories {i}this{/i} important..."
            $ _last_say_who = "C"
            scene bg bathroom
            show cecilia sad at mycenter
            with dissolvemed
            C "....."
            C thinking "Well, it was worth a shot."
            I "...Huh?"
            C default "Let's head back to the foyer."
            Y thinking "Y-yeah, let's."
            play ctc_sfx sfx_steps
            scene bg black with dissolvemed
            scene bg foyer with dissolvemed
            pause 1.0
            $ day3_checked_bathroom = True

        "[u_check]Investigate the [t_clue]Bathroom[t_cluee]" if day3_checked_bathroom:
            I "We already checked the bathroom, and he wasn't in there."

        "Investigate the [t_clue]Lounge[t_cluee]" if not day3_checked_lounge:
            Y blink "Let's head for the lounge. I get the feeling he could've gone back to the basement."
            $ _last_say_who = "C"
            show cecilia wink at mycenter
            with dissolve
            C "I admire your courage, [name_player]!"
            C blink "Heh. It's funny to think that just earlier, we were climbing up the floors, hoping to avoid the zombie..."
            C smug "And now here we are, doing the opposite of both."
            Y sad "....."
            C sweatdrop "...Alright, guess you're not in the mood for irony right now."
            play sound sfx_knifebrandish
            C blink knife "I'll leave opening the door to you. I'll just be ready for anything." with hpunch
            scene bg foyer with dissolve
            I "Okay, let's open the door to the lounge...{nw}"

            menu:
                extend ""
                "Open the door quickly":
                    window auto hide
                    play sound2 sfx_dooropenloud
                    scene bg lounge with custom_flashquick()
                    window auto show None
                    Y angry "NOW!!" with shakeshort
                    show cecilia determined knife at mycenter
                    with custom_flashquick()
                    play sound sfx_knifebrandish
                    C "...!!" with hpunch
                    C "....."
                    Y leering "....." with hpunch
                    C "....."
                    play ctc_sfx sfx_knifeequip
                    C sad "I guess he's not in the lounge, [name_player]."
                "Open the door carefully":
                    scene bg black with dissolvemed
                    pause 0.5
                    with shakeonce
                    play sound [sfx_dooropenslow_unlatch, "<silence 1.5>", sfx_dooropenslow_move]
                    pause 3.0
                    scene bg lounge:
                        matrixcolor BrightnessMatrix(-0.5)
                        easein 10.0 matrixcolor BrightnessMatrix(0.0)
                    with dissolvemed
                    pause 3.0
                    I "....."
                    I "I don't see him... Is the room empty...?" with hpunch
                    $ _last_say_who = "C"
                    scene bg lounge
                    show cecilia determined knife at mycenter
                    with dissolve
                    C "....."
                    window auto hide
                    show cecilia determined knife at myleft with move
                    pause 0.5
                    show cecilia determined knife at myright with move
                    pause 1.0
                    play ctc_sfx sfx_knifeequip
                    show cecilia sad at mycenter with move
                    C "No sign of him, [name_player]."

            Y thinking "Then I guess we should check the basement next."
            C thinking "We, uh...never closed the door to it, right?"
            C determined knife "Let me check it out first."
            window auto hide
            hide cecilia with dissolvemed
            pause 1.0
            I "....."
            scene bg lounge:
                xalign 0.2 yalign 0.2 zoom 1.5
            with dissolvemed
            pause 1.0
            Y sad "....."
            I "Is that zombie really not the father of the house? Ria was so sure the culprit is the father, but..."
            play ctc_sfx "<silence 1.0>"
            play sound sfx_flashback
            scene bg basement at grayscale_on
            show oriana injured at mycenter, grayscale_on
            with custom_flashbulblong()
            O "He's... Whoever this man is... He's dead."
            O "If he's the father of the house... If he's the mastermind behind the killing game..." with shakeonce
            play ctc_sfx sfx_heartbeat_single
            O horrified "Then the three of us are really [t_clue]all alone[t_cluee] in here! There's no way out of having one of us DIE!" with shakeshort
            scene bg black with dissolvemed
            scene bg lounge:
                xalign 0.2 yalign 0.2 zoom 1.5
            with dissolvemed
            I "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            I "What should I be doing...?"
            play ctc_sfx "<silence 1.0>"
            I "I want to know the truth, but... We also need to believe we can escape..." with shakeonce
            I "The mastermind...{w=1.0} The zombie...{w=1.0} The father of the house..."
            I "Are they all really the same person?{w=0.5} Or maybe one of these labels is...{w=0.5}{nw}"
            play ctc_sfx sfx_heartbeat_single
            extend "[t_clue]a fake[t_cluee]...?" with shakeonce
            $ show_side_cecilia = True
            C determined "[name_player]."
            $ show_side_cecilia = False
            scene bg basement entrance light
            show cecilia determined at mycenter
            with dissolvemed
            C "I couldn't hear anything so I tried going down for a bit."
            C sad "He's...not there. Not in the library either."
            Y wince "I see..." with hpunch
            C thinking "Do you want to check it out for yourself?{nw}"

            menu:
                extend ""
                "\"Yeah, I will.\"":
                    Y leering "Yeah, just to be sure."
                    play ctc_sfx "<silence 1.0>"
                    C blink knife "Okay, I'll be right [t_clue]behind[t_cluee] you with my knife at the ready."
                    play ctc_sfx sfx_heartbeat_single
                    Y depressed "...!" with shakeonce
                    play ctc_sfx "<silence 1.0>"
                    I "Wait... I..." with hpunch
                    C surprised "Huh? Why'd you freeze up? Did you change your mind?"
                    Y troubled "N-no, I'm...okay..." with hpunch
                    play ctc_sfx "<silence 1.0>"
                    I "{cps=6}..........{/cps}"
                    C determined knife "C'mon, stay focused! Even with the lights on, it's still pretty dark down there."
                    I "I guess there's no [t_clue]backing[t_cluee] out of this..."
                    play ctc_sfx "<silence 1.0>"
                    scene bg black with dissolveslow
                    pause 7.8
                    I "{cps=6}.....{/cps}"
                    play ctc_sfx "<silence 1.0>"
                    I "{cps=6}.......{/cps}"
                    play ctc_sfx "<silence 1.0>"
                    window auto hide
                    pause 7.8
                    scene bg basement nocorpse:
                        matrixcolor BrightnessMatrix(-0.5)
                        easein 10.0 matrixcolor BrightnessMatrix(0.0)
                    with dissolveslow
                    pause 5.0
                    I "....."
                    I "No sign of him..."
                    $ _last_say_who = "C"
                    scene bg basement nocorpse
                    show cecilia sad at mycenter
                    with dissolve
                    C "See? I told ya, not a single sign of life. Or reanimated life."
                    C thinking "Look, check the library."
                    scene bg basement nocorpse with dissolve
                    scene bg basement nocorpse:
                        xalign 0.0 yalign 0.6 zoom 1.0
                        easein 1.0 zoom 1.5
                    pause 2.0
                    scene bg black with dissolvemed
                    play sound sfx_dooropen
                    pause 0.5
                    scene bg library right with dissolvemed
                    pause 1.0
                    Y wince "....." with hpunch
                    scene bg library:
                        xalign 1.0
                        linear 3.0 xalign 0.0
                    pause 4.0
                    I "It's definitely her... The daughter...from the lounge photos..."
                    I "Why is her body here? Why wasn't it buried properly...?"
                    play ctc_sfx "<silence 1.0>"
                    play sound sfx_flashback
                    scene bg lounge at grayscale_on
                    show oriana leering2 at mycenter, grayscale_on
                    with custom_flashbulblong()
                    $ grayscale_sideimage = True
                    Y thinking "The mother mentions the addressee--most likely the father--was beating his son."
                    $ fadein_sideimage = False
                    Y "And the result of that is the son urging for the mother to leave the house..."
                    Y leering "But there's [t_clue]no mention of the daughter[t_cluee] at all."
                    Y sad "Nothing that suggests the mother took the daughter with her, or that the son rescued his sister himself..."
                    $ fadein_sideimage = True
                    O irritated "....." with shakeonce
                    O thinking "...Yes."
                    O "Through some unknown means, the daughter must have died first. That has to be the tragedy that tore their family apart."
                    scene bg black with dissolvemed
                    $ grayscale_sideimage = False
                    scene bg library left
                    with dissolvemed
                    I "{cps=6}.....{/cps}"
                    $ show_side_cecilia = True
                    C pout "[name_player], we don't have time to investigate! Let's get back to looking for the zombie!" with shakeonce
                    $ fadein_sideimage = False
                    Y sad "...Right..." with hpunch
                    $ fadein_sideimage = True
                    I "Back to the foyer..."
                    $ show_side_cecilia = False
                    scene bg black with dissolveslow
                    pause 5.0
                "\"No, there's no need.\"":
                    Y blink "No, I believe you. Let's not waste any more time."
                    C blink "Right. Let's pick up the pace."
                    C smile "Back to the foyer, we go~"
                    scene bg black with dissolveslow
                    pause 3.0

            play ctc_sfx sfx_steps fadein 1.0
            scene bg foyer with dissolveslow
            $ day3_checked_lounge = True

        "[u_check]Investigate the [t_clue]Lounge[t_cluee]" if day3_checked_lounge:
            I "There was no sign of the zombie in the lounge, basement, or library."
            I "I guess that means he went through the same route we took to get upstairs, and then never went back...?"

    if day3_checked_kitchen and day3_checked_bathroom and day3_checked_lounge:
        pass
    else:
        jump d3a2_start_investigation

label d3a3:
    scene bg foyer
    I "{cps=6}.....{/cps} ...Wait."
    play ctc_sfx sfx_heartbeat_single
    I "We...already checked everywhere...?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y depressed "{cps=12}That's...impossible...{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ _last_say_who = "C"
    scene bg foyer
    show cecilia thinking at mycenter
    with dissolve
    C "....."
    C sad "......."
    C "[name_player]--{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    show cecilia surprised with custom_flashquick()
    play sound sfx_deskslam
    Y scream "WHY CAN'T WE FIND HIM?!" with shakelong
    C "....."
    Y shocked "I don't get it... This doesn't make any sense..." with shakeonce
    $ fadein_sideimage = False
    Y pained2 "Where could he have gone...?!" with shakeonce
    $ fadein_sideimage = True
    C sad "[name_player]. You need to take a deep breath."
    C thinking "The only possible explanation is that at some point, he managed to slip past us."
    Y troubled "....." with shakeonce
    C determined "We should check the second floor again. Maybe he went up these stairs while we were gone."
    Y shadow "I'm...so tired of this..." with hpunch
    $ show_side_oriana = True
    $ fadein_sideimage = False
    O hidden "[name_player]."
    play ctc_sfx sfx_steps_heels
    window auto hide
    pause 0.5
    $ fadein_sideimage = True
    $ show_side_oriana = False
    show cecilia_raw surprised as cecilia at mycenter_to_myright, backedaway_on
    pause 0.3
    show oriana at myleft
    with dissolvemed
    O "....."
    Y depressed "...Ria...?"
    O thinking "....."
    I "Nrgh... Come on, snap out of it..." with hpunch
    Y sad "A-are you feeling better now?"
    O "......."
    play ctc_sfx "<silence 1.0>"
    O irritated "...Not exactly. There's something you need to see."
    Y surprised "Huh? What is it?"
    O leering2 "Just come upstairs. Quickly."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    play sound sfx_steps_heels
    hide oriana with dissolvemed
    pause 3.0
    show cecilia surprised at myright, backedaway_off
    $ _last_say_who = "C"
    show cecilia thinking at mycenter with move
    C "...Well, that was cryptic."
    Y wince "...I guess we should head up now?" with hpunch
    C blink "Yep, we've already checked out the bottom floors. Might as well head back up where it's safer."
    I "...\"Safer\", huh...?"
    scene bg black with dissolveslow
    pause 1.0
    play ctc_sfx sfx_steps_heels fadein 1.0
    play sound sfx_steps fadein 1.0
    pause 0.5
    scene bg hallway
    with dissolvemed
    pause 2.0
    scene bg hallway:
        xalign 0.3 yalign 0.5 zoom 1.5
    with dissolve
    pause 1.0
    Y surprised "Uh... Ria?"
    $ fadein_sideimage = False
    Y "Isn't that the [t_clue]little girl's bedroom[t_cluee]?{w=0.5} The one [t_clue]Cece was using[t_cluee]?"
    $ show_side_oriana = True
    O irritated "Yes. Here, this is what I wanted you to look at."
    Y thinking "....."
    $ fadein_sideimage = True
    $ show_side_oriana = False
    scene bg black with dissolveslow
    play sound sfx_dooropenslow_unlatch
    I "And as the door slowly opened... Little did I know that yet another [t_clue]sick surprise[t_cluee] awaited me." with shakeonce
    play ctc_sfx "<silence 1.0>"
    play sound sfx_dooropenslow_move
    I "{cps=24}One that would trigger a spiral of [t_clue]chaos[t_cluee] to bury us deeper still into this twisted box of horrors...{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y depressed "{cps=6}.....{/cps} ...That's..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    Y afraid2 "Th-that can't be...?!" with shakeshort
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 1.0
    call save_file_name_update (3, "d3a3")
    scene bg bedroom corpse:
        parallel:
            xalign 0.7 yalign 0.8 zoom 1.8
            easein 20.0 zoom 1.0
        parallel:
            matrixcolor BrightnessMatrix(-1.0)
            linear 10.0 matrixcolor BrightnessMatrix(0.0)
    with dissolveslow
    $ persistent.unlock_bg_bedroom_corpse = True
    pause 9.0
    Y depressed "{cps=18}The... The zombie...{/cps}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    Y "The one who...could be the mastermind of the killing game..."
    play ctc_sfx "<silence 1.0>"
    Y pained2 "{cps=18}He's been...{/cps}{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    show bg bedroom corpse:
        xalign 0.7 yalign 0.8 zoom 1.5
        matrixcolor BrightnessMatrix(0.0)
    with custom_flashquick()
    play music bgm_criminal
    $ show_music_info_timer = music_info_pop_out_time()
    extend afraid2 "[t_clue]KILLED[t_cluee]?!" with shakeshort
    $ show_side_cecilia = True
    $ show_side_oriana = True
    C surprised "....."
    $ fadein_sideimage = True
    I "HOW?!{w=1.0}{nw}" with shakeshort
    play ctc_sfx "<silence 1.0>"
    extend " WHYY?!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    I "WHO could have...?!{w=1.0}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    extend " But WE were supposed to...?!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    with custom_flashquick()
    Y scream "AAAAAAAAGGGGGGGGGGGGGHHHHHHHHHHH!!!" with shakelong
    $ fadein_sideimage = False
    O injured "...I...I wish it didn't have to end like this... With both [name_dog] and a human being dead..." with shakeonce
    O "But I suppose...{w=0.5}this must be how the killing game finally comes to a [t_clue]definitive end[t_cluee]."
    Y troubled "I... Th-this is..." with shakeonce
    $ fadein_sideimage = True
    I "I don't feel anything in my head... Guess my time travel power doesn't react to just {i}any{/i} dead body but..." with shakeonce
    I "THIS is how it ends...?! Somebody dead...and without any explanation...?!" with shakeshort
    I "But who IS this guy?! And [t_clue]who killed him[t_cluee]?!" with shakeshort
    C sad "[name_player]... You don't have to look so pained..."
    $ fadein_sideimage = False
    C thinking "I mean...we were already trying to hunt him down and kill him anyway, right?"
    Y pained "But this just doesn't make ANY amount of sense!" with shakeonce
    Y "Cece, you said that he wasn't in any of the rooms on the second floor!" with shakeonce
    C surprised "Th-that's..." with shakeonce
    O leering2 "Did you {i}seriously{/i} not notice something like this in your OWN room, Cecilia?"
    O irritated "{cps=9}Unless...{/cps}{w=0.5}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend leering "[t_clue]you lied to us[t_cluee]." with shakeonce
    play ctc_sfx sfx_emoteshout
    C pout "Wait wait wait, what's going on with you two?!" with shakeshort
    C "WHY would I lie about not knowing there was a goshdang CORPSE in my room?!" with shakeonce
    C "And then why would I tag along with [name_player] on a wild goose chase SEARCHING for said dead body?!" with shakeshort
    O injured "Nrgh..." with hpunch
    show bg bedroom corpse:
        xalign 0.7 yalign 0.8 zoom 1.5 blur 0
        linear 10.0 blur 20
    Y depressed "This...is [t_clue]insanity[t_cluee]..." with shakeonce
    Y "What am I supposed to do anymore..."
    O shouting "[name_player]! Snap out of it!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y shadow "....."
    O irritated "Even if this isn't the best way things could've turned out... The killing game is finally over."
    O leering "[t_clue]One of us died[t_cluee], exactly as that cursed message on the front door demanded."
    O "And you're not rewinding time anymore, right?"
    play ctc_sfx "<silence 1.0>"
    show bg bedroom corpse:
        xalign 0.7 yalign 0.8 zoom 1.5 blur 0
    Y shocked "...!!" with shakeonce
    O blink "This...{w=1.5} This must finally be the [t_clue]good ending[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    I "{cps=9}...The...{/cps}good ending...?"
    C thinking "....."
    $ fadein_sideimage = False
    O thinking "[name_player]. I...can't get near a corpse, so you should examine his [t_clue]pockets[t_cluee]."
    O "He'll likely have a [t_clue]key[t_cluee] or something that will let us finally leave."
    Y shadow2 "R-right... Leave it...to me..." with hpunch
    $ fadein_sideimage = True
    scene bg bedroom corpse:
        xalign 0.7 yalign 0.8 zoom 1.5
        easein 3.0 zoom 1.8
    pause 3.0
    I "Ria's right... The game is finally over..."
    I "I...just need to examine his [t_clue]pockets[t_cluee]..."
    $ show_side_cecilia = False
    $ show_side_oriana = False

    $ d3a3_corpse_clue1 = False
    $ d3a3_corpse_clue2 = False
    $ d3a3_corpse_clue3 = False
    $ d3a3_corpse_clue4 = False
    $ d3a3_corpse_clue5 = False
    $ d3a3_corpse_clue6 = False
    $ d3a3_corpse_clue7 = False
    $ d3a3_corpse_clue8 = False
    $ d3a3_corpse_clue9 = False

    $ investigation_location = "d3a3_corpse"


    $ investigation_clues_required = 9
    $ investigation_clues_required_found = 0
    $ investigation_clues_optional = 0
    $ investigation_clues_optional_found = 0
    jump d3a3_corpse_investigation

label d3a3_corpse_investigation:
    $ renpy.choice_for_skipping()
    if investigation_clues_required_found == investigation_clues_required:
        achieve 100_CORPSE
    scene bg bedroom corpse pac
    with dissolvequick
    call screen pac_d3a3_corpse with dissolvequick
    if investigation_location != None:
        jump d3a3_corpse_investigation
    else:
        jump d3a3_corpse_end

label d3a3_corpse_end:
    scene bg black
    scene bg bedroom corpse with dissolvemed
    I "...It's...not here..." with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    Y depressed "...Then...that means..."
    play ctc_sfx "<silence 1.0>"
    $ _last_say_who = 'O'
    show oriana leering2 at mycenter with dissolve
    O "...[name_player]. Why did you stop investigating?"
    Y shadow "....."
    O confused "....."
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}.......{/cps}{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    stop music fadeout 3.0
    extend surprised " ...Wait."
    O "You... Y-you couldn't find anything else on his person?" with hpunch
    Y troubled "....." with shakeonce
    O afraid "Nothing...{w=1.0} Nothing like a key? O-or a memo that explains how we could get out?" with hpunch
    Y pained2 "...No. There...wasn't anything like that..." with hpunch
    play ctc_sfx "<silence 1.0>"
    O depressed "{cps=6}.....{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O "The door..."
    play ctc_sfx "<silence 1.0>"
    O horrified "I-is the front door open? I mean, someone DIED now! According to the message, the door should..." with shakeonce
    Y shadow "....."
    $ fadein_sideimage = False
    $ show_side_cecilia = True
    C shadow "....."
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    O shouting "C-come on, let's hurry down!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolveslow
    pause 1.0
    call save_file_name_update (3, "d3a3_trial")
    play sound sfx_runninglong_heels fadein 1.0
    scene bg foyer with dissolveslow
    pause 2.0
    scene bg frontdoor:
        xalign 0.5 yalign 0.3 zoom 1.4
        easein 15.0 zoom 1.0
    with dissolveslow
    pause 3.0
    $ show_side_cecilia = True
    $ show_side_oriana = True
    O afraid "{cps=6}..........{/cps} ...No..."
    stop sound
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    O horrified "It's... It's still..." with shakeshort
    I "{cps=6}There's...{/cps}{color=#ff0000}no escape{/color}..." with hpunch
    $ fadein_sideimage = True
    C blink "Guys. Let's face reality now."
    $ _last_say_who = None
    $ show_side_oriana = False
    $ show_side_cecilia = False
    scene bg black with dissolvemed
    scene bg foyer
    show oriana horrified at myleft_fadein
    show cecilia blink at myright_fadein
    with dissolvemed
    O "{cps=9}...Re...ality...?{/cps}"
    C "Through one way or another, we successfully defeated the evil mastermind of this heinous killing game."
    C thinking "And yet...the door STILL refuses to open. Now, why do you suppose that is?"
    play ctc_sfx "<silence 1.0>"
    O depressed "....." with shakeonce
    C sad "Hmm. I guess Ria's still in shock."
    C smile "Okay, what do {i}you{/i} think, [name_player]?{w=1.0} Why is the door still closed despite the man upstairs being dead?{nw}"

    menu:
        extend ""
        "We're still missing something":
            Y afraid2 "Th-there has to be something else we need to do! Maybe if we examine the body again--" with shakeshort
            C sad "[name_player]. I said let's face reality. You were the one who checked that body thoroughly."
            play ctc_sfx sfx_heartbeat_single
            Y pained "Ngh..." with shakeshort
        "That person's death did not qualify":
            Y troubled "For some reason... The mastermind's death didn't trigger the door to open..." with hpunch
            $ fadein_sideimage = False
            Y "Maybe...he really {i}was{/i} an undead zombie...? Or the door requires someone younger to die?"
            $ fadein_sideimage = True
            C thinking "...Who knows? Either way, this can mean only one thing."
        "Only the culprit knows how to open it":
            Y shocked "Because...only the culprit knows how to open it."
            $ fadein_sideimage = False
            Y "He'd always watch us until one of us died, and then opened the door afterwards. But now..."
            $ fadein_sideimage = True
            C sad "Hmm... Does that really make sense considering your memories, [name_player]?"
            C thinking "You said you would always hear the front door opening [t_clue]immediately after[t_cluee] someone would die in front of you."
            Y troubled "Th-that could just be because... H-he knew, somehow! Maybe by using some occult magic!" with shakeonce
            C sad "C'mon, [name_player], it's really much more simple than that."
    C blink "We checked every room. The mastermind's pockets were empty. From this, we can draw only one conclusion."
    C grin "This house has a will of its own.{w=1.0} It [t_clue]operates on its own rules[t_cluee].{nw}"
    play ctc_sfx "<silence 1.0>"
    play music bgm_decision_chaos
    $ show_music_info_timer = music_info_pop_out_time()
    show bg foyer dark
    $ persistent.unlock_bg_foyer_dark = True
    extend "" with shakeshort
    Y shocked "The... The house itself?" with shakeonce
    O irritated "{cps=6}.....{/cps} ...What...?" with hpunch
    O shouting "Do you hear what you're saying?! And you're telling {i}us{/i} to face reality?!" with shakeshort
    C thinking "I mean, isn't it the only explanation that fits?"
    C default "[name_player], think back to all the other times the front door opened. What's the one thing they all had in common?"
    play ctc_sfx "<silence 1.0>"
    I "Every time the front door opened..."
    play ctc_sfx "<silence 1.0>"
    $ renpy.music.set_volume(0.5, 1, channel="music")
    scene cg chaos at grayscale_on
    show pov_knife at grayscale_on:
        xalign 0.5 yalign 1.0 zoom 0.8 alpha 1.0
    with custom_flash()
    pause 0.5
    scene bg emptybedroom dark chaos2 at grayscale_on
    show cecilia_raw happy knife bloody at mycenter, grayscale_on
    with dissolve
    pause 0.5
    scene cg order at grayscale_on with dissolve
    pause 0.4
    scene bg bedroom dark at grayscale_on
    show oriana_raw deranged at mycenter, grayscale_on
    with dissolve
    pause 0.4
    scene bg black
    show bloodsplatter_5 at truecenter, grayscale_on:
        alpha 0.5
    show oriana_raw stabbed at mycenter, grayscale_on
    show cecilia_raw shadow knife bloody at myleft, grayscale_on
    show stab censor
    with dissolve
    pause 0.3
    scene cg karma4 at grayscale_on with dissolve
    pause 0.3
    scene cg judgement at grayscale_on with dissolve
    pause 0.2
    scene cg despair at grayscale_on with dissolve
    pause 0.2
    scene bg frontdoor open at grayscale_on with dissolve
    pause 0.1
    $ renpy.music.set_volume(1.0, 3, channel="music")
    play sound sfx_frontdoor
    scene bg black with shakeshort
    scene bg foyer dark
    show oriana afraid at myleft_fadein
    show cecilia blink at myright_fadein
    with custom_flashbulblongred()
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    O "...[name_player]...?" with hpunch
    C smile "You know better than any of us what the only means of escape is, [name_player]."
    C sad "I know it's not exactly the most ideal means, but it's the only way to [t_clue]truly end all of this[t_cluee]."
    C determined "We have no more options to explore, and we're starting to run out of time."
    C thinking "And if a house can suddenly burn people alive on a whim, I hate to imagine what it could do if we wait out the time limit."
    C blink "We need to decide this. Now."
    O depressed "I... {size=-10}...can't... Not like...{/size}" with hpunch
    Y troubled "....." with shakeonce
    C "{cps=6}.....{/cps}{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend smile " ...Now, as horrible as this is, let's try to reach a group consensus on who should be the one to [t_clue]die[t_cluee]." with hpunch
    Y shocked "A...consensus?"
    C blink "Yes, as in all three of us must collectively agree on who should die, and [t_clue]accept that outcome[t_cluee]."
    C smug "...That's fine with you, right?"
    O horrified "...!{w=1.0} I..." with shakeonce
    C blink "[name_player], I have a proposition for you."
    play ctc_sfx sfx_emotequestion
    C thinking "Don't you agree that someone who has [t_clue]committed a crime[t_cluee]...is less deserving of salvation?"
    Y afraid "A crime...? What do you--" with shakeonce
    play ctc_sfx sfx_heartbeat_single
    show bg black
    hide oriana
    show cecilia determined at mycenter
    $ renpy.music.set_volume(0.0, 0, channel="music")
    $ renpy.music.set_volume(1.0, 3, channel="music")
    C "[t_clue]Who killed the mastermind[t_cluee], [name_player]?" with shakeshort
    Y depressed "...!! Wh-who...?" with shakeonce
    $ renpy.music.set_volume(0.25, 3, channel="music")
    scene bg bedroom corpse pac at grayscale_on:
        xalign 0.7 yalign 0.8 zoom 1.2
        easein 5.0 zoom 1.0
    with custom_flashbulblong()
    pause 3.0
    I "The mastermind... Th-the man upstairs..."
    I "....."
    I "...Wait. She's right..."
    play ctc_sfx "<silence 1.0>"
    I "Considering the circumstances, all the [t_clue]clues[t_cluee] I found...{w=1.0} Who could have possibly killed the mastermind?{nw}" with shakeonce


    menu:
        extend ""
        "Oriana":
            window auto hide
            pause 1.0
            scene bg black with dissolvemed
            $ renpy.music.set_volume(1.0, 3, channel="music")
            pause 1.0
            scene bg foyer dark
            show oriana shadow at myleft_fadein
            show cecilia blink at myright_fadein
            with dissolvemed
            pause 1.0
            Y depressed "...It...could have only been Ria..."
            O depressed "...!!" with shakeonce
            O afraid "[name_player]...?"
            C smile "...I think you may be right."
        "Cecilia":
            window auto hide
            pause 1.0
            scene bg black with dissolvemed
            $ renpy.music.set_volume(1.0, 3, channel="music")
            pause 1.0
            scene bg foyer dark
            show oriana shadow at myleft_fadein
            show cecilia blink at myright_fadein
            with dissolvemed
            pause 1.0
            Y shadow "...Cece. It could only have been you."
            $ fadein_sideimage = False
            Y angry "We all know you're the only one who stands a chance at fighting him." with shakeonce
            $ fadein_sideimage = True
            play ctc_sfx sfx_emotequestion
            C thinking "That's a fair point, [name_player], but keep in mind that I have an [t_clue]alibi[t_cluee]."
            C "In fact, {i}you're{/i} the one who can confirm it. I was with you the whole time, remember?"
            play ctc_sfx "<silence 1.0>"
            Y depressed "...!!{cps=1} {/cps}Then that means..." with shakeonce
            C smile "Yep. The same can't be said for Ria..."
            O afraid "Wh-what?!" with shakeshort
        "Me":
            window auto hide
            pause 1.0
            scene bg black with dissolvemed
            $ renpy.music.set_volume(1.0, 3, channel="music")
            pause 1.0
            scene bg foyer dark
            show oriana shadow at myleft_fadein
            show cecilia blink at myright_fadein
            with dissolvemed
            pause 1.0
            Y troubled "...{i}I{/i} could have done it...right?"
            play ctc_sfx sfx_emotequestion
            C surprised "Huh? DID you do it?"
            Y wince "N-no, but..." with hpunch
            C sad "Is this really the time for jokes, [name_player]? Besides, you have me to confirm your [t_clue]alibi[t_cluee] during his murder."
            C smile "However, the same can't be said for Ria..."
            O afraid "Wh-what?!" with shakeshort
        "The mastermind himself":
            window auto hide
            pause 1.0
            scene bg black with dissolvemed
            $ renpy.music.set_volume(1.0, 3, channel="music")
            pause 1.0
            scene bg foyer dark
            show oriana shadow at myleft_fadein
            show cecilia blink at myright_fadein
            with dissolvemed
            pause 1.0
            Y afraid "...It could have been a suicide. Maybe he felt really guilty about all of this and--" with hpunch
            C sad "[name_player]. You saw the state his body was in. Did that really look like anything but a homicide?"
            Y pained "Nrgh..." with hpunch
            play ctc_sfx "<silence 1.0>"
            $ renpy.music.set_volume(0.5, 0, channel="music")
            $ renpy.music.set_volume(1.0, 1, channel="music")
            C serious "There's no point trying to avoid it.{w=1.0} You know that [t_clue]it could have only been Ria[t_cluee]."
            play ctc_sfx "<silence 1.0>"
            I "{cps=6}.....{/cps}"
    O horrified "W-wait! What in the world are you talking about?!" with shakeshort
    C thinking "We know that the mastermind killed [name_dog] and left his body in the hallway. Which means he was still alive at that point."
    C default "After which, [name_player] and I went looking for the zombie in the lower floors."
    C blink "But Ria...was alone on the second floor. And the body was found in the little girl's bedroom, right?"
    O shouting "Do you HONESTLY believe I went looking for the man and killed him [t_clue]all by myself[t_cluee]?!" with shakeonce
    O "Need I remind you of the state of my arm?!" with shakeshort
    C smug "But is that the arm of your dominant hand?"
    O leering "N-no, but it's still insane to believe I could have taken his knife away and killed him with only one arm!" with hpunch
    C thinking "Hmm... But what if he was asleep?"
    O afraid "Wh-what...?"
    C smug "His body was by the bed, right? Plus there was no sign of any struggling in the room..."
    C grin "Maybe he was taking a nap when you found him in there and{cps=6}... ...{/cps}You know?"
    O horrified "You're...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " What is WRONG with you?!" with shakeshort
    C blink "I think you panicked. I think you saw an opportunity present itself, and took it."
    C sad "You scowled at the man. You wanted the killing game to end soooo badly...{w=1.0} You let your instincts take over."
    C "The [t_clue]bloodlust[t_cluee] within you... The depravity that [name_player] has witnessed before...{w=1.0} You can't deny any of it. So..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    O depressed "{cps=6}.....{/cps}"
    show bg black
    play ctc_sfx sfx_heartbeat_single
    stop music fadeout 3.0
    C serious "If you're nothing but a [t_clue]filthy murderer[t_cluee], then no one should have any complaints about you being our {color=#ff0000}sacrifice{/color}, right?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O "You're... You're serious..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    O troubled "You actually...want [name_player] to choose {i}me{/i} to be {color=#ff0000}the one to die{/color}..." with shakeonce
    C sad "It would be easier for all of us if you just admit to your crime, Ria."
    C creepygrin "Then we can all accept this outcome as [t_clue]the end of the killing game[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "...Why...? How did we get here...?" with hpunch
    play ctc_sfx "<silence 1.0>"
    I "This is...the [t_clue]good ending[t_cluee] we've been fighting all this time for...?" with shakeonce
    O irritated "{cps=6}.....{/cps} ...All right. ...If that's the way you're playing this..."
    O leering "[name_player]. If you believe that whoever murdered the mastermind should be the one to die, then..."
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}.....{/cps}{w=1.0} ...It's Cecilia.{nw}"
    play ctc_sfx "<silence 1.0>"
    show bg foyer at wobble, blurring, grayscale_on
    show trial gradient behind oriana at truecenter
    show oriana leering at myleft_trial
    show cecilia creepygrin at myright_trial
    play music bgm_decision_order
    $ show_music_info_timer = music_info_pop_out_time()
    extend "{w=1.0} She's the one who did it." with shakeshort
    Y shocked "...You too...?" with hpunch
    C blink "....."
    show trial gradient:
        easein 0.3 xalign 0.2
    O annoyed2 "You saw me wake up in the master bedroom, and stayed with me until Cecilia supposedly \"found\" [name_dog]'s body."
    O leering2 "But how do we know that she wasn't the one who put him in the hallway in the first place?"
    play ctc_sfx sfx_heartbeat_single
    Y depressed "That's..." with shakeonce
    show trial gradient:
        easein 0.3 xalign 0.8
    C surprised "You're accusing me of killing the dog too? Wow, you're certainly brazen today."
    show trial gradient:
        easein 0.3 xalign 0.2
    O irritated "I thought it was strange, you see... Why was Cecilia so sure that [name_dog]'s body was a \"warning\"?"
    O "Why did she suggest that you two check the lower floors instead of the second floor, where [name_dog]'s body was found?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y afraid "...You mean...?!" with shakeonce
    O annoyed "She'd [t_clue]already killed the mastermind[t_cluee] in the bedroom while she was wandering around alone." with shakeonce
    O irritated2 "And when she realized the door didn't open in spite of that, she devised this plan."
    O "She wanted to [t_clue]frame me[t_cluee]. Make it look like {i}I{/i} was the one who killed the mastermind while you two were downstairs."
    O leering "And then if she could convince you to turn against me, that would guarantee her own safe escape." with shakeonce
    show trial gradient:
        easein 0.3 xalign 0.8
    C surprised "Oooh..."
    play ctc_sfx sfx_emotehappy
    show cecilia happy at hop
    C "That's some impressive deductive reasoning!{w=0.5} On the spot, too!"
    play ctc_sfx "<silence 1.0>"
    C serious "{cps=24}...Too bad you don't have any proof.{/cps}"
    play ctc_sfx "<silence 1.0>"
    show trial gradient:
        easein 0.3 xalign 0.2
    O annoyed "And what proof do YOU have that I was able to kill that man with one arm?!" with shakeonce
    show trial gradient:
        easein 0.3 xalign 0.8
    C sad "Again, the state of the room, our respective alibis..."
    C grin "Oh, and here's another one! Why would I kill him with his own knife? I'm already carrying my own!" with vpunch
    show trial gradient:
        easein 0.3 xalign 0.2
    O afraid "Th-that's... Y-you could have switched the knives after killing him!" with shakeonce
    $ renpy.music.set_pan(0.65, 0.0, channel='sound')
    play sound sfx_knifebrandish
    with custom_flashquick()
    show trial gradient:
        easein 0.3 xalign 0.8
    C blink knife "Hmm... [name_player], do you see any blood on my knife here?" with hpunch
    show trial gradient:
        easein 0.3 xalign 0.2
    O shouting "You could have wiped it off!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    play sound sfx_knifeequip
    $ renpy.music.set_pan(0.0, 5.0, channel='sound')
    show trial gradient:
        easein 0.3 xalign 0.8
    C thinking "Also, if I really wanted to frame you, I wouldn't have just left the knife stuck in his body like that."
    C smug "I would've hidden it somewhere in the bedroom, and then later \"accidentally\" find it in the place YOU hid it in."
    show trial gradient:
        easein 0.3 xalign 0.2
    O injured "Your reasoning is still flawed! If it were really me, why would I just leave the knife stuck in the body?!" with shakeshort
    show trial gradient:
        easein 0.3 xalign 0.8
    C sad "How should I know? Maybe you panicked from committing such a heinous crime? Maybe you wanted to pass it off as a suicide?"
    show trial gradient:
        easein 0.3 xalign 0.2
    O troubled "Y-you..." with shakeshort
    play ctc_sfx sfx_emotesigh
    show cecilia sweatdrop at shrink
    show trial gradient:
        easein 0.3 xalign 0.8
    C "Look, we're not getting anywhere with this.{w=1.0} [name_player], as always, it's up to you."
    play ctc_sfx sfx_heartbeat_single
    Y shocked "Wh-what...?" with shakeonce
    show cecilia thinking at myright_trial
    C thinking "You've heard each of our arguments, and you're the only one who's had a consistent alibi this entire time."
    C smile "It doesn't look like a consensus will be possible, so you'll have to be our tiebreaker."
    Y depressed "{cps=12}The tie...{/cps}{cps=1} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend afraid2 "Wh-what the hell are you talking about?!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    Y "You're asking me to [t_clue]choose one of you to DIE[t_cluee]!" with shakeshort
    $ fadein_sideimage = True
    C grin "And I don't think either of us will object to your decision. Right, Ria...?"
    play ctc_sfx sfx_heartbeat_single
    show bg foyer at reset:
        matrixcolor BrightnessMatrix(0.0) * SaturationMatrix(0.0)
        linear 10.0 matrixcolor BrightnessMatrix(-1.0) * SaturationMatrix(0.0)
    O afraid "...!{w=1.0} {cps=6}...I...{/cps}" with shakeonce
    show trial gradient:
        easein 0.3 xalign 1.0
    O depressed "......."
    show trial gradient:
        alpha 1.0
        linear 5.0 alpha 0.0
    O dejected "...Yes. The choice...is yours, [name_player]."
    O "As long as the killing game FINALLY comes to an end... I'll accept [t_clue]whatever decision you make[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    Y depressed "{cps=6}.....{/cps} ...Ria...?"
    C creepy "....."
    C blink knife "[name_player]. I'll lend you my knife."
    window auto hide
    play ctc_sfx ["<silence 0.2>", sfx_knifeequip]
    show cecilia blink knife at shrink
    pause 0.4
    $ _last_say_who = None
    show cecilia blink at myright_trial with move
    pause 0.5
    show pov_knife:
        xalign 0.5 yalign 1.0
        zoom 0.8
    with dissolvemed
    pause 1.0
    Y troubled "{cps=9}...Is this...{/cps}{cps=1} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend pained2 "Does it HAVE to be like this...?" with shakeshort
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    O shadow "....."
    C blink "The most important thing is that you accept your choice, [name_player]."
    play ctc_sfx "<silence 1.0>"
    C creepy "There will be {color=#ff0000}no turning back{/color} once you make your decision."
    play ctc_sfx "<silence 1.0>"
    C creepygrin "Make this one last choice...and you'll never again be forced to experience a killing game."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    stop music fadeout 5.0
    pause 1.0
    scene bg black with dissolveslow


    pause 1.0
    I "...I didn't have a dream when I last woke up. I won't be rewinding time anymore."
    I "I guess...the killing games finally end because I make this [t_clue]one final choice[t_cluee]."
    I "And...it'll be a choice that I can accept. A choice that I won't want to take back."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    if not seen_ria_hearttoheart:
        I "It's no use... There's no option but to kill someone..."
        play ctc_sfx "<silence 1.0>"
        I "If only... If only [t_clue]I talked with Cece and Ria more[t_cluee]..." with shakeonce
        play ctc_sfx "<silence 1.0>"
        I "The truth...{w=1.0} It's {color=#ff0000}lost{/color} forever now..."
        play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 1.0
    I "It's time, [name_player_true].{w=1.0} Once you advance, there's no {color=#cccc00}turning back time{/color}. And no more [t_clue]pausing[t_cluee] to think."
    extend " {cps=6}.....{/cps} Am I ready...?{w=0.5}{nw}"
    $ mute_choice = True

    menu:
        extend ""
        "Proceed":
            window auto hide
    $ mute_choice = False
    $ renpy.block_rollback()
    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys
    pause 1.0
    play sound sfx_introambiance_sequence1
    pause 2.0
    "{cps=16}...This is it.{/cps}{w=2.0}{nw}"
    scene bg black with dissolvemed
    "{cps=16}...After all that's happened...{/cps}{w=2.0}{nw}"
    "{cps=16}It comes down to this after all...{/cps}{w=2.0}{nw}" with shakeonce
    play sound2 sfx_introambiance_sequence2 fadein 0.5
    scene bg black
    show oriana shadow at myleft
    show cecilia shadow at myright
    with dissolveslow
    stop sound fadeout 0.5
    "{cps=16}All I have to do...{/cps}{w=3.0}{nw}"
    "{cps=16}...is make one {color=#ff0000}final choice{/color}.{/cps}{w=3.0}{nw}"
    $ finalchoice_doubt = False
    $ finalchoice_chose_cece = False
    $ finalchoice_chose_ria = False
label d3a3_finalchoice:
    $ renpy.block_rollback()
    play ctc_sfx sfx_introambiance_pentagramknife
    if finalchoice_doubt:
        play sound sfx_introambiance_sequence3
    else:
        play loop_sfx sfx_introambiance_sequence4_loop
    scene bg black with custom_flashquick()
    stop sound2 fadeout 0.5

    $ countdown_time_max = 28
    $ countdown_time = 28
    $ renpy.set_mouse_pos(960, 540)
    call screen character_select_true with shakeshort

    if _return is "red":
        $ renpy.block_rollback()
        $ finalchoice_chose_ria = True
        if finalchoice_doubt:
            play loop_sfx sfx_introambiance_sequence4_loop fadein 0.5
        show oriana_raw horrified at myleft
        show oriana_raw horrified at mycenter with move
        if finalchoice_doubt:
            stop sound fadeout 0.5
        ".....{w=2.0}{nw}"
        $ show_choicegrand = True
        $ mute_choice = True
        menu:
            "KILL":
                pass
        play sound sfx_introkill_1
        show pov_knife:
            xalign 0.5 yalign 1.0
            zoom 0.8
        with dissolve
        ".....{w=2.0}{nw}"
        if seen_ria_hearttoheart:
            $ finalchoice_doubt = True
            I "{cps=6}.....{/cps} ...Ria..."
            play ctc_sfx "<silence 1.0>"
            scene cg ria hearttoheart at grayscale_on
            with custom_flashbulblong()
            pause 1.0
            scene cg ria hearttoheart2 at grayscale_on:
                xalign 0.5 yalign 0.0 zoom 1.1
                easein 10.0 zoom 1.3
            with dissolve
            I "{cps=6}.....{/cps} I..."
            play ctc_sfx "<silence 1.0>"
            I "I'm...so sorry..." with hpunch
            play ctc_sfx "<silence 1.0>"
            I "I was...supposed to {color=#ff0000}protect you{/color}... But now, I..."
            play ctc_sfx "<silence 1.0>"
            scene bg black with dissolveslow
            pause 1.0
            scene bg black
            show oriana_raw dejected at mycenter
            with dissolveslow
            pause 1.0
            Y crying "{cps=6}..........{/cps}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            window auto hide
            pause 1.0
            show pov_knife:
                parallel:
                    xalign 0.5 yalign 1.0 zoom 0.8 yoffset 200
                    easeout 1.2 yoffset 90
                    easein 1.2 yoffset 0
                parallel:
                    ease 0.25 xoffset -2
                    ease 0.75 xoffset 3
                    ease 0.25 xoffset -2
                    ease 0.25 xoffset 3
                    ease 0.75 xoffset -3
                    ease 0.25 xoffset 0
            with dissolvemed
            pause 2.0
            menu:
                "KILL":
                    pass
                "DON'T KILL":
                    $ show_choicegrand = False
                    $ mute_choice = False
                    show pov_knife:
                        xalign 0.5 yalign 1.0 zoom 0.8 yoffset 0 alpha 1.0
                        easeout 2.0 yoffset 200 alpha 0.0
                    pause 3.0
                    I "...I can't..."
                    play ctc_sfx "<silence 1.0>"
                    scene bg black
                    with dissolvemed
                    I "But then... [t_clue]What should I do[t_cluee]...?"
                    play ctc_sfx sfx_heartbeat_single
                    show timer background at truecenter:
                        alpha 0.5 zoom 1.0
                        easein 2.0 alpha 0.0 zoom 2.0
                    Y troubled "...!!" with shakeshort
                    play ctc_sfx "<silence 1.0>"
                    jump d3a3_finalchoice
        else:
            menu:
                "KILL":
                    pass

        $ renpy.block_rollback()
        $ show_choicegrand = False
        $ mute_choice = False
        stop loop_sfx fadeout 0.2
        play ctc_sfx ["<silence 0.5>", sfx_knifeslash]
        show oriana_raw horrified at mycenter:
            zoom 1.0 ypos 1.05
            easein 1.0 zoom 3.0 ypos 2.55
        show pov_knife:
            xalign 0.5 yoffset 0 zoom 0.8
            easein 0.5 yoffset 400 zoom 1.0
            linear 0.1 yoffset 200
        with shakeshort
        scene bg black
        show bloodsplatter_2 at truecenter
        show bloodsplatter_1 at truecenter
        with custom_flashbulblongred()
        pause 6.0
        scene bg black with dissolveslow
        pause 9.0
        stop ctc_sfx
        hide screen lock_hotkeys
        $ quick_menu = True
        $ music_info = True
        jump d3a3_cecilia_ending

    if _return is "blue":
        $ renpy.block_rollback()
        $ finalchoice_chose_cece = True
        if finalchoice_doubt:
            play loop_sfx sfx_introambiance_sequence4_loop fadein 0.5
        show cecilia_raw creepygrin at myright
        show cecilia_raw creepygrin at mycenter with move
        if finalchoice_doubt:
            stop sound fadeout 0.5
        ".....{w=2.0}{nw}"
        $ show_choicegrand = True
        $ mute_choice = True
        menu:
            "KILL":
                pass
        play sound sfx_introkill_1
        show pov_knife:
            xalign 0.5 yalign 1.0
            zoom 0.8
        with dissolve
        ".....{w=2.0}{nw}"
        if seen_cece_hearttoheart:
            if seen_ria_hearttoheart:
                $ finalchoice_doubt = True
            I "{cps=6}.....{/cps} ...Cece..."
            play ctc_sfx "<silence 1.0>"
            scene cg cece hearttoheart at grayscale_on
            with custom_flashbulblong()
            pause 1.0
            scene cg cece hearttoheart2 at grayscale_on:
                xalign 0.5 yalign 0.0 zoom 1.1
                easein 10.0 zoom 1.3
            with dissolve
            I "{cps=6}.....{/cps} I..."
            play ctc_sfx "<silence 1.0>"
            I "Can I...really do this...?" with hpunch
            play ctc_sfx "<silence 1.0>"
            I "{color=#ff0000}End her story{/color}... W-with my own hands...?"
            play ctc_sfx "<silence 1.0>"
            scene bg black with dissolveslow
            pause 1.0
            scene bg black
            show cecilia_raw blush at mycenter
            with dissolveslow
            pause 1.0
            Y crying "{cps=6}..........{/cps}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            window auto hide
            pause 1.0
            show pov_knife:
                parallel:
                    xalign 0.5 yalign 1.0 zoom 0.8 yoffset 200
                    easeout 1.2 yoffset 90
                    easein 1.2 yoffset 0
                parallel:
                    ease 0.25 xoffset -2
                    ease 0.75 xoffset 3
                    ease 0.25 xoffset -2
                    ease 0.25 xoffset 3
                    ease 0.75 xoffset -3
                    ease 0.25 xoffset 0
            with dissolvemed
            pause 2.0
            menu:
                "KILL":
                    pass
                "DON'T KILL":
                    $ show_choicegrand = False
                    $ mute_choice = False
                    show pov_knife:
                        xalign 0.5 yalign 1.0 zoom 0.8 yoffset 0 alpha 1.0
                        easeout 2.0 yoffset 200 alpha 0.0
                    pause 3.0
                    I "...I can't..."
                    play ctc_sfx "<silence 1.0>"
                    scene bg black
                    with dissolvemed
                    I "But then... [t_clue]What should I do[t_cluee]...?"
                    if seen_ria_hearttoheart:
                        play ctc_sfx sfx_heartbeat_single
                        show timer background at truecenter:
                            alpha 0.5 zoom 1.0
                            easein 2.0 alpha 0.0 zoom 2.0
                        Y troubled "...!!" with shakeshort
                        play ctc_sfx "<silence 1.0>"
                    jump d3a3_finalchoice
        else:

            menu:
                "KILL":
                    pass
        $ renpy.block_rollback()
        $ show_choicegrand = False
        $ mute_choice = False
        stop loop_sfx fadeout 0.2
        play ctc_sfx ["<silence 0.5>", sfx_knifeslash]
        show cecilia_raw creepygrin at mycenter:
            zoom 1.0 ypos 1.05
            easein 1.0 zoom 3.0 ypos 2.35
        show pov_knife:
            xalign 0.5 yoffset 0 zoom 0.8
            easein 0.5 yoffset 400 zoom 1.0
            linear 0.1 yoffset 200
        with shakeshort
        scene bg black
        show bloodsplatter_1 at truecenter
        show bloodsplatter_2 at truecenter
        with custom_flashbulblongred()
        pause 6.0
        scene bg black with dissolveslow
        pause 9.0
        stop ctc_sfx
        hide screen lock_hotkeys
        $ quick_menu = True
        $ music_info = True
        jump d3a3_oriana_ending

    if _return is "yellow":
        hide screen lock_hotkeys
        $ quick_menu = True
        $ music_info = True
        $ renpy.block_rollback()
        scene bg black
        show oriana afraid at myleft_trial:
            blur 30
        show cecilia surprised at myright_trial:
            blur 30
        show bloodsplatter_5 at truecenter:
            blur 20 alpha 0.5
        with custom_flashquick()
        stop sound
        stop loop_sfx
        play sound2 sfx_knifestab
        window auto show custom_flashquickred()
        Y pained2 "...!!!" with shakelong
        play ctc_sfx "<silence 1.0>"
        C "...!! {cps=6}...Wha...?{/cps}" with shakeshort
        play ctc_sfx "<silence 1.0>"
        O stabbed "{cps=6}.....{/cps}{w=0.5} ...No..."
        play ctc_sfx "<silence 1.0>"
        Y depressed stabbed "....." with shakeshort
        play ctc_sfx "<silence 1.0>"
        scene bg black with dissolvemed
        pause 1.0
        play sound sfx_fallhard
        show bloodsplatter_2 at truecenter:
            alpha 0.5
            linear 2.0 alpha 0.0
        with shakeshort
        play sound2 sfx_knifedrop
        pause 2.0
        scene bg bloodpool 1 with dissolvemed
        pause 1.0
        Y shadow stabbed "{cps=6}..........{/cps}"
        play ctc_sfx "<silence 1.0>"
        $ fadein_sideimage = False
        $ show_side_cecilia = True
        $ show_side_oriana = True
        C hidden "{size=-10}...in... ...[t_clue]heart[t_cluee]...{/size}" with shakeshort
        play ctc_sfx "<silence 1.0>"
        O hidden "{size=-15}...ey... ...no... ...ca...{/size}" with shakeshort
        play ctc_sfx "<silence 1.0>"
        $ fadein_sideimage = True
        scene bg bloodpool 2 with dissolvemed
        C hidden "{size=-20}.....{/size}" with shakelong
        $ fadein_sideimage = False
        play ctc_sfx "<silence 1.0>"
        O hidden "{size=-25}...{/size}" with shakelong
        play ctc_sfx "<silence 1.0>"
        $ fadein_sideimage = True
        scene bg bloodpool 3 with dissolvemed
        I "I...can't see... I can't...hear..."
        play ctc_sfx "<silence 1.0>"
        I "But why am I...still..."
        play ctc_sfx "<silence 1.0>"
        $ show_side_cecilia = False
        $ show_side_oriana = False
        play ctc_sfx sfx_whoosh
        with custom_flashquick()
        scene bg black
        with soulout

        scene bg black with dissolveslow
        pause 9.0
        $ renpy.block_rollback()
        stop ctc_sfx
        jump d3a3_martyr_ending

    if _return is "none":
        stop sound fadeout 0.2
    stop loop_sfx fadeout 0.2
    window auto hide None
    scene bg black with custom_flashquick()
    $ show_choicegrand = False
    $ mute_choice = False
    pause 5.0
    hide screen lock_hotkeys
    $ quick_menu = True
    $ music_info = True
    $ renpy.block_rollback()
    stop ctc_sfx
    jump d3a4

label d3a3_oriana_ending:
    call save_file_name_update (3, "d3a3_oriana_ending")
    scene bg black
    scene bg frontdoor open:
        xalign 0.5 yalign 0.5 zoom 1.5
        easein 20.0 zoom 1.0
    with dissolveslow
    U "{cps=6}.....{/cps}"
    U "So...{w=1.0} This is how it ends..."
    $ _last_say_who = "O"
    scene bg frontdoor open
    show oriana blink at mycenter
    with dissolveslow
    pause 0.5
    play music bgm_origin_order
    pause 1.5
    O "Yes. It's...finally over..."
    U "Ria... Did...I make the right decision...?" with shakeonce
    O thinking "...Do you really want to ask that now...?"
    U "It's just... ...I..." with shakeonce
    O injured "[t_clue]Don't look back[t_cluee]." with shakeonce
    O "If you do... You risk putting us through this {color=#ff0000}Hell{/color}...all over again..."
    play ctc_sfx "<silence 1.0>"
    U "{cps=6}.....{/cps}" with shakeonce
    O crying2 "{cps=6}.....{/cps} *sniff*" with shakeonce
    play ctc_sfx "<silence 1.0>"
    U "R-Ria..." with shakeonce
    O "*hic* {cps=6}.....{/cps} ...I-I..." with shakeonce
    U "I'm sorry... I'm so sorry I put you through all this..."
    U "It must've been...terrifying..." with hpunch
    O crying "*sob* Grk...! ...N-no... It's just..." with shakeonce
    O crying2 "I can...never start over with her..."
    play ctc_sfx sfx_heartbeat_single
    U "...!!!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    U "Ria, y-you..." with shakeonce
    O "*sniff* ..... ...I..." with hpunch
    window auto hide
    show oriana shadow at shudder
    pause 0.5
    O embarrassed "I-I'm sorry. Here I was, saying you shouldn't look back and..." with hpunch
    play ctc_sfx "<silence 1.0>"
    U "No, I get it..."
    U "It makes sense that you would cry like that..."
    O thinking "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    U "You can't stand injustice, but...you also see the good in anyone."
    U "You have [t_clue]infallible kindness[t_cluee], the purest of hearts...{w=1.0} Even for people who don't deserve it..."
    U "And that's exactly why I love you so much, Ria..."
    play ctc_sfx "<silence 1.0>"
    O dejected "{cps=6}.......{/cps}"
    U "Come on...! Don't give me that look!" with shakeonce
    U "I've seen all sides of you, Ria... That's why I can say without a doubt in my mind..."
    U "...You are the strongest person I have ever met.{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " So puff out your enormous chest! Be proud of yourself!" with shakeshort
    O irritated "....." with shakeonce
    U "...Uh... Was that too soon...?" with hpunch
    O blink "...You really are an idiot..."
    play ctc_sfx sfx_emotesigh
    U "Ahaha..." with hpunch
    O relaxed "....."
    O "You're right..."
    O "Even if we can't see Cecilia ever again... We can at least continue doing Occult Club activities in her honour."
    O thinking "And maybe... Maybe that will bridge the gulf between us at last..."
    U "I'm sure she would love to see that. The stoic skeptic Ria, leading the charge in exposing the paranormal..."
    O relaxed "Hmph. You wish."
    O confident "Only you could possibly be the next president."
    U "M-me? I..." with hpunch
    O blink "You should do your part in keeping Cecilia's memory alive too."
    O thinking "Especially considering that you and her..."
    play ctc_sfx "<silence 1.0>"
    U "{cps=6}.....{/cps}" with shakeonce
    O blink "No. That's enough seesawing with our emotions. Let's get going before the door suddenly decides to close on us."
    U "Yeah, that would be quite the nifty little ghost trick, huh?{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " Pft~" with hpunch
    O disappointed "Ugh. It's as though another Cecilia is right in front of me."
    play ctc_sfx sfx_emotehappy
    U "C'mon, let's go, Ria~" with vpunch
    O relaxed "Yes..."
    O happy "Let's go [t_clue]home[t_cluee]."
    scene bg frontdoor open
    with dissolveslow
    stop music fadeout 5.0
    pause 5.0
    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#00ff00}ХОРОШАЯ КОНЦОВКА{/color}{/size}\n{color=#000}Концовка Орианы{/color}{/font}" with dissolve
    pause 2.0
    achieve END_ORIANA
    pause 3.0
    hide text with dissolveslow
    pause 1.0
    scene bg black with dissolveslow
    pause 3.0
    play music bgm_order
    call screen credits(180, True)
    stop music fadeout 5.0
    $ _skipping = True
    pause 5.0
    show text "Это произведение является вымышленным. Любое сходство с реальными событиями и людьми, живыми\nили мёртвыми, является случайным. Мнения, выраженные персонажами этого\nпроизведения, не обязательно совпадают с мнением автора." with dissolvemed
    pause 15.0
    hide text with dissolvemed
    $ quick_menu = True
    $ music_info = True
    hide screen lock_hotkeys
    call ending_message
    call end_menu
    return

label d3a3_cecilia_ending:
    call save_file_name_update (3, "d3a3_cecilia_ending")
    scene bg black
    scene bg frontdoor open:
        xalign 0.5 yalign 0.5 zoom 1.5
        easein 20.0 zoom 1.0
    with dissolveslow
    U "{cps=6}.....{/cps}"
    U "So...{w=1.0} This is how it ends..."
    $ _last_say_who = "C"
    scene bg frontdoor open
    show cecilia blink at mycenter
    with dissolveslow
    pause 0.5
    play music bgm_origin_chaos
    pause 1.5
    C "...Yeah. We did it."
    C smile "We...ended the killing game."
    U "{cps=6}.....{/cps} ...Ria..."
    C sad "I know... This is probably the worst club outing in all of human history..."
    C determined "But she knew this was always a possibility.{w=0.5} {cps=9}And...{/cps}{w=0.5}you did too."
    play ctc_sfx "<silence 1.0>"
    U "That doesn't make it any better...!" with shakeshort
    U "Ria was undeniably a [t_clue]victim[t_cluee] of everything, and everyone... Including..."
    play ctc_sfx "<silence 1.0>"
    U "{cps=6}...Me...{/cps} ...I'm at fault too..." with shakeonce
    C sad "....."
    C "Uh... I don't know if this will be of any comfort to you, but..."
    C thinking "Do you think that Ria died a little easier since...it was [t_clue]by your own hands[t_cluee]?"
    play ctc_sfx "<silence 1.0>"
    U "...Wh-what do you mean...?" with shakeonce
    C "It's just...she seemed to calm down pretty quick when I said the decision was ultimately yours to make."
    C smile "Maybe on some level... Having you kill her was the [t_clue]greatest mercy[t_cluee] for her."
    C blink "Not by some maniac zombie... Or by a pit of fire... Or by some stabby-happy girl enjoying the situation way too much..."
    C blush "But by the hands of someone who had no other choice. Someone she could [t_clue]rescue by giving up her own life[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    U "{cps=6}.....{/cps}"
    play ctc_sfx sfx_emotesigh
    show cecilia sweatdrop at shrink
    C "But who knows if I'm right? After all, I'm sure all sorts of thoughts flash in your head when you're just about to die..."
    U "No... Knowing Ria...{w=1.0} She probably did exactly that." with hpunch
    show cecilia surprised at mycenter
    C "Huh...?"
    U "She considered how {i}I{/i} felt... She knew that...killing her...was the last thing I ever wanted to do..."
    U "And...she barely held herself together...with the belief that [t_clue]{i}her{/i} death would mean {i}my{/i} life[t_cluee]..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    C "....."
    C blink "...Heh. Yeah, that sounds like her."
    C smile "So...you don't regret choosing me?"
    U "{cps=6}.....{/cps}"
    C surprised "...Huh? What's that face supposed to mean?"
    U "I... I just couldn't get myself to kill you, so..." with hpunch
    C "....."
    C grin "Pft..." with hpunch
    play ctc_sfx "<silence 1.0>"
    show cecilia happy at doublehop
    with custom_flashquick()
    play ctc_sfx sfx_emotehappy
    C "AHAHAHAHAAA~ [u_music_note]" with shakeshort
    U "Y-you don't have to laugh so boisterously..." with hpunch
    C wink "Pft, how can I NOT laugh at how awkward you're being right now?" with vpunch
    U "I don't know, maybe out of respect for the..."
    U "....."
    C sad "C'mon, I'm only doing this to lighten the weight on your shoulders, y'know..."
    C smile "Again, Ria died for our sakes. She's a hero! Be proud of her already!" with vpunch
    U "{cps=6}.....{/cps} ...Yeah..."
    U "I don't think she'd want us to just mope around here when she's already given up her life for us..."
    C happy "Exactly! You're finally getting it!"
    C blink "Even though it's not ideal, this is still a [t_clue]good ending[t_cluee] for us."
    C smile "We should honour all the [t_clue]sacrifices[t_cluee] it took to get us in front of this open doorway, safe and sound."
    U "Y-yeah... {cps=6}.....{/cps}{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " {size=-10}...*sniff*...{/size}" with hpunch
    C pout "Hey c'mon, you JUST said we shouldn't mope anymore, what're you crying for...?"
    U "N-no, I'm just..." with hpunch
    U "...It's...the fatigue catching up to me.{w=0.5} I'm just...so relieved..."
    play ctc_sfx "<silence 1.0>"
    U "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    C blink "...Yeah, I guess that makes sense. You went through a lot."
    play ctc_sfx "<silence 1.0>"
    U "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    C blush "But you can rest now.{w=1.0} I'll protect you.{w=1.0} {cps=12}...Forever and ever... [u_heart]{/cps}"
    play ctc_sfx "<silence 1.0>"
    scene bg frontdoor open
    with dissolveslow
    stop music fadeout 5.0
    pause 5.0
    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#00ff00}ХОРОШАЯ КОНЦОВКА{/color}{/size}\n{color=#000}Концовка Сесилии{/color}{/font}" with dissolve
    pause 2.0
    achieve END_CECILIA
    pause 3.0
    hide text with dissolveslow
    pause 1.0
    scene bg black with dissolveslow
    pause 3.0
    play music bgm_chaos
    call screen credits(180, True)
    stop music fadeout 5.0
    $ _skipping = True
    pause 5.0
    show text "Это произведение является вымышленным. Любое сходство с реальными событиями и людьми, живыми\nили мёртвыми, является случайным. Мнения, выраженные персонажами этого\nпроизведения, не обязательно совпадают с мнением автора." with dissolvemed
    pause 15.0
    hide text with dissolvemed
    $ quick_menu = True
    $ music_info = True
    hide screen lock_hotkeys
    call ending_message
    call end_menu
    return

label d3a3_martyr_ending:
    call save_file_name_update (3, "d3a3_martyr_ending")
    scene bg black
    scene bg frontdoor open:
        xalign 0.5 yalign 0.5 zoom 1.5
        easein 20.0 zoom 1.0
    with dissolveslow
    $ renpy.music.set_volume(0.0, 0, channel="ctc_sfx")
    U "{cps=6}.....{/cps}"
    U "So...{w=1.0} This is how it ends..."
    U "Why...? Why did this have to happen to us..." with shakeonce
    U "...Come on.{w=0.5} Get up."
    U "[name_player] made the choice for us, as we always wanted."
    scene bg frontdoor open
    show oriana_raw hidden at myleft
    show cecilia_raw hidden at myright
    with dissolveslow
    U "She...wanted this...right...?"
    U "Of course not!{w=1.0} How could she..." with shakeshort
    U "How could she...have truly wanted to die...?" with shakeonce
    U "...It must've been {color=#ff0000}Hell{/color}..."
    U "But...I guess we'll never know now..."
    U "Let's go. We...need to honour her decision.{w=1.0} Her [t_clue]sacrifice[t_cluee]."
    U "{cps=6}..........{/cps}" with shakeonce
    scene bg frontdoor open
    with dissolveslow
    $ renpy.music.set_volume(1.0, 0, channel="ctc_sfx")
    pause 5.0
    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#00ff00}ХОРОШАЯ КОНЦОВКА{/color}{/size}\n{color=#000}Концовка мученика{/color}{/font}" with dissolve
    pause 2.0
    achieve END_MARTYR
    pause 3.0
    hide text with dissolveslow
    pause 1.0
    scene bg black with dissolveslow
    pause 3.0
    play music bgm_death
    call screen credits(180, True)
    stop music fadeout 5.0
    $ _skipping = True
    pause 5.0
    show text "Это произведение является вымышленным. Любое сходство с реальными событиями и людьми, живыми\nили мёртвыми, является случайным. Мнения, выраженные персонажами этого\nпроизведения, не обязательно совпадают с мнением автора." with dissolvemed
    pause 15.0
    hide text with dissolvemed
    $ quick_menu = True
    $ music_info = True
    hide screen lock_hotkeys
    call ending_message
    call end_menu
    return

label d3a4:
    stop music
    scene bg black
    Y shadow "{cps=6}..........{/cps}{cps=1} {/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    play sound sfx_knifedrop
    extend "" with shakeshort
    play ctc_sfx "<silence 1.0>"
    Y "{cps=12}I...can't do it...{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    window auto hide
    pause 3.0
    I "But...there's [t_clue]no other option[t_cluee]... ...Right...?"
    play ctc_sfx "<silence 1.0>"
    I "....."
    play ctc_sfx "<silence 1.0>"
    I "Maybe..."
    play ctc_sfx "<silence 1.0>"
    I "Maybe if I think about it from another angle..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    scene bg black
    show oriana_raw hidden at myleft_trial, backedaway_on, grayscale_on
    show cecilia_raw hidden at myright_trial, backedaway_on, grayscale_on
    show pov_knife at grayscale_on:
        xalign 0.5 yalign 1.0 zoom 0.8
    with dissolveslow
    pause 0.5
    I "If I [t_clue]ignore all the options[t_cluee] in front of me..."
    play ctc_sfx "<silence 1.0>"
    scene bg frontdoor at grayscale_on
    with dissolvemed
    pause 0.5
    I "Then...what could I do...?"
    play ctc_sfx sfx_heartbeat_single
    I "[t_clue]What else[t_cluee] could we do to get the door open...?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    I "Think, [name_player_true]... Think back to everything you saw..."
    play ctc_sfx "<silence 1.0>"
    scene bg bedroom corpse pac at grayscale_on
    with dissolvemed
    pause 0.5
    I "There was so much new information...{w=1.0} All at once, too..."
    play ctc_sfx "<silence 1.0>"
    scene cg deaddog at grayscale_on
    with dissolvemed
    pause 0.5
    I "Filter out the [t_clue]chaotic emotions[t_cluee]... The insanity of it all..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    scene cg ria hearttoheart2 at grayscale_on
    with dissolveslow
    pause 0.5
    play ctc_sfx sfx_emotequestion
    pause 1.0
    I "...Wait..."
    play ctc_sfx "<silence 1.0>"
    I "Why is this coming to mind...?"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y depressed "...!!!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    window auto hide
    play sound sfx_shardobtain
    scene bg black
    with custom_flashbulb()
    pause 3.0
    scene bg foyer dark with dissolveslow
    I "....."
    play ctc_sfx "<silence 1.0>"
    I "...It's...hardly an argument...{w=0.5} Barely even a [t_clue]clue[t_cluee]..."
    play ctc_sfx sfx_heartbeat_single
    with custom_flashquick()
    I "But it's the {color=#ff0000}only lead{/color} I have left...!" with shakeshort
    Y blink "{cps=6}.....{/cps}{cps=1} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend default "Ria. Cece."
    $ fadein_sideimage = True
    scene bg foyer
    show oriana dejected at myleft_fadein
    show cecilia at myright_fadein
    with dissolvemed
    C surprised "...[name_player]?"
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}.....{/cps}"
    play ctc_sfx sfx_emotequestion
    Y leering "You two are [t_clue]hiding something[t_cluee] from me."
    O surprised "...!" with shakeonce
    C sad "Wh-what do you mean? Why would we need to hide anything from--"
    Y thinking "Cece. You've said before that the Occult Club visited this house to confirm an urban legend."
    C thinking "Y-yeah...?"
    Y blink "And Ria. You said that there are exactly three members in the club. You, Cecilia, and [t_clue]Carol-Maria[t_cluee]."
    O leering "Yes, but Carol-Maria didn't come with us, so--"
    play ctc_sfx sfx_heartbeat_single
    show bg foyer dark with custom_flashquick()
    Y angry "That's a {color=#ff0000}LIE{/color}." with shakeshort
    O afraid "Wha-- Wh-what are you talking about?" with shakeonce
    Y leering "[t_clue]Carol-Maria[t_cluee] came to this house with you two.{cps=2} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend "That's a fact."
    Y thinking "Ria, you don't like Cece, and you don't like the occult."
    Y blink "It's not exactly difficult to deduce. The only reason you joined the club was because Carol-Maria did."
    Y leering "There's no way you'd be here right now if it wasn't for your best friend dragging you along." with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    O depressed "...That's...not..." with shakeonce
    C sad "Sorry, but does any of this matter? Are you suggesting we find and kill Carol-Maria or something?"
    Y thinking "I don't know if I would go that far, but...the fact that she's kept herself hidden this whole time is very suspicious."
    play ctc_sfx "<silence 1.0>"
    O troubled "Y-you...{w=0.5} Are you suggesting that...{w=0.5}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    extend " That Carol-Maria...?!" with shakeonce
    Y shadow2 "Might be the [t_clue]true mastermind[t_cluee] behind this killing game, yes."
    play ctc_sfx sfx_heartbeat_single
    O horrified "YOU--" with shakelong
    Y troubled "...Ria. Tell me the truth." with hpunch
    play ctc_sfx "<silence 1.0>"
    O depressed "{cps=6}.....{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    play loop_sfx sfx_heartbeat fadein 2.0
    O dejected "There's...nothing to tell..."
    O irritated "Carol-Maria...isn't here...{w=1.0} And even if she was, she's not a murderous maniac..."
    O "You... You DARE accuse her of such HEINOUS crimes?!{w=1.0}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    extend troubled "\nI...{w=1.0}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    show oriana depressed at myleft:
        linear 3.0 xalign 0.5
    extend " I'll ki--{w=1.0}{nw}" with shakeshort
    play ctc_sfx "<silence 1.0>"
    show bg black
    show oriana horrified at myleft
    show cecilia surprised
    with custom_flashquick()
    stop loop_sfx
    play sound sfx_deskslam
    Y scream "{size=+10}TELL ME THE TRUUUUUUTH!!!{/size}" with shakelong
    O "!!!" with shakeshort
    C "....." with shakeonce
    Y shocked "Why...? Why are you two [t_clue]trying to make me decide[t_cluee]...?"
    $ fadein_sideimage = False
    Y pained "What is going on?! Why are you doing this?! These are YOUR lives on the line here!" with shakeshort
    $ fadein_sideimage = True
    O afraid "....."
    Y pained2 "I...{cps=1} {/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend "I don't want to let either of you die..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y "[t_clue]Don't make me decide[t_cluee]...{cps=1} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend "Please..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    O shadow "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    C sad "{cps=6}...............{/cps}"
    play ctc_sfx sfx_emotequestion
    C thinking "...Ria. I think it's time for a new plan."
    O afraid "Huh? A...new plan?" with hpunch
    C default "It's something I realized after checking something in the attic."
    C surprised "Oh, but first..."
    Y shocked "Wh-what are you two talking abo--"
    play ctc_sfx sfx_whoosh
    window auto hide None
    scene bg foyer
    show oriana panicked at myleft
    show cecilia_raw blink at mycenter
    with custom_flashquick()
    scene bg black
    with soulout
    pause 1.0
    window auto hide
    play sound sfx_fallsoft
    pause 5.0

    call save_file_name_update (3, "d3a4")
    I "....."
    I "......."
    I ".........{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " ...Ugh..." with hpunch
    I "Where... What...happened...?"
    $ show_side_cecilia = True
    C hidden "Oh! Look, [name_player]'s starting to wake up!"
    $ show_side_cecilia = False
    window auto hide
    pause 1.0
    scene bg basement stairway at blurred
    show cecilia at mycenter, blurred
    show eye frame
    with eyeopen_slow
    scene bg black with eyeclose_slow
    scene bg basement stairway at blurred
    show cecilia at mycenter, blurred
    show eye frame
    with eyeopen
    scene bg black with eyeclose
    scene bg basement stairway:
        blur 20.0
        linear 1.0 blur 0.0
    show cecilia at mycenter:
        blur 20.0
        linear 1.0 blur 0.0
    with eyeopen_quick
    pause 3.0
    C happy "Hi, [name_player]! Are you feeling okay? Any dizziness?"
    YV hidden "...Cece...? What...happe...?"
    play ctc_sfx sfx_heartbeat_single
    $ fadein_sideimage = False
    YV "...! Wha... What's wrong with my voice?! W-wait, my body...?!" with shakeshort
    $ fadein_sideimage = True
    show cecilia surprised at mycenter:
        blur 0.0
    C "Oooh, yeeeeah, see, about that..."
    play ctc_sfx "<silence 1.0>"
    show bg black
    C grin "You're [t_clue]possessing the zombie's body[t_cluee] right now."
    show bg basement stairway:
        matrixcolor BrightnessMatrix(-1.0)
        linear 5.0 matrixcolor BrightnessMatrix(0.0)
    YV default "...H-huh?!{cps=1} {/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend "P-possessing?!{cps=1} {/cps}Wh-what's that supposed to...?!" with shakeshort
    play ctc_sfx sfx_restrain
    with custom_flashquick()
    YV "Nrgh...! Wh-why am I [t_clue]tied to this chair[t_cluee]...?! Is this... D-did you...?!" with shakeshort
    $ show_side_oriana = True
    O afraid "...It really worked..."
    $ show_side_oriana = False
    $ fadein_sideimage = True
    window auto hide
    show cecilia_raw as cecilia at mycenter_to_myright, backedaway_on
    pause 0.3
    show oriana afraid at myleft with dissolvemed
    O "[name_player] is...controlling his dead body..."
    YV "R-Ria! What is going on?! Please, you have to tell me!" with shakeshort
    $ fadein_sideimage = False
    play ctc_sfx sfx_restrain
    YV "Nrgh! H-how is this happening?! WHY are you two doing this?!" with shakeshort
    $ fadein_sideimage = True
    O dejected "I..." with hpunch
    show cecilia thinking at myright, backedaway_off
    C "Actually, before we get into that, let me check on what you know already, [name_player]."
    YV "H-huh...?! Wh-what I...{i}know{/i}...?"
    play ctc_sfx sfx_heartbeat_single
    C smile "First of all... You know that [t_clue]you're already dead[t_cluee], right?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    YV "...!!! H-how did you know that...? I didn't..." with shakeshort
    C sad "It's a bit of a complicated story. But okay, let's start from the beginning."
    window auto hide
    play sound sfx_doorclose
    pause 0.5
    with hpunch
    pause 0.5
    C surprised "...Oh! Actually, maybe it'd be better to hear it from [t_clue]her[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    YV "{cps=6}...\"Her\"...?{/cps}"
    play ctc_sfx "<silence 1.0>"
    scene bg basement stairway with dissolvemed
    I "And then I saw it.{w=1.0} The craziest, most unbelievable sight."
    play ctc_sfx sfx_steps
    scene bg black with dissolvemed
    pause 2.0
    I "A new figure emerged from the library door.{w=1.0} And now, standing in front of me..."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    show karma_raw tired as karma at mycenter
    with dissolveslow
    pause 3.0
    I "{cps=6}...was{/cps}{w=0.5} [t_clue]me[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    show bg basement stairway with dissolvemed
    pause 2.0
    show karma tired at mycenter
    YV "{cps=6}..........{/cps}"
    show karma tired at mycenter, backedaway_off
    $ name_karma = "{color=#cccc00}"+input_name+"?{/color}"
    K "......."
    K tiredblink "...[name_player]...{w=0.5}was {i}your{/i} name, right?{nw}"

    menu:
        extend ""
        "\"Who are you?\"":
            YV "...Wh-who... Who are you...?" with hpunch
            K "....."
        "\"Wait. You're...\"":
            YV "...You...must be..." with hpunch
            K "{cps=6}.....{/cps}{w=0.5} ...Yes."
    K tired "My name is [t_clue]Carol-Maria[t_cluee].{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend panicked " Ah, b-but you can call me \"Karma\" for short." with hpunch
    $ name_karma = _("Karma")
    YV "Ka... Karma...?"
    K sweatdrop "Yeah, it's a nickname Cece came up with. Cool, right? Ahaha..."
    YV "But...you're... I-I mean, I was..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    K tired "You lost all your memories, so [t_clue]you thought you were me[t_cluee], right?"
    play ctc_sfx "<silence 1.0>"
    YV "....."
    play ctc_sfx "<silence 1.0>"
    K tiredblink "{cps=16}But the truth is...{/cps}{w=0.5}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend tired "you're a [t_clue]spirit[t_cluee] that was possessing my body this entire time." with shakeonce
    play ctc_sfx "<silence 1.0>"
    YV shadow "{cps=6}.....{/cps} ...A...spirit..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    scene bg black with custom_flashbulblong()
    I "...At that moment, it all started to make sense..."
    play ctc_sfx "<silence 1.0>"
    I "How I remember my own death... My true name..."
    play ctc_sfx "<silence 1.0>"
    I "How my own \"face\" and \"body\" never felt right to me..."
    play ctc_sfx "<silence 1.0>"
    I "How it...always felt strange when I would be stabbed to death..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}...And also...{/cps}"
    play ctc_sfx sfx_wail
    window auto hide
    show ghostmessage_1 at truecenter with shakeshort
    hide ghostmessage_1 with dissolvemed
    pause 3.0
    scene bg basement stairway
    show karma sad at mycenter
    with dissolveslow
    YV "{cps=12}...It was you.{/cps}{cps=1} {/cps}You were the [t_clue]voice[t_cluee] screaming in my head."
    play ctc_sfx "<silence 1.0>"
    K "{cps=6}.......{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    YV "You were the one forcing me... Forcing {i}us{/i} to go back in time.{cps=1} {/cps}{cps=24}[t_clue]Restarting the killing game[t_cluee] over and over...{/cps}" with shakeonce
    play ctc_sfx sfx_heartbeat_single
    K afraid "...! Th-that's..." with shakeshort
    window auto hide
    show karma shocked at mycenter_to_myright
    $ _last_say_who = "O"
    pause 0.3
    show oriana leering at myleft
    with dissolve
    O "[name_player]. Please. Just hear us out."
    YV "...Ria..."
    O irritated "Once you know the [t_clue]whole truth[t_cluee], everything will make sense."
    play ctc_sfx "<silence 1.0>"
    YV shadow "{cps=6}.....{/cps}"
    O thinking "...Karma?"
    K shadow "....."
    play ctc_sfx "<silence 1.0>"
    K "...It... It feels like years ago now..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    play music bgm_origin_karma
    scene bg black with dissolveslow
    K "It all started when the three of us... Me, Cece, and Ria..."
    K "We traveled all the way out here to check out the legend of the Black Magic Mansion."
    K "But as soon as we opened the door, I...I blacked out. And when I came to..." with hpunch
    scene bg foyer at grayscale_on with dissolvemed
    pause 2.0
    scene bg frontdoor incomplete at grayscale_on with dissolvemed
    pause 2.0
    K "The three of us were in the foyer of this house, with that horrible red writing on the front door."
    scene bg black with dissolvemed
    pause 2.0
    K "Of course, we tried to ignore it at first. After all, the three of us are friends. There's no way we could turn against each other."
    K "We focused on trying to look for a way out, or at least some answers as to why we were trapped here."
    play ctc_sfx "<silence 1.0>"
    K "But then..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    scene bg black
    show bloodsplatter_2 at truecenter, blurring
    with custom_flashbulbred()
    pause 2.0
    K "...I can't remember who died first anymore.{w=1.0} Either Cece or Ria suddenly snapped, and the other one...{w=1.0}was {color=#ff0000}murdered{/color}."
    K "It was like the worst possible nightmare.{w=0.5} And...{w=0.5}I honestly thought that's what it was. Because the very next moment..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    scene bg foyer at grayscale_on with custom_flashbulblong()
    pause 2.0
    K "...I woke up in the foyer again. Cece and Ria were both alive, and didn't remember what happened."
    K "My own memories faded away quickly, so I thought it really {i}was{/i} just a gross dream."
    K "I decided to forget about it, and we tried looking for a way out all over again."
    play ctc_sfx "<silence 1.0>"
    scene bg black
    show bloodsplatter_1 at truecenter, blurring
    show bloodsplatter_2 at truecenter, blurring, upsidedown
    with custom_flashbulbred()
    pause 2.0
    K "And then it happened again."
    play ctc_sfx "<silence 1.0>"
    K "Someone died,{w=1.0} I screamed in despair,{w=1.0} and then...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    hide bloodsplatter_1
    hide bloodsplatter_2
    show bg foyer at grayscale_on
    with custom_flashquick()
    extend " I woke up in the foyer again." with shakeonce
    scene bg black with dissolvemed
    K "This sequence kept going over and over until finally, I realized what was going on."
    K "I was beginning to remember things that happened before time would rewind."
    K "Just like you, I also figured out that the culprit was in the basement."
    K "But whenever we were able to confront him..."
    play ctc_sfx "<silence 1.0>"
    scene bg black
    show bloodsplatter_1 at truecenter, blurring
    show bloodsplatter_3 at truecenter, blurring
    show bloodsplatter_2 at truecenter, blurring
    with custom_flashbulbred()
    pause 2.0
    K "He would kill one of us, and then time would rewind yet again." with shakeshort
    play ctc_sfx sfx_heartbeat_single
    window auto hide None
    scene bg black with custom_flashquick()
    window auto show None
    K "...There was no way out. I watched Cece and Ria die over and over..." with shakeshort
    K "Out of desperation, I even tried killing myself to set them free, but...time would rewind just before I could fade away..."
    K "I have [t_clue]no control[t_cluee] over my ability to rewind time." with shakeonce
    K "Probably because...deep down, I can't EVER be okay with any of us dying..."
    K "So it wouldn't stop."
    play ctc_sfx "<silence 1.0>"
    scene cg karma4 at grayscale_on:
        parallel:
            xalign 0.5 yalign 0.7 zoom 1.3
            linear 20.0 zoom 1.0
        parallel:
            xoffset 0 yoffset 0 matrixcolor BrightnessMatrix(0.0)
            choice:
                pause 1.0
            choice:
                pause 3.0
            choice:
                pause 5.0
            linear 0.05 xoffset 10 yoffset 10 matrixcolor BrightnessMatrix(-0.5)
            linear 0.05 xoffset -10 yoffset -10 matrixcolor BrightnessMatrix(0.0)
            linear 0.05 xoffset 10 yoffset 0 matrixcolor BrightnessMatrix(-1.0)
            linear 0.05 xoffset 0 yoffset -10 matrixcolor BrightnessMatrix(0.0)
            repeat
    with dissolvemed
    pause 2.0
    K "The killing game would restart, and no matter what I did, someone ends up dead."
    K "Even if I ask us all to do nothing, the culprit eventually comes and kills us."
    K "...My memories were no longer fading. I started to remember everything. [t_clue]All the horrible details[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    K "{cps=24}Over and over and over and over and over and over and over again,{/cps}{w=1.0} the killing game repeated..." with shakeonce
    K "What should've been a 20 hour killing game became days, weeks, months, years, maybe decades..."
    K "The pain of dying... The pain of having your best friend die in front of you..." with shakeonce
    K "The pain of watching your best friend become a murderer..."
    play ctc_sfx "<silence 1.0>"
    K "Even...{w=0.5}the pain of killing your best friend with your own two hands..." with shakeonce
    K "It was nonstop.{w=0.5} Endless."
    K "All I knew was pain. And no matter how much I struggled, I couldn't escape..."
    play ctc_sfx "<silence 1.0>"
    K "{color=#ff0000}I wanted to die.{/color}{w=1.0} I wanted to fade away.{w=0.5} I wanted to stop caring about my friends so I could leave them for dead."
    K "But no matter what attitude I had, it would always end the same... Time would flow back to the beginning..." with shakeonce
    K "The beginning of [t_clue]yet another killing game[t_cluee]..."
    K "Until finally...{w=1.0} Right from the moment I woke up in the foyer once again..."
    play ctc_sfx "<silence 1.0>"
    stop music
    show bg black
    K "I broke.{w=2.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    window auto hide None
    scene bg foyer at grayscale_on
    show oriana panicked at myleft, grayscale_on
    show cecilia surprised at myright, grayscale_on
    with custom_flashquick()
    window auto show None
    $ show_side_karma = True
    $ grayscale_sideimage = True
    $ fadein_sideimage = False
    K scream "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAUUUUUUUUUUUUUU\nUUUUUUUUUUUUUUUUUUUGGGGGGHHHHHHH!!!" with shakelong
    $ fadein_sideimage = True
    C "Uwawaaah! K-Karma?!" with shakeonce
    O shouting "What happened?! Did you have a nightmare?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    K crying "*pant* I-I...can't..." with shakeonce
    $ fadein_sideimage = False
    K "I can't... *sniff* ...Do this anymore..." with shakeshort
    $ fadein_sideimage = True
    O confused "Wh-what are you talking about? We only just woke up--"
    play ctc_sfx sfx_deskslam
    show oriana panicked
    show bg foyer at grayscale_on, wobble, blurring
    with custom_flashquick()
    play loop_sfx sfx_heartbeat
    K afraid "NO!! We've been here FOREVER! There's no way out!" with shakelong
    O depressed "...Karma...?"
    K crying "I don't want to reset the clock!{cps=2} {/cps}I'm DONE trying to get a happy ending!" with shakeshort
    $ fadein_sideimage = False
    K afraid "God... Satan...{w=1.0}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    extend pained2 " Anyone, PLEASE! Just end this already!" with shakeshort
    K depressed "Have one of us die... Or have ALL of us die...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend scream " I DON'T CARE ANYMORE!!" with shakelong
    $ fadein_sideimage = True
    C sad "....."
    play ctc_sfx "<silence 1.0>"
    O injured "......." with shakeonce
    K depressed "{cps=12}End this game...{/cps}" with hpunch
    $ fadein_sideimage = False
    K pained2 "End it...{w=0.5} Please..." with hpunch
    show oriana_raw injured as oriana at backedaway_on:
        blur 0
        linear 15.0 blur 20
    show cecilia_raw sad as cecilia at backedaway_on:
        blur 0
        linear 15.0 blur 20
    show bg foyer at grayscale_on:
        matrixcolor BrightnessMatrix(0.0)
        linear 15.0 matrixcolor BrightnessMatrix(-1.0)
    K scream "END IT!{w=0.5}{cps=24} End it, end it, end it, end it, end it, end it, end it...{/cps}" with shakeshort
    K pained2 "{cps=24}End it, end it, end it, end it, end it, end it, end it, end it, end it, end it, end it, end it, end it...{/cps}" with shakeshort
    K afraid "{cps=36}END IT END IT END IT END IT END IT END IT END IT END IT END IT END IT END IT END IT END IT END IT END IT END--{/cps}{nw}" with shakelong
    $ fadein_sideimage = True
    play ctc_sfx sfx_slap
    stop loop_sfx
    window auto hide None
    scene bg white with shakeshort
    scene bg foyer at grayscale_on:
        blur 20
        linear 5.0 blur 0
    show oriana leering2 at mycenter_closeup, grayscale_on:
        blur 20
        linear 5.0 blur 0
    with custom_flashbulb()
    pause 2.0
    K dejected "{cps=6}..........{/cps}"
    $ fadein_sideimage = False
    K "...I..."
    $ fadein_sideimage = True
    O shouting "KARMA!! Get a grip already!!" with shakeshort
    K shocked "...R-Ria..." with hpunch
    O leering "You...{w=0.5} This isn't you!{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " You're the type to [t_clue]never give up[t_cluee], no matter how hard things get!" with shakeonce
    K crying "But I WANT to give up! I don't want to do this anymore!" with shakeshort
    $ fadein_sideimage = False
    K dejected "Even if we all need to die...{w=0.5} I just want this to finally end..."
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    O injured "...Don't..."
    play ctc_sfx "<silence 1.0>"
    O "Don't talk like that..." with hpunch
    play ctc_sfx "<silence 1.0>"
    K "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    $ _last_say_who = "O"
    show oriana irritated at myleft, grayscale_on
    show cecilia surprised at myright_fadein, grayscale_on
    with dissolvemed
    pause 1.0
    O "......."
    O leering2 "Please... Just tell us what happened."
    play ctc_sfx "<silence 1.0>"
    K crying "{cps=6}.......{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolveslow
    $ show_side_karma = False
    K "...But as I was weakly telling them about my time traveling for possibly the millionth time..."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 1.0
    show villain_raw as villain at mycenter, backedaway_on, grayscale_on
    with dissolveslow
    pause 1.0
    K "{cps=6}...That's{/cps}{w=0.5} when [t_clue]he[t_cluee] appeared."
    play ctc_sfx "<silence 1.0>"
    $ show_side_karma = True
    K depressed "...!! You..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    window auto hide
    show bg foyer at grayscale_on with dissolveslow
    window auto show
    show villain as villain at backedaway_off, grayscale_on
    V "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}..........{/cps}{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " ...Good evening.{nw}"
    play ctc_sfx "<silence 1.0>"
    $ name_villain = _("Corpse?")
    play music bgm_discussion
    extend "" with shakeonce
    V "I understand you are having quite a bit of trouble with the writing on that door...?"
    play ctc_sfx "<silence 1.0>"
    $ show_side_oriana = True
    $ show_side_cecilia = True
    O afraid "K-Karma, is that...?" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotehappy
    C overjoyed "A zombie! Guys, it's a real zombie!" with vpunch
    K shouting "Why are you here?! What are you up to?!" with shakeshort
    $ fadein_sideimage = True
    V "....."
    V "Hm... So it's true then... You come from the future..."
    K leering "....."
    V "Oh, pardon my lack of etiquette. It has been quite some time since I have last spoken to...guests."
    V "The blonde one appears to recognize me, but as for you other maidens...{w=0.5} I hope you are not alarmed by my appearance."
    C overjoyed "..... [u_music_note]" with vpunch
    V "Let's see... My name is hardly relevant these days..."
    V "Please refer to me as...{w=1.0}the [t_clue]Professor[t_cluee]."
    $ name_villain = _("The Professor")
    O afraid "...The...Professor...?"
    play ctc_sfx sfx_whooshlow
    window auto hide custom_flashquick()
    K shouting "ENOUGH SMALL TALK!! Answer me! WHY are you up here?!" with shakeshort
    V "There's no need to be on guard. I do not intend to harm you for the duration of this conversation."
    V "I am here right now to offer you...{w=1.0}a [t_clue]solution[t_cluee]."
    K panicked "A solution? You mean...you'll let us leave?" with shakeonce
    V "Unfortunately, that won't be possible. The solution is regarding your unwanted time traveling ability."
    V "My apologies for eavesdropping on your private conversation."
    play ctc_sfx sfx_emotesigh
    C sweatdrop "You're weirdly polite for an evil zombie mastermind..." with hpunch
    $ fadein_sideimage = False
    O leering "What's the solution?"
    $ fadein_sideimage = True
    V "It's this object here."
    scene bg black
    show shackle_green at truecenter:
        zoom 0.75 alpha 0.0
        easein 10.0 zoom 1.0 alpha 1.0
    with dissolvemed
    pause 2.0
    $ show_side_villain = True
    K thinking "...A bracelet? No, isn't that a [t_clue]wrist shackle[t_cluee]?"
    $ fadein_sideimage = False
    V "Simply put this on, and your body will be possessed by a [t_clue]spirit[t_cluee] pulled from {color=#ff0000}Hell{/color}."
    play ctc_sfx "<silence 1.0>"
    K panicked "My body will-- Wait, a SPIRIT?!" with shakeshort
    O surprised "Wh-what?! And we're expected to believe that?!" with shakeonce
    V "I assure you, it is no joke nor exaggeration. If I understand your dilemma correctly..."
    V "Any...conclusion of the killing game triggers your power to restart it. Regardless of your own will, yes?"
    V shadow "But that should not come as a surprise. It is only human to desire your friends' safety...{w=1.0}and fear for your own life."
    play ctc_sfx "<silence 1.0>"
    K sad "....." with shakeonce
    V default "If your time traveling ability does indeed extend from your unyielding spirit, then why not cut it at the source?"
    V "By allowing the spirit to possess your body, your own consciousness will fall into a deep slumber. In other words..."
    V "The spirit will take your place in the killing game...{w=1.0}and YOU will be [t_clue]blind[t_cluee] to its ultimate outcome."
    play ctc_sfx sfx_heartbeat_single
    K depressed "...!!" with shakeonce
    O afraid "That's... Karma, you're not thinking of--"
    $ fadein_sideimage = True
    $ _last_say_who = "V"
    $ show_side_villain = False
    scene bg foyer at grayscale_on
    show villain at mycenter, grayscale_on
    with dissolvemed
    V "As I unfortunately cannot spare all of your lives, is this not an ideal proposition for both our sides?"
    V "I assure you that as a being from {color=#ff0000}Hell{/color}, the spirit will most certainly make a [t_clue]decisive choice[t_cluee] to end someone's life."
    play ctc_sfx "<silence 1.0>"
    V "And so long as your consciousness is in a deep, unknowing slumber, your [t_clue]curse[t_cluee] should not activate." with shakeonce
    K shadow "....."
    V "While I cannot say which of you three shall perish, the tragic loop you've been enduring will finally come to a definitive [t_clue]end[t_cluee]."
    O irritated "...Karma. No matter how well-spoken he is, you cannot trust a psychopath who {i}insists{/i} on someone getting murdered."
    $ fadein_sideimage = False
    O leering2 "There has to be another way.{w=0.5} We'll find it." with hpunch
    play ctc_sfx "<silence 1.0>"
    K "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    K tiredblink "...Yeah. You're right, Ria."
    K leering "I'm sorry, Mr. Professor, but I have to decline your proposition."
    C surprised "Huh? Wait, we're not doing it?" with hpunch
    play ctc_sfx sfx_emotesob
    C sobbing "Aw, but getting to meet a spirit from Hell would've been SOOOO cool, though..." with hpunch
    O annoyed "Cecilia, be quiet."
    $ fadein_sideimage = True
    V shadow "...And you are certain that you will not change your mind?"
    K sad "Yes. I can't just escape responsibility like that and let some [t_clue]stranger[t_cluee] kill my friends."
    $ fadein_sideimage = False
    K surprised "But can we negotiate some more? Exactly WHY can't you spare our lives?"
    K tired "Depending on what your goal is, maybe we can--{w=0.75}{nw}"
    play ctc_sfx "<silence 1.0>"
    play sound sfx_knifestab
    stop music
    show bg black
    show bloodsplatter_1 behind villain at truecenter:
        alpha 0.5
    show villain at mycenter_closeup, grayscale_on
    with custom_flashquickred()
    extend shocked " ...!!!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    V "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    V shadow "...Even if time will rewind, so be it."
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolvemed
    play sound sfx_fallhard
    show bloodsplatter_2 at truecenter:
        alpha 0.5
        linear 2.0 alpha 0.0
    with shakeshort
    pause 2.0
    scene bg bloodpool 1
    with dissolvemed
    pause 2.0
    K depressed stabbed "{cps=6}.....{/cps}"
    $ fadein_sideimage = False
    O depressed "...Karma...?"
    C surprised "...Wait..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    scene bg bloodpool 2
    with dissolvemed
    C injured "Did that...really just happen...?" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    K shadow stabbed "Ngh... {size=-10}...ah...{/size}" with shakeshort
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    scene bg bloodpool 3
    with dissolvemed
    O stabbed "{cps=6}...No...{/cps}{cps=2} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend horrified "NOOOOOOOOOO!!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    $ show_side_villain = True
    V shadow "This is our [t_clue]only option[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    play sound sfx_wail
    V "I'm sure after a few more loops...you will change your mind..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    play sound2 sfx_rewind
    $ show_side_villain = False
    $ fadein_sideimage = True
    scene bg black with pixellate
    $ show_side_oriana = False
    $ show_side_cecilia = False
    $ show_side_karma = False
    $ grayscale_sideimage = False
    pause 5.0
    K "...And it ended up exactly as he said."
    K "Even while remembering that conversation with the Professor, I still made no progress finding us a way out."
    K "I looped through several more killing games. My heart continued to crumble even more..."
    play ctc_sfx "<silence 1.0>"
    K "{cps=12}And eventually...{/cps}{w=1.0}I gave up.{w=1.0} The Professor appeared, and I accepted his offer before he could even explain it."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 1.0
    scene bg black at grayscale_on
    show oriana_raw surprised at myleft, grayscale_on
    show cecilia_raw surprised at myright, grayscale_on
    with dissolvemed
    pause 2.0
    K "And the last thing I said to my friends before [t_clue]abandoning them[t_cluee] was..."
    play ctc_sfx "<silence 1.0>"
    K "\"No matter what the spirit decides... No matter who gets killed, be it one of you two...or even me...\""
    play ctc_sfx "<silence 1.0>"
    K "\"...Accept the outcome. Accept it as [t_clue]the ending[t_cluee] to this story...\""
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolveslow
    pause 1.0
    scene bg basement stairway
    show karma tiredblink at mycenter
    with dissolveslow
    pause 1.0
    K "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    K sad "...You know what happened next, don't you, [name_player]?"
    YV shadow "{cps=6}.....{/cps} ...Even though you all left the final decision to me..."
    $ fadein_sideimage = False
    play ctc_sfx sfx_heartbeat_single
    YV "...{color=#ff0000}Nothing changed{/color}." with shakeshort
    YV "Your ability to rewind time would still activate whenever someone died..."
    YV "And no matter how hard Cece and Ria tried to pressure me, I refused to kill anyone..."
    YV "So now we're stuck at the same impasse."
    $ show_side_oriana = True
    $ show_side_cecilia = True
    O injured "....." with shakeonce
    C blink "....." with hpunch
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    K shadow "...That last part is where you're wrong."
    play ctc_sfx "<silence 1.0>"
    YV default "H-huh?" with shakeonce
    $ fadein_sideimage = False
    C smile "Let me take over from here, Karma."
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    K "{cps=6}.....{/cps}{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend sad " ...Okay."
    play ctc_sfx "<silence 1.0>"
    $ show_side_cecilia = False
    scene bg basement stairway with dissolvemed
    pause 1.0
    $ _last_say_who = "C"
    show cecilia at mycenter with dissolvemed
    C thinking "[name_player], do you remember when you jumped through the basement hatch, and into the underground passage?"
    YV "...Yeah...?"
    play ctc_sfx sfx_emotequestion
    C grin "That hatch is a [t_clue]Gate to Hell[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    YV "Wh-what?!" with shakeonce
    C thinking "To summarize the important details, it's a place where the boundary between the living and dead is very thin."
    C "Living people like us can't interact with it, but a spirit like you, well..."
    C blink "You would get burned to death because that's the process of the Gate [t_clue]pulling you back to where you belong[t_cluee]."
    YV shadow "..... That's..." with shakeonce
    C thinking "So in other words, if we cast the shackle harbouring you into the fires of the Gate from whence you came..."
    C smug "It's effectively the same as [t_clue]killing you[t_cluee]."
    C blush "And if you \"die\" like that, the condition for the front door would be met..."
    play ctc_sfx "<silence 1.0>"
    YV "...And all three of you can escape..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    O shadow "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    $ show_side_oriana = False
    window auto hide
    $ _last_say_who = "K"
    show cecilia_raw blink as cecilia at mycenter_to_myright, backedaway_on
    pause 0.3
    show karma shadow at myleft with dissolvemed
    K "...[name_player].{w=1.0} We finally found a way for all of us to escape."
    I "....."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    hide cecilia with dissolve
    $ _last_say_who = "K"
    show karma tiredblink at mycenter with move
    pause 1.0
    K tired "As someone who's already dead...{w=1.0} Won't you please show [t_clue]mercy[t_cluee] for those who still have their whole lives ahead of them?"
    window auto hide
    pause 0.5
    show karma crying2 with dissolvemed
    pause 0.5
    play music bgm_sad
    pause 1.5
    K "I...{w=1.0} I wish I didn't need to ask you to do this..." with hpunch
    K "From what Cece and Ria told me, you're actually a very kind soul who genuinely tried to protect all of us..."
    I "....."
    K crying "But now...{w=0.5} I need to ask you to...{w=1.0} ...To make the {color=#ff0000}ultimate sacrifice{/color}." with hpunch
    K crying2 "Please set me...{w=1.0} Set {i}us{/i} free from this neverending killing game.{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend "\nI'm begging you, [name_player]..." with hpunch
    play ctc_sfx "<silence 1.0>"
    I "......."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    show bg black with dissolveslow
    I "...We found it...{w=1.0} A solution that ends the killing game, and lets everyone escape with their lives."
    I "As for me... I've already lived my life. Do I really have the right to deny them of theirs?"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps} ...Karma looks torn about this. We shared a body for so long that I can tell she doesn't want to do this."
    I "It might be best if I make my decision before...{w=0.5}I too become someone she rewinds time to rescue..." with hpunch
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolvemed
    pause 0.5
    show oriana_raw dejected at myleft
    show cecilia_raw sad at myright
    with dissolvemed
    I "As for Cece and Ria... I...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " I don't think I could bear to see them die again..." with hpunch
    play ctc_sfx "<silence 1.0>"
    I "I already [t_clue]couldn't make the choice[t_cluee] to kill either of them before..."
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolveslow
    pause 1.5
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "...I guess...it's not a difficult decision to make..."
    play ctc_sfx "<silence 1.0>"
    I "Truly the [t_clue]final, final choice[t_cluee]..."
    play ctc_sfx "<silence 1.0>"
    YV shadow "{cps=6}...I...{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 1.5
    $ show_choicegrand = True
    $ menu_time_remaining = 9

label d3a4_finalchoice_fake:
    if seen_cece_hearttoheart:
        show screen menu_countdown("d3a4_finalchoice")
    else:
        show timer background at truecenter, grayscale_on, disabledcountdown_background_transform
    menu:
        "Sacrifice yourself and save them":
            hide screen menu_countdown
            jump d3a4_salvation_ending

label d3a4_finalchoice:
    play sound sfx_heartbeat_single
    with custom_flashquick()
    show bg black with shakeshort
    show timer background at truecenter, disabledcountdown_background_transform
    menu:
        "Sacrifice yourself and save them":
            jump d3a4_salvation_ending
        "Don't sacrifice yourself" if seen_cece_hearttoheart:


            hide timer background
            I "...It makes sense.{w=0.5} This is the ending I've been seeking." with shakeonce
            I "A way to save everyone...{w=0.5}{nw}"
            play ctc_sfx "<silence 1.0>"
            extend " We finally found it..." with shakeonce
            play ctc_sfx "<silence 1.0>"
            menu:
                "Sacrifice yourself":
                    window auto hide None
                    jump d3a4_salvation_ending
                "Don't sacrifice yourself":
                    play music bgm_sad
                    I "{cps=6}.....{/cps} ...Karma's been through absolute agony..."
                    play ctc_sfx "<silence 1.0>"
                    I "She doesn't deserve any more of this...{w=0.5} She deserves to be set [t_clue]free[t_cluee]..." with shakeonce
                    play ctc_sfx "<silence 1.0>"
                    menu:
                        "Come on, sacrifice yourself already":
                            window auto hide None
                            jump d3a4_salvation_ending
                        "Don't do it":
                            play music bgm_sad
                            I "{cps=6}.....{/cps} ...Why?"
                            play ctc_sfx "<silence 1.0>"
                            I "I'm already dead! Why shouldn't I do it?!" with shakeonce
                            play ctc_sfx "<silence 1.0>"
                            play music bgm_sad
                            I "They'll finally have a [t_clue]happy ending[t_cluee]!{w=1.0}{nw}" with shakeonce
                            play ctc_sfx "<silence 1.0>"
                            extend " It's the right thing to do!" with shakeshort
                            play ctc_sfx "<silence 1.0>"
                            menu:
                                "Okay, sacrifice yourself after all":
                                    window auto hide None
                                    jump d3a4_salvation_ending
                                "Seriously, stop":
                                    play music bgm_sad
                                    I "What is going on?!{w=1.0}{nw}" with shakeonce
                                    play ctc_sfx "<silence 1.0>"
                                    play music bgm_sad
                                    extend " [t_clue]Who are you?![t_cluee]" with shakeshort
                                    play music bgm_sad
                                    play ctc_sfx "<silence 1.0>"
                                    I "Why are you trying to prolong this?!{w=0.5} This nightmare has been going on for FAR too long already!" with shakeshort
                                    play ctc_sfx "<silence 1.0>"
                                    play music bgm_sad
                                    $ mute_choice = True
                                    menu:
                                        "Sorry, never mind, go ahead and sacrifice yourself":
                                            $ mute_choice = False
                                            play sound sfx_choicegrand
                                            window auto hide None
                                            jump d3a4_salvation_ending
                                        "There's something wrong here":
                                            play music bgm_sad
                                            pause 0.2
                                            play music bgm_sad
                                            pause 0.2
                                            play music bgm_sad
                                            pause 0.2
                                            play music bgm_sad
                                            pause 0.2
                                            play music bgm_sad
                                            pause 0.2
                                            play music bgm_sad
                                            pause 0.2
                                            $ mute_choice = False
                                            stop music
                                            window auto show custom_flashquick()
                                            I "...Huh?{w=0.5} Something's...wrong?" with hpunch
                                            play ctc_sfx "<silence 1.0>"
                                            I "What does that mean?{w=0.5} And why does it matter?"
                                            play ctc_sfx "<silence 1.0>"
                                            menu:
                                                "...Okay, it's nothing, go ahead and sacrifice yourself":
                                                    play music bgm_sad
                                                    window auto hide None
                                                    jump d3a4_salvation_ending
                                                "Think carefully about this...":
                                                    pause 1.0
                                                    I "{cps=6}.....{/cps}"
                                                    I "{cps=6}..........{/cps}"
                                                    I "{cps=6}...............{/cps}{nw}"
                                                    play ctc_sfx sfx_emotequestion
                                                    extend " ...Wait..." with shakeonce
                                                    play ctc_sfx "<silence 1.0>"
                                                    I "That's... Could it be...?" with shakeonce
                                                    play ctc_sfx "<silence 1.0>"
                                                    $ show_choicegrand = False
                                                    jump d3a5

label d3a4_salvation_ending:
    $ show_choicegrand = False
    scene bg black
    show karma shadow at mycenter
    with custom_flashbulb()
    pause 1.0
    show bg basement stairway with dissolvemed
    YV "...All right.{cps=2} {/cps}I'll do it."
    play ctc_sfx sfx_heartbeat_single
    K depressed "...!" with shakeonce
    K panicked "Did... Did you just say...?" with hpunch
    if died_with_regrets:
        YV shadow "While I wish I could return to the living world with you all..."
    else:
        YV shadow "It's not like I have any business to take care of in the living world. And besides..."
    $ fadein_sideimage = False
    YV "The fact of the matter is that I'm dead.{w=0.5} And I have no right to impede the lives of those who still live."
    $ show_side_oriana = True
    $ show_side_cecilia = True
    C sad "....."
    O leering2 "[name_player]... Are you absolutely certain?"
    YV default "...Yes. I am."
    play ctc_sfx "<silence 1.0>"
    O shadow "...You'll be returning to {color=#ff0000}Hell{/color}.{w=0.5} Most likely for good this time."
    YV "But that's where I was in the first place, right?"
    play ctc_sfx "<silence 1.0>"
    O injured "...But..." with shakeonce
    $ fadein_sideimage = True
    K tiredblink "Ria... Let's not drag this out."
    YV shadow "....."
    K "[name_player]... I'm so sorry it had to come to this."
    K sad "I wish... I wish we could've met under different circumstances." with hpunch
    YV default "...I'm just grateful I was able to meet you at all."
    K surprised "Huh?"
    YV "Ria talked a lot about you. In fact, she said--"
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotesigh
    O embarrassed "[name_player]! Y-you don't need to get into that right now!" with hpunch
    $ fadein_sideimage = True
    K "....."
    play ctc_sfx "<silence 1.0>"
    K "{cps=6}.....{/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend blink " ...Heh. Yeah, this sucks." with hpunch
    YV "...?"
    K default "If we met somewhere else...{w=0.5} If things happened just [t_clue]slightly differently[t_cluee]..."
    play ctc_sfx "<silence 1.0>"
    K happy "I'm sure we could've been good friends."
    YV "....."
    I "....."
    I "...Karma..."
    play ctc_sfx "<silence 1.0>"
    I "Take good care of [t_clue]them[t_cluee]...{w=1.0} I know you can do it..."
    play ctc_sfx "<silence 1.0>"
    $ show_side_oriana = False
    $ show_side_cecilia = False
    stop music fadeout 5.0
    scene bg black with dissolveslow
    call save_file_name_update (3, "d3a4_salvation_ending")
    pause 0.5
    scene bg basement hatch with dissolveslow
    pause 1.0
    I "...I guess I'm jumping in here again."
    I "But with my current body, time shouldn't rewind anymore."
    $ show_side_cecilia = True
    C surprised "...W-wait! [name_player]!" with shakeonce
    $ show_side_cecilia = False
    I "Huh? Is that...?"
    scene bg basement nocorpse
    show cecilia sad at mycenter
    with dissolvemed
    YV "...Cece...?"
    C surprised "I... Um, that is...uh..." with hpunch
    show cecilia pout at hop
    if died_with_regrets:
        C "Y-you said you wished you could return to the living world, right?"
    else:
        C "Y-you said you have nothing to take care of in the living world, right?"
    YV "Y-yeah...?"
    C surprised "Then...d-does that mean you...remember your old life?"
    play ctc_sfx sfx_emotequestion
    C "Including...your [t_clue]real name[t_cluee]?" with shakeonce
    YV "Not all the details, but yes for my name."
    play ctc_sfx "<silence 1.0>"
    C shouting "WHAT IS IT?! What is your name?!" with shakeshort
    $ show_side_karma = True
    K panicked "C-Cece...? What's going on with you...?" with hpunch
    $ show_side_karma = False
    $ fadein_sideimage = False
    if input_name_true == input_name:
        YV "[name_player_true] is in fact my real name."
    else:
        YV "It's...[name_player_true]. That's my real name."
    $ fadein_sideimage = True
    play ctc_sfx sfx_heartbeat_single
    C surprised "...!!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    C "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    C sad "{cps=6}..........{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    YV "...Cece...?"
    C surprised "...Ah. S-sorry, I didn't mean to interrupt like this..." with hpunch
    $ show_side_oriana = True
    O confused "..... ...?"
    $ show_side_oriana = False
    C happy "[name_player_true]!" with shakeonce
    YV "Wh-what now...?" with hpunch
    C smile "Thank you... Thank you for everything!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    C blush "[t_clue]I'll never forget you![t_cluee] Never ever ever ever EVER!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    YV shadow "{cps=6}.....{/cps}"
    $ fadein_sideimage = False
    YV "Yeah... I won't forget you either, Cece..."
    $ fadein_sideimage = True
    scene bg black with dissolveslow
    pause 0.5
    scene bg basement hatch with dissolveslow
    pause 1.0
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "...And with this..."
    play ctc_sfx "<silence 1.0>"
    I "The killing game...finally comes to a {color=#ff0000}true end{/color}..."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 2.0
    $ show_choicegrand = True
    menu:
        "Jump in yourself":
            $ show_choicegrand = False
            pause 1.0
    play sound sfx_flameburst
    play loop_sfx sfx_flameloop
    scene bg flamewall with custom_flashbulblongred()
    pause 5.0
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}It...doesn't hurt...?{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}I'm...fading away...{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}...It's really over.{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide None
    play sound sfx_frontdoor
    with shakeshort
    pause 2.0
    I "{cps=12}The door opened...{w=0.5} It...worked...{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}...ood... ...bye...{/cps} {cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 2.0
    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show pac_assistant_shadow at truecenter:
        zoom 1.75 alpha 0.4
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#cc00bb}ИСТИНАЯ КОНЦОВКА{/color}{/size}\nКонцовка спасения{/font}"
    with dissolve
    achieve END_SALVATION
    pause 2.0
    stop loop_sfx fadeout 10.0
    show bg flamewall:
        linear 2.0 matrixcolor BrightnessMatrix(0.25) * SaturationMatrix(0.0)
    with dissolvemed
    pause 1.5
    hide pac_assistant_shadow
    hide text
    with dissolveslow
    show bg flamewall:
        linear 2.0 matrixcolor BrightnessMatrix(0.0) * SaturationMatrix(1.0)
    with dissolvemed
    pause 1.5
    play music bgm_death
    call screen credits(180, True)
    stop music fadeout 5.0
    $ _skipping = True
    scene bg black with dissolveslow
    pause 5.0
    show text "Это произведение является вымышленным. Любое сходство с реальными событиями и людьми, живыми\nили мёртвыми, является случайным. Мнения, выраженные персонажами этого\nпроизведения, не обязательно совпадают с мнением автора." with dissolvemed
    pause 15.0
    hide text with dissolvemed
    $ quick_menu = True
    $ music_info = True
    hide screen lock_hotkeys
    call ending_message
    call end_menu
    return

label end_menu:
    menu:
        "Load a save file":
            $ renpy.run(ShowMenu("load"))
            jump end_menu
        "Return to the Title Screen":
            pass
    return

label ending_message:
    scene bg black with dissolveslow
    S "Congratulations for winning Yet Another Killing Game!"
    S "Thanks to your constant efforts, the killing game is finally over...{w=1.0}\nBut are you satisfied with this conclusion?"
    S "If you're not, then...{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend " Will you play [t_clue]yet another killing game[t_cluee] by your own free will?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    S "Will you throw the cast of ladies back in danger once more, just to {color=#cccc00}seek the truth{/color}?"
    play ctc_sfx "<silence 1.0>"

    if seen_cece_hearttoheart and seen_ria_hearttoheart:
        if finalchoice_doubt:
            if name_karma == _("Karma"):
                S "{cps=6}And...{/cps}will you relentlessly pursue that truth...{w=0.5}even if it means denying {color=#cccc00}her final plea{/color}...?"
            else:
                S "And when Death calls for you to deliver tribute, will you always, always {color=#ff0000}REFUSE to make that choice{/color}?"
        else:
            S "And though you may grasp freedom through Death's embrace, will you hold strong and [t_clue]face a RED or BLUE fate[t_cluee] nevertheless?"
    else:
        S "Will you spend the time to forge bonds [t_clue]both RED and BLUE[t_cluee], then test their strength with {color=#ff0000}blade in hand{/color}?"

    play ctc_sfx "<silence 1.0>"
    S "{cps=6}The decision is yours...{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 3.0
    return

label d3a5:
    call save_file_name_update (3, "d3a5")
    scene bg white with custom_flashbulblong()
    achieve REJECT_TRUE
    pause 0.5
    scene bg basement stairway
    show karma tired at mycenter_fadein
    with dissolveslow
    pause 1.5
    YV shadow "{cps=6}..........{/cps}"
    K surprised "...? [name_player]? Is something wrong?"
    play ctc_sfx "<silence 1.0>"
    I "...I think I figured it out. The reason why we [t_clue]can't let it end like this[t_cluee]..." with shakeonce
    $ show_side_cecilia = True
    $ show_side_oriana = True
    O leering "...What's going on? Why did [name_player] suddenly go silent?"
    $ fadein_sideimage = False
    C thinking "Beats me..."
    $ fadein_sideimage = True
    I "But I better tread carefully here.{w=0.5} Otherwise...{w=0.5} they'll think I'm trying to weasel myself out of getting sacrificed..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "Deep breaths... Be ready for this, [name_player_true]..." with hpunch
    I "If you mess up your deductive reasoning here..."
    play ctc_sfx sfx_heartbeat_single
    with custom_flashquick()
    I "It's {color=#ff0000}game over{/color} for all of us." with shakeshort
    K worried "Um... Earth to [name_player]...?"
    YV "...If you don't mind waiting just a moment... I would like us to discuss something before I give my answer."
    $ fadein_sideimage = False
    O confused "...Discuss...something...?"
    C thinking "....."
    $ fadein_sideimage = True
    K surprised "What is it?"
    play music bgm_truth
    $ show_music_info_timer = music_info_pop_out_time()
    YV "There's something I realized just now. Something that the rest of you might not have realized yet." with shakeonce
    $ fadein_sideimage = False
    O leering2 "...What's going on? Are you trying to get us to spare you or something?"
    YV "Just hear me out. It's strange that you all think that killing me will let you escape.{w=1.0} After all...{nw}"

    menu:
        extend ""
        "\"I'm already dead.\"":
            YV default "I'm already dead. Casting me into the Gate is simply returning me to where I belong."
            YV "There's no guarantee that that truly counts as a \"death\" that will open the door. That's only Cece's theory."
            C sad "...[name_player]. Is that really what you wanted to say?"
            play ctc_sfx sfx_emotequestion
            YV "Huh?" with hpunch
            C thinking "Even if you're right, it's not like we have any other options. It's at least worth trying."
            C smile "Unless...you're just saying this to weasel yourself out of getting sent back to Hell?"
            YV "Th-that's not..." with shakeshort
            jump d3a5_gameover
        "\"The Professor's death didn't open it.\"":
            pass
        "\"The door won't open without me.\"":
            YV default "Whenever the front door opened, it was always while I was still alive."
            YV "So...maybe it's connected to me somehow. Like, maybe it's only when I find someone's dead body does it--"
            O disappointed "[name_player]. You've said before that you would sometimes find the front door open BEFORE finding someone's corpse."
            YV "...Ah." with hpunch
            O irritated "Also... Your usage of the words \"maybe\" and \"somehow\" doesn't make it convincing that you truly figured something out."
            O annoyed "And you say the door won't open without you, so are you trying to threaten us into sparing your life?" with shakeonce
            YV "N-no! That's not--" with shakeshort
            jump d3a5_gameover

    YV default "Even though we found the Professor... Found {i}this{/i} body dead in the bedroom upstairs..."
    YV "The front door didn't open for us. Even though it's always opened without fail before..." with shakeonce
    $ fadein_sideimage = True
    K leering "...The Professor..."
    C "Oh yeah, I suppose that WAS kinda strange..."
    $ fadein_sideimage = False
    C smile "But I mean, he was the [t_clue]mastermind[t_cluee], right? Maybe he was an exception to the rule."
    YV "...No. There's more to it."
    YV "The reason why the Professor's death didn't open the front door is simple.{w=1.0} It was because...{nw}"

    menu:
        extend ""
        "\"He was dead from the start.\"":
            YV "...He was already dead from the start. Remember when we found this body in the basement?"
            YV "Cece checked for a pulse, and got nothing. In other words, the Professor is [t_clue]already dead[t_cluee]."
            YV "That's why he can't \"die\" like the front door requires."
            $ fadein_sideimage = True
            K worried "....." with hpunch
            YV shadow "And that's why...as someone who's also dead...{cps=2} {/cps}I also can't \"die\" in a way that will open the door{cps=4}...?{/cps}"
            $ fadein_sideimage = False
            O disappointed "...You realized midway that your argument doesn't help us at all, didn't you."
            C sad "Also, did you forget what I'd JUST explained earlier? If we throw your shackle into the Gate to Hell, THAT will open the door."
            $ fadein_sideimage = True
            I "Crap, that could've gone better..." with shakeonce
            jump d3a5_gameover
        "\"He's the owner of the house.\"":
            YV "From what I remember from Karma's story, it sounded like he [t_clue]lives here[t_cluee]. He referred to you all as \"guests\", didn't he?"
            $ fadein_sideimage = True
            K panicked "Y-yeah, he did!" with shakeonce
            YV "Then I was right... The Professor has to be the [t_clue]father of the house[t_cluee]. The one in the lounge photos..."
            $ fadein_sideimage = False
            play ctc_sfx sfx_emotequestion
            YV "And that must be why his death didn't open the door. Because he set it up to react to only {i}our{/i} deaths."
            $ fadein_sideimage = True
            K shadow "That...makes sense..." with shakeonce
            O irritated "...[name_player]. Your utter lack of evidence for any of your claims aside..." with shakeonce
            $ fadein_sideimage = False
            O confused "Over the course of several killing games, you've personally investigated this whole house from top to bottom."
            O leering2 "You should know better than any of us that [t_clue]no one has lived here for a long time[t_cluee]."
            play ctc_sfx "<silence 1.0>"
            YV "Nrgh... B-but..." with shakeonce
            YV "But we also know that this corpse has been dead for a long time too."
            YV "That means the Professor... Somehow, he became an [t_clue]immortal being[t_cluee], and lived here in this house for several years." with hpunch
            C sad "...Uh... [name_player]?"
            C thinking "You just said he's dead. How can he {i}also{/i} be immortal?"
            YV "Th-that's because, um..." with shakeonce
            O irritated "Furthermore, {i}you{/i} were the one who checked his dead body in the bedroom."
            O annoyed2 "If he really was immortal, why didn't you notice any signs of life from him? Or did you simply choose not to tell us you did?" with shakeonce
            $ fadein_sideimage = True
            I "Crap... I think I'm [t_clue]on the right track[t_cluee] with this idea, but I should've come at it from another angle..." with shakeonce
            jump d3a5_gameover
        "\"He didn't actually die.\"":
            pass
    YV "...He's not dead. That's the only explanation."
    C sweatdrop "{cps=9}He's...{/cps}NOT dead.{w=0.5} Wow. Um...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend "okay?" with hpunch
    $ fadein_sideimage = True
    play ctc_sfx sfx_emotesigh
    K worried "...Uh... You lost me, [name_player]..." with hpunch
    O surprised "....."
    $ fadein_sideimage = False
    C thinking "You do know you're possessing his rotting corpse right now?"
    YV "I'm aware. But my point still stands. The Professor is not dead."
    C sad "Ooookay?{w=1.0} Then explain the corpse."
    C thinking "Remember, we found a knife stuck into it earlier."
    YV shadow "This body I'm currently in...{nw}"

    menu:
        extend ""
        "\"It's someone else's corpse.\"":
            YV default "...It doesn't belong to the Professor.{w=0.5}. This is a [t_clue]different man's body[t_cluee]."
            YV "After all, the way we found this body in the basement... And how it matches up with the man from the lounge photos..."
            play ctc_sfx sfx_heartbeat_single
            YV "This body has to be that of the [t_clue]father of the house[t_cluee]." with shakeonce
            $ fadein_sideimage = True
            K tired "....."
            C sad "...And your point iiiiis...?"
            $ fadein_sideimage = False
            YV "I'm saying the Professor and the father of the house are [t_clue]two different people[t_cluee]."
            YV "In other words, we should be searching for the Professor right now! The mastermind behind this killing game!" with shakeonce
            O irritated "...[name_player]. All three of us can attest to your body being the Professor's."
            O "We all watched as he appeared in person to give Karma the shackle containing your soul."
            YV "...Oh.{w=0.5} Okay, I didn't know that.{w=0.5} Let me try another angle. How about--"
            jump d3a5_gameover
        "\"It's an artificial body.\"":
            YV default "It's a life-sized mobile doll designed to look like a rotting corpse."
            YV "In other words, this is a decoy planted by the Professor to--" with shakeonce
            C sweatdrop "[name_player], you've officially lost us." with hpunch
            C thinking "There's no mistake that your current body is the very one that approached us at the beginning of the killing game."
            C smug "And he was definitely capable of regular human speech."
            C grin "But if you're still not convinced, I could stick my knife into your chest and try pulling out some organs...?"
            play ctc_sfx "<silence 1.0>"
            YV "N-no, that won't be necessary." with shakeonce
            O disappointed "Furthermore, do you believe you could be talking to us right now if your body was indeed an inanimate object?"
            O confused "I've heard of ghosts inhabiting objects, but never of them being able to speak aloud while doing so..."
            play ctc_sfx sfx_emotesigh
            $ fadein_sideimage = True
            I "I thought she was supposed to be an occult skeptic..." with hpunch
            YV "Okay, maybe this isn't a doll, but--" with shakeonce
            jump d3a5_gameover
        "\"It's a soulless shell.\"":
            pass
        "\"It's a puppet he can control.\"":
            YV default "It's a puppet body that the Professor can control at will."
            O irritated "Now's not the time for fantasies, [name_player]..."
            YV "No, remember the legend of the Black Magic Mansion? How people came to be [t_clue]controlled like puppets[t_cluee]?"
            O annoyed "I repeat: now's not the time for FANTASIES, [name_player]..." with shakeonce
            YV "Cece, what do you think? Couldn't this be the body of a victim of that legend?"
            C sad "Hmmmmm..." with hpunch
            $ fadein_sideimage = True
            K surprised "...Cece...?"
            C thinking "I guess it's {i}possible{/i}... Maybe with voodoo magic of some kind..."
            $ fadein_sideimage = False
            play ctc_sfx sfx_emotequestion
            C serious "But what's your point with this line of reasoning?{w=0.5} Are you saying {i}you're{/i} the Professor controlling the puppet right now?"
            YV "N-no, of course not! I'm just saying that the Professor was never actually in this body, and that's how he survived!" with shakeonce
            O irritated "...Then [t_clue]where is he right now[t_cluee], [name_player]?"
            YV "I-I... I don't know, probably outside of the house where we can't find him...?" with hpunch
            play ctc_sfx sfx_emoteshout
            O shouting "You're not making ANY sense! And even if you were, WHAT are you asking us to do?!" with shakeshort
            I "Nrgh...! N-no, this...{w=1.0} I know I'm [t_clue]getting closer to the answer[t_cluee], so what am I doing wrong...?!" with shakeonce
            jump d3a5_gameover
    YV default "...It is indeed the Professor's body, but without his [t_clue]soul[t_cluee]."
    $ fadein_sideimage = True
    K panicked "His...\"soul\"...?" with shakeonce
    C thinking "Uhh.... Isn't that the same as being dead?"
    $ fadein_sideimage = False
    YV "No.{w=0.5} His soul has left his body, but it's still technically alive, and is [t_clue]somewhere in this house[t_cluee]."
    O irritated "This is officially getting ridiculous..."
    YV "We've been through way more ridiculous things than this, Ria."
    play ctc_sfx "<silence 1.0>"
    O annoyed "Tsk...{w=0.5} ...Fine. Then riddle me this." with shakeonce
    O leering2 "How does a soul [t_clue]move around freely[t_cluee] while still being \"alive\"?{nw}"

    menu:
        extend ""
        "\"By floating around.\"":
            YV "Just like any other spirit, he moves [t_clue]through the air[t_cluee], invisible to the naked eye."
            play ctc_sfx "<silence 1.0>"
            C sad "....."
            play ctc_sfx "<silence 1.0>"
            O irritated "....."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            K worried "....."
            YV "...Uh, guys?"
            $ fadein_sideimage = False
            O leering "...Is this some kind of joke to you? How does that explain ANYTHING?" with shakeonce
            YV "W-well, if he's floating around right now, maybe he's waiting for his chance to possess one of us and--" with hpunch
            jump d3a5_gameover
        "\"With spirit channeling.\"":
            YV "Obviously, by spirit channeling. The practice of [t_clue]summoning spirits[t_cluee] to possess one's body."
            O confused "...Where did you learn this?"
            YV "From the attic. I remember reading about people with immense spiritual power capable of calling spirits from the other side."
            YV "Spirit channeling is a technique that allows spirits to temporarily take control of a spirit medium's body."
            YV "Which must mean...this body is actually a spirit medium who stopped channeling the Professor, and is now channeling me."
            YV "Or maybe...! The Professor is the spirit medium, and--" with shakeonce
            O disappointed "[name_player]."
            O "You already declared you're currently inhabiting a soulless shell. Do you want to take that back?"
            $ fadein_sideimage = True
            I "...Ah."
            C thinking "The Professor's a spirit medium...? Oooh, so THAT'S why the door didn't open when he got stabbed a bajillion times."
            $ fadein_sideimage = False
            YV "Urgh... S-sorry, let me redo my arguments from the start. So first of all--" with hpunch
            jump d3a5_gameover
        "\"By getting killed.\"":
            YV shadow "{cps=6}.....{/cps} It must be through the killing game..."
            O surprised "...What?" with shakeonce
            YV default "Think about it. A large man like the Professor was killed with hardly any signs of struggle in the bedroom."
            YV "He must've let himself get killed on purpose.{w=0.5} That...must be how he moves around..."
            YV "The purpose of the killing game is to drive people like us to kill him, and then..." with shakeonce
            YV shadow "He...takes over the body of his murderer..."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            K depressed "....." with shakeonce
            O irritated "...[name_player]. You're trying to get us to suspect each other right now, aren't you...?"
            $ fadein_sideimage = False
            YV "But...that's the only way he could still be alive after his body was killed..."
            C sad "It's certainly a chilling possibility, [name_player], but I don't think that's it."
            C thinking "Remember how there were many instances where the Professor--in your current body--definitely KILLED one of us?"
            C "Why would he do that if his soul can only move when someone else kills {i}him{/i}?"
            YV default "That's... ...It must work either way, then.{w=0.5} He can also move if he kills someone himself..." with hpunch
            C sad "Then why wouldn't he {i}just{/i} do that? Why bother setting up a killing game when killing us himself works fine?"
            YV "I-I..." with shakeonce
            O leering "I knew it... You're trying to trick us right now, aren't you...?"
            YV "Wha-- N-NO, I--" with shakeshort
            jump d3a5_gameover
        "\"By inhabiting a host.\"":
            pass
    YV "...He's in a host. Someone or something is [t_clue]carrying his soul around[t_cluee]."
    C sweatdrop "A host...? You sure you're not just making this up?" with hpunch
    YV "Have you forgotten already? How am I currently possessing this body right now?"
    play ctc_sfx "<silence 1.0>"
    O panicked "...!{w=1.0} ...The [t_clue]wrist shackle[t_cluee]...!" with shakeshort
    $ fadein_sideimage = True
    K afraid "But that's specific to you! How do you know the Professor is doing something similar?" with shakeshort
    scene bg black
    show shackle_green at truecenter:
        zoom 0.75 alpha 0.0
        easein 10.0 zoom 1.0 alpha 1.0
    with dissolvemed
    pause 1.0
    YV "...You guys explained to me earlier that my soul is bound to a wrist shackle."
    $ fadein_sideimage = False
    YV "But just now...{w=1.0}I realized something.{nw}"
    $ show_side_karma = True

    menu:
        extend ""
        "\"There are multiple wrist shackles.\"":
            pass
        "\"There are two souls in this wrist shackle.\"":
            YV "This doesn't contain just {i}my{/i} soul.{w=0.5} [t_clue]Someone else[t_cluee] is in here too."
            O afraid "...What...?" with shakeonce
            C determined "Who else is in there, [name_player]?!" with shakeshort
            YV shadow "{cps=6}.....{/cps} ...The other soul in this shackle with me is...{w=0.5}{nw}"

            menu:
                extend ""
                "The Professor":
                    YV "...The Professor... He's in here..."
                    C serious "....."
                    O irritated "...[name_player]."
                    O annoyed "If you're serious, then isn't that all the more reason we should be throwing that shackle into the Gate?" with shakeonce
                    YV default "Wh-why? He's not...going anywhere with me in here too, tying him down..." with hpunch
                "The daughter of the house":
                    YV "The daughter of the house... The one that passed away..."
                    play ctc_sfx "<silence 1.0>"
                    C injured "...That's..." with shakeonce
                    O shadow "[name_player]... That's low, even for a being from Hell like yourself..." with shakeonce
                    O annoyed "Are you seriously using the tragedy of the daughter's death to lie yourself out of going back?!" with shakeshort
                    YV default "N-no, I... I just feel like she could be...in here..." with hpunch
                "A stranger":
                    YV "It's...a stranger. Someone none of us know..."
                    C surprised "....."
                    O irritated "...So what are you saying, [name_player]? Are you holding that other soul hostage so that we don't send you back to Hell?"
                    YV default "N-no, that's not what I'm doing! I just... I dunno, I feel like there's someone else in here with me..." with hpunch
                "Karma":
                    YV "It's...Karma."
                    C sad "....."
                    K worried "....."
                    O irritated "....."
                    K "Um... I'm right here, y'know..."
            play ctc_sfx sfx_emoteshout
            O shouting "Are you SERIOUSLY joking around at a time like this?!" with shakelong
            $ fadein_sideimage = True
            I "...What the hell am I saying...?! I'm not in Karma's body anymore; how could I possibly be hearing other voices...?!" with shakeonce
            scene bg basement stairway
            show karma tiredblink at mycenter_fadein
            with dissolve
            jump d3a5_gameover
        "\"There are other artifacts like this one.\"":
            YV "This shackle isn't the only object that can host souls."
            O surprised "You're saying...there's another?"
            YV "Yes...{w=0.5} The other artifact is...{nw}"
            menu:
                extend ""
                "Cece's Knife":
                    YV "Cece's knife. She's been basically attached to it this whole time."
                    YV "It's no stretch to say it's been magnifying her...{w=0.5}violent urges."
                    O irritated "....." with shakeonce
                    C sweatdrop "{cps=6}.....{/cps} ...[name_player], this is kinda weird for me to say, but..."
                    C sad "This is just my normal personality. The others can confirm it."
                    YV "They can?"
                    K worried "Yes."
                    O annoyed2 "Yes, she's always like this." with shakeonce
                    $ fadein_sideimage = True
                    I "Okay, I guess that was a bit of a wild guess..."
                "Ria's Choker":
                    YV "Ria's choker. You've been fiddling with it this whole time."
                    O surprised "Th-that's..." with shakeonce
                    K surprised "....."
                    play ctc_sfx sfx_heartbeat_single
                    O embarrassed "Y-you can confirm with either of the others that I've always worn this, even when we first arrived here!" with shakeshort
                    C blink "....."
                    play ctc_sfx sfx_emotesigh
                    K sweatdrop "She, uh...definitely wears it daily, [name_player]. I doubt it got cursed at any point." with hpunch
                    O leering2 "But also... Are you implying that I'm currently being possessed by the Professor?" with shakeonce
                    YV "O-oh, that's right, the Professor... Uh..." with hpunch
                    $ fadein_sideimage = True
                "Karma's Earring":
                    YV "Karma's earring. It must contain a soul inside. Why else would you only have one?"
                    K panicked "....."
                    O disappointed "...[name_player]. It's not unusual for people to wear a single earring."
                    YV "But let's say it {i}did{/i} contain a soul. That would explain why she's now in control of her body instead of me." with shakeonce
                    C sweatdrop "Uh, [name_player], you checked the mirror when you were in her body, right?"
                    C thinking "That earring has always been there. Are you saying you sensed her presence?"
                    YV "...Well, not all the time, but... Um..." with hpunch
                    $ fadein_sideimage = True
                    I "Wait, this is just confusing me. I've definitely gone off-track..."
                    O irritated "I also don't appreciate the implication that Karma's already dead, and is being controlled by her own spirit..." with shakeonce
            I "...What am I doing? I should already know the answer; why am I making guesses like this...?" with shakeonce
            scene bg basement stairway
            show karma tiredblink at mycenter_fadein
            with dissolve
            jump d3a5_gameover
        "\"I must be the Professor.\"":
            $ renpy.music.set_volume(0.0, 3.0, channel="music")
            YV shadow "{cps=6}.....{/cps} ...I must be the Professor..."
            play ctc_sfx "<silence 1.0>"
            K depressed "...What?" with shakeonce
            YV "It makes sense... The way {i}my{/i} soul moves around... It's exactly how the Professor could've avoided detection, avoided death..."
            YV default "I mean, look at me! I still have an open stab wound on my chest! That means I could easily pretend to be..." with shakeonce
            O irritated2 "[name_player]. That doesn't make ANY sense."
            O leering "You were possessing Karma this whole time, remember? Including [t_clue]when the zombie attacked us[t_cluee]."
            play ctc_sfx "<silence 1.0>"
            YV "...! Oh..." with shakeonce
            $ renpy.music.set_volume(1.0, 3.0, channel="music")
            O irritated "If you're actually the Professor, then we'd need a new explanation for that zombie."
            YV "Y-you're right... Then I guess he has to be somewhere else..." with hpunch
            O leering2 "...No.{w=0.5} I don't buy your act, [name_player]."
            O "You clearly don't know what you're talking about, and you're just trying to derail us from sacrificing you."
            YV "Th-that's...! I'm not...!" with shakeshort
            scene bg basement stairway
            show karma tiredblink at mycenter_fadein
            with dissolve
            jump d3a5_gameover
    scene bg black
    show shackle_purple at trueleft
    show shackle_green at trueright
    with custom_flashbulb()
    play sound sfx_emotequestion
    pause 2.0
    $ fadein_sideimage = True
    YV "...I have a lot of reasons to believe there's [t_clue]more than one[t_cluee] of these wrist shackles."
    $ fadein_sideimage = False
    O irritated "Don't you dare say it's because shackles usually come in a pair..."
    YV "No...{w=0.5} Thinking back now, I've seen something that looks just like a wrist shackle at least [t_clue]two times[t_cluee] before." with shakeonce
    YV "Ria. Remember [name_dog]'s collar?"
    O confused "...His collar...?{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend panicked " ...AH!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    window auto hide
    play sound sfx_flashback
    scene bg lounge at grayscale_on
    show dog_raw at mycenter, grayscale_on
    with custom_flashbulblong()
    pause 3.0
    YV "Exactly. It looked a lot like a wrist shackle, didn't it?"
    $ fadein_sideimage = False
    YV "And Cece. Remember when you fought the Professor while he was pretending to be a zombie?"
    C thinking "Huh?{w=0.5} Uh... That's kind of a blur now..."
    YV "No worries, because I remember."
    $ fadein_sideimage = True
    window auto hide
    scene bg basement nocorpse at grayscale_on
    show villain_raw attacking at mycenter, grayscale_on
    with dissolvemed
    pause 2.0
    YV "On his [t_clue]left wrist[t_cluee], there was something like a metal shackle wrapped around it."
    $ fadein_sideimage = False
    C surprised "...!!{w=0.5} ...Y-you mean..." with shakeonce
    YV "Yes.{w=0.5} I think just like me, the Professor's soul is also [t_clue]bound to a wrist shackle[t_cluee]."
    YV "And all the times any of us saw [name_dog] or the Professor moving, well..."
    $ fadein_sideimage = True
    window auto hide
    scene bg black with custom_flashbulblong()
    show dog_raw at myleft, grayscale_on
    show villain_raw at myright, grayscale_on
    with dissolveslow
    pause 3.0
    YV shadow "They were moving because of his shackle. He was possessing them just like I was with Karma."
    $ fadein_sideimage = False
    K afraid "W-wait...!! Wh-which one was he, the dog or the corpse?!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    YV "He was...{w=1.0}[t_clue]both of them[t_cluee]."
    K shocked "...Wh-what...? Isn't that...impossible...?"
    YV default "No, it's possible. After all..."
    play ctc_sfx "<silence 1.0>"
    YV "None of us have ever seen both [name_dog] and the zombie in the [t_clue]same place at the same time[t_cluee]." with shakeonce
    play ctc_sfx "<silence 1.0>"
    O depressed "{cps=6}.....{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    K depressed "{cps=6}.......{/cps}"
    O afraid "Wait..." with shakeonce
    O horrified "But when we found [name_dog]'s body..." with shakeshort
    $ fadein_sideimage = True
    window auto hide
    scene cg deaddog at grayscale_on
    with dissolvemed
    pause 3.0
    O horrified "A-and then, the Professor's body in the bedroom..." with shakeonce
    window auto hide
    scene bg bedroom corpse pac at grayscale_on
    with dissolvemed
    pause 3.0
    O horrified "There was nothing! No collar, and no wrist shackle!" with shakeshort
    $ fadein_sideimage = False
    YV shadow "{cps=12}...Exactly.{/cps}{w=0.5} And there's only one explanation for that.{nw}"

    menu:
        extend ""
        "\"It moved to find a new host.\"":
            YV default "After each one died, the wrist shackle pulled itself free to go search for a new host."
            YV "That's why we don't know where it is. And thus, we don't know where the Professor is..."
            play ctc_sfx "<silence 1.0>"
            K pained2 "No..." with shakeonce
            play ctc_sfx "<silence 1.0>"
            O depressed "{cps=6}.....{/cps}"
            C sad "I hate to interrupt a moment of collective terror, but..."
            play ctc_sfx sfx_emotequestion
            C thinking "Ria, when you found the Professor's body in the bedroom, did you have to [t_clue]open the door[t_cluee] to see inside?"
            play ctc_sfx "<silence 1.0>"
            O panicked "...!!{w=0.5} Y-yes, I did...!" with shakeonce
            $ fadein_sideimage = True
            I "WHAT?!" with shakeshort
            C smug "Just like I thought."
            $ fadein_sideimage = False
            C blink "[name_player], let's say your wild theory about an animated wrist shackle is true."
            C "How do you propose it managed to open and close a door without being discovered?"
            YV shadow "....." with hpunch
            K panicked "Y-you're right! That doesn't make any sense!" with shakeonce
            C smile "Also... You're in a shackle too, right? Give your idea a try!"
            C grin "Pull yourself off the corpse and try to jump onto one of us. C'mon, don't be shy~"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            I "AAAARGHHH!! I... I was so close...!" with shakeshort
            scene bg basement stairway
            show karma tiredblink at mycenter_fadein
            with dissolve
            jump d3a5_gameover
        "\"Someone picked it up.\"":
            pass
        "\"It dissolved away.\"":
            YV "It must have dissolved away after its host died..."
            YV "That means... The Professor is gone now..."
            K panicked "Wh-wha...?! Then...it's over?!" with shakeshort
            O confused "...[name_player]. That can't be how it works."
            O irritated "We found [name_dog]'s dead body first, then the Professor's body shortly after."
            O leering2 "If it dissolves after its host dies, then how was the Professor [t_clue]able to move[t_cluee] after we found [name_dog]'s body?" with shakeonce
            YV default "Th-that's... I-I..." with shakeonce
            C sad "Come on, [name_player]... You almost had something there..."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            I "No... I was so close...!{w=0.5} The answer should be SO obvious now...!" with shakeshort
            scene bg basement stairway
            show karma tiredblink at mycenter_fadein
            with dissolve
            jump d3a5_gameover
    scene bg black with dissolveslow
    pause 1.0
    scene bg basement stairway
    show karma shadow at mycenter_fadein
    with dissolveslow
    pause 1.0
    $ show_side_karma = False
    $ fadein_sideimage = True
    YV shadow "Someone took the Professor's wrist shackle.{cps=1} {/cps}And that person...still has it."
    stop music fadeout 3.0
    play ctc_sfx "<silence 1.0>"
    K "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    C shadow "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    O shadow "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    I "{cps=6}.....{/cps} ...This is it.{w=0.5} This explains why something's been [t_clue]feeling so off[t_cluee] for the past while."
    I "[name_player_true], don't mess up here..." with hpunch
    play ctc_sfx "<silence 1.0>"
    YV "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    YV "The one who took the Professor's wrist shackle was..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True

    $ show_choicegrand = True
    $ mute_choice = True
    menu:
        "Karma":
            play sound sfx_choicegrand
            YV default "...Karma. It was you."
            play ctc_sfx "<silence 1.0>"
            K depressed "{cps=6}.....{/cps}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            C blink "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = False
            O irritated "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            YV "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            I "{cps=6}.....{/cps} ...I...messed up..."
            play ctc_sfx "<silence 1.0>"
            I "Karma couldn't possibly be the one. She was being possessed by me up till now..."
            $ mute_choice = False
            jump d3a5_gameover
        "Cecilia":
            $ show_side_cecilia = False
            $ show_side_oriana = False
            $ show_choicegrand = False
            $ mute_choice = False
            stop music
            scene bg white with custom_flashbulblong()
            call save_file_name_update (3, "d3a6")
            scene bg black
            show cecilia at mycenter_fadein
            with dissolveslow
            pause 2.0
            $ fadein_sideimage = True
            YV shadow "...Cece.{cps=1} {/cps}It was you."
            $ fadein_sideimage = False
            play ctc_sfx "<silence 1.0>"
            YV default "You took the wrist shackle containing the Professor's soul."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            window auto hide
            show bg basement stairway with dissolveslow
            C "{cps=6}..........{/cps}{w=1.0}{nw}"
            play ctc_sfx sfx_emotequestion
            extend surprised " ...Huh?"
            C "Why would I do that?"
            jump d3a6
        "Oriana":
            play sound sfx_choicegrand
            YV default "...Ria. It was you."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = False
            O depressed "{cps=6}.....{/cps}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            C sad "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            K panicked "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            K "...Uh... Um, [name_player]?"
            K leering "You...look like you regret what you just said. Did you...not think your answer through...?"
            YV shadow "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            I "{cps=6}.....{/cps} ...I...messed up..."
            play ctc_sfx "<silence 1.0>"
            I "Ria's...been [t_clue]acting the same as always[t_cluee]... She couldn't possibly be..." with hpunch
            $ mute_choice = False
            jump d3a5_gameover

label d3a5_gameover:
    $ show_choicegrand = False
    stop music fadeout 3.0
    $ show_side_karma = False
    $ fadein_sideimage = True
    K tiredblink "[name_player]. I'm sorry, but..."
    K "While I was hoping you would voluntarily sacrifice yourself for our sakes...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend leering "it was [t_clue]not a request you could refuse[t_cluee]." with shakeshort
    K sad "...I...{w=0.5} I won't forget you, though.{w=0.5} Please...{w=0.5}rest in peace."
    YV default "N-no, wait, I--" with shakeshort
    $ _last_say_who = "K"
    play ctc_sfx sfx_whoosh
    show karma crying with custom_flashquick()
    scene bg black
    with soulout
    pause 0.5
    play sound sfx_flameburst
    play loop_sfx sfx_flameloop
    scene bg flamewall with custom_flashbulb()
    pause 5.0
    I "...As my consciousness fell into an inescapable darkness,{w=1.0} I bitterly lamented the failure in my deduction..." with shakeshort
    play ctc_sfx "<silence 1.0>"
    I "For at that moment, I realized it.{w=1.0} By letting them leave like that..."
    play ctc_sfx "<silence 1.0>"
    I "The three of them, and perhaps even the whole world..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}...were {color=#ff0000}doomed{/color}.{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide dissolveslow
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show pac_assistant_shadow at truecenter:
        zoom 1.75 alpha 0.4
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#ff0000}ПЛОХАЯ КОНЦОВКА{/color}{/size}\nВЫ ПРОИГРАЛИ{/font}"
    with dissolve
    achieve YOU_LOSE
    pause 2.0
    $ _skipping = True
    pause 3.0
    hide pac_assistant_shadow
    hide text
    with dissolveslow
    pause 2.0
    menu:
        "TRY AGAIN":
            stop loop_sfx fadeout 3.0
            scene bg black with dissolveslow
            jump d3a5

label d3a6:
    YV "The reason you took the wrist shackle is...{nw}"
    $ fadein_sideimage = False

    menu:
        extend ""
        "\"You love occult stuff.\"":
            YV "...You love the occult. Obviously, you wanted it as a..."
            $ fadein_sideimage = True
            I "Wait, that's stupid. Come on, don't joke around now!" with hpunch
            YV "...No, the REAL reason..."
            $ fadein_sideimage = False
            jump d3a6
        "\"You picked it up by mistake.\"":
            YV "...You found it on the floor, and..."
            $ fadein_sideimage = True
            I "...Wait, why would she do that? She was there when Karma took my shackle. She would've known what would happen..."
            I "Then...that means..." with shakeonce
            YV "...No, the REAL reason..."
            $ fadein_sideimage = False
            jump d3a6
        "\"You were forced to take it.\"":
            YV "...You didn't want to take it. It was forced onto you."
            play ctc_sfx "<silence 1.0>"
            YV "...Isn't that right...{w=1.0}{nw}"
            play ctc_sfx sfx_heartbeat_single
            extend " \"[t_clue]Professor[t_cluee]\"?" with shakeshort
            $ fadein_sideimage = True
    C sad "...No, seriously. I have no idea what you're talking about."
    $ show_side_karma = True
    $ show_side_oriana = True
    K shocked "...[name_player]? What are you doing...?"
    $ fadein_sideimage = False
    YV "Then let me ask you just one question.{cps=1} {/cps}And if you answer correctly, I'll back off."
    O afraid "....."
    YV "About 10 years ago...{cps=1} {/cps}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend "[t_clue]What did Serena kill?[t_clue]" with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    C surprised "{cps=6}.....{/cps} ...Who?{w=1.0} \"Serena\"?"
    play ctc_sfx "<silence 1.0>"
    C sweatdrop "Sorry, I guess it's been too long that I don't remember that name..."
    play ctc_sfx "<silence 1.0>"
    YV "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    play music bgm_tragedy fadein 2.0
    $ fadein_sideimage = False
    YV shadow "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    show bg basement stairway:
        matrixcolor BrightnessMatrix(0.0)
        linear 5.0 matrixcolor BrightnessMatrix(-1.0)
    C default "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    O "...[name_player]. Are you saying...?"
    $ fadein_sideimage = False
    YV "It all makes sense now.{w=0.5} Ever since we found [name_dog]'s body, you've been acting strange." with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    scene bg hallway at grayscale_on
    show cecilia thinking at mycenter, grayscale_on
    with custom_flashbulblong()
    $ grayscale_sideimage = True
    Y angry "We can't go back to that! We're so close to the truth! Once we find the true mastermind--" with shakeonce
    C sad "But there was no such person in the basement, now was there?"
    Y shocked "That's..."
    C smug "Unless you want to claim that mindless, rotting zombie is somehow the cunning mastermind behind all this."
    Y pained "B-but he might be exactly that! Maybe he's pretending to be mindless? Or he lost his sanity just before he attacked..." with shakeshort
    C thinking "Either way, what do you propose we do, then?"
    C sad "It's not like we have any clue as to where that zombie went."
    C determined "And as you recall, we were given [t_clue]20 hours[t_cluee]. Time is running out."
    Y shocked "Cece... What are you doing?"
    $ fadein_sideimage = False
    Y "We're supposed to be a team now, right?"
    play ctc_sfx sfx_heartbeat_single
    Y "Why are you trying to [t_clue]restart the killing game[t_cluee]?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    $ grayscale_sideimage = False
    scene bg black with dissolveslow
    pause 1.0
    YV shadow "{cps=6}.....{/cps} ...It was weird.{cps=1} {/cps}You were so calm, so cold..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    YV "You said [name_dog] was killed somewhere else, then left in the hallway as a warning...with a lot of confidence."
    play ctc_sfx "<silence 1.0>"
    YV "Almost as though...that was your plan. You wanted to use [name_dog]'s death to [t_clue]pressure me[t_cluee]..." with shakeonce
    $ show_side_cecilia = True
    C sad "That's kinda flimsy reasoning, [name_player]."
    C thinking "I found [name_dog]'s body first. So naturally, I had the most time to think about what we could do next."
    YV "No, that's only the first thing I noticed. Next, there was the time we found the body in the bedroom."
    play ctc_sfx "<silence 1.0>"
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene bg bedroom corpse at grayscale_on
    show oriana irritated at myleft_fadein, grayscale_on
    show cecilia thinking at myright_fadein, grayscale_on
    with custom_flashbulblong()
    $ grayscale_sideimage = True
    $ show_side_oriana = False
    O annoyed "...Tsk. No signal. Cecilia, how about you?" with shakeonce
    C surprised "Huh? O-oh, I, uh..."
    O leering2 "What is it? ...Looks like you don't have a signal either."
    C sweatdrop "Yeah, I guess we'll have to try again later..."
    I "....."
    C surprised "Huh? What's wrong, [name_player]? You're staring at me."
    Y sad "O-oh. Sorry, it's nothing..."
    C thinking "...?"
    play ctc_sfx "<silence 1.0>"
    $ _last_say_who = None
    $ show_side_oriana = True
    $ grayscale_sideimage = False
    scene bg black with dissolveslow
    pause 1.0
    YV shadow "{cps=6}.....{/cps} ...You were...weirdly confused and unexcited.{cps=1} {/cps}Almost as though..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    YV "You didn't [t_clue]recognize your own phone[t_cluee]." with shakeonce
    $ show_side_cecilia = True
    C sad "...Huh? Is that really such a weird thing to do?"
    C thinking "It's just a phone, right? Plus, without any signal, it's not useful for anything..."
    play ctc_sfx "<silence 1.0>"
    K depressed "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    O afraid "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    YV "{cps=6}.....{/cps}"
    C sweatdrop "...Uh... Wh-what's with you all?" with shakeonce
    O "{cps=12}Cecilia, you...{/cps}"
    play ctc_sfx "<silence 1.0>"
    K "...You love your phone.{w=1.0} You play all those games...that require you to open them daily."
    play ctc_sfx "<silence 1.0>"
    O "Why didn't you...try to play your porcupine game right away...?"
    play ctc_sfx "<silence 1.0>" 
    C surprised "{cps=6}.......{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>" 
    $ fadein_sideimage = True
    I "{cps=6}.....{/cps} ...I knew it..."
    play ctc_sfx "<silence 1.0>" 
    YV default "Finally... We have what you said just moments earlier..."
    play ctc_sfx "<silence 1.0>"
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene bg basement stairway at grayscale_on
    show cecilia at mycenter, grayscale_on
    with custom_flashbulblong()
    $ grayscale_sideimage = True
    C thinking "[name_player], do you remember when you jumped through the basement hatch, and into the underground passage?"
    YV "...Yeah...?"
    play ctc_sfx sfx_emotequestion
    C grin "That hatch is a [t_clue]Gate to Hell[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    YV "Wh-what?!" with shakeonce
    C thinking "To summarize the important details, it's a place where the boundary between the living and dead is very thin."
    C "Living people like us can't interact with it, but a spirit like you, well..."
    C blink "You would get burned to death because that's the process of the Gate [t_clue]pulling you back to where you belong[t_cluee]."
    YV shadow "..... That's..." with shakeonce
    C thinking "So in other words, if we cast the shackle harbouring you into the fires of the Gate from whence you came..."
    C smug "It's effectively the same as [t_clue]killing you[t_cluee]."
    C blush "And if you \"die\" like that, the condition for the front door would be met..."
    play ctc_sfx "<silence 1.0>"
    YV "...And all three of you can escape..."
    play ctc_sfx "<silence 1.0>"
    $ grayscale_sideimage = False
    scene bg black with dissolveslow
    pause 1.0
    YV shadow "{cps=6}.....{/cps} ...How...?"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    YV "How do you know that hatch is a Gate to Hell?!{w=1.0} How do you know my burning to death is equivalent to me \"returning to Hell\"?!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    YV "How do you know that doing that will meet the \"condition\" of the front door?!{w=1.0}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    extend default " HOW DO YOU KNOW SO MUCH?!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    K afraid "{cps=6}.....{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O horrified "{cps=6}.....{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ show_side_cecilia = True
    C sad "{cps=6}.....{/cps} ...You're really keen on making me into some kind of [t_clue]demon[t_cluee] here..."
    play ctc_sfx "<silence 1.0>"
    YV shadow "...No. I'm not. Cece is..." with shakeonce
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    play ctc_sfx "<silence 1.0>"
    scene cg cece hearttoheart at grayscale_on
    with custom_flashbulblong()
    pause 1.0
    scene cg cece hearttoheart2 at grayscale_on:
        xalign 0.5 yalign 0.0 zoom 1.1
        easein 10.0 zoom 1.3
    with dissolve
    YV shadow "{cps=6}...Cece...{/cps}is no demon."
    $ fadein_sideimage = False
    YV "She thinks and acts {i}really{/i} differently from average girls, but...{w=1.0}she's as [t_clue]human[t_cluee] as any of them."
    YV "She protected us from getting attacked...{w=0.5} She watched over us, giving us encouragement when we needed it..." with shakeonce
    YV "She...{w=0.5}[t_clue]wants ALL of us[t_cluee] to escape safely..." with shakeonce
    YV "{cps=24}...She would never try to restart the killing game the way you did...{/cps}{w=2.0}{nw}"
    stop music
    play ctc_sfx sfx_heartbeat_single
    show bg black with custom_flashquick()
    extend default " \"[t_clue]Professor[t_cluee]\"." with shakeshort
    play ctc_sfx "<silence 1.0>"
    window auto hide
    $ fadein_sideimage = True
    pause 2.0
    scene bg basement stairway
    show cecilia at mycenter_fadein
    with dissolveslow
    pause 2.0
    C "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    show cecilia blink at mycenter:
        alpha 1.0
    C "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    C "{cps=6}...............{/cps}{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    $ name_cecilia = _("{color=#cc00bb}Cece...?{/color}")
    extend shadow " ...Heh." with shakeonce
    play ctc_sfx "<silence 1.0>"
    C "{cps=6}Hehehe...{/cps}" with shakeonce
    K depressed "...Cece...?"
    $ fadein_sideimage = False
    O leering2 "Karma, take a step back." with hpunch
    $ fadein_sideimage = True
    C "I'm impressed, [name_player].{w=1.0} I wonder if you worked as a [t_clue]detective[t_cluee] while you were alive."
    play ctc_sfx "<silence 1.0>"
    YV shadow "{cps=6}.....{/cps}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    YV "...So it's true, then."
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    C "Yes, it is as you surmised.{w=0.5} There's no point in denying it anymore..."
    play ctc_sfx "<silence 1.0>"
    window auto hide
    play sound sfx_introambiance_sequence1
    show bg black with dissolveslow
    pause 3.0
    with shakeonce
    pause 2.0
    show cecilia shadow:
        ypos 1.05
        linear 0.9 ypos 1.15
        linear 0.6 ypos 1.20
    pause 2.0
    play sound2 sfx_clothrustle volume 0.7
    with shakeshort
    pause 1.0
    with shakeonce
    pause 1.0
    $ ctc_timer = 0
    show cecilia possessed blink:
        ypos 1.20
    with dissolvemed
    with shakeonce
    show cecilia possessed blink:
        ypos 1.20
        easein 1.5 ypos 1.05
    pause 2.0
    stop sound fadeout 2.0
    pause 3.0
    play music bgm_criminal
    $ show_music_info_timer = music_info_pop_out_time()
    show bg basement stairway:
        matrixcolor InvertMatrix(1.0)
    show cecilia possessed at mycenter:
        zoom 1.05
        easein 0.3 zoom 1.0
    show cecilia_raw possessed:
        xalign 0.5 yanchor 0.5 ypos 0.65
        zoom 1.5 alpha 1.0
        easein 2.0 zoom 2.0 alpha 0.0
    with shakeshort
    pause 1.0
    show bg basement stairway:
        matrixcolor InvertMatrix(0.0)
    with dissolveslow
    pause 2.0
    $ name_cecilia = _("{color=#cc00bb}The Professor{/color}")
    C "...Good evening."
    C "I am the [t_clue]Professor[t_cluee].{w=0.5} Or more specifically, the spirit of the Professor."
    play ctc_sfx sfx_chainrattle
    C possessed grin "Bound to a wrist shackle much like yourself,{w=0.5} and currently overwriting the consciousness of this girl named \"Cecilia\"." with shakeonce
    K shocked "This...isn't an act, is it...?"
    $ fadein_sideimage = False
    YV default "Why are you in Cecilia's body?! What's your plan right now?!" with shakeshort
    $ fadein_sideimage = True
    C possessed thinking "\"Why\", you ask...? Hmm..."
    C possessed blink "I suppose considering what you all have been through, I can disclose some of my motivations."
    play ctc_sfx sfx_emotequestion
    C possessed "My goal is to [t_clue]escape this house[t_cluee]."
    YV "Escape... B-but isn't this {i}your{/i} house?" with shakeonce
    C possessed thinking "It is indeed, but due to the black magic I utilized, it's become something of a [t_clue]prison[t_cluee] for me."
    C possessed "To summarize quickly, the only means of me escaping this place is to [t_clue]offer souls[t_cluee] to the hatch. The Gate to {color=#ff0000}Hell{/color}."
    play ctc_sfx "<silence 1.0>"
    O depressed "Offer...souls..." with shakeonce
    $ fadein_sideimage = False
    K afraid "...That's why...?! That's why you said you couldn't spare our lives?!" with shakeshort
    $ fadein_sideimage = True
    C possessed blink "To clarify, I said I couldn't spare ALL of your lives.{w=0.5} This is because after decades of collection..."
    play ctc_sfx "<silence 1.0>"
    C possessed grin "I now need only one more sacrifice.{w=0.5} [t_clue]One last person[t_cluee] to die in my house." with shakeonce
    YV "And that's why...you started a killing game..." with shakeonce
    C possessed "It's certainly a cleaner way to obtain what I need, wouldn't you say?"
    C possessed blink "I detest cutting down people, especially women and children..."
    play ctc_sfx "<silence 1.0>"
    K depressed "....." with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    O horrified "....." with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    C possessed thinking "...You all seem confused. Perhaps my explanations were lacking due to their brevity?"
    C possessed "Very well, how about this?{w=1.0} In honour of your undeterred efforts and expert deductions..."
    play ctc_sfx sfx_emotequestion
    C "I will answer any [t_clue]3 questions[t_cluee] you may have."
    YV "Questions...?" with shakeonce
    C possessed grin "We will soon be approaching the {color=#ff0000}ending{/color} of this whole ordeal.{w=1.0} I wouldn't mind giving everyone a sense of closure."
    I "...The ending...?"
    C possessed blink "The others still appear stunned, so [name_player]... You should take the reins for this as well."
    $ d3a6_questions_remaining = 3
    $ d3a6_questioning_clue1 = False
    $ d3a6_questioning_clue2 = False
    $ d3a6_questioning_clue3 = False
    $ d3a6_questioning_clue4 = False
    $ d3a6_questioning_clue5 = False
    $ d3a6_questioning_clue6 = False
    $ d3a6_questioning_clue7 = False

label d3a6_questioning:
    C possessed "Go ahead and ask me anything you'd like me to explain."
    menu:
        "\"Why did you take over Cece's body?\"" if not d3a6_questioning_clue1:
            call d3a6_question1
        "[u_check]\"Why did you take over Cece's body?\"" if d3a6_questioning_clue1:
            call d3a6_question1

        "\"Are you the father of the house?\"" if not d3a6_questioning_clue2:
            call d3a6_question2
        "[u_check]\"Are you the father of the house?\"" if d3a6_questioning_clue2:
            call d3a6_question2

        "\"What were you doing as the dog?\"" if not d3a6_questioning_clue3:
            call d3a6_question3
        "[u_check]\"What were you doing as the dog?\"" if d3a6_questioning_clue3:
            call d3a6_question3

        "\"Is this house really the Black Magic Mansion?\"" if not d3a6_questioning_clue4:
            call d3a6_question4
        "[u_check]\"Is this house really the Black Magic Mansion?\"" if d3a6_questioning_clue4:
            call d3a6_question4

        "\"Do you know who I am?\"" if not d3a6_questioning_clue5:
            call d3a6_question5
        "[u_check]\"Do you know who I am?\"" if d3a6_questioning_clue5:
            call d3a6_question5

        "\"How come nobody noticed my wrist shackle?\"" if not d3a6_questioning_clue6:
            call d3a6_question6
        "[u_check]\"How come nobody noticed my wrist shackle?\"" if d3a6_questioning_clue6:
            call d3a6_question6

        "\"Why is Karma able to rewind time?\"" if not d3a6_questioning_clue7:
            call d3a6_question7
        "[u_check]\"Why is Karma able to rewind time?\"" if d3a6_questioning_clue7:
            call d3a6_question7
        "[t_clue]\"That's enough Q and A.\"[t_cluee]":

            YV "I have nothing more to say to you..."
            play ctc_sfx sfx_emoteshout
            $ fadein_sideimage = False
            YV default "Get out of Cece's body right now!" with shakeshort
            $ fadein_sideimage = True
            C possessed surprised "Oh? You wish to cut this short?"
            play ctc_sfx "<silence 1.0>"
            K shocked "....."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = False
            O injured "....."
            $ fadein_sideimage = True
            C possessed blink "...Very well. It appears that each of you are satisfied with your current levels of knowledge."
            jump d3a6_chase

    $ d3a6_questions_remaining = d3a6_questions_remaining - 1
    if d3a6_questions_remaining > 1:
        C possessed "You may ask me [d3a6_questions_remaining] more questions."
        jump d3a6_questioning
    elif d3a6_questions_remaining == 1:
        C possessed "You may ask me one [t_clue]final question[t_cluee]."
        jump d3a6_questioning
    else:
        C possessed blink "...That was question number three.{w=0.5} Well then.{w=0.5} That's all the time I'm willing to offer you for questioning."
        jump d3a6_chase

label d3a6_question1:
    YV default "Why did you take over Cece's body?! In fact, how did you even do that?!" with shakeshort
    if d3a6_questioning_clue1:
        C possessed blink "...Hm. You've asked this question already. Very well, like any good instructor, I will repeat myself."
    C possessed blink "Possessing this girl's body was the first step of my newest [t_clue]plan[t_cluee]."
    K shocked "Your...{i}newest{/i} plan...?"
    C possessed thinking "After my surprise attack in the basement failed, and you locked yourselves away in my library..."
    C possessed "I knew that it was only a matter of time before you learned the truth of this house. About [name_player] and myself."
    C possessed blink "That's why I had to ensure the original plan of having [name_player] choose one of you to die would continue."
    I "....." with shakeonce
    C "I had to do something shocking to divert your attention away from \"solving the mysteries\", and refocus it to the killing game."
    O afraid "...That's why...you left [name_dog]'s body in the hallway..." with hpunch
    C "Correct. But I knew that wouldn't be enough. After all, there's the possibility of doubt when a dog's death doesn't open the door."
    C possessed "That's why I had to use a human body. And the only one that could convince you to turn on each other..."
    play ctc_sfx sfx_heartbeat_single
    C possessed grin "...was my own." with shakeonce
    play ctc_sfx "<silence 1.0>"
    O injured "....." with shakeshort
    C "It worked brilliantly. You convinced yourselves that my body was \"alive\". That killing me would open the door."
    C possessed "And when you found my corpse in the bedroom, and the front door still shut tight..."
    C possessed blink "...The rest fell into place. You were all ready for [name_player] to choose someone to die. Accepted it as the [t_clue]only option[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    C possessed "And even if you had chosen to kill Cecilia... [t_clue]{i}I{/i} would still live on[t_cluee], take over her corpse, and leave through the open door behind you." with shakeonce
    YV shadow "Th-that's..." with shakeonce
    C possessed thinking "But of course, that didn't work... [name_player] refused to kill anyone yet again."
    C possessed "So once again, I had to improvise. Bring more of the truth to light. Incorporate Carol-Maria's story into the plan."
    play ctc_sfx "<silence 1.0>"
    K depressed "....."
    C "And you, [name_player]... You were supposed to willingly sacrifice yourself."
    YV "....."
    C possessed blink "You continually defy my expectations, [name_player]. So now, there is only one [t_clue]final option[t_cluee] left to me..."
    C "....."
    $ d3a6_questioning_clue1 = True
    return
label d3a6_question2:
    YV default "This is your house... So that means... You really {i}are{/i} the father from the lounge photos, aren't you?" with shakeonce
    if d3a6_questioning_clue2:
        C possessed blink "...Hm. You've asked this question already. Very well, like any good instructor, I will repeat myself."
    C possessed "That is correct. Decades ago, I lived in this very house with my family.{w=1.0} ...Before they left me one by one."
    O injured "So... {i}You're{/i} the one from the letter..." with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    O "You...beat your son..." with shakeonce
    $ fadein_sideimage = True
    C possessed blink "{cps=6}.....{/cps} ...I do not take pride in that fact, but yes, it is true."
    O shouting "How could you do that?! After everything you've done for your family up until..." with shakeshort
    C "You speak out of place, child. There were many circumstances plaguing our family during that time."
    C "For instance, my son... He...{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend "[t_clue]forgot his sin[t_cluee]... What he'd done to our family..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    O depressed "{cps=9}...You mean...{/cps}"
    C possessed "But that's all in the past now. My family [t_clue]no longer matters to me[t_cluee]."
    C "All I desire now is my freedom..."
    I "....."
    $ d3a6_questioning_clue2 = True
    return
label d3a6_question3:
    YV default "...Why did you need to possess [name_dog]'s body? Isn't using your own body more convenient?"
    if d3a6_questioning_clue3:
        C possessed blink "...Hm. You've asked this question already. Very well, like any good instructor, I will repeat myself."
    C possessed "Naturally, I would use the dog's body in order to [t_clue]spy on your activities[t_cluee]."
    C possessed grin "Not only is it small and light on its feet, but if any of you spotted me, I was nothing more than a harmless pet."
    play ctc_sfx sfx_emotesigh
    O panicked "...So... A-all those times I..." with hpunch
    C possessed blink "Yes, that was me. But why speak of such embarrassing things right now?"

    if investigated_bathroom:
        YV "W-wait, but what about the time in the bathroom? When you would stare at me, and then run away?" with hpunch
        C possessed thinking "...I do not recall this. Is this from a different future you have experienced?"
        YV "O-oh, that's right... It never happened this time around..." with hpunch
        C "....."
        C possessed blink "...But tell me something, [name_player]."
        play ctc_sfx sfx_emotequestion
        C possessed "While chasing the dog around, did any [t_clue]memories[t_cluee] come to mind?"
        YV "...No? I don't think so..."
        C possessed blink "{cps=6}.....{/cps} ...I see."
        I "...?"

    C possessed "I'm sure we have more important matters to get to."
    $ d3a6_questioning_clue3 = True
    return
label d3a6_question4:
    YV default "This house... Is this the Black Magic Mansion the Occult Club was looking for?"
    if d3a6_questioning_clue4:
        C possessed blink "...Hm. You've asked this question already. Very well, like any good instructor, I will repeat myself."
    C possessed thinking "I was unaware my home had received such a...clever moniker."
    C possessed "So naturally, I am not familiar with the legend. Perhaps you could enlighten me on it before I answer?"
    YV "...Uh..."
    I "...Cece's not exactly {i}here{/i} right now..." with hpunch
    YV "Karma? Could you explain it?"
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotesigh
    K worried "I'm...not as knowledgeable about it as Cece is, but I'll try." with hpunch
    K tired "Basically, the Black Magic Mansion is a house that got haunted around the time the family living in it went missing."
    K tiredblink "The neighbours at the time said they heard strange sounds coming from the house, and made a lot of attempts to check it out."
    K sad "But...a lot of them went missing afterwards...or were mysteriously found dead around the house."
    K "This scared everyone so much, the neighbourhood itself was abandoned."
    K tired "And since then, no one's dared to approach the house for years...{w=1.0} Until now, of course."
    $ fadein_sideimage = True
    C possessed blink "{cps=6}.....{/cps} ...I see. So that's the outside world's understanding of it."
    YV "So is it true...?"
    C possessed thinking "As I have said before, I have been [t_clue]collecting souls[t_cluee] to feed the Gate for decades now."
    C possessed "The process is simple. First, living humans must approach the entrance of my house."
    play ctc_sfx sfx_heartbeat_single
    C "Doing so will immediately warp them here: a [t_clue]closed-off space[t_cluee] between the realms of the living and the dead." with shakeonce
    YV "W-wait, what?!" with shakeshort
    C possessed surprised "Oh? Have you not realized it yet?"
    C possessed "What did you think the [t_clue]fog[t_cluee] outside was?"
    play ctc_sfx "<silence 1.0>"
    K depressed "The fog..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    O horrified "W-wait, so the reason the windows wouldn't break...?!" with shakeshort
    $ fadein_sideimage = True
    C possessed blink "Those aren't windows. Those are the [t_clue]edges[t_cluee] of this world."
    play ctc_sfx "<silence 1.0>"
    C possessed "There is {color=#ff0000}nothing{/color} outside the house."
    play ctc_sfx "<silence 1.0>"
    YV "No..." with shakeonce
    play ctc_sfx sfx_knifebrandish
    C possessed grin knife "As such, the humans warped here are easy prey for me." with shakeonce
    C "All I have to do is have them [t_clue]die[t_cluee] somehow, and the Gate will [t_clue]absorb their souls[t_cluee]."
    O horrified "...Then... You really DID kill all those people...?!" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    O "And even...sent their souls to {color=#ff0000}Hell{/color}?!" with shakeshort
    $ fadein_sideimage = True
    C possessed blink "I will do {i}anything{/i} to achieve my objectives. ...My humanity died decades ago..."
    I "....."
    $ d3a6_questioning_clue4 = True
    return
label d3a6_question5:
    YV shadow "...You had my shackle... You're the one who gave it to Karma..."
    $ fadein_sideimage = False
    YV "Does that mean...you know who I am? [t_clue]{i}What{/i} I am[t_cluee]?" with shakeonce
    $ fadein_sideimage = True
    if d3a6_questioning_clue5:
        C possessed blink "...Hm. You've asked this question already. Very well, like any good instructor, I will repeat myself."
    C possessed "My answer to your question is the same as I have explained to Carol-Maria."
    C "You are [t_clue]a spirit pulled from Hell[t_cluee]."
    YV "So... I came out of that Gate...?" with shakeonce
    C possessed blink "That is correct. You are the result of one of my most complicated [t_clue]summoning rituals[t_cluee]."
    play ctc_sfx "<silence 1.0>"
    C possessed "No one should be able to escape {color=#ff0000}Hell{/color}.{w=0.5} But you are proof that it is possible." with shakeonce
    YV default "But why did you summon me?! What were you trying to accomplish?!" with shakeshort
    C possessed blink "{cps=6}.....{/cps} ...That doesn't matter anymore."
    YV "Wh-what...?"
    C "When I first awakened you...you had none of your memories."
    C "Your soul naturally has no physical form outside of your shackle. And your voice is based on the body you are possessing."
    C "I don't know your [t_clue]true name[t_cluee], your age, your gender, your personal history...{w=0.5} Nothing, not even a lead to follow."
    play ctc_sfx "<silence 1.0>"
    C possessed "You are, by every definition of the word,{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend " a [t_clue]stranger[t_cluee]." with shakeonce
    play ctc_sfx "<silence 1.0>"
    YV shadow "....."
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    K sad "....."
    $ fadein_sideimage = True
    $ d3a6_questioning_clue5 = True
    return
label d3a6_question6:
    YV default "...There's something that's been bothering me this whole time.{cps=2} {/cps}While I was in Karma's body..."
    $ fadein_sideimage = False
    YV "How did no one--not even ME--notice that I had a large, clunky shackle on my wrist?!" with shakeonce
    $ fadein_sideimage = True
    if d3a6_questioning_clue6:
        C possessed blink "...Hm. You've asked this question already. Very well, like any good instructor, I will repeat myself."
    C possessed "It's quite simple, if you think about it. In all honesty, I wonder if this is even worth using up your questions for."
    YV "B-but the shackle... You've all been saying that I'm possessing the Professor's body with it, but..." with hpunch
    play ctc_sfx sfx_heartbeat_single
    $ fadein_sideimage = False
    YV "[t_clue]I still don't see it![t_cluee] I don't even feel it on my wrist!" with shakeshort
    $ fadein_sideimage = True
    C possessed blink "Let me attempt to explain this swiftly with an analogy."
    C possessed "[name_player]. Have you ever directly looked at your own eyes before?"
    play ctc_sfx "<silence 1.0>"
    play sound sfx_flashback
    scene cg mirror2:
        xalign 0.4 yalign 0.4 zoom 1.3
        easein 6.0 xalign 0.5 yalign 0.5 zoom 1.0
    with custom_flashbulblong()
    pause 1.0
    YV "...Yeah, in the mirror..."
    $ fadein_sideimage = False
    $ show_side_cecilia = True
    C possessed thinking "The mirror shows you a {i}reflection{/i} of your eyes. I'm talking about your actual eyes."
    YV "N-no, of course not. That's impossible." with hpunch
    C possessed "It is a similar system. Because your [t_clue]soul[t_cluee] lives inside the shackle, naturally you would not be able to see yourself."
    C possessed grin "I cannot see my own shackle either. But I know it is there."
    YV "Th-then... Why didn't anyone else...?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O injured "....." with shakeonce
    C possessed blink "...Isn't it obvious?"
    $ fadein_sideimage = True
    I "...!!{w=1.0} Ah..." with shakeshort
    play ctc_sfx "<silence 1.0>"
    $ persistent.unlock_cg_mirror2 = True
    scene cg mirror with dissolveslow
    pause 3.0
    I "They...{w=1.0} They COULD see it, but they [t_clue]kept quiet[t_cluee] about it because of the killing game..."
    C possessed thinking "...Now, if your curiosity is sufficiently satiated..."
    $ show_side_cecilia = False
    scene bg black with dissolvemed
    scene bg basement stairway
    show cecilia possessed at mycenter
    with dissolvemed
    $ d3a6_questioning_clue6 = True
    return
label d3a6_question7:
    YV default "Why is Karma able to rewind time? Is it black magic of some kind?"
    if d3a6_questioning_clue7:
        C possessed blink "...Hm. You've asked this question already. Very well, like any good instructor, I will repeat myself."
    C possessed thinking "...I'm afraid [t_clue]I don't know anything[t_cluee] about Carol-Maria's power."
    play ctc_sfx "<silence 1.0>"
    K afraid "Wh-what?! But...you said it was connected to my consciousness!" with shakeshort
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    K pained "That's why you gave me [name_player]'s wrist shackle! You said it would make sure my power wouldn't--" with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx sfx_emotequestion
    C possessed blink "Naturally, those were all [t_clue]guesses[t_cluee]."
    K shocked "...Wha..." with hpunch
    C possessed thinking "Your ability to rewind time wasn't in any of the black magic materials I've researched."
    C "It is most likely some other form of power that is [t_clue]unique to you[t_cluee]. I do not know where one would even begin to investigate its origin."
    C possessed blink "If I had known such a power existed, then... {cps=6}.....{/cps}"
    I "...?"
    C "...No. I suppose it is far too late now. In any case..."
    C possessed "I promise you that I truly believed giving you [name_player]'s shackle would work."
    C possessed thinking "After all, if the killing game never ends, that would be problematic for myself as well. It would mean [t_clue]I could never leave either[t_cluee]."
    YV "...Right..." with hpunch
    $ d3a6_questioning_clue7 = True
    return

label d3a6_chase:
    stop music fadeout 3.0
    play ctc_sfx "<silence 1.0>"
    C possessed blink "{cps=12}On to the next matter...{/cps}"
    YV default "The...next matter...?"
    C "Naturally, all that's left is...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend possessed "the [t_clue]ending[t_cluee] of this story." with shakeonce
    K shocked "The...ending...?"
    C "Simply put, I believe we should all stick to my current, latest plan. That is..."
    play ctc_sfx "<silence 1.0>"
    show bg black
    C "Tossing [name_player]'s shackle into the Gate to {color=#ff0000}Hell{/color}." with shakeonce
    play ctc_sfx "<silence 1.0>"
    YV "...!!" with shakeshort
    $ fadein_sideimage = False
    K afraid "B-but that's..." with shakeonce
    O shadow "....."
    $ fadein_sideimage = True
    C possessed thinking "No one will complain about a spirit originally from Hell being sent back there, correct?"
    play ctc_sfx "<silence 1.0>"
    C possessed grin "Besides...{w=0.5}it was me who brought you out into this world.{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend " Does that not give me the right to do with you as I please?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    YV shadow "...You..." with shakeonce
    C possessed "Once the deed is done, the four of us will be able to go out the open front door, and return to the world of the living."
    C possessed surprised "Oh, and do not fret; I will return to my original body and set Cecilia free, of course."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.......{/cps}"
    C possessed grin "Now, what say you, fair maidens? Is this not a perfectly reasonable plan?"
    C possessed blink "After all, you were prepared to sacrifice [name_player] in the first place. Has [t_clue]anything changed[t_cluee], really?"
    play ctc_sfx "<silence 1.0>"
    O "{cps=6}.....{/cps}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    K dejected "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    K "{cps=24}I...{w=0.5} If it means it can all end, then...{/cps}"
    play ctc_sfx "<silence 1.0>"
    K "{cps=24}Then I...{w=0.5} I want to...end it... I want to be...free...{/cps}" with shakeonce
    O irritated "Karma."
    K shocked "...!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O annoyed2 "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    K panicked "{cps=6}..........{/cps}{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend leering " ...Okay." with shakeonce
    $ fadein_sideimage = True
    C possessed thinking "Hmm? What are you--"
    play ctc_sfx sfx_whoosh
    show bg basement stairway
    show cecilia possessed surprised with custom_flashquick()
    scene bg black
    with soulout
    pause 1.0
    $ show_side_karma = False
    $ show_side_oriana = False
    $ _last_say_who = None
    window auto hide
    pause 1.0
    scene bg basement at blurred:
        xalign 0.0 yalign 0.6 zoom 1.5
    show oriana_raw at myleft, backedaway_on, blurred
    show cecilia_raw possessed surprised at myright, backedaway_on, blurred
    show eye frame
    with eyeopen_slow
    scene bg black with eyeclose_slow
    scene bg basement at blurred:
        xalign 0.0 yalign 0.6 zoom 1.5
    show oriana_raw at myleft, backedaway_on, blurred
    show cecilia_raw possessed surprised at myright, backedaway_on, blurred
    show eye frame
    with eyeopen
    scene bg black with eyeclose
    scene bg basement:
        xalign 0.0 yalign 0.6 zoom 1.5
        blur 20.0
        linear 1.0 blur 0.0
    show oriana at myleft:
        blur 20.0
        linear 1.0 blur 0.0
    show cecilia possessed surprised at myright:
        blur 20.0
        linear 1.0 blur 0.0
    with eyeopen_quick
    pause 3.0
    Y wince "{cps=6}..........{/cps}"
    play ctc_sfx sfx_heartbeat_single
    $ fadein_sideimage = False
    Y afraid "*gasp* Wh-wha...?! I'm...?!" with shakeshort
    $ fadein_sideimage = True
    I "Karma...took my shackle...?" with hpunch
    C possessed thinking "...So you are now {i}against{/i} the plan.{w=0.5} But why?{w=0.5} Why would you want to impede your own safe escape?"
    play ctc_sfx "<silence 1.0>"
    O shadow "{cps=6}.....{/cps}"
    Y depressed "Ria...? What are you--" with shakeonce
    $ fadein_sideimage = False
    hide cecilia
    show oriana_raw shadow as oriana at mycenter_closeup
    Y afraid "Huh?!" with shakeonce
    play ctc_sfx sfx_choicegrand
    $ fadein_sideimage = True
    scene bg white with custom_flashbulb()
    play sound sfx_whooshlow
    scene cg hope:
        parallel:
            xalign 0.0 yalign 0.5 zoom 1.5
            pause 1.0
            easeout 1.5 zoom 1.25
            easein 1.5 zoom 1.0
        parallel:
            matrixcolor BrightnessMatrix(0.5)
            easein 3.0 matrixcolor BrightnessMatrix(0.0)
    with shakeshort
    pause 2.5
    play music bgm_hope_order
    $ show_music_info_timer = music_info_pop_out_time()
    pause 1.0
    $ show_side_oriana = True
    $ show_side_cecilia = True
    O leering2 "[name_player] being a spirit from Hell aside..."
    $ fadein_sideimage = False
    O "There's no way we can let a mass murderer like you walk free." with shakeonce
    Y afraid2 "Ria, wh-what are you doing?!" with shakeshort
    C possessed blink "{cps=6}.....{/cps} ...You are naive, child."
    C "Do you honestly believe you have any sort of power in this situation?"
    O "....."
    C "You are unarmed.{w=0.5} Weak.{w=0.5} And still recovering from an injury."
    C possessed "Meanwhile, I am in control of a young lady blessed with immense strength.{w=0.5}{nw}"
    play ctc_sfx sfx_knifebrandish
    with custom_flashquick()
    extend possessed grin " ...Oh, and this knife as well." with hpunch
    O irritated2 "....." with shakeonce
    C possessed blink "...See?{w=0.5} You flinched.{w=0.5} And you are right to do so."
    C possessed "Now, put your arm down and back away. To save you the embarrassment, I will even pretend this never happened."
    Y pained "Ria... Don't do this..." with shakeonce
    Y pained2 "You and Karma can escape now! Just leave me behind!" with shakeonce
    show cg hope:
        zoom 1.0 matrixcolor BrightnessMatrix(0.0) blur 20
        linear 5.0 blur 0
    play ctc_sfx "<silence 1.0>"
    Y depressed "I was...never supposed to be here anyway..."
    O "{cps=6}.....{/cps} ...This isn't about you, [name_player]."
    Y shocked "....."
    O annoyed2 "No matter how you look at this twisted situation... We can't just let it end like this."
    C possessed blink "...I understand it is not ideal, especially when I am currently hijacking the body of your friend."
    C possessed "But I assure you, I am [t_clue]sane[t_cluee]. And I am serious about returning this body to her."
    O irritated2 "You murdered countless people."
    C possessed blink "As a means to an end. As I have stated before, I detest cutting down people, especially women and children..."
    O shouting "But the fact remains. You killed those people with your own hands." with shakeonce
    O "If you are truly sane, you know that you need to answer for your crimes. Answer...to [t_clue]justice[t_cluee]."
    C "...\"Justice\"...? ...Pft..." with shakeonce
    C possessed grin "Do you remember with whom you are speaking? I am a [t_clue]spirit[t_cluee]."
    C "The only \"justice\" I answer to now is [t_clue]God Himself[t_cluee]. Do you claim to be His avatar?" with vpunch
    Y troubled "Ria... Please..." with shakeonce
    O annoyed "Even when you're not really Cecilia, you still go on the most infuriating tangents..." with shakeonce
    C possessed blink "{cps=6}.....{/cps} ...You're right. Forgive me for mocking you."
    C possessed "It is as you say. I know I must answer to my crimes."
    Y shocked "Wh-what?!" with shakeonce
    O leering2 "....."
    C possessed thinking "I still have [t_clue]unresolved matters[t_cluee] in the world of the living. So naturally, I must follow that world's rules once more."
    C possessed blink "I vow to you, dear Oriana and [name_player]... I will turn myself in for every one of my crimes over the decades."
    Y depressed "....." with shakeonce
    play ctc_sfx "<silence 1.0>"
    O disappointed "{cps=6}.....{/cps}"
    C possessed surprised "...Hm? What is that...puzzling expression?" with hpunch
    O thinking "I can tell you've thought a lot about this over the years..."
    O irritated "You've wanted to escape this house for so long...{w=0.5} There's an objective you so badly want to achieve..."
    C possessed blink "....."
    O leering "...But...you're also an immortal. [t_clue]Time has no meaning for you.[t_cluee]"
    O "You've already waited decades in solitude, with nothing but corpses keeping you company..."
    play ctc_sfx "<silence 1.0>"
    O "A normal prison is a mere instant compared to that." with shakeonce
    play ctc_sfx "<silence 1.0>"
    C shadow "{cps=6}.....{/cps}"
    O irritated "And then when us mere humans can't confine you anymore..."
    O dejected "You will start again. Continue to do absolutely anything it takes to achieve your [t_clue]final objective[t_cluee]."
    O injured "...And you will be a [t_clue]prisoner[t_cluee] to your impossible task once more..." with shakeonce
    C possessed surprised "{cps=6}.....{/cps} ...I see."
    C "Your defiance stems not from your morality nor convictions, but rather{cps=3}...{/cps}your [t_clue]kindness[t_cluee]."
    Y shadow "....."
    O leering "You are sane.{w=0.5} That's why...you continue to torture yourself." with shakeonce
    O "Killing people over and over and over again, even though it eats away at your soul." with shakeonce
    O irritated2 "That's why...{w=0.5}we must end it here.{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend leering2 " {color=#ff0000}YOU{/color} must end it here." with shakeshort
    play ctc_sfx "<silence 1.0>"
    C possessed blink "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    I "...Professor...?"
    play ctc_sfx "<silence 1.0>"
    C "{cps=6}..........{/cps} ...You have a valiant spirit, Oriana.{cps=1} {/cps}I commend you for showing a wretch like myself such consideration."
    $ fadein_sideimage = False
    Y panicked "W-wait, are you...?" with hpunch
    O injured "{cps=6}.....{/cps} ...I..." with shakeonce
    O "I wish...I could do more..." with shakeonce
    $ fadein_sideimage = True
    $ renpy.music.set_volume(0.5, 3.0, channel="music")
    scene bg black with dissolvemed
    pause 2.0
    Y shocked "...What...?"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    stop music fadeout 3.0
    pause 3.0
    $ show_side_oriana = False
    $ show_side_cecilia = False
    $ persistent.unlock_cg_hope = True
    scene bg basement:
        xalign 0.0 yalign 0.6 zoom 1.5
    show oriana injured at myleft
    show cecilia possessed blink at myright
    with dissolvemed
    $ renpy.music.set_volume(1.0, 1.0, channel="music")
    pause 3.0
    I "...What...happened?"
    play ctc_sfx "<silence 1.0>"
    I "They both just...stopped...?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    C possessed blink "....."
    C "...Perhaps if I had successfully kept you out of my library, this could have all been avoided."
    C possessed thinking "*sigh* What to do, what to do..." with hpunch
    Y wince "...?"
    play ctc_sfx sfx_heartbeat_single
    C possessed "...Oh! I suppose you don't have Cecilia to protect you at the moment." with shakeonce
    C possessed blink "And as long as none of you are fatally wounded...{w=1.0}there should be no risk of time travel occurring..."
    O panicked "...!!!" with shakeonce
    play sound sfx_knifebrandish
    show cecilia_raw possessed grin knife as cecilia at myright, backedaway_on:
        linear 2.0 xalign 0.5
    O shouting "[name_player]! RUN!!{w=1.0}{nw}" with shakeshort
    $ fadein_sideimage = True
    $ show_side_oriana = False
    $ show_side_cecilia = False
    play ctc_sfx sfx_knifeswing
    hide oriana
    show bg basement at blurring, wobble:
        xalign 0.1 yalign 0.6 zoom 2.0
    show cecilia possessed grin knife at mycenter_return, backedaway_off
    with custom_flashquick()
    play music bgm_chase
    $ show_music_info_timer = music_info_pop_out_time()
    play sound sfx_whooshlow
    Y afraid "Ngh!!" with shakeshort
    C "You can avoid any needless pain by simply handing over [name_player]'s shackle, you know."
    $ show_side_oriana = True
    hide cecilia
    show bg basement:
        xalign 0.3 yalign 0.0 zoom 2.0
    with custom_flashquick()
    O shouting "This way! Hurry!" with shakelong
    $ show_side_oriana = False
    play ctc_sfx sfx_runninglong_heels
    play sound sfx_runninglong
    scene bg black
    with fade
    pause 0.5


    call save_file_name_update (3, "d3a6_chasestart")
    show bg lounge
    with fade
    pause 0.5
    play ctc_sfx sfx_slamwall
    play sound sfx_doorcloseloud
    show bg lounge at blurring
    with shakeshort
    play loop_sfx sfx_heartbeat
    Y pained2 "*pant*{cps=2} {/cps}{nw}" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx sfx_heartbeat_single
    extend "*gasp*" with shakeonce
    $ fadein_sideimage = True
    I "Why...? Wh-why is this...?" with shakeonce
    $ _last_say_who = 'O'
    scene bg lounge
    show oriana leering at mycenter
    with dissolve
    stop loop_sfx fadeout 3.0
    O "Did he cut you?"
    Y pained "No... *pant* Just grazed me..." with hpunch
    $ fadein_sideimage = False
    play ctc_sfx sfx_emoteshout
    Y shouting "Wh-what are we doing?! Why did you two save me?!" with shakeshort
    $ fadein_sideimage = True
    O leering2 "Now that we know that we'd be releasing a madman from his prison, we can't just let him sacrifice you."
    O confused "We need a plan..."
    window auto hide None
    $ renpy.music.set_volume(0.0, 0, channel="music")
    $ renpy.music.set_volume(1.0, 1, channel="music")
    play ctc_sfx sfx_dooropenloud
    scene bg basement entrance light
    show cecilia possessed at mycenter_closeup
    with custom_flashquick()
    window auto show None
    Y afraid "AAAAGGHH!!" with shakeshort
    play sound sfx_knifebrandish
    show cecilia possessed grin knife at mycenter_closeup
    C "You realize I don't need to act like a zombie this time, yes?" with hpunch
    $ show_side_oriana = True
    O horrified "[name_player]!"
    play ctc_sfx sfx_strikeperson
    $ show_side_oriana = False
    show bg black
    show cecilia possessed grin knife at mycenter_zoomstill
    with custom_flashquick()
    play sound sfx_fallhard
    Y pained "ARGH!!" with shakelong
    C "Hold still now... I don't want to mess this up and hurt your host..." with hpunch
    play ctc_sfx sfx_restrain
    I "Nrgh... Not good, he's got me pinned down!" with shakeshort
    KI "[t_ghost]No...! We can't lose here...![t_ghoste]" with shakeshort
    I "It's...{color=#ff0000}game over{/color} already?! What do I--" with shakeshort
    play sound sfx_wail
    KI "{size=+5}[t_ghost]I NEED TO [t_ghoste]SAVE {color=#fff}[input_name]{/color}!!{/size}" with shakelong
    play ctc_sfx "<silence 1.0>"
    play sound2 sfx_rewind
    $ renpy.music.set_volume(0.0, 3, channel="music")
    scene bg black with pixellate
    pause 4.0
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y wince "....."
    play ctc_sfx "<silence 1.0>"
    play sound sfx_flashback
    scene bg white with dissolve
    scene bg lounge:
        xalign 0.5 yalign 0.5 zoom 2.0
        easein 1.0 zoom 1.0
    show oriana leering at mycenter_fadein
    with soulin
    pause 1.0
    $ renpy.music.set_volume(1.0, 3, channel="music")
    Y afraid "*gasp* Wha... Wait..." with shakeshort
    O leering2 "Now that we know that we'd be releasing a madman from his prison, we can't just let him sacrifice you."
    O confused "We need a plan..."
    play ctc_sfx "<silence 1.0>"
    Y shouting "RIA, GET BACK!!" with shakeshort
    O panicked "Wha--"
    window auto hide None
    play ctc_sfx sfx_dooropenloud
    scene bg basement entrance light
    show cecilia possessed at mycenter_return
    with custom_flashquick()
    pause 0.5
    C possessed thinking "Hmm? Where did--"
    play ctc_sfx "<silence 1.0>"
    show bg basement entrance light:
        xalign 0.5 yalign 0.4 zoom 1.5
    show cecilia possessed thinking at mycenter_closeup
    Y scream "NRAAAGHH!!" with shakelong
    play ctc_sfx sfx_whooshlow
    pause 0.1
    play sound sfx_strikeperson
    show bg basement entrance light:
        xalign 0.5 yalign 0.4 zoom 1.0
    show cecilia possessed surprised at mycenter, shrink:
        zoom 1.0
    with custom_flashquick()
    C "AGGGHH!!{w=1.0}{nw}" with shakelong
    play ctc_sfx "<silence 1.0>"
    window auto hide
    show cecilia possessed surprised at crouch:
        alpha 1.0
        linear 0.5 alpha 0.0
    pause 0.5
    scene bg black with dissolve
    play sound sfx_fallstairs
    with shakelong
    pause 0.4
    with shakeshort
    pause 0.6
    with shakeonce
    pause 1.0
    Y pained "*gasp* *pant*" with shakeonce
    play sound sfx_doorcloseloud
    window auto hide shakeshort
    scene bg lounge
    with fade
    I "Sorry, Cece... But if anyone can survive a tumble down a flight of stairs, it'd be you..." with hpunch
    window auto hide
    $ _last_say_who = 'O'
    show oriana panicked at mycenter
    with dissolve
    O "[name_player]... D-did you just--" with shakeonce
    Y shouting "Quick, let's get to the foyer!" with shakeonce
    O leering2 "R-right!"
    play ctc_sfx sfx_runninglong_heels
    play sound sfx_running
    scene bg black
    with dissolve
    pause 0.5
    play sound [ sfx_doorcloseloud, sfx_running ]
    show bg black with shakeshort
    pause 0.5
    scene bg foyer
    with dissolve
    pause 2.0
    Y pained "*huff* Damn... *huff* The front door is still closed..." with shakeshort
    window auto hide
    $ _last_say_who = 'O'
    show oriana leering2 at mycenter with dissolve
    O "[name_player]. Did you just [t_clue]turn back time[t_cluee] again?"
    Y panicked "I... I-I think so?"
    I "I heard that voice again...{w=0.5} ...Wait, but that voice is..." with hpunch
    Y thinking "...Karma?"
    KI "Yeah, I'm here! Do you hear me?" with shakeonce
    Y afraid2 "...!!!{cps=1} {/cps}Ria, I... I can [t_clue]hear Karma's voice[t_cluee] in my head!" with shakeshort
    O panicked "What?! How is that possible?!" with shakeonce
    KI "I don't know why exactly, but I can still feel all my senses, even if I'm not in control of my body..." with hpunch
    Y angry "S-so you can hear Ria too?" with shakeonce
    O confused "Hear...me? What?"
    KI "I can, yeah! But it looks like she can't hear {i}my{/i} voice, which makes sense..." with vpunch
    Y worried "Uh... R-Ria, it seems that Karma can hear you, but you can't hear her at the moment..."
    O irritated2 "...Ugh, I guess there's no point in being skeptical. I'll just have to trust what you say." with shakeonce
    O leering "Karma. If you can hear me, I think you and I both know what we have to do here."
    KI "Yeah... We need to [t_clue]get that shackle off Cece's wrist[t_cluee]..."
    play ctc_sfx sfx_heartbeat_single
    I "...!{w=0.5} That's true, that would solve everything!" with shakeonce
    O annoyed "The tricky part is catching the Professor off guard... And avoiding that knife all the while..." with hpunch
    window auto hide None
    $ renpy.music.set_volume(0.0, 0, channel="music")
    $ renpy.music.set_volume(1.0, 1, channel="music")
    play ctc_sfx sfx_dooropenloud
    scene bg foyer dark
    show cecilia possessed at mycenter_closeup
    with custom_flashquick()
    window auto show None
    C "Come now, isn't it a tad cruel to push your friend down a flight of stairs?" with hpunch
    play ctc_sfx sfx_knifebrandish
    show cecilia possessed grin knife
    Y afraid "CRAP, HE CAUGHT UP!!" with shakeshort
    show cecilia possessed grin knife at mycenter_zoomstill
    play ctc_sfx sfx_knifeswing
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O horrified "NO!!" with shakelong
    play ctc_sfx sfx_knifeslash
    $ show_side_oriana = False
    $ fadein_sideimage = True
    window auto hide custom_flashquickred()
    $ renpy.music.set_volume(0.0, 0, channel="music")
    scene bg black
    show bloodsplatter_5 behind oriana at truecenter:
        alpha 0.5
    show oriana stabbed at mycenter
    show stab censor
    show cecilia possessed grin knife at myright
    with shakelong
    pause 1.0
    show oriana horrified at shrink
    O "Krrgh! ...A-ah..." with shakeshort
    C possessed surprised "...Now {i}why{/i} would you jump in front of a knife like that...?{w=0.5} Don't you know how dangerous that is...?"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    hide oriana
    hide stab censor
    hide bloodsplatter_5
    with dissolve
    $ _last_say_who = None
    play sound sfx_fallhard
    show bloodsplatter_1 at truecenter:
        alpha 1.0
        linear 2.0 alpha 0.0
    with shakeshort
    pause 1.0
    Y depressed bloody "{cps=6}R-Ria...{/cps}" with shakeonce
    play sound sfx_wail
    with custom_flashquick()
    KI "{size=+5}RIA!! NOOOOOOOO!!{/size}" with shakelong
    play ctc_sfx "<silence 1.0>"
    play sound2 sfx_rewind
    $ renpy.music.set_volume(0.0, 3, channel="music")
    scene bg black with pixellate
    pause 4.0
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y wince "....."
    play ctc_sfx "<silence 1.0>"
    play sound sfx_flashback
    scene bg white with dissolve
    scene bg foyer:
        xalign 0.5 yalign 0.5 zoom 2.0
        easein 1.0 zoom 1.0
    show oriana annoyed at mycenter_fadein
    with soulin
    pause 1.0
    $ renpy.music.set_volume(1.0, 3, channel="music")
    Y afraid "... *gasp* ...I..." with shakeshort
    O "The tricky part is catching the Professor off guard... And avoiding that knife all the while..." with hpunch
    window auto hide None
    play ctc_sfx sfx_dooropenloud
    scene bg foyer dark
    show cecilia possessed at mycenter_closeup
    with custom_flashquick()
    window auto show None
    C "Come now, isn't it a tad cruel to push your friend down a flight of stairs?" with hpunch
    play ctc_sfx sfx_whooshlow
    window auto hide None
    scene bg foyer
    show oriana panicked at mycenter
    with custom_flashquick()
    window auto show None
    Y shouting "RIA! THIS WAY!" with shakeshort
    O "Ah-- [name_player]?!" with shakeonce
    window auto hide
    play ctc_sfx sfx_running_heels
    play sound sfx_running
    show bg foyer:
        xalign 0.6 yalign 0.8 zoom 1.0
        linear 1.0 zoom 1.5
    hide oriana
    with dissolvequick
    scene bg black
    with dissolve
    play sound2 sfx_dooropen
    pause 1.0
    play sound2 sfx_doorcloseloud
    with shakeshort
    scene bg bathroom:
        xalign 0.0 yalign 0.4 zoom 1.4
        easein 3.0 zoom 1.3
    with dissolve
    pause 1.0
    Y pained "*gasp*{cps=2} {/cps}{nw}" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend "*pant*" with shakeonce
    $ fadein_sideimage = True
    $ _last_say_who = "O"
    scene bg bathroom:
        xalign 0.0 yalign 0.4 zoom 1.3
    show oriana irritated2 at mycenter
    with dissolve
    O "*pant* *huff* ...This is..." with shakeonce
    O horrified "Wha... [name_player], you've put us in a corner!" with shakeshort
    Y angry "W-well, it's better than letting you throw yourself in front of a knife!" with shakeonce
    stop music fadeout 3.0
    play ctc_sfx sfx_heartbeat_single
    O panicked "...!!!" with shakeshort
    O surprised "Y-you... You just did it again, didn't you?" with hpunch
    play ctc_sfx sfx_emotequestion
    O "You turned back time [t_clue]just a small amount[t_cluee]..."
    Y thinking "Huh? {cps=6}.....{/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend panicked " ...Oh!" with shakeonce
    $ fadein_sideimage = True
    KI "{color=#fff}[input_name]{/color}! I...I think I'm starting to get the hang of this!" with shakeonce
    Y shouting "Karma's getting the hang of this!{cps=2} {/cps}Apparently!" with vpunch
    O irritated "This... This is it." with shakeonce
    O "{cps=6}.....{/cps} ...The [t_clue]miracle[t_cluee] we've been looking for...{nw}"
    play ctc_sfx "<silence 1.0>"
    play music bgm_truth
    $ show_music_info_timer = music_info_pop_out_time()
    extend "" with shakeonce
    Y surprised "M-miracle...? What do you mean?"
    O default "[name_player], if you can turn back time at will, then it should be possible for you to [t_clue]cheat[t_cluee] us out of this."
    Y thinking "\"Cheat\"...?"
    KI "Ah! Of course!" with vpunch
    O leering2 "Whenever you're about to be captured, turn back time and [t_clue]try again[t_cluee]."
    O "Keep doing so until you manage to remove that shackle from Cecilia's wrist." with shakeonce
    Y panicked "Ooooh... That might just work!" with shakeonce
    play ctc_sfx sfx_heartbeat_single
    KI "It HAS to work! That's the only shot we have at [t_clue]winning[t_cluee]!" with shakeonce
    O thinking "Don't be reckless, though... Even if you can revert any injuries you get, they will obviously still hurt."
    O irritated "And remember... Just like how {i}I{/i} can faintly recall memories from before you reverted time..."
    O leering "It's possible the Professor will [t_clue]start to notice[t_cluee] as well. You'll want to avoid using your power too much." with shakeonce
    Y leering "Right, makes sense."
    I "I should try to play this carefully wherever I can..." with hpunch

label d3a6_chase_pt1:
    window auto hide None
    $ renpy.music.set_pan(0.75, 0, channel='sound')
    play sound sfx_slamwall2
    show oriana panicked with shakeshort
    $ sfx_slamwall_random("sound")
    with shakeonce
    pause 0.5
    $ show_side_cecilia = True
    C hidden "I would rather not break apart my own house, but I'm at the limits of my patience now."
    $ fadein_sideimage = False
    C "Hmm... I suppose to take down a door, an axe is the best tool for that.{w=1.0} There should be one in the basement..."
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    play sound sfx_steps
    $ renpy.music.set_pan(0.0, 1, channel='sound')
    window auto hide
    $ renpy.music.set_volume(0.5, 3, channel="music")
    pause 3.0
    O thinking "...I think now's our chance.{w=0.5} Are you ready?{nw}"

    menu:
        extend ""
        "Go out now":
            Y thinking "Yeah, while he's away for a moment..."
            window auto hide
            hide oriana with dissolve
            Y blink "{cps=12}Okay, quietly...open...{/cps}"
            play ctc_sfx sfx_dooropen
            show bg bathroom:
                xalign 0.0 yalign 0.4 zoom 1.3
                easeout 1.0 xalign 0.5
            window auto hide
            pause 0.4
            stop ctc_sfx
            stop sound
            $ renpy.music.set_volume(0.0, 0, channel="music")
            window auto hide None
            scene bg black
            show cecilia possessed grin knife at mycenter_zoomstill
            $ show_side_cecilia = False
            window auto show None
            C "You fell for it."
            play ctc_sfx "<silence 1.0>"
            Y afraid "AUUUGHHH!!" with shakeshort
            play sound sfx_wail
            KI "GO BACK, GO BACK!!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            play sound2 sfx_rewind
            $ renpy.music.set_volume(0.0, 3, channel="music")
            scene bg black with pixellate
            achieve THE_SHINING
            pause 1.5
            play ctc_sfx sfx_flashback
            scene bg white with dissolve
            scene bg bathroom:
                xalign 0.5 yalign 0.5 zoom 2.0
                easein 1.0 xalign 0.0 yalign 0.4 zoom 1.3
            show oriana leering at mycenter_fadein
            with soulin
            $ renpy.music.set_volume(1.0, 3, channel="music")
            pause 1.0
            window auto show
            play ctc_sfx sfx_emotesigh
            show bg bathroom:
                xalign 0.0 yalign 0.4 zoom 1.3
            I "...Ugh... I'm starting to get dizzy..." with hpunch
            jump d3a6_chase_pt1
        "Wait a little longer":
            Y angry "No, let's wait a little bit. Just in case." with shakeonce
            $ fadein_sideimage = False
            C "....."
            $ fadein_sideimage = True
            O irritated "....."
            play ctc_sfx "<silence 1.0>"
            C "{cps=6}.....{/cps} ...Hm, you [t_clue]didn't fall for that[t_cluee]... I suppose that would have been too easy..."
            $ fadein_sideimage = False
            play ctc_sfx sfx_emotehappy
            C "Very well, the axe it is!" with vpunch
            play ctc_sfx "<silence 1.0>"
            $ renpy.music.set_pan(0.75, 0, channel='sound')
            play sound sfx_steps
            window auto hide
            pause 3.0
            $ renpy.music.set_pan(0.0, 1, channel='sound')
            O leering "....."
            $ fadein_sideimage = True
            Y blink "{cps=6}.....{/cps} *deep inhale*"
            stop music
            $ renpy.music.set_volume(1.0, 0, channel="music")
            I "Now!" with shakeshort
    window auto hide None
    play music bgm_chase
    play ctc_sfx sfx_dooropenloud
    with custom_flashquick()
    scene bg foyer
    show cecilia possessed blink at mycenter
    with shakeshort
    $ show_side_cecilia = False
    C possessed surprised "Hmm?{w=0.5} Are you giving up?"
    show bg foyer at wobble, blurring
    Y shouting "{cps=24}RAAAAAGGHHH!!{/cps}{nw}" with shakeshort
    $ fadein_sideimage = False

    menu:
        extend ""
        "Grab the wrist shackle":
            show cecilia possessed surprised at mycenter_closeup
            Y pained "Grgh!" with shakeshort
            $ fadein_sideimage = True
            $ _last_say_who = "C"
            play sound sfx_whoosh
            show cecilia possessed blink at myright with shakeshort
            C "Hmph!{w=0.5} ...I see, so {i}that's{/i} your plan..."
            I "No... I couldn't grab it..." with hpunch
            show cecilia_raw possessed grin knife as cecilia at mycenter_closeup
            pause 0.5
        "Punch her in the face":
            show cecilia possessed surprised at mycenter_closeup
            play sound sfx_whooshlow
            Y "TAKE THIS!!" with shakeshort
            $ fadein_sideimage = True
            play ctc_sfx sfx_strike
            show bg black
            show cecilia possessed blink at mycenter_zoomstill
            C "....." with shakeshort
            I "...!! She...caught my fist..." with hpunch
            play ctc_sfx sfx_knifebrandish
            C possessed grin knife "I see... You're just handing your wrist over to me, is that it?" with hpunch
    window auto hide None
    play ctc_sfx sfx_whooshlow
    scene bg black with custom_flashquick()
    Y scream "AAAAGH!!" with shakeshort
    play ctc_sfx sfx_fallhard
    window auto hide shakelong
    show bg foyer dark:
        xalign 0.2 zoom 2.0
    with dissolve
    $ show_side_cecilia = True
    play sound sfx_restrain
    C possessed grin "I'll be taking this now..." with shakeshort
    $ show_side_cecilia = False
    play sound sfx_wail
    KI "NO!! GO BACK!!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    play sound2 sfx_rewind
    $ renpy.music.set_volume(0.0, 3, channel="music")
    scene bg black with pixellate
    pause 1.5
    play ctc_sfx sfx_flashback
    scene bg white with dissolve
    scene bg black with soulin
    $ renpy.music.set_volume(1.0, 3, channel="music")
    pause 1.0
    play music bgm_chase

label d3a6_chase_pt2:
    play ctc_sfx sfx_dooropenloud
    with custom_flashquick()
    scene bg foyer
    show cecilia possessed blink at mycenter
    with shakeshort
    $ show_side_cecilia = False
    C possessed surprised "Hmm?{w=0.5} Are you giving up?"
    play ctc_sfx "<silence 1.0>"
    Y scream "RIA! LET'S HEAD UP!" with shakelong
    $ show_side_oriana = True
    $ fadein_sideimage = False
    O panicked "Huh?! Wha--" with hpunch
    $ show_side_oriana = False
    $ fadein_sideimage = True
    play ctc_sfx sfx_knifebrandish
    show bg foyer:
        xalign 1.0 yalign 0.8 zoom 1.5
    show cecilia possessed grin knife at myright
    C "No, I don't think I'll allow that." with hpunch
    show bg foyer at wobble, blurring:
        xalign 1.0 yalign 0.8 zoom 1.5
    show cecilia possessed grin knife at mycenter_closeup
    I "Ngh! She's fast...{nw}" with shakeonce

    menu:
        extend ""
        "Headbutt her":
            Y shouting "Take...{cps=3} {/cps}{nw}"
            $ fadein_sideimage = False
            play ctc_sfx sfx_strikeperson
            show bg foyer at reset:
                zoom 1.0 blur 0
            show cecilia possessed surprised at mycenter_return
            with custom_flashquick()
            extend pained2 "THIS!!" with shakelong
            $ fadein_sideimage = True
            C "NGH!! Tch..." with shakeshort
            play ctc_sfx "<silence 1.0>"
            I "Ow... My head..." with hpunch
            show cecilia_raw possessed grin knife as cecilia at mycenter_closeup
            play ctc_sfx sfx_whooshlow
            Y afraid "Uwah!" with shakeshort
            hide cecilia
            show bg foyer at wobble, blurring:
                xalign 0.5 yalign 0.5 zoom 1.5
            with custom_flashquick()
            play ctc_sfx sfx_restrain
            $ show_side_cecilia = True
            C possessed blink "Were you trying to knock me unconscious with that?! Did you forget I am a spirit controlling this girl like a puppet?" with hpunch
            $ fadein_sideimage = False
            C possessed grin "Oh, I suppose you're in the same boat. Not for long, though--{w=1.0}{nw}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            $ show_side_cecilia = False
            $ fadein_sideimage = True
            play sound sfx_wail
            KI "GO BACK!! BAAAACK!!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            play sound2 sfx_rewind
            $ renpy.music.set_volume(0.0, 3, channel="music")
            scene bg black with pixellate
            pause 1.5
            play ctc_sfx sfx_flashback
            scene bg white with dissolve
            scene bg black with soulin
            $ renpy.music.set_volume(1.0, 3, channel="music")
            pause 1.0
            jump d3a6_chase_pt2
        "Grab the shackle once she's close":
            I "3... 2..." with hpunch
            show cecilia_raw possessed grin knife as cecilia at mycenter_zoomstill
            C "...Heh."
            Y afraid "Uwah!" with shakeshort
            play ctc_sfx sfx_fallhard
            window auto hide None
            hide cecilia
            show bg foyer dark:
                xalign 0.8 zoom 2.0
            window auto show custom_flashquick()
            Y pained "NRGH!!" with shakelong
            $ fadein_sideimage = False
            $ show_side_cecilia = True
            C possessed grin "You don't think I'm on to your schemes?"
            C possessed blink "Now, I'll be taking that sha--{w=1.0}{nw}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            $ show_side_cecilia = False
            $ fadein_sideimage = True
            play sound sfx_wail
            KI "GO BACK!! BAAAACK!!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            play sound2 sfx_rewind
            $ renpy.music.set_volume(0.0, 3, channel="music")
            scene bg black with pixellate
            pause 1.5
            play ctc_sfx sfx_flashback
            scene bg white with dissolve
            scene bg black with soulin
            $ renpy.music.set_volume(1.0, 3, channel="music")
            pause 1.0
            jump d3a6_chase_pt2
        "Turn back":
            pass
    C "Oh? Are you going to--{w=0.5}{nw}"
    play ctc_sfx sfx_whooshlow
    $ show_side_cecilia = True
    window auto hide None
    scene bg foyer at reset:
        zoom 1.0 blur 0
    show oriana panicked at mycenter
    with custom_flashquick()
    window auto show None
    extend possessed surprised " Ah!" with shakeonce
    O "AHH! [name_player], I can run without you pulling on my hand!" with shakeonce
    I "It worked! We got him out of the way!" with vpunch
    C possessed thinking "You're a crafty one, aren't you, [name_player]...?"
    O shouting "[name_player], we need to get that shackle off of--" with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y pained "NOT YET!" with shakeshort
    $ show_side_cecilia = False
    window auto hide None
    play ctc_sfx sfx_running_heels
    play sound sfx_running
    show bg foyer:
        xalign 0.1 yalign 0.8 zoom 1.0
        linear 1.0 zoom 1.5
    hide oriana
    with dissolvequick
    scene bg black
    with dissolve
    play sound2 sfx_dooropen
    pause 1.0
    play sound2 sfx_doorcloseloud
    with shakeshort
    scene bg diningroom:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 3.0 zoom 1.0
    with dissolve
    pause 1.0
    Y pained2 "*pant*{cps=2} {/cps}{nw}" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend "*gasp*{cps=2} {/cps}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    extend pained "Damn it... He doesn't have any blind spots..." with shakeonce
    $ fadein_sideimage = True
    window auto hide
    $ _last_say_who = "O"
    show oriana irritated2 at mycenter
    with dissolve
    O "Nrgh... [name_player], did you have to rewind time again?" with shakeonce
    Y scream "ARGH!! This is IMPOSSIBLE! My hands just can't reach fast enough!" with shakelong
    KI "Sorry... If only my body was a little more athletic..." with hpunch
    O leering2 "...[name_player]. Don't forget that I'm here."
    O confused "The Professor's target is you, but maybe I could distract him somehow, if only momentarily..."
    Y angry "No, it's too dangerous. Even knowing time will rewind, I don't think he hesitates from killing you at all." with shakeonce
    $ fadein_sideimage = False
    Y wince "Plus, I...{w=0.5} Karma and I both...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " We don't EVER want to see you die again." with hpunch
    $ fadein_sideimage = True
    play ctc_sfx sfx_emotehappy
    KI "That's right! Well said, {color=#fff}[input_name]{/color}!" with vpunch
    O thinking "...All right.{w=1.0} Is there anything we could use here...{w=1.0}{nw}"
    window auto hide None
    $ renpy.music.set_volume(0.0, 0, channel="music")
    play ctc_sfx "<silence 1.0>"
    play sound sfx_knifeslash
    show bg black
    show bloodsplatter_5 behind oriana at truecenter:
        alpha 0.5
    show oriana stabbed
    with custom_flashquickred()
    window auto show None
    O "NGGHHH!!" with shakeshort
    Y afraid2 "RIAAA!!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    show bloodsplatter_5:
        linear 3.0 alpha 0.0
    show oriana injured at crouch
    O "M-my... My [t_clue]leg[t_cluee]..." with shakeonce
    $ show_side_cecilia = True
    C hidden "Did you forget about the [t_clue]pet doors[t_cluee]? I suppose they don't squeak nearly as loudly as the human-sized doors."
    $ fadein_sideimage = False
    Y pained "Y-you..." with shakeonce
    $ fadein_sideimage = True
    $ renpy.music.set_volume(1.0, 3, channel="music")
    scene bg black with dissolvemed
    pause 0.5
    scene bg diningroom with dissolvemed
    $ show_side_oriana = True
    C hidden "Now then...{cps=2} {/cps}What will you do next, runaway spirit from Hell?"
    $ fadein_sideimage = False
    C "Your friend is no longer able to run. Do you dare risk her becoming a hostage?"
    O injured "[name_player]... I'm so sorry..." with shakeonce
    C "Of course, she won't be able to die thanks to your time traveling power."
    C "But I wonder if it would be just as effective to have you watch me kill her over and over?"
    Y scream "I'll never let you do that!" with shakeshort
    C "Then take off your shackle and place it near the pet door. I promise this will all be over if you do so."
    Y pained "Grr..." with shakeonce
    $ show_side_oriana = False
    $ fadein_sideimage = True
    window auto hide
    $ _last_say_who = "O"
    show oriana irritated at mycenter
    with dissolvemed
    O "[name_player]...{w=0.5} Karma...{w=0.5} {size=-10}I...{w=0.5}I have [t_clue]one last idea[t_cluee]...{/size}"
    Y shocked "Ria?" with shakeonce
    O injured "{size=-10}Buy me some time... I need...to get [t_clue]upstairs[t_cluee]...{/size}" with shakeonce
    C hidden "Hmm? Are you whispering your final farewells to each other?"
    $ fadein_sideimage = False
    Y angry "...No, we're just agreeing that we won't give up." with shakeonce
    $ fadein_sideimage = True
    I "Okay, think... How do we get Ria upstairs...?" with hpunch
    I "The Professor's trying to come in through the door that Ria needs to use..."
    play ctc_sfx sfx_emotehappy
    KI "{color=#fff}[input_name]{/color}! Let's lure him into the [t_clue]kitchen[t_cluee]!" with vpunch
    I "The kitchen...? How can we--"
    play ctc_sfx sfx_heartbeat_single
    I "Ah! That's it!" with shakeonce
    Y leering "{size=-10}Ria! Get under the table!{/size}" with shakeonce
    hide oriana with dissolve
    Y blink "...Professor. How about we have a little [t_clue]duel[t_cluee]?"
    $ fadein_sideimage = False
    C "A...duel? What are you proposing?"
    Y thinking "I'm going to take one of the other [t_clue]knives[t_cluee] from the kitchen."
    Y leering "We'll have a good ol' fashioned [t_clue]sword fight[t_cluee]. But with knives."
    C "And why would I agree to that when I have one knife over you already?"
    Y blink "You said that you don't like cutting down people, didn't you?"
    Y "If you can corner me in a duel, fair and square, I'll give you my wrist shackle without any more trouble."
    C "...What you're proposing is absolutely absurd."
    C "You lack the physical ability to defeat me while I am using this girl's body."
    C "And even if you had the ability, can you bear to swing a knife at someone so dear to you?"
    C "Finally, [t_clue]none of us can leave this place[t_cluee] until someone goes to Hell. Even if you somehow win, I will still kill you."
    play ctc_sfx sfx_heartbeat_single
    Y wince "....." with shakeonce
    Y thinking "...True... So how about this?"
    Y blink "If I can fend off your attacks for [t_clue]one minute[t_cluee], OR [t_clue]knock away your knife[t_cluee] from your hands...{w=1.0} You must...{nw}"

    menu:
        extend ""
        "Sacrifice yourself as well":
            $ fadein_sideimage = True
            KI "Wha-- {color=#fff}[input_name]{/color}! But h-he's done so much, killed SO many people, all to escape this place!" with shakeshort
            KI "He'd never--" with shakeonce
            stop music fadeout 3.0
            play ctc_sfx "<silence 1.0>"
            Y shadow2 "...You must {color=#ff0000}go to Hell{/color} with me."
            $ fadein_sideimage = False
            play ctc_sfx "<silence 1.0>"
            C "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            Y "{cps=6}.....{/cps} ...Neither of us have the right to return to the world of the living. Especially at the cost of other people's lives."
            play ctc_sfx "<silence 1.0>"
            Y "You and I both...{w=1.0}{nw}"
            play ctc_sfx "<silence 1.0>"
            extend "need to move on." with shakeonce
            play ctc_sfx "<silence 1.0>"
            C "{cps=6}.......{/cps}"
            $ fadein_sideimage = True
            KI "...{color=#fff}[input_name]{/color}..."
            play ctc_sfx "<silence 1.0>"
            C "{cps=6}.....{/cps} ...Yes.{cps=1} {/cps}I suppose no matter how much I may wish for my family to be whole again..."
            $ fadein_sideimage = False
            C "...It is far too late now. Even with a new life, nothing will ever be the same as those days..."
            $ show_side_oriana = True
            play ctc_sfx "<silence 1.0>"
            O shadow "{cps=6}.....{/cps}"
            $ show_side_oriana = False
        "Throw yourself into the Gate instead":
            $ fadein_sideimage = True
            KI "Wait, {color=#fff}[input_name]{/color}! He'd never agree to that!" with shakeonce
            stop music fadeout 3.0
            Y angry "...You must throw yourself into the Gate instead."
            $ fadein_sideimage = False
            C "{cps=6}.....{/cps} ...That may sound like a fair wager, but to reiterate, I have one knife over you already."
            C "Why would I agree to bet my life in addition to allowing you a weapon and easier victory conditions?"
            $ fadein_sideimage = True
            KI "Exactly..." with shakeonce
            Y blink "Because there's no way you'll lose."
            $ fadein_sideimage = False
            C "....."
            Y thinking "It's not like I have any chance of knocking away your knife. And one minute is a very long time for a duel."
            Y relaxed "Or what, are you too scared for your life to give me one last, futile chance to protect myself?"
            C "...Hmph. Is that your idea of a taunt? Do you consider me a prideful man?"
            play ctc_sfx "<silence 1.0>"
            C "I care for nothing but achieving my objectives. I will endure any shame, disgrace, or atrocious acts to that end." with shakeonce
            play ctc_sfx "<silence 1.0>"
            Y troubled "....." with shakeonce
            C "But I sense there is another purpose for this...duel."
            C "Perhaps I will humour you for a moment, if only to satisfy my curiosity at your sudden bravado."
            $ fadein_sideimage = True
            KI "I-It worked...?!" with shakeonce
        "Wait for the next victim":
            stop music fadeout 3.0
            Y blink "...You must promise to wait for the next person to enter this space, and sacrifice them instead."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            KI "...{color=#fff}[input_name]{/color}... You can't be serious, right...?" with shakeonce
            if died_with_regrets:
                play ctc_sfx "<silence 1.0>"
                I "{cps=6}.....{/cps} ...I am."
                I "There's still something I need to do. I can't just let myself die here..."
            else:
                I "Of course I'm not."
                I "It's not like I really want to live again, but...I need him to think I'm serious about this..." with hpunch
            $ show_side_oriana = True
            play ctc_sfx "<silence 1.0>"
            O irritated "{cps=6}.....{/cps}"
            $ fadein_sideimage = False
            $ show_side_oriana = False
            C "...Heh.{cps=1} {/cps}{nw}"
            play ctc_sfx "<silence 1.0>"
            extend "AHAHAHAHAHAHAAA!!" with shakeshort
            C "You truly are a spirit from {color=#ff0000}Hell{/color}. Letting innocent people perish for your own revival..."
            Y wince "....."
            C "...But I suppose I am no different."
    C "Very well. I accept your conditions."
    $ fadein_sideimage = False
    Y leering "All right.{w=1.0} Count to 10, then meet me in the kitchen."
    C "As you wish. One... Two..."
    $ fadein_sideimage = True
    I "...Looks like Ria understands the plan. Okay, let's go."
    $ show_side_cecilia = False
    play ctc_sfx sfx_steps
    scene bg black with fade
    pause 1.0
    scene bg kitchen with dissolvemed
    pause 2.0
    scene bg kitchen:
        xalign 0.5 yalign 0.6 zoom 1.8
    with dissolve
    Y shadow2 "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    play sound sfx_knifebrandish
    show bg kitchen twoknives:
        xalign 0.5 yalign 0.6 zoom 1.8
    with hpunch
    $ persistent.unlock_bg_kitchen_twoknives = True
    show pov_knife:
        xalign 0.5 yalign 1.0
        zoom 0.8
    with dissolve
    play sound2 sfx_knifeglint
    show knife glint at mycenter:
        zoom 1.0 ypos 1.05 alpha 0.0 xalign 0.38
        easein 0.4 zoom 1.2 ypos 1.1 alpha 1.0 xalign 0.28
        linear 0.2 alpha 0.0
    pause 2.0
    KI "Remember, {color=#fff}[input_name]{/color}...{w=0.5} Don't hurt Cece, or else I'll..." with hpunch
    I "Rewind time, right? I know."
    $ renpy.music.set_pan(-0.75, 0, channel='sound')
    $ renpy.music.set_pan(-0.75, 0, channel='ctc_sfx')
    play ctc_sfx sfx_dooropen
    window auto hide shakeonce
    play sound sfx_steps
    $ renpy.music.set_pan(0.0, 3, channel='sound')
    $ renpy.music.set_pan(0.0, 3, channel='ctc_sfx')
    scene bg black with dissolvemed
    pause 1.0
    scene bg kitchen twoknives with dissolvemed
    $ d3a6_duel_hp = 3

label d3a6_chase_duel:
    scene bg kitchen twoknives
    pause 1.0
    $ _last_say_who = 'C'
    show cecilia possessed blink at mycenter
    with dissolvemed
    pause 1.0
    play music bgm_tension
    $ show_music_info_timer = music_info_pop_out_time()
    show cecilia possessed at mycenter
    with shakeonce
    pause 1.0
    C "...Are you prepared?"
    $ _last_say_who = None
    window auto hide
    play sound sfx_knifebrandish
    with custom_flashquick()
    show pov_knife:
        xalign 0.5 zoom 0.8 yalign 1.1
        easein 0.5 yalign 1.0
    with dissolve
    pause 0.5
    Y leering "....." with shakeonce
    C possessed grin "Excellent. Try to make this entertaining for me."
    I "....."
    show bg black with dissolve
    I "...Like he said, I probably [t_clue]can't actually win[t_cluee] this duel...{w=0.5} Plus, I don't want to hurt Cece..."
    I "But he knows that if he kills me, time will rewind. So he'll probably focus on [t_clue]injuring me[t_cluee] until I {color=#ff0000}lose all my strength{/color}..."
    I "But that's okay... All I have to do is [t_clue]drag this out[t_cluee] for as long as I can..." with shakeonce
    if d3a6_duel_hp < 3:
        I "And...{w=0.5}he doesn't know that I can [t_clue]turn back time at will[t_cluee] now..."
        I "If I mess up, all I need to do is {color=#cccc00}roll back the clock{/color}{image=intext_iconback} a bit..."
        KI "Good luck, {color=#fff}[input_name]{/color}! I'll be at the ready!" with vpunch
    window auto hide
    show bg kitchen twoknives with dissolve
    $ d3a6_duel_hp = 3
    C possessed blink "Now.{w=0.5} Let's begin the duel."
    play ctc_sfx "<silence 1.0>"
    play sound sfx_knifebrandish
    C possessed grin knife "I will allow you the first move.{w=0.5} Come at me.{nw}"


    menu:
        extend ""
        "Strike first":
            hide pov_knife with custom_flashquick()
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeswing
            Y shouting "HA!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeclash
            show bg black
            show cecilia possessed blink at mycenter_closeup with custom_flashquick()
            C "Weak." with hpunch
            play ctc_sfx sfx_strikeperson
            show cecilia possessed at mycenter
            show bloodsplatter_5 at truecenter:
                alpha 0.5
                linear 3.0 alpha 0.0
            with custom_flashquick()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            Y pained "KURGHHH!!" with shakelong
            I "Urgh... Right in the gut..." with shakeshort
        "Bide your time":
            hide pov_knife with dissolve
            Y leering "....."
            C possessed "....."
            C possessed blink "...You are right to be cautious. Very well, I rescind my generosity."
    show cecilia possessed grin knife:
        zoom 1.0
    C "Now...{w=0.5} I will make {i}my{/i} move...{nw}"

    menu:
        extend ""
        "Block high":
            Y angry "No you do--" with shakeshort
            window auto hide None
            show bg black
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show cecilia possessed blink at mycenter_closeup with custom_flashquickred()
            show bloodsplatter_5 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with shakeshort
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            Y pained2 "AAAUGHHH!!" with shakeshort
            show cecilia possessed blink at mycenter_return
            I "He cut...my leg..."
        "Block low":
            Y angry "No you don't!" with shakeshort
            window auto hide None
            $ _last_say_who = "C"
            show bg black
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeclash
            show cecilia possessed at mycenter_closeup
            with shakeshort
            C "...Good read."
            show cecilia possessed at mycenter_return
            Y leering "....."
    show cecilia possessed grin knife at mycenter:
        zoom 1.0
        linear 1.0 xalign 0.75
    C "Next...{nw}"

    menu:
        extend ""
        "Try to attack first":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeswing
            show cecilia possessed surprised at mycenter_closeup
            Y shouting "TAKE THIS!!" with shakeshort
            show cecilia possessed surprised at myleft
            play ctc_sfx sfx_whooshlow
            C "HMPH!!" with hpunch
            C possessed thinking "I wasn't expecting that..."
            Y angry "What, are you SCARED?!" with shakeshort
            C possessed grin "Heheh... You're an amusing one..."
        "Run away":
            I "I need some distance...!" with shakeonce
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show cecilia possessed grin knife at mycenter_zoomstill
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with shakeshort
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            Y scream "GAAAAAAGHHH!!" with shakeshort
            show cecilia possessed grin knife at mycenter_return
            C "You are far, {i}far{/i} too slow..."
            if d3a6_duel_hp <= 0:
                jump d3a6_chase_duel_lose
    show cecilia possessed blink at mycenter:
        zoom 1.0
    with move
    C "Now then...{nw}"

    menu:
        extend ""
        "Stab":
            show pov_knife:
                xalign 0.5 yalign 1.0 zoom 0.8
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeswing
            Y shouting "HYA!" with shakeshort
            play ctc_sfx sfx_strikeperson
            hide pov_knife
            show cecilia possessed grin knife at mycenter_zoomstill
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with shakeshort
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            Y shocked "Urgh...!" with shakeonce
            show cecilia possessed at mycenter_return
            C "You're panicking. You may want to calm your mind first."
            if d3a6_duel_hp <= 0:
                jump d3a6_chase_duel_lose
        "Dodge":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeswing
            show cecilia possessed surprised at mycenter_closeup
            Y pained "Hnggghh...!!" with shakelong
            show cecilia possessed thinking at mycenter_return
            C "Interesting... You saw through that...?"
            I "I can do this! I just have to keep--" with vpunch
        "Block":
            show pov_knife:
                xalign 0.5 yalign 1.0 zoom 0.8
            Y leering "...!!" with hpunch
            play ctc_sfx sfx_introkill_6
            hide pov_knife
            show cecilia possessed grin knife at mycenter_zoomstill
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            Y shocked "KUGH...!" with shakeshort
            show cecilia possessed at mycenter_return
            C "You are too relaxed. Keep your guard up."
            if d3a6_duel_hp <= 0:
                jump d3a6_chase_duel_lose

    show cecilia possessed grin knife at mycenter_zoomstill
    Y afraid "A-agh!!{nw}" with shakeshort
    $ fadein_sideimage = False

    menu:
        extend ""
        "PANIC":
            Y afraid2 "GET AWAY!!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show cecilia possessed blink at mycenter_return
            show bloodsplatter_5 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            Y scream "AAAUGHHH!!" with shakelong
            $ fadein_sideimage = True
            C possessed thinking "Where did your courage from earlier go?"
            if d3a6_duel_hp <= 0:
                jump d3a6_chase_duel_lose
        "Slash vertically":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeswing
            Y scream "HYAAAA!!" with shakeshort
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show cecilia possessed surprised at mycenter_return
            show bloodsplatter_5 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            Y pained "...NRGH!!" with shakeshort
            C "Hmph, my wrist is... So you managed to land a hit after all..."
            if d3a6_duel_hp <= 0:
                jump d3a6_chase_duel_lose
        "Block horizontally":
            Y pained "Nrghhh!!" with shakeshort
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeclash
            show cecilia possessed surprised at mycenter_closeup
            with shakeshort
            C "...Impressive."
            show cecilia possessed at mycenter_return
            Y troubled "...*pant*..." with shakeonce
        "Bide your time":
            Y angry "....." with shakeonce
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show cecilia possessed blink at mycenter_return
            show bloodsplatter_5 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            Y scream "AAARRRGHHH!!" with shakelong
            $ fadein_sideimage = True
            C possessed thinking "Should you really be freezing up at a time like this?"
            if d3a6_duel_hp <= 0:
                jump d3a6_chase_duel_lose
    I "I'm...somehow getting through this..." with shakeonce
    KI "This is working! Just a little more!" with vpunch
    C possessed blink "{cps=6}.....{/cps} ...I believe...{w=0.5}it is time to bring this farce to an end."
    play ctc_sfx sfx_heartbeat_single
    Y shocked "{cps=6}.....{/cps} ...Something's coming...{nw}" with shakeonce
    $ fadein_sideimage = False
    $ mute_choice = True

    menu:
        extend ""
        "Block left":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show cecilia possessed
            show bloodsplatter_5 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            $ fadein_sideimage = True
            I "NGH!! Th-there?!" with shakelong
        "Block high":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeclash
            show cecilia possessed
            $ fadein_sideimage = True
            I "NGH!! So fast...!" with shakelong
        "Block right":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show cecilia possessed
            show bloodsplatter_5 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            $ fadein_sideimage = True
            I "NGH!! How did...?!" with shakelong
        "Block low":
            play sound "<silence 1.0>"
            play ctc_sfx sfx_knifeslash
            show cecilia possessed
            show bloodsplatter_5 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            $ fadein_sideimage = True
            I "NGH!! I can't..." with shakelong
    window auto hide None
    show cecilia possessed grin knife at mycenter, shudder:
        zoom 1.0
    pause 0.5
    menu:
        "{size=+10}{font=DejaVuSans.ttf}←{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_3 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "WHAT?!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}↑{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_3 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "STOP!!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}↺{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_3 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "NO!!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}→{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_3 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "H-HOW!!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}↓{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeclash
            window auto show None
            I "AGH?!" with shakeshort
    window auto hide None
    show cecilia possessed grin knife at mycenter_closeup with shakeshort
    menu:
        "{size=+10}{font=DejaVuSans.ttf}↖{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            show cecilia possessed grin knife at mycenter_zoomstill
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "CAN'T...!!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}↷{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            show cecilia possessed grin knife at mycenter_zoomstill
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "URGH!!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}↩{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            show cecilia possessed grin knife at mycenter_zoomstill
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "PLEASE...!!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}↙{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            show cecilia possessed grin knife at mycenter_zoomstill
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "HELP!!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}⇊{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            show cecilia possessed grin knife at mycenter_zoomstill
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            $ fadein_sideimage = True
            window auto show None
            I "WH-WHAT?!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}↱{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            show cecilia possessed grin knife at mycenter_zoomstill
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "H-HOW IS...!!" with shakelong
        "{size=+10}{font=DejaVuSans.ttf}↻{/font}{/size}":
            show cecilia possessed grin knife at mycenter_return
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeclash
            with shakeshort
            show pov_knife at mycenter_to_myleft with custom_flashquick()
            show cecilia possessed grin knife at mycenter_to_myright
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeclash
            with shakelong
            hide pov_knife
            show cecilia possessed grin knife at mycenter_zoomstill
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeclash
            window auto show custom_flashquick()
            I "Nrrrgghhh...!!" with shakeshort
        "{size=+10}{font=DejaVuSans.ttf}↳{/font}{/size}":
            play ctc_sfx "<silence 1.0>"
            play sound sfx_knifeslash
            show bloodsplatter_1 behind cecilia at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            show cecilia possessed grin knife at mycenter_zoomstill
            with custom_flashquickred()
            $ d3a6_duel_hp = d3a6_duel_hp - 1
            window auto show None
            I "NOT LIKE THIS...!!" with shakelong
    $ mute_choice = False
    show cecilia possessed at mycenter_return
    if d3a6_duel_hp <= 0:
        jump d3a6_chase_duel_lose
    stop music fadeout 3.0
    Y troubled "*pant*{cps=2} {/cps}{nw}" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend "*gasp*{cps=2} {/cps}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    extend "...Agh..." with shakeonce
    $ fadein_sideimage = True
    I "...I...{w=0.5} I think it's been about a minute now..." with hpunch
    show cecilia possessed surprised at mycenter:
        zoom 1.0
    C "{cps=6}.....{/cps} ...Impressive."
    if d3a6_duel_hp >= 3:
        achieve KNIFE_DUEL
        play ctc_sfx sfx_emotequestion
        C "You...avoided [t_clue]every single attack[t_cluee]..."
        I "...!" with shakeonce
    else:
        C "You held your ground for this long... You are more skilled than I anticipated..."
        Y shouting "[t_clue]I win[t_cluee], Professor! It's been one minute, and you couldn't corner me!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    C possessed thinking "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    C possessed blink "...Oh. Ohooo... I understand now." with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y shocked "....." with shakeonce
    play ctc_sfx "<silence 1.0>"
    C possessed grin "[name_player]...{w=0.5} You cunning, little...{w=1.0}[t_clue]cheater[t_cluee].{nw}"
    play ctc_sfx "<silence 1.0>"
    play music bgm_tragedy fadein 1.0
    extend "" with shakeonce
    C "You...or maybe I should say Carol-Maria within you...{w=1.0} You can [t_clue]manipulate time freely[t_cluee] now. Am I correct?"
    play ctc_sfx "<silence 1.0>"
    Y afraid "{cps=6}.....{/cps}" with shakeonce
    KI "No... We... W-we overdid it..." with shakeonce
    C possessed blink "Surely you can't expect me to acknowledge your \"victory\" as legitimate."
    C "No, if anything...{w=1.0}you have forfeited this duel."
    Y troubled "....." with shakeonce
    C possessed "Now, as the winner by default, I demand my prize.{w=1.0} You will now give me your wrist shackle without any more resistance.{nw}"

    menu:
        extend ""
        "Stay silent":
            Y shadow2 "{cps=6}.....{/cps}"
            C "{cps=6}.....{/cps}"
            KI "{color=#fff}[input_name]{/color}, wh-wha... What do we do now...?" with shakeonce
        "Agree and surrender":
            Y sad "...All right, I--"
            KI "{color=#fff}[input_name]{/color}! What are you doing?!" with shakeonce
            I "What? We cheated, so we have to--"
            play ctc_sfx sfx_emoteshout
            KI "THIS ISN'T THE TIME FOR FAIR PLAY! YOU COULD DIE HERE!!" with shakeshort
            Y panicked "W-wait, I...don't think it's been a minute yet after all! We need to keep dueling!" with shakeonce
        "Claim you didn't cheat":
            Y angry "Wh-what are you talking about? I fended off your attacks fair and square!" with shakeonce
            $ fadein_sideimage = False
            play ctc_sfx sfx_emoteshout
            Y "You're just mad that you lost, and you're calling me a cheater to get your way!" with shakeshort
            $ fadein_sideimage = True
            play ctc_sfx sfx_emotesigh
            KI "Why are you acting like a kid in a playground...?" with hpunch
    stop music fadeout 3.0
    C "{cps=6}..........{/cps}"
    C "...So it's true. For whatever reason, you're stalling for time."
    play ctc_sfx "<silence 1.0>"
    C "That was the true purpose behind this whole \"duel\", wasn't it?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y troubled "{cps=6}.....{/cps}" with shakeonce
    C "....."
    C possessed blink "I'll take your silence as an affirmation. Very well."
    C possessed "This duel is null and void. I trust you have no complaints about that?"
    I "....."
    C possessed grin "...Now, back to our original arrangeme--{w=1.0}{nw}"
    play ctc_sfx sfx_whooshhigh
    window auto hide
    play sound [sfx_knifeclash, sfx_knifedrop]
    show bg kitchen twoknives
    show cecilia possessed surprised at myright
    with custom_flashquick()
    window auto show None
    C "WHA-- MNGH?!" with shakelong
    hide cecilia
    show bg black
    C "You...threw your knife?! Your friend's face could've been--" with shakeonce
    play ctc_sfx sfx_whooshlow
    $ show_side_cecilia = True
    C possessed surprised "Ah! Get back here!" with shakeshort
    $ show_side_cecilia = False
    play sound sfx_runninglong
    I "That's all the time I can buy! Ria, I hope you have everything ready...!" with shakeonce
    play sound sfx_doorcloseloud
    window auto hide shakeshort
    pause 3.0
    jump d3a6_chase_duel_win

label d3a6_chase_duel_lose:
    play ctc_sfx sfx_heartbeat_single
    stop music fadeout 5.0
    Y depressed stabbed "{cps=12}...Urgh... ...ah...{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    play sound ["<silence 0.4>", sfx_knifedrop]
    I "{cps=6}...I'm...{/cps}{color=#ff0000}finished{/color}..." with shakeonce
    C possessed blink "Hmph. So that's all you're capable of..."
    play sound sfx_wail
    KI "{color=#fff}[input_name]{/color}, we're going back!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    play sound2 sfx_rewind
    scene bg black with pixellate
    pause 1.5
    play ctc_sfx sfx_flashback
    scene bg white with dissolve
    scene bg kitchen twoknives:
        xalign 0.5 yalign 0.5 zoom 2.0
        easein 1.0 zoom 1.0
    with soulin
    pause 1.0
    jump d3a6_chase_duel

label d3a6_chase_duel_win:
    call save_file_name_update (3, "d3a6_chase_finale")
    play sound sfx_runninglong fadein 2.0
    scene bg hallway with dissolveslow
    Y pained2 "*huff*{cps=2} {/cps}{nw}" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend "*pant*{cps=2} {/cps}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    extend pained "R-Ria?!" with shakeshort
    stop sound
    $ fadein_sideimage = True
    I "She said she needed to go upstairs, but where--" with hpunch
    $ show_side_oriana = True
    O hidden "[name_player], this way!" with shakeonce
    $ show_side_oriana = False
    play ctc_sfx sfx_emotequestion
    I "The... The [t_clue]empty bedroom[t_cluee]?" with hpunch
    play sound sfx_running
    scene bg black with dissolve
    play sound2 sfx_dooropen
    scene bg emptybedroom
    show oriana_raw leering at mycenter, backedaway_on
    with dissolve
    Y shocked "Ria, what are you--{w=1.0}{nw}"
    play ctc_sfx sfx_whoosh
    hide oriana_raw
    show bg emptybedroom
    with custom_flashquick()
    scene bg black
    with soulout
    pause 1.0
    window auto hide
    play sound sfx_fallsoft
    pause 5.0
    scene bg emptybedroom at blurred
    show oriana_raw sideeyeblink at myleft, backedaway_on, blurred
    show karma_raw shadow at myright, backedaway_on, blurred
    show eye frame
    with eyeopen_slow
    scene bg black with eyeclose_slow
    scene bg emptybedroom at blurred
    show oriana_raw sideeyeblink at myleft, backedaway_on, blurred
    show karma_raw shadow at myright, backedaway_on, blurred
    show eye frame
    with eyeopen
    scene bg black with eyeclose
    scene bg emptybedroom:
        blur 20.0
        linear 1.0 blur 0.0
    show oriana sideeyeblink at myleft:
        blur 20.0
        linear 1.0 blur 0.0
    show karma shadow at myright:
        blur 20.0
        linear 1.0 blur 0.0
    with eyeopen_quick
    pause 3.0
    I "{cps=6}..........{/cps}"
    I "...Wha...? ...Ria...and...Karma...?" with hpunch
    K "Ria... Are you sure about this?"
    O "It's our only shot at [t_clue]winning[t_cluee]."
    K sad "But your leg..." with shakeonce
    O thinking "I can handle a little stealth. Besides, as long as [name_player] can pull off the last step..."
    YD hidden "Rrgh..." with hpunch
    play ctc_sfx sfx_emotequestion
    I "...! Wh-what? ...\"Rrgh\"...?" with shakeonce
    O surprised "Oh, [name_player], you're awake."
    play ctc_sfx "<silence 1.0>"
    O leering2 "You probably already noticed, but you're in [name_dog]'s body right now." with shakeonce
    play ctc_sfx "<silence 1.0>"
    play music bgm_tension
    YD default "...?! RUFF?!" with shakeshort
    I "I'm...possessing a DOG?!" with shakeshort
    K panicked "It actually worked...!" with hpunch
    O "[name_player], listen carefully. We don't have time to discuss this."
    O "Once Karma and I [t_clue]both grab Cecilia[t_cluee]..."
    O irritated2 "That will be your cue, [name_player], to [t_clue]run out[t_cluee] and pull off her wrist shackle with your teeth."
    I "...! That's..." with shakeonce
    K leering "Okay, I'm heading out!"
    play ctc_sfx sfx_steps
    window auto hide
    hide karma with dissolve
    pause 1.0
    $ _last_say_who = "O"
    show oriana leering at mycenter with move
    O "....."
    YD "...?"
    O thinking "I...{w=1.0} ...Thank you, [name_player]."
    if d3a6_duel_hp >= 3:
        O "You protected Karma from getting even a single scratch...{w=0.5} I can't thank you enough."
    else:
        O "Karma has a couple of cuts and bruises, but...{w=0.5} She's alive, and it's thanks to you."
    YD "....."
    O annoyed2 "This is it, though. We can finally {color=#ff0000}end this game{/color} once and for all." with shakeonce
    play ctc_sfx sfx_heartbeat_single
    O leering2 "Don't lose focus." with shakeonce
    YD "Ruff." with vpunch
    O "....."
    I "...She's staring at me fiercely..."
    YD "...Hrf?"
    O embarrassed "...I-it's nothing. Just...the barking..." with hpunch
    play ctc_sfx sfx_steps
    pause 1.0
    O panicked "Here she-- Er, here he comes! Get ready!" with shakeonce
    stop music fadeout 3.0
    scene bg black with dissolveslow
    pause 1.0

label d3a6_chase_finale:
    scene bg black
    play sound sfx_dooropenslow_move
    scene bg hallwayend withladder with dissolveslow
    I "Okay... So I just gotta [t_clue]wait for my chance[t_cluee] to grab that shackle..."
    window auto hide
    show karma tiredblink at mycenter_fadein with dissolvemed
    pause 1.0
    I "Karma's [t_clue]hiding her arm behind her back[t_cluee]..."
    I "Oh, I get it...!" with shakeonce
    $ show_side_cecilia = True
    play sound sfx_steps
    C hidden "Hmm? You ran into a dead end? I thought you would know this house very well by now."
    K "....."
    $ show_side_cecilia = False
    window auto hide
    show karma tired at mycenter_to_myright
    show cecilia possessed grin at myleft with dissolvemed
    C "But I suppose with this house being an enclosed space, every part of it is a dead end..."
    $ _last_say_who = "K"
    show karma leering at myright_trial with move
    K "I just have one more question for you, Professor."
    C possessed "And what might that be...?{nw}"

    menu:
        extend ""
        "Run out now":
            play ctc_sfx sfx_whoosh
            hide karma
            show cecilia possessed surprised at mycenter
            with custom_flashquick()
            play sound sfx_dogsteps
            YD "RUFF!!" with shakeshort
            $ fadein_sideimage = False
            $ show_side_oriana = True
            $ show_side_karma = True
            O panicked "Wha-- [name_player], WAIT!!" with shakeshort
            $ fadein_sideimage = True
            play ctc_sfx sfx_strike
            show bg black
            show cecilia possessed grin at mycenter_closeup
            with custom_flashquick()
            YD "...?!" with shakeshort
            I "C-crap, he grabbed me!!"
            play ctc_sfx sfx_restrain
            C "I see... So this was your [t_clue]last gambit[t_cluee]..." with hpunch
            C "It is a good plan. It may have even worked if you bided your time just a little--"
            play ctc_sfx "<silence 1.0>"
            play sound sfx_wail
            K scream "GO BAAAACK!!" with shakelong
            $ show_side_oriana = False
            $ show_side_karma = False
            play ctc_sfx "<silence 1.0>"
            play sound2 sfx_rewind
            scene bg black with pixellate
            pause 1.5
            play ctc_sfx sfx_flashback
            scene bg white with dissolve
            scene bg black with soulin
            pause 1.0
            jump d3a6_chase_finale
        "Wait a little longer":
            I "Not yet..." with hpunch
    K thinking "Let's say you keep your promise and let Cece's body go. How do you plan on moving around in the living world?"
    C possessed blink "Naturally, I intend to return to my own body. I've been keeping it well maintained for that purpose."
    $ show_side_oriana = True
    play ctc_sfx "<silence 1.0>"
    O leering "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ show_side_oriana = False
    I "Ria...{w=0.5} She's starting to move...{nw}"

    menu:
        extend ""
        "Run out now":
            play ctc_sfx sfx_whoosh
            hide karma
            show cecilia possessed surprised at mycenter
            with custom_flashquick()
            play sound sfx_dogsteps
            YD "RUFF!!" with shakeshort
            $ fadein_sideimage = False
            $ show_side_oriana = True
            $ show_side_karma = True
            K afraid "[name_player], NO, you have to wait till...!!" with shakeshort
            $ fadein_sideimage = True
            play ctc_sfx sfx_strike
            show bg black
            show cecilia possessed grin at mycenter_closeup
            with custom_flashquick()
            YD "...?!" with shakeshort
            I "C-crap, he grabbed me!!"
            play ctc_sfx sfx_restrain
            C "I see... So this was your [t_clue]last gambit[t_cluee]..." with hpunch
            C "It is a good plan. It may have even worked if you bided your time just a little--"
            play ctc_sfx "<silence 1.0>"
            play sound sfx_wail
            K scream "GO BAAAACK!!" with shakelong
            $ show_side_oriana = False
            $ show_side_karma = False
            play ctc_sfx "<silence 1.0>"
            play sound2 sfx_rewind
            scene bg black with pixellate
            pause 1.5
            play ctc_sfx sfx_flashback
            scene bg white with dissolve
            scene bg black with soulin
            pause 1.0
            jump d3a6_chase_finale
        "Wait a little longer":
            I "Not yet..." with hpunch
    K leering "You consider {i}that{/i}...well-maintained? Your head's wrapped in bandages, and the skin underneath's all rotting and gross."
    play ctc_sfx "<silence 1.0>"
    C "{cps=6}.....{/cps} ...You're not [name_player], are you?"
    play ctc_sfx sfx_heartbeat_single
    K shocked "H-huh?! Wh-what do you mean...?" with shakeshort
    C "Do you think I haven't noticed how you're hiding your arm behind your back?"
    show oriana_raw leering as oriana behind cecilia at myleft_far, backedaway_on:
        alpha 0.0
        linear 0.5 alpha 1.0
    C "Furthermore, you--{w=1.0}{nw}"
    play ctc_sfx sfx_whooshlow
    hide karma
    show oriana annoyed2 at myleft, backedaway_off:
        alpha 1.0
    show cecilia possessed surprised at mycenter
    with custom_flashquick()
    play music bgm_chase
    $ show_music_info_timer = music_info_pop_out_time()
    extend " HMM?!" with shakeshort
    O shouting "Got you!" with shakeshort
    $ show_side_karma = True
    play ctc_sfx sfx_knifebrandish
    show cecilia possessed grin knife
    K afraid "Ah! Ria, watch out for the knife!" with shakeshort
    $ show_side_karma = False
    play sound sfx_restrain
    show cecilia possessed surprised
    O injured "Hnnghh!!" with shakelong
    C "Mrgh...!{w=0.5} Hmph, so you still have some strength left in you, eh...?{nw}"

    menu:
        extend ""
        "Run out now":
            play ctc_sfx sfx_whoosh
            with custom_flashquick()
            play sound sfx_dogsteps
            YD "RUFF!!" with shakeshort
            O horrified "Ah-- [name_player] wait--{w=0.5}{nw}" with shakeonce
            play ctc_sfx sfx_introkill_6
            show bg black
            show oriana stabbed at myleft_far
            show cecilia possessed grin knife at myleft
            show bloodsplatter_4 behind oriana at truecenter:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            extend " KURRGGHHH!" with shakelong
            $ show_side_karma = True
            K afraid "RIA!!" with shakeshort
            show oriana injured at crouch
            window auto hide
            show cecilia possessed at mycenter, shudder
            C "Hmm?"
            hide oriana
            show cecilia possessed grin at mycenter:
                zoom 1.5
            YD "...!!" with shakeonce
            play ctc_sfx sfx_whooshhigh
            pause 0.2
            play sound sfx_strike
            hide cecilia
            with custom_flashquick()
            YD "*whine*" with shakelong
            play ctc_sfx sfx_strikeperson
            window auto hide shakeonce
            scene bg black
            pause 0.2
            play sound sfx_fallhard
            with shakelong
            I "Ugh... He...kicked me... I can't..." with shakeshort
            K depressed "No... [name_player]..." with shakeonce
            $ _last_say_who = "C"
            show cecilia possessed grin at mycenter_closeup with dissolve
            C possessed grin "So {i}that{/i} was your plan, hmm?"
            C "You almost had me there! If only you had someone without an injured arm to grab--" with vpunch
            play ctc_sfx "<silence 1.0>"
            play sound sfx_wail
            K scream "GO BAAAAAAAAACK!!" with shakelong
            $ show_side_karma = False
            play ctc_sfx "<silence 1.0>"
            play sound2 sfx_rewind
            stop music fadeout 3.0
            scene bg black with pixellate
            pause 1.5
            play ctc_sfx sfx_flashback
            scene bg white with dissolve
            scene bg black with soulin
            pause 1.0
            jump d3a6_chase_finale
        "Wait a little longer":
            I "Ngh... N-not yet..." with hpunch
    play ctc_sfx sfx_restrain
    show oriana injured at mycenter
    show cecilia possessed surprised at myright
    O "Just...give it up...!" with hpunch
    play ctc_sfx sfx_restrain
    show oriana injured at myleft_far
    show cecilia possessed grin at myleft
    C "You're a stubborn one, aren't you...?" with shakeshort
    play ctc_sfx sfx_whooshlow
    show oriana injured at myright
    show cecilia possessed grin at myright_far
    O "I...won't let go! Karma, quick!" with shakelong
    play ctc_sfx sfx_whooshlow
    show oriana injured at myleft_far
    show cecilia possessed grin at myleft
    C "You forget that this girl's legs are also powerful." with shakelong
    play ctc_sfx sfx_whooshlow
    show oriana panicked
    show cecilia possessed at mycenter
    show karma_raw shadow as karma behind cecilia at myright_fadein, backedaway_on
    C "I can shake you off, just like--{w=1.0}{nw}" with shakeshort

    play ctc_sfx sfx_strike
    play sound sfx_restrain
    hide oriana
    show karma pained behind cecilia at myright_trial, backedaway_off
    show cecilia possessed surprised at myright
    with custom_flashquick()
    extend " UWAH!!" with shakeshort
    K "You're not...getting away...!" with shakeshort
    I "She...grabbed her waist and [t_clue]one of her legs[t_cluee]?!" with shakeonce
    play ctc_sfx sfx_restrain
    C "Ngh... This is less than ideal...{nw}" with shakeshort

    menu:
        extend ""
        "Run out now":
            play ctc_sfx sfx_whoosh
            with custom_flashquick()
            play sound sfx_dogsteps
            YD "RUFF!!" with shakeshort
            play ctc_sfx sfx_knifebrandish
            show cecilia possessed grin knife at mycenter_closeup
            K afraid "[name_player]! WAIT!! DON'T--{w=1.0}{nw}" with shakeshort
            play ctc_sfx sfx_introkill_5
            window auto hide None
            scene bg black
            show bloodsplatter_5 at truecenter:
                alpha 1.0
                linear 5.0 alpha 0.0
            show stab censor:
                alpha 1.0
                linear 3.0 alpha 0.0
            with custom_flashquickred()
            window auto show None
            YD hidden "...!!! *whine*" with shakelong
            play ctc_sfx "<silence 1.0>"
            window auto hide None
            play sound sfx_fallhard
            scene bg black
            show bloodsplatter_2 at truecenter:
                alpha 1.0
                easein 3.0 alpha 0.0
            with shakelong
            pause 1.0
            I "{cps=12}...I...messed up...{/cps}"
            $ show_side_oriana = True
            O horrified "NOOOOOO!!!" with shakeshort
            $ show_side_oriana = False
            $ _last_say_who = "C"
            show cecilia possessed grin at mycenter_closeup with dissolve
            C possessed grin "So {i}that{/i} was your plan, hmm? [name_player] is possessing the dog?"
            C "How FOOLISH of you to charge at me when my knife arm is still free--" with vpunch
            play ctc_sfx "<silence 1.0>"
            play sound sfx_wail
            $ show_side_karma = True
            K scream "GO BAAAAAAAAACK!!" with shakelong
            $ show_side_karma = False
            play ctc_sfx "<silence 1.0>"
            play sound2 sfx_rewind
            stop music fadeout 3.0
            scene bg black with pixellate
            pause 1.5
            play ctc_sfx sfx_flashback
            scene bg white with dissolve
            scene bg black with soulin
            pause 1.0
            jump d3a6_chase_finale
        "Wait a little longer":
            I "Not yet... NOT YET...!" with shakeshort
    play ctc_sfx sfx_knifebrandish
    C possessed grin knife "But you realize that I can still stab you{cps=5}... ...{/cps}{nw}" with hpunch
    play ctc_sfx sfx_knifeswing
    show bg black
    show oriana_raw shouting as oriana behind cecilia at mycenter, backedaway_on
    show karma afraid behind cecilia at myright_far
    with custom_flashquick()
    extend "RIGHT--{w=1.0}{nw}" with shakeshort
    play ctc_sfx sfx_introkill_6
    window auto hide None
    scene bg black
    show bloodsplatter_1 at truecenter:
        alpha 1.0
        linear 5.0 alpha 0.0
    show oriana injured at myleft, backedaway_off
    show cecilia possessed surprised at mycenter
    show karma pained behind cecilia at myright
    with custom_flashquickred()
    window auto show None
    O "NRGHHH!!!" with shakelong
    I "Ria...[t_clue]took the knife into her shoulder[t_cluee]...?!" with shakeshort
    K afraid "RIA!!" with shakeshort
    C "Have you lost your mind?! You--" with shakeshort
    play ctc_sfx sfx_restrain
    C "Nggghhh!! Let go of my arm!!" with hpunch
    O "You...[t_clue]can't use your knife[t_cluee] like this...!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ renpy.music.set_volume(0.25, 0, channel="music")
    $ renpy.music.set_volume(1.0, 2, channel="music")
    play loop_sfx sfx_heartbeat
    I "...!!!" with shakeshort
    play ctc_sfx sfx_strikeperson
    C "UNHAND ME, BOTH OF YOU!!" with shakeshort
    play ctc_sfx sfx_strikeperson
    K pained2 "Krgh!! ...Your [t_clue]left hook[t_cluee]...doesn't hurt at all!!" with shakeshort
    play ctc_sfx sfx_strikeperson
    O "[name_player]!!!{w=0.5}{nw}" with shakelong

    menu:
        extend ""
        "Run out now":
            stop music
            stop loop_sfx
            play ctc_sfx sfx_whoosh
            show bg white
            with custom_flashquick()
            YD "RUFF!!" with shakeshort
            C "Wha-- YOU?!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            show cecilia possessed surprised at mycenter_closeup
            hide karma
            hide oriana
            play sound sfx_dogsteps
            $ show_side_karma = True
            $ show_side_oriana = True
            K scream "[name_player], now!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = False
            O shouting "IT'S OVER!!" with shakeshort
            play ctc_sfx "<silence 1.0>"
            $ show_side_karma = False
            $ show_side_oriana = False
            $ fadein_sideimage = True
            show cecilia possessed surprised at mycenter_zoomstill
            play sound sfx_dogsteps
            I "THE KILLING GAME {color=#ff0000}ENDS HERE!!{/color}" with shakeshort
            play ctc_sfx "<silence 1.0>"
            C "{cps=9}...No...{/cps}{w=0.5} {cps=9}...I was...{/cps}{w=1.0}{nw}"
            play ctc_sfx "<silence 1.0>"
            window auto hide None
            scene bg black
            window auto show custom_flashquick()
            C "{cps=18}{size=+10}NOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!{/size}{/cps}" with shakelong
            play ctc_sfx "<silence 1.0>"
            show screen lock_hotkeys
            $ quick_menu = False
            $ music_info = False
            play sound sfx_whoosh
            with custom_flashquick()
            show bg white
            with soulout
            window auto hide dissolveslow
            $ renpy.pause(5.0, hard=True)
            scene bg black with dissolveslow
            hide screen lock_hotkeys
            $ quick_menu = True
            $ music_info = True
            pause 3.0
        "Wait a little longer":
            I "Not yet... NOT--{w=1.5}{nw}" with shakeshort
            window auto hide None
            stop music
            stop loop_sfx
            play ctc_sfx sfx_whooshhigh
            play sound sfx_introkill_6
            play sound2 sfx_introkill_5
            scene bg black
            show bloodsplatter_2 at truecenter:
                alpha 1.0
                linear 5.0 alpha 0.0
            show bloodsplatter_5 at truecenter:
                alpha 1.0
                linear 5.0 alpha 0.0
            show oriana stabbed at myleft_far:
                alpha 1.0
                pause 5.0
                linear 3.0 alpha 0.0
            show karma depressed stabbed at myright_far:
                alpha 1.0
                pause 5.0
                linear 3.0 alpha 0.0
            show bloodsplatter_1 at truecenter:
                alpha 1.0
                linear 5.0 alpha 0.0
            show cecilia possessed grin knife at mycenter, shudder
            show cecilia_raw possessed grin knife at mycenter_closeup:
                alpha 1.0
                easein 1.0 alpha 0.0
            with custom_flashquickred()
            window auto show None
            C "[u_music_note]~" with shakelong
            play ctc_sfx "<silence 1.0>"
            window auto hide
            hide oriana
            hide karma
            with dissolvemed
            show bloodsplatter_1 at truecenter:
                alpha 1.0
                linear 2.0 alpha 0.0
            play sound sfx_fallhard
            play sound2 sfx_fallsoft
            with shakeshort
            pause 3.0
            I "{cps=6}.......... ...No...{/cps}"
            play ctc_sfx "<silence 1.0>"
            show cecilia possessed grin knife at mycenter_closeup
            C "Now I am left wondering... For what purpose were they trying to [t_clue]hold me down[t_cluee] for...?"
            play ctc_sfx "<silence 1.0>"
            play sound sfx_wail
            $ show_side_karma = True
            K depressed stabbed "{cps=9}...Go...ba...ack...{/cps}"
            $ show_side_karma = False
            play ctc_sfx "<silence 1.0>"
            play sound2 sfx_rewind
            stop music fadeout 3.0
            scene bg black with pixellate
            achieve GAMBIT_LOSE
            pause 1.5
            play ctc_sfx sfx_flashback
            scene bg white with dissolve
            scene bg black with soulin
            pause 1.0
            jump d3a6_chase_finale
label d3a7:
    call save_file_name_update (3, "d3a7")
    scene bg black
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.......{/cps} ...Finally..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}It's...finally over...{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 2.0
    play sound [sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime]
    pause 3.0
    scene bg basement:
        xalign 0.0 yalign 0.6 zoom 1.6
        easein 10.0 zoom 1.5
    with dissolveslow
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}...This...{/cps}has been a long journey..."
    scene bg basement:
        xalign 0.0 yalign 0.6 zoom 1.5
    show oriana thinking at myleft_fadein
    show karma tiredblink at myright_fadein
    with dissolveslow
    pause 3.0
    O "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    K "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    YD "{cps=6}.....{/cps}"
    I "...I kinda thought the vibe would be happier..." with hpunch
    O "{cps=6}.......{/cps}"
    K shadow "{cps=6}..........{/cps}{w=1.0}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend " *sniff*" with shakeonce
    play ctc_sfx "<silence 1.0>"
    O surprised "...Karma?" with shakeonce
    play ctc_sfx "<silence 1.0>"
    play music bgm_relaxed
    K crying "I'm... I'm so glad... I never gave up..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    K "I spent...so much time wishing one of us would die already. ...Much more time than I did for the opposite..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    K crying2 "I...{w=0.5} I honestly think this moment is just a dream...{w=1.0} A fleeting fantasy to momentarily distract me from..." with shakeonce
    O blink "{cps=6}.....{/cps} ...This isn't a dream, Karma.{w=0.5} This is real."
    O confident "We...ended the killing game.{w=0.5} Ended your neverending nightmare."
    K "It's thanks to you guys! You...and [name_player]..." with shakeonce
    K crying "Ria, you...you got so many injuries... It's amazing that you can still stand tall..." with shakeonce
    O sideeyeblink "...This is nothing compared to what you had to go through."
    play ctc_sfx sfx_heartbeat_single
    K crying2 "....." with shakeonce
    O relaxed "Heh. It's just like you, though.{w=0.5} To go through an endless cycle of torment just because you couldn't ever possibly give up on us..."
    O confident "You truly are an [t_clue]idiot[t_cluee], through and through."
    play ctc_sfx sfx_emotesigh
    K crying2 "*sniffle* Riiiaaa..." with hpunch
    O relaxed "But we're all here now only because you hung in there. You brought [name_player] to us."
    O "And your [t_clue]stubbornness[t_cluee] combined with [name_player]'s deductions brought us to this: the [t_clue]best possible ending[t_cluee]."
    play ctc_sfx sfx_emotehappy
    YD "*nods*" with vpunch
    K "Ria... [name_player]..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    K tiredblink "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    hide oriana with dissolve
    show karma tiredblink at myright:
        easein 2.0 xalign 0.5
    pause 2.0
    K tired "I'm...an [t_clue]idiot[t_cluee] so...I don't know what words I could say to express just how grateful and relieved I am..."
    K crying2 "I was so convinced that there were no endings to this game without one of us dying... Without regret and suffering..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    window auto hide
    pause 1.0
    $ renpy.music.set_volume(0.25, 2, channel="music")
    show bg black
    show karma overjoyed at mycenter
    with dissolvemed
    play sound sfx_shardobtain
    show backshards_1 behind karma at blurring:
        alpha 0.45
    show backshards_2 behind karma at blurring:
        alpha 0.55
    show backshards_3 behind karma at blurring:
        alpha 0.65
    show backshards_4 behind karma at blurring:
        alpha 0.75
    with custom_flashbulb()
    $ renpy.pause(2.0, hard=True)
    K "{cps=12}Thank you...{/cps}{w=1.0}{cps=24}for bringing me to the {color=#cccc00}best possible ending{/color}.{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "....."
    play ctc_sfx sfx_emotehappy
    YD "RUFF~ [u_music_note]" with vpunch
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O happy "....."
    $ show_side_oriana = False
    $ fadein_sideimage = True
    $ renpy.music.set_volume(1.0, 2, channel="music")
    scene bg black with dissolveslow
    scene bg basement:
        xalign 0.0 yalign 0.6 zoom 1.5
    with dissolveslow
    $ name_cecilia = _("Cece")
    $ show_side_cecilia = True
    C sad "Mrgh..."
    $ show_side_cecilia = False
    window auto hide
    play sound sfx_clothrustle volume 0.5
    with hpunch
    pause 1.0
    show cecilia injured at mycenter with dissolvemed
    play sound sfx_emotequestion
    pause 0.5
    C "Hurgh...?{w=0.5} An unfamiliar ceiling...?"
    C surprised "...Wha... Why is [name_player] crying...?" with hpunch
    $ show_side_oriana = True
    O panicked "Cecilia! Are you all right?!" with shakeshort
    $ show_side_oriana = False
    play ctc_sfx sfx_emotesigh
    show cecilia sweatdrop at shrink
    C "Huh? I mean, I feel sore in a ton of places."
    show cecilia smug at shudder
    C "GASP?! Wait, did you guys do something to my sleeping body?!"
    play ctc_sfx sfx_whooshlow
    show cecilia surprised at myright
    show oriana injured behind cecilia at mycenter
    with custom_flashquick()
    play sound sfx_strike
    C "Awawawawawawa!" with hpunch
    O "....." with shakeonce
    C "Whoa! I, uh... A-are you okay, Ria?{w=1.0} You've never been so--{w=1.0}{nw}" with shakeonce
    play ctc_sfx sfx_punch
    show cecilia sobbing at crouchquick
    show oriana irritated at myleft, hop
    with custom_flashquick()
    extend sobbing " BWAAAH-IOLENT MOOD SWINGS?!" with shakelong
    play ctc_sfx sfx_emoteshout
    O shouting "YOU BLUE IMBECILE!" with shakeshort
    show cecilia injured at myright
    C "Ow... Wh-why, what did I--" with hpunch
    play ctc_sfx "<silence 1.0>"
    O injured "You let yourself get possessed by a spirit...{w=0.5} [name_player] could have died..."
    C surprised "E-eh? What? Wait, hang on, I'm SO confused!" with shakeonce
    C thinking "Last I remember, [name_player] took you to the bedroom, and I was in the attic reading about--"
    stop music fadeout 3.0
    $ show_side_karma = True
    K panicked "G-guys! The Professor, he's..." with shakeshort
    C surprised "Th-the Professor?!" with hpunch
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}...Well done.{/cps}"
    O leering2 "....." with shakeonce
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    hide cecilia
    hide oriana
    with dissolvemed
    $ _last_say_who = "V"
    scene bg basement nocorpse:
        xalign 0.0 yalign 0.6 zoom 1.3
        easein 4.0 zoom 1.0
    with dissolvemed
    pause 2.0
    show villain exposed at mycenter_fadein
    with dissolveslow
    play music bgm_sad
    $ show_music_info_timer = music_info_pop_out_time()
    pause 3.0
    $ show_side_oriana = True
    $ show_side_cecilia = True
    show bg basement nocorpse:
        zoom 1.0
    V "...You have overcome the odds...{w=0.5}and brought an end to my game."
    V "{cps=6}.....{/cps} ...Congratulations.{w=0.5} Truly."
    play ctc_sfx "<silence 1.0>"
    I "...Professor..." with shakeonce
    show villain exposed at shudder
    V "...Hmm? Why did you remove my bandages?"
    O blink "I wanted to confirm it. Confirm that you really are the man in the lounge's photos."
    V "Of course I am. Why would you think otherwise?"
    play ctc_sfx "<silence 1.0>"
    O injured "Because...{cps=2} {/cps}This would be easier if you weren't." with shakeonce
    $ fadein_sideimage = False
    K sad "....."
    $ fadein_sideimage = True
    V "...You mean [t_clue]sending me to Hell[t_cluee]?"
    O dejected "You and your family...{cps=2} {/cps}What happened to you all was a tragedy."
    $ fadein_sideimage = False
    O shadow "And even if you're a heinous criminal who slaughtered a countless number of innocent people..."
    O troubled "...You suffered through it all. You never wanted to do any of those horrible things..." with shakeonce
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}.....{/cps}"
    O injured "I...don't know what to believe..." with shakeonce
    $ fadein_sideimage = False
    O "As a criminal, you must be punished, but..."
    O "The [t_clue]purpose of a punishment[t_cluee]...{w=1.0} Isn't it to get them to understand where they went wrong, and guide them to a better path?"
    play ctc_sfx "<silence 1.0>"
    O crying "But...you know what you did wrong.{w=0.5} And the path you were walking... Was it really so terrible...?" with shakeonce
    $ fadein_sideimage = True
    I "...Ria...?"
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}.....{/cps} ...You are gravely mistaken, child."
    V "I am a madman blinded by my wicked ambition to cheat the rules of life and death. My motivations are impure."
    V "To put a stop to the havoc wreaked by a twisted, self-serving demon{cps=6}... ...{/cps}That is not punishment.{w=1.0} That is [t_clue]justice[t_cluee]."
    K crying "....." with shakeonce
    $ fadein_sideimage = False
    O injured "...Don't talk to me about \"justice\"..."
    $ fadein_sideimage = True
    V "....."
    O irritated2 "\"Justice\" would've been never allowing you on your path in the first place."
    $ fadein_sideimage = False
    O "This...blood-soaked path...that runs for an eternity before you could ever reach your goal..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    O leering "\"Justice\" would've been if God had struck you down before ever allowing you to get this far!" with shakeshort
    $ fadein_sideimage = True
    V "....."
    play ctc_sfx "<silence 1.0>"
    O injured "And now...all that blood was spilled for nothing... Because of ordinary people like us..."
    $ fadein_sideimage = False
    O "People who were ready and willing to partake in a [t_clue]killing game[t_cluee]..." with shakeonce
    O "What right do we have to judge you?! What right do we have to {color=#ff0000}send you to Hell{/color} just for our own sakes?!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    I "....." with shakeonce
    $ fadein_sideimage = True
    V "...You are young, so I shall forgive your naivete. For you see..."
    play ctc_sfx sfx_heartbeat_single
    V "Concepts like God or justice care not of human affairs and emotions. They are [t_clue]beyond mortal comprehension[t_cluee]." with shakeonce
    V "The right to condemn others can never truly be earned. It can only be appropriated by those who have a life to [t_clue]protect[t_cluee]."
    O afraid "...!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    V "{color=#ff0000}I no longer have any life to protect.{/color}{w=0.5} Conversely, {i}you{/i} have your own and more.{w=0.5} You have every right to pass judgement on me."
    V "You must not allow your immense aptitude for empathy steer you away from your [t_clue]duty[t_cluee] to yourself and your fellow mortals."
    O injured "That's... That's not...what..." with shakeonce
    V "...I lost the last of my humanity the moment this body perished. You are misguided to believe I am worthy of mercy."
    play ctc_sfx sfx_heartbeat_single
    O horrified "YOU'RE WRONG!! YOU--" with shakelong
    $ fadein_sideimage = False
    play ctc_sfx sfx_strike
    with custom_flashquick()
    K scream "RIA, STOP!" with shakeshort
    O afraid "N-no... He's...wrong..." with shakeonce
    K crying2 "Stop...[t_clue]playing dumb[t_cluee] already..."
    play ctc_sfx "<silence 1.0>"
    O shadow "{cps=6}.....{/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend crying " ...Kgh..." with shakeonce
    $ fadein_sideimage = True
    V "You know nothing of my life, child. And that is how it should be."
    V "Why burden yourself with the history of a killer? The history of a restless, ageless specter?"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}..........{/cps}" with shakeonce
    V "Now go on. Send this wretched wraith to the depths where it belongs, and return to your world of light."
    YD "Ruff."
    $ fadein_sideimage = False
    K panicked "Huh...? [name_player]?" with hpunch
    play ctc_sfx "<silence 1.0>"
    YD "....."
    K surprised "....."
    K tired "...You want to talk to him, don't you?"
    play ctc_sfx "<silence 1.0>"
    YD "....." with vpunch
    K "Okay, come here."
    play ctc_sfx "<silence 1.0>"
    K tiredblink "....."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    scene bg black with soulout
    pause 1.0
    scene bg basement nocorpse
    with dissolvemed
    show villain exposed at mycenter_fadein
    with dissolvemed
    Y blink "....."
    $ fadein_sideimage = False
    Y default "Professor."
    $ fadein_sideimage = True
    V "Hmm? ...You're [name_player], aren't you?"
    Y "I just have one question for you."
    V "Hm. By all means, let's hear it.{nw}"

    menu:
        extend ""
        "\"Why did you give Karma {i}my{/i} shackle?\"":
            Y thinking "Why did you give me... Give Karma my shackle?"
            V "I believe I have already explained that. It was an attempt to curb her time travel pow--"
            play ctc_sfx sfx_emotequestion
            Y leering "No, I mean... Why {i}me{/i}?{cps=2} {/cps}Why didn't you simply [t_clue]use your own shackle[t_cluee] to take control of her?"
        "\"Why did you keep my shackle at all?\"":
            Y thinking "You said that you only needed one more soul to feed the Gate before you could escape this house..."
            play ctc_sfx sfx_emotequestion
            $ fadein_sideimage = False
            Y default "But then... Why didn't you just throw me into the Gate [t_clue]from the start[t_cluee]? Why did you wait until the Occult Club showed up?"
            $ fadein_sideimage = True
    V "...!" with shakeonce
    Y blink "You...{cps=2} {/cps}You could've prevented all of this from happening.{cps=2} {/cps}Escaped the house so much sooner."
    $ fadein_sideimage = False
    Y sad "And when you gave my shackle to Karma, you could've predicted things would turn out this way.{w=1.0} So why take that risk?"
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}.....{/cps}" with shakeonce
    V "...Yes... Why indeed...?"
    Y surprised "...?"
    V "Forgive me, but let me ask you something first."
    V "{cps=6}.....{/cps} ...Is your name truly \"[name_player]\"?"
    I "My name..."
    if input_name_true == input_name:
        Y default "Yes. [name_player_true] is in fact my real name."
    else:
        Y default "No. My real name is...{cps=1} {/cps}[name_player_true]."
    V "[name_player_true]..."
    V "....."
    Y surprised "Professor...?"
    V "...Heh. I suppose the chances were practically non-existent."
    V "You had lost all memories of your life. Including the memory of your own name. So I thought..."
    V "Maybe if you were in a healthy girl's body...{w=1.0} Maybe if you wandered this house on your own two feet, you would remem..."
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    O depressed "{cps=6}.......{/cps} ...You thought..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps}{w=0.5}{nw}"
    play ctc_sfx sfx_heartbeat_single
    extend " ...!!!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}.....{/cps} ...I suppose it no longer matters. And now, it never will..."
    play ctc_sfx "<silence 1.0>"
    Y depressed "{cps=6}...You...{/cps}" with shakeonce
    V "To answer your question..."
    V "I suppose...deep down, I wished to be stopped."
    V "There were still so many more theories I could test... And without a human lifespan to limit me, I could test every last one..."
    V "But...{w=0.5}the [t_clue]possibility of failure[t_cluee] haunted me. The possibility that I embarked on this hellish, unending path for naught..."
    play ctc_sfx "<silence 1.0>"
    V "And now, I shall never know...{w=0.5} What a blessing this truly is..."
    play ctc_sfx "<silence 1.0>"
    Y troubled "{cps=6}.....{/cps}" with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    O crying2 "{cps=6}.......{/cps}" with shakeonce
    $ fadein_sideimage = True
    V "If that is all, then let this be where I bid you all farewell."
    V "I...am very tired."
    V "Let the flames of {color=#ff0000}Hell{/color} consume me so that it may finally all end."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}..........{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    stop music fadeout 3.0
    scene bg black with dissolveslow
    pause 1.0
    scene bg basement hatch with dissolveslow
    I "...He's...really going in voluntarily..."
    I "I suppose...it's so his body can finally rest too..."
    scene bg basement nocorpse
    show villain exposed at mycenter_fadein
    with dissolvemed
    pause 1.0
    V "...Hmm...{w=0.5} I just realized...I have some final words to say..."
    play ctc_sfx sfx_emotequestion
    V "...To Oriana."
    O dejected "....."
    V "...You appear lost in thought. Very well, I shall speak without requiring you to listen."
    V "When you protected [name_player], and forced me to confront the very nature of my own insanity..."
    V "I felt...as though I was [t_clue]saved[t_cluee] by your words."
    O shadow "....." with shakeonce
    V "I am now moments away from a second, truer death... And yet, I do not tremble."
    V "You have given me new power... The strength to end my own curse... My own endless torment..."
    V "I fear no amount of words will be sufficient to express my gratitude...{w=1.0} I...wonder if this is what [t_clue]salvation[t_cluee] feels like...?"
    play ctc_sfx sfx_heartbeat_single
    O troubled "...!!!" with shakelong
    $ fadein_sideimage = False
    O "...Professor. You're..." with shakeonce
    O injured "...You're...a hopeless, complete and utter [t_clue]FOOL[t_cluee]."
    $ fadein_sideimage = True
    V "...Hm?"
    O irritated2 "If your daughter truly was the precious little [t_clue]angel[t_cluee] as you wrote in your journal..." with shakeonce
    $ fadein_sideimage = False
    play ctc_sfx sfx_heartbeat_single
    O troubled "Then why... WHY would you search for her by making a gate to HELL?!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    O crying "...Don't you think...she would have gone to [t_clue]Heaven[t_cluee]?!" with shakeshort
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    show bg black
    with custom_flashquick()
    V "...!!!" with shakelong
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    V "{cps=6}..........{/cps}{nw}"
    play ctc_sfx sfx_emotehappy
    extend smile " ...Heh." with shakeonce
    play ctc_sfx "<silence 1.0>"
    V "Hehehe... Heh HEH..." with shakeshort
    play ctc_sfx [sfx_emoteshout, "<silence 0.4>", sfx_emoteshout, "<silence 0.4>", sfx_emoteshout]
    with custom_flashquick()
    play sound ["<silence 0.2>", sfx_emoteshout, "<silence 0.4>", sfx_emoteshout, "<silence 0.4>", sfx_emoteshout]
    play music bgm_relaxed
    V laugh "{size=+10}BWAHAHAHAHAHAHAHAHAHAHAAAAA!!{/size}{w=0.5}{nw}" with shakelong
    play ctc_sfx [sfx_emoteshout, "<silence 0.1>", sfx_emoteshout]
    with custom_flashquick()
    extend "" with shakelong
    C surprised "ACK!! That was...loud..." with hpunch
    $ fadein_sideimage = False
    O crying2 "*sniff* ....." with shakeonce
    $ fadein_sideimage = True
    KI "Ria..."
    play ctc_sfx sfx_emotehappy
    V smile "You truly are brilliant. I would have loved to have you as one of my students." with vpunch
    V "A remarkably intelligent young woman with the mightiest convictions I've ever witnessed..."
    V "...is now offering solaces to a villain that recently tried to murder her.{w=1.0} You are astounding, young Oriana."
    O crying "{cps=3}.......{/cps}" with shakeonce
    V "\"Heaven\"...{w=1.0} Yes...{w=1.0} Yes, I suppose that must be where she has been all this time..."
    play ctc_sfx "<silence 1.0>"
    V "{cps=9}I...hope she is well...{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    hide villain with dissolveslow
    play loop_sfx sfx_flameloop fadein 3.0
    scene bg white with dissolvemed
    pause 0.5
    scene bg flamewall:
        matrixcolor BrightnessMatrix(0.25) * SaturationMatrix(0.0)
    with dissolveslow
    pause 1.0
    I "{cps=6}..........{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=9}...Goodbye... Professor...{/cps}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ show_side_oriana = False
    $ show_side_cecilia = False
    $ show_side_karma = False
    stop music fadeout 5.0
    scene bg black with dissolveslow
    stop loop_sfx fadeout 5.0
    pause 5.0
label d3a8:
    call save_file_name_update (3, "d3a8")
    scene bg black
    scene bg frontdoor open:
        xalign 0.5 yalign 0.5 zoom 1.5
        easein 20.0 zoom 1.0
    with dissolveslow
    pause 1.0
    I "{cps=6}.....{/cps}"
    I "So...{w=1.0} This is how it ends..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.....{/cps} ...For [t_clue]real[t_cluee] this time...{nw}"
    play ctc_sfx "<silence 1.0>"
    play music bgm_victory
    $ show_music_info_timer = music_info_pop_out_time()
    extend ""
    $ _last_say_who = "C"
    scene bg foyer
    show cecilia thinking at mycenter
    with dissolveslow
    pause 1.0
    C "I see... A lot happened while I was under his control, huh...?"
    $ _last_say_who = "K"
    show cecilia thinking at mycenter_to_myright
    pause 0.3
    show karma tiredblink at myleft with dissolve
    K "He really had us all fooled."
    K sad "If [name_player] hadn't stopped us to question the whole situation..."
    show cecilia overjoyed at myright, hop
    show karma panicked at myleft
    play ctc_sfx sfx_emotehappy
    C overjoyed "Being possessed by a ghost is like, the DREAM, though~" with vpunch
    C sobbing "Man, I wish I could remember it more clearly..."
    $ _last_say_who = "O"
    show karma worried at mycenter
    show cecilia sobbing at myright_far
    with move
    show oriana annoyed at myleft_far with dissolve
    O "Of course that's your main comment." with shakeonce
    C default "Oh yeah, [name_player]! What does a dog's body feel like? Your heart beats faster, right?"
    YD "Ruff."
    play ctc_sfx sfx_emotesigh
    C sweatdrop "...Ah yeah, I guess you can't talk while you're--" with hpunch
    play ctc_sfx "<silence 1.0>"
    K panicked "W-wait, [name_player], say that again?" with shakeonce
    YD "...Ruff?"
    K surprised "...\"It's a corpse, so the heart doesn't beat at all.\""
    O panicked "Wha--" with shakeonce
    play ctc_sfx sfx_emotequestion
    C surprised "HUH?! K-Karma, you can understand dogs?!" with shakeonce
    K sweatdrop "Ah-- Er, no, it's more like I can kinda feel what [name_player]'s soul is trying to express...?" with hpunch
    C happy "Ooooh. Makes sense; you two have been sharing a body for quite a while now."
    C smile "I wonder if that carries over even back in the living world."
    O thinking "....."
    K panicked "Ah..."
    I "...The living world..."
    I "That's right... I'm not alive anymore..."
    I "Do I deserve to leave this place when...the Professor had to..."
    K blink "[name_player]. Don't think about that."
    play ctc_sfx "<silence 1.0>"
    YD "...! Ruff?!" with shakeonce
    K default "Yep. You don't even have to bark. I can still [t_clue]hear your thoughts[t_cluee]."
    K "Ria wanted to save you, so I took your shackle and lent you my body, remember?"
    K blink "And through one way or another, we prevented you from getting sacrificed."
    K happy "Now [t_clue]the choice is yours[t_cluee]. What will you do with the life we fought to preserve?"
    YD "....."
    play ctc_sfx sfx_emotehappy
    show cecilia happy at hop
    C "Isn't the choice obvious? [name_player], you should [t_clue]escape with us[t_cluee]!"
    C overjoyed "You could be the official Occult Club mascot! I mean, nothing's more perfect than a dog without a heartbeat!"
    O blink "...I think [name_player] might be considering staying behind."
    show karma surprised
    C surprised "What?! Why?!" with shakeonce
    O confused "The Professor and [name_player]... Both of them were bound to shackles. Both were souls meant to go to Hell."
    O irritated "And though the Professor committed many atrocities to escape this house, he ultimately couldn't."
    O thinking "Because WE made the decision to sacrifice him instead of [name_player]."
    K sad "....."
    O irritated "Does [name_player] truly deserve to return to the world of the living instead of the Professor..."
    O "...simply because of the feelings of outsiders like us?"
    C thinking "I think we might be overthinking this. I mean, if [name_player] stays behind, that's the same as [t_clue]choosing to die[t_cluee]."
    C sad "You and Karma would've gone through a lot of trouble, and all for nothing."
    K tiredblink "No, I don't think it would've been for nothing."
    K tired "We couldn't just let [name_player] be so coldly sacrificed like that. Not after everything we've been through together."
    O sideeye "Exactly. We did it because it was the right thing to do."
    O sideeyeblink "That's why... [name_player], don't feel obligated to go one way or the other."
    O confident "Make a decision [t_clue]based on your own will[t_cluee]."
    C blush "Agreed~ [u_music_note]" with vpunch
    I "....."
    I "My own will... My own desires..."
    window auto hide
    show bg black with dissolvemed

    if died_with_regrets:
        I "I don't remember much about my life... But I remember I [t_clue]had some lingering regrets[t_cluee]..."
        I "Maybe... Maybe I should take this second chance at life..."
    else:
        I "I remember... I died with [t_clue]no regrets[t_cluee]..."
        I "I don't need a second chance in life...right?"

    K blink "...[name_player]. You don't have to think too hard about this."
    K default "Forget about things like responsibilities, [t_clue]regrets[t_cluee], or anything."
    K "Just follow your own heart. [t_clue]What do YOU want to do?[t_cluee]"
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "This is...the [t_clue]REAL final choice[t_cluee]..."
    play ctc_sfx "<silence 1.0>"
    I "Follow...my own heart..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}...I...{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ show_choicegrand = True

    menu:
        "Escape the house with the others":
            with custom_flashbulb()
            pause 0.5
            show bg foyer with dissolve
            $ show_choicegrand = False
            I "...I'm going with you guys."
            K blink "{cps=6}.....{/cps} ...Mm. Okay."
            C surprised "What did [name_player] say?"
            K happy "[name_player] is coming with us!"
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "Really?! YAYYY~ [u_heart]"
            O panicked "[name_player], are you sure? You'll probably need to continue using a dog's body, and who knows for how long..." with shakeonce
            C smug "Meh, we can always find another dead body to move [name_player] into. Ooh, maybe even a human--"
            play ctc_sfx "<silence 1.0>"
            O leering2 "No humans." with shakeonce
            O confused "I mean... *sigh* Perhaps using dogs may also be unethical..." with hpunch
            play ctc_sfx sfx_emotesigh
            K sweatdrop "Ahaha... I suppose there might be some challenges living life with the way your soul works..." with hpunch
            K blink "But you're one of us now, [name_player].{w=0.5} We won't ever abandon you."
            I "Karma... Everyone..."
            O blink "[name_player]. We cannot thank you enough for saving all of our lives."
            O embarrassed "Even if you can't necessarily return to a human's lifestyle... We could...um..."
            C smile "In case you're confused, [name_player], Ria's never once been allowed to keep a dog before."
            C smug "She's probably half-thrilled, but also half-embarrassed since she knows you as a person too."
            O annoyed "Enough with the unnecessary exposition." with shakeonce
            C wink "The same as always to the very end, huh, Ria?"
            O sideeyeblink "...[name_player]. As a dog, you could come with us to our other club excursions."
            O relaxed "Or if there's a place you want to visit, we can go there too."
            O confident "And then once you feel satisfied, you can rest wherever you want."
            YD "....."
            O panicked "...D-does that sound acceptable to you?{nw}" with shakeonce

            menu:
                extend ""
                "Bark":
                    YD "Ruff."
                    O surprised "....."
                    O "Uh... K-Karma, I-is that a \"yes\"?"
                    K happy "Tee hee. Who knows~"
                "Don't bark":
                    YD "....."
                    O surprised "...D-do you not want to do that...?"
                    play ctc_sfx sfx_emotesob
                    O sobbing2 "Karma... Wh-why did [name_player] go all quiet...?" with hpunch
                    K happy "There's a lot going through [name_player]'s mind right now. I think that's a great plan, Ria."
            C pout "Okay, enough humming and hawing! Let's goo~" with shakeonce
            hide oriana
            hide karma
            show bg foyer:
                xalign 0.8 yalign 0.5 zoom 1.5
            show cecilia grin at mycenter_closeup
            play ctc_sfx sfx_strike
            I "Uwah!" with shakeshort
            hide cecilia
            show bg foyer:
                xalign 0.2 yalign 0.5 zoom 2.0
            show oriana panicked at mycenter_zoom
            play sound sfx_whooshlow
            $ renpy.music.set_volume(0.0, 2, channel="music")
            O "Wha-- HEY!!{w=1.0}{nw}" with shakelong
            play ctc_sfx "<silence 1.0>"
            window auto hide None
            scene bg black with custom_flashquick()
            play sound sfx_fallsoft
            with shakeshort
            pause 1.0
            $ renpy.music.set_volume(1.0, 2, channel="music")
            I "She really just...picked me up and threw me..."
            I "...Wait, where am I?"
            $ show_side_oriana = True
            $ show_side_cecilia = True
            $ show_side_karma = True
            scene cg trueend:
                xalign 0.15 yalign 0.8 zoom 2.5
                easein 5.0 yalign 0.7
            with dissolvemed
            YD "...?!" with shakeshort
            I "Something soft...pressing on my head..." with vpunch
            O panicked "Wh-wha..."
            $ fadein_sideimage = False
            show cg trueend:
                xalign 0.15 yalign 0.7 zoom 2.5
                easein 5.0 yalign 0.3
            C wink "Oh come on, don't pretend you didn't want to pick up and hold [name_player]'s fuzzy doggy body."
            O shouting "That's..."
            O embarrassed "That's...not true at all..." with hpunch
            K default "Ria, you're grinning."
            play ctc_sfx sfx_emotesigh
            O panicked "Ah! Er, w-well..." with hpunch
            play ctc_sfx sfx_heartbeat_single
            I "I can hear her heart pounding..." with shakeonce
            scene cg trueend:
                xalign 0.75 yalign 0.8 zoom 2.0
                easein 6.0 yalign 0.3
            with dissolve
            C happy "Ah~ What a fun club outing that was! We got to see ghosts, zombies, a bit of blood..."
            K worried "Maybe YOU only saw a bit of blood, but me and [name_player]..."
            C smile "If you're already able to joke about it, then you really are a tough cookie, Karma."
            K blink "I'm just so relieved it's finally over..."
            scene cg trueend:
                xalign 0.6 yalign 0.4 zoom 1.5
                easein 5.0 xalign 0.5 yalign 0.5 zoom 1.1
            with dissolve
            O embarrassed "[name_player]... C-can I nuzzle you?"
            play ctc_sfx "<silence 1.0>"
            YD "Ruff?!" with shakeshort
            C happy "Come on, let's go home already!"
            K blink "...Yeah..."
            play ctc_sfx "<silence 1.0>"
            K overjoyed "Yeah! Let's go {color=#cccc00}home{/color}!" with vpunch
            stop music fadeout 5.0
            $ fadein_sideimage = True
            $ show_side_oriana = False
            $ show_side_cecilia = False
            $ show_side_karma = False
            scene cg trueend:
                xalign 0.5 yalign 0.5 zoom 1.1
                easein 5.0 zoom 1.0
            with dissolvemed
            scene bg black with dissolveslow
            pause 2.0
            $ quick_menu = False
            $ music_info = False
            show screen lock_hotkeys
            pause 2.0
            $ renpy.choice_for_skipping()
            $ _skipping = False
            show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#fff}КОНЕЦ{/color}{/size}{/font}" with dissolve
            pause 2.0
            achieve END_FINAL
            pause 3.0
            hide text with dissolveslow
            pause 3.0
            show backshards_1:
                alpha 0.5
                linear 2.0 yoffset -10
                block:
                    yoffset -10
                    ease 1.5 yoffset 10
                    ease 1.5 yoffset -10
                    repeat
            show backshards_2:
                alpha 0.5
                linear 2.5 yoffset -10
                block:
                    yoffset -10
                    ease 1.5 yoffset 10
                    ease 1.5 yoffset -10
                    repeat
            show backshards_3:
                alpha 0.5
                linear 3.0 yoffset -10
                block:
                    yoffset -10
                    ease 1.5 yoffset 10
                    ease 1.5 yoffset -10
                    repeat
            show backshards_4:
                alpha 0.5
                linear 3.5 yoffset -10
                block:
                    yoffset -10
                    ease 1.5 yoffset 10
                    ease 1.5 yoffset -10
                    repeat
            with dissolveslow
            play music bgm_credits noloop            
            show screen credits_slideshow
            call screen credits(200, True)
            stop music fadeout 3.0
            $ _skipping = True
            hide screen credits_slideshow
            scene bg black
            with dissolvemed
            pause 3.0
            show text "Это произведение является вымышленным. Любое сходство с реальными событиями и людьми, живыми\nили мёртвыми, является случайным. Мнения, выраженные персонажами этого\nпроизведения, не обязательно совпадают с мнением автора." with dissolvemed
            pause 15.0
            hide text with dissolvemed
            show text "Спасибо моей команде, всем, кто помог мне воплотить это видение в жизнь\nи, конечно, тебе, [name_player_true], за то, что досмотрел эту историю до конца.\n\nИскренне ваш,\nJun Kakeru (2025)" with dissolvemed
            pause 15.0
            hide text with dissolvemed
            pause 3.0
            $ quick_menu = True
            $ music_info = True
            hide screen lock_hotkeys
            $ persistent.unlock_cg_trueend = True
            $ persistent.unlock_gameclear_cgs = True
            return
        "Stay behind and pass on":
            with custom_flashbulb()
            pause 0.5
            show bg foyer with dissolve
            $ show_choicegrand = False
            I "...I'm going to stay."
            K blink "{cps=6}.....{/cps} ...Mm. Okay."
            C surprised "What did [name_player] say?"
            K "[name_player]...will be staying here."
            O surprised "Wha-- [name_player], don't tell me..."
            play ctc_sfx "<silence 1.0>"
            O shouting "You...you intend to follow the Professor and throw yourself into that Gate as well?!" with shakeonce
            play ctc_sfx "<silence 1.0>"
            YD "{cps=6}.....{/cps}"
            K shadow "...If there's no other way to truly die, then it's better than wandering around this house for eternity, apparently..."
            C thinking "Ria, wasn't it your idea for [name_player] to stay?"
            O afraid "I-I..." with shakeonce
            K "....."
            O dejected "{cps=6}...I...{/cps}"
            K tiredblink "Yeah. It's not going to be easy, saying goodbye like this."
            K tired "Especially after all that [name_player] suffered through to save us."
            play ctc_sfx "<silence 1.0>"
            I "{cps=6}.....{/cps}" with shakeonce
            play ctc_sfx "<silence 1.0>"
            O shadow "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            C sad "{cps=6}.....{/cps} ...Aight, if everyone's gonna get all quiet and awkward like this, then I'll say it first."
            window auto hide
            play sound sfx_whooshlow
            scene bg black with custom_flashquick()
            window auto show None
            I "Whoa! S-spinning... D-dizzy..." with hpunch
            show bg frontdoor open
            show cecilia smile at mycenter
            with custom_flashquick()
            $ show_side_oriana = True
            $ show_side_karma = True
            C smile "[name_player]!" with hpunch
            YD "...!" with shakeonce
            play ctc_sfx sfx_emotehappy
            C happy "{size=+10}Thank you!{/size}" with shakeshort
            C smile "You were a [t_clue]random spirit[t_cluee] from Hell who had nothing to do with the Professor or any of us."
            C sad "Your eternal rest was disturbed just so you could go through an endless cycle of killing games..."
            C blush "And at the very end, you broke that cycle and gave the three of us [t_clue]the ultimate good ending[t_cluee]."
            K panicked "Ah..." with shakeonce
            $ fadein_sideimage = False
            O stunned "....."
            $ fadein_sideimage = True
            play ctc_sfx sfx_emotehappy
            C overjoyed "Thank you for saving us! We'll never forget you!" with shakeshort
            window auto hide
            $ show_side_cecilia = True
            $ show_side_karma = False
            $ _last_say_who = "K"
            show cecilia overjoyed at mycenter_to_myright
            pause 0.3
            show karma sweatdrop at myleft with dissolve
            K "Y-yeah! [name_player], thank you!" with hpunch
            hide cecilia with dissolve
            show karma tiredblink at mycenter with move
            K "If it weren't for you, I... I would've gone through hell over and over a couple million times more..."
            play ctc_sfx "<silence 1.0>"
            K crying "My mind would've broken for sure. I was already going to let a spirit take over and kill one of my dear friends..." with shakeonce
            K crying2 "You saved me from that fate. I'll...{w=1.0}{nw}"
            play ctc_sfx sfx_heartbeat_single
            extend " I'll never forget that." with shakeonce
            I "...You're wrong, Karma."
            K "...?" with shakeonce
            I "We only got here thanks to you. Because you never truly gave up."
            I "I've been hearing your [t_clue]voice[t_cluee] from the very beginning. This...could have ended badly really quickly if it weren't for you."
            I "...Thank you for protecting my [t_clue]dear friends[t_cluee] too."
            play ctc_sfx "<silence 1.0>"
            K overjoyed "{cps=6}.....{/cps} ...Yeah. We have the greatest of friends, don't we...?" with shakeonce
            play ctc_sfx sfx_emotesigh
            C sobbing "They're having a private, telepathic conversation... So jelly..." with hpunch
            $ fadein_sideimage = False
            O thinking "....."
            YD "....."
            $ fadein_sideimage = True
            window auto hide
            $ show_side_oriana = False
            $ show_side_karma = True
            hide karma with dissolvemed
            $ _last_say_who = "O"
            show oriana thinking at mycenter with dissolvemed
            pause 1.0
            O thinking "{cps=6}.....{/cps}"
            C smug "...Ria?"
            O irritated "...Is there anything more for me to add?" with shakeonce
            K happy "Come on, it's not about {i}what{/i} you say, but the intent behind it! What feelings do you want to convey?"
            O confused "Feelings...?"
            YD "....."
            play ctc_sfx "<silence 1.0>"
            O embarrassed "...Those literal puppy dog eyes are disrupting my thoughts..." with shakeonce
            play ctc_sfx sfx_emotehappy
            K "You can do it, Ria!" with vpunch
            $ fadein_sideimage = False
            play ctc_sfx sfx_emotehappy
            C happy "Yeah, do it!" with vpunch
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            O annoyed "Will the peanut gallery please shut up?!" with shakeonce
            YD "....." with vpunch
            O blink "{cps=6}.....{/cps} ...[name_player]."
            O thinking "I was...cold to you when we first met."
            O irritated "I couldn't accept a spirit from Hell controlling my best friend, after all."
            I "....."
            O default "But... I'm grateful you decided to help us despite that. Despite all the pain you endured from the endless killing games."
            O happy "So...{w=0.5} Thank you.{w=0.5} Thank you so much for protecting us."
            play ctc_sfx sfx_heartbeat_single
            YD "...!!" with shakeonce
            $ fadein_sideimage = False
            play ctc_sfx "<silence 1.0>"
            K crying2 "Riiiaaa..." with hpunch
            play ctc_sfx sfx_emotesob
            C sobbing "They grow up so fast..." with hpunch
            $ fadein_sideimage = True
            O embarrassed "I-if we're done here, let's hurry out. Who knows how long this door will remain open..." with shakeonce
            K blink "Yeah, I guess it's time."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = False
            YD "{cps=6}.....{/cps}"
            $ fadein_sideimage = True
            play ctc_sfx "<silence 1.0>"
            $ show_side_cecilia = False
            $ show_side_karma = False
            scene bg black with dissolveslow
            I "Cecilia... Oriana... And Karma..."
            I "I hope I never forget you guys either."
            I "Even if the flames of Hell burn away any trace of my soul..."
            I "May this house... This space between the realms of the living and the dead..."
            I "May it serve as proof of my existence. ...Of our [t_clue]bond's existence[t_cluee]."
            $ show_side_karma = True
            K happy "Heehee... You're actually pretty poetic, huh, [name_player]?"
            I "...You didn't have to comment on my monologue."
            K blink "Probably not. But I'm glad we could joke around one last time."
            $ fadein_sideimage = False
            K default "...[name_player_true]. Maybe one day, we'll meet again."
            K "Whether in this world or the other one, if we ever meet again, I hope we can be friends."
            $ fadein_sideimage = True
            I "...Yeah. Yeah, I'd like that."
            K overjoyed "Don't forget me.{cps=1} {/cps}Until next time..."
            play ctc_sfx "<silence 1.0>"
            $ show_side_karma = False
            stop music fadeout 5.0
            scene bg black with dissolveslow
            pause 2.0
            $ quick_menu = False
            $ music_info = False
            show screen lock_hotkeys
            pause 2.0
            $ renpy.choice_for_skipping()
            $ _skipping = False
            show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#fff}КОНЕЦ{/color}{/size}{/font}" with dissolve
            pause 2.0
            achieve END_FINAL
            pause 3.0
            hide text with dissolveslow
            pause 3.0
            show backshards_1:
                alpha 0.5
                linear 2.0 yoffset -10
                block:
                    yoffset -10
                    ease 1.5 yoffset 10
                    ease 1.5 yoffset -10
                    repeat
            show backshards_2:
                alpha 0.5
                linear 2.5 yoffset -10
                block:
                    yoffset -10
                    ease 1.5 yoffset 10
                    ease 1.5 yoffset -10
                    repeat
            show backshards_3:
                alpha 0.5
                linear 3.0 yoffset -10
                block:
                    yoffset -10
                    ease 1.5 yoffset 10
                    ease 1.5 yoffset -10
                    repeat
            show backshards_4:
                alpha 0.5
                linear 3.5 yoffset -10
                block:
                    yoffset -10
                    ease 1.5 yoffset 10
                    ease 1.5 yoffset -10
                    repeat
            with dissolveslow
            play music bgm_credits noloop
            show screen credits_slideshow
            call screen credits(200, True)
            stop music fadeout 3.0
            $ _skipping = True
            hide screen credits_slideshow
            scene bg black
            with dissolvemed
            pause 3.0
            show text "Это произведение является вымышленным. Любое сходство с реальными событиями и людьми, живыми\nили мёртвыми, является случайным. Мнения, выраженные персонажами этого\nпроизведения, не обязательно совпадают с мнением автора." with dissolvemed
            pause 15.0
            hide text with dissolvemed
            show text "Thank you to my team, to everyone who helped me bring this vision to life,\nand of course, you, [name_player_true], for seeing this story to the end.\n\nSincerely yours,\nJun Kakeru (2025)" with dissolvemed
            pause 15.0
            $ persistent.unlock_gameclear_cgs = True
            if not chose_suspect:
                hide text with dissolvemed
                pause 3.0
                $ quick_menu = True
                $ music_info = True
                hide screen lock_hotkeys
            else:
                call save_file_name_update (3, "d3a8_secret")
                $ quick_menu = True
                $ music_info = True
                hide screen lock_hotkeys
                show bg secretending with dissolveslow
                $ renpy.pause(3.0, hard=True)
                pause 2.0
                $ _last_say_who = 'C'
                show cecilia thinking behind text at myright_far with moveinright
                play sound sfx_emotequestion
                with dissolve
                C "...?"
                show cecilia surprised at mycenter with move
                C "...Huh? Why are you still here?"
                C pout "Ack, what is this floating text? Wait, let me clear this..."
                window auto hide
                pause 0.5
                play sound sfx_whoosh
                show cecilia pout at shudder
                show text "Thank you to my team, to everyone who helped me bring this vision to life,\nand of course, you, [name_player_true], for seeing this story to the end.\n\nSincerely yours,\nJun Kakeru (2025)":
                    rotate 0
                    linear 0.5 rotate 270
                hide text with moveoutleft
                pause 0.5
                C default "There we go! So! Again, why are you still here?"
                C thinking "The credits have finished rolling, and the story has been brought to a conclusive end!"
                C "....."
                C surprised "...Huh? You don't know what's going on?"
                C thinking "Hmm... Wait, what's that say above me? \"bg...\""
                C "\"bg secretending\", huh? So what, was something supposed to be revealed here?"
                show cecilia pout at doublehop
                C "It's all gray! There's nothing! Was this a developer oversight?!"
                C "....."
                C blink "...Okay. I guess if you {i}really{/i} want to keep sticking around, there IS a [t_clue]secret[t_cluee] I could tell you."
                C default "But you have to PROMISE not to tell anyone, okay? Not Karma, not Ria..."
                C blink "...And not even [name_player]."
                C default "Hmm? Yeah, I see you there. You're completedly exposed right now."
                C smile "You're the one who's been pushing [name_player] to do certain things, aren't you?"
                C thinking "After all, from what I know, it doesn't make sense. How did [name_player] get out of being sacrificed like that?"
                C sweatdrop "Especially considering all the emotional aspects, like wouldn't [name_player] WILLINGLY get sacrificed at that point?"
                C blink "But I digress. That's not the secret I wanted to tell you."
                C thinking "Hmm... What's the best way to reveal this..."
                C wink "Actually, maybe you already know so I'll just drop it like it's hot."
                C blink "The [t_clue]mastermind[t_cluee] who orchestrated the killing game? ...Yeah, that wasn't the Professor."
                play ctc_sfx "<silence 1.0>"
                C "{cps=6}.....{/cps}{w=0.5}{nw}"
                play ctc_sfx "<silence 1.0>"
                extend creepy " ...It was [t_clue]me[t_cluee].{nw}"
                play music bgm_chaos
                play ctc_sfx "<silence 1.0>"
                show bg secretending:
                    matrixcolor InvertMatrix(1.0)
                    linear 5.0 matrixcolor InvertMatrix(0.0)
                extend "" with shakeonce
                C "....."
                play ctc_sfx sfx_emotehappy
                show cecilia happy at hop
                C "I know, right?! DUN DUN DUUUUN! Mind blown! You should look at your face right now!" with shakeonce
                C blink "But think about it. Doesn't it make a lot of sense?"
                C default "The Professor has been killing people who enter his house in order to feed the Gate to Hell, and eventually escape..."
                C thinking "So WHY would he suddenly decide to mix it up and make his victims try to kill each other instead?"
                C blink "The answer is...{w=0.5}{nw}"
                play ctc_sfx "<silence 1.0>"
                extend grin "there IS no reason! He saw the writing on the door and just rolled with it!" with shakeonce
                C sad "Maybe he thought it would be one less sin for him to bear if his last victim wasn't killed by his own hands? Who knows!"
                C default "So then, if it wasn't the Professor, who do you think wrote that writing on the door?"
                C "....."
                show cecilia happy at hop
                C "That's right! Who else but CECE~"
                C default "Ria doesn't know this, but when we all got pulled into this house, I actually woke up first."
                C thinking "It was maybe about...20 minutes before Ria woke up? Anyway, I was enthused so I went around the house alone."
                C blink "When I wandered into the little girl's bedroom, I saw the paint set on the desk, and came up with the BEST idea."
                C smug "\"What if when Ria and Karma wake up, they see writing on the door telling them they need to kill someone to leave?\""
                C wink "It was sort of a prank, sort of morbid curiosity, but I did it and pretended to not know a thing!"
                C surprised "But boy, it came as a big shock to see Karma wake up screaming. Who would've guessed she could control time?"
                C sad "I never would have thought she'd go through the killing game so many times."
                C overjoyed "And then the Professor coming out to offer a spirit from Hell to help us kill each other? THAT was rad." with vpunch
                C smile "Things just kept getting more and more interesting from there... We had to find a solution to work around Karma's time traveling..."
                C happy "At some point, I forgot that I was the one who wrote the writing on the door in the first place!"
                C grin "But like, it all worked out in the end, right?"
                C "In fact, if we DIDN'T do the killing game, the Professor would've just killed us normally anyway!" with hpunch
                C sad "And because of Karma's power, we would've been [t_clue]killed over and over again[t_cluee]!"
                C smug "It's thanks to the killing game that we were able to get [name_player]'s help, and buy enough time to corner the Professor."
                C happy "So if anything, the [t_clue]true hero[t_cluee] of this story is ME!"
                C "....."
                play ctc_sfx sfx_emotesigh
                show cecilia sweatdrop at shrink
                C "...You don't look too impressed. Well, I suppose calling me a \"hero\" is a bit of a stretch here..."
                show cecilia sad at mycenter
                C "And just maaaybe we could've found a way out without needing to involve a killing game in any way or form..."
                C smile "But killing games are FUN, though! You think so too, don't you? I mean,{w=1.0} [t_clue]why else would you be playing this game?[t_cluee]"
                C "People degrading their morals... Turning against even their best friends as fear for their lives takes over..."
                C happy "It's truly the most addictive form of entertainment! Man, I'm glad to be living in modern times!"
                C "....."
                C surprised "...Hmm? It should be limited to fiction, you say?"
                C "....."
                C thinking "Hmm... Correct me if I'm wrong, but..."
                play ctc_sfx sfx_emotequestion
                C default "From your point of view, isn't this all a [t_clue]work of fiction[t_cluee] in the first place?"
                C thinking "Like, wasn't there a disclaimer or something when you started playing this game?"
                C "It even appeared again after the end credits. Remember? \"This is a work of...\""
                C "....."
                C surprised "Oooh, you mean like in MY world? The morality that Ria likes to preach about?"
                C thinking "Hmmmmmmmmm..."
                C smug "I mean, you don't live on this side. Who's to say our moral values are the same as yours?"
                C blink "You saw for yourself that even Ria is capable of committing murder when her back is against the wall."
                C "Maybe she was just saying pretty words that make sense to you, but not to the rest of us."
                C grin "Do you expect us fictional characters to adhere to your \"real-life\" morals?"
                C "....."
                C blink "Besides, the ultimate outcome of my little prank with the door is that all of us got to escape safely."
                C "A classic \"the ends justifies the means\" argument, perhaps, but isn't it valid?"
                C smile "We all survived. That's all anyone needs to know."
                show bg black with dissolve
                C surprised "Oh, looks like the game is finally ending."
                C blush "Okay, I'll be going now. And don't forget our promise, okay?"
                play ctc_sfx "<silence 1.0>"
                C "{cps=6}...{/cps}{w=0.5}{nw}"
                play ctc_sfx "<silence 1.0>"
                extend creepy "{color=#ff0000}Don't tell anyone about this secret ending.{/color}" with shakeonce
                play ctc_sfx "<silence 1.0>"
                $ renpy.music.set_volume(0.2, 10, channel="music")
                show cecilia creepygrin at mycenter:
                    zoom 1.0 ypos 1.05
                    easein 20.0 zoom 2.5 ypos 2.1
                C "Don't tell Karma, Ria, or [name_player], of course, but also don't tell your friends or family."
                play ctc_sfx "<silence 1.0>"
                C "Don't even post any screenshots or recordings of this ending on the Internet or social media. Because if you do..."
                play ctc_sfx "<silence 1.0>"
                if input_name_true == input_name:
                    C "...I'll know. You and [name_player] share a name, right? Or maybe you lied at that screen?"
                else:
                    C "...I'll know. [name_player_true], was it? Or maybe that was also a fake name?"
                play ctc_sfx "<silence 1.0>"
                C "You can't hide your face from me though. I'm looking at it right now. And I'll remember it."
                play ctc_sfx "<silence 1.0>"
                C "Even if I'm a fictional character, I exist."
                play ctc_sfx "<silence 1.0>"
                C "You and all the other players who know me grant me a presence in your world."
                play ctc_sfx "<silence 1.0>"
                C "{cps=24}And as that presence...{/cps}{w=0.5} {color=#ff0000}I will be watching you.{/color}{w=1.0} Very carefully..."
                play ctc_sfx "<silence 1.0>"
                $ renpy.music.set_volume(1.0, 0, channel="music")
                play ctc_sfx sfx_emotehappy
                show cecilia happy at hop:
                    zoom 1.0
                C "Anyway, the developers and I hope you had a great time playing\n[t_clue]Yet Another Killing Game[t_cluee]!"
                C wink "Have fun playing your next game, okay? Byeeee~ [u_music_note]"
                achieve THE_TRUTH
                stop music fadeout 5.0
                scene bg black with dissolveslow
                pause 3.0
                $ persistent.unlock_bg_secretending = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
