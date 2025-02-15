


screen pac_d1a1_kitchen:
    style_prefix "pac"

    use pac_progress_gui(_("The Kitchen with Cecilia"))


    use pac_assistant_button(1200, 1030, 0.77, 1140, 500, "gui/pac/pac_assistant_cecilia.png", "pac_assistant_cecilia_hop", "d1a1_kitchen_assistant", _("Talk to Cecilia"))


    use pac_end_button("d1a1_kitchen_confirm_end", investigated_kitchen)


    use pac_button(1600, 680, d1a1_kitchen_clue1, "d1a1_check_refrigerator", _("Refrigerator"))
    use pac_button(1700, 240, d1a1_kitchen_clue2, "d1a1_check_pantry", _("Cabinets"))
    use pac_button(1350, 590, d1a1_kitchen_clue3, "d1a1_check_phone", _("Phone"))
    use pac_button(450, 590, d1a1_kitchen_clue4, "d1a1_check_stove", _("Stove"))
    use pac_button(950, 590, d1a1_kitchen_clue5, "d1a1_check_knives", _("Knife Rack"))

    use pac_button(800, 550, d1a1_kitchen_clue6, "d1a1_check_microwave", _("Microwave"))
    use pac_button(660, 580, d1a1_kitchen_clue7, "d1a1_check_pot", _("Pot"))
    use pac_button(70, 470, d1a1_kitchen_clue8, "d1a1_check_kitchenwindow", _("Window"))
    use pac_button(150, 770, d1a1_kitchen_clue9, "d1a1_check_kitchendrawer", _("Drawer"))
    use pac_button(1500, 610, d1a1_kitchen_clue10, "d1a1_check_peppershaker", _("Shaker"))

image pac_assistant_cecilia_hop:
    "gui/pac/pac_assistant_cecilia.png"
    yoffset 0
    easeout 0.1 yoffset -15
    easein 0.1 yoffset 0



screen pac_d1a1_diningroom:
    style_prefix "pac"


    use pac_assistant_button(530, 1040, 0.73, 480, 540, "gui/pac/pac_assistant_cecilia_thinking.png", "pac_assistant_cecilia_shudder", "d1a1_kitchen_assistant", _("Talk to Cecilia"))


    use pac_progress_gui(_("The Kitchen with Cecilia"))


    use pac_end_button("d1a1_kitchen_confirm_end", investigated_kitchen)


    use pac_button(190, 560, d1a1_diningroom_clue1, "d1a1_check_diningroomwindow", _("Window"))
    use pac_button(670, 950, d1a1_diningroom_clue2, "d1a1_check_petbowl", _("Pet Bowl"))
    use pac_button(920, 780, d1a1_diningroom_clue3, "d1a1_check_table", _("Table"))

    use pac_button(1020, 660, d1a1_diningroom_clue4, "d1a1_check_candelabra", _("Candelabra"))
    use pac_button(1060, 260, d1a1_diningroom_clue5, "d1a1_check_chandelier", _("Chandelier"))
    use pac_button(1480, 660, d1a1_diningroom_clue6, "d1a1_check_flowervase", _("Flower Vase"))
    use pac_button(1090, 560, d1a1_diningroom_clue7, "d1a1_check_chinacabinet", _("China Cabinet"))
    use pac_button(1480, 480, d1a1_diningroom_clue8, "d1a1_check_diningroompainting", _("Large Painting"))
    use pac_button(1560, 860, d1a1_diningroom_clue9, "d1a1_check_brokenchair", _("Broken Chair"))
    use pac_button(1800, 600, d1a1_diningroom_clue10, "d1a1_check_kitchenentrance", _("Kitchen"))
    use pac_button(630, 630, d1a1_diningroom_clue11, "d1a1_check_chairfragments", _("Fragments"))

image pac_assistant_cecilia_shudder:
    "gui/pac/pac_assistant_cecilia.png"
    xoffset 0
    linear 0.1 xoffset 5
    linear 0.1 xoffset -5
    linear 0.1 xoffset 0



label d1a1_kitchen_assistant:
    $ _last_say_who = "C"
    if investigation_location == "d1a1_diningroom":
        show bg diningroom withchair:
            xalign 0.0 yalign 0.5 zoom 1.5
        show cecilia at mycenter
        with dissolve
    else:
        show bg kitchen:
            xalign 0.8 yalign 0.5 zoom 1.5
        show cecilia at mycenter
        with dissolve
    C happy "Oh? Did you need something from me, [name_player]?{nw}"

    menu:
        "[t_clue]End your investigation[t_cluee]" if investigation_perfect:
            call d1a1_kitchen_confirm_end
        "\"Any ideas?\"":
            Y "Just wondering if anything comes to mind."
            C thinking "Hmm..."
            if investigation_clues_required_found == investigation_clues_required:
                C "Don't you think we checked everything worth checking by now?"
                C default "Unless you want to give everything a [t_clue]second glance[t_cluee], I think we should start wrapping this investigation up."
                I "Hmm... She's probably right..."
            elif investigation_progress_percent() >= 0.66:
                C "There's probably only a few things left that are worth checking out..."
                Y sad "And yet, we still haven't found anything remotely useful..."
                C sad "Aww, [name_player], don't go frowning like that..."
                C smile "I get that you're worried, but all we can control is what we do now, at this very moment."
                C default "There are still clues left to find. Once we have them all, we can talk about it over dinner."
                if d1a1_kitchen_clue2 == True:
                    C thinking "Oh, I guess only the canned food is edible, huh? Hmm, is there a can opener here...?"
                else:
                    show cecilia happy at hop
                    C "Speaking of which, we should check the [t_clue]cabinets[t_cluee] next! Hopefully there's something good to eat in there!"
                I "...That was...unexpectedly comforting. Didn't expect that from her."
                I "Why did that give me chills, though...?" with hpunch
            elif investigation_progress_percent() >= 0.33:
                if d1a1_kitchen_clue5:
                    C blink "I suppose there's one thing I'm curious about."
                    Y surprised "Oh? And what's that?"
                    C smile "If you don't want to use the [t_clue]knife[t_cluee], what's your preferred murder weapon of choice?{nw}"

                    menu:
                        extend ""
                        "A different sharp instrument":
                            Y thinking "A knife is a little tricky to use... You basically need to use it for stabbing, when sometimes that--"
                            $ fadein_sideimage = False
                        "A blunt instrument":
                            Y relaxed "A blunt weapon is a lot easier to handle. There's also less chance of blood getting all ove--"
                            $ fadein_sideimage = False
                        "My bare hands":
                            Y blink "You can't know if you'll have an actual weapon on hand, so it's good to know how to use your own hands to--"
                            $ fadein_sideimage = False
                        "Nothing":
                            Y angry "Wh-what are you talking about?! I wouldn't use {i}any{/i} weapon!" with hpunch
                            C smug "I see~ You prefer an indirect approach, then? Maybe manipulating someone else to--"
                    Y panicked "Wait, I was talking about the investigation! Did you have any ideas about THAT?" with shakeonce
                    $ fadein_sideimage = True
                    C default "Oh, nothing related to that. But back to the topic of murder weapons..."
                    Y worried2 "Never mind, I'll just keep looking by myself..."
                else:
                    C smug "If you ask me, I'm surprised you ignored the prominent interactive point on the kitchen island."
                    Y worried "The...\"interactive point\"...?"
                    C sad "I even went through the trouble of standing right next to it when you started your investigation..."
                    I "...I guess there's no getting around it, then. Better check that out..."
            else:
                C default "We've only just started to look around, right?"
                C happy "Try [t_clue]looking REALLY carefully[t_cluee] at certain objects in this room. I'm sure you'll figure it out!"
                I "\"Look REALLY carefully\", she says... Did she already notice something and just isn't telling me?"
        "\"Let's check [t_clue]the other room[t_cluee].\"" if not d1a1_visited_diningroom and investigation_location != "d1a1_diningroom":
            Y default "The other room I passed to get here... The one with the big table..."
            C default "Yeah? The [t_clue]dining room[t_cluee], right?"
            Y thinking "Did you look around there at all while you were...swinging the chair?"
            C thinking "Not that carefully, I guess. I was sorta distracted, as you know."
            I "Yes, you sure were..."
            C default "It's a pretty clean room overall, though. I don't recall anything interesting sticking out at me."
            C blush "But if you really wanna, we can go check it out!"
            Y default "Yeah, let's go take a closer look."
            play ctc_sfx sfx_steps
            play sound ["<silence 0.2>", sfx_steps]
            scene bg black with fade
            scene bg diningroom withchair with fade
            pause 2.0
            I "...Hmm..."
            I "...Other than the broken chair, a couple of things stick out at me..."
            $ _last_say_who = 'C'
            show cecilia thinking at mycenter with dissolve
            C "See? Not much here, right?"
            Y default "I disagree. Here, let me show you..."
            $ d1a1_visited_diningroom = True
            $ investigation_location = "d1a1_diningroom"

        "\"Let's check the [t_clue]Dining Room[t_cluee] again.\"" if d1a1_visited_diningroom and investigation_location != "d1a1_diningroom":
            Y default "Let's go check out the dining room again."
            if not d1a1_diningroom_clue2 or not d1a1_diningroom_clue3:
                C thinking "Really? I still don't think there's anything there, but okay."
            else:
                C thinking "Again? Didn't you already say we covered everything important?"
                Y thinking "Yeah... But it can't hurt to take another look."
                C sweatdrop "You're a diligent one, aren't you, [name_player]?"
            play ctc_sfx sfx_steps
            play sound ["<silence 0.1>", sfx_steps]
            scene bg black with fade
            scene bg diningroom withchair with fade
            pause 2.0
            $ investigation_location = "d1a1_diningroom"

        "\"Let's go back to the [t_clue]Kitchen[t_cluee].\"" if investigation_location == "d1a1_diningroom":
            if not d1a1_diningroom_clue2 or not d1a1_diningroom_clue3:
                Y default "Let's go back to the kitchen."
                C smile "Good idea! Most of the interesting clues are over there."
            else:
                Y blink "Yeah, I think we covered everything important here."
                C smile "Back to the kitchen, then? Okay dokay~"
            play ctc_sfx sfx_steps
            play sound ["<silence 0.2>", sfx_steps]
            scene bg black with fade
            scene bg kitchen with fade
            pause 2.0
            $ investigation_location = "d1a1_kitchen"
        "\"Never mind...\"":
            pass

    return

label d1a1_kitchen_complete:
    I "...Hmm... I think I've checked everything that really stuck out to me..."
    I "Maybe I can start wrapping this up?"
    return

label d1a1_kitchen_perfect:
    I "...All right, I've definitely checked every little nook and cranny now..."
    I "Guess I should [t_clue]end my investigation[t_cluee] and move on."
    return

label d1a1_kitchen_confirm_end:
    if investigated_kitchen and not investigation_complete:
        I "...It's strange but..."
        I "I feel like I [t_clue]already know[t_cluee] what to expect from investigating around here."
        I "Maybe I can zone out a bit as I go through everything...?{nw}"

        menu:
            extend ""
            "Skip this investigation":
                scene bg black with dissolvemed
                $ investigation_location = None
            "Cancel":
                I "...Actually, I should stay alert... Especially while I'm with Cecilia..."
    else:
        $ _last_say_who = "C"
        show cecilia at mycenter with dissolve
        C "Hmm? What's up, [name_player]? Are we wrapping up?{nw}"
        menu:
            extend ""
            "End your investigation":
                Y blink "Yeah... I think we've found everything remotely useful..."
                scene bg black with dissolvemed
                $ investigation_location = None
            "Cancel":
                Y default "...No, let's look around a bit more."
    return
label d1a1_check_refrigerator:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 1.0 yalign 0.8 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue1 == False:
        I "A [t_pacclue]refrigerator[t_paccluee]..."
        I "...I'm just looking for clues. It's not that I feel hungry or anything."
        I "Let's see..."
        Y blink "......."
        play ctc_sfx "<silence 1.0>"
        $ fadein_sideimage = False
        Y afraid "WHAT THE--{w=0.3}{nw}" with shakeshort
        $ fadein_sideimage = True
        play ctc_sfx sfx_fridgeclose
        window auto hide None
        show bg kitchen at reset with custom_flashquick()
        show cecilia surprised at mycenter, hop with shakeshort
        C "Ah! [name_player], you scared me!"
        Y panicked "S-sorry. It's just..."
        $ fadein_sideimage = False
        Y pained "It REALLY stinks in there!" with shakeonce
        $ fadein_sideimage = True
        C default "Huh? Really?"
        hide cecilia with dissolve
        Y blink "Yeah, I guess the [t_clue]power's been out[t_cluee] for a long time, and all the food in there has gone-- {w=0.5}{nw}"
        $ fadein_sideimage = False
        play ctc_sfx "<silence 1.0>"
        extend panicked "WHAT ARE YOU DOING?!" with shakeonce
        $ show_side_cecilia = True
        C blink "*sniff*"
        C "{size=+20}*long sniff*{/size}" with shakeshort
        $ show_side_cecilia = False
        Y "....."
        $ fadein_sideimage = True
        $ _last_say_who = "C"
        show cecilia blink at mycenter with dissolve
        C "{cps=6}.......{/cps}"
        show cecilia sobbing at shudder
        C "...Yeah, it's really bad."
        I "...She's tearing up HARD..."
        play ctc_sfx sfx_emoteshout
        Y shouting "I TOLD you it stinks in there!" with shakeshort
        show cecilia pout at hop
        C "I know! I know, but..."
        C default "If someone tells you that anything is really REALLY bad..."
        C "...Don't you kind of get an urge to check it out?{nw}"

        menu:
            extend ""
            "\"Yeah, I feel you.\"":
                Y thinking "I...guess I can understand that."
                play ctc_sfx sfx_emotehappy
                show cecilia happy at hop
                C "See! I knew you would get me, [name_player]!"
            "\"No.\"":
                Y worried "No."
                play ctc_sfx sfx_emotesob
                show cecilia sobbing at shrink
                C "No hesitation at all? You're a meanie, [name_player]."
        Y sad "...Anyways, I definitely lost my appetite. Let's just move on."
        if not d1a1_kitchen_clue1:
            $ investigation_clues_required_found += 1
            $ d1a1_kitchen_clue1 = True
    else:
        I "I don't think I need to check out this [t_pacclue]refrigerator[t_paccluee] anymore..."
        $ show_side_cecilia = True
        C "Hmm? What's up? Are you thinking of taking another whiff?"
        $ fadein_sideimage = False
        Y blink "Absolutely not."
        C thinking "Oh."
        C default "....."
        C grin "......."
        Y worried "Please don't open the refrigerator again. The smell might spread."
        play ctc_sfx sfx_emotesigh
        C sweatdrop "Fine, fine." with hpunch
        $ fadein_sideimage = True
        $ show_side_cecilia = False
    return
label d1a1_check_pantry:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 1.0 yalign 0.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue2 == False:
        Y "Some overhead [t_pacclue]cabinets[t_paccluee]. There's probably food up there."
        I "It's pretty high up. But I think I should be able to reach it..."
        $ _last_say_who = "C"
        scene bg kitchen
        show cecilia sad at mycenter
        with dissolve
        C "This probably doesn't come as a surprise, but I couldn't check what's up there."
        Y surprised "You couldn't... Ooooh, because of your height--"
        play ctc_sfx sfx_emotesob
        show cecilia sobbing at crouch
        C "You don't have to say it!"
        I "Guess that's a bit of a sore spot for her..."
        scene bg kitchen:
            xalign 1.0 yalign 0.0 zoom 1.5
            easein 5.0 zoom 1.8
        with dissolve
        Y wince "Nrgh... Yep, looks like I can barely reach it." with vpunch
        $ show_side_cecilia = True
        $ fadein_sideimage = False
        C overjoyed "Okay, open it up and we can take a look from a distance!"
        $ renpy.music.set_volume(0.5, 1.5, channel="music")
        scene bg black with dissolvemed
        $ fadein_sideimage = True
        Y thinking "Hmm... Mostly [t_clue]canned food[t_cluee] and some stuff in jars that...mutated a bit."
        $ fadein_sideimage = False
        C surprised "Oh, [name_player], look! That yellow can in the middle there."
        Y surprised "What is that? ...R..."
        play ctc_sfx sfx_heartbeat_single
        $ renpy.music.set_volume(0.0, 0, channel="music")
        $ renpy.music.set_volume(0.5, 3, channel="music")
        Y afraid "...[t_clue]Rat poison[t_cluee]?" with shakeonce
        C smug "Kind of a scary place to leave a can of poison, huh?"
        Y leering "\"Kind of scary\"? It's super obvious why this is here."
        C blink "Yeah, guess we oughta be careful of what we eat here, huh?"
        Y worried "D-don't even go there..." with shakeonce
        $ show_side_cecilia = False
        $ fadein_sideimage = True
        $ _last_say_who = "C"
        $ renpy.music.set_volume(1.0, 1.5, channel="music")
        scene bg kitchen
        show cecilia thinking at mycenter
        with dissolvemed
        C "I guess these cans should be enough food for three of us?"
        Y default "Yeah, I think so."
        C smug "And you're sure about leaving the rat poison up there?"
        Y worried "I'm very sure, yes."
        I "Let's hope it stays up there forever..."
        if not d1a1_kitchen_clue2:
            $ investigation_clues_required_found += 1
            $ d1a1_kitchen_clue2 = True
    else:
        Y default "It's a relief the [t_pacclue]cabinets[t_paccluee] were pretty well stocked."
        $ show_side_cecilia = True
        $ fadein_sideimage = False
        C "The fruit and baked goods are a little sus, but I think the canned food should be fine."
        Y "Are you hungry at all, Cecilia?"
        C thinking "Hmm? No, not really. How about you, [name_player]?"
        if d1a1_kitchen_clue1 == False:
            Y surprised "Maybe a little, but..."
            Y blink "Nah, let's wait until Oriana is done checking out the floor above us."
        else:
            Y worried "After opening that fridge? Nope, not even a little."
            $ fadein_sideimage = True
            I "I don't remember the last time I ate, but the fact that I feel fine must mean I ate recently..."
            Y default "Let's wait until Oriana is done checking out the floor above us."
            $ fadein_sideimage = False
        Y default "That way, we can talk about our findings while we eat."
        C blink "Hmm... Alright, if you say so."
        $ _last_say_who = None
        $ show_side_cecilia = False
        $ fadein_sideimage = True
        scene bg kitchen
        show cecilia_raw blink as cecilia at mycenter, backedaway_on
        with dissolve
        I "She seems disappointed. Maybe she's a little hungry after all?"
        show cecilia blink at mycenter, backedaway_off
        C smile "...So?"
        Y surprised "...So...what?"
        C "Why are you checking the cabinets again?"
        C "Could it be that you're interested in that can of [t_clue]rat poison[t_cluee] after all?"
        Y sad "N-no, I..." with hpunch
        play ctc_sfx sfx_emotehappy
        show cecilia happy at hop
        C "Ahaha~ Don't worry, I'm just teasing!"
        C default "C'mon, let's keep looking around."
    return

label d1a1_check_phone:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 0.8 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue3 == False:
        Y panicked "...! There's a [t_pacclue]telephone[t_paccluee] there!" with shakeonce
        $ fadein_sideimage = False
        Y leering "Cecilia, have you tried using that phone?"
        $ show_side_cecilia = True
        C surprised "Huh? Oh yeah, that's a phone too."
        C happy "Crazy what phones used to look like, amirite?"
        Y worried "...Okay, I'm just gonna try it."
        $ renpy.music.set_volume(0.5, 1.5, channel="music")
        scene bg black with dissolve
        play sound sfx_phonepickup
        $ fadein_sideimage = True
        Y leering "....."
        $ fadein_sideimage = False
        Y "{cps=6}.......{/cps}"
        C default "{cps=6}.........{/cps}"
        Y "{cps=6}...........{/cps}"
        C "Any luck?"
        play sound ["<silence 0.5>", sfx_phonehangup]
        Y sad "No... I think the line is cut."
        $ renpy.music.set_volume(1.0, 1.5, channel="music")
        $ show_side_cecilia = False
        $ fadein_sideimage = True
        $ _last_say_who = "C"
        scene bg kitchen
        show cecilia blink at mycenter
        with dissolve
        C "Makes sense. They took away our cell phones too, after all."
        C thinking "I don't think we'll have any luck trying to call for help."
        Y thinking "So we need to find a way to [t_clue]escape by ourselves[t_cluee]..."
        C sad "Speaking of phones... I didn't play any of my mobile games today..."
        play ctc_sfx sfx_emoteshout
        show cecilia pout at doublehop
        C "I swear, the SECOND I get my phone back, I'm gonna slug the culprit once for every login reward I missed!" with shakeshort
        Y worried "...Uh, what do you mean by... Er..."
        I "Actually, something tells me I'm better off not knowing..."
        if not d1a1_kitchen_clue3:
            $ investigation_clues_optional_found += 1
            $ d1a1_kitchen_clue3 = True
    else:
        Y sad "The [t_pacclue]telephone[t_paccluee]'s line is cut, so we can't call for any help..."
        $ show_side_cecilia = True
        $ fadein_sideimage = False
        C pout "It's so annoying that they took away our cell phones."
        C "How are we supposed to pass the time when we get bored?"
        Y worried "I don't know... Maybe look for ways to escape with our lives?"
        C thinking "I'm just saying that if we're supposed to be characters in some cursed manor story..."
        C "Wouldn't it be spookier if there was simply no reception here?"
        play ctc_sfx sfx_emotequestion
        Y surprised "...Huh? Is this a [t_clue]cursed manor[t_cluee]?"
        C surprised "...!"
        C thinking "I-I don't know..."
        C pout "Anyways, I just wanna play games! I gotta feed my porcupines before the daily reset!" with shakeonce
        $ fadein_sideimage = True
        I "...? That was...a weird reaction..."
        $ show_side_cecilia = False
    return

label d1a1_check_stove:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 0.1 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue4 == False:
        I "That's...a [t_pacclue]stove[t_paccluee], right?"
        Y thinking "....."
        I "Nope, none of the buttons or the knobs do anything. Guess it's broken..."
        $ _last_say_who = "C"
        scene bg kitchen
        show cecilia at mycenter
        with dissolve
        C "The stove doesn't work, huh? Must be due to the power outage."
        C thinking "Wait... This looks like a gas stove, doesn't it? So maybe if we had something to ignite it..."
        Y surprised "You mean like some matches?"
        C default "Matches, or a lighter, yeah. Let's take a look."
        $ renpy.music.set_volume(0.5, 1.5, channel="music")
        scene bg black with dissolvemed
        pause 1.0
        $ renpy.music.set_volume(1.0, 1.5, channel="music")
        scene bg kitchen
        show cecilia sad at mycenter
        with dissolvemed
        C "No luck, huh? Darn."
        Y annoyed "Yeah... Guess dinner will have to be a little cold toni--"
        C sobbing "No chance of us using fire as a murder weapon, then."
        play ctc_sfx sfx_emoteshout
        Y panicked "THAT'S what you're upset about?!" with shakeonce
        if not d1a1_kitchen_clue4:
            $ investigation_clues_required_found += 1
            $ d1a1_kitchen_clue4 = True
    else:
        I "The [t_pacclue]stove[t_paccluee] is still broken."
        $ show_side_cecilia = True
        C thinking "I guess if you think about it realistically, it'd be hard to murder someone with fire when we're all stuck in the same house."
        $ fadein_sideimage = False
        Y worried "Yes. Let's be realistic here."
        $ show_side_cecilia = False
        $ fadein_sideimage = True
    return

label d1a1_check_knives:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 0.5 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue5 == False:
        I "A [t_pacclue]knife rack[t_paccluee]... With knives."
        I "Very...sharp knives."
        Y sad "....."
        I "I guess it makes sense for them to be in a kitchen, but..."
        I "...Wait. Is one of them missing?"
        $ show_side_cecilia = True
        C smile "Oh [name_player]~ Look here!"
        $ show_side_cecilia = False
        scene bg kitchen
        show cecilia smile at mycenter
        with dissolve
        Y default "What is it--{w=0.2}{nw}"
        $ fadein_sideimage = False
        play ctc_sfx sfx_knifebrandish
        show cecilia_raw happy knife as cecilia at mycenter_closeup
        show bg kitchen:
            matrixcolor BrightnessMatrix(-0.25)
            linear 3.0 matrixcolor BrightnessMatrix(0.0)
        with custom_flashquick()
        extend afraid " GAAAH, WHAT ARE YOU DOING." with shakeonce
        $ fadein_sideimage = True
        show cecilia happy knife at myright, doublehop:
            zoom 1.0
        $ renpy.music.set_pan(0.65, 0.0, channel='ctc_sfx')
        play ctc_sfx sfx_knifeswing
        C "Look how shinyyyy! Everything else is a little dusty, but here's this knife, glistening in the moonlight~" with custom_flashquick()
        $ renpy.music.set_pan(-0.65, 0.0, channel='ctc_sfx')
        play ctc_sfx sfx_knifeswing
        show cecilia blink knife at shudder with custom_flashquick()
        Y shouting "Can you stop waving that around?!" with shakeshort
        $ renpy.music.set_pan(0.0, 0.0, channel='ctc_sfx')
        play ctc_sfx sfx_knifeequip
        $ _last_say_who = "C"
        show cecilia wink
        pause 0.2
        show cecilia wink at mycenter with movequick
        C "Oh, don't be such a scaredy cat, [name_player]."
        C blush "I'm just appreciating the efforts spent to make this place so unsettling~"
        I "Is that something a kidnapping victim ought to be appreciating?!" with shakeonce
        C thinking "Oh wait, [name_player], look at this."
        scene bg kitchen:
            xalign 0.5 yalign 0.6 zoom 1.8
        with dissolve
        pause 1.0
        Y thinking "...What, the other knives?"
        $ show_side_cecilia = True
        $ fadein_sideimage = False
        play ctc_sfx sfx_emotehappy
        C overjoyed "The way the knife rack is prominently placed on this island... Reminds you of those legendary swords in games, doesn't it?" with vpunch
        Y worried "You're having way too much fun here, and that scares me. In many ways."
        $ show_side_cecilia = False
        $ fadein_sideimage = True
        scene bg kitchen with dissolve
        if not d1a1_kitchen_clue5:
            $ investigation_clues_required_found += 1
            $ d1a1_kitchen_clue5 = True
    else:
        I "The [t_pacclue]knife rack[t_paccluee]..."
        I ".....{w=1.0} ...Wait."
        Y blink "Cecilia?"
        $ _last_say_who = "C"
        scene bg kitchen
        show cecilia at mycenter
        with dissolve
        C "Yes, [name_player]?"
        Y "You see how there's a knife missing from this rack?"
        C thinking "Hmm?"
        scene bg kitchen:
            xalign 0.5 yalign 0.6 zoom 1.8
        with dissolve
        $ show_side_cecilia = True
        C thinking "....."
        I "......."
        C surprised "Oh whaddya know, you're right!"
        play ctc_sfx sfx_emotesigh
        I "You didn't need to stare for that long to notice..." with hpunch
        $ show_side_cecilia = False
        scene bg kitchen
        show cecilia at mycenter_fadein
        with dissolve
        Y leering "Where did the knife go, Cecilia?"
        C blink "Who can say...? Maybe a ghost took it?"
        Y worried "....." with shakeonce
        I "The real mystery is where did she put away such a large knife on her outfit...?"
    return

label d1a1_check_microwave:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 0.4 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue6 == False:
        I "...Huh? That's..."
        $ show_side_cecilia = True
        C happy "Oh, it's a [t_pacclue]microwave[t_paccluee]!"
        $ fadein_sideimage = False
        play ctc_sfx sfx_emotequestion
        Y thinking "Isn't that a [t_clue]microwave oven[t_cluee]?"
        C surprised "What's the difference?"
        Y worried "I don't know, I always thought those two were different..."
        C thinking "Huh... Maybe they are..."
        C default "But I dunno, [name_player], at the end of the day, language is just a tool for communication."
        C happy "As long as everyone knows what's being talked about, who cares about the little details?"
        I "Yeah... This certainly isn't worth having more than one dispute over..."
        $ fadein_sideimage = True
        $ show_side_cecilia = False
        if not d1a1_kitchen_clue6:
            $ investigation_clues_optional_found += 1
            $ d1a1_kitchen_clue6 = True
    else:
        I "A [t_pacclue]microwave[t_paccluee]."
        I "....."
        play ctc_sfx sfx_emotesigh
        I "Yes, it's a [t_clue]microwave[t_cluee]. Moving on..." with hpunch
        $ show_side_cecilia = True
        C smile "....."
        $ show_side_cecilia = False
    return

label d1a1_check_pot:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 0.25 yalign 0.55 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue7 == False:
        I "A [t_pacclue]metal pot[t_paccluee]. Wonder what's inside it..."
        Y "....."
        $ fadein_sideimage = False
        Y blink "It's empty..."
    else:
        I "A [t_pacclue]metal pot[t_paccluee]. It's empty."
    $ show_side_cecilia = True
    C smile "Hmm? What's up, [name_player]? Thinking of putting that on your head?"
    $ fadein_sideimage = False
    Y thinking "Huh? Why would I do that?"
    C blink "Well, beginner adventurers need to start out with {i}something{/i}, right? Even a pot helmet could give you a couple extra defense points."
    C smug "You never know; a single point could be the difference between one HP and game over."
    Y worried "....."
    $ fadein_sideimage = True
    if d1a1_kitchen_clue7 == False:
        I "Was I supposed to understand that?"
    else:
        I "...Nope, still don't get it."
    $ show_side_cecilia = False
    if not d1a1_kitchen_clue7:
        $ investigation_clues_optional_found += 1
        $ d1a1_kitchen_clue7 = True
    return

label d1a1_check_kitchenwindow:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 0.0 yalign 0.4 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A small [t_pacclue]window[t_paccluee]. Looks like it's the type to slide up and down..."
    Y leering "Mrgh... " with shakeonce
    $ fadein_sideimage = False
    Y sad "Yeah, looks like it's not gonna budge..."
    $ show_side_cecilia = True
    C sad "I really wish these types of windows were built with handles, y'know?"
    C thinking "Especially on cold and humid days, the glass gets all slippery so you can't push them open with your palm..."
    Y thinking "Huh? Can't you just tug on the frame with your fingers?"
    C pout "Not if you care about your nails! I keep a very strict routine to make these babies shine!" with shakeonce
    Y panicked "R-right. Good for you."
    I "...Hmm... But yeah, it would hurt if my nails got caught. I should leave this window alone."
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    if not d1a1_kitchen_clue8:
        $ investigation_clues_optional_found += 1
        $ d1a1_kitchen_clue8 = True
    return

label d1a1_check_kitchendrawer:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 0.0 yalign 1.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue9 == False:
        I "There are so many [t_pacclue]drawers[t_paccluee] down here. Guess there's no getting around having to open each of these..."
        $ show_side_cecilia = True
        C "Hmm? Are we opening drawers, [name_player]?"
        $ fadein_sideimage = False
        Y "Yeah, could you give me a hand?"
        $ renpy.music.set_volume(0.5, 1.5, channel="music")
        scene bg black with dissolvemed
        play sound sfx_drawer_open
        $ fadein_sideimage = True
        Y thinking "....."
        play sound [sfx_drawer_close, sfx_drawer_open]
        $ fadein_sideimage = False
        C sad "It's all just boring kitchen supplies and cooking tools, [name_player]..."
        play sound sfx_drawer_open
        Y worried "Yeah, I expected as much... Still, we had to be sure, you know...?"
        C blink "Mhm, I get it. Sometimes things can jump out of unexpected places."
        if d1a1_kitchen_clue2:
            I "At least there aren't any more poisons..." with hpunch
        Y thinking "Okay, let's just close all these again."
        play sound [sfx_drawer_close, sfx_drawer_close]
        window auto hide
        pause 1.0
        $ show_side_cecilia = False
        $ fadein_sideimage = True
        $ renpy.music.set_volume(1.0, 1.5, channel="music")
        scene bg kitchen
        show cecilia at mycenter
        with dissolvemed
        I "Probably wasn't the best use of our time..."
    else:
        I "Searching the [t_pacclue]drawers[t_paccluee] didn't turn up anything..."
        I "No point in wasting time, going through them all again..."
        $ _last_say_who = "C"
        scene bg kitchen
        show cecilia sweatdrop at mycenter
        with dissolve
    play ctc_sfx sfx_emotesigh
    C sweatdrop "Aww, don't look so disappointed, [name_player]."
    if d1a1_kitchen_clue2:
        C thinking "Gotta say though, the tidiness of this kitchen is world-class. Everything's so neatly organized and put away..."
        C happy "If only I could get whoever did this to clean up {i}my{/i} kitchen, heehee~"
        I "Yeah, assuming they're not a kidnapper out to kill us, that'd be nice..."
    else:
        C smug "Let's keep our chins up! We'll definitely find something interesting here!"
        I "\"Chins [t_clue]up[t_cluee]\"...? ..... ...Hmm, I guess we only checked out the cabinets by the floor so far..."
    if not d1a1_kitchen_clue9:
        $ investigation_clues_optional_found += 1
        $ d1a1_kitchen_clue9 = True
    return

label d1a1_check_peppershaker:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg kitchen:
        xalign 1.0 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_kitchen_clue10 == False:
        I "Huh? Why is there a single [t_pacclue]pepper shaker[t_paccluee] on this counter?"
        Y thinking "Uh... Cecilia? Was this always here?"
        $ fadein_sideimage = False
        $ show_side_cecilia = True
        C surprised "Hmm? Oh! No, I pulled that outta one of the drawers."
        Y default "....."
        C default "....."
        Y thinking "...Uh... Wh-why?"
        C blink "Well, if you MUST know..."
        C smile "I wanted to see if it's actually possible to force a sneeze with it."
        Y worried "...Why does that not surprise me?"
        C sad "I fumbled and dropped it before I could give it a shot, though. That's why there isn't much left."
        play ctc_sfx sfx_emotehappy
        C overjoyed "Oooh, come to think of it, you know how they say spilling salt is bad luck? I wonder if it's the opposite for pepper?" with vpunch
        $ fadein_sideimage = True
        I "With the way I'm feeling right now, probably not..."
        $ show_side_cecilia = False
        if not d1a1_kitchen_clue10:
            $ investigation_clues_optional_found += 1
            $ d1a1_kitchen_clue10 = True
    else:
        I "A nearly empty [t_pacclue]pepper shaker[t_paccluee] that Cecilia played with."
        Y blink "Of all the things someone can play wi..."
        $ fadein_sideimage = False
        Y worried "...Wuh..." with hpunch
        play sound sfx_emoteshout
        Y scream "{size=+20}WAHCHOO!!{/size}" with shakeshort
        $ show_side_cecilia = True
        C happy "Nice one, [name_player]! Great form!"
        $ show_side_cecilia = False
        $ fadein_sideimage = True
        play ctc_sfx sfx_emotesigh
        I "Ugh... There must still be some pepper floating around this part of the room..." with hpunch
    return



label d1a1_check_diningroomwindow:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.0 yalign 0.7 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "The [t_pacclue]window[t_paccluee]..."
    Y default "....."
    $ fadein_sideimage = False
    Y thinking "......."
    $ fadein_sideimage = True
    $ _last_say_who = "C"
    show cecilia at mycenter with dissolve
    C "Hmm? Whatcha thinkin' about, [name_player]?"
    Y default "Just...that fog outside is really thick."
    C thinking "Yeah, we can't see a thing past the glass. Not even the ground just outside."
    show cecilia happy at hop
    C "Ooh, I wonder if we're floating up in the sky or something? Maybe that fog is actually a cloud!"
    Y thinking "I'm pretty sure houses are incapable of flying..."
    C blink "Nah, haven't you heard of that story?"
    C happy "The one where a twister ripped a house off the ground, and transported it to a fantasy world!"
    Y surprised "A twister...picked a house up off the ground and transported it somewhere? That's even more unbelievable."
    $ fadein_sideimage = False
    Y thinking "At least with a flying house, there are more realistic ways it could take flight."
    Y default "Like...what if you filled up a countless number of helium balloons, and attached it to--"
    $ fadein_sideimage = True
    C sad "I'm gonna stop you right there because I'm not sure if that's something we're allowed to talk about."
    Y surprised "Huh? \"Allowed to\"...?"
    C default "Anyways, every window here just [t_clue]won't open or break[t_cluee], so there's not much else we can do with them."
    Y sad "Opening is one thing, but I wonder why it won't break?"
    C thinking "I guess it must be reinforced to make sure we can't break out."
    C smug "But I'm sure if I can find something heavier to use, it'll break for sure."
    Y worried "Not that I don't have faith in your brute strength or anything but..."
    $ fadein_sideimage = False
    Y thinking "It feels very odd that the wooden chair would break before making even a crack..."
    $ fadein_sideimage = True
    if not d1a1_diningroom_clue1:
        $ investigation_clues_optional_found += 1
        $ d1a1_diningroom_clue1 = True
    return

label d1a1_check_petbowl:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.3 yalign 1.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_diningroom_clue2:
        I "...Hmm?"
        scene bg diningroom withchair:
            xalign 0.3 yalign 1.0 zoom 1.5
            easein 0.75 zoom 2.5
        pause 1.0
        $ show_side_cecilia = True
        C "[name_player]? Did you find something?"
        $ fadein_sideimage = False
        Y surprised "Yeah, some...small bowl?"
        C happy "Ooh, that's a [t_pacclue]pet bowl[t_paccluee]! There must have been a cat or a dog living here!"
        $ fadein_sideimage = True
        if d1a1_checked_bathroom:
            I "It must be for that dog from earlier..."
        else:
            I "A cat or dog, huh...?"
        $ show_side_cecilia = False
        scene bg diningroom withchair
        with dissolve
        $ _last_say_who = "C"
        show cecilia at mycenter
        with dissolve
        C "Hey, [name_player], would you say you're a cat person or a dog person?"
        Y surprised "Huh? Where's this coming from?"
        C smile "Just curious, come on!"
        Y thinking "Well, if I had to choose...{nw}"
        $ fadein_sideimage = False
        $ preferred_pet = ""

        menu:
            extend ""
            "Cats":
                $ preferred_pet = "cat"
                Y default "Definitely a cat person."
                Y blink "I like how they're self-sufficient and keep an air of mystery about them."
                Y relaxed "Makes it all the more endearing when they cuddle up to you."
                $ fadein_sideimage = True
                C surprised "I see... That's quite a thought-out answer..."
                I "Well, I don't have any memories, so that was pretty much all made-up..."
            "Dogs":
                $ preferred_pet = "dog"
                Y default "I guess dogs?"
                Y relaxed "They're always really eager to spend time with you."
                Y happy "Plus it's cute how you can always tell how they're feeling for the most part."
                $ fadein_sideimage = True
                C smug "Ohooo~ So that sort of thing is important to you, huh...?"
                I "I mean, I wouldn't know. I don't have any of my memories."
            "Neither":
                $ preferred_pet = "none"
                Y worried "I can't say I lean either way."
                $ fadein_sideimage = True
                I "Mostly because I don't remember anything about myself..."
                C sad "Aw. Lame."
        Y default "What about you, Cecilia? Cats or dogs?"
        C surprised "Me?"
        C thinking "Hmm..."
        C "....."
        C sweatdrop "...I guess neither. I'm more of a porcupine gal."
        Y annoyed "....."
        show cecilia pout at doublehop
        C "What's that look for? You've never seen a porcupine's nose before, have you?"
        C blink "Plus they're born with quills all over that are soft at first, but as they mature, the quills turn into prickly spikes..."
        C smile "Kinda like us humans, right? So soft, then growing up to be so prickly, so guarded...{w=1.0}{nw}"
        play ctc_sfx sfx_emotehappy
        show cecilia happy at shudder
        extend " Ehueheh~ There's nothing cuter~ [u_heart]"
        Y worried "...Okay, good talk. Let's get back to work, porcupine gal."
        if not d1a1_diningroom_clue2:
            $ investigation_clues_required_found += 1
            $ d1a1_diningroom_clue2 = True
    else:
        I "Just a [t_pacclue]pet bowl[t_paccluee] over there. Nothing else."
        if preferred_pet == "cat" or preferred_pet == "dog":
            $ _last_say_who = "C"
            scene bg diningroom withchair
            show cecilia thinking at mycenter
            with dissolve
        if preferred_pet == "cat":
            C "Hey, [name_player]? You said you were a cat person, right?"
            C default "Does that mean you don't like dogs?{nw}"
            menu:
                extend ""
                "\"Yeah, I hate dogs.\"":
                    Y blink "Yeah, I'm not a fan. They're really high maintenance."
                    $ fadein_sideimage = False
                    Y sad "I don't think I have the stamina to play with them all the time."
                    $ fadein_sideimage = True
                    C blink "...You don't, huh...?"
                    I "...?"
                "\"No, dogs are fine.\"":
                    Y thinking "I wouldn't say that. I just have a preference. One over the other." with shakeonce
                    C blink "Fair enough. I guess I was just curious if you would cringe at adamant dog lovers."
                    Y worried "That's...an odd thing to worry about."
                    C smile "Eh... You never know~"
                    I "Huh?"
        if preferred_pet == "dog":
            C "Hey, [name_player]? You said you were a dog person, right?"
            C default "Does that mean you don't like cats?{nw}"
            menu:
                extend ""
                "\"Yeah, I hate cats.\"":
                    Y sad "Yeah, not really. They can be really cold and distant."
                    $ fadein_sideimage = False
                    Y blink "Plus they just sleep on whatever, no matter how inconvenient it may be for their owners."
                    Y annoyed "Frankly, I don't understand why people tolerate how high and mighty they--"
                    $ fadein_sideimage = True
                    show cecilia surprised at hop
                    C "Whoa, those are some bold statements! You might want to reel that in a little!"
                    Y surprised "Why? I'm just saying--"
                    play ctc_sfx sfx_emotesob
                    show cecilia sobbing at shrink
                    C "Okay okay, I'm sorry I asked. Let's just move on before anyone flames us in the reviews..."
                    show cecilia determined at mycenter_closeup with shakeonce
                    C "Reminder: \"Opinions expressed by the characters of this work are not necessarily shared by the author.\""
                    I "...Who is she talking to?"
                "\"No, cats are fine.\"":
                    Y default "Cats are okay. I just like dogs a little more."
                    C blink "...I see. {size=-10}...the same...{/size}"
                    Y thinking "Huh? What'd you say?"
                    C happy "Nothing! Let's keep looking around, [name_player]!"
    return
label d1a1_check_table:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.5 yalign 1.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_diningroom_clue3:
        I "A big [t_pacclue]table[t_paccluee]. Wouldn't be a good dining room without it."
        Y "So this table has four chairs total?"
        $ show_side_cecilia = True
        $ fadein_sideimage = False
        C blink "Yep. Well, three now. No other chairs, from where I could see."
        C smug "Guess this means there must have been a [t_clue]family of four[t_cluee] living here!"
        Y thinking "Hmm..."
        $ fadein_sideimage = True
        $ show_side_cecilia = False
        $ _last_say_who = "C"
        scene bg diningroom withchair
        show cecilia sweatdrop at mycenter
        with dissolve
        C "...Uh... Something wrong, [name_player]? You're giving a simple table quite the detailed inspection."
        C sad "I think I mentioned this before, but there's really not that much to check out here.{nw}"

        menu:
            extend ""
            "\"Yeah, you're right...\"":
                Y blink "Yeah, you're right... Guess that's about all we're gonna learn from this."
                C happy "Come on, [name_player], let's check someplace else!"
            "\"But isn't that strange?\"":
                Y thinking "But isn't that strange?"
                C surprised "Hmm? What is?"
                Y default "I mean...there are plenty of signs that indicate there was a big family living here."
                $ fadein_sideimage = False
                Y thinking "But everything here is just...barren."
                Y "Nothing out in the open, and a layer of dust is on the table..."
                Y blink "It's like [t_clue]no one's lived here for a long time[t_cluee]."
                $ fadein_sideimage = True
                C surprised "...Oooooooh."
                play ctc_sfx sfx_emotehappy
                show cecilia overjoyed at hop
                C "Wow, you're a smart cookie, [name_player]!"
                Y surprised "...Th-thanks, but that's all you have to say?"
                C thinking "I mean, what else do you want me to say?"
                C default "If no one's lived here for a long time, that just means we're probably alone in this house with the culprit."
                C blink "We can't bank on the family that lived here to come to our rescue. Who knows, they might even be in on it."
                C smug "So...that observation you made isn't exactly a shimmering ray of hope, now is it?"
                Y worried "...Mrgh..." with shakeonce
                C happy "Don't worry, [name_player], I still think you're a smart cookie!"
                I "Now I'm bummed out... Maybe I should have just stayed quiet..."
                Y sad "Okay, let's look for clues that might help us get out of here."
        if not d1a1_diningroom_clue3:
            $ investigation_clues_required_found += 1
            $ d1a1_diningroom_clue3 = True
    else:
        I "It's just a [t_pacclue]table[t_paccluee]. Let's move on."
    return
label d1a1_check_candelabra:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.65 yalign 0.7 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "It's...some metal fixture holding three candles..."
    $ show_side_cecilia = True
    play ctc_sfx sfx_emotehappy
    C overjoyed "Wow, a real-life [t_pacclue]candelabra[t_paccluee]! So fancy~"
    $ fadein_sideimage = False
    Y surprised "A can-da...what?"
    C default "It's basically a classy decoration nowadays. You light these candles and enjoy the ambience with your meal."
    Y relaxed "Huh... Yeah, I can see that being relaxing."
    C happy "And then once the candles melt off, you can use the spikes and make a distinct three-holed stab wound on someone!"
    Y worried "Now I'm less relaxed..."
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    if not d1a1_diningroom_clue4:
        $ investigation_clues_optional_found += 1
        $ d1a1_diningroom_clue4 = True
    return

label d1a1_check_chandelier:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.7 yalign 0.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    Y panicked "Uh... Wh-what's that thing hanging above the table...?"
    $ show_side_cecilia = True
    $ fadein_sideimage = False
    C surprised "Hm? You've never seen a [t_pacclue]chandelier[t_paccluee] before?"
    C default "It's like the fanciest form of overhead lighting. I bet it's real pretty if we turn it on."
    Y sad "So that's definitely not gonna come crashing down?"
    C sweatdrop "I didn't think you were the type to worry about that, [name_player]..."
    C thinking "Although it {i}does{/i} look pretty old. Might be wise to avoid touching it."
    I "The things people do just for aesthetic..." with hpunch
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    if not d1a1_diningroom_clue5:
        $ investigation_clues_optional_found += 1
        $ d1a1_diningroom_clue5 = True
    return

label d1a1_check_flowervase:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.95 yalign 0.8 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_diningroom_clue6:
        I "A small [t_pacclue]flower vase[t_paccluee]. The flower in it is wilting."
        I "...? Wait a second..."
        Y panicked "This flower is artificial!" with hpunch
        $ show_side_cecilia = True
        $ fadein_sideimage = False
        C surprised "Huh? Oh, you're right!"
        C thinking "If they're gonna put an artificial flower in here, why pick one that's shaped like it's wilting?"
        Y worried "Don't ask me..."
        $ show_side_cecilia = False
        $ fadein_sideimage = True
        if not d1a1_diningroom_clue6:
            $ investigation_clues_optional_found += 1
            $ d1a1_diningroom_clue6 = True
    else:
        I "A small [t_pacclue]flower vase[t_paccluee]. The wilting flower in it is artificial for whatever reason."
        $ show_side_cecilia = True
        C thinking "Y'know, maybe the flower is a metaphor. Like, a reminder of how death is a stagnant constant in our lives?"
        $ fadein_sideimage = False
        Y worried "And they need that reminder during mealtime...?"
        $ show_side_cecilia = False
        $ fadein_sideimage = True
    return

label d1a1_check_chinacabinet:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.7 yalign 0.65 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A [t_pacclue]china cabinet[t_paccluee]. From what I can see, it's filled with fancy plates and stuff."
    play sound sfx_doorrattle
    I "...Hrm. It's locked." with shakeonce
    $ show_side_cecilia = True
    C sweatdrop "I've never understood the point of caging away china like this. Plates are meant for eating off of, y'know?"
    $ fadein_sideimage = False
    Y "But in terms of decor for a dining room, it makes sense. Food-related objects to adorn a room meant for eating food?"
    C surprised "Oh, I never thought of that!"
    C thinking "Mmm... But if that's the case, couldn't you get by with using paper plates as decorations?"
    C surprised "Ooh, especially if you jazz them up with some illustrations... Maybe some lace and glitter... And stick them to the walls!"
    play ctc_sfx sfx_emotehappy
    C overjoyed "Yeah, this could work! A paper plate-themed dinner party! Creative, fun for kids, and easy on the wallet!" with vpunch
    play ctc_sfx sfx_emotesigh
    Y worried2 "Now's not the time to be planning dinner parties, Cecilia..." with hpunch
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    if not d1a1_diningroom_clue7:
        $ investigation_clues_optional_found += 1
        $ d1a1_diningroom_clue7 = True
    return

label d1a1_check_diningroompainting:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.95 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A large [t_pacclue]painting[t_paccluee] of...something."
    Y thinking "...?"
    $ show_side_cecilia = True
    $ fadein_sideimage = False
    C default "Something wrong, [name_player]? You're staring awfully hard at that painting."
    Y "Yeah, I'm just at a loss as to what this even is."
    C thinking "Hmm... I suppose it {i}is{/i} pretty abstract."
    C default "Well, what's the first description that comes to mind?"
    Y surprised "Hmm... A warrior? Or maybe a bird?"
    C blink "I see. So you're the type to not back down from violence, and your deepest wish is to take flight and be free."
    play ctc_sfx sfx_emotequestion
    C smile "Sounds like you'll have an [t_clue]important choice[t_cluee] to make soon..."
    Y worried "...On second thought, I see nothing. Let's move on."
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    if not d1a1_diningroom_clue8:
        $ investigation_clues_optional_found += 1
        $ d1a1_diningroom_clue8 = True
    return

label d1a1_check_brokenchair:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.95 yalign 1.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_diningroom_clue9:
        I "The [t_pacclue]broken chair[t_paccluee]. Hard to imagine Cecilia swinging this around..."
        Y thinking "....."
        I "Maybe I should clean this up..."
        $ show_side_cecilia = True
        C surprised "Ah! [name_player], it's okay! I can take care of that later!" with hpunch
        $ fadein_sideimage = False
        Y sad "But it's sort of dangerous... Shouldn't we at least move it somewhere out of the way?"
        C pout "Don't you know the number one rule of investigating?"
        C "\"Don't mess with the crime scene!\"" with shakeonce
        Y thinking "But there wasn't any crime here..."
        C surprised "Sure there was! Property damage, for one!"
        Y worried "But...that was you."
        C sad "Yeah, I know! That's why I need to make reparations and clean it up myself!" with hpunch
        Y worried2 "....."
        play ctc_sfx sfx_emotesigh
        $ fadein_sideimage = True
        I "I'm confused. Guess I'll just leave it alone." with hpunch
        $ show_side_cecilia = False
        if not d1a1_diningroom_clue9:
            $ investigation_clues_optional_found += 1
            $ d1a1_diningroom_clue9 = True
    else:
        I "The [t_pacclue]broken chair[t_paccluee]. For some reason, Cecilia wants to clean this up by herself later..."
        I "I wonder if she's hiding something...?"
        I "...Or maybe things will just be more [t_clue]convenient for everyone[t_cluee] if we leave it like this."
    return

label d1a1_check_kitchenentrance:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 1.0 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "We can see the [t_pacclue]kitchen[t_paccluee] from here."
    $ show_side_cecilia = True
    C "Hmm? Are you heading back to the kitchen, [name_player]?"
    if not d1a1_diningroom_clue2 or not d1a1_diningroom_clue3:
        I "Mrm... I still feel like there's something left to find here... But maybe the kitchen's more important...?{nw}"
    else:
        I "Yeah, something tells me there's nothing important left here...{nw}"

    menu:
        extend ""
        "Return to the [t_clue]Kitchen[t_cluee]":
            if not d1a1_diningroom_clue2 or not d1a1_diningroom_clue3:
                Y default "Let's go back to the kitchen."
                $ fadein_sideimage = False
                C smile "Good idea! Most of the interesting clues are over there."
                $ fadein_sideimage = True
            else:
                Y blink "Yeah, I think we covered everything important here."
                $ fadein_sideimage = False
                C smile "Back to the kitchen, then? Okay dokay~"
                $ fadein_sideimage = True
            play ctc_sfx sfx_steps
            play sound ["<silence 0.2>", sfx_steps]
            scene bg black with fade
            scene bg kitchen with fade
            pause 2.0
            $ investigation_location = "d1a1_kitchen"
        "Stay here":
            I "No, let's take another look around here first..."
    $ show_side_cecilia = False
    if not d1a1_diningroom_clue10:
        $ investigation_clues_optional_found += 1
        $ d1a1_diningroom_clue10 = True
    return
label d1a1_check_chairfragments:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg diningroom withchair:
        xalign 0.2 yalign 0.7 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "Wooden [t_pacclue]fragments[t_paccluee]..."
    I "...It's probably safe to say these came from when Cecilia swung the chair and smashed it."
    scene bg diningroom withchair with dissolve
    I "Hmm... But wait, now that I think about it, I wonder why she didn't use the chair closest to this window?"
    I "Maybe she tossed it aside over there in a fit of frustration? Or swapped the chairs around afterwards for...some reason?"
    $ show_side_cecilia = True
    C default "...?"
    $ show_side_cecilia = False
    play ctc_sfx sfx_emotesigh
    I "...Both of those are scary images. Maybe I should let this go." with hpunch
    if not d1a1_diningroom_clue11:
        $ investigation_clues_optional_found += 1
        $ d1a1_diningroom_clue11 = True
    return




screen pac_d1a1_bathroom:
    style_prefix "pac"

    use pac_progress_gui(_("The Bathroom with..."))




    use pac_end_button("d1a1_bathroom_confirm_end", investigated_bathroom)


    use pac_button(1440, 800, d1a1_bathroom_clue0, "d1a1_check_door", _("Door"))

    use pac_button(420, 250, d1a1_bathroom_clue1, "d1a1_check_mirror", _("Mirror"))
    use pac_button(860, 570, d1a1_bathroom_clue2, "d1a1_check_toilet", _("Toilet"))
    use pac_button(900, 290, d1a1_bathroom_clue3, "d1a1_check_bathroomwindow", _("Window"))
    use pac_button(1075, 740, d1a1_bathroom_clue4, "d1a1_check_trashcan", _("Waste Bin"))
    use pac_button(600, 720, d1a1_bathroom_clue5, "d1a1_check_sink", _("Sink"))

    use pac_button(190, 860, d1a1_bathroom_clue6, "d1a1_check_towel", _("Towel"))
    use pac_button(260, 110, d1a1_bathroom_clue7, "d1a1_check_bathroomlights", _("Lights"))
    use pac_button(420, 660, d1a1_bathroom_clue8, "d1a1_check_soap", _("Soap"))
    use pac_button(760, 590, d1a1_bathroom_clue9, "d1a1_check_paperroll", _("Paper Roll"))
    use pac_button(1630, 610, d1a1_bathroom_clue10, "d1a1_check_lightswitch", _("Light Switch"))
    use pac_button(960, 920, d1a1_bathroom_clue11, "d1a1_check_bathmat", _("Bath Mat"))



label d1a1_bathroom_complete:
    I "...Maybe I'm just wasting time here..."
    I "I should [t_clue]end my investigation[t_cluee]."
    return

label d1a1_bathroom_perfect:
    I "...All right, for some reason, I checked everything thoroughly..."
    I "Now I REALLY should [t_clue]end my investigation[t_cluee] and move on."
    return

label d1a1_bathroom_confirm_end:
    if investigated_bathroom and not investigation_complete:
        I "...Why does this room feel familiar? Like, as if I already checked everything here...?"
        I "Maybe I should just stop here, save some time?{nw}"

        menu:
            extend ""
            "Skip this investigation":
                if d1a1_sink_on:
                    I "...I should turn off the sink before I leave."
                else:
                    scene bg bathroom
                    with fade
                    $ fadein_sideimage = True
                    I "...Yeah, something tells me it really won't be worth it to search around here any more..."
                    I "I should try checking out another place."
                    $ investigation_location = None
            "Cancel":
                I "...On second thought, it can't hurt to be thorough..."
    else:
        I "Should I wrap up my investigation here?{nw}"
        menu:
            extend ""
            "End your investigation":
                if d1a1_sink_on:
                    I "...I should turn off the sink before I leave."
                else:
                    scene bg bathroom
                    with fade
                    $ fadein_sideimage = True
                    I "It's a small bathroom so...I guess that's all the clues I'm gonna be getting."
                    I "Nothing useful came out of this... Welp, can't say I didn't try."
                    $ investigation_location = None
            "Cancel":
                I "...No, let's look around a bit more."
    return
label d1a1_check_door:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 1.0 yalign 0.9 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 1.0 yalign 0.9 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    I "The [t_pacclue]door[t_paccluee] that I came in through. Past it is the foyer.{nw}"

    menu:
        "[t_clue]End your investigation[t_cluee]" if investigation_perfect:
            call d1a1_bathroom_confirm_end
        "\"Any ideas?\"":
            if not d1a1_bathroom_clue1:
                I "...Something tells me that I won't find anything important here..."
                I "I guess at the very least, I should take a [t_clue]good look at my own face[t_cluee], and see if any of my memories come back..."
            else:
                I "Hmm... Looking at my own face didn't bring back any memories..."
                I "And I don't think there'll be much else I can figure out on my own..."
                Y sad "....."
                I "...Yeah, I should wrap this up soon. Is there anywhere else a clue could be hiding...?"
        "\"Never mind...\"":
            pass
        extend ""
    if not d1a1_bathroom_clue0:
        $ investigation_clues_optional_found += 1
        $ d1a1_bathroom_clue0 = True
    return
label d1a1_check_mirror:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.0 yalign 0.1 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.0 yalign 0.1 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_bathroom_clue1 == False:
        if not d1a1_checked_upstairs:
            Y surprised "The [t_pacclue]mirror[t_paccluee]..."
            scene cg mirror:
                xalign 0.4 yalign 0.4 zoom 1.3
                easein 6.0 xalign 0.5 yalign 0.5 zoom 1.0
            with dissolvemed
            $ persistent.unlock_cg_mirror = True
            pause 2.0
            $ show_side_player = True
            Y surprised "....."
            $ fadein_sideimage = False
            Y "...So this is [t_clue]my face[t_cluee]?"
            Y thinking "Other than my name, I can't remember anything about myself..."
            Y default "But I guess deep down, this face kinda looks familiar..."
            $ fadein_sideimage = True
            if d1a1_sink_on:
                scene bg bathroom sinkon with dissolve
            else:
                scene bg bathroom with dissolve
            Y blink "....."
            $ fadein_sideimage = False
            Y default "...Okay, that's enough staring. Let's keep looking." with hpunch
            $ fadein_sideimage = True
        else:
            I "There's a [t_pacclue]mirror[t_paccluee] here..."
            Y default "....."
            $ fadein_sideimage = False
            Y thinking "Other than my name, I can't remember anything about myself..."
            Y default "But I guess deep down, this face kinda looks familiar..."
            Y blink "....."
            Y default "...Okay, that's enough staring. Let's keep looking." with hpunch
            $ fadein_sideimage = True
        if not d1a1_bathroom_clue1:
            $ investigation_clues_required_found += 1
            $ d1a1_bathroom_clue1 = True
    else:
        I "The [t_pacclue]mirror[t_paccluee]..."
        Y default "....."
        $ fadein_sideimage = False
        Y "Short blonde hair... Brown eyes..."
        Y wince "My eyes look kinda dead... I guess I'm still a little tired..." with hpunch
        Y sad "...Can we afford to sleep tonight, though...?"
        $ fadein_sideimage = True
    return

label d1a1_check_toilet:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.5 yalign 0.7 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.5 yalign 0.7 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    play sound sfx_toilet
    with shakeshort
    pause 2.0
    if d1a1_bathroom_clue2 == False:
        Y blink "......."
        $ fadein_sideimage = False
        Y default "No problems with the [t_pacclue]toilet[t_paccluee]."
        Y "....."
        Y thinking "...Do I need to go?{nw}"

        menu:
            extend ""
            "Use the toilet":
                Y blink "Yeah, let's take a short break..."
                play ctc_sfx sfx_emoteshout
                extend panicked " Wait, I don't need to go! What the heck am I doing?!" with shakeshort
                I "...That was...a weird impulse I just had."
                I "Is something [t_clue]controlling me[t_cluee]?"
            "Don't use the toilet":
                Y sad "...Let's not."
                Y "The thought of doing that right now feels...wrong somehow."
        $ fadein_sideimage = True
        if not d1a1_bathroom_clue2:
            $ investigation_clues_optional_found += 1
            $ d1a1_bathroom_clue2 = True
    else:
        Y blink "......."
        $ fadein_sideimage = False
        Y default "Still no problems with the [t_pacclue]toilet[t_paccluee]."
        $ fadein_sideimage = True
        I "It's an oddly satisfying sound..."
    return
label d1a1_check_bathroomwindow:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.5 yalign 0.1 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.5 yalign 0.1 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_bathroom_clue3 == False:
        Y leering "...Nngh!" with shakeonce
        $ fadein_sideimage = False
        Y "HNGGGHHH!" with shakeshort
        Y "....."
        Y worried "Yep, the [t_pacclue]window[t_paccluee]'s locked."
        Y sad "The others mentioned that all the windows were locked, so I guess this was to be expected."
        Y "We won't be able to escape from here."
        Y surprised "...Unless...{nw}"

        $ punched_window = False

        menu:
            extend ""
            "Try breaking it":
                Y leering "Alright, 3, 2..."
                $ fadein_sideimage = True
                window auto hide
                pause 0.5
                play sound sfx_punchwall
                if d1a1_sink_on:
                    scene bg bathroom sinkon:
                        xalign 0.5 yalign 0.1 zoom 2.0
                        linear 0.3 zoom 1.75
                    with shakeshort
                else:
                    scene bg bathroom:
                        xalign 0.5 yalign 0.1 zoom 2.0
                        linear 0.3 zoom 1.75
                    with shakeshort
                pause 1.0
                Y blink "....."
                $ fadein_sideimage = False
                Y pained "...Aggghhh..." with shakeonce
                $ fadein_sideimage = True
                I "Okay... That was a mistake..."
                I "Oww, my hand..."
                $ punched_window = True
            "Leave it be":
                Y thinking "...Nah, I doubt that's gonna work."
                $ fadein_sideimage = True
        if not d1a1_bathroom_clue3:
            $ investigation_clues_optional_found += 1
            $ d1a1_bathroom_clue3 = True
    else:
        I "The sole [t_pacclue]window[t_paccluee] in this bathroom."
        if punched_window == False:
            Y thinking "....."
            $ fadein_sideimage = False
            Y "Actually, should I try it...?{nw}"
            menu:
                extend ""
                "Try breaking it":
                    Y leering "Alright, 3, 2..."
                    $ fadein_sideimage = True
                    window auto hide
                    pause 0.5
                    play sound sfx_punchwall
                    if d1a1_sink_on:
                        scene bg bathroom sinkon:
                            xalign 0.5 yalign 0.1 zoom 2.0
                            linear 0.3 zoom 1.75
                        with shakeshort
                    else:
                        scene bg bathroom:
                            xalign 0.5 yalign 0.1 zoom 2.0
                            linear 0.3 zoom 1.75
                        with shakeshort
                    pause 1.0
                    Y blink "....."
                    $ fadein_sideimage = False
                    Y pained "...Aggghhh..." with shakeonce
                    I "Okay... I was right the first time..."
                    I "Oww, my hand..."
                    $ fadein_sideimage = True
                    $ punched_window = True
                "Just leave it be":
                    Y worried "N-no, come on, me, let's just look somewhere else."
                    $ fadein_sideimage = True
        else:
            I "I was an idiot to think I could punch through it..."
            if d1a1_checked_kitchen == True:
                I "Now that I think about it, if Cecilia couldn't break the dining room windows with a chair, how was {i}I{/i} gonna do any better..."
            else:
                I "Maybe if I threw something heavy at it...?"
                I "...Actually, I should run it by the others first before trying something drastic like that."
    return
label d1a1_check_trashcan:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.6 yalign 0.8 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.6 yalign 0.8 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_checked_trash == False:
        Y surprised "Oh, a [t_pacclue]waste bin[t_paccluee]!"
        $ fadein_sideimage = False
        Y "There's gotta be a clue in there, right?"
        Y default "....."
        Y worried "...The lid's stuck... I'll have to just stick my hand in...{nw}"

        menu:
            extend ""
            "Test your luck":
                $ d1a1_checked_trash = True
                call d1a1_search_trash
            "Never mind":
                Y panicked "...Wait, gross, what am I doing?!" with shakeonce
                Y annoyed "Who KNOWS what could be in there..."
                $ fadein_sideimage = True
    else:
        if d1a1_treasure_found == False:
            Y thinking "There might be more in this [t_pacclue]waste bin[t_paccluee]... Should I try sticking my hand in again...?{nw}"
            $ fadein_sideimage = False
            menu:
                extend ""
                "Test your luck":
                    call d1a1_search_trash
                "Never mind":
                    Y blink "...Nah, maybe the first time was enough."
                    Y sad "If anything's in there, it probably isn't worth the grossness."
        else:
            I "The [t_pacclue]waste bin[t_paccluee]."
            Y annoyed "...That's enough touching trash for one day."

    $ fadein_sideimage = True
    if not d1a1_bathroom_clue4:
        $ investigation_clues_required_found += 1
        $ d1a1_bathroom_clue4 = True
    return

label d1a1_search_trash:
    Y default "Alright, let's see..."
    play sound sfx_wastebin
    Y "....." with shakeonce
    $ rng = renpy.random.randint(rng_min, 21)
    if rng <= 10:
        Y "A wadded up tissue."
        Y blink "Looks about right."
    if rng > 10 and rng <= 13:
        Y "An empty roll of toilet paper."
        Y blink "I guess that makes sense."
    if rng > 13 and rng <= 16:
        Y surprised "A snack wrapper."
        Y thinking "Kinda smells like chocolate."
        Y panicked "....Wait, why the hell am I sniffing garbage?" with shakeonce
    if rng > 16 and rng <= 18:
        Y panicked "A wadded up tissue...covered in blood."
        Y sad "...I hope that's just from a nosebleed."
    if rng > 18 and rng <= 20:
        Y annoyed "...A soda can?"
        Y "Should this really be in the garbage?"
        Y worried "..... *sigh* I guess I'll put it back in here... Pretend I didn't see anything..."
    if rng == 21:
        $ renpy.music.set_volume(0.0, 3, channel="music")
        Y surprised "...Huh? There's something kinda thin and flat..."
        Y default "....."
        Y thinking "A piece of paper...with a map drawn on it?"
        $ fadein_sideimage = True
        I "It kinda looks like [t_clue]directions to a house[t_cluee]..."
        I "...Maybe it's for {i}this{/i} house? Did one of us use this to come here?"
        Y blink "....."
        $ renpy.music.set_volume(1.0, 3, channel="music")
        I "Well... Either way, this isn't going to be useful for getting us out of here..."
        I "This is probably about the most useful thing I'll find in this waste bin. I should stop rummaging now..."
        $ d1a1_treasure_found = True
    $ rng_min = rng_min + 2
    return

label d1a1_check_sink:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.1 yalign 0.8 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.1 yalign 0.8 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_bathroom_clue5 == False:
        I "A [t_pacclue]sink[t_paccluee] with two knobs."
        $ renpy.music.set_pan(-0.45, 0.0, channel='loop_sfx')
        play loop_sfx sfx_sink fadein 0.5
        scene bg bathroom sinkon:
            xalign 0.1 yalign 0.8 zoom 1.5
        with dissolve
        $ persistent.unlock_bg_bathroom_sinkon = True
        pause 1.0
        Y default "Okay, cold water works..."
        stop loop_sfx fadeout 0.5
        scene bg bathroom:
            xalign 0.1 yalign 0.8 zoom 1.5
        with dissolvequick
        pause 1.0
        play loop_sfx sfx_sink fadein 0.5
        scene bg bathroom sinkon:
            xalign 0.1 yalign 0.8 zoom 1.5
        with dissolve
        pause 1.0
        Y "And...hot water works."
        $ fadein_sideimage = False
        Y blink "Nothing unusual here, I guess."
        $ fadein_sideimage = True
        $ d1a1_sink_on = True
        if not d1a1_bathroom_clue5:
            $ investigation_clues_required_found += 1
            $ d1a1_bathroom_clue5 = True
    else:
        if d1a1_sink_on:
            Y blink "...Okay, let's turn the [t_pacclue]sink[t_paccluee] off..."
            stop loop_sfx fadeout 0.5
            scene bg bathroom:
                xalign 0.1 yalign 0.8 zoom 1.5
            with dissolvequick
            pause 1.0
            Y worried "There we go, I can THINK again, agh."
            $ d1a1_sink_on = False
            $ renpy.music.set_pan(0.0, 1.0, channel='loop_sfx')
        else:
            Y default "...Actually, let's turn the [t_pacclue]sink[t_paccluee] on again."
            $ renpy.music.set_pan(-0.45, 0.0, channel='loop_sfx')
            play loop_sfx sfx_sink fadein 0.5
            scene bg bathroom sinkon:
                xalign 0.1 yalign 0.8 zoom 1.5
            with dissolve
            pause 1.0
            Y relaxed "There's something soothing about this sound."
            $ d1a1_sink_on = True
    return

label d1a1_check_towel:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.0 yalign 1.0 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.0 yalign 1.0 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    I "A typical bathroom [t_pacclue]towel[t_paccluee] for drying hands."
    I "It's a little damp. Guess someone used it very recently."
    I "Not much else I can learn from this..."
    if not d1a1_bathroom_clue6:
        $ investigation_clues_optional_found += 1
        $ d1a1_bathroom_clue6 = True
    return

label d1a1_check_bathroomlights:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.0 yalign 0.0 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.0 yalign 0.0 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    I "Are those... No, they're [t_pacclue]lights[t_paccluee] designed to look like table lamps."
    I "Even without any light, thick layers of dust can be seen on the lampshades and the metal mounts."
    I "Not much else to say about them. Er, or think about them."
    if not d1a1_bathroom_clue7:
        $ investigation_clues_optional_found += 1
        $ d1a1_bathroom_clue7 = True
    return

label d1a1_check_soap:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.1 yalign 0.8 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.1 yalign 0.8 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    I "A [t_pacclue]soap dispenser[t_paccluee]. No label, but it smells okay enough..."
    Y thinking "Hmm... I wonder if I should wash my hands.{nw}"
    $ fadein_sideimage = False

    menu:
        extend ""
        "Wash your hands":
            if not d1a1_sink_on:
                Y default "I should have the sink running first."
            else:
                Y blink "....."
                Y default "......."
                Y "Okay, all cleaned up."
        "Don't wash your hands":
            pass
    $ fadein_sideimage = True
    if not d1a1_bathroom_clue8:
        $ investigation_clues_optional_found += 1
        $ d1a1_bathroom_clue8 = True
    return
label d1a1_check_paperroll:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.3 yalign 0.6 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.3 yalign 0.6 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    I "An empty [t_pacclue]roll of toilet paper[t_paccluee].."
    I "So inconsiderate, leaving it like this..."
    I "....."
    I "Well, it's not like there's anything I can do about this. I don't see any replacement rolls in here."
    I "Good thing I don't feel any urge to go right now..."
    if not d1a1_bathroom_clue9:
        $ investigation_clues_optional_found += 1
        $ d1a1_bathroom_clue9 = True
    return

label d1a1_check_lightswitch:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 1.0 yalign 0.6 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 1.0 yalign 0.6 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    play sound ["<silence 0.2>", sfx_lightswitch, "<silence 0.4>", sfx_lightswitch]
    pause 1.2
    I "Mrgh... This [t_pacclue]switch[t_paccluee] doesn't seem to do anything." with hpunch
    I "Inconvenient, but at least the window's letting in enough light for me to see everything."
    if not d1a1_bathroom_clue10:
        $ investigation_clues_optional_found += 1
        $ d1a1_bathroom_clue10 = True
    return

label d1a1_check_bathmat:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    if d1a1_sink_on:
        scene bg bathroom sinkon:
            xalign 0.5 yalign 1.0 zoom 1.0
            easein 0.5 zoom 1.5
    else:
        scene bg bathroom:
            xalign 0.5 yalign 1.0 zoom 1.0
            easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_bathroom_clue11 == False:
        I "A single [t_pacclue]bath mat[t_paccluee] is decorating the cold, wooden floor."
        play sound sfx_clothrustle
        I "Hrm... Nope, nothing underneath it." with vpunch
        if not d1a1_bathroom_clue11:
            $ investigation_clues_optional_found += 1
            $ d1a1_bathroom_clue11 = True
    else:
        I "A single [t_pacclue]bath mat[t_paccluee] is decorating the cold, wooden floor."
        I "There wasn't anything underneath it."
    return




screen pac_d1a1_hallway:
    style_prefix "pac"

    use pac_progress_gui(_("The 2F Hallway"))


    use pac_assistant_button(950, 790, 0.45, 910, 460, "gui/pac/pac_assistant_oriana_thinking.png", "gui/pac/pac_assistant_oriana_thinking.png", "d1a1_upstairs_assistant", _("Talk to Oriana"))


    use pac_end_button("d1a1_upstairs_confirm_end", investigated_upstairs)


    use pac_button(330, 665, d1a1_upstairs_clue1, "d1a1_check_first_room", _("Bathroom"))
    use pac_button(690, 595, d1a1_upstairs_clue2, "d1a1_check_second_room", _("Bedroom"))
    use pac_button(780, 580, d1a1_upstairs_clue3, "d1a1_check_third_room", _("Empty Bedroom"))
    use pac_button(1190, 580, d1a1_upstairs_clue4, "d1a1_check_masterbedroom", _("Master Bedroom"), special="d1a1_visited_masterbedroom")
    use pac_button(1120, 430, d1a1_upstairs_clue5, "d1a1_check_hallwaywindow", _("Window"))
    use pac_button(1280, 610, d1a1_upstairs_clue6, "d1a1_check_goldvase", _("Gold Vase"))
    use pac_button(1460, 230, d1a1_upstairs_clue7, "d1a1_check_hallwaypaintingsright", _("Paintings"))
    use pac_button(980, 140, d1a1_upstairs_clue8, "d1a1_check_hallwaylights", _("Lights"))
    use pac_button(1200, 700, d1a1_upstairs_clue9, "d1a1_check_hallwaytable", _("Console Table"))
    use pac_button(590, 380, d1a1_upstairs_clue10, "d1a1_check_hallwaypaintingleft", _("Painting"))



screen pac_d1a1_masterbedroom:
    style_prefix "pac"

    use pac_progress_gui(_("The Master Bedroom"))


    use pac_assistant_button(600, 1000, 0.75, 560, 420, "gui/pac/pac_assistant_oriana_thinking.png", "gui/pac/pac_assistant_oriana_thinking.png", "d1a1_upstairs_assistant", _("Talk to Oriana"))


    use pac_end_button("d1a1_upstairs_confirm_end", investigated_upstairs)


    use pac_button(260, 270, d1a1_masterbedroom_clue1, "d1a1_check_masterbedroom_windows", _("Window"))
    use pac_button(840, 510, d1a1_masterbedroom_clue2, "d1a1_check_wardrobe", _("Wardrobe"))
    use pac_button(1000, 670, d1a1_masterbedroom_clue3, "d1a1_check_bed", _("Bed"))
    use pac_button(1720, 600, d1a1_masterbedroom_clue4, "d1a1_check_masterbathroom", _("Bathroom"))

    use pac_button(1260, 320, d1a1_masterbedroom_clue5, "d1a1_check_masterpainting", _("Painting"))
    use pac_button(385, 550, d1a1_masterbedroom_clue6, "d1a1_check_silvervase", _("Figurine"))
    use pac_button(1460, 730, d1a1_masterbedroom_clue7, "d1a1_check_nightstand", _("Nightstand"))
    use pac_button(1495, 480, d1a1_masterbedroom_clue8, "d1a1_check_masterlamp", _("Lamp"))
    use pac_button(330, 680, d1a1_masterbedroom_clue9, "d1a1_check_masterdresser", _("Dresser"))
    use pac_button(800, 930, d1a1_masterbedroom_clue10, "d1a1_check_carpet", _("Rug"))
    use pac_button(280, 520, d1a1_masterbedroom_clue11, "d1a1_check_smallmirror", _("Mirror"))


label d1a1_upstairs_assistant:
    $ _last_say_who = "O"
    if investigation_location == "d1a1_masterbedroom":
        show bg masterbedroom:
            xalign 0.0 yalign 0.5 zoom 1.5
        show oriana thinking at mycenter
        with dissolve
    else:
        show bg hallway:
            xalign 0.5 yalign 0.5 zoom 2.5
        show oriana thinking at mycenter
        with dissolve
    O default "...Yes? What is it, [name_player]?{nw}"

    menu:
        "[t_clue]End your investigation[t_cluee]" if investigation_perfect:
            call d1a1_upstairs_confirm_end
        "\"Any ideas?\"":
            Y default "Is there anything you think we should check out?"
            if investigation_clues_required_found == investigation_clues_required:
                O thinking "Not off the top of my head... We could probably finish up our investigation now."
                O sideeye "But perhaps checking things a [t_clue]second time[t_cluee] might reveal some new information?"
                I "Hmm... I suppose if we still have time, we may as well..."
            elif investigation_progress_percent() >= 0.66:
                O blink "I suppose we're almost done examining each of the rooms now..."
                O sideeye "In fact, let me ask {i}you{/i} a question, [name_player]."
                Y surprised "Uh... Okay?"
                play ctc_sfx sfx_emotequestion
                O "Have you ever heard of the [t_clue]trolley problem[t_cluee]?"
                I "The trolley problem...{nw}"

                menu:
                    extend ""
                    "\"I know it.\"":
                        Y default "Yeah, I know it."
                        O blink "Then to cut to the chase..."
                    "\"Never heard of it.\"":
                        Y thinking "No, what's that?"
                        O default "The trolley problem is a famous thought experiment in ethics and psychology."
                        O blink "Imagine that you're standing by a train track, and a train is coming at full speed."
                        O "But down the track, you see [t_clue]five people[t_cluee] tied to it. The train will, of course, kill them if it comes and runs over them."
                        Y panicked "....."
                        O "You don't have enough time to rescue the five people, but what you CAN do is pull a nearby lever to change the train's track."
                        Y surprised "Oh, then--"
                        O thinking "HOWEVER. On the other track, there is [t_clue]one person[t_cluee] tied to it." with shakeonce
                        O default "So if you pull the lever, the train will go down the other track and kill that person instead."
                        Y sad "O-oh..."
                        O blink "So with all that in mind..."
                O default "Would you pull the lever and kill one person?{w=0.5} Or refrain from pulling it and let the train kill five people?{nw}"
                menu:
                    extend ""
                    "Pull the lever":
                        Y sad "...It's a horrible choice to make, but..."
                        $ fadein_sideimage = False
                        Y blink "It's better to save as many lives as possible, right? Then pulling the lever is the [t_clue]right thing to do[t_cluee]."
                        $ fadein_sideimage = True
                        O irritated "....."
                    "Don't pull the lever":
                        Y blink "...Even if more people will die..."
                        $ fadein_sideimage = False
                        Y leering "I could never make a choice while knowing someone will die from it. I don't have the right to [t_clue]choose who lives or dies[t_cluee]."
                        $ fadein_sideimage = True
                        O surprised "....." with shakeonce
                    "\"I don't have an answer.\"":
                        Y thinking "....."
                        $ fadein_sideimage = False
                        Y "...I don't know. I can't decide."
                        $ fadein_sideimage = True
                        O leering "This is a situation where you HAVE to decide, [name_player]."
                        Y leering "Why would a situation like that ever happen? Who tied up those people and left them on a train track in the first place?"
                        O confused "....."
                        O "...So what I'm hearing is..."
                        O leering2 "You can't make a decision until you know more about the specific circumstances?"
                        Y blink "...I guess so, yeah."
                        O thinking "....."
                Y default "...So? What's the correct answer?"
                O thinking "...There isn't one. It's a thought experiment, after all."
                Y thinking "Oh. ...Then what's {i}your{/i} answer to it?"
                O blink ".....{w=1.0} ...I'll tell you later."
                Y panicked "....."
                play ctc_sfx sfx_emotesigh
                I "That's...not really fair..." with hpunch
            elif investigation_progress_percent() >= 0.33:
                O thinking "We haven't taken a good look through all the rooms yet..."
                if d1a1_upstairs_clue4:
                    O default "But the master bedroom certainly gave us a lot of food for thought."
                    Y thinking "Hmm..."
                    O "Is there something on your mind?"
                    Y "It's just... Considering how it's called a \"master bedroom\", you'd think it would have some more useful clues."
                    O thinking "Yes, all we could really learn is that there was [t_clue]one man[t_cluee] using it."
                    Y worried "Didn't really give us a clue on how to FIND him either."
                    O irritated "If only it did. I'm sure finding him would give us the answers to all of our questions."
                    I "...But if he's the culprit, would he really just answer our questions without killing us first?"
                else:
                    if d1a1_visited_masterbedroom or investigation_location == "d1a1_masterbedroom":
                        O default "I think there's still some clues left to be found in the [t_pacclue]master bedroom[t_paccluee]."
                        I "The master bedroom... I wonder who last used it...?"
                    else:
                        O default "You haven't seen the [t_clue]master bedroom[t_cluee] yet, have you?"
                        I "The master bedroom...? Huh, I guess it's behind one of the doors I haven't checked yet..."
            else:
                O sideeye "...Really? We've barely started, and you're already stuck?"
                Y sad "I-I mean... You've checked over most of this place already, right?"
                O sideeyeblink "...So what, you only want to check what I haven't already?"
                O annoyed2 "If that's the case, why did you come up here? I would've inspected every part of this floor regardless."
                play ctc_sfx sfx_emotesob
                I "...Okay, fair point, but like, does she have to be rude about it?" with shakeonce
                O blink "...There's a lot of rooms, so [t_clue]start with going through any doors[t_cluee] you see."
                O sideeye "I'm sure {i}something{/i} will catch your interest if you just keep doing that."
                I "Right... I guess I want to check every room here eventually. Let's not overcomplicate this..."
        "\"Let's check a [t_clue]different room[t_cluee].\"" if investigation_location == "d1a1_masterbedroom":
            if not d1a1_upstairs_clue4:
                Y thinking "There's another room I'm curious about..."
                if not d1a1_visited_masterbedroom:
                    O blink "...Is that so?"
                    Y default "Yeah, so I'll be right--"
                    O default "Let's go, then. Which room is it?"
                    Y surprised "Huh? N-no, I can go check it out myself."
                    O irritated "...Are you that eager to get away from me?"
                    Y worried "That's... Uh..." with hpunch
                    O sideeye "Hmph. That was a joke."
                    Y panicked "It was?" with shakeonce
                    I "It's not a good one, then..."
                    O "There are plenty of reasons why I'm following you. Just do what you need to do, and don't mind me."
                    O sideeyeblink "....."
                    I "\"Plenty of reasons\", yet you don't even name ONE..."
                    I "Agh, whatever, let's focus on more important things..." with hpunch
                else:
                    O blink "...Again, huh?"
                    O thinking "You certainly enjoy moving around, don't you?"
                    I "She's looking at me like I'm some restless kid..."
            else:
                Y blink "Yeah, I think we checked everything worthwhile in here."
                O blink "I agree. Let's go visit the other rooms."

            play sound sfx_steps
            play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
            scene bg black with fade
            play sound sfx_doorclose
            scene bg hallway with fade
            pause 2.0
            $ d1a1_visited_masterbedroom = True
            $ investigation_location = "d1a1_hallway"

        "\"Let's check the [t_clue]Master Bedroom[t_cluee] again.\"" if d1a1_visited_masterbedroom and investigation_location != "d1a1_masterbedroom":
            if not d1a1_upstairs_clue4:
                Y thinking "We should visit the master bedroom one more time."
                O blink "I agree. I think we missed something important in there."
            else:
                Y thinking "Thinking about it now... Maybe there's something we missed in the master bedroom?"
                O thinking "I don't think so... But I suppose it can't hurt to be thorough."
                O default "Let's go, [name_player]."
            play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
            play sound sfx_steps
            scene bg black with fade
            play sound sfx_dooropen
            scene bg masterbedroom with fade
            pause 2.0
            $ investigation_location = "d1a1_masterbedroom"
        "\"Never mind...\"":
            pass

    return

label d1a1_upstairs_complete:
    I "...Something tells me I got a good look at everything worth looking at..."
    I "Oriana already searched this floor pretty thoroughly too... Maybe I can just stop here?"
    return

label d1a1_upstairs_perfect:
    I "...All right, it took forever, but I think I checked every inch of this floor by now."
    I "I should [t_clue]end my investigation[t_cluee] and talk with Oriana about next steps."
    return

label d1a1_upstairs_confirm_end:
    if investigated_upstairs and not investigation_complete:
        I "...It's strange but..."
        I "I feel like I [t_clue]already know[t_cluee] what to expect from investigating around here."
        I "Maybe I can zone out a bit as I go through everything...?{nw}"

        menu:
            extend ""
            "Skip this investigation":
                scene bg black with dissolvemed
                $ investigation_location = None
            "Cancel":
                I "...No, I'm sure Oriana won't let me slack off like that. Better focus..."
    else:
        $ _last_say_who = "O"
        show oriana confused at mycenter with dissolve
        O "Hmm? Do you think we've checked everything important now, [name_player]?{nw}"
        menu:
            extend ""
            "End your investigation":
                Y blink "Yeah... I think this is about all we're gonna find..."
                scene bg black with dissolvemed
                $ investigation_location = None
            "Cancel":
                Y default "...No, let's look around a bit more."
    return
label d1a1_check_first_room:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.0 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_upstairs_clue1:
        Y surprised "What was in {i}that{/i} room? The one you came out of when I arrived."
        $ show_side_oriana = True
        $ fadein_sideimage = False
        O "It's a [t_pacclue]bathroom[t_paccluee]. I finished checking every square inch of it just before you came up."
        O blink "It's completely barren of any supplies besides a couple of [t_clue]towels[t_cluee]. My guess is that no one really uses it."
        Y default "No one, huh...?"
        O default "The sink and toilet are functional, but the shower in there is not."
        O confused "There must be some faulty piping that the owner of this house never got around to fix."
        Y thinking "Even more reason to believe that no one really uses that bathroom, then."
        $ fadein_sideimage = True
        $ show_side_oriana = False
        if not d1a1_upstairs_clue1:
            $ investigation_clues_optional_found += 1
            $ d1a1_upstairs_clue1 = True
    else:
        I "This door leads to a [t_pacclue]bathroom[t_paccluee]."
        I "According to Oriana, there's only a couple of [t_clue]towels[t_cluee] in it."
        I "Probably won't be very useful to us..."
    return

label d1a1_check_second_room:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.3 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_upstairs_clue2:
        Y default "What's that middle room? Between the other doors on this side?"
        $ _last_say_who = "O"
        show oriana blink at mycenter with dissolve
        O "....."
        O "You might as well go and see for yourself."
        Y surprised "...? Okay..."
        play ctc_sfx sfx_steps
        scene bg black with fade
        play sound sfx_dooropen
        pause 1.0
        scene bg bedroom:
            zoom 1.75 xalign 0.4 yalign 0.0
            linear 6.0 xalign 0.0
        with dissolvemed
        pause 2.0
        scene bg bedroom:
            zoom 1.5 xalign 0.6 yalign 1.0
            linear 6.0 xalign 1.0
        with dissolvemed
        pause 2.0
        scene bg bedroom:
            xalign 0.5 yalign 0.5 zoom 1.1
            easein 3.0 zoom 1.0
        with dissolvemed
        show screen notify_location("2 этаж - Спальня", persistent.unlock_bg_bedroom)
        $ persistent.unlock_bg_bedroom = True
        pause 2.0
        I "Looks like a child's [t_pacclue]bedroom[t_paccluee]..."
        window auto hide
        play sound sfx_steps_heels
        pause 1.5
        $ _last_say_who = "O"
        show oriana at mycenter with dissolve
        O "This was the first room I investigated up here."
        O "I thought I might be able to find some clues about the culprit."
        Y thinking "...In a little kid's bedroom?"
        O thinking "......."
        O sideeyeblink "Anyways, I investigated this room thoroughly, and there's nothing out of the ordinary."
        O sideeye "If you don't believe me, you can take a look around by yourself."
        I "She's weirdly on edge...{nw}"

        menu:
            extend ""
            "Investigate here":
                Y default "Okay, I'll take a look around here."
                O irritated "....."
                O "...Fine."
                O annoyed2 "I'll be waiting outside."
                play ctc_sfx sfx_steps_heels
                scene bg bedroom with dissolve
                pause 2.0
                I "....."
                I "I better make this quick..."
                hide screen notify_location
                $ investigation_location = "d1a1_bedroom"
            "Believe her and leave":
                Y default "No, I believe you. Let's not waste any time and check the other rooms instead."
                O default "....."
                Y surprised "...?"
                O blink "...Right, let's go."
                hide screen notify_location
                play ctc_sfx sfx_steps
                play sound ["<silence 0.2>", sfx_steps_heels]
                scene bg black with fade
                scene bg hallway with fade
                pause 1.0
                play ctc_sfx sfx_doorclose
                pause 1.0
                if not d1a1_upstairs_clue2:
                    $ investigation_clues_required_found += 1
                    $ d1a1_upstairs_clue2 = True
    else:

        I "A child's [t_pacclue]bedroom[t_paccluee]..."
        Y thinking "...I wonder where that kid is now..."
        $ fadein_sideimage = False
        $ show_side_oriana = True
        O default "....."
        $ show_side_oriana = False
        $ fadein_sideimage = True
    return

label d1a1_check_third_room:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.4 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_upstairs_clue3:
        Y default "What's that room all the way down the hall?"
        $ fadein_sideimage = False
        $ show_side_oriana = True
        O thinking "...I think it's a bedroom."
        Y thinking "You...\"think\"?"
        O irritated "...Just open it."
        $ show_side_oriana = False
        $ fadein_sideimage = True
        play ctc_sfx sfx_steps
        scene bg black with fade
        play sound sfx_dooropen
        pause 1.0
        scene bg emptybedroom:
            xalign 0.5 yalign 0.5 zoom 1.25
            easein 5.0 zoom 1.0
        with dissolvemed
        pause 2.0
        show screen notify_location("2 этаж - Пустая Спальня", persistent.unlock_bg_emptybedroom)
        $ persistent.unlock_bg_emptybedroom = True
        pause 2.0
        Y panicked "Wha..."
        $ fadein_sideimage = False
        Y "It's basically [t_pacclue]empty[t_paccluee]!" with shakeonce
        $ fadein_sideimage = True
        scene bg emptybedroom:
            xalign 0.5 yalign 0.9 zoom 1.2
            easein 5.0 yalign 0.6
        with dissolve
        $ show_side_oriana = True
        O "Yes. Not a thing in here but a single [t_clue]bed[t_cluee]. Just the frame and mattress, at that."
        $ show_side_oriana = False
        I "It really is just this one barren bed..."
        scene bg emptybedroom with dissolve
        $ _last_say_who = "O"
        show oriana blink at mycenter with dissolve
        O "..... [name_player]."
        O default "Do you think anyone was using this room?{nw}"

        menu:
            extend ""
            "\"Yeah, someone was living here.\"":
                Y thinking "I mean, there's a bed there, so I'm thinking someone was using this room purely for sleeping."
                O leering "On just this? Without any pillow or covers?"
                Y worried "Maybe...those got moved to another room?"
                O "...Are you just making guesses?"
                Y leering "Well, what do {i}you{/i} think this room was for?"
                O annoyed "....." with shakeonce
                O irritated "...Forget it. Let's just move on."
                I "...What is her problem?" with shakeonce
            "\"No, there's no way.\"":
                Y thinking "The bed is covered in way too much dust. Clearly, [t_clue]no one has slept on it for a long time[t_cluee]."
                O blink "I agree."
                Y surprised "But I mean... Even if no one needed this room as a bedroom, you'd think they would do something else with it."
                $ fadein_sideimage = False
                Y default "Like...use it as a study. Or maybe storage."
                $ fadein_sideimage = True
                O confused "Exactly. Yet, here it is. Barren without purpose."
                O "It almost feels...intentional."
                I "I wonder what this means..."
                O "....."
                O blink "...In any case, there's nothing else to find here."

        O sideeye "Let's go, [name_player]."
        hide screen notify_location
        play ctc_sfx sfx_steps
        play sound ["<silence 0.2>", sfx_steps_heels]
        scene bg black with fade
        scene bg hallway with fade
        pause 1.0
        play ctc_sfx sfx_doorclose
        pause 1.0
        if not d1a1_upstairs_clue3:
            $ investigation_clues_required_found += 1
            $ d1a1_upstairs_clue3 = True
    else:
        I "That room is just completely [t_pacclue]empty[t_paccluee]..."
        $ show_side_oriana = True
        O thinking "......."
        $ show_side_oriana = False
        $ _last_say_who = None
        scene bg hallway
        show oriana thinking at mycenter
        with dissolve
        Y surprised "...Oriana?"
        O default "...Yes?"
        Y "You okay? You looked like you were lost in thought."
        O thinking "...I was just thinking about that lone bed."
        O "Considering how difficult it is to throw away a bed, maybe what happened was..."
        I "...?"
        O blink "...No, never mind. We don't have enough information."
        O sideeye "Come on, [name_player]. Pick another room."
    return

label d1a1_check_masterbedroom:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.7 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_visited_masterbedroom:
        Y thinking "What's this room here? There's only one door on this whole wall..."
        $ _last_say_who = "O"
        show oriana at mycenter with dissolve
        O "It seems to be a [t_pacclue]master bedroom[t_paccluee]. I haven't given this one a good look yet."
        I "A master bedroom... So the owner of the house probably uses it..."
        O sideeye "We may as well investigate it together, [name_player]. Come on, I'm right behind you."
        play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
        play sound sfx_steps
        scene bg black with fade
        play sound sfx_dooropen
        scene bg masterbedroom:
            xalign 0.0 yalign 0.5 zoom 1.3
            linear 5.0 xalign 0.5
        with fade
        pause 3.0
        scene bg masterbedroom:
            xalign 0.5 yalign 0.5 zoom 1.1
            easein 3.0 zoom 1.0
        with dissolvemed
        show screen notify_location("2 этаж - Главная Спальня", persistent.unlock_bg_masterbedroom)
        $ persistent.unlock_bg_masterbedroom = True
        pause 2.0
        Y surprised "Yep, this is definitely a master bedroom. Really has that \"master\" feeling."
        $ _last_say_who = "O"
        show oriana thinking at mycenter with dissolve
        O "It's tidier than I would have expected. We might have some trouble finding good clues here."
        Y blink "Still, it's worth a shot. Let's look around."
        hide screen notify_location
        $ investigation_location = "d1a1_masterbedroom"
    else:
        if not d1a1_upstairs_clue4:
            Y thinking "We should visit the master bedroom one more time."
            $ _last_say_who = "O"
            show oriana blink at mycenter with dissolve
            O "I agree. I think we missed something important in there."
            play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
            play sound sfx_steps
            scene bg black with fade
            play sound sfx_dooropen
            scene bg masterbedroom with fade
            pause 2.0
            $ investigation_location = "d1a1_masterbedroom"
        else:
            I "I don't think there's anything worthwhile left to find, but should I check out the [t_pacclue]master bedroom[t_paccluee] again?{nw}"

            menu:
                extend ""
                "\"Sure, why not?\"":
                    Y default "Let's go to the master bedroom again."
                    $ _last_say_who = "O"
                    show oriana thinking at mycenter with dissolve
                    O "Is there something you wanted to double-check?"
                    Y blink "Something like that, yeah."
                    play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
                    play sound sfx_steps
                    scene bg black with fade
                    play sound sfx_dooropen
                    scene bg masterbedroom with fade
                    pause 2.0
                    $ investigation_location = "d1a1_masterbedroom"
                "\"Nah, I'm good.\"":
                    I "On second thought, maybe it's not worth the trip..."
    return
label d1a1_check_hallwaywindow:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.6 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "An eerie light from the [t_pacclue]window[t_paccluee] illuminates the hallway..."
    if not d1a1_upstairs_clue5:
        Y sad "What a creepy fog..."
        $ _last_say_who = "O"
        show oriana thinking at mycenter with dissolve
        O "It's quite unusual for fog to be this thick."
        Y default "Do you think it might clear by tomorrow?"
        O blink "Tomorrow..."
        O default "We heard the 6 o'clock bell earlier, if you recall. But do you think it's morning or evening right now?{nw}"

        menu:
            extend ""
            "Morning":
                Y thinking "The fog looks kinda bright, so...maybe it's dawn right now?"
                O disappointed "....."
                I "What's with that look? Am I wrong?" with shakeonce
            "Evening":
                Y surprised "Considering how dark it is in here, I thought for sure it's evening right now..."
                O thinking "Well..."
                Y thinking "Actually, why do you ask?"
        O blink "...Sorry, I guess you have no way of knowing this, but..."
        O thinking "I remember that it was [t_clue]early evening[t_cluee] when I was captured."
        O "So it's most likely that we were all thrown into this house immediately, but..."
        O "...What if in fact, an entire day has passed already... Or maybe even..."
        $ renpy.music.set_volume(0.0, 3, channel="music")
        Y surprised "...Wait."
        $ fadein_sideimage = False
        Y shouting "You REMEMBER how you got captured?!" with shakeshort
        $ fadein_sideimage = True
        O surprised "Ah... U-um, hang on, let me explain..."
        O confused "I don't remember {i}exactly{/i}... Some parts are still fuzzy."
        O "But one thing I remember is I was walking outside, just as the sky was getting dark."
        show oriana irritated at shudder
        O "And...that's when I lost consciousness. When I woke up, I was on the floor in the foyer with you and Cecilia."
        I "The foyer... If I think back to what we talked about there..."
        play sound sfx_flashback
        scene bg foyer at grayscale_on
        show oriana sideeyeblink at myleft, grayscale_on
        show cecilia grin at myright, grayscale_on
        with custom_flashbulblong()
        O "The most unsettling part is..."
        O thinking "Neither of us have any memory of being kidnapped or brought here."
        C thinking "It's the strangest thing, right? Almost like we were spirited away!"
        scene bg black with dissolvemed
        scene bg hallway
        show oriana thinking at mycenter
        with dissolvemed
        I "....."
        I "I guess she hasn't really lied about anything, but...{nw}"

        menu:
            extend ""
            "Accept her explanation":
                Y blink "...All right. Let me know if you remember anything else."
                O blink "....."
                O default "...Thank you, [name_player]."
                I "....."
            "Pressure her for more":
                Y leering "Is that really all you remember? No other details?"
                $ fadein_sideimage = False
                Y "...You're not...hiding anything from me, right?"
                $ fadein_sideimage = True
                O panicked "I-I..."
                O leering "...N-no, look, that's all I remember, okay?" with shakeonce
                O irritated "Besides, does it really matter HOW we ended up here?"
                O "Either way, we're dealing with a criminal toying with our lives!"
                O shouting "This is no time to be doubting each other!" with shakeonce
                I "...You're one to talk..."
                play ctc_sfx sfx_heartbeat_single
                I "She's definitely [t_clue]hiding something[t_cluee] from me. But what...?" with hpunch
                O irritated "....."
        O blink "...Anyway, circling back..."
        $ renpy.music.set_volume(1.0, 3, channel="music")
        O default "I wanted to say that since it's likely evening right now, we should turn in for the night later."
        Y thinking "Y-you mean...sleep here? In this house? That we're trapped in?"
        O blink "I know it's not ideal... But if anyone's feeling drained, it's important to sleep at least a little bit."
        play ctc_sfx sfx_emotequestion
        O confused "Sleep deprivation tends to lead to [t_clue]bad decisions[t_cluee]..."
        I "Ugh... Now that she said that, I'm noticing how tired I am..." with shakeonce
        if not d1a1_upstairs_clue5:
            $ investigation_clues_required_found += 1
            $ d1a1_upstairs_clue5 = True
    else:
        I "This...has to be moonlight, right? It's a little too bluish to be sunlight..."
    return

label d1a1_check_goldvase:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.8 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_upstairs_clue6:
        Y surprised "Whoa... That thing's really shiny..."
        $ show_side_oriana = True
        $ fadein_sideimage = False
        O "It's shaped like a [t_pacclue]vase[t_paccluee], but it's made of a heavy, gold-coloured material."
        Y thinking "Huh? So this isn't gold?"
        O sideeye "Do you really think a solid gold object would be here in the hallway for anyone to just walk by and take?"
        Y worried "Well...when you put it that way..."
        O confused "...It's certainly heavy, despite being empty. And these engravings..."
        O blink "It's most likely some sort of antique. Maybe a souvenir."
        Y surprised "Wow, you really know your stuff."
        O thinking "It's just a guess. In any case, this won't be of any use to us."
        Y default "Yeah, I suppose we should move on."
        $ fadein_sideimage = True
        $ show_side_oriana = False
        if not d1a1_upstairs_clue6:
            $ investigation_clues_optional_found += 1
            $ d1a1_upstairs_clue6 = True
    else:
        I "A shiny [t_pacclue]gold vase[t_paccluee]. It's heavy, but otherwise nothing else special about it..."
        Y thinking "Looks like there's a regular ceramic vase next to the gold one, but..."
        $ show_side_oriana = True
        $ fadein_sideimage = False
        O blink "I already checked. It's also empty."
        Y worried "Yeah, I thought so..."
        $ fadein_sideimage = True
        I "Maybe she really doesn't need my help here..."
        $ show_side_oriana = False
    return

label d1a1_check_hallwaypaintingsright:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.9 yalign 0.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "There's a bunch of [t_pacclue]paintings[t_paccluee] along this wall. Which one should I take a closer look at?{nw}"

    menu:
        extend ""
        "Check the flower painting":
            I "Hmm... It's not composed of a ton of paint strokes, but that gives it a calming sleekness."
            I "The rest of the canvas being bare conveys a feeling of pure, untainted potential."
            $ show_side_oriana = True
            O "...Did you notice anything, [name_player]?"
            $ fadein_sideimage = False
            Y relaxed "Yeah, just thinking about how I totally get art."
            O irritated "...I meant did you notice anything that would be useful to our situation."
            Y "....."
            Y worried2 "No, I'm sorry."
            O disappointed "....."
            play ctc_sfx sfx_emotesigh
            I "Please stop giving me that look..." with hpunch
        "Check the bird painting":
            Y surprised "That's...a crane, right?"
            $ show_side_oriana = True
            $ fadein_sideimage = False
            O blink "That's right. Cranes can be found in all parts of the world, so they've been given all kinds of symbolic meanings."
            O default "Longevity, fortune, tranquility, and immortality, to name a few."
            Y thinking "...Immortality, huh...?"
            Y surprised "Huh, so you've an interest in birds, Oriana?"
            O "....."
            O blink "...No. I just happened to learn that somewhere."
            O sideeye "There doesn't seem to be more to these paintings. Let's move on, [name_player]."
    $ show_side_oriana = False
    $ fadein_sideimage = True
    if not d1a1_upstairs_clue7:
        $ investigation_clues_optional_found += 1
        $ d1a1_upstairs_clue7 = True
    return
label d1a1_check_hallwaylights:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.6 yalign 0.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    Y surprised "Huh? What are those things on the ceiling? Are they [t_pacclue]lights[t_paccluee]?"
    $ show_side_oriana = True
    $ fadein_sideimage = False
    O confused "Unusually designed, but yes, I think so. There's no way to check until we get the power back on, though."
    Y thinking "Huh... So those aren't real candles, then?"
    O blink "It would be an awfully inconvenient lighting system if they were."
    I "Their bases are transparent... Hmm, looks like there's nothing unusual inside them."
    $ show_side_oriana = False
    $ fadein_sideimage = True
    if not d1a1_upstairs_clue8:
        $ investigation_clues_optional_found += 1
        $ d1a1_upstairs_clue8 = True
    return

label d1a1_check_hallwaytable:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.8 yalign 0.8 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A [t_pacclue]console table[t_paccluee] with what looks like a handle for a drawer."
    play sound sfx_drawer_open
    Y "....."
    $ fadein_sideimage = False
    play sound sfx_drawer_close
    Y blink "...Nothing inside, huh?"
    $ show_side_oriana = True
    O confused "It shouldn't be a surprise that there are no worthwhile clues or tools in a hallway, [name_player]."
    $ fadein_sideimage = True
    I "Guess not... Maybe I should be pulling on some doorknobs instead?"
    $ show_side_oriana = False
    if not d1a1_upstairs_clue9:
        $ investigation_clues_optional_found += 1
        $ d1a1_upstairs_clue9 = True
    return

label d1a1_check_hallwaypaintingleft:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg hallway:
        xalign 0.2 yalign 0.3 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "There's [t_pacclue]one painting[t_paccluee] on this wall..."
    Y surprised "A field of flowers..."
    $ show_side_oriana = True
    $ fadein_sideimage = False
    O sideeye "....."
    if not d1a1_upstairs_clue10:
        I "....."
        I "Okay, I guess there isn't much else to say about this..." with hpunch
        $ show_side_oriana = False
        $ fadein_sideimage = True
        if not d1a1_upstairs_clue10:
            $ investigation_clues_optional_found += 1
            $ d1a1_upstairs_clue10 = True
    else:
        Y worried "...Hey, Oriana?"
        O "...Yes?"
        Y "I know you've already checked out most of this floor so...do you really need to keep watching my every movement?"
        O sideeyeblink "Sometimes, you can get a new perspective by seeing someone else's reactions."
        Y "Then can't you...I dunno, at least SAY something when I make my comments?"
        O disappointed "There wasn't anything I wanted to say to your latest one."
        play ctc_sfx sfx_emotesigh
        I "...Ugh, fine, I'll just try to get used to her silent stares..." with hpunch
        $ show_side_oriana = False
        $ fadein_sideimage = True
    return

label d1a1_check_masterbedroom_windows:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.0 yalign 0.2 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "The fog is so thick, it's like these aren't even [t_pacclue]windows[t_paccluee], but just...panes of glass painted white."
    Y thinking "Is anyone even outside?"
    window auto hide
    play sound sfx_punchwall
    hide oriana with shakeonce
    pause 0.3
    play sound sfx_punchwall
    hide oriana with shakeonce
    pause 0.3
    Y shouting "HELLOOO?!" with shakeshort
    I "....."
    window auto hide
    play sound sfx_punchwall
    hide oriana with shakeonce
    pause 0.3
    play sound sfx_punchwall
    hide oriana with shakeonce
    pause 0.3
    Y "IS ANYONE OUT THERE?!" with shakeshort
    I "......."
    $ _last_say_who = "O"
    scene bg masterbedroom
    show oriana leering at mycenter
    with dissolve
    O "We've already tried that, [name_player]. I don't think there's anyone nearby who can hear us."
    I "Nrgh... Just what is this place...?" with hpunch
    if not d1a1_masterbedroom_clue1:
        $ investigation_clues_optional_found += 1
        $ d1a1_masterbedroom_clue1 = True
    return

label d1a1_check_wardrobe:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.4 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_masterbedroom_clue2:
        Y surprised "That's...a [t_pacclue]wardrobe[t_paccluee], right? For storing clothes?"
        $ fadein_sideimage = False
        $ show_side_oriana = True
        O "It appears so, yes. We should search it for clues."
        Y default "All right, hang on..."
        $ fadein_sideimage = True
        $ renpy.music.set_volume(0.5, 3, channel="music")
        scene bg black with dissolvemed
        play sound sfx_clothrustle
        Y "....."
        $ fadein_sideimage = False
        Y thinking "Clothes, clothes... And..."
        Y "...Yep. More clothes."
        O "Seems like these are all [t_clue]men's clothes[t_cluee]."
        I "Too big for any of us to use..."
        $ show_side_oriana = False
        $ fadein_sideimage = True
        $ renpy.music.set_volume(1.0, 3, channel="music")
        $ _last_say_who = "O"
        scene bg masterbedroom
        show oriana blink at mycenter
        with dissolvemed
        O "...Men's clothes..."
        Y "So...does this mean our culprit is a man?"
        O "...It's too soon to say. All we know is that a man was living in this room."
        O default "There's also a bedroom across the hall that looks like it belongs to a young girl."
        O thinking "And of course, it's possible the culprit isn't someone who lived in this house, which might make this investigation pointless..."
        Y thinking "...Wait, back up. You think our culprit could actually be a little girl?"
        O blink "....."
        O "...It's not completely out of the question.{nw}"

        menu:
            extend ""
            "Agree there's a possibility":
                Y sad "...I suppose it wouldn't be the strangest thing."
                $ fadein_sideimage = False
                Y default "But considering the three of us were kidnapped and brought here, I doubt a little girl could've done that alone."
                $ fadein_sideimage = True
                play ctc_sfx sfx_emotequestion
                O surprised "...You think there might have been an [t_clue]accomplice[t_cluee]?"
                Y thinking "...Yeah, if there's more than one person involved, a lot of this makes sense."
                $ fadein_sideimage = False
                Y leering "Why was this ordinary house turned into the setting of some crazy escape game with our lives on the line?"
                $ fadein_sideimage = True
                O "....."
                Y surprised "...Huh? What's wrong?"
                O thinking "N-nothing. It's just..."
                O confident "I'm glad you're thinking hard about this, [name_player]."
                I "...Should... Should I be happy to hear that?"
            "Deny it":
                Y thinking "No, come on, that can't be it."
                $ fadein_sideimage = False
                Y "How could a little girl even imagine a twisted situation like this?"
                $ fadein_sideimage = True
                O leering "...Are you really that narrow-minded?"
                Y panicked "Wha-- No, my mind is NORMAL!" with shakeonce
                $ fadein_sideimage = False
                Y angry "We JUST found evidence that a man was living here, and your first idea is that a little girl must be our kidnapper?!" with shakeonce
                $ fadein_sideimage = True
                O annoyed "...Tsk." with shakeonce
                O leering2 "Forget about it. Start looking somewhere else."
                I "What the hell..."
        if not d1a1_masterbedroom_clue2:
            $ investigation_clues_required_found += 1
            $ d1a1_masterbedroom_clue2 = True
    else:
        I "The [t_pacclue]wardrobe[t_paccluee] is filled with men's clothes..."
        I "Probably won't be of any use to us..."
    return
label d1a1_check_bed:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.5 yalign 0.8 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A large [t_pacclue]bed[t_paccluee]. Looks like it hasn't been used in a while."
    I "{cps=6}.......{/cps}{nw}"

    menu:
        extend ""
        "Jump on it":
            show bg masterbedroom:
                xalign 0.5 yalign 0.8 zoom 1.75
            I "Woop!"
            play ctc_sfx sfx_bedjump
            show bg black
            I "*bounce*" with vpunch
            Y worried "*cough* Okay-- *cough* That...might have been a mistake." with shakeshort
            if d1a1_jumped_bed == False:
                play ctc_sfx sfx_emoteshout
                show bg masterbedroom at reset
                show oriana angry at mycenter
                with custom_flashquick()
                O "Are you a child?! Can't you see all the dust on that bed?!" with shakeshort
                show oriana shouting
                Y sad "Sorry, I, uh...couldn't help it."
                O irritated "Ugh... I can't believe you can have impulses like that even with our situation being what it is..."
                I "Hmm... If I can just air out these sheets, this bed would be perfect."
                I "...But wait, if the windows don't open, how do I air it out?"
                O disappointed "...You're not listening to me, are you?"
                Y thinking "{cps=6}.......{/cps}{nw}"
                play ctc_sfx "<silence 1.0>"
                $ fadein_sideimage = False
                extend surprised " ...Sorry, what?"
                $ fadein_sideimage = True
                O annoyed "...Never mind." with shakeonce
                O irritated "Now come on, get up. We'll talk about the beds later tonight."
                O leering2 "...And [t_clue]don't jump on this bed again[t_cluee]."
                $ d1a1_jumped_bed = True
            else:
                $ _last_say_who = "O"
                show bg masterbedroom at reset
                show oriana irritated at mycenter
                with dissolve
                O "...A mistake you already made earlier. What did I say about jumping on the bed?"
                Y surprised "Uh... Do it?"
                play ctc_sfx sfx_emoteshout
                O angry "DON'T DO IT." with shakeshort
                O irritated "Ugh... How did I end up with babysitting duty...?"
                Y thinking "Huh, you know, this bed is already plenty comfortable, even with all the dust."
                window auto hide
                show bg black with dissolve
                Y relaxed "In fact... {cps=12}I'm already... {size=-10}Falling... .....{/size}{/cps}"
                $ quick_menu = False
                $ music_info = False
                $ renpy.music.set_volume(0.0, 3, channel="music")
                scene bg black with dissolveslow
                show text "[name_player] fell asleep, and soon woke up in the real world.\nThe three of them being trapped in that house was all just a [t_clue]dream[t_cluee]." with dissolve
                pause 6.0
                hide text with dissolve
                show text "By doing the unthinkable and falling asleep in that horrible situation,\n[name_player] saved everyone, and they all soon returned to their normal lives." with dissolve
                pause 6.0
                hide text with dissolve
                show text "THE END" with dissolve
                pause 1.0
                hide text
                $ quick_menu = True
                $ music_info = True
                $ _last_say_who = "O"
                show bg masterbedroom with custom_flashquick()
                show oriana angry at mycenter
                window auto show None
                $ renpy.music.set_volume(1.0, 0, channel="music")
                play ctc_sfx sfx_emoteshout
                O "DON'T JUST FALL ASLEEP!" with shakeshort
                show oriana shouting
                I "Agh, so close..." with hpunch
                O irritated "You're not going to accomplish anything by sleeping, [name_player]."
                O leering2 "Come on, keep moving."
                Y worried2 "Mrgh..."
        "Don't jump on it":
            if d1a1_jumped_bed == False:
                I "This isn't the time for fooling around. Let's look somewhere else." with hpunch
            else:
                I "Oriana will get mad if I jump on this again. Let's move on." with hpunch

    if not d1a1_masterbedroom_clue3:
        $ investigation_clues_optional_found += 1
        $ d1a1_masterbedroom_clue3 = True
    return

label d1a1_check_masterbathroom:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 1.0 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_masterbedroom_clue4 == False:
        Y surprised "Another door in this room...?"
        $ _last_say_who = "O"
        show oriana at mycenter with dissolve
        O "Considering this is a master bedroom, that door likely leads into a [t_pacclue]private bathroom[t_paccluee]."
        Y default "Let's go check it out."
        play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
        play sound sfx_steps
        scene bg black with fade
        play sound sfx_dooropen
        pause 1.0
        scene bg masterbathroom:
            xalign 0.4 yalign 0.5 zoom 1.25
            easein 5.0 zoom 1.0
        with dissolve
        pause 1.0
        show screen notify_location("2 этаж - Главная Ванная", persistent.unlock_bg_masterbathroom)
        $ persistent.unlock_bg_masterbathroom = True
        pause 2.0
        I "Bingo. It's a bathroom."
        $ _last_say_who = "O"
        show oriana surprised at mycenter with dissolve
        O "Oh, there's a shower in here! I'll go see if it works."
        hide oriana with dissolve
        I "Overall, it's pretty clean. I wonder if the culprit was in here recently?"
        I "Not a lot to look at here, so let's just give it all a quick glance..."
        if not d1a1_checked_bathroom:
            hide screen notify_location
            scene bg masterbathroom:
                xalign 0.8 yalign 0.0 zoom 1.5
            with dissolve
            I "...Wait. The mirror..."
            scene cg mirror:
                xalign 0.4 yalign 0.4 zoom 1.3
                easein 6.0 xalign 0.5 yalign 0.5 zoom 1.0
            with dissolvemed
            $ persistent.unlock_cg_mirror = True
            pause 2.0
            $ show_side_player = True
            Y surprised "....."
            $ fadein_sideimage = False
            Y "...So this is [t_clue]my face[t_cluee]?"
            Y thinking "....."
            $ fadein_sideimage = True
            I "...Nah, I guess I can wonder about myself later. Let's keep looking around."
            scene bg masterbathroom with dissolve
        else:
            I "There's a mirror here... But I already know what I look like."

        Y default "Let's see... By the sink..."
        $ fadein_sideimage = False
        Y "A half-empty bottle of toothpaste and...[t_clue]one toothbrush[t_cluee]."
        play sound sfx_showeron
        $ renpy.music.set_volume(0.5, 0, channel="loop_sfx")
        play loop_sfx sfx_showerloop fadein 2.0
        $ show_side_oriana = True
        O "Just one? Then I think it's safe to assume that only [t_clue]one person[t_cluee] was using the master bedroom and this bathroom."
        Y thinking "...Doesn't look like there's any spare toothbrushes either."
        O blink "There weren't supplies like that in the other bathroom either."
        Y worried "So none of us will be able to brush our teeth while we're here..."
        O sideeye "I don't know about you, but I don't intend on staying here for long."
        play sound sfx_showeron
        Y relaxed "Heh... Anyways, sounds like the shower's working, at least."
        O blink "Yes, it's a huge relief since the shower in the other bathroom is broken."
        O default "There's a shampoo bottle and a bar of soap in here too. Hope the culprit doesn't mind us using it."
        $ show_side_oriana = False
        $ fadein_sideimage = True
        scene bg masterbathroom
        play sound sfx_showeroff
        pause 0.5
        stop loop_sfx fadeout 1.0
        pause 2.0
        $ _last_say_who = None
        show oriana at mycenter_fadein
        pause 1.0
        Y sad "I guess nothing else looks particularly interesting..."
        O thinking "It makes sense that a bathroom wouldn't have anything useful for escaping this place."
        Y default "At least now we know that we can shower here."
        O blink "Mhm..."
        O "....."
        Y surprised "...?"
        O embarrassed "...A-all right, let's go outside now."
        $ renpy.music.set_volume(1.0, 3.0, channel="loop_sfx")
        hide screen notify_location
        play sound sfx_steps
        play ctc_sfx ["<silence 0.2>", sfx_steps_heels]
        scene bg black with fade
        play sound sfx_doorclose
        scene bg masterbedroom with fade
        pause 2.0
        I "Back in the master bedroom..."
        if not d1a1_masterbedroom_clue4:
            $ investigation_clues_required_found += 1
            $ d1a1_masterbedroom_clue4 = True
    else:
        I "We already checked that [t_pacclue]private bathroom[t_paccluee] pretty thoroughly. Only the [t_clue]one toothbrush[t_cluee] stood out."
        $ _last_say_who = "O"
        show oriana thinking at mycenter with dissolve
        O "....."
        Y surprised "Hmm? Something on your mind?"
        O "It's...unusually clean. Everything we've seen so far."
        O blink "If this was truly an ordinary house before it turned into a cage for us, it's... What's the word...?{nw}"

        menu:
            extend ""
            "Minimalistic":
                Y default "Minimalistic?"
                O confused "Something like that, yes."
                O "It's like whoever was living here was doing the bare minimum to get by."
                O thinking "They were keeping themselves tidy and hygienic, sure. But, like...they were also avoiding...making memories?"
                Y thinking "Memories?"
                O surprised "No, maybe it's more like they wanted to preserve the original memories of this place..."
                Y worried "...What?"
            "Unnatural":
                Y default "Unnatural?"
                O confused "I suppose?"
                O blink "It's certainly odd that things are both tidy and dusty..."
                O default "But this is most certainly a real home. Or at least...it used to be."
                Y thinking "....."
        O embarrassed "S-sorry. I normally have my thoughts more sorted out than this..."
        O sideeye "Let's just keep looking around."
    return
label d1a1_check_masterpainting:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.8 yalign 0.2 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    Y "Another [t_pacclue]painting[t_paccluee]. There sure are a lot of these throughout the house..."
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O default "It's clear that whoever lived in this house had a refined sense of aesthetics."
    O sideeyeblink "Mostly Impressionist works... Figures found in nature..."
    Y worried "..... You're going over my head here, Oriana..."
    O disappointed "...All I'm saying is that they don't seem very interested in the more abstract painting styles."
    O relaxed "I feel a slight kinship with whoever chose these works to display."
    $ fadein_sideimage = True
    $ show_side_oriana = False
    I "Uh... Glad to hear you're bonding with a potential kidnapper, then...?" with hpunch
    if not d1a1_masterbedroom_clue5:
        $ investigation_clues_optional_found += 1
        $ d1a1_masterbedroom_clue5 = True
    return

label d1a1_check_silvervase:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.2 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_masterbedroom_clue6:
        Y surprised "...Oh. I thought there was a vase there, but looks like it's actually a vase-shaped [t_pacclue]figurine[t_paccluee]."
        $ fadein_sideimage = False
        $ show_side_oriana = True
        O stunned "How strange... Is it some type of cultural artifact?"
        Y thinking "No idea... It feels kinda fragile when I hold it."
        Y surprised "Huh... I wonder why there's no dust on it?"
        O confused "I supposed it must have been handled recently."
        $ fadein_sideimage = True
        $ show_side_oriana = False
        I "I wonder what this is for...?"
        if not d1a1_masterbedroom_clue6:
            $ investigation_clues_optional_found += 1
            $ d1a1_masterbedroom_clue6 = True
    else:
        I "A vase-shaped [t_pacclue]figurine[t_paccluee]."
        Y thinking "....."
        $ fadein_sideimage = False
        $ show_side_oriana = True
        O leering "...Why are you still staring at that?"
        Y worried "It's just... Seriously, what is this thing?" with hpunch
        O confused "Well... Considering the shape and pattern, this figurine might just be purely decorative."
        Y thinking "But then what about the lack of dust? That means someone either used it or wiped it or took it out someplace or..."
        O blink "...[name_player]. It's great that you're the type to give things a second glance, but..."
        O disappointed "...At a certain point, it's better to just check out new things instead of revisiting old ones."
        $ fadein_sideimage = True
        $ show_side_oriana = False
        play ctc_sfx sfx_emotesigh
        I "...Mrgh. All right, maybe this is just a red herring..." with hpunch
    return

label d1a1_check_nightstand:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.9 yalign 0.8 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A [t_pacclue]nightstand[t_paccluee] with a lamp on it."
    if not d1a1_masterbedroom_clue7:
        play sound sfx_drawer_open
        Y thinking "Hrm... The drawers just have random stuff like watches, loose change, a copy of the Bible..."
        $ fadein_sideimage = False
        Y surprised "Oh look, there's a pair of reading glasses in here."
        $ show_side_oriana = True
        O annoyed2 "Why are those glasses not stored inside a case? Anything in that drawer could break them."
        Y sad "Don't ask me..." with hpunch
        $ fadein_sideimage = True
        $ show_side_oriana = False
        play sound sfx_drawer_close
        I "Not much else to look at here..."
        if not d1a1_masterbedroom_clue7:
            $ investigation_clues_optional_found += 1
            $ d1a1_masterbedroom_clue7 = True
    else:
        I "The drawers had a bunch of random stuff, including a pair of reading glasses."
        Y surprised "Come to think of it, you wear glasses, don't you Oriana?"
        $ fadein_sideimage = False
        $ show_side_oriana = True
        O disappointed "...What gave it away?"
        Y worried "Nah, it's just... It seemed like you have strong feelings regarding...proper care and handling of...glasses?"
        O thinking "I suppose. I've been wearing glasses almost my whole life."
        O default "I have a proper holder for mine on my own nightstand."
        Y surprised "Oh, cool..."
        Y thinking "....."
        O disappointed "...Did you not have a purpose for that question?"
        Y worried2 "I guess I didn't..."
        I "Maybe this wasn't worth the second glance..."
        $ fadein_sideimage = True
        $ show_side_oriana = False
    return

label d1a1_check_masterlamp:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.9 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "An ornate [t_pacclue]lamp[t_paccluee]. The lampshade is made of a thin white paper."
    Y surprised "...Wait, is this not plugged in?"
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O confused "Does it matter? It's not like there's any power running."
    Y thinking "Sure, but...if the cord's not even plugged in, then that suggests that this lamp was never in use even before the power went out."
    O surprised "That's...a fair point..." with shakeonce
    O confused "But this is just a bedside lamp, which can hardly serve as a room's main source of lighting."
    O "There could be any number of reasons why it was unplugged. Perhaps even long before the power outage."
    $ fadein_sideimage = True
    $ show_side_oriana = False
    I "Mrgh... I feel like I'm collecting more questions than answers looking around here..." with hpunch
    if not d1a1_masterbedroom_clue8:
        $ investigation_clues_optional_found += 1
        $ d1a1_masterbedroom_clue8 = True
    return

label d1a1_check_masterdresser:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.0 yalign 0.8 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if not d1a1_masterbedroom_clue9:
        I "A large [t_pacclue]dresser[t_paccluee]. Let's take a look through the drawers..."
        play ctc_sfx sfx_drawer_open
        Y default "And inside the top drawer is...{cps=1} {/cps}{nw}"
        play ctc_sfx "<silence 1.0>"
        $ fadein_sideimage = False
        extend relaxed "Drawers." with hpunch
        $ show_side_oriana = True
        O disappointed "....."
        Y "{cps=6}.....{/cps}{nw}"
        play ctc_sfx sfx_emotesigh
        extend worried2 " ...Okay, I'm not proud of that one." with hpunch
        Y default "But in all seriousness, it's mostly undershirts and undershorts in here. White and gray ones."
        O thinking "And the other drawers?"
        play ctc_sfx [sfx_drawer_open, sfx_drawer_open]
        Y thinking "The others..." with hpunch
        Y surprised "Huh. They're both empty."
        O confused "Empty...?"
        $ fadein_sideimage = True
        $ show_side_oriana = False
        play sound [sfx_drawer_close, sfx_drawer_close]
        I "Strange... So less than half of this dresser is in use..."
        if not d1a1_masterbedroom_clue9:
            $ investigation_clues_optional_found += 1
            $ d1a1_masterbedroom_clue9 = True
    else:
        I "A large [t_pacclue]dresser[t_paccluee]. There's some innerwear in one drawer, but the others are empty."
        $ show_side_oriana = True
        O confused "The possible reasons a dresser has only one of its drawers in use..."
        $ fadein_sideimage = False
        Y surprised "Huh? What'd you say?"
        O blink "...Nothing, just thinking to myself."
        O sideeye "Let's look elsewhere, [name_player]."
        $ fadein_sideimage = True
        $ show_side_oriana = False
    return

label d1a1_check_carpet:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.4 yalign 1.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A simple green [t_pacclue]rug[t_paccluee] is keeping the bed and other furniture off the hardwood floor."
    if not d1a1_masterbedroom_clue10:
        Y default "Maybe there's something under the rug?"
        $ fadein_sideimage = False
        $ show_side_oriana = True
        O thinking "Not a bad theory... Let's take a look."
        $ fadein_sideimage = True
        $ renpy.music.set_volume(0.5, 1.5, channel="music")
        scene bg black with dissolvemed
        pause 1.0
        $ renpy.music.set_volume(1.0, 1.5, channel="music")
        scene bg masterbedroom:
            xalign 0.4 yalign 1.0 zoom 1.5
        with dissolvemed
        Y thinking "Hrm... Nothing, huh?"
        $ fadein_sideimage = False
        O blink "It certainly would've been nice to find a key or something after all that effort..."
        I "Yeah... Oh well, nothing ventured, nothing gained." with hpunch
        $ fadein_sideimage = True
        $ show_side_oriana = False
        if not d1a1_masterbedroom_clue10:
            $ investigation_clues_optional_found += 1
            $ d1a1_masterbedroom_clue10 = True
    else:
        I "Nothing strange over or under it."
    return

label d1a1_check_smallmirror:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg masterbedroom:
        xalign 0.1 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A small [t_pacclue]mirror[t_paccluee]. The kind used for applying makeup, I think."
    Y thinking "I can't really see my reflection in this..."
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O blink "The glass is really cloudy. It must be quite the historical artifact to get this bad..."
    show bg masterbedroom:
        xalign 0.1 yalign 0.5 zoom 1.5
        easein 2.0 xalign 0.0
    Y surprised "Huh, but there's also makeup stuff on this dresser. Doesn't that mean someone was using this mirror?"
    O confused "Actually... Considering the products here, it's not a very comprehensive set."
    O default "I have a feeling this is an assortment of makeup [t_clue]lost or left behind[t_cluee]."
    Y worried "You say it so ominously..."
    if d1a1_masterbedroom_clue2:
        Y thinking "Come to think of it, we said earlier that a man must've been using this room, right?"
        Y default "Are those products meant for men?"
        O thinking "They're certainly not branded for men, but of course, that doesn't mean men can't use them."
        O default "But again, since these are pretty random, I don't think even a man would seriously have {i}this{/i} be his whole makeup kit."
    $ fadein_sideimage = True
    I "Hmm... I wonder what the story is behind all these cosmetics..."
    $ show_side_oriana = False
    if not d1a1_masterbedroom_clue11:
        $ investigation_clues_optional_found += 1
        $ d1a1_masterbedroom_clue11 = True
    return



screen pac_d1a1_bedroom:
    style_prefix "pac"

    use pac_progress_gui(_("The Bedroom"))



    use pac_return_button("d1a1_bedroom_confirm_return", _("EXIT"))


    use pac_button(1550, 560, d1a1_bedroom_clue1, "d1a1_check_bedroom_bed", _("Bed"))
    use pac_button(630, 390, d1a1_bedroom_clue2, "d1a1_check_bookshelf", _("Bookshelf"))
    use pac_button(180, 630, d1a1_bedroom_clue3, "d1a1_check_dresser", _("Dresser"))
    use pac_button(470, 570, d1a1_bedroom_clue4, "d1a1_check_desk", _("Desk"))
    use pac_button(400, 750, d1a1_bedroom_clue5, "d1a1_check_unicorn", _("Unicorn"))
    use pac_button(400, 380, d1a1_bedroom_clue6, "d1a1_check_drawings", _("Drawings"))
    use pac_button(1180, 540, d1a1_bedroom_clue7, "d1a1_check_clock", _("Clock"))
    use pac_button(880, 630, d1a1_bedroom_clue8, "d1a1_check_redpanda", _("Red Panda"))
    use pac_button(1190, 640, d1a1_bedroom_clue9, "d1a1_check_cutedresser", _("Nightstand"))
    use pac_button(1570, 810, d1a1_bedroom_clue10, "d1a1_check_toybox", _("Toybox"))
    use pac_button(1580, 210, d1a1_bedroom_clue11, "d1a1_check_poster", _("Poster"))
    use pac_button(1140, 270, d1a1_bedroom_clue12, "d1a1_check_bedroomwindow", _("Window"))
    use pac_button(1080, 900, d1a1_bedroom_clue13, "d1a1_check_bedroomcarpet", _("Rug"))
    use pac_button(500, 60, d1a1_bedroom_clue14, "d1a1_check_decorations", _("Decorations"))
    use pac_button(1250, 460, d1a1_bedroom_clue15, "d1a1_check_bedroomlamp", _("Lamp"))
    use pac_button(1020, 670, d1a1_bedroom_clue16, "d1a1_check_stool", _("Stool"))
    use pac_button(590, 690, d1a1_bedroom_clue17, "d1a1_check_chair", _("Chair"))

label d1a1_check_bedroom_bed:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 1.0 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A very pretty [t_pacclue]bed[t_paccluee]. Complete with lace and heart decorations."
    if d1a1_bedroom_clue1 == False:
        I "It looks big enough for maybe two kids...but it might be a tight fit."
        I "So it was probably just [t_clue]one kid[t_cluee] using it."
        $ d1a1_bedroom_clue1 = True
    else:
        I "There was probably just [t_clue]one kid[t_cluee] using it."
    return

label d1a1_check_bookshelf:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.3 yalign 0.4 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A [t_pacclue]bookshelf[t_paccluee] decorated with an array of colourful book spines."
    I "Hmm... Skimming the titles..."
    I "Looks like they're mostly storybooks and study guides at an [t_clue]elementary school[t_cluee] level."
    $ d1a1_bedroom_clue2 = True
    return

label d1a1_check_dresser:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.0 yalign 0.7 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A cute [t_pacclue]dresser[t_paccluee] for storing clothes."
    if d1a1_bedroom_clue3 == False:
        I "...Looks like it's mainly [t_clue]girls' clothes[t_cluee] but..."
        I "They're definitely too small for any of us to wear."
        $ d1a1_bedroom_clue3 = True
    else:
        I "There's mainly little [t_clue]girls' clothes[t_cluee] in there."
    return

label d1a1_check_desk:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.2 yalign 0.6 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A small, but well-crafted [t_pacclue]desk[t_paccluee]."
    if d1a1_bedroom_clue4 == False:
        I "Looks like whoever used it was into [t_clue]painting[t_cluee]. Look at all of these different brushes and paints..."
        I "All covered with a layer of [t_clue]dust[t_cluee], though."
        I "Guess that means no one's used this for a while..."
        $ d1a1_bedroom_clue4 = True
    else:
        I "All the different [t_clue]paints and brushes[t_cluee] are covered in dust."
    return

label d1a1_check_unicorn:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.1 yalign 0.9 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_bedroom_clue5 == False:
        I "A stuffed animal shaped like a [t_pacclue]unicorn[t_paccluee]."
        I "Wait... Is a unicorn an animal?"
        I "...Okay, maybe it's just a stuffed unicorn...doll."
        $ d1a1_bedroom_clue5 = True
    else:
        I "A stuffed animal shaped like a... ...Wait."
        play ctc_sfx sfx_emotequestion
        I "Doesn't a [t_pacclue]unicorn[t_paccluee] have a horn? This doesn't have one..." with hpunch
        I "So this is just a...horse with wings? Is there a name for a creature like that?"
    return

label d1a1_check_drawings:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.2 yalign 0.4 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "Some [t_pacclue]drawings[t_paccluee] are taped to the wall here. Looks like a child drew them."
    I "A house, a person, and a...cat, I think?"
    if d1a1_checked_bathroom:
        play ctc_sfx sfx_emotequestion
        I "Huh, a [t_clue]black dog[t_cluee]... Wonder where I've seen one of those before..."
    else:
        I "And at the top is a dog and...something riding a rainbow."
    I "...Oh, there's more to the right. Another cat, a snowman, and a couple holding hands..."
    I "..... ...I guess these are cute, yeah."
    $ d1a1_bedroom_clue6 = True
    return

label d1a1_check_clock:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.7 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A little [t_pacclue]alarm clock[t_paccluee]."
    if d1a1_bedroom_clue7 == False:
        I "...9:55...? That can't be right..."
        play ctc_sfx sfx_emotesigh
        I "Oh wait, the hands aren't moving. The battery must've died a long time ago." with hpunch
        $ d1a1_bedroom_clue7 = True
    else:
        I "The battery's dead so it's not showing the correct time."
    return

label d1a1_check_redpanda:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.45 yalign 0.7 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_bedroom_clue8 == False:
        I "A stuffed animal shaped like..."
        I "...Uhh... Hold on, what is this called again...?{nw}"

        menu:
            extend ""
            "Raccoon":
                I "Right, this is a [t_pacclue]raccoon[t_paccluee]!" with vpunch
                I "Aren't these considered pests, though? Weird choice to make into a doll."
            "Tanuki":
                I "Oh right, this is a [t_pacclue]tanuki[t_paccluee]!" with vpunch
                I "I guess it makes sense to have a tanuki as a doll. I think they have magical powers...?"
        $ d1a1_bedroom_clue8 = True
    else:
        I "...Wait.{w=0.5} OH.{w=0.5}{nw}"
        play ctc_sfx sfx_emotehappy
        extend " Right, this is a [t_pacclue]red panda[t_paccluee]!" with vpunch
        I "Can't believe it slipped my mind. Glad it... Er..."
        play ctc_sfx sfx_emotequestion
        I "...Actually, how DID I suddenly remember its name?" with hpunch
    return
label d1a1_check_cutedresser:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.7 yalign 0.7 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A cute little [t_pacclue]nightstand[t_paccluee]. Going through the drawers..."
    play sound sfx_drawer_open
    I "A storybook... A box of marbles... Various plastic toys..." with hpunch
    play sound sfx_drawer_close
    I "Nothing useful here..."
    $ d1a1_bedroom_clue9 = True
    return

label d1a1_check_toybox:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 1.0 yalign 1.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    if d1a1_bedroom_clue10 == False:
        I "Is that a handle...? Oooh, this is a storage box!"
        I "Let's take a peek inside..."
        $ renpy.music.set_volume(0.5, 1.5, channel="music")
        scene bg black with dissolvemed
        I "Hmm... It's completely filled with toys... So I guess this is a [t_pacclue]toybox[t_paccluee]?"
        I "....." with hpunch
        I "Nope, nothing that seems like a useful clue..."
        $ renpy.music.set_volume(1.0, 1.5, channel="music")
        scene bg bedroom:
            xalign 1.0 yalign 1.0 zoom 1.5
        with dissolvemed
        I "....."
        play ctc_sfx sfx_emotesigh
        I "Sigh... I'm starting to think I should've just agreed with Oriana and left this room alone..." with hpunch
        $ d1a1_bedroom_clue10 = True
    else:
        I "A [t_pacclue]toybox[t_paccluee] completely packed with toys."
        I "I guess the heart pillow and the teddy bear were the child's favourites...?"
    return

label d1a1_check_poster:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 1.0 yalign 0.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A [t_pacclue]poster[t_paccluee] of a rabbit gazing out into the distance."
    I "...I wonder what troubles the rabbit has to think about."
    I "....."
    I "How it will survive the day, I bet. In that case, I guess I can relate..." with hpunch
    $ d1a1_bedroom_clue11 = True
    return

label d1a1_check_bedroomwindow:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.7 yalign 0.1 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A [t_pacclue]window[t_paccluee]. Looks the same as any other window I've seen so far."
    I "....." with shakeonce
    I "...Yep, doesn't open. Oh well, it's important to {i}try{/i}, at least."
    $ d1a1_bedroom_clue12 = True
    return

label d1a1_check_bedroomcarpet:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.6 yalign 1.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "There's a circular [t_pacclue]rug[t_paccluee] with a floral pattern on the floor."
    I "Hrm... Oh, it's really soft."
    I "Agh, I wonder if we're not supposed to wear shoes here." with hpunch
    $ d1a1_bedroom_clue13 = True
    return

label d1a1_check_decorations:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.0 yalign 0.0 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "There are some plastic star [t_pacclue]decorations[t_paccluee] hanging along the wall."
    I "Considering the dust on them, I guess they're not intended for any particular holiday or event."
    I "...Or maybe...they {i}were{/i} for an event, but something happened and..." with hpunch
    I "....."
    $ d1a1_bedroom_clue14 = True
    return

label d1a1_check_bedroomlamp:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.7 yalign 0.5 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A pretty table [t_pacclue]lamp[t_paccluee]. Looks like it's the type where you pull a chain to turn on or off."
    play ctc_sfx sfx_lightswitch
    I "....." with vpunch
    I "Oh yeah, there's no electricity right now."
    $ d1a1_bedroom_clue15 = True
    return

label d1a1_check_stool:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.55 yalign 0.7 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A tiny [t_pacclue]stool[t_paccluee]. I think only small children could sit on this."
    I "Hmm... I don't see us ever having a need for this..."
    $ d1a1_bedroom_clue16 = True
    return

label d1a1_check_chair:
    show pac_explode_star at pac_explode()
    show pac_explode at pac_explode()
    pause 0.25
    scene bg bedroom:
        xalign 0.2 yalign 0.7 zoom 1.0
        easein 0.5 zoom 1.5
    pause 0.25
    I "A [t_pacclue]chair[t_paccluee]. It's smaller than average to make it fit well with the desk."
    I "..... ...Yeah, I have no other thoughts about it."
    $ d1a1_bedroom_clue17 = True
    return

label d1a1_bedroom_confirm_return:
    I "Have I checked this room out enough yet...?{nw}"

    menu:
        extend ""
        "Return to the [t_clue]Hallway[t_cluee]":
            I "...Yeah, that's enough. I shouldn't keep Oriana waiting any longer."
            play ctc_sfx sfx_steps
            scene bg black with fade
            scene bg hallway with fade
            pause 1.0
            play ctc_sfx sfx_doorclose
            pause 1.0
            $ _last_say_who = 'O'
            show oriana sideeyeblink at mycenter with dissolve
            O "....."
            O sideeye "Well? Find anything?"
            Y sad "...No."
            O sideeyeblink "...Hmph."
            I "Yeah yeah, act smug if you want. I still think it was worth seeing for myself."
            $ investigation_location = "d1a1_hallway"
            if not d1a1_upstairs_clue2:
                $ investigation_clues_required_found += 1
                $ d1a1_upstairs_clue2 = True
        "Cancel":
            I "No, let's look around a bit more."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
