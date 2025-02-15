
label d1a0:
    $ quick_menu = False
    $ music_info = False
    call save_file_name_update (1, "d1a0")



    call screen new_game_darken_flashes

    show screen lock_hotkeys
    pause 1.0
    play sound sfx_introambiance_sequence1
    pause 2.0
    $ _history = False
    "{cps=16}...This is it.{/cps}{w=2.0}{nw}"
    scene bg black with dissolvemed
    "{cps=16}...After all that's happened...{/cps}{w=2.0}{nw}"
    "{cps=16}It comes down to this after all...{/cps}{w=2.0}{nw}" with shakeonce
    play sound2 sfx_introambiance_sequence2 fadein 0.5
    scene bg black
    show oriana hidden at myleft
    show cecilia hidden at myright
    with dissolveslow
    stop sound fadeout 0.5
    "{cps=16}All I have to do...{/cps}{w=3.0}{nw}"
    "{cps=16}...is make one {color=#ff0000}final choice{/color}.{/cps}{w=3.0}{nw}"
    play ctc_sfx sfx_introambiance_pentagramknife
    play sound sfx_introambiance_sequence3
    scene bg black with custom_flashquick()
    stop sound2 fadeout 0.5
    $ countdown_time_max = 28
    $ countdown_time = 28
    $ renpy.set_mouse_pos(960, 540)
    call screen character_select with shakeshort
    $ show_choicegrand = True
    $ mute_choice = True
    if _return is "red":
        play loop_sfx sfx_introambiance_sequence4_loop fadein 0.5
        show oriana_raw hidden at myleft
        show oriana_raw hidden at mycenter with move
        stop sound fadeout 0.5
        ".....{w=2.0}{nw}"
        menu:
            "KILL":
                pass
        play sound sfx_introkill_1
        show pov_knife:
            xalign 0.5 yalign 1.0
            zoom 0.8
        with dissolve
        ".....{w=2.0}{nw}"
        menu:
            "KILL":
                pass
        play sound sfx_introkill_2
        menu:
            "KILL":
                pass
        play sound sfx_introkill_3
        show bloodsplatter_1 at truecenter, blurring
        show oriana_raw hidden zorder 1 at mycenter:
            zoom 1.1 ypos 1.1
        show pov_knife zorder 3 at truecenter:
            xalign 0.5 yalign 1.0
            zoom 0.8
        with shakeonce
        menu:
            "KILL":
                pass
        play sound sfx_introkill_4
        show bloodsplatter_2 zorder 2 at truecenter, blurring
        show oriana_raw hidden at mycenter:
            zoom 1.3 ypos 1.25
        with shakeonce
        menu:
            "KILL":
                pass
            "KILL":
                pass
        play sound sfx_introkill_5
        show bloodsplatter_3 at truecenter, blurring
        show oriana_raw hidden at mycenter:
            zoom 1.5 ypos 1.4
        with shakeonce
        menu:
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
        play sound sfx_introkill_6
        show bloodsplatter_4 zorder 2 at truecenter, blurring
        show oriana_raw hidden at mycenter:
            zoom 1.7 ypos 1.55
        with shakeshort
        menu:
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
        play sound sfx_introkill_7
        show bloodsplatter_5 at truecenter, blurring
        show oriana_raw hidden at mycenter:
            zoom 1.9 ypos 1.7
        with shakeshort
        menu:
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
        play sound sfx_introkill_8

    if _return is "blue":
        play loop_sfx sfx_introambiance_sequence4_loop fadein 0.5
        show cecilia_raw hidden at myright
        show cecilia_raw hidden at mycenter with move
        stop sound fadeout 0.5

        ".....{w=2.0}{nw}"
        menu:
            "KILL":
                pass
        play sound sfx_introkill_1
        show pov_knife:
            xalign 0.5 yalign 1.0
            zoom 0.8
        with dissolve
        ".....{w=2.0}{nw}"
        menu:
            "KILL":
                pass
        play sound sfx_introkill_2
        menu:
            "KILL":
                pass
        play sound sfx_introkill_3
        show bloodsplatter_1 at truecenter, blurring
        show cecilia_raw hidden zorder 1 at mycenter:
            zoom 1.1 ypos 1.1
        show pov_knife zorder 3 at truecenter:
            xalign 0.5 yalign 1.0
            zoom 0.8
        with shakeonce
        menu:
            "KILL":
                pass
        play sound sfx_introkill_4
        show bloodsplatter_2 zorder 2 at truecenter, blurring
        show cecilia_raw hidden at mycenter:
            zoom 1.3 ypos 1.2
        with shakeonce
        menu:
            "KILL":
                pass
            "KILL":
                pass
        play sound sfx_introkill_5
        show bloodsplatter_3 at truecenter, blurring
        show cecilia_raw hidden at mycenter:
            zoom 1.5 ypos 1.3
        with shakeonce
        menu:
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
        play sound sfx_introkill_6
        show bloodsplatter_4 zorder 2 at truecenter, blurring
        show cecilia_raw hidden at mycenter:
            zoom 1.7 ypos 1.4
        with shakeshort
        menu:
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
        play sound sfx_introkill_7
        show bloodsplatter_5 at truecenter, blurring
        show cecilia_raw hidden at mycenter:
            zoom 1.9 ypos 1.5
        with shakeshort
        menu:
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
            "KILL":
                pass
        play sound sfx_introkill_8

    if _return is "none":
        stop sound fadeout 0.2
    stop loop_sfx fadeout 0.2
    window auto hide None
    scene bg black with custom_flashquick()
    $ show_choicegrand = False
    $ mute_choice = False
    pause 2.0

    play sound sfx_chapterintro
    scene cg eyecatch cecilia bloody at wobble
    show chaptertitle1_text:
        xpos 1300 xanchor 0.5 yalign 0.5 alpha 0.0 zoom 1.0
        pause 3.0
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 1.5 matrixcolor BrightnessMatrix(0.0)
            linear 1.5 matrixcolor BrightnessMatrix(0.5)
            repeat
    show chaptertitle1_subtext:
        xpos 1300 xanchor 0.5 yalign 0.57 alpha 0.0
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
    $ _history = True

label d1a1:
    $ renpy.block_rollback()
    call save_file_name_update (1, "d1a1")
    if day1_loop_count <= 0:
        $ show_side_player = False
        $ rollback_unlocked = False
    else:
        if not rollback_unlocked:
            $ rollback_unlocked = True
            $ toggle_rollback()
            call screen tutorial("anotherkillinggame")
            pause 0.5
            play sound sfx_flashback
            with custom_flashbulb()
            pause 0.5
            play sound2 sfx_shardobtain
            call screen tutorial("rollback")
            call screen tutorial("rollback2")
            pause 2.0

    play music bgm_awakening
    $ show_music_info_timer = music_info_pop_out_time()
    $ name_cecilia = _("???")
    $ name_oriana = _("???")
    $ input_name_dog = _("Dog")
    $ name_dog = "{color=#606060}"+input_name_dog+"{/color}"

    show text "{image=gui/ctc/10.png}\n{font=fonts/Changa-SemiBold.ttf}{size=+5}Advance dialogue to continue...{/size}\n{size=24}[t_hotkey]Left Click[t_hotkeye] or [t_hotkey]Space[t_hotkeye] or [t_hotkey]Enter[t_hotkeye] or {/size}{color=#888}{font=DejaVuSans.ttf}{size=24}{b}(A/Bottom Button){/b}{/size}{/font}{/color}{/font}":
        alpha 0.0
        pause 5.0
        linear 2.0 alpha 1.0
    $ show_side_cecilia = True
    $ fadein_sideimage = True
    C hidden "{size=-15}...ey...{/size}"
    hide text
    $ fadein_sideimage = False
    C "{size=-15}...awake...{/size}"
    $ fadein_sideimage = True
    I "Urgh..."
    I "What... What happened?"
    $ show_side_oriana = True
    O hidden "{size=-15}...if it didn't work...{/size}"
    I "...I hear...voices..."
    scene cg wakeup at wobble:
        blur 50.0
    show eye frame
    with eyeopen_slow
    pause 1.0
    $ renpy.pause(0.5, hard=True)
    Y wince "...Rrgh..."
    $ fadein_sideimage = False
    C hidden "Oh! She's waking up!"
    $ fadein_sideimage = True
    scene bg black with eyeclose_slow
    scene cg wakeup_blurring at wobble
    show eye frame at blurred
    with eyeopen
    scene bg black with eyeclose_quick
    scene cg wakeup_blurring at wobble
    show eye frame
    with eyeopen_quick
    scene bg black with eyeclose_quick
    scene cg wakeup_blurring at wobble
    show eye frame:
        xalign 0.5 yalign 0.5 zoom 1.0 alpha 1.0
        easein 0.7 zoom 2.0 alpha 0.5
        linear 0.5 alpha 0.0
    with eyeopen_quick
    show cg wakeup at wobble
    with dissolve
    pause 1.0
    $ renpy.pause(0.5, hard=True)
    $ name_cecilia = _("Strange Girl")
    C happy "Hey there, sleepyhead! Rise and shine!"
    scene cg wakeup:
        zoom 1.1 blur 5.0 xalign 0.5 yalign 0.5
        easein 5.0 zoom 1.0 blur 0.0
    with dissolve
    $ persistent.unlock_cg_wakeup = True
    I "Ugh, my head..."
    Y wince "...Where...am I...?"
    scene bg black with dissolvemed
    scene bg foyer:
        zoom 1.5 xalign 0.6 yalign 0.0
        linear 6.0 xalign 1.0
    with dissolvemed
    $ ctc_timer = 0
    pause 2.0
    scene bg foyer:
        zoom 1.5 xalign 0.4 yalign 1.0
        linear 6.0 xalign 0.0
    with dissolvemed
    $ ctc_timer = 0
    pause 2.0
    scene bg foyer:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 3.0 zoom 1.0
    with dissolvemed
    $ ctc_timer = 0
    show screen notify_location("1 этаж - Фойе", persistent.unlock_bg_foyer) 
    $ persistent.unlock_bg_foyer = True
    pause 2.5
    $ _last_say_who = 'C'
    scene bg foyer
    show cecilia at mycenter
    with dissolve
    $ show_side_cecilia = False
    C "Are you okay? Does anything hurt?"
    Y wince "...Nrgh..." with hpunch
    $ fadein_sideimage = False
    Y "...Wh-who are you?"
    $ fadein_sideimage = True
    C "....."
    Y surprised "...?"
    C thinking "Hmm... I suppose we've never met before, huh?"
    O hidden "Is she awake?"
    scene bg foyer
    show cecilia_raw as cecilia at mycenter_to_myright, backedaway_on
    pause 0.3
    show oriana at myleft with dissolve
    $ show_side_oriana = False
    $ name_oriana = _("Gloomy Girl")
    O "....."
    Y surprised "Um... And you are...?"
    play ctc_sfx sfx_whooshlow
    show cecilia_raw surprised as cecilia
    show oriana leering2 at mycenter_closeup
    O "Well? What do you remember?" with shakeshort
    Y panicked "Wha...?!" with hpunch
    show oriana leering2 at myleft
    play ctc_sfx sfx_emotesigh
    show cecilia sweatdrop at myright, shrink, backedaway_off
    C "Hey now! She only just woke up! Let's take it easy with the questions."
    O confused "R-right. We should first make sure there isn't anything wrong with her."
    Y thinking "Um... What's going on? What is this place?"
    show cecilia at myright
    C "Before we answer that, let's start with some introductions!"
    $ name_cecilia = _("Cecilia")
    $ name_oriana = _("Oriana")
    C happy "My name's Cecilia! And the beautiful, bespectacled bombshell to my right here is...?"
    O irritated "...Oriana. {size=-10}That lead-in was unnecessary...{/size}"
    C smile "So! What is {i}your{/i} name?"
    Y surprised "My name...?"
    I "My name..."

    if not seen_ending_chaos and not seen_ending_order and not seen_ending_karma:
        hide screen notify_location
        scene bg black
        with dissolve
        call name_entry

    if input_name == "Karma" or input_name == "Carol-Maria":
        Y default "...It's...[name_player]."
        stop music
        show oriana surprised
        show cecilia_raw surprised as cecilia at backedaway_on
        show bg black
        with custom_flashquick()
        O "!!!"
        show cecilia surprised at backedaway_off
        C "!!!"
        O "...Did... Did it not work...?"
        C thinking "No, I think this might be a coincidence..."
        Y "...I..."
        O leering "We can't be too careful. Let's {color=#ff0000}start over{/color}."
        C blink "Yeah, that's probably for the best."
        Y "What are you--"
        $ _last_say_who = 'C'
        play ctc_sfx sfx_whoosh
        show cecilia blink with custom_flashquick()
        scene bg black
        with soulout
        $ quick_menu = False
        pause 3.0
        show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}THE END{/size}\nThank you for playing!{/font}" with dissolve
        pause 3.0
        hide text with dissolveslow
        pause 2.0
        $ quick_menu = True
        return
    else:
        Y default "...It's...[name_player]."

    C "[name_player], huh...?"
    C happy "Nice to meet you, [name_player]!"
    O default "....."
    O blink "Alright... [name_player]. I guess since you just woke up..."
    O sideeye "You don't know anything about the situation we're in, do you?"
    Y thinking "A...situation?"
    C smug "Look behind you! See the writing on that door there?"
    Y surprised "Behind me...?"
    hide screen notify_location
    scene bg black with dissolve
    scene bg frontdoor incomplete
    with dissolvemed
    $ persistent.unlock_bg_frontdoor_incomplete = True
    stop music fadeout 2
    pause 2.0
    I "That's...quite the door..."
    show bg frontdoor incomplete:
        zoom 1.2 xalign 0.5 yalign 1.0
        easein 6.0 zoom 1.3 xalign 0.4 yalign 0.0
    with dissolve
    I "...Hm? There's something written on it."
    play ctc_sfx sfx_heartbeat_single
    I "{cps=12}\"This door will not open...\"{/cps}"
    play ctc_sfx sfx_heartbeat_single
    I "{cps=12}\"...until one of you...{color=#ff0000}DIES{/color}...?\"{/cps}"
    scene bg black with dissolvemed
    scene bg foyer
    show oriana thinking at myleft_fadein
    show cecilia smile at myright_fadein
    with dissolvemed
    Y surprised "...Wha..."
    $ fadein_sideimage = False
    play music bgm_criminal
    $ show_music_info_timer = music_info_pop_out_time()
    Y afraid2 "What is this?! Are we trapped in here?!" with shakeshort
    $ fadein_sideimage = True
    show cecilia happy at myright, hop
    C "Ahaha, good to see you got the right idea!"
    Y "How can you laugh at something like this?!" with hpunch
    show oriana sideeyeblink at myleft
    O "Ignore her. Ever since she woke up, she's been all giddy like that."
    Y shocked "Ever since...? S-so, both of you woke up here without any explanation too?"
    C grin "Pretty much! Spooky, isn't it?"
    O "The most unsettling part is..."
    O confused "Neither of us have any memory of being kidnapped or brought here."
    C thinking "It's the strangest thing, right? Almost like we were spirited away!"
    I "...Come to think of it... I don't recall how I fell asleep in the first place."
    if seen_ending_chaos and seen_ending_order and seen_ending_karma:
        I "In fact..."
        I "....."
        I "......."
        jump d1a4
    else:
        I "In fact..."
    play ctc_sfx "<silence 1.0>"
    $ renpy.music.set_volume(0.0, 0, channel="music")
    $ renpy.music.set_volume(1.0, 3, channel="music")
    hide oriana
    hide cecilia
    show bg black
    with custom_flashquick()
    I "...I can't remember anything."
    play ctc_sfx "<silence 1.0>"
    I "It's all blank. I...don't remember anything about myself!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    scene bg foyer
    show oriana leering2 at myleft
    show cecilia surprised at myright
    with fade
    $ renpy.music.set_volume(1.0, 3, channel="music")
    C "Hmm? What's wrong, [name_player]? You look kinda pale."
    Y sad "...! I...uh... It's nothing..." with hpunch
    O thinking "...[name_player]. I think I know what your answer will be, but..."
    O default "Do you remember anything about how you ended up here? Anything at all?{nw}"

    menu:
        extend ""
        "Tell the truth":
            Y sad "Well... The truth is..."
            $ fadein_sideimage = False
            Y "I don't seem to have any memory about myself at all."
            $ fadein_sideimage = True
            O stunned "...None at all?"
            Y default "Just that my name is [name_player]. Nothing else."
            O confused "....."
            C smile "....."
            Y sad "...Wh-what? What are those looks for?"
            O surprised "I-it's nothing, don't worry about it."
            O thinking "I guess you must have experienced the worst of...whatever this is."
            O "The most I can say is that my memory is...fuzzy in some places."
            C happy "Ooh! Me too!"
            C thinking "Like, I remember who I am, but the past day or so's a total blur!"
            I "They're acting kinda weird..."
        "Lie to them":
            Y sad "N-no, sorry. I don't remember how I got brought here."
            $ fadein_sideimage = False
            Y thinking "I guess someone kidnapped me while I was sleeping...?"
            $ fadein_sideimage = True
            O leering "....."
            C surprised "....."
            C smile "...Well, that's unfortunate. I guess none of us have any clues as to how we ended up here."
            O sideeyeblink "The culprit responsible for trapping us here is a complete mystery..."
            Y blink "....."
            I "Good, I think they bought it."
            I "I feel bad, but it's probably safer if they don't know about my amnesia..."
            O sideeye "....."

    O sideeyeblink "...Well, no matter. It doesn't change the fact that we need to find a way to escape this place."
    C pout "Yeah, I don't want to stay here overnight! I can't sleep unless I have my special pillow!"
    I "I think a bigger concern is that there's someone in this house out to kill us...?" with hpunch
    O default "Just to finish catching you up, [name_player], Cecilia and I woke up about an hour before you did."
    O blink "Since you weren't coming to, we took a look around to see if there were any other exits."
    C happy "Good thing I came back here in time to notice you waking up!"
    C smile "Imagine how scared you would've been if you woke up in this creepy house, and no one was around~"
    Y worried "...Y-yeah. So did you find anything?"
    O confused "A couple of the doors are unlocked, but none of them lead to an exit..."
    C thinking "Meanwhile, the windows are all TOTALLY locked, and we can't even see what's outside because of that weird fog!"
    O thinking "If we keep looking, maybe we'll find some keys or other [t_clue]clues[t_cluee]..."
    C happy "It's like an escape room! Fun, right?"
    Y sad "....."
    O annoyed "Tsk..." with shakeonce
    O irritated "In any case, this is probably a lot to take in all at once."
    O default "Do you have any questions, [name_player]?{nw}"

    menu:
        extend ""
        "\"What is the weird fog?\"":
            Y surprised "What do you mean by \"weird fog\"?"
            O "Every window we've checked, there's an unnaturally thick fog covering up the outside."
            O sideeye "You can see it for yourself. Look at the door behind you again."
            scene bg frontdoor incomplete
            with fade
            pause 1.0
            Y default "...Oh yeah. There are windows surrounding the door..."
            $ fadein_sideimage = False
            $ show_side_oriana = True
            O confused "That fog makes it hard to tell if there are any people nearby that could hear us call for help..."
            $ fadein_sideimage = True
            $ show_side_oriana = False
            I "It's weirdly thick and bright... Why does it make me feel so uneasy...?"
            scene bg foyer
            show oriana confused at myleft
            show cecilia thinking at myright
            with fade
            C thinking "What's {i}really{/i} strange is that the fog makes it hard to tell if it's day or night."
            C blink "At least we have the clock here by the door, even if it doesn't say if it's A.M. or P.M.--"
        "\"Can't we call for help?\"":
            Y leering "Have you tried calling for help?"
            O leering "Obviously."
            O irritated2 "We screamed, banged on the doors... But nothing. No response from anyone."
            C sad "And of course, they took away our phones."
            C happy "But at least thanks to modern technology, the culprit won't unlock my secrets so easily~"
            C thinking "Well, unless they chop off one of my fingers. Or maybe use the facial recognition by--"
        "\"About the writing on the door...\"":

            Y thinking "So, um... If the writing on the door is for real, then will it really open if... Well..."
            C grin "Oooh, you're going straight there? Love it~"
            O leering2 "Shut up, Cecilia."
            O irritated2 "And [name_player], no. That is NOT an option."
            Y surprised "But it sure seems like the only way out is to have one of us--"
            play ctc_sfx sfx_emoteshout
            O shouting "I said that's NOT an option!" with shakeshort
            C smug "You're pushing it, [name_player]. Let's give it some time first."
            I "Give it some time...?"

    play ctc_sfx "<silence 1.0>"
    play sound [sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime]
    stop music
    $ _last_say_who = None
    window auto hide None
    show bg black
    with custom_flashquick()
    show cecilia surprised at hop
    show oriana surprised at hop
    with shakeshort
    pause 2.0
    Y panicked "...Wha..." with vpunch
    I "That startled me..." with shakeonce
    show bg foyer with dissolve
    C thinking "Oooh, look, it came from the clock by the door! Looks like it's 6 o'clock!"
    O irritated "6 o'clock..."
    C default "Hmm? What's that scowl on your face for? Are you hungry?"
    O "....."
    play ctc_sfx sfx_emotequestion
    O "...[t_clue]How much time[t_cluee] do you think we have?"
    Y thinking "...!" with shakeonce
    C sweatdrop "\"How much\"...? Er, what do you mean?"
    O leering2 "Do you think whoever trapped us here will be fine with us taking our sweet time, looking for a way to escape?"
    C default "....."
    O shadow "Or perhaps..."
    show bg black with dissolve
    O "Perhaps this house is in fact inescapable...{w=0.5} And we'll simply starve to death if we don't...{nw}" with shakeonce

    menu:
        extend ""
        "Say something":
            Y panicked "H-hey, don't go giving up already! We haven't checked out every part of this house yet, right?"
            O "....."
            C sweatdrop "Acting all smart and determined one minute, then completely deflated the next... *sigh* This girl is such a mess..."
            C smile "...Don't you think so too, [name_player]?"
            Y sad "I..." with shakeonce
        "Say nothing":
            Y sad "....."
            C surprised "Whoa whoa, [name_player], you too?"
            C "....."
            C thinking "Gosh, you guys are such downers... Here we are in one of the most thrilling situations one could ever be in..."
            C sad "And you just give up all hope immediately? Laaaaame~"
    O "......."
    O irritated "Tch. ...All right, that's enough talking. We need to move." with hpunch
    C grin "...Pft."
    I "...?"
    show bg foyer with dissolvemed
    play music bgm_discussion
    $ show_music_info_timer = music_info_pop_out_time()
    O leering "[name_player], now that you're awake, you can help us look for clues."
    O thinking "Even if we can't find a way out, we might be able to figure out who's keeping us here and why."
    C happy "Yeah! And then we can take it to 'em!"
    Y surprised "...Er... Take what, exactly?"
    C smug "You know, vengeance! Retribution!"
    C blink "I mean, this person kidnapped three defenseless girls, trapped them in a creepy house, and is threatening to kill them all."
    C smile "Don't you think people like that should just drop dead?{nw}"
    menu:
        extend ""
        "\"Absolutely.\"":
            Y blink "If our kidnapper's serious about the writing on the door, then..."
            $ fadein_sideimage = False
            Y leering "We need to put an end to this before anyone else becomes a victim."
            $ fadein_sideimage = True
            C surprised "....."
            C smile "Hmm... So THAT'S your answer, huh?"
            I "...What?"
        "\"Hard to say...\"":
            Y sad "I mean... Death might be a little harsh..."
            $ fadein_sideimage = False
            Y "We can just turn them in to the authorities, right?"
            $ fadein_sideimage = True
            C surprised "....."
            C thinking "Hmm... So THAT'S your answer, huh?"
            I "...What?"
    O leering "I get where both of you are coming from, but we should prioritize our personal safety."
    O "[name_player], if you run into anyone suspicious, [t_clue]run away immediately[t_cluee]."
    Y default "Right."
    O "Cecilia, that goes for you too."
    C pout "Yeah yeah..."
    O sideeyeblink "Again, we're focusing on collecting information."
    O sideeye "Let's split up and investigate every room in this house thoroughly."
    C default "I was in the middle of checking out the kitchen so...I guess I'll go back there."
    C happy "[name_player], come join me if you get lonely~ [u_heart]"
    play ctc_sfx "<silence 1.0>"
    play sound sfx_steps
    window auto hide
    hide cecilia
    with dissolvemed
    play sound sfx_doorclose
    pause 0.5
    $ _last_say_who = "O"
    show oriana sideeyeblink at mycenter
    with move
    O "...In that case, I'll continue investigating the rooms upstairs."
    O "Based on what I've found so far, this seems to be an ordinary house, but..."
    O thinking "I wonder if this place holds some dark secret..."
    play sound sfx_steps_heels
    scene bg foyer with dissolvemed
    stop music fadeout 3
    pause 3.0
    I "...And just like that, they're both gone."
    I "I still have so many questions, though..."
    Y thinking ".....{w=1.0}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    extend worried " *sigh*" with hpunch
    $ fadein_sideimage = True
    I "I guess there isn't much else to do but join in on the investigation effort."
    scene bg foyer:
        zoom 1.5 xalign 0.0 yalign 0.8
    with dissolve
    I "So Cecilia went to the [t_clue]kitchen[t_cluee]..."
    scene bg foyer:
        zoom 1.5 xalign 1.0 yalign 0.0
    with dissolve
    I "Oriana went [t_clue]upstairs[t_cluee]..."
    scene bg foyer:
        zoom 1.5 xalign 0.6 yalign 1.0
    with dissolve
    I "...Huh? I think that door under the stairs is a little open."
    I "Looks like...a [t_clue]bathroom[t_cluee]? That might be worth checking out..."
    scene bg foyer
    with dissolve
    I "All of them seem promising... Guess I'll just pick wherever I want to go first..."
    if day1_loop_count <= 0:
        call screen tutorial("controls")
        call screen tutorial("save1")
        pause 0.5
    if day1_loop_count == 1:
        call screen tutorial("skip")
        pause 0.5


    $ d1a1_checked_kitchen = False
    $ d1a1_checked_bathroom = False
    $ d1a1_checked_upstairs = False
    $ d1a1_chaos_flag = ""
    $ d1a1_order_flag = ""

label d1a1_start_investigation:
    call save_file_name_update (1, "d1a1_start_investigation")
    I "Let's see... Where should I go?"
    menu:
        "Investigate the [t_clue]Kitchen[t_cluee]" if d1a1_checked_kitchen == False:
            I "I might as well join Cecilia in the kitchen."
            I "It'd be nice if I can find something to eat too..."
            if d1a1_checked_bathroom and d1a1_checked_upstairs:
                jump d1a2
            else:
                call d1a1_kitchen
        "[u_check]Investigate the [t_clue]Kitchen[t_cluee]" if d1a1_checked_kitchen == True:
            I "I checked out the kitchen pretty thoroughly. No need to go back there unless it's time for us to eat."
            I "Besides, I...don't know if I want to spend more time talking to Cecilia..."
            jump d1a1_start_investigation

        "Investigate the [t_clue]Bathroom[t_cluee]" if d1a1_checked_bathroom == False:
            I "I guess I should go check out that bathroom."
            I "There probably isn't any way to escape there, but might as well see if there are any interesting clues."
            if d1a1_checked_kitchen and d1a1_checked_upstairs:
                jump d1a2
            else:
                call d1a1_bathroom
        "[u_check]Investigate the [t_clue]Bathroom[t_cluee]" if d1a1_checked_bathroom == True:
            I "There was nothing in that bathroom that could serve as a useful clue."
            I "I wonder why the dog suddenly appeared there. And then it took off so suddenly..."
            I "Maybe... Was it checking {i}me{/i} out?"
            Y blink "...I wonder if I'll see that dog again..."
            jump d1a1_start_investigation

        "Investigate the rooms [t_clue]Upstairs[t_cluee]" if d1a1_checked_upstairs == False:
            I "There's probably lots to check out upstairs."
            I "I should go give Oriana a hand with investigating all of that."
            if d1a1_checked_kitchen and d1a1_checked_bathroom:
                jump d1a2
            else:
                call d1a1_upstairs
        "[u_check]Investigate the rooms [t_clue]Upstairs[t_cluee]" if d1a1_checked_upstairs == True:
            I "We already checked all the rooms upstairs."
            I "...I wonder what Oriana feels like she still needs to investigate...?"
            jump d1a1_start_investigation

        "{color=#cccc00}Gather your thoughts{/color}" if seen_ending_chaos or seen_ending_order or seen_ending_karma:
            I "...Huh? I wonder why I have this strange feeling of [t_clue]déjà vu[t_cluee]."
            Y thinking "{cps=6}.....{/cps} ...Maybe I don't need to be in a rush..."
            I "Should I think more carefully about where I should go next?{nw}"

            menu:
                extend ""
                "{color=#cccc00}Learn what to do next{/color}":
                    if not seen_ending_chaos:
                        if not d1a1_checked_kitchen:
                            I "...Hmm... I guess it can't hurt to hang out with Cecilia."
                            I "She seems like a fun, cheery girl. What's the worst that could happen?"
                        else:
                            I "......."
                            I "...I can't help but think about what Cecilia said..."
                            I "Mrgh... Agh, okay, let's just do what we can for now..."
                    elif not seen_ending_order:
                        if d1a1_order_flag == "A":
                            I "It's good that I managed to calm Oriana down but..."
                            play ctc_sfx sfx_heartbeat_single
                            I "Why do I have a strong feeling that I made the [t_clue]wrong choice[t_cluee] somehow...?" with shakeonce
                            I "Agh, if only I could turn back time..."
                        else:
                            if not d1a1_checked_kitchen:
                                I "...I have a very bad feeling about Cecilia. If possible, I should [t_clue]avoid hanging out with her[t_cluee]..."
                                if not d1a1_checked_upstairs:
                                    I "It might be good to talk with Oriana [t_clue]upstairs[t_cluee] and see how she feels about all this."
                                    if seen_ending_karma:
                                        play ctc_sfx sfx_heartbeat_single
                                        I "...I also have a feeling that [t_clue]we can't avoid violence[t_cluee] here..." with shakeonce
                            else:
                                I "......."
                                I "...Maybe I shouldn't have hung out with Cecilia..."
                                I "Why does it feel like I know what's going to happen later...?" with hpunch
                    else:
                        I "...Something's wrong... I can't shake this horrible feeling in my gut..."
                        if not d1a1_checked_bathroom:
                            if not d1a1_checked_kitchen or not d1a1_checked_upstairs:
                                I "I should talk to [t_clue]both[t_cluee] Cecilia and Oriana. Before it's too late..."
                            else:
                                I "But... I think I've done everything I can..."
                        else:
                            I "...I think it might be too late... I never should've [t_clue]investigated the bathroom[t_cluee]..." with hpunch
                "\"I don't need any hints!\"":
                    I "...No, I guess I shouldn't depend on strange feelings right now."
                    I "This is a serious situation. I should make my decisions more carefully..."
            jump d1a1_start_investigation

    if not d1a1_checked_kitchen or not d1a1_checked_bathroom or not d1a1_checked_upstairs:
        I "Guess I should investigate somewhere else now."
        jump d1a1_start_investigation



label d1a1_kitchen:
    call save_file_name_update (1, "d1a1_kitchen")
    play ctc_sfx sfx_steps
    scene bg black with fade
    play sound sfx_dooropen
    pause 1.0
    scene bg diningroom withchair:
        xalign 0.3 yalign 0.5 zoom 1.5
        easein 7.0 zoom 1.0
    with fade
    play sound ["<silence 1.0>", sfx_doorclose]
    pause 2.0
    show screen notify_location("1 этаж - Столовая", persistent.unlock_bg_diningroom_withchair)
    $ persistent.unlock_bg_diningroom_withchair = True
    pause 2.0
    I "This...doesn't look like the kitchen..."
    I "Looks more like a [t_clue]dining room[t_cluee]?"
    scene bg diningroom withchair:
        zoom 1.5 xalign 1.0 yalign 1.0
    with dissolve
    I "Oh, I think the kitchen is further ba... Er..."
    play ctc_sfx sfx_emotequestion
    I "...Wh-what's that mess over there? A...broken chair?"
    scene bg diningroom withchair with dissolve
    Y worried "....."
    $ fadein_sideimage = False
    Y default "Uh... C-Cecilia...?"
    $ show_side_cecilia = True
    C hidden "...Hmm? Oh! [name_player]! I'm over here!"
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    I "Yep, she's in the kitchen. ...Let's just walk around this mess, I guess..."
    hide screen notify_location
    play ctc_sfx sfx_steps
    scene bg black with fade
    pause 1.0
    scene bg kitchen fullknives:
        zoom 1.75 xalign 0.6 yalign 0.0
        linear 6.0 xalign 1.0
    with dissolvemed
    pause 2.0
    scene bg kitchen fullknives:
        zoom 1.5 xalign 0.4 yalign 1.0
        linear 6.0 xalign 0.0
    with dissolvemed
    pause 2.0
    scene bg kitchen fullknives:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 3.0 zoom 1.0
    with dissolvemed
    show screen notify_location("1 этаж - Кухня", persistent.unlock_bg_kitchen_fullknives)
    $ persistent.unlock_bg_kitchen_fullknives = True
    pause 2.0
    $ _last_say_who = 'C'
    show cecilia happy at mycenter with dissolve
    play ctc_sfx sfx_emotehappy
    C "Hiii~[u_music_note] Did you come to see little ol' me?"
    Y surprised "Y-yeah, I guess? I just thought it might be good to help you investigate this room."
    I "And see if I can get something to eat..."
    C smile "That's really sweet of you, [name_player]!"
    show cecilia sweatdrop at shrink
    play ctc_sfx sfx_emotesigh
    C "Truth be told, I haven't really looked around this kitchen yet."
    show cecilia at mycenter
    C "I was in the dining room trying to see if I could break open any of the windows."
    C thinking "They're made of glass, right? So I figured swinging a chair at it would definitely do the trick."
    Y panicked "You...SWUNG that chair?"
    C happy "Like a rioter, yep!"
    show cecilia pout at hop
    C "But it's so strange! The chair fell apart, and yet there's not even a crack on that glass!"
    I "Just how strong is this girl...?" with hpunch
    C thinking "Hmm... Maybe if I could find something heavier. Something metal..."
    Y thinking "I think before we try breaking more things, maybe we can take a look around for some clues first?"
    C happy "Okay~ Sounds like a plan!"
    hide cecilia with dissolve
    I "...Hmm... It may also be worth it to check out that dining room I passed through."
    I "Guess I have my work cut out for me. Better get...{nw}"
    play ctc_sfx "<silence 1.0>"
    show cecilia_raw grin as cecilia at mycenter, backedaway_on:
        alpha 0.0
        linear 1.0 alpha 1.0
    extend "{w=1.0}started...?"
    play ctc_sfx "<silence 1.0>"
    show cecilia grin at mycenter, backedaway_off:
        alpha 1.0
    C "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y surprised "...Uh... Is there something on my face?" with shakeonce
    C blink "Oh, don't mind me~ Just look around to your heart's content!"
    C smile "And if you need any help, just give me a little [t_clue]poke[t_cluee]!"
    I "....."
    I "...I had a feeling, but now I'm sure about it."
    I "This girl...is a little scary..."
    hide screen notify_location
    $ persistent.unlock_bg_kitchen = True

    if not seen_tutorial_investigations:
        call screen tutorial("investigations")
        $ seen_tutorial_investigations = True

    $ d1a1_kitchen_clue1 = False
    $ d1a1_kitchen_clue2 = False
    $ d1a1_kitchen_clue3 = False
    $ d1a1_kitchen_clue4 = False
    $ d1a1_kitchen_clue5 = False
    $ d1a1_kitchen_clue6 = False
    $ d1a1_kitchen_clue7 = False
    $ d1a1_kitchen_clue8 = False
    $ d1a1_kitchen_clue9 = False
    $ d1a1_kitchen_clue10 = False

    $ d1a1_visited_diningroom = False
    $ d1a1_diningroom_clue1 = False
    $ d1a1_diningroom_clue2 = False
    $ d1a1_diningroom_clue3 = False
    $ d1a1_diningroom_clue4 = False
    $ d1a1_diningroom_clue5 = False
    $ d1a1_diningroom_clue6 = False
    $ d1a1_diningroom_clue7 = False
    $ d1a1_diningroom_clue8 = False
    $ d1a1_diningroom_clue9 = False
    $ d1a1_diningroom_clue10 = False
    $ d1a1_diningroom_clue11 = False

    $ investigation_location = "d1a1_kitchen"
    $ investigation_complete = False
    $ investigation_perfect = False
    $ investigation_clues_required = 6
    $ investigation_clues_required_found = 0
    $ investigation_clues_optional = 15
    $ investigation_clues_optional_found = 0

    $ music_info = False
    scene bg kitchen with dissolve
    play sound sfx_pac_intro2
    call screen pac_investigation_start(_("The Kitchen with Cecilia"), _("Search the kitchen and dining room for clues to escape!\nTalk to Cecilia when you want to switch rooms."))
    $ music_info = True
    stop sound
    play music bgm_chaos
    $ show_music_info_timer = music_info_pop_out_time()

label d1a1_kitchen_investigation:
    $ renpy.choice_for_skipping()
    if investigation_location == "d1a1_diningroom":
        scene bg diningroom withchair with dissolvequick
        if not investigation_complete:
            if investigation_clues_required_found >= investigation_clues_required:
                $ investigation_complete = True
                if investigation_clues_optional_found >= investigation_clues_optional:
                    $ investigation_perfect = True
                    call d1a1_kitchen_perfect
                else:
                    call d1a1_kitchen_complete
        elif not investigation_perfect:
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d1a1_kitchen_perfect
        call screen pac_d1a1_diningroom with dissolvequick
    else:
        scene bg kitchen with dissolvequick
        if not investigation_complete:
            if investigation_clues_required_found >= investigation_clues_required:
                $ investigation_complete = True
                if investigation_clues_optional_found >= investigation_clues_optional:
                    $ investigation_perfect = True
                    call d1a1_kitchen_perfect
                else:
                    call d1a1_kitchen_complete
        elif not investigation_perfect:
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d1a1_kitchen_perfect
        call screen pac_d1a1_kitchen with dissolvequick
    if investigation_location != None:
        jump d1a1_kitchen_investigation
    else:
        jump d1a1_kitchen_end

label d1a1_kitchen_end:
    $ investigated_kitchen = True
    scene bg black
    scene bg diningroom withchair with dissolvemed
    $ fadein_sideimage = True
    Y blink "Looks like that's everything covered. Both the kitchen and the dining room."
    $ fadein_sideimage = False
    Y sad "And there really was nothing useful..."
    $ fadein_sideimage = True
    I "...I can't help but wonder if there's really no way out of this place..."
    I "And that our only choice if we want to escape is to really..."
    play ctc_sfx "<silence 1.0>"
    window auto hide None
    show zoom_cecilia at truecenter
    $ renpy.music.set_volume(0.0, 0, channel="music")
    pause 0.5
    hide zoom_cecilia
    show cecilia at mycenter_return with custom_flashquick()
    play sound sfx_whooshlow
    window auto show None
    Y afraid "AAAAHHHHH!!" with shakelong
    show cecilia at mycenter:
        zoom 1.0 xalign 0.5 yanchor 1.0 ypos 1.05
    show cecilia happy at hop
    play ctc_sfx sfx_emotehappy
    C "Ahahahaha~ You really jumped there, [name_player]!"
    $ renpy.music.set_volume(1.0, 3, channel="music")
    play ctc_sfx sfx_emoteshout
    Y shouting "DON'T DO THAT! I thought my heart was gonna stop!" with shakeshort
    C smile "Then stop brooding already~ You're gonna get wrinkles on your forehead, you know."
    Y worried "That's the least of my problems right now..."
    I "How can she be fooling around in a situation like this...?" with shakeonce
    C thinking "Anyway... Not a lot of clues overall, huh?"
    C blink "But at least we got two clues towards getting out of here."
    Y surprised "W-wait, really? Two? What are they?"
    play ctc_sfx "<silence 1.0>"
    stop music fadeout 3.0
    call save_file_name_update (1, "d1a1_kitchen_end")
    C grin "The [t_clue]knives[t_cluee] and the [t_clue]rat poison[t_cluee]."
    Y afraid "...! Wha..." with shakeonce
    C smug "Hey c'mon, [name_player], don't give me that look~"
    C blink "Isn't it obvious that whoever trapped us here wants one of us to die?"
    C default "Since we've been given at least two possible murder weapons, it sure seems like they'll actually let us go if we do what they say."
    Y shouting "Y-you're talking about killing someone here! Ending someone's life!" with shakeonce
    C thinking "Um, yeah? Duh?"
    C default "You know, I'm starting to think you don't fully understand the situation here."
    Y shocked "I-I don't..?"
    C blink "[name_player], think about it."
    C default "There's exactly three of us in this house."
    C "Only one of us needs to die."
    C blink "That means all it takes is for two people to agree that the third person should... Well, give up on escaping, I suppose."
    I "....."
    C thinking "Afterwards, those two people can go home safe and sound. And if anyone asks what happened..."
    show bg diningroom withchair dark
    $ persistent.unlock_bg_diningroom_withchair_dark = True
    show cecilia surprised at myleft with hpunch
    C "A crazy kidnapper abducted three innocent girls, murdered one of them..."
    show cecilia sobbing at myright with hpunch
    C "...and the other two, traumatized from the event, are unable to remember what exactly went down."
    show cecilia blink at mycenter, shudder with move
    C "The kidnapper and potential murderer remains at large to this day..."
    show bg diningroom withchair with dissolve
    C happy "...And the truth behind that one girl's murder never comes to light. The end."
    Y shocked "...Y-you're not suggesting..."
    $ fadein_sideimage = False
    Y "...that you and I..."
    Y "{cps=6}...{/cps}{w=0.8}[t_clue]kill Oriana[t_cluee]?{nw}"
    play music bgm_decision_chaos
    $ show_music_info_timer = music_info_pop_out_time()
    play ctc_sfx "<silence 1.0>"
    extend "" with shakeonce
    $ fadein_sideimage = True
    C blink "......."
    C "...Who knows? I'm just exploring a very plausible sequence of events that could occur."
    C smile "...Do you...find it interesting?"
    $ _last_say_who = None
    show bg black with dissolve
    I "...If I think about it, it's a tempting idea..."
    I "Nobody would find out what we'd done. But more importantly..."
    I "What would happen...if I refuse her offer?"
    I "Wha... Wh-what should I do...? What should I say?" with shakeonce
    play ctc_sfx sfx_heartbeat_single
    play loop_sfx sfx_heartbeat
    show cecilia smile at mycenter:
        zoom 1.0 ypos 1.05
        easein 20.0 zoom 1.5 ypos 1.25
    with dissolve
    $ show_choicegrand = True
    menu:
        "\"Yes, let's kill her.\"":
            $ show_choicegrand = False
            $ d1a1_chaos_flag = "A"
            stop music
            stop loop_sfx
            scene bg black
            show cecilia smile at mycenter
            with custom_flashbulb()
            pause 0.5
            show bg diningroom withchair with dissolve
            Y shadow2 "...Alright. I'm in."
            $ fadein_sideimage = False
            Y "I think we should do it."
            $ fadein_sideimage = True
            play ctc_sfx sfx_emotequestion
            C surprised "Hmm? Do what? What are you talking about?"
            Y panicked "Wh-what do you mean? Weren't you saying that we should--" with shakeonce
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "I was just exploring possibilities!"
            C grin "It's important to consider all of them when you're investigating mysteries, you know!"
            Y troubled "...S-so...you were just...?"
            C blink "...But that's what you think we should do, huh...?"
            C smile "[name_player]..."
            Y afraid "Huh?"
            C happy "Welp! I think that about wraps up this conversation!"
            C default "Just leave the rest here to me! I'll clean up this busted chair and start getting dinner ready!"
            if d1a1_kitchen_clue1:
                C sweatdrop "Well, if you're still hungry of course. I know the refrigerator might have spoiled your appetite."
            else:
                C smile "You can last a little longer without food, right?"
            Y sad "Y-yeah, I think I'm still good for a while." with hpunch
            $ fadein_sideimage = False
            Y "I'll go look around the rest of the house until it's time to eat."
            $ fadein_sideimage = True
            C default "Sure thing! I'll go look for you once I figure out how I'm gonna open the canned food."
            C happy "Stay safe, [name_player]!"
            play ctc_sfx sfx_steps
            scene bg black with fade
            play sound sfx_dooropen
            scene bg foyer with fade
            play sound ["<silence 1.0>", sfx_doorclose]
            pause 2.0
            Y shadow "......."
            I "I have a very strong feeling that later tonight..."
            play ctc_sfx sfx_heartbeat_single
            I "{color=#ff0000}Something{/color}...is going to happen..." with shakeonce
            I "Did I...make a bad decision here?"
            Y blink "....... *sigh*" with hpunch
            $ fadein_sideimage = False
            Y sad "Well... No point in thinking too hard about it."
            Y default "It's not like I can turn back time or anything. Let's keep moving forward."
            $ fadein_sideimage = True
        "\"No, we can't do this!\"":

            $ show_choicegrand = False
            $ d1a1_chaos_flag = "B"
            stop music
            stop loop_sfx
            scene bg black
            show cecilia smile at mycenter
            with custom_flashbulb()
            pause 0.5
            show bg diningroom withchair with dissolve
            Y blink "...No. We can't kill anyone."
            $ fadein_sideimage = False
            Y "We have to get out here together. All of us."
            Y leering "That's...the right thing to do."
            $ fadein_sideimage = True
            C surprised "....."
            Y "......."
            C thinking "Hmm. That's a surprisingly respectable answer."
            Y worried2 "\"Surprisingly\"...?"
            C sad "But...yeah, I suppose that's the outcome all of us would prefer."
            C smug "Let's just hope it's doable before time runs out."
            Y sad "Right... We still don't know how long we have..."
            C happy "Aw, don't worry too much about it, [name_player]."
            C default "If life has taught me anything, it's that things have a mysterious way of just working out."
            C blink "But you know... [t_clue]Time never flows backwards[t_cluee]."
            C "And sometimes, you're forced to make a decision to go one way or the other."
            C "Sacrifice something to gain something else."
            C smile "Those are the moments where it might be worth worrying. Just a little bit."
            Y thinking "....."
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "Hey c'mon, you're scowling again! Don't wrinkle that pretty face of yours!"
            C grin "Right now, you still have plenty of options! One of them is bound to let you get everything you want!"
            C blink "Now go take a walk. Check out some of the other rooms. I need to clean up this busted chair before we can all eat dinner."
            Y surprised "Right... Okay."
            C blush "See you later!"
            play ctc_sfx sfx_steps
            scene bg black with fade
            play sound sfx_dooropen
            scene bg foyer with fade
            play sound ["<silence 1.0>", sfx_doorclose]
            pause 2.0
            Y thinking "......."
            I "Cecilia... Just what {i}is{/i} she...?"
            I "Is she someone I can trust? Someone who has our best interests at heart?"
            I "...I...don't know why, but... Deep down, I know [t_clue]I can trust her[t_cluee]..."
            play ctc_sfx sfx_emotequestion
            I "But at the same time, I also know that [t_clue]I CAN'T trust her[t_cluee]... What is this bizarre feeling...?"
            Y worried "..... *sigh*" with hpunch
        "\"I...I don't know...\"":

            $ show_choicegrand = False
            $ d1a1_chaos_flag = "C"
            stop music
            stop loop_sfx
            scene bg black
            show cecilia smile at mycenter
            with custom_flashbulb()
            pause 0.5
            show bg diningroom withchair with dissolve
            Y shadow "...I... I don't know what the right decision is here..."
            $ fadein_sideimage = False
            Y "If we can't leave without having one of us die, then..."
            Y "Does it have to be Oriana? Does it have to be whoever simply {i}happened{/i} to be absent from this conversation?"
            Y "As a person, I don't know her at all. ...Does she...deserve to be the one to die?"
            $ fadein_sideimage = True
            C blink "....."
            C "Who \"deserves\" death, huh...?"
            C "It's easy to say that people who are genuinely evil deserve to die."
            C "In fact, our society endorses it. Calls it pretty words like \"justice\" or \"retribution\"."
            Y wince "...!" with shakeonce
            C thinking "But wanting someone to die... How different is that from actually making someone die?"
            C default "In some cultures, wishing death upon others is the same sin as actually killing them."
            C "So then, wouldn't those people clamoring for the deaths of others be just as evil as those they condemn?"
            C "Can \"justice\" end up being \"evil\" in disguise?"
            I "....."
            C thinking "Then what is \"evil\" anymore? Killing people definitely makes someone \"evil\", right?"
            C "Is it NOT \"evil\" to kill someone who IS \"evil\"? Is it \"evil\" to refuse to kill someone who is, by all definitions, \"evil\"?"
            Y thinking "...What are you..."
            C sweatdrop "I dunno, the line gets blurry and confusing really fast, so I don't blame you for not knowing what to do."
            C blink "\"Does Oriana DESERVE to die?\" ...You don't need to find an answer to that question."
            C smile "...At least...not yet."
            Y sad "...Huh? What do you--{w=0.3}{nw}"
            play ctc_sfx sfx_slap
            $ fadein_sideimage = False
            show cecilia happy at mycenter_zoom with custom_flashquick()
            extend panicked " Mmph!" with shakeshort
            $ fadein_sideimage = True
            play ctc_sfx sfx_emotehappy
            show cecilia blush
            C "Anyways, c'mon, smile now! Lift those cheeks!"
            Y worried "Leh go oh mah hace!" with shakeonce
            show cecilia blush at mycenter_return
            pause 0.5
            hide cecilia
            show cecilia wink at mycenter
            C "I didn't mean to stress you out, [name_player]. Forgive me, okay? [u_heart]"
            C default "Why don't you go check out the other parts of the house now?"
            C happy "It's good to lose yourself in an activity to shake off those meaningless worries!"
            Y surprised "...Uh..."
            C thinking "I'll stay here, though. I need to clean up this chair and maybe see if I can get dinner ready."
            Y sad "...I... I guess...thank you?"
            C blush "No need for thanks! Catch you later, [name_player]~"
            play ctc_sfx sfx_steps
            scene bg black with fade
            play sound sfx_dooropen
            scene bg foyer with fade
            play sound ["<silence 1.0>", sfx_doorclose]
            pause 2.0
            Y thinking "......."
            I "It's weird but..."
            I "I feel like that might have been Cecilia's crazy way of...encouraging me."
            I "She knows how severe our situation is, and I think she wanted me to just think seriously about what we're gonna do."
            I "...That hypothetical threw me for a loop, though. I mean, this is murder we're talking about."
            Y worried "Yeesh..." with hpunch

    $ d1a1_checked_kitchen = True
    return




label d1a1_bathroom:
    call save_file_name_update (1, "d1a1_bathroom")
    play ctc_sfx sfx_steps
    scene bg black with fade
    play sound sfx_dooropen
    pause 1.0
    scene bg bathroom:
        xalign 0.2 yalign 0.5 zoom 1.5
        ease 5.0 zoom 1.0
    with fade
    pause 3.0
    show screen notify_location("1 этаж - Ванная", persistent.unlock_bg_bathroom)
    $ persistent.unlock_bg_bathroom = True
    pause 2.0
    I "..... ...It's smaller than I thought."
    I "Guess this is supposed to be a guest bathroom."
    I "There isn't much besides a sink and a toilet, but if I look carefully, I might find something interesting."
    Y leering "Alright, investigation time!" with shakeonce
    hide screen notify_location

    if not seen_tutorial_investigations:
        call screen tutorial("investigations")
        $ seen_tutorial_investigations = True

    $ d1a1_bathroom_clue0 = False
    $ d1a1_bathroom_clue1 = False
    $ d1a1_bathroom_clue2 = False
    $ d1a1_bathroom_clue3 = False
    $ d1a1_bathroom_clue4 = False
    $ d1a1_bathroom_clue5 = False
    $ d1a1_bathroom_clue6 = False
    $ d1a1_bathroom_clue7 = False
    $ d1a1_bathroom_clue8 = False
    $ d1a1_bathroom_clue9 = False
    $ d1a1_bathroom_clue10 = False
    $ d1a1_bathroom_clue11 = False

    $ d1a1_sink_on = False
    $ d1a1_checked_trash = False
    $ rng_min = 1
    $ rng = renpy.random.randint(rng_min, 21)
    $ d1a1_treasure_found = False

    $ investigation_location = "d1a1_bathroom"
    $ investigation_complete = False
    $ investigation_perfect = False
    $ investigation_clues_required = 3
    $ investigation_clues_required_found = 0
    $ investigation_clues_optional = 9
    $ investigation_clues_optional_found = 0

    $ music_info = False
    scene bg bathroom with dissolve
    play sound sfx_pac_intro
    call screen pac_investigation_start(_("The Bathroom with..."), _("What clues can you discover in this tiny bathroom?\nMaybe some can only be found while you're alone...?"))
    $ music_info = True
    stop sound
    play music bgm_karma
    $ show_music_info_timer = music_info_pop_out_time()

label d1a1_bathroom_investigation:
    $ renpy.choice_for_skipping()
    if d1a1_sink_on:
        scene bg bathroom sinkon with dissolvequick
    else:
        scene bg bathroom with dissolvequick
    if not investigation_complete:
        if investigation_clues_required_found >= investigation_clues_required:
            $ investigation_complete = True
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d1a1_bathroom_perfect
            else:
                call d1a1_bathroom_complete
    elif not investigation_perfect:
        if investigation_clues_optional_found >= investigation_clues_optional:
            $ investigation_perfect = True
            call d1a1_bathroom_perfect
    call screen pac_d1a1_bathroom with dissolvequick
    if investigation_location != None:
        jump d1a1_bathroom_investigation
    else:
        jump d1a1_bathroom_end

label d1a1_bathroom_end:
    call save_file_name_update (1, "d1a1_bathroom_end")
    $ investigated_bathroom = True
    Y blink "Alright, let's get out of--{w=0.3}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx sfx_strike
    stop music fadeout 3
    extend panicked "WHOA!" with shakeshort
    $ fadein_sideimage = True
    scene bg black with custom_flashquick()
    play sound sfx_fallsoft
    pause 1.0
    I "Ow... I think I tripped over something..."
    Y wince "Agh... Wh-what was..."
    $ _last_say_who = "D"
    scene bg bathroom
    show dog at mycenter
    with dissolvemed
    pause 2.0
    D "....."
    I "...Wha..."
    I "Is that...a [t_clue]dog[t_cluee]?"
    I "Where did it come from? ...Does... Does it live here?"
    Y thinking "......."
    D "........."
    I "It's just sitting there. Staring at me..."
    I "Is it friendly...?{nw}"

    menu:
        extend ""
        "Pet it":
            I "It's kinda cute... Let's try petting it."
            I "Slowly now..."
            window auto hide
            $ _last_say_who = "D"
            show bg bathroom:
                zoom 1.0
                easein 3.0 zoom 1.5
            show dog:
                zoom 1.0 ypos 1.05
                easein 3.0 zoom 1.5 ypos 1.2
            pause 4.0
            D "....."
            I "Yep, still sitting there, not making a sound..."
            Y surprised "Whoa, its fur is [t_clue]really cold[t_cluee]. Maybe it was playing outside?"
            $ fadein_sideimage = False
            Y thinking "...\"Outside\"? Wait..."
            Y leering "Could this dog have come from...?!" with shakeonce
        "Don't pet it":
            I "...I think I'll just stare back at it and keep my guard up."
            I "I can't really remember, but I don't think I'm good with dogs."
            I "Besides, the others didn't mention there being a dog so...it could only belong to the culprit."
            I "...Wait, that's weird. Why would a kidnapper bring their dog here before locking everything up?"
            window auto hide
            $ _last_say_who = "D"
            pause 0.5
            show collar glow at mycenter:
                alpha 0.0
                easein 0.4 alpha 1.0
                linear 1.2 alpha 0.0
            pause 1.5
            D "....."
            Y surprised "...Huh? That's a pretty [t_clue]weird collar[t_cluee]..."
            $ fadein_sideimage = False
            Y thinking "Looks like it's made of heavy metal. It's like a prisoner's shackle..."

    play ctc_sfx sfx_whoosh
    play sound sfx_dogsteps
    show bg bathroom:
        zoom 1.0
    hide dog
    with custom_flashquick()
    Y panicked "Hey-- Whoa!" with shakeonce
    $ fadein_sideimage = True
    I "It ran off!"
    play music bgm_tension
    $ show_music_info_timer = music_info_pop_out_time()
    Y shouting "Wait, come back!" with shakeshort
    play ctc_sfx ["<silence 1.0>", sfx_doorclose_quick] 
    play sound sfx_running
    scene bg black with dissolve
    pause 1.0
    scene bg foyer with dissolve
    pause 2.0
    Y surprised "...Huh? Where is..."
    show dog_raw at myleft with moveinleft
    Y shouting "There it is!" with shakeonce
    I "What should I do?{nw}"

    menu:
        extend ""
        "Try to catch it":
            Y surprised "Okay, come on... Come here now..."
        "Let it go":
            jump d1a1_dog_escaped

    show dog_raw at myright with move
    I "It's avoiding me...{nw}"


    menu:
        extend ""
        "Pounce and grab it":
            Y leering "3... 2... 1!"
            window auto hide None
            play ctc_sfx sfx_whooshlow
            show dog_raw at myleft with hpunch
            play sound sfx_fallsoft
            show dog_raw with shakeshort
            pause 1.0
            I "It dodged?!"
        "Approach it slowly":
            Y happy "Okay, come on... Come here now..."
            D "....."
            I "Steady..."
            window auto hide None
            play ctc_sfx sfx_whooshlow
            show dog_raw at mycenter with hpunch
            pause 0.2
            play ctc_sfx sfx_whoosh
            show dog_raw at myleft with vpunch
            pause 0.5
            play ctc_sfx sfx_whooshhigh
            show dog_raw at myright with custom_flashquick()
            pause 0.5
            I "Wha-- It zipped around me!"
        "Let it go":

            jump d1a1_dog_escaped

    window auto hide
    show dog_raw at hop
    pause 0.3
    show dog_raw at mycenter with move
    play sound sfx_emotehappy
    show dog_raw at doublehop
    pause 0.5
    show dog_raw at shudder
    pause 0.3
    window auto show
    I "...It's..."
    I "Is it...TAUNTING me?!{nw}" with shakeonce


    menu:
        extend ""
        "Approach it from the left":
            Y annoyed "Okay... THIS way!"
            play ctc_sfx sfx_whooshlow
            show dog_raw at myright with vpunch
            I "Or so you think but..."
            show dog_raw at myleft with custom_flashquick()
            Y shouting "I'm over here!" with shakeonce
            window auto hide None
            play ctc_sfx sfx_whoosh
            show dog_raw at myright with hpunch
            pause 0.2
            play sound sfx_fallsoft
            show dog_raw with shakeshort
            pause 0.5
            Y wince "Ow... How did it...?!"
        "Approach it from the right":
            Y shouting "Okay... THAT way!"
            D "....."
            I "...It's not falling for that."
            Y blink "Alright... Then how about--"
            play ctc_sfx sfx_whoosh
            show dog_raw at myleft with custom_flashquick()
            pause 0.5
            show dog_raw at doublehop
            Y shouting "THERE!"
            window auto hide None
            play ctc_sfx sfx_whooshlow
            show dog_raw at myright with hpunch
            pause 0.2
            play ctc_sfx sfx_whoosh
            show dog_raw at mycenter with shakeonce
            show dog_raw at shudder
            pause 0.5
            I "Damn it, so close!"
        "Let it go":

            jump d1a1_dog_escaped

    show dog_raw at hop
    pause 0.3
    show dog_raw at myleft with move
    I "...I'm not done yet!{nw}"


    menu:
        extend ""
        "Try to trick it":
            Y relaxed "...Okay. You win, little doggy."
            $ fadein_sideimage = False
            Y "I'll just be on my..."
            $ fadein_sideimage = True
            play ctc_sfx sfx_whoosh
            show dog_raw at myright with custom_flashquick()
            play sound sfx_fallsoft
            show dog_raw with shakeshort
            pause 0.5
            I "I'm still on my feet!"
        "Match its movements":
            Y leering "All right, you're not fooling me anymore..."
            I "If I do this...!"
            play ctc_sfx sfx_whooshlow
            show dog_raw at mycenter with vpunch
            I "Yeah! And next...!"
            play ctc_sfx sfx_whooshlow
            show dog_raw at mycenter with hpunch
            show dog_raw at doublehop
            I "NOW!"
        "Let it go":

            jump d1a1_dog_escaped

    window auto hide None
    play ctc_sfx sfx_whoosh
    show dog_raw at myleft with vpunch
    pause 0.5
    play ctc_sfx sfx_whooshlow
    show dog_raw at mycenter with shakeonce
    pause 0.3
    play ctc_sfx sfx_whooshlow
    show dog_raw at right with hpunch
    pause 0.2
    play ctc_sfx sfx_whoosh
    show dog_raw at myleft
    show dog_raw as dog2 at myright
    with custom_flashquick()
    pause 0.25
    play sound sfx_emoteshout
    window auto show None
    Y afraid2 "WHAT THE HECK?!{nw}" with shakeshort
    $ fadein_sideimage = False


    menu:
        extend ""
        "Grab the right one":
            Y shouting "AGH, OKAY, THAT ONE!" with shakeonce
            $ fadein_sideimage = True
            play ctc_sfx sfx_whoosh
            window auto hide None
            show dog_raw as dog2 at mycenter with vpunch
            pause 0.2
            play ctc_sfx sfx_whooshlow
            show dog_raw at right with hpunch
            pause 0.2
            play ctc_sfx sfx_whooshlow
            show dog_raw as dog2:
                rotate 180 xalign 0.5
                yalign 1.0
            show dog_raw at right with hpunch
            pause 0.3
            play ctc_sfx sfx_whoosh
            show dog_raw at left with vpunch
            pause 0.2
            play ctc_sfx sfx_whooshlow
            hide dog_raw as dog2
            show dog_raw at myright
            with custom_flashquick()
            show dog_raw at hop
            window auto show
            play sound sfx_emoteshout
            Y afraid "WHAT IS THIS THING?!" with shakeshort
        "Grab the wrong one":
            Y angry "Okay, I'll--{w=0.5}{nw}"
            play sound sfx_emoteshout
            extend panicked " Wait, grab the [t_clue]WRONG[t_cluee] one?!" with shakeshort
            Y "How do I--"
            $ fadein_sideimage = True
            show dog_raw at hop
            show dog_raw as dog2 at doublehop
            show dog_raw at offscreenright with move
            show dog_raw as dog2 at offscreenleft with move
            I "What the..."
            window auto hide None
            hide dog_raw
            hide dog_raw as dog2
            show dog_raw at myleft with moveinbottom
            play sound sfx_emotehappy
            pause 0.1
            hide dog_raw with moveoutbottom
            show dog_raw at mycenter with moveinbottom
            play sound sfx_emotesigh
            pause 0.1
            hide dog_raw with moveoutbottom
            show dog_raw at myright with moveinbottom
            play sound sfx_emotequestion
            pause 0.1
            hide dog_raw with moveoutbottom
            show dog_raw at mycenter with moveinbottom
            play sound sfx_emotesigh
            pause 0.1
            hide dog_raw with moveoutbottom
            show dog_raw at myright with moveinbottom
            play sound sfx_emotequestion
            pause 0.1
            hide dog_raw with moveoutbottom
            show dog_raw at myleft with moveinbottom
            play sound sfx_emotehappy
            pause 0.1
            hide dog_raw with moveoutbottom
            show dog_raw at mycenter with moveinbottom
            play sound sfx_emotesigh
            pause 0.1
            hide dog_raw with moveoutbottom
            show dog_raw at myleft with moveinbottom
            play sound sfx_emotehappy
            Y pained "OKAY, OKAY, STOP!" with shakeshort
        "Let it go":

            $ fadein_sideimage = True
            scene bg foyer
            show dog_raw at mycenter
            with dissolve
            jump d1a1_dog_escaped

    play sound sfx_fallsoft
    play ctc_sfx sfx_whoosh
    show dog_raw at mycenter with custom_flashquick()
    show dog_raw with shakeshort
    show dog_raw at shudder
    stop music fadeout 3.0
    Y troubled "*pant* *pant*" with shakeonce
    show dog_raw at doublehop
    $ fadein_sideimage = False
    Y "*gasp* *pant* *cough*" with shakeonce
    $ fadein_sideimage = True

    label d1a1_dog_escaped:
        stop music fadeout 3.0
        I "...Wait, what am I doing? How is chasing this dog gonna help us at all?"
        $ _last_say_who = 'D'
        scene bg foyer
        show dog at mycenter
        with dissolve
        D "....."
        window auto hide
        show dog at shudder
        pause 1.0
        play sound sfx_dogsteps
        hide dog with dissolve
        pause 1.5
        window auto show
        I "...And there it goes. Gone without a trace."
        I "Why did it show up in the first place...?"
        Y thinking "{cps=12}.....{/cps}{w=0.5}{nw}"
        play ctc_sfx "<silence 1.0>"
        $ fadein_sideimage = False
        extend worried " *sigh*" with shakeonce
        Y sad "Investigating by myself didn't amount to anything... I better stop wasting time and go meet up with someone..."
        $ fadein_sideimage = True
        I "...Hrm... There's definitely more than meets the eye to that dog, though."
        I "Next time I see it, I'd better catch it for sure..."
        I "....."

    $ d1a1_checked_bathroom = True
    return




label d1a1_upstairs:
    call save_file_name_update (1, "d1a1_upstairs")
    play ctc_sfx sfx_steps
    scene bg black with fade
    pause 1.0
    scene bg hallway:
        xalign 0.5 yalign 0.5 zoom 1.25
        easein 5.0 zoom 1.0
    with dissolvemed
    pause 2.0
    show screen notify_location("2 этаж - Коридор", persistent.unlock_bg_hallway)
    $ persistent.unlock_bg_hallway = True
    pause 2.0
    I "A lot of doors..."
    I "I guess Oriana must be behind one of them."
    Y surprised "Hello? Oriana?"
    $ _last_say_who = 'O'
    $ renpy.music.set_pan(-0.65, 0.0, channel='ctc_sfx')
    $ renpy.music.set_pan(-0.65, 0.0, channel='sound')
    play ctc_sfx sfx_dooropen
    play sound sfx_steps_heels
    $ renpy.music.set_pan(-0.1, 2.0, channel='sound')
    scene bg black with dissolve
    pause 1.0
    scene bg hallway
    show oriana blink at myleft_far
    with dissolve
    pause 0.5
    play ctc_sfx sfx_doorclose
    pause 0.5
    show oriana blink at mycenter with move
    O default "Oh. ...[name_player]. What brings you here?"
    $ renpy.music.set_pan(0.0, 0.0, channel='ctc_sfx')
    $ renpy.music.set_pan(0.0, 0.5, channel='sound')
    Y default "I thought that you could use some help going through all these rooms."
    O thinking "Is that so? ...Thank you."
    O default "I already gave every room a quick glance, but I couldn't find anything that could help us escape."
    O "However, I think it's still worth examining each room carefully for any clues on the [t_clue]demon[t_cluee]."
    Y thinking "Er... \"demon\"?"
    O leering "The person responsible for trapping us here in the first place."
    I "Oh, the kidnapper. Our culprit. The mastermind. I-I guess \"demon\" is now another label...?"
    O irritated2 "Writing that horrible condition on the door to trick us into killing each other..."
    O leering "Only a deranged, psychopathic monster would do something like that."
    Y sad "......."
    O blink "...In any case. Let's go take a look around, [name_player]. You take the lead."
    Y surprised "Huh? Me?"
    O sideeye "Is that a problem?"
    Y thinking "N-no, I guess I... N-never mind."
    O sideeyeblink "....."
    I "Is she...testing me or something...?"
    hide screen notify_location

    if not seen_tutorial_investigations:
        call screen tutorial("investigations")
        $ seen_tutorial_investigations = True

    $ d1a1_upstairs_clue1 = False
    $ d1a1_upstairs_clue2 = False
    $ d1a1_upstairs_clue3 = False
    $ d1a1_upstairs_clue4 = False
    $ d1a1_upstairs_clue5 = False
    $ d1a1_upstairs_clue6 = False
    $ d1a1_upstairs_clue7 = False
    $ d1a1_upstairs_clue8 = False
    $ d1a1_upstairs_clue9 = False
    $ d1a1_upstairs_clue10 = False

    $ d1a1_bedroom_clue1 = False
    $ d1a1_bedroom_clue2 = False
    $ d1a1_bedroom_clue3 = False
    $ d1a1_bedroom_clue4 = False
    $ d1a1_bedroom_clue5 = False
    $ d1a1_bedroom_clue6 = False
    $ d1a1_bedroom_clue7 = False
    $ d1a1_bedroom_clue8 = False
    $ d1a1_bedroom_clue9 = False
    $ d1a1_bedroom_clue10 = False
    $ d1a1_bedroom_clue11 = False
    $ d1a1_bedroom_clue12 = False
    $ d1a1_bedroom_clue13 = False
    $ d1a1_bedroom_clue14 = False
    $ d1a1_bedroom_clue15 = False
    $ d1a1_bedroom_clue16 = False
    $ d1a1_bedroom_clue17 = False

    $ d1a1_visited_masterbedroom = False
    $ d1a1_masterbedroom_clue1 = False
    $ d1a1_masterbedroom_clue2 = False
    $ d1a1_masterbedroom_clue3 = False
    $ d1a1_masterbedroom_clue4 = False
    $ d1a1_masterbedroom_clue5 = False
    $ d1a1_masterbedroom_clue6 = False
    $ d1a1_masterbedroom_clue7 = False
    $ d1a1_masterbedroom_clue8 = False
    $ d1a1_masterbedroom_clue9 = False
    $ d1a1_masterbedroom_clue10 = False
    $ d1a1_masterbedroom_clue11 = False
    $ d1a1_jumped_bed = False

    $ investigation_location = "d1a1_hallway"
    $ investigation_complete = False
    $ investigation_perfect = False
    $ investigation_clues_required = 6
    $ investigation_clues_required_found = 0
    $ investigation_clues_optional = 15
    $ investigation_clues_optional_found = 0

    $ music_info = False
    scene bg hallway with dissolve
    play sound sfx_pac_intro
    call screen pac_investigation_start(_("2F with Oriana"), _("Check out each room in the 2nd floor with Oriana!\nSome rooms may have more clues than others..."))
    $ music_info = True
    stop sound
    play music bgm_order
    $ show_music_info_timer = music_info_pop_out_time()

label d1a1_upstairs_investigation:
    $ renpy.choice_for_skipping()
    if investigation_location == "d1a1_masterbedroom":

        if d1a1_masterbedroom_clue2 and d1a1_masterbedroom_clue4:
            if not d1a1_upstairs_clue4:
                $ investigation_clues_required_found += 1
                $ d1a1_upstairs_clue4 = True
        scene bg masterbedroom with dissolvequick
        if not investigation_complete:
            if investigation_clues_required_found >= investigation_clues_required:
                $ investigation_complete = True
                if investigation_clues_optional_found >= investigation_clues_optional:
                    $ investigation_perfect = True
                    call d1a1_upstairs_perfect
                else:
                    call d1a1_upstairs_complete
        elif not investigation_perfect:
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d1a1_upstairs_perfect
        call screen pac_d1a1_masterbedroom with dissolvequick
    elif investigation_location == "d1a1_bedroom":
        scene bg bedroom with dissolvequick
        call screen pac_d1a1_bedroom with dissolvequick
    else:
        scene bg hallway with dissolvequick
        if not investigation_complete:
            if investigation_clues_required_found >= investigation_clues_required:
                $ investigation_complete = True
                if investigation_clues_optional_found >= investigation_clues_optional:
                    $ investigation_perfect = True
                    call d1a1_upstairs_perfect
                else:
                    call d1a1_upstairs_complete
        elif not investigation_perfect:
            if investigation_clues_optional_found >= investigation_clues_optional:
                $ investigation_perfect = True
                call d1a1_upstairs_perfect
        call screen pac_d1a1_hallway with dissolvequick
    if investigation_location != None:
        jump d1a1_upstairs_investigation
    else:
        jump d1a1_upstairs_end

label d1a1_upstairs_end:
    $ investigated_upstairs = True
    scene bg black
    scene bg hallway with dissolvemed
    $ fadein_sideimage = True
    Y "We've checked out every room on this floor now, haven't we?"
    $ _last_say_who = 'O'
    show oriana blink at mycenter with dissolve
    O "Yes. It took some time, but at least we now have a few clues gathered."
    O thinking "And one conclusion we can make for sure is that there were [t_clue]two people[t_cluee] living in this house."
    I "The man in the master bedroom, and the little girl in the bedroom across the hall..."
    Y surprised "...Oh wait, at the end of the hall, what's around the corner over there?"
    O sideeyeblink "Just a dead end. Come on, you should go take a look."
    play ctc_sfx sfx_steps
    play sound ["<silence 0.2>", sfx_steps_heels]
    scene bg black with fade
    pause 0.5
    scene bg hallwayend:
        xalign 0.5 yalign 0.5 zoom 1.2
        easein 5.0 zoom 1.0
    with fade
    $ persistent.unlock_bg_hallwayend = True
    pause 3.0
    Y default "...Another painting. Kind of an eerie one too."
    $ fadein_sideimage = False
    Y surprised "But yeah, this really is just a dead end. What a strange layout..."
    $ fadein_sideimage = True
    $ _last_say_who = "O"
    show bg hallwayend at reset
    show oriana thinking at mycenter
    with dissolve
    O "....."
    Y thinking "And this wall on the right... I guess the master bedroom is on the other side?"
    O "......."
    Y surprised "...Oriana?"
    O "........."
    Y shouting "Oriana!" with shakeonce
    O ".........{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    show oriana panicked at hop
    extend "Huh? Wh-what is it?"
    Y leering "You went all quiet and spaced out there. What's wrong?"
    O thinking "O-oh... I'm sorry..."
    Y worried "I mean, it's nothing you need to apologize for..."
    O "I was just thinking about the writing on that door downstairs."
    O "\"This door will not open until one of you dies\"..."
    Y thinking "...Y-yeah?"
    O irritated "Why was that the extent of the information? Why was there nothing about a time limit, or the...the means of death?"
    O "It's as though the author of that message {i}wanted{/i} us to agonize over what that message means..."
    O "Hopelessly wander around the house, only to find there really isn't any other exit..."
    stop music fadeout 3.0
    call save_file_name_update (1, "d1a1_upstairs_end")
    O shadow "...And then have us, by our own free will, decide to kill each other, all without directly forcing us to do so..."
    Y sad "...That's..."
    O "Utterly demonic, yes..."
    O "We're dealing with someone who wants us to forsake our morals... Our humanity..."
    I "....."
    Y leering "B-but that's exactly why we're looking for the culprit, right?"
    $ fadein_sideimage = False
    Y shouting "We need to find them and put an end to all of this!" with shakeonce
    $ fadein_sideimage = True
    O irritated "The culprit... The...demon..."
    Y default "O-Oriana?"
    O "Let's say we DO find the culprit. What do we do from there?"
    Y surprised "Uh... I-I guess...demand they set us free?"
    O leering "And what if they refuse? What do you think will happen then?"
    Y sad "Then...they'll probably just kill us..."
    O irritated2 "....." with shakeonce
    Y leering "B-but there's three of us! If we just gang up on--"
    O shouting "What if it's a large, burly man?! What if it's more than one person?!" with shakeonce
    O "Do you honestly think the three of us are going to be any good in a fight?!" with shakeonce
    Y sad "I-I..."
    show bg hallwayend dark
    $ persistent.unlock_bg_hallwayend_dark = True
    O horrified "Don't you get it, [name_player]...?"
    O "There's no way out of this! One of us will have to DIE!" with shakeshort
    Y shocked "O-Oriana..."
    O depressed "...Why were we brought here? What did we do to deserve this?"
    O "Why can't they just kill us instead of making us turn on each other...?"
    Y sad "....." with hpunch
    O dejected "....."
    show oriana irritated at shudder
    O "Mrgh..."
    O "...Tell me something, [name_player]."
    O leering "...Are you..."
    O "{cps=6}...{/cps}{w=0.8}thinking of [t_clue]killing someone[t_cluee]?{nw}"
    play music bgm_decision_order
    $ show_music_info_timer = music_info_pop_out_time()
    play ctc_sfx "<silence 1.0>"
    extend "" with shakeonce
    Y panicked "...Wha..."
    O sideeye "You don't know me or Cecilia. Why should it matter to you if one of us dies, right?"
    Y afraid "That's--" with shakeonce
    O sideeyeblink "....."
    O irritated "...Murder is wrong."
    O "No matter the situation, no one deserves to end someone's life."
    O "Even THINKING about ending someone's life is disgusting." with shakeonce
    O shadow "...You...understand this, don't you?"
    $ _last_say_who = None
    show bg black with dissolve
    I "I... I'm pretty sure that depending on my answer to this question, things might take an unexpected turn..."
    I "I need to choose my answer carefully..."
    Y blink "{cps=6}.....{/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend default " ...I..."
    $ fadein_sideimage = True
    play ctc_sfx sfx_heartbeat_single
    play loop_sfx sfx_heartbeat
    show oriana shadow at mycenter:
        zoom 1.0 ypos 1.05
        easein 20.0 zoom 1.5 ypos 1.25
    with dissolve
    $ show_choicegrand = True
    menu:
        "\"It's always wrong to kill people.\"":
            $ show_choicegrand = False
            $ d1a1_order_flag = "A"
            stop music
            stop loop_sfx
            scene bg black
            show oriana shadow at mycenter
            with custom_flashbulb()
            pause 0.5
            show bg hallwayend with dissolve
            Y blink "...I agree with you completely."
            $ fadein_sideimage = False
            Y leering "I don't believe it's ever right to kill people either."
            $ fadein_sideimage = True
            O surprised "....."
            Y blink "The culprit definitely wants us to panic and try to kill each other, but..."
            $ fadein_sideimage = False
            Y leering "We can't lose to them. We need to do everything we can and get out of here. All of us. Together."
            $ fadein_sideimage = True
            O blink "....."
            O "...Yes. Yes, exactly."
            O happy "...You're a good person, [name_player]. I'm glad there's at least two of us who are."
            I "Whew... She looks a lot more relaxed now..."
            play ctc_sfx sfx_heartbeat_single
            I "In fact... I think this is the first time she's smiled that...warmly..." with hpunch
            play music bgm_order fadein 3.0
            $ show_music_info_timer = music_info_pop_out_time()
            O blink "All right, so back to the topic at hand..."
            O default "Even though we have access to the entire second floor, the same can't be said for the first."
            O "But I'm confident the last door in the foyer could be unlocked if we can find its [t_clue]key[t_cluee]."
            Y surprised "Really?"
            O confused "Well... There's reason to believe that would be the case."
            O "Before you woke up, Cecilia and I found a key behind the clock downstairs."
            O leering2 "It turned out to be the key for the furnished bedroom on this floor."
            Y thinking "You mean the little girl's bedroom? Why would that be locked up?"
            O thinking "Your guess is as good as mine..."
            O default "Anyway, considering the layout of the second floor, it's very likely that a large portion of the first floor is blocked off."
            scene cg floordiagram:
                xalign 0.5 yalign 0.5 zoom 1.2 matrixcolor BrightnessMatrix(-0.75)
                easein 3.0 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
            with dissolvemed
            $ persistent.unlock_cg_floordiagram = True
            $ show_side_oriana = True
            O "The last of the locked doors are in the [t_clue]foyer[t_cluee] and the [t_clue]kitchen[t_cluee]."
            $ fadein_sideimage = False
            O blink "And based on their directions, I think they lead to the same room."
            O "It's probably a living room, or some space that has more doors connected to it."
            Y surprised "And you think if we gain access to the rest of the first floor, we might find something interesting?"
            O blink "Exactly. It may not be a way out, but it'll be something the culprit [t_clue]didn't want us to find[t_cluee]."
            $ fadein_sideimage = True
            $ show_side_oriana = False
            scene bg black with dissolvemed
            scene bg hallwayend
            show oriana thinking at mycenter
            with dissolvemed
            O "That said, if they {i}really{/i} didn't want us to go in there, they probably wouldn't hide the key anywhere we could find it..."
            O irritated "The key might also just be in the culprit's possession... And they might in fact be hiding in that room, watching us..."
            Y sad "This isn't gonna be easy, huh...?"
            O thinking "...I think...I'll search around here a little longer. You can stay and help if you want, but..."
            I "...She looks a little worn out. I should give her some space."
            Y blink "Nah, I'll go investigate the first floor now. Who knows, I might find that key. Or a clue to that key."
            O default "All right."
            O happy "...Thank you, [name_player]."
            stop music fadeout 3.0
            play ctc_sfx sfx_steps
            scene bg black with fade
            scene bg foyer with fade
            pause 2.0
            I "....."
            I "...That door in the middle... Between the kitchen and bathroom..."
            scene bg foyer:
                zoom 1.5 xalign 0.25 yalign 1.0
            with dissolve
            play ctc_sfx sfx_doorrattle
            with shakeshort
            Y leering "....." with vpunch
            I "Yep, just like Oriana said, this door is locked, but a key might open it..."
            scene bg foyer
            with dissolve
            I "Where am I gonna find a tiny key, though? Ugh, I better check everything carefully from now on."
            Y worried "*sigh* ...Well... No point standing here and staring at it."
        "\"If it's to preserve life, we should kill.\"":

            $ show_choicegrand = False
            $ d1a1_order_flag = "B"
            stop music
            stop loop_sfx
            scene bg black
            show oriana shadow at mycenter
            with custom_flashbulb()
            pause 0.5
            show bg hallwayend with dissolve
            Y sad "...I think...killing someone in self-defence is fine. ...Isn't it?"
            O "......."
            Y panicked "I-I mean, we're in a pretty dire situation right now. One of us could die. Maybe even all of us."
            $ fadein_sideimage = False
            Y sad "In that case, wouldn't it be better to save as many lives as possi--"
            $ fadein_sideimage = True
            O irritated "And how exactly do we decide which of those lives are saved?" with shakeonce
            Y surprised "Th-that's..."
            O leering "I imagine {i}you{/i} want to get out of here alive, right?"
            Y sad "Well, I--" with shakeonce
            O "So which one of us should die here? Me or Cecilia?"
            Y afraid "I... You can't just..." with shakeonce
            O shouting "Well?! What is your decision, [name_player]?!" with shakeonce
            Y scream "I DON'T KNOW!!" with shakeshort
            play ctc_sfx sfx_deskslam
            window auto hide None
            $ _last_say_who = 'O'
            show oriana injured at mycenter with custom_flashquick()
            with shakeshort
            pause 1.5
            play loop_sfx sfx_heartbeat
            O "{cps=6}.....{/cps}"
            Y afraid2 "...O-Oriana...?"
            O irritated "....."
            O "...If you don't know..."
            stop loop_sfx
            play ctc_sfx "<silence 1.0>"
            show bg black
            O shadow "Then you're [t_clue]useless[t_cluee]..."
            Y afraid "...Huh? What does that--"
            $ _last_say_who = 'O'
            show oriana dejected
            pause 0.1
            show bg hallwayend
            with dissolve
            O "Leave me now. Please."
            Y shocked "....."
            O "....."
            O irritated "I... I'm sorry. I'm not handling this situation very well, clearly."
            O "Just give me some time alone. I want to look around these rooms a bit more anyway."
            Y sad "....."
            $ fadein_sideimage = False
            Y "Alright. I'm sorry I upset you."
            $ fadein_sideimage = True
            O shadow "......."
            play ctc_sfx sfx_steps
            scene bg black with fade
            scene bg foyer with fade
            pause 2.0
            I "...I probably could have handled that a lot better..."
            I "Oriana... Despite her attitude, she's probably the most scared out of all of us..."
            I "....."
            I "...\"Useless\", huh...?"
            Y shadow "....."
            I "I hope...I can help her get out of here alive."
            I "....."
        "\"Some people deserve to die.\"":

            $ show_choicegrand = False
            $ d1a1_order_flag = "C"
            stop music
            stop loop_sfx
            scene bg black
            show oriana shadow at mycenter
            with custom_flashbulb()
            pause 0.5
            show bg hallwayend with dissolve
            Y blink "...I mean... In our case, there's an exception."
            $ fadein_sideimage = False
            Y default "We could kill the culprit."
            $ fadein_sideimage = True
            O surprised "...!" with shakeonce
            Y leering "I mean, whoever this person is, they kidnapped us, trapped us in this creepy house..."
            $ fadein_sideimage = False
            Y thinking "...forced us into this kill-or-be-killed situation, and for what? Probably a good laugh."
            Y angry "Someone like that...won't be missed by anyone."
            $ fadein_sideimage = True
            O "....."
            O "The person...who brought us to this place..."
            Y surprised "...? Oriana?"
            O thinking "I... N-no, it's nothing."
            O "I...think I agree with you."
            O irritated "The person who's responsible for putting us in this situation..."
            play loop_sfx sfx_heartbeat fadein 1.0
            show bg black
            show oriana shadow at mycenter
            with dissolve
            O "...A horrible little demon...{w=0.5}who derives pleasure in causing chaos and misery..."
            O "...An...unforgivable..." with shakeonce
            I "....."
            I "...What is this...?" with hpunch
            I "I feel like...something's going on inside Oriana's head that I can't even begin to imagine..."
            Y shouting "Oriana!" with shakeshort
            stop loop_sfx
            show bg hallwayend
            show oriana panicked at hop
            O "Ah! Wh-what? What is it?"
            Y sad "I'm not saying we should actually do it. Like you said, the culprit could be dangerous."
            $ fadein_sideimage = False
            Y default "And even if we could take 'em... \"No one deserves to end someone's life\", right?"
            $ fadein_sideimage = True
            O thinking "\"Deserves\"..."
            O blink "....."
            O "I'm sorry, [name_player], but can you leave me alone for a while?"
            O default "There are some places I would like to give a second glance at."
            Y surprised "Huh? O-okay."
            $ fadein_sideimage = False
            Y "Then...I'll see you later?"
            $ fadein_sideimage = True
            O blink "Yes. Thank you, [name_player]."
            O shadow "Thank you very much..."
            play ctc_sfx sfx_steps
            scene bg black with fade
            scene bg foyer with fade
            pause 2.0
            Y shadow "......."
            I "I have a very strong feeling that later tonight..."
            play ctc_sfx sfx_heartbeat_single
            I "{color=#ff0000}Something{/color}...is going to happen..." with shakeonce
            I "Did I...make a bad decision here?"
            I "It really felt like Oriana turned into someone else for a moment there..."
            Y worried "*sigh* ...Well, I can't take back what I said. I'll just have faith in her..." with hpunch

    $ d1a1_checked_upstairs = True
    return




label d1a2:
    call save_file_name_update (1, "d1a2")
    scene bg foyer
    if d1a1_checked_kitchen:
        play ctc_sfx sfx_dooropen
        play sound ["<silence 0.5>", sfx_steps]
        pause 2.0
        $ _last_say_who = "C"
        show cecilia surprised at mycenter with dissolve
        C "Oh, [name_player]! You're still here?"
        Y surprised "Cecilia? Y-yeah, I was about to--"
    else:
        play ctc_sfx sfx_dooropen
        pause 0.5
        $ _last_say_who = "C"
        play sound sfx_whooshlow
        show cecilia surprised at mycenter_zoomstill
        window auto show None
        C "Ahh!" with shakeshort
        show cecilia surprised at mycenter_return
        Y panicked "Woah!" with shakeshort
        I "I almost ran right into her!" with hpunch
        hide cecilia
        show cecilia default at mycenter
        C "Oh, [name_player]! Sorry, did I scare you?"
        Y surprised "I-I'm fine. How about you--"

    play ctc_sfx sfx_emotehappy
    show cecilia happy at hop
    C "Aha! I knew it! [name_player], look at the clock!"
    Y thinking "Huh?"
    I "....."
    C default "See? It's a little past 8!"
    C smug "We heard a loud chime when it was 6 o'clock, but did we hear any chimes for 7 or 8?"
    Y afraid "....." with shakeonce
    C sweatdrop "Uh... [name_player]? Are you listening? The clock might be magi--"
    Y "Forget about the clock, Cecilia."
    C surprised "Huh?"
    Y "Look at the door."

    scene bg black with dissolve
    scene bg frontdoor with dissolvemed
    $ persistent.unlock_bg_frontdoor = True
    pause 2.0
    $ show_side_cecilia = True
    C thinking "Hmm? What about the door?"
    $ fadein_sideimage = False
    C surprised "It still has...the... Huh?"
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    show bg frontdoor:
        zoom 1.2 yalign 1.0
        easein 6.0 zoom 1.3 yalign 0.0
    with dissolve
    play ctc_sfx sfx_heartbeat_single
    I "{cps=18}\"This door will not open...\"{/cps}"
    play ctc_sfx sfx_heartbeat_single
    I "{cps=18}\"...until one of you...DIES...\"{/cps}"
    play ctc_sfx sfx_heartbeat_single
    I "{cps=12}\"...YOU HAVE {color=#ff0000}20 HOURS{/color}...\"{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide None
    scene bg black with custom_flashquickred()
    show text "{size=+30}{color=#ff0000}20 HOURS{/color}{/size}"
    pause 2.0
    hide text with dissolveslow
    pause 0.5
    play music bgm_criminal
    $ show_music_info_timer = music_info_pop_out_time()
    $ _last_say_who = 'C'
    scene bg foyer
    show cecilia surprised at mycenter
    with dissolvemed
    C "....."
    Y afraid "...That... That third line wasn't always there, right?"
    C "...Not that I'm aware of... It's definitely the first time {i}I'm{/i} seeing it."
    Y troubled "...What is this...?"
    $ fadein_sideimage = False
    Y scream "Why are they doing this to us?!" with shakeshort
    $ fadein_sideimage = True
    C blink "..... ...I know..."
    play ctc_sfx sfx_emotehappy
    show cecilia overjoyed at doublehop
    C "Isn't it WONDERFUL?!"
    Y afraid "Wait, WHAT?!" with shakeshort
    C "Now we know this death game is for real!"
    C "If we don't kill someone real soon, we're all gonna be in big, biiig trouble!"
    Y pained "Have you lost your mind?!" with shakeshort
    C blush "Anyway, [name_player]! Considering the time, let's have dinner now!"
    Y shocked "D-dinner...? How can you be thinking about dinner when..."
    C blink "[name_player], relax. It's not like the door is saying we have 20 {i}minutes{/i} or something."
    C default "Let's all gather in the dining room for dinner, and talk about what our plan is going forward."
    Y surprised "...!" with shakeonce
    I "She's...got a good point... We really need to talk about what that message update could mean..."
    C surprised "Is...Oriana still upstairs? Boy, she's a hard worker, huh?"
    C thinking "Or maybe... She's sleeping in one of the bedrooms?"
    if d1a1_checked_upstairs:
        Y sad "I...don't think so..."
    else:
        Y thinking "I wouldn't be able to tell you. I haven't checked upstairs yet."
    C happy "I'll go fetch her! You go ahead to the dining room and wait for us!"
    stop music fadeout 3.0
    play sound sfx_steps
    scene bg foyer with dissolve
    pause 3.0
    I "....."
    I "...I guess I'll have to check the [t_clue]rest of the house[t_cluee] another time."
    I "What a depressing note to end an investigation on. ...Ugh..."
    I "Even though I woke up only a couple hours ago, I feel so drained..." with hpunch


    $ day1_dinner_skipped = False
    if day1_loop_count >= 2:
        I ".....{w=0.5}{nw}"
        play ctc_sfx "<silence 1.0>"
        show bg foyer:
            blur 20.0
            linear 3.0 blur 0.0
        extend " Urgh..." with shakeonce
        I "Why do I feel like I've been running around in circles...?"
        I "...Maybe I should pass on dinner and get some rest in one of the bedrooms upstairs?{nw}"

        menu:
            extend ""
            "{color=#cccc00}Skip the discussion and dinner{/color}":
                call save_file_name_update (1, "d1a2_part2")
                I "...Yeah, I definitely don't feel well."
                I "I should go upstairs and tell the others I'll be skipping dinner."
                scene bg black with dissolvemed
                I "I told Cecilia and Oriana about my condition, and they seemed sympathetic enough."
                I "They said to go ahead and use the master bedroom, which definitely has the best bed in the house."
                I "...I wonder if those two will be all right without me...? Maybe it's because of that sudden time limit but..."
                I "....I can't shake this feeling that [t_clue]something will happen[t_cluee] tonight..."
                I "Ugh, but I'm so tired..." with hpunch
                I "I guess...I won't be very helpful in this state... Let's get some sleep for now..."
                I "....."
                I ".........."
                play ctc_sfx "<silence 1.0>"
                I "{cps=6}...............{/cps}"
                play ctc_sfx "<silence 1.0>"
                scene bg black
                $ day1_dinner_skipped = True
                pause 2.0
                jump d1a3
            "Don't skip":
                I "...No, it wouldn't be fair to just dip out like this."
                I "That sudden time limit... I should talk with the others about it."
    Y worried "Okay, off to the dining room..."
    play ctc_sfx sfx_steps
    scene bg black with fade
    play sound sfx_dooropen
    scene bg diningroom withchair with fade
    pause 2.0
    I "....."
    if d1a1_checked_kitchen:
        I "...She still hasn't cleaned up that chair..."
        Y annoyed "Acted all responsible about it too..."
        I "...Let's see how she planned on handling dinner."
        play ctc_sfx sfx_steps
        scene bg black with fade
        pause 2.0
        I "Well, at least it looks like she got the canned food open."
        I "...Wait..."
        play ctc_sfx sfx_heartbeat_single
        I "...Did... Did she just [t_clue]stab them repeatedly[t_cluee] with a knife...?" with shakeonce
    else:
        $ persistent.unlock_bg_diningroom_withchair = True
        I "...What is that? Something wooden got smashed up..."
        play ctc_sfx sfx_emotequestion
        I "...A...broken chair? What happened here...?"
        Y blink "....."
        I "Never mind this, let's see what the food situation is."
        I "I guess the kitchen is further back?"
        play ctc_sfx sfx_steps
        scene bg black with fade
        pause 2.0
        I "Oh, so this is what the kitchen looks like."
        I "...There's cut-up cans of food on the counter... Is that our dinner?"
        I "...Uh..."
        play ctc_sfx sfx_heartbeat_single
        I "...Why does it look like they've been [t_clue]stabbed open[t_cluee]...?" with shakeonce

    play ctc_sfx "<silence 1.0>"
    X "[name_player]."
    play ctc_sfx "sound/ctc_sound.ogg"
    Y afraid "WAH!!{w=0.5}{nw}" with shakeshort
    play ctc_sfx sfx_whooshlow
    show bg kitchen
    $ persistent.unlock_bg_kitchen = True
    show oriana surprised at mycenter, hop
    with custom_flashquick()
    O "AAHH!!" with shakeonce
    Y "O-Oriana?! You surprised me!" with shakeonce
    O shouting "Right back at you! What do you think you're doing?!" with shakeonce
    Y sad "I was just...looking at the food..."
    $ fadein_sideimage = False
    Y surprised "...Huh? Where's Cecilia?"
    $ fadein_sideimage = True
    O confused "Hmm? I thought she was right behind me..."
    O disappointed "I guess something upstairs must've caught her attention."
    Y thinking "Oh."
    O thinking "....."
    Y sad "....."
    O "...So I saw the door."
    Y thinking "...Yeah..."
    O leering2 "...It...wasn't you, right?"
    Y panicked "O-of course not!" with shakeonce
    O confused "I figured as much. Then that means..."
    I "...?"
    O disappointed "Also, care to explain that broken pile of wood in the other room?"
    Y surprised "Oh yeah, the broken chair. Uh..."
    O "That was Cecilia's doing, wasn't it?"
    if d1a1_checked_kitchen:
        Y worried "Yeah, good guess."
        O irritated "There was no guesswork needed. Ugh, that little imp..."
    else:
        Y sad "I don't know... Probably?"
    O leering "And...is THAT supposed to be the dinner Cecilia wants us to eat?" with hpunch
    Y thinking "I mean, it all smells okay. I guess she couldn't find a can opener."
    O irritated2 "Unbelievable..."
    O sideeye "I'll go put these on proper plates. In the meantime, can you clean up that mess in the other room?"
    Y surprised "O-okay, sure."
    scene bg black with dissolvemed
    I "Guess it's up to me to clean this up after all..."
    I "Where the heck did Cecilia run off to...?"
    scene bg kitchen
    show oriana blink at mycenter
    with dissolvemed
    Y default "I finished cleaning up the chair."
    O default "Good work. I'm just about done here too."
    Y "....."
    O blink "......."
    Y sad "........." with hpunch
    if d1a1_checked_upstairs:
        $ fadein_sideimage = False
        Y surprised "O-oh yeah, did you find anything upstairs after I left?"
        $ fadein_sideimage = True
        O default "Yes, actually. I managed to find this in the pocket of one of the coats in the wardrobe."
        play ctc_sfx sfx_emotequestion
        Y panicked "...! I-is that a [t_clue]key[t_cluee]?!" with shakeonce
        O thinking "Most likely, but...I don't know what it's for. It doesn't fit any of the remaining locked doors."
        I "A hidden key... I wonder what this will do for us...?"
        if d1a1_order_flag == "A":
            Y thinking "...Wait, you mentioned you used a key to open one of the rooms upstairs, right? Where's {i}that{/i} key?"
            O confused "Um... Oh, here it is."
            Y default "....."
            $ fadein_sideimage = False
            Y surprised "...It's different. This new key is smaller than the first one."
            $ fadein_sideimage = True
            O surprised "Good point... I wonder if this means [t_clue]this key isn't for a door[t_cluee]..."
            Y annoyed "But if it's not for a door, then what {i}could{/i} it be for?"
        else:
            Y thinking "...Wait, \"remaining\"? So you were able to unlock some of the doors?"
            O stunned "R-right, that was before you woke up."
            O thinking "There was a key behind the clock by the entrance, and--"
    else:
        I "...This is...awkward..."
        Y surprised "S-so, did you find anything interesting upstairs?"
        O default "...Interesting?"
        Y confused "Like, any useful clues? Or a way to escape?" with hpunch
        O blink "...No."
        Y worried "I-I see..."
        I "She's really wary of me. But I guess we {i}are{/i} strangers to each other..."

    play ctc_sfx sfx_dooropenloud
    show bg black
    hide oriana
    with custom_flash()
    $ show_side_cecilia = True
    play sound sfx_emotehappy
    C happy "I'm baaaaack~ You guys didn't start without me, right?" with shakeshort
    $ show_side_cecilia = False
    I "Agh, another scare... My poor heart..." with shakeonce
    play ctc_sfx sfx_steps
    play sound ["<silence 0.2>", sfx_steps_heels]
    scene bg black
    with fade
    $ _last_say_who = 'C'
    scene bg diningroom
    show cecilia overjoyed at mycenter
    with fade
    $ persistent.unlock_bg_diningroom = True
    C "Wowww, everything's all tidied up too!"
    $ _last_say_who = 'O'
    show cecilia overjoyed at mycenter_to_myright
    show oriana leering2 at myleft with dissolve
    O "Where have you been? And...what are you holding?"
    if d1a1_upstairs_clue6:
        Y thinking "It looks like..."
        play ctc_sfx sfx_emotequestion
        $ fadein_sideimage = False
        Y panicked "Wait, isn't that the [t_clue]gold vase[t_cluee] in the upstairs hallway?!" with shakeonce
        $ fadein_sideimage = True
    else:
        Y surprised "It looks like...a [t_clue]vase made out of gold[t_cluee]...?!"
    show cecilia blush at myright
    C "Oh don't mind this! I'm just borrowing it for a bit~"
    C smug "It looked pretty heavy and good for smashing windows, so I gave it a shot, whipping this at all the ones upstairs."
    if d1a1_checked_kitchen:
        Y worried2 "You really went rampaging off-screen again..."
    else:
        Y panicked "Y-you were...what?!" with shakeonce
    O confused "And? Any luck?"
    C thinking "Nope! Not a single one would break! It's super weird!"
    Y thinking "Um, Oriana? She said she was upstairs, trying to smash windows. Don't you have any issues with that?"
    O disappointed "Why would I? It's not like this is {i}my{/i} house."
    Y worried "That's...not what I meant..."
    C happy "Relax [name_player], it's only throwing things! I grew up playing softball, I'll have you know~"
    show cecilia grin at doublehop
    C "If you put up your hoodie, I could whip this thing and knock it clean off without even grazing your hair~ [u_music_note]"
    play ctc_sfx sfx_emotesigh
    Y worried2 "Please don't." with hpunch
    O sideeyeblink "Just put the vase down and sit. We have a lot to discuss."
    $ _last_say_who = None
    play music bgm_discussion
    scene bg black with dissolvemed
    scene bg diningroom with dissolvemed
    show oriana blink at myleft
    show cecilia at myright
    with dissolve
    $ show_music_info_timer = music_info_pop_out_time()
    O "Still, the fact that not a single window broke..."
    O thinking "I suppose that means this house has been modified to keep people trapped inside."
    O leering "Which can only mean that this is a [t_clue]premeditated kidnapping[t_cluee]."
    Y leering "You mean the culprit planned ahead to trap the three of us in here?"
    O blink "...There's a good chance that's the case, yes.{nw}"

    menu:
        extend ""
        "\"How did they catch us?\"":
            Y thinking "A carefully planned kidnapping..."
            $ fadein_sideimage = False
            Y default "I still have no idea, but do either of you remember how you got kidnapped?"
            $ fadein_sideimage = True
            C thinking "Hmmmmmmmmmmm..."
            C sad "Nope, can't say I do."
            C thinking "I was out for a walk just before sunset, and next thing I know, I'm waking up on the floor here."
            if d1a1_checked_upstairs:
                I "That's pretty much the same story Oriana told me earlier..."
                O thinking "....."
            else:
                O blink "It was more or less the same for me."
            C default "Since the clock was around 5 when we woke up, I guess we got brought to this house right away?"
            C surprised "Or maybe a day passed? Or maybe just 12 hours? We still can't really tell if it's morning or night with that fog..."
            C "....."
            C sweatdrop "Sorry, [name_player], looks like that's pretty much all we can say."
            I "...No, that can't be all. Let's try a more specific question...{nw}"
            menu:
                extend ""
                "\"Were you alone?\"":
                    Y leering "Were you taking a walk by yourself? And there weren't any other people nearby?"
                "\"Where were you?\"":
                    Y leering "Where were you taking your walk? Were you anywhere near this house?"
            C thinking "Well..."
            O blink "I'm sorry, [name_player], but Cecilia and I talked about that before you woke up."
            O confused "And all we remember is that we were both [t_clue]outside in the early evening[t_cluee] when we were kidnapped."
            C sad "Yeah, the last day's just a big blur in my head."
            C thinking "I know it was a day off, but I honestly can't remember what I was doing the whole day."
            C "Was I in the city? On my way home?"
            C sweatdrop "I guess whatever the culprit used to put us to sleep did a number on my head."
            Y sad "...I see."
            I "....."
            O blink "I'm still wondering how they managed to put us to sleep so quickly and without our noticing."
            O thinking "For example, if they knocked us out with blunt force, our heads would be aching, but they're not."
            O "If they used tranquilizer darts, we would feel some numbness wherever they hit."
            O "Or if they had used some type of sleep-inducing gas, there's no way we would forget something that sudden and unusual."
            C wink "You've certainly thought this through~ [u_music_note]"
            O irritated "...And yet here we are, without any injury or memory of how we came to be here."
            I "Well, in my case, I just don't remember anything at all..."
            O default "Anyways, it's safe to say that the culprit put each of us to sleep using the same mysterious method."
        "\"Why are they doing this?\"":
            Y thinking "Trapping us in this modified house, writing...THAT on the door..."
            $ fadein_sideimage = False
            Y "They clearly want us to turn on each other, but why? What do they get from making us do this?"
            $ fadein_sideimage = True
            play ctc_sfx sfx_emotequestion
            C surprised "Huh? You don't know about [t_clue]death games[t_cluee]?"
            Y panicked "D-death...{i}games{/i}...?"
            C grin "You know, like the battle royale genre? Stories where people compete for survival!"
            C blink "Sometimes they do it for a big prize, and other times they're just forced into it at the whims of a [t_clue]mastermind[t_cluee]."
            C smug "Usually the contestants try to kill each other, but other times, they play games where losing means death."
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "It's a very popular form of [t_clue]entertainment[t_cluee] these days!"
            Y surprised "Entertainment...?"
            $ fadein_sideimage = False
            Y angry "This is all just a [t_clue]GAME[t_cluee] to someone?!" with shakeonce
            $ fadein_sideimage = True
            O blink "...I don't believe this situation is for someone's entertainment."
            C surprised "Oh? And why's that?"
            O default "Because there's [t_clue]no electricity[t_cluee] running through this house."
            Y worried "...What? What does that have to do with--"
            C smug "Ahaaa, I see what you're saying~"
            Y panicked "Wh-what is it? What is she saying?" with hpunch
            C default "Well, there's no power, right? That means there's no way for any [t_clue]surveillance cameras[t_cluee] to work."
            C thinking "...Not that we found any from looking around."
            O thinking "Without cameras, there are no means to watch or record us trying to kill each other."
            C blink "Which means the only way the culprit could be enjoying this...[t_clue]killing game[t_cluee] is if they were watching us directly."
            C smile "...Perhaps...in plain sight?"
            O irritated "...!" with shakeonce

    I "The culprit...{nw}"

    menu:
        extend ""
        "\"Is this the culprit's house?\"":
            Y default "If this house was modified, that means the culprit is the owner of this house, right?"
            C thinking "Not necessarily. I mean, this place looks like a typical family's home."
            if d1a1_checked_upstairs:
                C default "Our culprit could be someone else in that family.{nw}"
                menu:
                    extend ""
                    "\"You might be right...\"":
                        Y sad "Yeah, I guess that possibility exists..."
                        O leering2 "[name_player], have you seriously forgotten?"
                        O "We already know that any family living here couldn't have been more than [t_clue]two people[t_cluee], one of them being a [t_clue]child[t_cluee]."
                        Y surprised "Ah... R-right..." with hpunch
                    "\"No, that can't be it.\"":
                        Y leering "No, it couldn't have been anyone else but the owner."
                        $ fadein_sideimage = False
                        Y blink "Considering what Oriana and I found upstairs, only the owner and a small child could have been living here."
                        $ fadein_sideimage = True
                        O blink "Good, you remembered that."
            else:
                C default "Our culprit could be someone else in that family."
                I "I guess that makes sense, considering what Cecilia and I found here..."
                O sideeyeblink "Sorry, but you're wrong, Cecilia."
                O sideeye "The rooms upstairs make it clear that only [t_clue]one adult[t_cluee] and [t_clue]one child[t_cluee] were living here."
                Y surprised "R-really...?"
            C surprised "A child...?"
            C thinking "...So...what?"
            C smile "You think that a child couldn't possibly be our culprit? I dunno... Kids can be crafty~"
            O confused "But we're talking about who modified the house."
            O leering2 "It's impossible for a child to replace the windows with unbreakable glass, both physically and financially."
            C blink "..... Alright, can't argue with that."
            C default "So that narrows it down to just one other person."
            I "The owner of this house..."
            O blink "...I'm not saying that either."
            C surprised "Oh? Then who do {i}you{/i} think the culprit is?"
            O "....."
            O irritated "......."
            C smug "Oh detectiiiiive~ [u_music_note] You have the scowl of someone who really really wants to say somethiiiiing~ [u_music_note]"
            O "...No."
            O thinking "I'm sorry, I don't know who it could be."
            C grin "Pft..."
        "\"Who is our culprit?\"":
            Y thinking "Who do you think it is? The person that brought us here?"
            C blink "....."
            O thinking "....."
            Y surprised "...Uh, guys?"
            C smile "...Oriana was looking for clues regarding that, right?"
            O sideeyeblink "Yes. My current theory is that there are at least two people involved."
            play ctc_sfx sfx_emotequestion
            O sideeye "One culprit...and an [t_clue]accomplice[t_cluee]."
            C surprised "An accomplice..."
            C smug "...I see! That {i}would{/i} make the most sense, considering how they caught three people all at once."
            Y thinking "...?"
            C default "But did you find any clues about the IDENTITIES of this evil duo?"
            O irritated ".....{w=1.0} ...No."
            C smug "Really! Even though you're SOOO sure that there are two people involved?{nw}"

            menu:
                extend ""
                "Say something":
                    Y panicked "H-hang on, there's no need to taunt her like that. We're all on the same team here."
                    C sad "Aww, I wasn't taunting her! Do you really think that little of me?"
                    O thinking "...The same team..."
                "Say nothing":
                    Y sad "....."
                    O leering "You already mentioned how the three of us were brought here all at once."
                    O "Anyone would have trouble doing something like that alone."
                    C blink "..... Hmph. I guess I did say that."
            C smile "But come to think of it, [name_player], {i}you{/i} posed the initial question. So let's hear YOUR thoughts!"
            C default "Who do {i}you{/i} think the culprit could be?"
            Y panicked "...Huh? M-me?"
            C happy "Yeah, show us your detective skills!{nw}"

            menu:
                extend ""
                "Admit you have no idea":
                    Y worried "...Sorry, I got nothing."
                    show cecilia pout at doublehop
                    C "You're not even gonna try? Booooo."
                    O blink "That's probably for the best. It won't do us any good to jump to a wrong conclusion."
                "Try making a deduction":
                    I "...I have no idea who it could be but..."
                    Y thinking "...I guess something I noticed is there's a lot of dust around here. On top of other signs that no one's been living here for a while."
                    $ fadein_sideimage = False
                    Y blink "That means there's a chance that the culprit just happened to find this house, and modified it for trapping people."
                    Y worried "In other words, I don't think anything we find in this house is guaranteed to be related to the culprit's identity..."
                    $ fadein_sideimage = True
                    C sweatdrop "Boy, that's a bleak conclusion..."
                    O blink "[name_player] makes a good point, though."
                    O thinking "If the culprit simply repurposed this house, it'd be hard to believe they would leave any clues that point to their identity."
                    C thinking "So no matter what we learn about the people who lived here, it won't do us any good?"

    Y sad "....."
    C default "....."
    O thinking "....."
    C blink "...Alright, so I guess we don't have enough clues to identify our mystery culprit."
    I "Then let's try a different angle...{nw}"


    menu:
        extend ""
        "\"Why were we the victims?\"":
            Y thinking "Why did they kidnap us? Does the culprit have something against any of us?"
            O blink "Who can say...?"
            C smug "Hmmm? What, do you believe there isn't a single person out there holding a grudge against you?"
            O leering "...You're one to talk. I'm sure your carefree tactlessness rubbed some people the wrong way."
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "Ahaha, I'm totally sure it has!"
            Y shadow "....."
            $ renpy.music.set_volume(0.5, 2, channel="music")
            show bg black with dissolve
            I "I don't know anything about either of these two... Heck, I don't know anything about myself..."
            I "I wonder... Have I done anything horrible enough for someone to want me dead?"
            I "...But if that's the case, why not just kill me directly? Why put me to sleep and bring me here instead?" with shakeonce
            I "Something's not adding up..."
            $ renpy.music.set_volume(1.0, 2, channel="music")
            show bg diningroom with dissolve
            Y sad "....." with hpunch
            C default "Don't overthink it, [name_player]. It's also possible that anyone would have been fine."
            C "And we simply happened to be the first couple of targets they spotted along the street."
            O irritated "....."
            C blink "But I suppose the fact that they targeted exclusively girls is pretty telling."
            C smile "This whole situation might just be the culprit acting out some weird fetish."
            O leering "There's that tactlessness again..."
        "\"Why three victims?\"":
            Y blink "I wonder why there's three of us...?"
            C surprised "Hmm? What do you mean?"
            C thinking "It would be pretty hard to have a death game with only one person. And with two, well, it would just be a duel to the--"
            Y annoyed "N-no, I mean why is it JUST three of us?" with shakeonce
            $ fadein_sideimage = False
            Y default "I mean, the writing on the door says \"one of you\", without specifying the number of people."
            Y "So maybe...there could be a fourth or fifth person trapped in here with us."
            $ fadein_sideimage = True
            C surprised "....."
            play ctc_sfx sfx_emotehappy
            show cecilia overjoyed at hop
            C "That's a good catch, [name_player]!"
            O confused "I hate to rain on your parade, but do you honestly believe there's a fourth or fifth person here that we don't know about?"
            Y thinking "Well, how about before I woke up?"
            O leering2 "No. It has always been just us three."
            C default "Well, us three, and the culprit."
            C thinking "But I do see where you're coming from, [name_player]."
            Y surprised "Huh?"
            C "If the goal of the culprit was to have a group of girls go insane and try to murder each other..."
            C smug "It certainly would be more interesting if there were more of us."
            O irritated "....." with shakeonce
            Y panicked "Th-that's not--"

    stop music fadeout 3.0
    C blink "On that note actually, something's been bothering me for a while..."
    Y default "And what's that?"
    C default "The fact that this all ends when just one of us dies."
    C thinking "Why only one of us? Why isn't it a...last-one-standing-gets-to-leave kind of game?"
    Y worried "What are you..." with hpunch
    O leering2 "Isn't it obvious? There's something that can only happen with that rule and exactly three people."
    O "Two of us could collude and kill the third person in order to escape."
    Y afraid "...! ...That's--" with shakeonce
    if d1a1_checked_kitchen:
        I "So Oriana realized that too...!"
        C smile "Something on your mind, [name_player]?"
        Y sad "N-no. I-I was just..."

    O "Don't tell me you didn't realize that until now, [name_player]."
    Y shouting "I-I mean, that's crazy!" with shakeonce
    show cecilia pout at doublehop
    C "Yeah, it's crazy! Like, where's the fun in that?"
    C "At least with a free-for-all, everyone has a fair shot at winning!"
    O irritated "Ngh..." with shakeonce
    Y shocked "Th-that's not what I..."
    C blink "But if only one of us has to die, this can all end preeetty quickly."
    if d1a1_checked_kitchen:
        C smug "[name_player] and I even found some potential murder weapons, remember?"
        play ctc_sfx sfx_emotehappy
        show cecilia wink at hop
        C "I'm still particularly fond of the [t_clue]knife[t_cluee]. [u_heart]"
    else:
        C wink "How 'bout it, [name_player]? Care to...take a \"stab\" at it?"
    Y troubled "{cps=6}.....{/cps}{nw}"
    play ctc_sfx sfx_heartbeat_single
    $ fadein_sideimage = False
    extend " ...Cecilia, please..." with hpunch
    $ fadein_sideimage = True
    play loop_sfx sfx_heartbeat
    hide oriana
    $ _last_say_who = "C"
    show cecilia surprised at mycenter
    show bg diningroom dark at wobble
    with custom_flashquickred()
    $ persistent.unlock_bg_diningroom_dark = True
    C "But sheesh, now that we got that out in the open, doesn't it feel way more tense here?"
    show cecilia sobbing:
        zoom 1.2 ypos 1.2 xalign 0.30
        easein 5.0 xalign 0.25
    with hpunch
    C "We can't split up anymore! Two of us could rendezvous and agree to kill the loner!"
    show cecilia grin at myright:
        zoom 1.5 ypos 1.4 xalign 0.75
        easein 5.0 xalign 0.80
    with shakeonce
    C "Heck, there doesn't even need to be collusion! Any of us could just straight up murder someone right now!"
    show cecilia happy at mycenter, shudder:
        zoom 2.5 ypos 2.1
        easein 5.0 zoom 3.5 ypos 2.8
    with shakeshort
    C "After all, only ONE of us needs to die,{w=0.5} so whoever doesn't get killed only stands to benefit from--{w=1.5}{nw}"
    window auto hide None
    play ctc_sfx sfx_deskslam
    stop loop_sfx
    scene bg diningroom
    show oriana shouting at myleft:
        ypos 1.15 zoom 1.2
        linear 0.2 ypos 1.05 zoom 1.0
    show cecilia surprised at myright
    with custom_flashquick()
    window auto show None
    O "ENOUGH!!" with shakelong
    C "....."
    I "....."
    O irritated "...You..."
    O irritated "...Even if you're only saying the truth..."
    O shadow "There are some things you just don't say, Cecilia..."
    C default "....."
    window auto hide
    pause 0.5
    show cecilia smile
    pause 0.5
    window auto show
    C "......."
    C blink "You're right. That wasn't fair."
    C default "There's enough stress as it is, right, [name_player]?"
    Y shocked "...Y-yeah..."
    O "....."
    play music bgm_tension
    $ show_music_info_timer = music_info_pop_out_time()
    C happy "Anyways~ Whew, we've been talking for a while! What do you guys think, have we covered everything?"
    I "...I think...I'm afraid to ask anything more..." with hpunch
    C thinking "We've been talking a lot about our culprit for the most part, but let's be real here."
    C default "Does it really matter who the culprit is?"
    C blink "There are no other exits besides that door, and now we have a 20 hour clock literally counting down to our doom."
    C smile "Why don't we stop wasting time and cut to the chase?"
    O afraid "...!" with shakeonce
    C "...[name_player]?"
    Y afraid "Wh-what?" with shakeonce
    C sad "Weren't you listening? I said let's cut to the chase!"
    C grin "Who do you think should [t_clue]die[t_cluee] here?{nw}"

    menu:
        extend ""
        "One of us":
            Y troubled "....."
            $ fadein_sideimage = False
            Y "...It has to be one of us. There's...really no other way..." with shakeonce
            $ fadein_sideimage = True
            C blush "There we go~ I knew you'd be the sensible type, [name_player]!"
            C smug "Alright, now for the important choice. You have three options."
            C blink "Oriana could die..."
            O shadow "....."
            C smile "...{i}I{/i} could die..."
            Y "....."
            C happy "Or of course, [name_player], YOU could die!"
            C grin "It wouldn't be the worst thing, sacrificing yourself to save a pair of fair maidens, don't you think?"
            Y afraid "...Why is it up to me?"
            C surprised "\"Why\"?"
            C thinking "....."
            C default "...Why not? Would you prefer it if the choice wasn't up to you?"
            Y depressed "That's... I-I..." with shakeonce
        "The culprit":
            Y pained "The culprit. If we can just find the culprit, then--" with shakeonce
            C pout "Enough about the culprit, [name_player]. Were you not paying attention?"
            C "We have no clues on who the culprit is or where they could be. And even if we did,{w=0.3}{nw}"
            play ctc_sfx sfx_emoteshout
            extend " IT DOESN'T MATTER." with shakeonce
            O shadow "....."
            C sad "Do you really think we can all stay calm and settled for 20 whole hours?"
            C "Instead of waiting anxiously for the culprit to come and kill us all, or for one of us to panic and kill someone..."
            C smile "...Wouldn't it be merciful to just decide who dies now?"
            Y afraid "That's..." with shakeonce
        "Nobody":

            Y afraid "Nobody needs to die! We... We all need to get out of this alive!" with shakeshort
            C sweatdrop "*sigh* Oh, [name_player]... You're just as stubborn as someone I know..."
            O shadow "....."
            C blink "We're boxed in, [name_player]. There's literally no way to escape."
            C "None of the windows will even crack, and we can't call for help."
            C thinking "Honestly, where's that optimism coming from?"

    stop music fadeout 3.0
    O "...Heh..." with hpunch
    I "...?"
    O "Pft..." with shakeonce
    show bg black with custom_flashquick()
    O laughing "PffhehahaHAHAHAHAHAA~" with shakelong
    Y panicked "O-Oriana?!" with shakeonce
    C surprised "Oh no, she's lost it!" with shakeonce
    show bg diningroom
    show oriana panicked at doublehop
    O "AGH! S-something just brushed along my leg!" with shakeonce
    show cecilia thinking at crouch
    C "Hmm? What's down here..."
    show cecilia surprised at standup
    pause 0.25
    play ctc_sfx sfx_emotehappy
    show cecilia overjoyed at hop
    C "...Oh, a puppy!"
    $ _last_say_who = None
    show dog_raw at mycenter with moveinbottom
    Y panicked "Wha-- WHOA!" with shakeonce
    $ fadein_sideimage = False
    if d1a1_checked_bathroom:
        Y "Wait... You're the dog from earlier!"
    else:
        Y "A... A dog?!"
    $ fadein_sideimage = True
    C default "I think it's a...black poodle? I don't really know dog breeds."
    O "Wh-wha..."
    O "Whawhawhawha..." with shakeonce
    I "Uh oh, Oriana seems flustered. I wonder if she--"
    play ctc_sfx sfx_fallsoft
    hide oriana
    hide dog_raw
    play music bgm_comedy
    $ show_music_info_timer = music_info_pop_out_time()
    $ show_side_oriana = True
    O overjoyed "WHAT IS THIS PRECIOUS CREATUUUURE?! [u_heart]" with shakeshort
    I "{cps=12}...likes...{/cps}{w=1.0}dogs."
    play ctc_sfx sfx_emotehappy
    O sobbing "[u_heart] OHMERGOSH ISSOOOOO FLOOFFYYY~ [u_heart] I could just dig my face in dis FLOOFY LI'L BELLY~ [u_heart]{w=0.5}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend " *SNIFFFFFFF*" with shakeshort
    $ fadein_sideimage = True
    show cecilia sweatdrop at shrink
    play ctc_sfx sfx_emotesigh
    C "You're, uh... You're already doing that."
    Y confused "Uh... Oriana? You're suddenly acting very out of character..."
    $ _last_say_who = 'C'
    show cecilia blush at myright
    show cecilia blush at mycenter with move
    C "Meh, it's fine, isn't it? Might as well let her relieve some stress."
    play ctc_sfx sfx_emotehappy
    O overjoyed "EEEEEEEEEEEEEEE, IT'S GOT THE CUDDIWIEST WITTLE PAW PAAADS~ [u_music_note] Squishy squish squish~" with shakeshort
    C default "Anyways, [name_player], have you seen this dog before?"
    if d1a1_checked_bathroom:
        Y surprised "Y-yeah, when I was searching the bathroom."
        $ fadein_sideimage = False
        Y default "It ran off and disappeared before I could get a good look at it."
    else:
        Y surprised "No, it's my first time seeing it."
        $ fadein_sideimage = False
        Y thinking "But I guess that explains the [t_clue]pet bowl[t_cluee] by the table here."
    O panicked "Ooh, it can stand up! And from a glance below..."
    O laughing "Aha! He's a healthy little baby boy, look at his widdle--{w=1.0}{nw}" with vpunch
    play ctc_sfx sfx_emoteshout
    Y worried2 "*AHEM* Yes, we see it. Th-the...yeah." with shakeshort
    $ fadein_sideimage = True
    play ctc_sfx sfx_emotesigh
    show cecilia sweatdrop at shrink
    C "Ahaha..."
    Y confused "She's...REALLY having fun down there..."
    show cecilia thinking at mycenter
    C "Hmm... I guess that dog's here right now because it's looking for food. The pet bowl is right over there, after all."
    C default "Which means the dog probably [t_clue]lives here[t_cluee].{nw}"

    menu:
        extend ""
        "\"Does it belong to the owner of this house?\"":
            Y thinking "So it belongs to the owner of this house?"
            C thinking "Probably not? A lot of clues indicate no one's lived here for a while."
            Y blink "Right, a dog wouldn't be able to live in a house alone."
            $ fadein_sideimage = False
            Y "....."
            Y surprised "...Wait, but then why would the dog know to come here for food?"
            $ fadein_sideimage = True
            C blink "It probably smelled our dinner, right?"
            Y annoyed "But you had the cans cut open since long before we came in. So why would it wait until now?"
        "\"Does it belong to the culprit?\"":
            Y thinking "Did the culprit bring it here?"
            C smile "That's my best guess, yep."
            C thinking "Who knows, this dog might lead us to our culprit..."
            Y surprised "But isn't that strange...?"
            $ fadein_sideimage = False
            Y "If the culprit was planning on using this house for a crazy death game, why would they leave their dog here?"
            $ fadein_sideimage = True

    C surprised "Ooooh, good point."
    C thinking "...Huh. This dog actually raises a lot of questions."
    C "We were all pretty sure this was a premeditated kidnapping, but..."
    Y thinking "Yeah, it's hard to believe the culprit would just leave a dog wandering around here."
    C blink "But you know, it's possible there's a simple explanation for it."
    $ renpy.music.set_volume(0.0, 2, channel="music")
    C smug "...Maybe the dog snuck in from the outside."
    Y surprised "...! Wait, but that would mean--" with shakeonce
    play ctc_sfx sfx_whooshlow
    $ show_side_oriana = False
    show oriana shouting at myleft
    show cecilia surprised at myright
    with custom_flashquick()
    O "EXCUSE me!" with shakeshort
    Y panicked "WAH! She's back..." with shakeonce
    O irritated "You two have been going on and on about this dog..."
    O leering2 "But isn't it rude to keep calling him \"the dog\" and not use his name?!"
    Y "....."
    $ renpy.music.set_volume(1.0, 2, channel="music")
    C sweatdrop "....."
    Y worried "...Um. We don't know his name."
    C default "It looks like his collar doesn't have a name tag. {size=-10}Ooh, what a neat collar...{/size}"
    Y default "So I guess we should just give him a name for now?"
    C happy "Ooh, how about \"Cerberus\"? He looks like a powerful little guard dog, don't you think?"
    I "That...might be a little cringey..."
    O annoyed "What kind of a cringey name is that?! That's unacceptable for a cutie patootie like him!" with hpunch
    O thinking "A creature with such magnificent, FLOOFY fur should be given a name befitting its charm and elegance."
    O happy "That's why his name can only be \"Shaggy\"!" with shakeonce
    Y worried2 "....."
    I "...Not that I'm one to judge, but both these two are awful at picking names, just...awful."
    play ctc_sfx sfx_emoteshout
    show cecilia pout at hop
    C "Where's the ELEGANCE in that name?! Did rubbing your face in that dog's belly rub out your brain cells?!" with shakeonce
    play ctc_sfx sfx_emoteshout
    show oriana leering at hop
    O "It's more elegant than what YOU came up with! Why is your head only filled with violence?!" with shakeonce
    play ctc_sfx sfx_emoteshout2
    show oriana leering behind cecilia:
        easein 0.1 xalign 0.19
        linear 0.05 xalign 0.2
    show cecilia shouting at myright:
        zoom 1.4 ypos 1.3
    C "At least I'M being consistent with my aesthetic! How does a single dog regress your mental age to 5 in an instant?!" with shakeshort
    play ctc_sfx sfx_emoteshout2
    show cecilia shouting behind oriana at myright:
        zoom 1.0
        easein 0.1 xalign 0.86
        linear 0.05 xalign 0.85
    show oriana angry at myleft:
        zoom 2.0 ypos 1.8
    O "Oh puh-LEASE, if anyone's mental age is 5, it'd be YOU, you blue dwarf!" with shakeshort
    play ctc_sfx sfx_emoteangry
    show oriana shouting behind cecilia at myleft_far:
        zoom 1.0
    show cecilia angry at mycenter_zoom
    C "AHHHHH! YOU WENT THERE!! YOU MADE FUN OF MY HEIGHT, DIDN'T YOU?!" with shakeshort
    hide oriana
    hide cecilia
    show oriana shouting at myleft
    show cecilia pout at myright
    play ctc_sfx sfx_emotesigh
    Y panicked "Uhh, guys? Is a dog's name really worth getting so heated over?" with hpunch
    O leering "[name_player], you be the tiebreaker! Which name do you like?"
    show cecilia pout at hop
    C "Yeah, [name_player], YOU decide!"
    Y worried "Ehhhhhhh..." with hpunch
    O leering2 "Come on, [name_player], just pick one!"
    show cecilia pout at doublehop
    C "Yeah, yeah! Pick one!"
    I "...Both of them are pretty bad..."
    I "...Nrgh, it's too much of a pain to come up with a better one right now." with hpunch
    Y "Fine...{cps=1} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend thinking "Let's go with...{nw}"

    menu:
        extend ""
        "Cerberus":
            $ input_name_dog = "Cerberus"
            $ name_dog = "{color=#606060}"+input_name_dog+"{/color}"
            play ctc_sfx sfx_emotehappy
            show cecilia overjoyed at hop
            C "Aha! \"[name_dog]\" it is!"
            O annoyed "...[name_player]. You have done this dog a great disservice. ...I hope you're ashamed of yourself."
        "Shaggy":
            $ input_name_dog = "Shaggy"
            $ name_dog = "{color=#606060}"+input_name_dog+"{/color}"
            play ctc_sfx sfx_emotehappy
            show oriana laughing at hop
            O "Good choice, [name_player]! Welcome to the family, [name_dog]!"
            show cecilia sobbing
            C "Aw, seriously, [name_player]? You don't think that's super lame?" with hpunch

    $ fadein_sideimage = True
    Y worried "Calm down, it's just a temporary name."
    $ fadein_sideimage = False
    Y blink "Anyways, should we actually start eating dinner now?"
    Y surprised "Oh, and I guess we should make something for [name_dog] too."
    $ fadein_sideimage = True
    C default "Yep, I think I remember seeing some dog food in the kitchen drawers."
    C happy "I'll go get it. B-R-B~"
    play ctc_sfx sfx_steps
    window auto hide
    hide cecilia with dissolve
    pause 0.5
    window auto show None
    $ _last_say_who = 'O'
    show oriana panicked at mycenter, hop
    O "Ahh, WAIT! Lemme do it! I WANNA DO IT! PRETTY PLEASE?!" with hpunch
    play ctc_sfx sfx_running_heels
    show oriana panicked at myright_far with move
    window auto hide
    hide oriana with dissolve
    pause 1.0
    stop music fadeout 3
    scene bg black with dissolvemed
    call save_file_name_update (1, "d1a2_part2")
    pause 1.0
    scene bg diningroom with dissolvemed
    I "....."
    I "It's a relief that [name_dog] came in when he did, but..."
    I "We never really landed on what we're gonna do about this situation."
    I "...Is there really no other option? Does one of us HAVE to die here?"
    $ _last_say_who = "C"
    show cecilia blush at mycenter with custom_flashquick()
    C "Welp! I'm beat! Let's call it a night, everyone!" with vpunch
    Y panicked "H-huh?" with shakeonce
    play music bgm_relaxed
    $ show_music_info_timer = music_info_pop_out_time()
    show cecilia smile at mycenter_to_myright
    pause 0.3
    $ _last_say_who = "O"
    show oriana sideeyeblink at myleft with dissolve
    O "I agree. We haven't searched for that long, but I can tell everyone is feeling tired, especially [name_player]."
    O sideeye "It would be more efficient to get some sleep and try again in the morning.{nw}"

    menu:
        extend ""
        "Agree":
            Y sad "...I mean, if you're both okay with that..."
            I "I'm definitely reaching my limit..." with hpunch
            C surprised "Whoa, hang in there, [name_player]! We haven't figured out who sleeps where yet!"
        "Object":
            Y wince "B-but what about our time limit?" with hpunch
            C default "Don't worry, [name_player], 20 hours is a TON of time!"
            C thinking "If anything, maybe we WANT time to run out!"
            C grin "The culprit would make an appearance to kill us, and then we could ambush 'em together!"
            Y worried "...M-maybe we shouldn't bet it all on that gamble..." with hpunch
    O blink "Let's see... 8 hours should be more than enough sleep. We'll resume our investigation at [t_clue]6 in the morning[t_cluee]."
    C thinking "6 o'clock...?"
    C surprised "Oh yeah, the clock in the foyer! It still hasn't gone off since 6!"
    O thinking "...Huh, now that you mention it... I wonder if that last loud chime broke it...?"
    C smile "Or, OR! If it really only rings at 6 o'clock, it might be able to serve as our [t_clue]morning alarm[t_cluee]."
    O blink "If it wakes everyone up on time, I won't complain."
    O default "[name_player], you should go to sleep right away."
    O thinking "You... You don't look well."
    Y surprised "O-okay...?"
    scene bg black with dissolvemed
    pause 1.0
    scene bg hallway with dissolvemed
    $ persistent.unlock_bg_hallway = True
    $ _last_say_who = None
    show oriana at myleft_fadein
    show cecilia at myright_fadein
    Y default "...So...how do we go about splitting the rooms?"
    O "Besides the master bedroom, there are two bedrooms, one furnished and one empty."
    if d1a1_checked_upstairs:
        Y blink "The little girl's room, and the suspiciously empty bedroom, huh...?"
    else:
        Y thinking "...Empty?"
        O thinking "Completely empty, yes. But there's a bed in it, so it's possible to sleep there."
        O disappointed "...Not comfortably, of course. There's no covers or a pillow."
        Y worried "....." with hpunch
    C smug "Wanna do rock-paper-scissors for the master bedroom?"
    O sideeye "That's fair."
    Y surprised "Sure, I guess?"
    I "Guess it's up to fate..."
    C happy "Okay! Rock, paper...{nw}"
    menu:
        extend ""
        "Play rock":
            C pout "Scissors... SHOOT!" with shakeonce
            C sobbing "Aww, I lost."
            O blink "We both played scissors so...it looks like [name_player] gets the master bedroom."
        "Play paper":
            C pout "Scissors... SHOOT!" with shakeonce
            C sobbing "Aww, I lost."
            O blink "We both played rock so...it looks like [name_player] gets the master bedroom."
        "Play scissors":
            C pout "Scissors... SHOOT!" with shakeonce
            C sobbing "Aww, I lost."
            O blink "We both played paper so...it looks like [name_player] gets the master bedroom."
    I "Huh. Guess I'm pretty good at this."
    C smug "Alright, now let's play for the furnished bedroom!"
    O disappointed "I don't mind either way, but fine."
    C pout "Rock, paper, scissors...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend " SHOOT!" with shakeonce
    play ctc_sfx sfx_emotehappy
    show oriana_raw surprised as oriana at backedaway_on
    show cecilia happy at hop
    C "Yes, I win!"
    show oriana annoyed at backedaway_off
    O "...Mrgh." with shakeonce
    Y relaxed "Sore loser, huh...?"
    O leering2 "....." with shakeonce
    Y panicked "Ah--"
    play ctc_sfx sfx_emotesob
    I "Crap, I said that out loud!" with hpunch
    C smile "You said you didn't mind either way~"
    O irritated "I don't. I'm perfectly fine using that room."
    Y thinking "But there's no covers or a pillow. Will you be okay?"
    play ctc_sfx sfx_emotesigh
    show oriana surprised at shrink
    O "R-right, there's no..."
    show oriana sideeyeblink at myleft
    O "Er, w-well, I'll be sleeping with [name_dog] anyway! So I'll have no trouble staying warm!" with hpunch
    Y sad "He's not very big, you know..."
    C thinking "Plus he's cold to the touch..."
    O confused "I-I mean... His cute and cuddliness will...keep me all worked up and warm?"
    O embarrassed "Er... {size=-10}W-wait, that sounded kind of...{/size}" with hpunch
    C grin "Pft~"
    Y happy "Heh..."
    play ctc_sfx sfx_emoteshout
    O angry "Don't laugh!" with shakeshort
    show oriana shouting
    C happy "Alright, let's get ready for bed!"
    $ _last_say_who = None
    scene bg black with dissolveslow
    I "...Is this really alright?"
    I "I can't shake this feeling that [t_clue]something will happen[t_cluee] tonight..."
    I "Ugh, but I'm so tired..." with hpunch
    stop music fadeout 5.0
    I "We'll investigate...again in the morning..."
    I "For now...let's get some sleep..."
    I "....."
    I ".........."
    play ctc_sfx "<silence 1.0>"
    I "{cps=6}...............{/cps}"
    play ctc_sfx "<silence 1.0>"
    scene bg black
    pause 2.0
    jump d1a3
label d1a3:
    if d1a1_order_flag != "A" and d1a1_order_flag != "" and d1a1_chaos_flag == "A":

        call d1a3_karma

    elif d1a1_order_flag == "C":

        if seen_ending_order and d1a1_chaos_flag != "":
            call d1a3_karma
        else:

            call d1a3_order
    else:
        if seen_ending_chaos == False:

            call d1a3_chaos
        else:

            if seen_ending_order == False:
                if d1a1_order_flag != "A" and d1a1_order_flag != "":
                    if d1a1_chaos_flag == "A":

                        call d1a3_karma
                    else:

                        call d1a3_order
                else:
                    call d1a3_chaos
            else:

                if d1a1_order_flag != "" and d1a1_chaos_flag != "":
                    call d1a3_karma
                else:
                    call d1a3_chaos

    jump gameover

label d1a3_karma:
    call save_file_name_update (1, "d1a3_karma")
    stop music
    scene bg black with dissolve
    X "...ey..."
    play ctc_sfx "sound/ctc_sound.ogg"
    I "Mrgh..."
    $ show_side_cecilia = True
    C hidden "...awake? ...[name_player]..."
    $ show_side_cecilia = False
    I "...Urgh... Is... Is that Cecilia?"
    $ _last_say_who = "C"
    scene bg masterbedroom dark
    show cecilia at mycenter
    with dissolvemed
    $ persistent.unlock_bg_masterbedroom_dark = True
    C happy "There we go! [name_player]! Hi! How do you feel?"
    Y wince "How do I...? Wha... I-is it 6 o'clock?"
    C blink "Nope, it's still the middle of the night. But I just thought you should know..."
    play ctc_sfx "<silence 1.0>"
    C smile "...We can escape now."
    Y afraid "...Wh...what...?"
    play music bgm_murder_chaos
    $ show_music_info_timer = music_info_pop_out_time()
    C thinking "Well, I guess not RIGHT now right now, but very very soon!"
    C happy "Come on, follow me!"
    play ctc_sfx sfx_steps
    scene bg masterbedroom dark with dissolve
    I "...Wait... No..."
    I "Is she... Is this what I think it is...?" with shakeonce
    play ctc_sfx sfx_steps
    scene bg black with fade
    scene bg hallway dark with fade
    $ persistent.unlock_bg_hallway_dark = True
    pause 1.0
    show cecilia blink at mycenter_fadein
    play sound ["<silence 0.5>", sfx_doorclose]
    pause 2.0
    C smile "Right this way~"
    hide cecilia with dissolve
    scene bg hallway dark:
        xalign 0.4 yalign 0.5 zoom 2.0
    with dissolve
    I "....."
    I "...This is...Oriana's room...?" with shakeonce
    $ show_side_cecilia = True
    C blink "Ready?"
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotehappy
    C happy "Ta-da~ [u_music_note]" with hpunch
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    $ renpy.music.set_volume(0.25, 3.0, channel="music")
    scene bg black with dissolvemed
    play sound [sfx_dooropenslow_unlatch, "<silence 1.5>", sfx_dooropenslow_move]
    pause 3.0
    scene bg emptybedroom dark chaos:
        xalign 1.0 yalign 0.5 zoom 1.15 matrixcolor BrightnessMatrix(-0.5)
        easein 10.0 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    with dissolvemed
    $ renpy.music.set_volume(1.0, 3.0, channel="music")
    $ persistent.unlock_bg_emptybedroom_dark_chaos = True
    pause 3.0
    I "...Huh...? Where's Oriana...?"
    Y sad "...Oriana...?"
    $ renpy.music.set_volume(0.0, 0.0, channel="music")
    play ctc_sfx sfx_heartbeat_single
    $ fadein_sideimage = False
    $ renpy.music.set_volume(1.0, 3.0, channel="music")
    Y afraid "...!!" with shakeshort
    $ fadein_sideimage = True
    scene cg chaos at wobble with dissolvemed
    play sound sfx_restrain
    O "Mmmmph!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    Y afraid "Oriana...!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    I "She's...tied up... And...a gag... A...t-towel...?"
    play ctc_sfx sfx_knifebrandish
    window auto hide None
    scene bg emptybedroom dark chaos
    show cecilia blink knife at mycenter
    with custom_flashquick()
    window auto show None
    Y wince "Nrgh!" with hpunch
    $ _last_say_who = "C"
    window auto hide
    play sound sfx_knifeglint
    show knife glint at mycenter:
        zoom 1.0 ypos 1.05 alpha 0.0
        easein 0.4 zoom 1.2 ypos 1.15 alpha 1.0
        linear 0.2 alpha 0.0
    pause 1.0
    I "A... A knife...?!" with shakeonce
    C smile "I was actually planning to finish this quickly, but then I figured that you should be a part of it."
    Y afraid "A-a part of it?" with shakeonce
    C happy knife "Yeah, you know! [t_clue]Killing[t_cluee] Oriana!"
    C grin "I mean, come on, this is so simple! We just play by the rules, and we get to escape! Easy-peasy!"
    Y "Easy-peasy?!" with shakeshort
    if d1a1_chaos_flag == "A":

        C surprised "What's wrong, [name_player]? Didn't you already agree that we'd do this?"
        C default "All I did was save you most of the dirty work."
        play ctc_sfx sfx_emotesigh
        show cecilia sweatdrop at shrink
        C "Getting her to settle down while I tied her up was NOT easy."
        Y shocked "But I... I-I thought you were just exploring possibilities!" with shakeonce
        show cecilia blink at mycenter
        C "And you gave me an answer."
        C creepy "You said that you were in, and that we should do it."
        Y afraid "That's... I-I..." with shakeonce
        $ renpy.music.set_volume(0.25, 1.5, channel="music")
        scene bg black with blot_in
        I "...No... She's right..."
        I "...I...chose this path."
        I "This scene in front of me... It's happening...because of me..."
        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play ctc_sfx sfx_emotehappy
        show bg emptybedroom dark chaos:
            matrixcolor BrightnessMatrix(-1.0)
            linear 5.0 matrixcolor BrightnessMatrix(0.0)
        show cecilia happy at mycenter, hop
        C "That's right! This is all because of you!" with hpunch
        C default "[t_clue]You made the decision that brought us here.[t_cluee]"
        stop music fadeout 3.0
        C smile "So now, it's time for you to make one more...deci...sion..."
    elif d1a1_chaos_flag == "B":

        $ fadein_sideimage = False
        Y shouting "Cecilia, I told you we can't do this!" with shakeonce
        Y pained "I told you that all of us have to get out of here together!"
        Y angry "That it's the right thing to do!" with shakeshort
        $ fadein_sideimage = True
        C blink "....."
        C thinking "Yeah. What you're suggesting is certainly the right thing to do."
        Y angry "Then--" with shakeonce
        C blink "But remember what I told {i}you{/i}, [name_player]?"
        C "Sometimes, you're forced to make a decision to go one way or the other."
        C "Sacrifice something to gain something else."
        play ctc_sfx "<silence 1.0>"
        C creepy "...This is one of those moments."
        play ctc_sfx "<silence 1.0>"
        show cecilia creepygrin at shudder
        C "And the thing forcing you...is me~ [u_music_note]" with hpunch
        Y afraid "Cecilia... You...{cps=2} {/cps}{nw}"
        play ctc_sfx "<silence 1.0>"
        $ fadein_sideimage = False
        extend afraid2 "YOU MONSTER!" with shakeshort
        $ fadein_sideimage = True
        play ctc_sfx sfx_emotesigh
        stop music fadeout 3.0
        show cecilia sobbing at shrink
        C "Aww, now that's hurtful! I'm still giving you a chance to make a...decision...here..."
    else:

        $ fadein_sideimage = False
        Y "Cecilia, you... I...{w=0.3}{nw}"
        play ctc_sfx "<silence 1.0>"
        extend " H-how could you do something like this?!" with shakeonce
        $ fadein_sideimage = True
        C surprised "What's wrong, [name_player]? Do you feel surprised by this? Perhaps even a little disgusted?"
        Y pained "Wh-what?!" with shakeonce
        play ctc_sfx sfx_emotehappy
        show cecilia overjoyed at hop
        C "Oooh~ Looks like you're VERY disgusted! Then I have some good news for you!"
        C blush "[name_player], you're a [t_clue]good person[t_cluee] after all!"
        Y shocked "Wh-what are you...?" with shakeonce
        C thinking "I mean, I dunno if you talked with Oriana while I was somewhere else, but..."
        C default "As far as I know, you never wished for anybody to die here."
        C blink "And your reaction to all this tells me that you don't find this sort of action to be justified."
        C smile "So even in this crazy situation, with everything so {i}perfectly{/i} set up for you, you STILL wouldn't wish for someone to die!"
        show cecilia happy at shudder
        C "How righteous of you!"
        Y scream "What the hell are you talking about?!" with shakeshort
        C sad "...You know... I have nothing against Oriana."
        C "She has traditional ideals and an uptight sense of justice that I can find a little cringey at times, but..."
        C smile "She's a good person. The thought of killing someone to escape this place never once passed her mind."
        C blink "Truly, she's the LAST person in the world who deserves to die."
        play ctc_sfx "<silence 1.0>"
        $ renpy.music.set_volume(0.0, 0.0, channel="music")
        show bg black with custom_flashquickred()
        show cecilia creepygrin at mycenter:
            zoom 1.05
            easein 0.5 zoom 1.0
        $ renpy.music.set_volume(1.0, 2.0, channel="music")
        C "...And that's exactly why she's here now, moments before this blade ends her life." with shakeonce
        Y troubled "Cecilia...!" with shakeonce
        show bg emptybedroom dark chaos
        show cecilia creepygrin at mycenter:
            zoom 1.0
        with dissolve
        C blink "...But depending on what you do now, we'll find out if I truly am the sole evil of this group."
        Y afraid "Wha... Wh-what are you talking about?" with hpunch
        stop music fadeout 3.0
        C default "I'm gonna ask you to make a...decision..."

    show cecilia at mycenter
    C "A...deci..."
    show cecilia surprised with custom_flashquick()
    show cecilia surprised at shrink
    C "Mngh?!" with shakeonce
    window auto hide
    play sound sfx_heartbeat_single
    show cecilia injured with shakeshort
    pause 1.0
    scene bg emptybedroom dark chaos with dissolve
    play sound sfx_fallhard
    show bg emptybedroom dark chaos with shakeonce
    pause 1.0
    Y panicked "...Huh? Cecilia?!" with shakeonce
    $ fadein_sideimage = False
    $ show_side_cecilia = True
    C hidden "Urk... Knngh!" with shakeshort
    C "NRRRRRRRRRRGHGHGHGHH!!" with shakelong
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    I "Wh-what's happening to her?! She looks like she's in a lot of pain!" with shakeonce
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O hidden "...Mmmf..."
    O "Mmfmfmfm~" with hpunch
    $ show_side_oriana = False
    Y shocked "...! O-Oriana...?" with shakeonce
    $ fadein_sideimage = True
    I "Oriana's not struggling anymore..."
    I "...Is she...laughing?"
    I "Wait, I should untie her first..." with hpunch
    scene bg black with fade
    play sound sfx_clothrustle
    pause 1.0
    scene bg emptybedroom dark with fade
    $ persistent.unlock_bg_emptybedroom_dark = True
    $ _last_say_who = 'O'
    show oriana irritated at mycenter with dissolve
    O "*cough* *cough* Thank you, [name_player]..." with shakeshort
    Y panicked "What's happening to Cecilia?!"
    O default "Oh, that?"
    O relaxed "That's simply divine retribution at work."
    Y "R-retribution...?"
    O sideeye "Why do you look so surprised, [name_player]? We talked about this earlier."
    Y angry "What are you talking about?! Talked about what?!" with shakeonce
    O shouting "Isn't it obvious NOW?! Cecilia is the culprit!" with shakeshort
    O "She brought us here and orchestrated this whole killing game in order to kill ME!" with shakeshort
    Y afraid "Cecilia...is the culprit?"
    $ fadein_sideimage = False
    $ show_side_cecilia = True
    C hidden "...Y-you...!" with shakeshort
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    play ctc_sfx "<silence 1.0>"
    O shadow "....."
    play ctc_sfx sfx_heartbeat_single
    O "...Heh." with shakeonce
    play ctc_sfx sfx_heartbeat_single
    show bg emptybedroom dark:
        matrixcolor BrightnessMatrix(-0.25)
        linear 0.1 matrixcolor BrightnessMatrix(0.0)
    O "...Ehe... Hehe..." with shakeshort
    play ctc_sfx "<silence 1.0>"
    window auto hide
    show bg emptybedroom dark:
        matrixcolor BrightnessMatrix(-1.0)
        pause 2.0
        linear 3.0 matrixcolor BrightnessMatrix(0.0)
    show oriana deranged at mycenter
    with custom_flashbulblongred()
    play music bgm_murder_order
    $ show_music_info_timer = music_info_pop_out_time()
    window auto show None
    O "{size=+10}AHAHHAHAHAHHAHAHAHAAAAAAA!!{/size}" with shakelong
    Y afraid2 "O-Oriana?!" with shakeonce
    show oriana insane at mycenter
    O "Hey, what's wrong? You look like you're having some trouble breathing down there!"
    O grin "Could it be that [t_clue]rat poison[t_cluee] is not to your throat's liking?"
    O relaxed "I suspected you might try something like this... So I laced your plate at dinner."
    O deranged "For it to start kicking in now is nothing less than GODLY timing!" with shakeshort
    Y afraid "Y-you...poisoned Cecilia...?" with shakeonce
    O irritated "It was the only way, [name_player]. Neither of us could possibly take her on in a fight."
    Y pained "But YOU were the one so adamantly against us killing each other!" with shakeonce
    O sideeyeblink "Obviously, that was so Cecilia would let her guard down."
    if d1a1_chaos_flag == "A":
        O sideeye "I mean, isn't that why you agreed to help her with killing me?"
        Y afraid "Th-that's..." with shakeonce
        O leering "....."
        O irritated "...Well, it doesn't matter either way now. In the end, we won."
    else:
        O confident "You deserve some credit too, [name_player]. Your genuine shock and terror really helped fool her."
        Y shocked "That's... I..."
    O relaxed "All that's left is for the villain of this story to just die already."
    $ show_side_cecilia = True
    C hidden "{size=-10}...ah...{/size}" with hpunch
    $ fadein_sideimage = False
    C "{cps=6}.........{/cps}"
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    I "...Cecilia... She's...not moving..."
    O "Hehehe...{w=1.0}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    play loop_sfx sfx_heartbeat
    show bg emptybedroom dark at wobble
    with custom_flashquick()
    extend deranged " OH HOW THE HIGH AND MIGHTY HAVE FALLEN!!" with shakelong
    Y afraid "O-Oriana?!"
    play ctc_sfx sfx_strike
    show oriana creepy at hop:
        zoom 1.05
        linear 0.3 zoom 1.0
    O "Your mistake was not killing me sooner, Cece!" with shakeshort
    play ctc_sfx sfx_strike
    show oriana creepy at hop:
        zoom 1.05
        linear 0.3 zoom 1.0
    O "Now DIE at my feet! Pant for breath like the VILE creature you are!" with shakeshort
    O leering2 "Kidnapping the two of us... Forcing us to play your insane killing game...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend annoyed " A [t_clue]demon[t_cluee] like you has no right to breathe our air!" with shakeonce
    O shouting "You're a STAIN to humanity! You bring nothing but chaos and misery to EVERYWHERE YOU GO!" with shakeshort
    Y troubled "...That's enough..." with hpunch
    show oriana insane:
        easein 20.0 zoom 1.5 ypos 1.5
    show bg emptybedroom dark:
        matrixcolor BrightnessMatrix(0.0)
        easein 20.0 matrixcolor BrightnessMatrix(-1.0)
    O "Come on, Cece... Flash that knife again! I'm right heeeere~ [u_music_note]" with shakeshort
    Y "Oriana..." with shakeonce
    O grin "You were so close, so VERY close... I've never seen anything so laughably TRAGIC before."
    Y pained2 "Oriana... Please..." with shakeonce
    O deranged "Don't just fade away like this! Squeal more! SQUIRM MORE!" with shakeshort
    show bg emptybedroom dark at reset:
        zoom 1.0
        matrixcolor BrightnessMatrix(0.0)
    show oriana deranged at mycenter
    show cecilia_raw shadow knife as cecilia at myright, backedaway_on
    O "{cps=36}I WANT TO SEE YOU--{/cps}{w=0.1}{nw}"
    play ctc_sfx sfx_knifestab
    stop music
    stop loop_sfx
    show bg black at reset
    show oriana stabbed
    show stab censor
    with custom_flashquickred()
    extend " ....!!!" with shakeonce
    show cecilia shadow knife at myright, backedaway_off
    play ctc_sfx "<silence 1.0>"
    C "{cps=12}...Will you...shut up...already...{/cps}"
    play ctc_sfx ["<silence 0.3>", sfx_knifeslash]
    window auto hide
    show bg black
    show bloodsplatter_5 behind oriana at truecenter:
        alpha 0.5
    show cecilia shadow knife bloody at myleft
    with custom_flashbulblongred()
    $ renpy.pause(1.0, hard=True)
    show bg black with dissolve
    show oriana_raw stabbed as oriana at shrink, backedaway_on
    pause 2.5
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
    pause 3.0
    hide bloodsplatter_1
    Y depressed "{cps=6}.........{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    Y "{cps=6}.......{/cps} ...What...just..."
    $ fadein_sideimage = True
    play ctc_sfx ["<silence 0.2>", sfx_bloodsquish_thud] volume 0.5
    show cecilia_raw shadow knife bloody as cecilia at mycenter, backedaway_on with move
    I "...She...stabbed her...in the throat...and..."
    play ctc_sfx "<silence 1.0>"
    I "{cps=12}Oriana is...{/cps}{w=0.5}[t_clue]dead[t_cluee]...?"
    play ctc_sfx "<silence 1.0>"
    show cecilia shadow knife bloody at backedaway_off
    C "{cps=12}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    play sound ["<silence 0.5>", sfx_knifedrop]
    show cecilia shadow bloody at shrink
    C "...Heh..."
    play ctc_sfx "<silence 1.0>"
    show cecilia poisonedgrin
    C "{cps=24}Look who's...got a problem...breathing...now...{/cps}"
    play ctc_sfx "<silence 1.0>"
    window auto hide
    hide cecilia with dissolvemed
    pause 0.5
    play sound sfx_fallsoft
    with vpunch
    pause 3.0
    Y "...Ce...{cps=1} {/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend afraid2 "CECILIA!!" with shakeshort
    $ fadein_sideimage = True
    window auto hide
    pause 0.5
    play sound ["<silence 0.1>", sfx_clothrustle] volume 0.5
    play ctc_sfx sfx_fallsoft
    show bg black with shakeonce
    pause 2.0
    $ _last_say_who = 'C'
    scene bg black
    show cecilia_raw poisoned at mycenter_closeup:
        blur 20.0
        linear 5.0 blur 5.0
        block:
            linear 2.0 blur 0.0
            linear 2.0 blur 5.0
            repeat
    with dissolveslow
    pause 0.5
    play music bgm_tragedy fadein 0.5
    C "...Kar...ma..."
    I "Her eyes are still open...{nw}"

    menu:
        extend ""
        "Say something":
            Y shocked "...Ah..."
            $ fadein_sideimage = False
            Y "....."
            $ fadein_sideimage = True
            I "I...don't know what to say..." with hpunch
        "Say nothing":
            Y troubled "....."
    C "I guess... ...just you now..."
    Y afraid "H-huh...?"
    show cecilia_raw poisoned at mycenter_closeup:
        zoom 1.0
        easeout 3.0 zoom 1.2
    with dissolve
    scene cg karma1 at wobble:
        xalign 0.5 yalign 1.0 zoom 1.1
        easein 3.0 yalign 0.5 zoom 1.0
    with dissolvemed
    pause 1.0
    $ show_side_cecilia = True
    C poisonedgrin "...Sorry... ...about Ria..."
    $ fadein_sideimage = False
    C poisonedgrin bloody "I couldn't... ...resi... ...shut... ...her...up..."
    Y troubled "Don't talk... Just...keep breathing..."
    C poisoned bloody "{size=-5}You'll... ...to leave... ...by your...{/size}"
    C "{size=-10}...orry... ...oodbye...{/size}"
    C "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ show_side_cecilia = False
    $ fadein_sideimage = True
    scene cg karma1 at reset:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 2.5 zoom 1.0
    with dissolve
    pause 2.0
    scene cg karma2 with dissolvequick
    $ renpy.music.set_pan(0.15, 0.0, channel='sound')
    play sound ["<silence 0.1>", sfx_bloodsquish_thud]
    with shakeonce
    $ renpy.pause(1.0, hard=True)
    pause 2.0
    scene cg karma with dissolve
    pause 2.0
    I "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y depressed bloody "{cps=6}.........{/cps}"
    window auto hide None
    $ renpy.music.set_pan(0.0, 0.0, channel='sound')
    play sound sfx_frontdoor
    show bg black with shakeshort
    pause 3.0
    I "...That must be...the front door downstairs opening..."
    I "But...only one of us...needed to die..."
    I "...Oriana... Cecilia..."
    scene cg karma4:
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
    I "They're...both dead..."
    I "And...it's my fault... It's [t_clue]all my fault[t_cluee]."
    I "Because of choices I made..."
    I "This...is how it all ends...?" with shakeonce
    I "Both of them are... A-are..." with shakeonce
    Y troubled bloody "...Ahh..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    show cg karma4 at reset:
        xalign 0.5 yalign 0.7 zoom 2.0
        matrixcolor InvertMatrix(0.75)
    with custom_flashquick()
    Y whiteeyes bloody "..... ...aaaaAAAGGHH...!{w=1.0}{nw}" with shakeshort
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    stop music
    window auto hide None
    scene bg black with custom_flashquick()
    window auto show None
    KI "[t_ghost]{size=+5}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAGGGGGGGGHHHHHHHHHH!!!{/size}[t_ghoste]" with shakelong
    play ctc_sfx "<silence 1.0>"
    play sound sfx_wail
    window auto hide dissolveslow
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#ff0000}BAD END{/color}{/size}\nKarma Ending{/font}" with dissolve
    pause 2.0
    $ _skipping = True
    pause 3.0
    hide text with dissolveslow
    $ seen_ending_karma = True
    $ persistent.unlock_cg_chaos = True
    $ persistent.unlock_cg_karma = True
    $ shard_string = "Karma"
    return
label d1a3_order:
    call save_file_name_update (1, "d1a3_order")
    stop music
    scene bg black with dissolve
    pause 1.0
    play sound sfx_frontdoor
    show bg black with shakeshort
    pause 6.0
    play sound sfx_knock
    X "...[name_player]..."
    play ctc_sfx "sound/ctc_sound.ogg"
    I "Mrgh..."
    $ show_side_oriana = True
    O hidden "...wake up... ...[name_player]..."
    $ show_side_oriana = False
    play ctc_sfx sfx_knock
    I "...Urgh... Is... Is that Oriana?" with hpunch
    play ctc_sfx sfx_steps
    window auto hide
    pause 2.0
    play ctc_sfx sfx_dooropen
    play sound sfx_steps_heels
    pause 2.0
    $ _last_say_who = "O"
    scene bg masterbedroom dark
    show oriana at mycenter
    with dissolvemed
    $ persistent.unlock_bg_masterbedroom_dark = True
    O "...Good, you're awake."
    Y wince "Oriana...? Sorry, did I miss the clock chime?"
    O blink "...No, it's still the middle of the night."
    Y surprised "Then... Wh-what's up?"
    O "...It's done."
    Y "Huh? What's done?"
    play ctc_sfx "<silence 1.0>"
    O happy "...We...can leave now..."
    Y panicked "Wh-what do you mean? I-is... Is the front door open?" with shakeonce
    show oriana happy at mycenter_closeup
    O "Come on, just get up and follow me!" with hpunch
    I "She's tugging my arm..." with shakeonce
    I "Why is she so eager...?"
    play ctc_sfx sfx_steps
    scene bg black with fade
    scene bg hallway dark with fade
    $ persistent.unlock_bg_hallway_dark = True
    pause 1.0
    play sound ["<silence 0.5>", sfx_doorclose]
    pause 2.0
    scene bg hallway dark:
        xalign 0.3 yalign 0.5 zoom 1.0
        easein 3.0 zoom 1.5
    pause 2.0
    I "...This is...Cecilia's room...?"
    $ show_side_oriana = True
    O shadow "Go ahead. Open it."
    $ show_side_oriana = False
    $ fadein_sideimage = False
    Y shocked "....." with shakeonce
    $ fadein_sideimage = True
    I "...There's no way, right?"
    scene bg black with dissolvemed
    pause 1.0
    with shakeonce
    play sound [sfx_dooropenslow_unlatch, "<silence 1.5>", sfx_dooropenslow_move]
    pause 3.0
    scene bg bedroom dark:
        xalign 0.8 yalign 0.2 zoom 1.7 matrixcolor BrightnessMatrix(-0.9)
        easein 5.0 zoom 1.5 matrixcolor BrightnessMatrix(-0.5)
    with dissolvemed
    pause 3.0
    play ctc_sfx sfx_heartbeat_single
    Y wince "...!" with shakeshort
    I "What's...that smell...?"
    scene bg bedroom dark:
        matrixcolor BrightnessMatrix(-0.5)
        xalign 0.8 yalign 0.2 zoom 1.5
        easein 5.0 xalign 1.0
    with dissolve
    I "Cecilia's...not in bed?"
    I "....."
    play ctc_sfx sfx_heartbeat_single
    show bg bedroom dark:
        matrixcolor BrightnessMatrix(-0.5)
        xalign 1.0 yalign 0.2 zoom 1.5
    I "...!" with shakeonce
    $ persistent.unlock_bg_bedroom_dark = True
    scene bg bedroom dark:
        xalign 1.0 yalign 0.3 zoom 1.5 matrixcolor BrightnessMatrix(-0.5)
        easein 2.0 yalign 1.0 matrixcolor BrightnessMatrix(-1.0)
    with dissolve
    I "She's...on the floor...?"
    Y sad "Hey..."
    $ fadein_sideimage = False
    Y "What are you doing, Cecilia? Your bed's...right..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    Y depressed "...!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    scene cg order:
        xalign 0.5 yalign 0.5
        parallel:
            matrixcolor BrightnessMatrix(-1.0)
            linear 8.0 matrixcolor BrightnessMatrix(0.0)
        parallel:
            zoom 1.5
            easein 15.0 zoom 1.0
    with dissolvemed
    pause 5.0
    I "{cps=12}Her face...{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y shocked "{cps=12}She's...{/cps}{cps=1} {/cps}{nw}"
    $ fadein_sideimage = False
    play ctc_sfx "<silence 1.0>"
    play loop_sfx sfx_introambiance_sequence4_loop fadein 3.0
    extend "{cps=12}...[t_clue]dead[t_cluee]...?{/cps}"
    Y "...No..." with shakeonce
    Y pained2 "No, no, no no no..." with shakeshort
    $ fadein_sideimage = True
    scene bg black with dissolveslow
    $ _last_say_who = "O"
    scene bg bedroom dark
    show oriana sideeyeblink at mycenter
    with dissolveslow
    O "....."
    O "It looks like she spent her final moments in complete agony, crawling towards the door to get help."
    O happy "...Pft. Like a snake. How fitting..." with shakeonce
    Y troubled "This... This isn't what I think it is..."
    $ fadein_sideimage = False
    Y afraid2 "It's NOT, right, Oriana?!" with shakeonce
    $ fadein_sideimage = True
    O sideeye "And what do you think this is, [name_player]?{nw}"

    menu:
        extend ""
        "Accuse her":
            Y troubled "You did this..."
            $ fadein_sideimage = False
            Y "You killed her, didn't you, Oriana?" with shakeonce
            $ fadein_sideimage = True
            O leering "You're accusing me of a crime? Where's your evidence?"
            Y scream "Who else could it possibly be?! There's only three of us in this whole house!" with shakeshort
            O blink "...Exactly."
            Y shocked "...Huh?"
        "Say nothing":
            Y angry "....."
            O leering "Hmph. Do you think glaring at me will do anything?"
    O blink "...I remembered something, you see. Earlier, when we were talking in the hallway."
    stop loop_sfx fadeout 3.0
    O default "...It was Cecilia. She's the reason we're all here..."
    O leering2 "She's the [t_clue]demon[t_cluee] we were looking for."
    Y afraid "...Cecilia's the...?"
    play ctc_sfx "<silence 1.0>"
    O shadow "....." with shakeonce
    play ctc_sfx sfx_heartbeat_single
    show bg bedroom dark:
        matrixcolor BrightnessMatrix(-0.25)
        linear 0.1 matrixcolor BrightnessMatrix(0.0)
    O "...Hmph..." with shakeshort
    play ctc_sfx "<silence 1.0>"
    show bg bedroom dark:
        matrixcolor BrightnessMatrix(-0.5)
        linear 0.2 matrixcolor BrightnessMatrix(0.0)
    O "...Ehe... Hehe..." with shakeshort
    play ctc_sfx "<silence 1.0>"

    scene bg black with dissolvemed
    pause 0.77
    window auto show None
    show bg bedroom dark at wobble, blurring:
        matrixcolor BrightnessMatrix(-1.0)
        pause 2.0
        linear 3.0 matrixcolor BrightnessMatrix(0.0)
    show oriana deranged at mycenter_closeup
    play music bgm_murder_order
    $ show_music_info_timer = music_info_pop_out_time()
    O "{size=+10}AHAHHAHAHAHHAHAHAHAAAAAAA!!{/size}" with shakelong
    Y afraid2 "O-Oriana?!" with shakeonce
    hide oriana
    show oriana surprised at mycenter:
        zoom 1.05
        easein 0.2 zoom 1.0
    O "It's only fair... It's only correct..." with hpunch
    O annoyed "If one of us has to die, it should be her!" with shakeonce
    O leering "After all... She set up this whole situation so that she could kill ME! That was her plan from the start!"
    Y scream "What the hell are you talking about?!" with shakeshort
    if d1a1_checked_kitchen:
        O irritated2 "Oh, don't pretend you don't know! I saw your reaction earlier!"
        O "She suggested that you two team up and kill ME, didn't she?" with shakeonce
        Y shocked "Th-that's... She... Well..." with shakeonce
        O surprised "...I knew it.{w=0.5}{nw}"
        play ctc_sfx "<silence 1.0>"
        extend laughing " I KNEW IT!" with shakeonce
        O insane "I'm so glad you didn't listen to her, [name_player]. You stayed on the side of [t_clue]justice[t_cluee]..."
        Y afraid "This...is justice?!" with shakeonce
    O disappointed "Didn't you say it yourself, [name_player]?"
    O thinking "A horrible person who derives pleasure in causing chaos and misery..."
    O blink "...Someone like that won't be missed by anyone."
    play ctc_sfx sfx_emotequestion
    O confident "Someone like that...[t_clue]deserves to die[t_cluee], wouldn't you agree?"
    Y pained "But you said yourself that \"no one deserves to end someone's life\"!" with shakeonce
    O sideeyeblink "And certainly, no one does. I don't have that right."
    O confused "But those cans in the kitchen cabinets are hard to read in the dark... I could have made a liiiittle mistake with Cecilia's food..."
    if d1a1_checked_kitchen:
        Y troubled "...! Y-you... You used the [t_clue]rat poison[t_cluee]..." with shakeonce
        O insane "Oh so you saw it too? I can't believe Cecilia was stupid enough to leave that lying around..."
    else:
        Y shocked "...! Y-you... You [t_clue]poisoned[t_cluee] her..." with shakeonce
        O insane "Hey now, that's a hasty conclusion. Maybe her food was just particularly spoiled."
    Y scream "ORIANA!!" with shakeshort
    play ctc_sfx sfx_emotehappy
    show oriana grin at hop
    O "Anyway, that doesn't matter, [name_player]! What matters is we can escape now!"
    O sobbing "And the culprit just HAPPENED to choke and die too! She'll never bother us again!"
    show oriana overjoyed at shudder
    O "Don't you see?! This is the [t_clue]best possible ending[t_cluee]!"
    Y scream "This CAN'T be the best ending! Someone DIED here!" with shakeshort
    O annoyed "And again, she deserved it. The world is better off without her."
    Y shocked "...Oriana... Do you hear yourself right now?"
    $ _last_say_who = "O"
    show oriana dejected
    pause 0.01
    show bg bedroom dark:
        matrixcolor BrightnessMatrix(0.0)
        linear 5.0 matrixcolor BrightnessMatrix(-1.0)
    with dissolvemed
    O "{cps=6}.....{/cps}"
    $ renpy.music.set_volume(0.5, 3, channel="music")
    O "If it weren't for her..." with shakeonce
    play ctc_sfx "<silence 1.0>"
    O troubled "If it weren't for HER, I'd..." with shakeshort
    play ctc_sfx "<silence 1.0>"
    Y "...I don't understand..."
    $ fadein_sideimage = False
    Y "Why...? ...Why do you [t_clue]hate her so much[t_cluee]...?"
    $ fadein_sideimage = True
    $ renpy.music.set_volume(1.0, 0, channel="music")
    show bg bedroom dark:
        matrixcolor BrightnessMatrix(0.0)
    play ctc_sfx sfx_emotehappy
    show oriana laughing at hop
    O "Come on, [name_player]! Let's not waste any more time!"
    O confident "I already checked the front door! It's wide open! We can leave!"
    I "....."
    I "...It's no use..."
    I "She's...not listening to me anymore..."
    O relaxed "Everything worked out perfectly..."
    play ctc_sfx "<silence 1.0>"
    O grin "Hehe...{w=1.0}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    stop music
    show bg bedroom dark:
        matrixcolor BrightnessMatrix(-1.0)
        linear 3.0 matrixcolor BrightnessMatrix(0.0)
    show oriana deranged:
        zoom 1.2 ypos 1.15
        pause 0.1
        easein 0.5 zoom 1.0 ypos 1.05
    with custom_flashquick()
    extend deranged " {size=+10}AHAHAHHAHAHHAHAA!!{/size}" with shakelong
    play ctc_sfx sfx_steps
    scene bg bedroom dark at reset
    with dissolvemed
    pause 5.0
    Y shadow "{cps=6}.....{/cps}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    Y "{cps=6}.......{/cps}"
    play ctc_sfx "<silence 1.0>"
    Y "...Cecilia..."
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = True
    scene cg order with dissolvemed
    pause 2.0
    play loop_sfx sfx_heartbeat
    Y shadow "Was it...really you...?" with shakeonce
    I "....."
    show cg order:
        blur 0
        linear 10.0 blur 20.0
    Y "...Were you...really the culprit all along...?"
    $ fadein_sideimage = False
    Y troubled "...Hey... Talk to me... Do you... ...deserve to be...?" with shakeonce
    $ fadein_sideimage = True
    show bg black with custom_flashquick()
    I "Ngh! What...is that...?" with shakeonce
    KI "[t_ghost]...can't...[t_ghoste]"
    I "A voice...? Where is it...?!"
    KI "[t_ghost]...like this... Can't...[t_ghoste]"
    I "Something's...screaming...!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    stop loop_sfx
    show bg black with custom_flashquick()
    KI "[t_ghost]{size=+5}IT CAN'T END LIKE THIIIIIIIS!!{/size}[t_ghoste]" with shakelong
    play ctc_sfx "<silence 1.0>"
    play sound sfx_wail
    window auto hide dissolveslow
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#ff0000}BAD END{/color}{/size}\nOrder Ending{/font}" with dissolve
    pause 2.0
    $ _skipping = True
    pause 3.0
    hide text with dissolveslow
    $ seen_ending_order = True
    $ persistent.unlock_cg_order = True
    $ shard_string = "Order"
    return

label d1a3_chaos:
    call save_file_name_update (1, "d1a3_chaos")
    stop music
    scene bg black with dissolve
    X "...ey..."
    play ctc_sfx "sound/ctc_sound.ogg"
    I "Mrgh..."
    $ show_side_cecilia = True
    C hidden "...awake? ...[name_player]..."
    $ show_side_cecilia = False
    I "...Urgh... Is... Is that Cecilia?"
    $ _last_say_who = "C"
    scene bg masterbedroom dark
    $ persistent.unlock_bg_masterbedroom_dark = True
    show cecilia at mycenter
    with dissolvemed
    C happy "There we go! [name_player]! Hi! How do you feel?"
    Y wince "How do I...? Wha... I-is it 6 o'clock?"
    C blink "Nope, it's still the middle of the night. But I just thought you should know..."
    play ctc_sfx "<silence 1.0>"
    C smile "...We can escape now."
    Y afraid "...Wh...what...?"
    play music bgm_murder_chaos
    $ show_music_info_timer = music_info_pop_out_time()
    C thinking "Well, I guess not RIGHT now right now, but very very soon!"
    C happy "Come on, follow me!"
    play ctc_sfx sfx_steps
    scene bg masterbedroom dark with dissolve
    I "...Wait... No..."
    I "Is she... Is this what I think it is...?" with shakeonce
    play ctc_sfx sfx_steps
    scene bg black with fade
    scene bg hallway dark with fade
    $ persistent.unlock_bg_hallway_dark = True
    pause 1.0
    show cecilia blink at mycenter_fadein
    play sound ["<silence 0.5>", sfx_doorclose]
    pause 2.0
    C smile "Right this way~"
    hide cecilia with dissolve
    scene bg hallway dark:
        xalign 0.4 yalign 0.5 zoom 2.0
    with dissolve
    I "....."
    I "...This is...Oriana's room...?" with shakeonce
    $ show_side_cecilia = True
    C blink "Ready?"
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotehappy
    C happy "Ta-da~ [u_music_note]" with hpunch
    $ fadein_sideimage = True
    $ show_side_cecilia = False
    $ renpy.music.set_volume(0.25, 3.0, channel="music")
    scene bg black with dissolvemed
    play sound [sfx_dooropenslow_unlatch, "<silence 1.5>", sfx_dooropenslow_move]
    pause 3.0
    scene bg emptybedroom dark chaos:
        xalign 1.0 yalign 0.5 zoom 1.15 matrixcolor BrightnessMatrix(-0.5)
        easein 10.0 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    with dissolvemed
    $ renpy.music.set_volume(1.0, 3.0, channel="music")
    $ persistent.unlock_bg_emptybedroom_dark_chaos = True
    pause 3.0
    I "...Huh...? Where's Oriana...?"
    Y sad "...Oriana...?"
    $ renpy.music.set_volume(0.0, 0.0, channel="music")
    play ctc_sfx sfx_heartbeat_single
    $ fadein_sideimage = False
    $ renpy.music.set_volume(1.0, 3.0, channel="music")
    Y afraid "...!!" with shakeshort
    $ fadein_sideimage = True
    scene cg chaos at wobble with dissolvemed
    play sound sfx_restrain
    O "Mmmmph!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    Y afraid "Oriana...!" with shakeonce
    play ctc_sfx "<silence 1.0>"
    I "She's...tied up... And...a gag... A...t-towel...?"
    play ctc_sfx sfx_knifebrandish
    window auto hide None
    scene bg emptybedroom dark chaos
    show cecilia blink knife at mycenter
    with custom_flashquick()
    window auto show None
    Y wince "Nrgh!" with hpunch
    $ _last_say_who = "C"
    window auto hide
    play sound sfx_knifeglint
    show knife glint at mycenter:
        zoom 1.0 ypos 1.05 alpha 0.0
        easein 0.4 zoom 1.2 ypos 1.15 alpha 1.0
        linear 0.2 alpha 0.0
    pause 1.0
    I "A... A knife...?!" with shakeonce
    C smile "I was actually planning to finish this quickly, but then I figured that you should be a part of it."
    Y afraid "A-a part of it?" with shakeonce
    C happy knife "Yeah, you know! [t_clue]Killing[t_cluee] Oriana!"
    C grin "I mean, come on, this is so simple! We just play by the rules, and we get to escape! Easy-peasy!"
    Y "Easy-peasy?!" with shakeshort
    if d1a1_chaos_flag == "A":

        C surprised "What's wrong, [name_player]? Didn't you already agree that we'd do this?"
        C default "All I did was save you most of the dirty work."
        play ctc_sfx sfx_emotesigh
        show cecilia sweatdrop at shrink
        C "Getting her to settle down while I tied her up was NOT easy."
        Y shocked "But I... I-I thought you were just exploring possibilities!" with shakeonce
        show cecilia blink at mycenter
        C "And you gave me an answer."
        C creepygrin "You said that you were \"in\", and that we should do it."
        Y afraid "That's... I-I..." with shakeonce
        $ renpy.music.set_volume(0.25, 1.5, channel="music")
        scene bg black with blot_in
        I "...No... She's right..."
        I "...I...chose this path."
        I "This scene in front of me... It's happening...because of me..."
        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play ctc_sfx sfx_emotehappy
        show bg emptybedroom dark chaos:
            matrixcolor BrightnessMatrix(-1.0)
            linear 5.0 matrixcolor BrightnessMatrix(0.0)
        show cecilia happy at mycenter, hop
        C "That's right! This is all because of you!" with hpunch
        C default "[t_clue]You made the decision that brought us here.[t_cluee]"
        C smile "So now, it's time for you to make one more decision."
    elif d1a1_chaos_flag == "B":

        $ fadein_sideimage = False
        Y shouting "Cecilia, I told you we can't do this!" with shakeonce
        Y pained "I told you that all of us have to get out of here together!"
        Y angry "That it's the right thing to do!" with shakeshort
        $ fadein_sideimage = True
        C blink "....."
        C thinking "Yeah. What you're suggesting is certainly the right thing to do."
        Y angry "Then--" with shakeonce
        C blink "But remember what I told {i}you{/i}, [name_player]?"
        C "Sometimes, you're forced to make a decision to go one way or the other."
        C "Sacrifice something to gain something else."
        play ctc_sfx "<silence 1.0>"
        C creepy "...This is one of those moments."
        play ctc_sfx "<silence 1.0>"
        show cecilia creepygrin at shudder
        C "And the thing forcing you...is me~ [u_music_note]" with hpunch
        Y afraid "Cecilia... You...{w=0.5}{nw}"
        play ctc_sfx "<silence 1.0>"
        $ fadein_sideimage = False
        extend afraid2 " YOU MONSTER!" with shakeshort
        $ fadein_sideimage = True
        play ctc_sfx sfx_emotesigh
        show cecilia sobbing at shrink
        C "Aww, now that's hurtful! I'm still giving you a chance to make a decision here..."
    else:

        $ fadein_sideimage = False
        Y "Cecilia, you... I...{w=0.3}{nw}"
        play ctc_sfx "<silence 1.0>"
        extend " H-how could you do something like this?!" with shakeonce
        $ fadein_sideimage = True
        C surprised "What's wrong, [name_player]? Do you feel surprised by this? Perhaps even a little disgusted?"
        Y pained "Wh-what?!" with shakeonce
        play ctc_sfx sfx_emotehappy
        show cecilia overjoyed at hop
        C "Oooh~ Looks like you're VERY disgusted! Then I have some good news for you!"
        C blush "[name_player], you're a [t_clue]good person[t_cluee] after all!"
        Y shocked "Wh-what are you...?" with shakeonce
        C thinking "I mean, I dunno if you talked with Oriana while I was somewhere else, but..."
        C default "As far as I know, you never wished for anybody to die here."
        C blink "And your reaction to all this tells me that you don't find this sort of action to be justified."
        C smile "So even in this crazy situation, with everything so {i}perfectly{/i} set up for you, you STILL wouldn't wish for someone to die!"
        show cecilia happy at shudder
        C "How righteous of you!"
        Y scream "What the hell are you talking about?!" with shakeshort
        C sad "...You know... I have nothing against Oriana."
        C "She has traditional ideals and an uptight sense of justice that I can find a little cringey at times, but..."
        C smile "She's a good person. The thought of killing someone to escape this place never once passed her mind."
        C blink "Truly, she's the LAST person in the world who deserves to die."
        play ctc_sfx "<silence 1.0>"
        $ renpy.music.set_volume(0.0, 0.0, channel="music")
        show bg black with custom_flashquickred()
        show cecilia creepygrin at mycenter:
            zoom 1.05
            easein 0.5 zoom 1.0
        $ renpy.music.set_volume(1.0, 2.0, channel="music")
        C "...And that's exactly why she's here now, moments before this blade ends her life." with shakeonce
        Y troubled "Cecilia...!" with shakeonce
        show bg emptybedroom dark chaos
        show cecilia creepygrin at mycenter:
            zoom 1.0
        with dissolve
        C blink "...But depending on what you do now, we'll find out if I truly am the sole evil of this group."
        Y afraid "Wha... Wh-what are you talking about?" with hpunch
        C default "I'm gonna ask you to make a decision."

    Y shocked "A...decision...?"
    show cecilia smile at mycenter
    C "Yep! I'm gonna ask you to choose one of two options."
    C blink "The first option is you turn away and [t_clue]let me kill Oriana[t_cluee]."
    Y troubled "....."
    C creepy knife "The second option is you take this knife and [t_clue]kill her yourself[t_cluee]."
    Y shocked "...! You..." with shakeonce
    C happy "Well? What do you think, [name_player]?"
    show cecilia overjoyed at hop
    C "You have {i}no{/i} idea how excited I am to hear your answer!"
    Y "...I..." with shakeonce
    C creepygrin "Come on, [name_player], don't keep me in suspense!"
    $ _last_say_who = None
    $ renpy.music.set_volume(0.5, 1.0, channel="music")
    show bg black with dissolvemed
    I "...Oriana..."
    C "What will you choose?"
    play loop_sfx sfx_heartbeat fadein 1.0
    show cecilia creepygrin at mycenter:
        zoom 1.0 ypos 1.05
        easein 20.0 zoom 1.5 ypos 1.25
    with dissolve
    menu:
        "Let Cecilia kill her":
            stop loop_sfx
            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            scene bg emptybedroom dark chaos
            show cecilia creepygrin at mycenter
            with dissolve
            Y shadow "...I can't..."
            $ fadein_sideimage = False
            stop music fadeout 3.0
            Y "I...give up..."
            $ fadein_sideimage = True
            C surprised "Huh? What do you mean?"
            Y "....."
            play ctc_sfx sfx_steps
            scene bg black with fade
            scene bg hallway dark with fade
            pause 2.0
            I "....."
            $ show_side_cecilia = True
            C hidden "So... That's your answer, huh? ...Well, I can't say I blame you."
            $ fadein_sideimage = False
            C "You're choosing to walk the less messy path. In a way, I respect it."
            $ fadein_sideimage = True
            I "......."
            C "But... I have to say..."
            $ fadein_sideimage = False
            C "...I'm just a little bit disappointed in you, [name_player]."
            C "You're disappointed too, aren't you? ...Oriana..."
            $ fadein_sideimage = True
            I "........."
            play ctc_sfx "<silence 1.0>"
            scene bg hallway dark
            pause 3.7
            $ renpy.music.set_pan(-0.65, 0.0, channel='sound')
            play sound sfx_knifestab
            window auto show None
            $ show_side_oriana = True
            O hidden "!!!" with shakeshort
            $ show_side_oriana = False
            window auto hide None
            play ctc_sfx sfx_knifeslash volume 0.5
            with shakelong
            pause 3.0
            $ renpy.music.set_pan(0.0, 1.0, channel='sound')
            Y troubled "{cps=6}.....{/cps}"
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = False
            Y "{cps=6}.......{/cps}"
            play ctc_sfx "<silence 1.0>"
            Y "I'm...sorry..." with shakeonce
            play ctc_sfx "<silence 1.0>"
            Y "Oriana... I..."
            play ctc_sfx "<silence 1.0>"
            $ fadein_sideimage = True
            window auto hide None
            play sound sfx_frontdoor
            show bg hallway dark with shakeshort
            pause 3.0
            show bg hallway dark at blurring with dissolve
            Y depressed "That...must be the front door opening..."
            $ fadein_sideimage = False
            Y "Cecilia and I... The two of us can escape now..."
            Y "...Just...us two..." with hpunch
            $ fadein_sideimage = True
            scene bg black with dissolveslow
            I "....."
            C surprised bloody "Hm? What're you zoning out for, [name_player]?"
            play ctc_sfx "<silence 1.0>"
            $ renpy.music.set_pan(0.65, 0, channel='sound')
            play sound sfx_bloodsquish
            I "...!" with shakeonce
            I "Something cold and wet...on my shoulder..."
            I "...Her hand..."
            play ctc_sfx "<silence 1.0>"
            I "...The smell...of [t_clue]blood[t_cluee]..." with hpunch
            play ctc_sfx sfx_emotehappy
            C happy bloody "Come on, let's go~ [u_music_note]"
            window auto hide
            $ renpy.music.set_pan(0.0, 0, channel='sound')
            play sound sfx_steps
            $ show_side_cecilia = False
            scene bg black
            pause 4.0
            play loop_sfx sfx_heartbeat fadein 1.0
            I "...Why...?"
            I "Why did it have to end like this...?" with shakeonce
        "Kill Oriana yourself":

            stop loop_sfx
            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            scene bg emptybedroom dark chaos
            show cecilia creepygrin at mycenter
            with dissolve
            Y shadow "...I'll do it."
            $ fadein_sideimage = False
            Y "Give me that knife. I'll... I'll end this myself."
            $ fadein_sideimage = True
            C default "....."
            C "So that's what it looks like...?"
            C "The face of a [t_clue]demon[t_cluee] who has long abandoned human morality..."
            C "Steadfast and merciless, spilling blood to serve only their own selfish ambitions..."
            C blink "...Heh... Ehehehe..." with shakeonce
            window auto hide
            play ctc_sfx ["<silence 0.2>", sfx_knifeequip]
            show cecilia blink knife at shrink
            pause 0.4
            show cecilia blink at mycenter with move
            C smile "You're super interesting, [name_player]! I'm so...{w=0.5}{nw}"
            play ctc_sfx "<silence 1.0>"
            extend blush " So INCREDIBLY happy I met you!" with vpunch
            hide cecilia with dissolve
            Y shadow2 "....."
            play ctc_sfx sfx_knifebrandish
            scene bg emptybedroom dark chaos
            with custom_flashquick()
            show cg chaos:
                zoom 1.05
                easein 1.0 zoom 1.0
            show pov_knife:
                xalign 0.5 yalign 1.0 zoom 0.8 alpha 0.0
                easein 1.0 alpha 1.0
            with dissolve
            pause 1.0
            if d1a1_chaos_flag == "A":
                I "...To think it would be this easy..."
                Y blink "{cps=6}.......{/cps}{nw}"
                $ fadein_sideimage = False
                play ctc_sfx "<silence 1.0>"
                stop music
                extend happy " ...Heh.{w=1.5}{nw}"
                $ fadein_sideimage = True
                hide pov_knife
                play ctc_sfx ["<silence 0.3>", sfx_knifeslash]
                show cg chaos:
                    matrixcolor BrightnessMatrix(0.0)
                    xalign 0.4 yalign 0.2 zoom 1.1
                    easein 1.0 zoom 3.0 matrixcolor BrightnessMatrix(-0.5)
                scene bg black with custom_flashbulblongred()
                pause 1.0
                scene bg emptybedroom dark chaos2 with dissolvemed
                $ persistent.unlock_bg_emptybedroom_dark_chaos2 = True
                $ _last_say_who = "C"
                show cecilia surprised at mycenter with dissolvemed
                C "....."
                show cecilia surprised at shudder
                C "...Ah..."
                C "Aha... Ahahha..." with shakeonce
                play ctc_sfx "<silence 1.0>"
                show cecilia creepygrin with custom_flashquick()
                C "{size=+10}AHAHHAHAHAHHAHAAHHAHAAAAA!!{/size}" with shakelong
                C "Did you LAUGH?! You laughed, didn't you, [name_player]?!" with shakeonce
                I "....."
                C "I thought you were just emotionlessly doing what needed to be done, but you totally ENJOYED that!"
                Y blink bloody "...I guess...I did, didn't I?"
                C overjoyed "You're crazy, [name_player]! Meeting you's truly the best thing that's ever happened to me!" with shakeshort
                window auto hide None
                play sound sfx_frontdoor
                show bg emptybedroom dark chaos2 with shakeshort
                show cecilia surprised at hop
                pause 1.0
                show bg emptybedroom dark chaos2 with dissolve
                C "...Oh! I think that was the sound of the door downstairs opening!"
                C blush "Come on, [name_player]! Let's get out of here~"
                play ctc_sfx sfx_steps
                scene bg emptybedroom dark chaos2 with dissolvemed
                pause 5.0
                Y blink bloody "....."
                $ fadein_sideimage = False
                Y bloody "Sorry, Oriana. It's nothing personal..."
                Y "{cps=6}.....{/cps} ...Goodbye."
                $ fadein_sideimage = True
                play loop_sfx sfx_heartbeat
            else:
                menu:
                    "Kill Oriana quickly":
                        hide pov_knife with dissolve
                        I "No. There's no need to hesitate."
                        I "I've... I've made up my mind."
                        stop music
                        call d1a3_chaos_kill
                    "Apologize first":
                        Y shadow "...I'm sorry about this, Oriana..."
                        O "....."
                        window auto hide
                        show cg chaos1 with dissolve
                        $ persistent.unlock_cg_chaos1 = True
                        pause 1.0
                        hide pov_knife with dissolve
                        Y afraid "...!" with shakeonce
                        I "She's calmed down... Has she given up...?"
                        I "Is she...[t_clue]letting me kill her[t_cluee]...?" with shakeonce
                        scene cg chaos2 with dissolve
                        $ persistent.unlock_cg_chaos2 = True
                        pause 1.0
                        O "......."
                        Y shocked "...Don't..."
                        $ fadein_sideimage = False
                        Y "Don't look at me like that..."
                        play ctc_sfx "<silence 1.0>"
                        stop music
                        show pov_knife:
                            xalign 0.5 yalign 1.0 zoom 0.8
                        Y scream "DON'T LOOK AT ME LIKE THAAAAAAAAAAAAAAAAAAT!!{w=1.0}{nw}" with shakeshort
                        hide pov_knife
                        $ fadein_sideimage = True
                        call d1a3_chaos_kill
                    "{color=#ff0000}Kill Cecilia instead{/color}":
                        Y shadow "....."
                        stop music
                        play ctc_sfx "<silence 1.0>"
                        window auto hide None
                        scene bg emptybedroom dark chaos
                        show cecilia at mycenter
                        with custom_flashquick()
                        $ fadein_sideimage = False
                        play ctc_sfx sfx_knifeswing
                        window auto show None
                        Y angry "RAAAAAAAAAAGGGGHHHH!!!{w=0.5}{nw}" with shakeshort
                        window auto hide None
                        $ fadein_sideimage = True
                        play ctc_sfx "<silence 1.0>"
                        scene bg black
                        show cecilia at mycenter_zoom
                        with custom_flashquickred()
                        $ _last_say_who = "C"
                        play sound sfx_knifestab
                        show cecilia surprised with shakelong
                        pause 2.4
                        C "{cps=6}.......{/cps}"
                        play ctc_sfx "<silence 1.0>"
                        Y troubled "{cps=6}.........{/cps}"
                        play ctc_sfx "<silence 1.0>"
                        C "[name_player]... Y-you..." with hpunch
                        play ctc_sfx "<silence 1.0>"
                        C "You're..." with shakeshort
                        play ctc_sfx "<silence 1.0>"
                        window auto hide
                        pause 0.25
                        show cecilia creepygrin with dissolvemed
                        pause 0.5
                        window auto show
                        play loop_sfx sfx_introambiance_sequence4_loop fadein 2.0
                        C "...everything I could have asked for..."
                        play ctc_sfx "<silence 1.0>"
                        Y shocked "...Wh-what...?" with hpunch
                        play ctc_sfx "<silence 1.0>"
                        I "She...caught it...?" with shakeonce
                        play ctc_sfx sfx_whooshlow
                        hide cecilia with custom_flashquick()
                        Y pained "UWAAAHHH!!"
                        window auto hide None
                        play sound [sfx_fallhard, sfx_knifedrop]
                        show bg black with shakelong
                        pause 1.0
                        show bg emptybedroom dark chaos:
                            xalign 0.7 zoom 3.0
                        with dissolve
                        $ show_side_cecilia = True
                        C sad "Did you honestly think I wouldn't know you'd try that? It was MY idea to give you the knife!"
                        $ fadein_sideimage = False
                        C smile "Or what, was this your way of being the big hero? You were gonna commit murder for something silly like that?" with shakeshort
                        play ctc_sfx sfx_restrain
                        Y pained2 "AAAAUGHH!!" with shakeshort
                        $ fadein_sideimage = True
                        I "I...can't...escape..." with shakeonce
                        C creepygrin "[t_clue]You can't kill me by yourself[t_cluee], [name_player]. But don't worry. You can rest in peace now..."
                        $ fadein_sideimage = False
                        $ show_side_cecilia = False
                        Y pained "CECILIA, YOU--{w=1.0}{nw}" with shakeonce
                        $ fadein_sideimage = True
                        stop loop_sfx
                        jump d1a3_chaos_betray
        "Stop Cecilia":

            stop loop_sfx
            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            scene bg emptybedroom dark chaos
            show cecilia creepygrin at mycenter
            with dissolve
            Y blink "...No. This ends now."
            $ fadein_sideimage = False
            Y default "Give me the knife, Cecilia. We're not killing anyone."
            $ fadein_sideimage = True
            C creepygrin "....."
            C creepy "......."
            C blink "Interesting. So that's your answer, huh, [name_player]?"
            Y leering "Give me the knife."
            play ctc_sfx sfx_heartbeat_single
            C sad "Even when the situation before you is set up perfectly like this... You choose to stop me."
            play ctc_sfx "<silence 1.0>"
            C "You choose...to prolong our [t_clue]hell[t_cluee]."
            Y "Give.{nw}"
            $ fadein_sideimage = False
            play ctc_sfx "<silence 1.0>"
            extend "{w=0.5} Me.{w=0.5} The knife."
            $ fadein_sideimage = True
            C blink "...[name_player]..."
            C "...No. \"Stranger\"."
            play ctc_sfx "<silence 1.0>"
            stop music
            show bg black
            C serious "You no longer interest me."
            play ctc_sfx "<silence 1.0>"
            Y shouting "I SAID GIVE ME--{w=0.5}{nw}"
            show bg emptybedroom dark chaos
            jump d1a3_chaos_betray

    play ctc_sfx "<silence 1.0>"
    show bg black with custom_flashquick()
    I "Ngh! What...is that...?" with shakeonce
    KI "[t_ghost]...can't...[t_ghoste]"
    I "A voice...? Where is it...?!"
    KI "[t_ghost]...cept this... I...[t_ghoste]"
    I "Something's...screaming...!" with shakeshort
    play ctc_sfx "<silence 1.0>"
    stop loop_sfx
    show bg black with custom_flashquick()
    KI "[t_ghost]{size=+5}I CAN'T ACCEPT THIIIIIIS!!{/size}[t_ghoste]" with shakelong
    play ctc_sfx "<silence 1.0>"
    jump d1a3_chaos_end

label d1a3_chaos_end:
    show bg black
    play sound sfx_wail
    window auto hide dissolveslow
    pause 2.0
    $ renpy.choice_for_skipping()
    $ _skipping = False
    show text "{font=fonts/AveriaLibre-Regular.ttf}{size=+30}{color=#ff0000}BAD END{/color}{/size}\nChaos Ending{/font}" with dissolve
    pause 2.0
    $ _skipping = True
    pause 3.0
    hide text with dissolveslow
    $ seen_ending_chaos = True
    $ persistent.unlock_cg_chaos = True
    $ shard_string = "Chaos"
    return

label d1a3_chaos_kill:
    play ctc_sfx ["<silence 0.3>", sfx_knifeslash]
    show cg chaos:
        matrixcolor BrightnessMatrix(0.0)
        xalign 0.4 yalign 0.2 zoom 1.1
        easein 1.0 zoom 3.0 matrixcolor BrightnessMatrix(-0.5)
    scene bg black
    with custom_flashbulblongred()
    pause 1.0
    scene bg emptybedroom dark chaos2 with dissolvemed
    $ persistent.unlock_bg_emptybedroom_dark_chaos2 = True
    Y troubled bloody "{cps=5}.........{/cps}"
    play ctc_sfx "<silence 1.0>"
    I "{cps=5}.....{/cps}{nw}"
    $ renpy.music.set_pan(-0.12, 0, channel='sound')
    play sound sfx_knifedrop
    extend " ...I..." with shakeonce
    window auto hide None
    $ renpy.music.set_pan(0.0, 0, channel='sound')
    play sound sfx_frontdoor
    show bg emptybedroom dark chaos2 with shakeshort
    pause 1.0
    show bg emptybedroom dark chaos2 with dissolve
    $ _last_say_who = "C"
    show cecilia surprised at mycenter with dissolve
    C "...Oh! I think I just heard the door downstairs open!"
    C happy "Come on, [name_player]! Let's get out of here~"
    play ctc_sfx sfx_steps
    scene bg emptybedroom dark chaos2 with dissolvemed
    pause 5.0
    play loop_sfx sfx_heartbeat
    scene bg emptybedroom dark chaos2 at blurring with dissolve
    Y depressed bloody "...Oriana... Ori...ana..." with shakeonce
    $ fadein_sideimage = False
    Y "I'm... I....." with shakeshort
    $ fadein_sideimage = True
    return

label d1a3_chaos_betray:
    play ctc_sfx sfx_whoosh
    hide cecilia with custom_flashquick()
    show bg black
    with soulout
    pause 1.0
    window auto hide
    play sound sfx_fallsoft
    pause 5.0
    $ name_npc = name_player
    X "....."
    X "......."
    X "...gh... Grrgh..."
    $ name_npc = _("???")
    I "Wha... What happened..."
    I "It's so dark..."
    I "I...feel so weak..."
    I "...! That... That smell..." with shakeonce
    play loop_sfx sfx_heartbeat
    I "...[t_clue]Blood[t_cluee]...?" with shakeonce
    I "...Wait... I...see something..."
    I "Is that Oriana...?"
    I "...No..."
    I "I'm...on the floor... And the stench of blood is creeping closer..."
    play ctc_sfx sfx_bloodsquish
    I "Ngh! It's...reached my face..." with shakeonce
    I "The smell's so strong..."
    I "I think...I'm gonna be sick..." with shakeonce
    I "...Oriana..."
    I "I... I couldn't save you..."
    I "...I'm...sorry..."
    I "....."
    I "......."
    play ctc_sfx "<silence 1.0>"
    stop loop_sfx
    I "{cps=5}..............{/cps}{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    jump d1a3_chaos_end

label d1a4:
    window auto hide
    stop music fadeout 3.0
    show bg black with dissolve
    I ".........Wait."
    I "I... I remember something..."
    scene bg foyer at grayscale_on
    show oriana_raw irritated at myleft, grayscale_on, backedaway_on
    show cecilia_raw happy at myright, grayscale_on
    with custom_flashbulblong()
    I "...That's right..."
    scene bg kitchen at grayscale_on
    show cecilia_raw smile at mycenter, grayscale_on
    with dissolvemed
    I "I've...been here before...!" with shakeonce
    scene bg masterbedroom at grayscale_on
    show oriana_raw shouting at mycenter, grayscale_on
    with dissolvemed
    I "I know what's going to happen..."
    scene bg diningroom at grayscale_on
    show oriana_raw shadow at myleft, grayscale_on
    show cecilia_raw surprised at myright, grayscale_on, backedaway_on
    with dissolvemed
    I "It's the same...every single time..."
    play ctc_sfx sfx_heartbeat_single
    window auto hide None
    scene bg black with custom_flashquick()
    window auto show None
    I "I...I've played this killing game [t_clue]over and over[t_cluee]!" with shakeonce
    I "And...every single time..."
    I "One of these two... Or even both of them..."
    window auto hide
    scene bg foyer
    show oriana at myleft
    show cecilia surprised at myright
    with custom_flashbulblongred()
    C "Hmm? What's wrong, [name_player]? You look kinda pale."
    Y shadow "...I..."
    O thinking "...[name_player]. I think I know what your answer will be, but..."
    O default "Do you remember anything about how you ended up here? Anything at all?{nw}"

    menu:
        extend ""
        "Tell the truth (disabled)":
            pass
        "Lie to them (disabled)":
            pass
        "{color=#cccc00}Tell the WHOLE truth{/color}":
            Y shadow "....."
    call save_file_name_update (1, "d1a4")
    $ fadein_sideimage = False
    Y "...I remember..."
    Y wince "...I... I've been through all of this before..."
    $ fadein_sideimage = True
    C thinking "You've..."
    O surprised "...What?"
    Y blink "This might sound a little crazy, but..."
    play ctc_sfx sfx_emotequestion
    $ fadein_sideimage = False
    Y leering "I'm a [t_clue]time traveler[t_cluee] from the future."
    Y "I've experienced this killing game a countless number of times."
    $ fadein_sideimage = True
    C surprised "Wait, are you--"
    O leering2 "....." with shakeonce
    C thinking "Er..."
    Y shadow "And every single time, without fail..."
    scene cg chaos at grayscale_on:
        xalign 0.5 yalign 0.5 zoom 1.0
        easein 5.0 zoom 1.1
    with custom_flashbulblong()
    play loop_sfx sfx_heartbeat fadein 3.0
    pause 1.0
    scene cg order at grayscale_on:
        xalign 0.5 yalign 0.5 zoom 1.0
        easein 5.0 zoom 1.1
    with dissolvemed
    pause 1.0
    scene cg karma4 at grayscale_on:
        xalign 0.5 yalign 0.5 zoom 1.0
        easein 5.0 zoom 1.1
    with dissolvemed
    pause 1.0
    scene bg black
    show shard_chaos at grayscale_on:
        matrixcolor BrightnessMatrix(1.0) * OpacityMatrix(0.0)
        pause 0.5
        linear 1.0 matrixcolor BrightnessMatrix(1.0) * OpacityMatrix(1.0)
        easeout 0.8 matrixcolor BrightnessMatrix(0.0) * OpacityMatrix(1.0)
    show shard_order at grayscale_on:
        matrixcolor BrightnessMatrix(1.0) * OpacityMatrix(0.0)
        pause 1.5
        linear 1.0 matrixcolor BrightnessMatrix(1.0) * OpacityMatrix(1.0)
        easeout 0.8 matrixcolor BrightnessMatrix(0.0) * OpacityMatrix(1.0)
    show shard_karma at grayscale_on:
        matrixcolor BrightnessMatrix(1.0) * OpacityMatrix(0.0)
        pause 2.5
        linear 1.0 matrixcolor BrightnessMatrix(1.0) * OpacityMatrix(1.0)
        easeout 0.8 matrixcolor BrightnessMatrix(0.0) * OpacityMatrix(1.0)
    with custom_flashbulblong()
    pause 1.0
    stop loop_sfx fadeout 3.0
    Y troubled "{cps=12}At least one of you two{/cps}{cps=3}...{/cps}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend "[t_clue]dies tonight[t_cluee]." with shakeonce
    $ fadein_sideimage = True
    scene bg black with dissolveslow
    scene bg foyer
    show oriana blink at myleft
    show cecilia thinking at myright
    with dissolveslow
    Y depressed "{cps=12}No matter what I do... I...{/cps}" with shakeonce
    C "....."
    O "...[name_player]."
    O default "Let's go to the table in the dining room. I think we should sit down and talk about this."
    play ctc_sfx "<silence 1.0>"
    Y shadow "......."
    play ctc_sfx "<silence 1.0>"
    scene bg black with dissolveslow
    I "I told them everything I could remember."
    I "Every [t_clue]clue[t_cluee] we found in the house... Every conversation I had with either of them..."
    I "The writing on the front door changing... Playing rock-paper-scissors to decide on the bedrooms..."
    play ctc_sfx sfx_heartbeat_single
    show bg black with custom_flashquickred()
    I "And...how we would never get through the night...without someone getting murdered..." with shakeonce
    window auto hide
    play sound [sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime]
    pause 5.0
    scene bg diningroom
    show oriana_raw thinking as oriana at myleft, backedaway_on
    show cecilia_raw sad as cecilia at myright, backedaway_on
    with dissolvemed
    pause 0.5
    $ _last_say_who = "O"
    show oriana thinking at myleft, backedaway_off
    O "...I see. You've been through a lot, [name_player]."
    show cecilia thinking at myright, backedaway_off
    C "Still, it's pretty hard to believe."
    C smug "I can't picture Oriana having the guts to kill anyone."
    O leering2 "...Do you want to try me?"
    Y thinking "...Actually, now might be a good time to ask."
    C default "Hmm? Ask what?"
    Y "Each time one of you...died... It's strange but..."
    $ fadein_sideimage = False
    play ctc_sfx sfx_emotequestion
    Y leering "It felt like you two...[t_clue]knew each other already[t_cluee]. Like, even before all this."
    Y thinking "Oriana, you even called her \"Cece\"..."
    $ fadein_sideimage = True
    O panicked "...!" with shakeonce
    C blink "....."
    C smile "...Looks like the jig is up, Ria."
    O annoyed "Tsk. It's not like we got very far with it..." with shakeonce
    Y surprised "Um..."
    O irritated "{cps=12}.........{/cps}{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend thinking " *sigh*" with hpunch
    O blink "I suppose considering all you've been through, [name_player]... You deserve to know the [t_clue]truth[t_cluee]."
    Y panicked "Then..." with shakeonce
    O leering2 "That said, we can only answer you with what we actually know."
    O thinking "For questions like \"Why are we trapped here?\", we're in the dark as much as you are."
    Y default "...Sure."
    show cecilia happy at hop
    C "Okay! What do you want to know, [name_player]? Ask away!"
    I "There's so many questions I need answers to... I guess I should start with the important ones."
    I "Okay, let's do this!" with shakeonce
    play music bgm_truth
    $ show_music_info_timer = music_info_pop_out_time()
    $ d1a4_questioning_clue1 = False
    $ d1a4_questioning_clue2 = False
    $ d1a4_questioning_clue2A = False
    $ d1a4_questioning_clue2AA = False
    $ d1a4_questioning_clue2AB = False
    $ d1a4_questioning_clue2B = False
    $ d1a4_questioning_clue3 = False
    $ d1a4_third_member_mentioned = False

label d1a4_questioning_menu:
    $ _last_say_who = None
    menu:
        "\"Why were you keeping secrets from me?\"" if not d1a4_questioning_clue1:
            call d1a4_question1
        "[u_check]\"Why were you keeping secrets from me?\"" if d1a4_questioning_clue1:
            call d1a4_question1

        "\"How do you two know each other?\"" if not d1a4_questioning_clue2:
            call d1a4_question2
        "[u_check]\"How do you two know each other?\"" if d1a4_questioning_clue2:
            call d1a4_question2

        "\"Could Cecilia really be the culprit?\"" if not d1a4_questioning_clue2A and d1a4_questioning_clue2:
            call d1a4_question2A
        "[u_check]\"Could Cece really be the culprit?\"" if d1a4_questioning_clue2A:
            call d1a4_question2A

        "\"Why does Oriana hate Cece so much?\"" if not d1a4_questioning_clue2AA and d1a4_questioning_clue2A:
            call d1a4_question2AA
        "[u_check]\"Why does Ria hate Cece so much?\"" if d1a4_questioning_clue2AA:
            call d1a4_question2AA

        "\"Can we trust Cece?\"" if not d1a4_questioning_clue2AB and d1a4_questioning_clue2A:
            call d1a4_question2AB
        "[u_check]\"Can we trust Cece?\"" if d1a4_questioning_clue2AB:
            call d1a4_question2AB

        "\"About your club's third member...\"" if not d1a4_questioning_clue2B and d1a4_third_member_mentioned:
            call d1a4_question2B
        "[u_check]\"About your club's third member...\"" if d1a4_questioning_clue2B:
            call d1a4_question2B

        "\"Why do I keep going back in time?\"" if not d1a4_questioning_clue3:
            call d1a4_question3
        "[u_check]\"Why do I keep going back in time?\"" if d1a4_questioning_clue3:
            call d1a4_question3

        "[t_clue]End your questioning[t_cluee]" if d1a4_questioning_clue3:
            jump d1a4_questioning_end

    jump d1a4_questioning_menu

label d1a4_question1:
    Y thinking "I don't understand why you two were hiding the fact that you know each other...?"
    O blink "There were a couple of reasons for that."
    O default "The first is that we didn't know how you would react to us."
    C smile "Yep! I mean, if you knew the two of us were connected, wouldn't you have been super scared?"
    C thinking "You might've thought we would team up to kill you...or maybe that we were the ones who kidnapped you in the first place.{nw}"

    menu:
        extend ""
        "\"That's a good point...\"":
            Y surprised "I guess that makes sense..."
            C sad "Sorry, [name_player]. It was all Ria's idea."
            C thinking "I was of the mind of just giving you all the details and letting things happen from there."
            O leering "That's too careless. [name_player]'s [t_clue]power[t_cluee] is one thing, but from our point of view, we only have one shot of getting out alive."
            I "....."
        "\"I would never do that!\"":
            Y annoyed "That's a bit of a stretch, wouldn't you say?"
            O thinking "We couldn't take any chances, not with the situation being like it is."
            C sweatdrop "In the end, sounds like that kinda backfired on us, huh?"
            C smug "To think there were some instances where you spurred us on to turn against each other..."
            I "....." with shakeonce
    O blink "Moving on... The other reason we didn't say anything was because we wanted to collect information first."
    O default "If we told you about our background, you might've been too distracted thinking about it to investigate properly."
    show cecilia happy at hop
    C "And boy, did that work out! You remembering everything from other timelines saved us from a lot of aimlessly looking around!"
    I "I...guess that's one good thing about all this...?"
    I "Ugh... I'm so exhausted though... Like I've been awake for days straight..." with shakeonce
    C smile "But now that the cat's outta the bag, we don't have to play dumb anymore, right Ria?"
    O thinking "I suppose not."
    play ctc_sfx sfx_emotequestion
    I "So basically...[t_clue]no more secrets[t_cluee], huh...?"
    $ d1a4_questioning_clue1 = True
    return
label d1a4_question2:
    Y default "So how do you two know each other?"
    O blink "Cecilia and I are in the same club at our university."
    play ctc_sfx sfx_emotequestion
    O default "...The [t_clue]Occult Club[t_cluee]."
    Y surprised "The...Occult Club...?"
    play ctc_sfx sfx_emotehappy
    show cecilia happy at hop
    C "And I'm the president!"
    Y panicked "YOU'RE the president?!" with shakeonce
    play ctc_sfx sfx_emoteshout
    show cecilia pout at doublehop
    C "Hey! Why are you more shocked about that part?!" with shakeonce
    O blink "Just as it sounds, we research and investigate supernatural phenomena, particularly with spirits, curses, and so on."
    O irritated "...Although in reality, it's more of a fan club, with our president gushing over any urban legends posted on the Internet."
    C happy "Hey, c'mon, ghosts are cool! Ever since I was a toddler, I've always wanted to play with one!"
    Y worried2 "Aha..."
    O thinking "*sigh* ...She's my senior by one year, and yet she's never without this child-like enthusiasm...{nw}"

    menu:
        extend ""
        "\"[name_cecilia] is older?!\"":
            Y panicked "[name_cecilia]'s older than you are?!" with shakeonce
            C sad "You're being awfully rude, [name_player]..."
            play ctc_sfx sfx_emoteshout
            show cecilia pout at hop
            C "Wait, you thought I was a child this whole time, didn't you?{nw}" with shakeonce
            menu:
                extend ""
                "\"Yes.\"":
                    Y sad "Well... To be honest..."
                    play ctc_sfx sfx_emotesob
                    C sobbing "Mrgh... I suppose standing next to a stunning beauty like Ria here, I don't stand a chance, huh...?" with hpunch
                    O disappointed "Is it really necessary to have this conversation?"
                    C pout "Oh, don't act like you're not happy to hear the compliment."
                    C wink "You think she's pretty too, right, [name_player]?"
                    Y panicked "Well--{w=1.0}{nw}"
                    O irritated "You don't need to humour her, [name_player]. Let's move on." with shakeonce
                "\"No...\"":
                    Y panicked "N-no, I just figured out of all of us... I-I don't know, [name_oriana] just seemed like... Uh..."
                    O disappointed "...Do you want to finish that sentence?"
                    C smug "Oh, [name_player]... You're a clumsy one, aren't you?"
                    I "...Maybe I didn't need to follow this train of thought..."
        "\"Why is [name_oriana] in the club?\"":
            Y default "You...don't seem to be into the occult as much, huh?"
            O default "....."
            O blink "No. Not even a little."
            Y thinking "Then...why are you in the Occult Club?"
            O irritated "....." with shakeonce
            C smug "......."
            Y default "...?"
            O sideeye "...I have my reasons. It has nothing to do with our current situation."
            Y surprised "O-oh, okay. ...Sorry?"
        "\"Who else is in the Occult Club?\"":
            Y default "Are there others in the club besides you two?"
            O leering "...Does that matter?"
            Y sad "Uh... I don't know, I guess I was just curious...?"
            O thinking "....."
            play ctc_sfx sfx_emotequestion
            C default "We do have a [t_clue]third member[t_cluee], but she's not with us at the moment."
            play ctc_sfx sfx_emoteshout
            O shouting "Cecilia!" with shakeshort
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "Whaaat, it doesn't matter!"
            C smug "Don't mind her, [name_player]. Let's just say that our third member is...a bit of a sensitive subject for Ria here."
            O irritated "....."
            I "The third member..."
            $ d1a4_third_member_mentioned = True
    $ _last_say_who = 'C'
    show cecilia blink at mycenter with move
    show cecilia happy at shudder
    play ctc_sfx sfx_emotehappy
    C "Anyways, that's how we know each other. As you can see, me and Ria are the bestest of friends~ [u_heart]"
    O irritated "....."
    play ctc_sfx sfx_whooshlow
    $ _last_say_who = 'C'
    show cecilia surprised at myright_far with custom_flashquick()
    C "Ahh!{w=0.5}{nw}" with hpunch
    play ctc_sfx sfx_emotesigh
    show cecilia sweatdrop at myright, shrink
    if not d1a4_questioning_clue2:
        extend " ...Aw, guess she's feeling shy right now..."
    else:
        extend " ...Aw, she's STILL feeling shy..."
    show cecilia sweatdrop at myright
    I "Hm..."
    $ d1a4_questioning_clue2 = True
    return

label d1a4_question2A:
    if not d1a4_questioning_clue2A:
        Y sad "Um, so... When Cecilia...died..."
        C smug "That's such a freaky sentence. I love it."
        show cecilia happy at hop
        C "Oh, you can call me \"Cece\" by the way, [name_player]!"
        Y surprised "R-right..."
        I "\"Cece\"... \"See see\"... I guess that's a little easier to say..."
        $ name_cecilia = _("Cece")
    Y sad "Um, so... When Cece...died..."
    $ fadein_sideimage = False
    Y thinking "[name_oriana]... She said something about how Cece is the reason we're trapped here. What does that mean?"
    $ fadein_sideimage = True
    C surprised "Wait, psycho-killer Ria said it like THAT?!" with vpunch
    O blink "...It's exactly what it sounds like."
    O default "It was Cecilia's idea for us to come here."
    play ctc_sfx sfx_emoteshout
    show cecilia pout at doublehop
    C "Oh c'mon, you too?! You make it sound like it was MY idea to put us in a killing game!" with shakeonce
    O irritated "Well, if you recall, I was firmly against it..."
    Y panicked "S-sorry, can you please back up? Why did Cece want all of us to come here?"
    O default "As you know, the two of us are members of the Occult Club."
    O "A couple days ago, our president learned about this legend featuring a haunted house in a mostly abandoned--"
    play ctc_sfx sfx_emotehappy
    show cecilia happy at hop
    stop music fadeout 1.0
    C "\"[t_clue]The Black Magic Mansion[t_cluee]\"!"
    Y annoyed "The...th-the what?"
    $ _last_say_who = 'C'
    show cecilia blink
    pause 0.1
    hide oriana
    show bg diningroom dark
    with dissolve
    show cecilia blink at mycenter with move
    C "Once upon a time, a long time ago, there was an ordinary family living in an ordinary mansion..."
    I "She suddenly started telling a story..."
    play music bgm_awakening
    C "This family was a modest one, having a fair amount of wealth and close ties with the neighbours."
    C "The master of the house in particular was very friendly, and everyone knew how devoted he was to his family."
    C default "But then one day, this sociable man suddenly closed himself off from the world."
    C thinking "Nobody ever saw him or his family again... But they could hear [t_clue]eerie sounds[t_cluee] coming from their house."
    play sound sfx_showeron
    C default "Sounds like scraping metal, flames being{nw}" with vpunch
    play ctc_sfx sfx_flameburst
    extend " waved about..." with hpunch
    C smug "And eventually, [t_clue]unholy things[t_cluee] started happening around the house."
    show cecilia surprised at myleft with hpunch
    C "Some of the neighbours saw strange apparitions and fled for their lives."
    C grin "Those that didn't...came to be controlled like puppets."
    show cecilia sad at myright, shrink with hpunch
    C "They staggered around the surrounding streets, seemingly possessed by something evil..."
    show cecilia blink at myright
    C "And anyone who mistakenly thought they were some drunks and approached them..."
    stop music
    show bg black
    play ctc_sfx sfx_knifeswing
    show cecilia injured at mycenter_zoom with custom_flashquickred()
    C "GOT STABBED!{w=0.3}{nw}" with shakeonce
    play ctc_sfx sfx_knifeslash
    show bg black
    show cecilia determined at mycenter_zoom with custom_flashquickred()
    extend " STRANGLED!{w=0.2}{nw}" with shakeonce
    play sound sfx_introkill_7
    show bg red
    show cecilia creepygrin at mycenter_zoom with custom_flashquickred()
    extend " SKINNED ALIIIIIIIVE!!{w=0.6}{nw}" with shakeshort
    play ctc_sfx sfx_heartbeat_single
    show bg black
    show cecilia grin at mycenter_return
    with custom_flashquick()
    Y afraid "AH!" with shakeshort
    play loop_sfx sfx_heartbeat fadein 3.0
    C blink "...And then, the next morning..."
    show cecilia
    C "The people controlled would wake up from their trances, and see before them..."
    play ctc_sfx sfx_introambiance_sequence2 fadein 0.5
    show bloodsplatter_2 behind cecilia at truecenter:
        alpha 0.0
        pause 0.4
        easeout 4.0 alpha 1.0
    show bloodsplatter_4 behind cecilia at truecenter:
        alpha 0.0
        pause 0.8
        easeout 4.0 alpha 1.0
    show cecilia surprised:
        zoom 1.0 matrixcolor BrightnessMatrix(0.0)
        easeout 5.0 zoom 2.0 ypos 1.8 matrixcolor BrightnessMatrix(-1.0)
    C "{cps=20}...The corpses of those they HORRIBLY SLAUGHTERED--{/cps}{w=1.0}{nw}"
    play ctc_sfx sfx_lightswitch
    hide cecilia
    window auto hide None
    stop loop_sfx
    $ _last_say_who = "O"
    scene bg diningroom
    show cecilia surprised at myright
    show oriana disappointed at myleft
    window auto show None
    O "Okay, that's enough, Cecilia."
    C sad "Aww... Ria, you killjoy."
    C wink "[name_player], did I spook you at least a little bit?{nw}"

    menu:
        extend ""
        "\"Not at all.\"":
            Y blink "No."
            play ctc_sfx sfx_emotesob
            show cecilia sobbing at shrink
            C "No hesitation at all? You're a meanie, [name_player]." with shakeonce
        "\"A little.\"":
            Y sad "...Fine. Maybe a little."
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "Yay!"
        "\"I was about to cry...\"":
            Y worried "...Please don't do that again..." with hpunch
            show cecilia surprised at hop
            C "Oh no! I didn't mean to scare you THAT bad, [name_player]!"
    play music "<from 90.0>music/bgm_truth.ogg" fadein 3.0
    queue music bgm_truth
    O default "...Anyway, Cecilia insisted that the Occult Club check out this \"legend\" in person. See if it's for real."
    O confused "But as soon as we arrived... Well, my memory goes blank from there."
    show cecilia thinking at myright
    C "Yep, me too! I guess the culprit must have nabbed us there and then."
    Y thinking "So then...{nw}"
    $ fadein_sideimage = False
    menu:
        extend ""
        "\"Is our culprit a ghost?\"":
            Y "Could our kidnapper be the man in that legend? Or perhaps one of those apparitions?"
            $ fadein_sideimage = True
            O disappointed "...Are you being serious right now, [name_player]?"
            Y panicked "I mean, wouldn't that explain a lot of things going on here?"
            O leering2 "[name_player]. Listen to yourself. You're suggesting that a {i}ghost{/i} is responsible for trapping us here."
            C smile "And what's wrong with that? All of this could totally be a malevolent spirit's twisted game."
            O annoyed "Ugh... I can't believe I'm the only sane one here..."
            O leering2 "...Okay, look. Say our culprit is indeed a ghost; what would be our plan for stopping it?"
            Y surprised "Uh..."
            $ fadein_sideimage = False
            Y default "....."
            Y thinking "Uh... Cece?"
            $ fadein_sideimage = True
            C thinking "Hmm... I doubt this place will have any tools we could use to perform an exorcism..."
            play ctc_sfx sfx_emotesigh
            show cecilia sweatdrop at shrink
            C "Yeah, if the culprit is actually a ghost, we'd be completely screwed."
            Y worried "...All right, let's scrap that idea, then. Might as well think positively."
            O blink "That's all I'm trying to say, yes."
            I "But still... [t_clue]Black magic[t_cluee], huh...?"
            I "I wonder if that has anything to do with what's been happening to me..."
        "\"Is the legend true?\"":
            Y default "Is the legend true? Were you able to find anything?"
            $ fadein_sideimage = True
            O blink "From a distance, the house was certainly eerie. And the surrounding houses were all empty as well."
            O default "But that could all be easily explained by local weather conditions, real estate trends, and other data."
            O irritated "But our president INSISTED we take the long commute to explore a dangerous part of town by ourselves."
            O "Is it any surprise that we ended up getting kidnapped and forced into this crazy game?"
            C blink "Oh Ria... Sometimes I wonder if your lack of any child-like wonder is the secret to your voluptuous adult figure."
            O "....."
            window auto hide
            play sound sfx_deskslam
            hide cecilia with hpunch
            pause 0.2
            play sound sfx_fallhard
            show oriana irritated with shakeshort
            pause 0.2
            $ show_side_cecilia = True
            C sobbing "Ow..."
            $ show_side_cecilia = False
            I "She kicked her chair out from under her..."
            $ _last_say_who = 'C'
            show cecilia sweatdrop at myright with dissolve
            C "Anyways, [name_player], since we got knocked out just before we were about to enter the house, it's safe to say this place is it."
            C thinking "There's nothing here that indicates anything occult was going on, so it's possible the culprit posted that legend as bait..."
            O default "So to answer your original question, [name_player], us being trapped here is one hundred percent Cecilia's fault."
            C pout "I'll admit to eighty percent. There's no way I could've known THIS would happen."
            I "...So that's the story of how the Occult Club ended up here, huh...?"
            I "But what about me? I'm not part of the club, so how did I end up here...? ...Unless..."
    $ d1a4_questioning_clue2A = True
    return
label d1a4_question2AA:
    Y sad "When, um...[name_oriana] killed Cece..."
    O thinking "....."
    C sad "That's still SO hard to believe..."
    if not d1a4_questioning_clue2AA:
        C default "Oh yeah, [name_player], you can call her Ria, by the way."
        Y surprised "...\"Ria\"?"
        C "Yeah, you know? \"Oriana\"? \"Riana\"? \"Ria\"?"
        Y annoyed "Uhh..."
        O blink "It's not even the worst one she came up with."
        O default "But it's fine, I don't mind if you call me that."
        $ name_oriana = _("Ria")
        Y blink "Okay so... When Ria killed Cece..."
        C blush "See? Doesn't that sentence roll off the tongue better than \"Oriana killed Cece\"?"
        I "I think there're bigger problems with this sentence than pronunciation, but..."
    Y blink "...After we found Cece dead, Ria seemed to...snap."
    $ fadein_sideimage = False
    Y sad "She said a lot of things that made it very clear that...[t_clue]she despises you[t_cluee], Cece."
    $ fadein_sideimage = True
    O irritated "....."
    C smug "Mhhmmm~ Quite the thing to say out loud, [name_player]~"
    Y default "...Ria?"
    O thinking "....."
    C happy "Oh Riaaaa? [name_player] is asking you a questiiiion~ [u_music_note]"
    O sideeyeblink "...I don't have an answer to that."
    O "I've known Cecilia for about a year now, and sure, I have my issues with her but..."
    O sideeye "...I can't say I \"despise\" her, as you put it."
    C grin "....."
    Y sad "O-okay, I guess...you were pretty stressed at the time..."
    I "No thanks to the things I said..."
    O blink "...I'm sorry if you had to see a version of me act in such a disturbing manner."
    O default "But rest assured, you won't see it again."
    I "...It's hard to get that deranged laugh out of my mind, though..."
    play ctc_sfx sfx_emotehappy
    show cecilia happy at doublehop
    C "See, [name_player]? I told ya we're the bestest of friends~ [u_heart]"
    O annoyed "...Tsk." with shakeonce
    I "...Yeah, no, there's definitely some tension there."
    I "But it might not be my place to pry any deeper..."
    $ d1a4_questioning_clue2AA = True
    return

label d1a4_question2AB:
    $ _last_say_who = None
    hide oriana
    show cecilia at mycenter
    with dissolve
    Y leering "Cece. Please be honest with me."
    C surprised "Hmm? What's wrong, [name_player], you look kinda nervous..."
    show cecilia overjoyed at hop
    C "GASP, could this be... Oh, [name_player]~ [u_heart]"
    Y "You're not the culprit responsible for trapping us in here...right?"
    C pout "Aww, that's all you wanted to ask? You got my hopes up..."
    Y sad "Cece, please. I need you to take this seriously."
    $ fadein_sideimage = False
    $ show_side_oriana = True
    O confused "...?"
    $ fadein_sideimage = True
    C default "....."
    C blink "That's right. I'm not the one who trapped us in this house."
    C default "I'm as much of a victim here as you two are."
    I "....."
    I "...I don't think she's lying."
    I "I guess that means [name_oriana] just convinced herself that Cece's the culprit whenever she would kill her..."
    Y sad "Okay. Sorry, I-I know we have enough facts to believe you can't be the culprit, but..."
    C blush "You had to ask! I get it~"
    Y blink "...But there's another issue..."
    C default "Hm?"
    $ renpy.music.set_volume(0.0, 3.0, channel="music")
    Y "...I remember... Each time you killed [name_oriana]... It felt like you were enjoying the situation."
    $ fadein_sideimage = False
    Y leering "Enjoying the sight of [name_oriana] struggling for her life, and...having me choose to kill her myself or not."
    O panicked "...Wha...{w=1.0}{nw}"
    play ctc_sfx "<silence 1.0>"
    extend shouting " WHAT?!" with shakeshort
    O "Are you serious, [name_player]?!" with shakeonce
    $ fadein_sideimage = True
    C blink "....."
    show bg diningroom dark with dissolve
    Y "...Cece. We...can trust you, right?"
    $ fadein_sideimage = False
    O leering2 "....."
    $ fadein_sideimage = True
    C "......."
    C "...Yeah. That certainly sounds like something I might do."
    Y angry "Then--" with shakeonce
    show cecilia pout at doublehop
    C "Hey, hold on there, both of you! All we've talked about are things that happened in other timelines!"
    C "As far as the me right here, right now is concerned, I've never done anything THAT horrible in my whole life!"
    Y sad "That's...true..."
    C sad "*sigh* ...Fine, how about this?"
    C default "[name_player]."
    C blink "I swear to you here and now, with Ria as my witness..."
    C "I won't allow either of you to come into any harm."
    C smile "That's a promise."
    I "......."
    I "...It's strange, but..."
    I "I can feel it. She's serious." with hpunch
    show bg diningroom with dissolve
    Y blink "...Okay. Thanks, Cece."
    C happy "Don't mention it~"
    O annoyed "...Tsk." with shakeonce
    $ _last_say_who = None
    $ show_side_oriana = False
    show cecilia_raw smile as cecilia at mycenter_to_myright, backedaway_on
    pause 0.3
    show oriana annoyed at myleft with dissolve
    show cecilia smile at myright, backedaway_off
    C "Oh? Were you touched by my speech, Ria?"
    O leering2 "...I don't care if it happened in other timelines. What you did was unforgivable."
    C blink "And it's fine you feel that way. You don't have to let that go."
    C default "But going forward, I'll be on your side."
    C blush "And yours too, [name_player]."
    $ renpy.music.set_volume(1.0, 3.0, channel="music")
    $ d1a4_questioning_clue2AB = True
    return

label d1a4_question2B:
    Y thinking "Um... So about the third member of your club..."
    O leering "She's not relevant to our situation."
    C sweatdrop "Oh relaaax, Ria. Let [name_player] finish."
    Y surprised "S-so... The third member...{nw}"
    $ fadein_sideimage = False

    menu:
        extend ""
        "\"What kind of person is she?\"":
            Y default "What kind of person is this third member?"
            $ fadein_sideimage = True
            C thinking "Hmmmmmmmmmmm..."
            O thinking "....."
            C smile "...\"Stubborn\". That word just about sums her up."
            O leering2 "That's a very crude way to describe her."
            Y "But is she interested in the occult?"
            play ctc_sfx sfx_emotehappy
            show cecilia happy at hop
            C "Oh yeah, totally! Definitely way more than Ria here."
            O confused "But since she couldn't make it, she had me join our club president on this excursion..."
            C smug "...Yeah, I wonder what it would've been like if she were caught up in this whole thing...?"
            O leering2 "....."
            C blink "Eh. Not like it matters now."
            C default "[name_player], don't you have other questions you'd rather be asking?"
            I "...Yeah, I guess there's not much point asking about someone who isn't here..."
        "\"Is that person me?\"":
            Y thinking "Is that person...me?"
            $ fadein_sideimage = True
            play ctc_sfx sfx_emotequestion
            O surprised "...What?"
            C surprised "Heh?"
            O confused "Care to explain how you came to such an odd conclusion?{nw}"
            menu:
                "Because of what Cece said" if d1a4_questioning_clue2AB:
                    Y sad "Well, I remember that time when...you two killed each other at the same time..."
                    O irritated "...Of all the versions, I would've liked to forget about that one the most..." with shakeonce
                    C smile "....."
                    $ renpy.music.set_volume(0.0, 3, channel="music")
                    Y leering "When Cece was suffocating on the floor, she looked at me and...I heard her dying words."
                    $ fadein_sideimage = False
                    Y thinking "I think among them was \"Sorry about Ria\"...?"
                    $ fadein_sideimage = True
                    O surprised "...!" with shakeonce
                    C thinking "...So? What's your point?{nw}"

                    menu:
                        extend ""
                        "It was too friendly":
                            $ _last_say_who = None
                            hide oriana
                            show cecilia thinking at mycenter
                            with dissolve
                            Y annoyed "I dunno, it was just...oddly friendly?"
                            C sweatdrop "...And what's strange about that? We'd known each other for a whole evening at that point, right?"
                            C smug "Plus, I'm very sociable, ya know! I can make a friend using only eye contact and body language!"
                            $ show_side_oriana = True
                            O disappointed "....."
                            $ fadein_sideimage = False
                            Y worried "I don't doubt that, but..."
                            Y sad "...I don't know, it felt like you were looking at me as though...I had been a close friend. Definitely longer than one evening."
                            $ fadein_sideimage = True
                        "She used the wrong name":
                            $ _last_say_who = None
                            hide oriana
                            show cecilia thinking at mycenter
                            with dissolve
                            Y leering "You said \"Ria\" when that whole evening, you were calling her \"Oriana\"."
                            C "....."
                            Y thinking "You said it as though...you knew I would be familiar with that nickname."
                            $ fadein_sideimage = False
                            Y "But you've definitely never used it before, and only started now. After I mentioned Ria calling you \"Cece\"."
                            $ show_side_oriana = True
                            O irritated "....."
                            $ fadein_sideimage = True
                            C surprised "...!" with shakeonce
                            play ctc_sfx sfx_emotehappy
                            show cecilia overjoyed at hop
                            C "Niiiice~ That's some solid detective work there, [name_player]!"
                            Y panicked "I-is that all you have to say? How do you explain suddenly using the wrong name?"
                    C thinking "Hmm... Maybe I slipped up because I was delirious from blood loss?"
                    Y leering "You were poisoned."
                    C blink "Then I guess the poison did something to my brain."
                    Y worried "Come on..." with hpunch
                    C sweatdrop "Look, [name_player], I dunno what to tell ya."
                    C default "You're talking about an alternate, future version of me who stabbed someone in the neck, all while choking from rat poison."
                    C sad "Do you really wanna trust the words of someone like that? And this is ME talking."
                    Y "....."
                    $ fadein_sideimage = False
                    Y thinking "[name_oriana]? What do you think?"
                    $ fadein_sideimage = True
                    $ show_side_oriana = False
                    $ _last_say_who = "O"
                    show cecilia_raw sad as cecilia at mycenter_to_myright, backedaway_on
                    pause 0.3
                    show oriana blink at myleft with dissolve
                    O "...For once, I think Cecilia is making perfect sense."
                    O default "That version of her is not only dead, but from a timeline where things played out...chaotically, to say the least."
                    O blink "I wouldn't put much faith in someone like that either."
                    show cecilia at myright, backedaway_off
                    C "....."
                    I "...Why?"
                    play ctc_sfx sfx_emotequestion
                    I "Why can't I shake this feeling that...they're still [t_clue]hiding something[t_cluee] from me?" with shakeonce
                    $ renpy.music.set_volume(1.0, 3, channel="music")
                "Because of the Occult Club" if d1a4_questioning_clue2A:
                    Y thinking "You said earlier that the Occult Club came here to check out that legend. And this whole area is...mostly abandoned, right?"
                    $ fadein_sideimage = False
                    Y default "Then the most plausible reason I'm here and stuck alongside you two is because...I came with you guys..."
                    $ fadein_sideimage = True
                    C blink "...Yeah, that's a reasonable conclusion to make."
                    O blink "....."
                    O "...I'm sorry, but..."
                    if input_name == "Cecilia" or input_name == "Oriana":
                        O default "There is only one person named \"[name_player]\" in the Occult Club."
                    else:
                        O default "There is nobody named \"[name_player]\" in the Occult Club."
                    O "You are a [t_clue]stranger[t_cluee] to us."
                    Y sad "...! I...I see..." with shakeonce
                    C default "....."
                    I "Yeah... I guess that makes sense..."
                    I "I mean, if I really was part of their club, why wouldn't they tell me as soon as I woke up?"
                "\"I don't know...\"":
                    Y worried "...Never mind. Sorry, I guess that was kind of a weird question..."
                    C smug "....."
                    O thinking "...No, it's fine. I'm sorry for reacting so harshly."
                    if not d1a4_questioning_clue2AB:
                        I "[name_cecilia]'s giving me a weird look..."
                        I "Something tells me I'm not too far off here... Maybe I [t_clue]need more information[t_cluee] first?"
                    O default "Anything else you want to ask?"
    $ d1a4_questioning_clue2B = True
    return

label d1a4_question3:
    Y sad "So what's been happening to me? Why am I constantly going back to the beginning of this day?"
    O thinking "That's...not something we can answer. What you've been through defies all common sense."
    C smug "But Ria, what about...you-know-what?"
    C blink "Clearly, you don't have any choice but to keep an open mind here..."
    O irritated "But if that's true, then there's actually [t_clue]no hope for us[t_cluee]..."
    if not d1a4_questioning_clue1:
        I "...What are they talking about...?"
        I "...Maybe I should [t_clue]ask something else first[t_cluee] before coming back to this question..."
        return
    else:
        I "Is that supposed to be whispering...? I can hear them...{nw}"

        menu:
            extend ""
            "No more secrets":
                pass
        Y leering "There's no reason for you two to keep secrets from me anymore, right? Are you sure nothing comes to mind?"
        O blink "....."
        O "...You mentioned that your memories of a day end whenever one of us dies, correct?"
        O default "That must be the [t_clue]trigger[t_cluee] that sends you backwards in time."
        C thinking "But isn't that the same trigger for opening the front door? Seems like a rigged game..."
        O thinking "But if you recall what [name_player] said, there's always the SOUND of the door opening..."
        show cecilia happy at hop
        C "Ooh, what if the door is what's causing you to go back in time?"
        C smug "After all, it's never been YOU who died, right, [name_player]?"
        Y sad "That's..." with shakeonce
        O confused "But that would mean the two of us should also be going back in time."
        O "After all, according to [name_player], there were some instances where one of us survived and even left first."
        C thinking "That's true... I guess we've no reason to believe this game's rigged, then..."
        Y surprised "So it's really just {i}me{/i} traveling back in time? No one else remembers going through all this before?"
        O default "It is just you, yes."
        C default "For us, there's just been two weird things. First, waking up here with no way out..."
        C smug "...And now you, saying things you can't possibly know without being a real time traveler."
        Y sad "But then...where is this power coming from...?"
        O thinking "....."
        C thinking "....."
        if not d1a4_questioning_clue2A:
            I "...Ugh, there's gotta be something I'm missing here..."
            play ctc_sfx sfx_emotequestion
            I "I should [t_clue]ask something else[t_cluee] and come back to this question later."
            return
        else:
            I "Wait... What did [name_cecilia] finish sharing with us earlier...?{nw}"
            menu:
                extend ""
                "The Black Magic Mansion":
                    pass
            Y thinking "...Maybe it could have something to do with that legend?"
            C "\"The Black Magic Mansion\"?"
            C surprised "Ooooh, you think black magic could be causing your time traveling? Hmm..."
            O leering2 "We're living in the 21st century. This isn't hundreds of years ago where everything was signed off as magic."
            C smug "Oh yeah, I'm sure there's a scientific reason for why [name_player] is time traveling. Pft."
            O irritated2 "...Even if there are supernatural elements at play here, I'm sure there's a logical ruleset to everything. That's all I'm saying."
            C happy "Yeah, that's what I think too!"
            C sweatdrop "But until we narrow down [t_clue]what type of black magic[t_cluee] it is, my occult knowledge won't help us out yet."
            I "The type...?"
            C default "Actually, on that note... So you don't have any control over your time traveling, right, [name_player]?"
            Y thinking "No... I've never even seen the front door open, even though I always HEAR it opening."
            C blink "Interesting... That's a bit of a problem then."
            Y surprised "A problem?"
            C thinking "I mean, if you keep traveling back in time whenever one of us dies..."
            $ renpy.music.set_volume(0.0, 3, channel="music")
            C default "How will {i}you{/i} ever get to leave this place?"
            Y afraid "...!" with shakeshort
            O surprised "That's..." with shakeonce
            show bg diningroom:
                matrixcolor BrightnessMatrix(0.0)
                linear 5.0 matrixcolor BrightnessMatrix(-1.0)
            show oriana surprised:
                alpha 1.0
                linear 1.0 alpha 0.0
            show cecilia blink at myright:
                easein 3.0 xalign 0.5
            C blink "Another thing I noticed, in all your time travel tales, not a single one ends with {i}you{/i} being killed."
            C grin "Which begs the question: what happens if YOU die? Do you still go back in time?"
            I "....."
            C creepygrin "...Well, [name_player]? Aren't you just a teeny-tiny bit curious?"
            Y shocked "I..." with shakeonce
            play ctc_sfx "<silence 1.0>"
            hide oriana
            show bg diningroom dark:
                matrixcolor BrightnessMatrix(0.0)
            show oriana irritated at myleft
            show cecilia grin at myright
            with custom_flashquick()
            O "Stop. That's enough, Cecilia."
            O "After everything [name_player]'s been through, we..."
            O thinking "...We just can't do that." with shakeonce
            C default "....."
            C blink "Fair enough."
            I "....."
            show bg diningroom with dissolve
            C thinking "I suppose our only option is to just find an actual way out of here."
            C sad "But [name_player], from everything you remember, there isn't any other exit, now is there...?"
            Y sad "Mrgh..." with shakeonce
            O irritated "....."
            I "Come on, think, was there really no way to get outside...?"
            I "....."
            I ".......Wait."
            I "There was one thing we never finished talking about...!" with shakeonce
            I "But I guess if we're gonna go looking for him, I'll need to [t_clue]end my questioning[t_cluee]..."
            $ renpy.music.set_volume(1.0, 3, channel="music")
            $ d1a4_questioning_clue3 = True
            return
label d1a4_questioning_end:
    scene bg black with dissolvemed
    scene bg diningroom
    with dissolvemed
    show oriana at myleft_fadein
    show cecilia at myright_fadein
    stop music fadeout 3.0
    call save_file_name_update (1, "d1a4_questioning_end")
    I "...I guess that's enough questions for now..."
    I "Boy, this ended up being a long discussion..." with hpunch
    show cecilia surprised:
        alpha 1.0
    C "How do you feel, [name_player]? Was that too much for you?"
    Y blink "N-no, I'm fine. Everything you guys told me makes perfect sense with what I remember..."
    I "But...I still feel like there're so many details I'm missing..."
    I "Like my memories from {i}before{/i} all this... I'm still basically an [t_clue]amnesiac[t_cluee]..."
    Y thinking "So...neither of you know who I am, right?"
    C happy "Nope!"
    show oriana thinking:
        alpha 1.0
    O "...No, sorry."
    Y sad "...I see..."
    play ctc_sfx sfx_emotesigh
    show cecilia sweatdrop at shrink
    C "Aww, don't look so sad, [name_player]!"
    show cecilia blink at reset, myright
    C "As far as I'm concerned, you're an honorary member of the Occult Club until we get out of here!"
    C smile "That means we're on your side to the bitter end! President's orders! Right, Ria?"
    O blink "....."
    Y surprised "....."
    O embarrassed "Y-yes, of course. {size=-10}...Don't look at me like that...{/size}"
    C blush "Oh Ria... You're so adorable. [u_heart]"
    window auto hide
    $ _last_say_who = None
    show bg black with dissolvemed
    I "...It's no use, I can't remember..."
    I "I don't think either of them realize this, but..."
    window auto hide
    hide oriana
    hide cecilia
    show oriana_raw embarrassed at myleft, backedaway_on:
        matrixcolor SaturationMatrix(0.0)
    show cecilia_raw blush at myright, backedaway_on:
        matrixcolor SaturationMatrix(0.0)
    with dissolve
    pause 1.0
    scene bg black
    with blot_in
    pause 0.5
    play loop_sfx sfx_heartbeat
    I "If I'm not part of the Occult Club, then [t_clue]how did I end up here[t_cluee]?"
    I "The only explanation is the culprit captured me from some other, distant place..."
    I "Or maybe... Have I...always been inside this house?"
    I "But then...wouldn't that mean that I'm..." with shakeonce
    play ctc_sfx sfx_emotequestion
    stop loop_sfx
    show bg diningroom
    show oriana shadow at myleft
    show cecilia at myright

    O "...Heh..." with hpunch
    Y wince "...?"
    O "Pft..." with shakeonce
    show bg black with custom_flashquick()
    O laughing "PffhehahaHAHAHAHAHAA~" with shakelong
    Y panicked "[name_oriana]?!" with shakeonce
    C surprised "Oh no, she's lost it!" with shakeonce
    I "...No, wait. It's just this again."
    show bg diningroom
    show oriana panicked at doublehop
    O "AGH! S-something just brushed along my leg!" with shakeonce
    show cecilia thinking at crouch
    C "Hmm? What's down here..."
    show cecilia surprised at standup
    pause 0.25
    play ctc_sfx sfx_emotehappy
    show cecilia overjoyed at hop
    C "...Oh, a puppy!"
    $ _last_say_who = None
    show dog_raw at mycenter with moveinbottom
    I "There he is. The dog."
    C default "Looks like...a black poodle? I don't really know dog breeds."
    O "Wh-wha..."
    O "Whawhawhawha..." with shakeonce
    I "Wait for it..."
    play ctc_sfx sfx_fallsoft
    hide oriana
    hide dog_raw
    play music bgm_comedy
    $ show_side_oriana = True
    O overjoyed "WHAT IS THIS PRECIOUS CREATUUUURE?! [u_heart]" with shakeshort
    I "Aaaand there it is again."
    play ctc_sfx sfx_emotehappy
    O sobbing "[u_heart] OHMERGOSH ISSOOOOO FLOOFFYYY~ [u_heart] I could just dig my face in dis FLOOFY LI'L BELLY~ [u_heart]{w=0.5}{nw}" with shakeonce
    play ctc_sfx "<silence 1.0>"
    $ fadein_sideimage = False
    extend " *SNIFFFFFFF*" with shakeshort
    Y relaxed "...Heh..."
    $ fadein_sideimage = True
    $ _last_say_who = "C"
    show cecilia at mycenter with move
    C surprised "Hmm? [name_player], you don't look very surprised at Ria's doggy antics."
    Y confused "Yeah, because I've seen this before. Like...a lot of times."
    C smug "Oh yeah! Time traveler, doyyy~"
    play ctc_sfx sfx_emotehappy
    O overjoyed "EEEEEEEEEEEEEEE, IT'S GOT THE CUDDIWIEST WITTLE PAW PAAADS~ [u_music_note] Squishy squish squish~" with shakeshort
    C default "So [name_player], you know this dog?"
    Y surprised "Yeah. Well... Not his real name or why he's here."
    $ fadein_sideimage = False
    Y thinking "All I know is we always met him here, [name_oriana] would get super attached, and we'd give him a temporary name."
    Y surprised "If I recall, the name we came up with was, uhh..."
    $ fadein_sideimage = True
    $ show_side_oriana = False
    scene bg black with dissolve
    show dog_raw at mycenter with dissolve
    jump dogname_select

label dogname_select:
    I "The dog's name was...{nw}"

    menu:
        extend ""
        "Cerberus":
            $ input_name_dog = "Cerberus"
            $ name_dog = "{color=#606060}"+input_name_dog+"{/color}"
            jump dogname_confirmed
        "Shaggy":
            $ input_name_dog = "Shaggy"
            $ name_dog = "{color=#606060}"+input_name_dog+"{/color}"
            jump dogname_confirmed
        "Make up a new one":

            jump dogname_entry

label dogname_entry:
    $ quick_menu = False
    $ music_info = False
    $ input_name_dog = renpy.input("ВВЕДИТЕ ИМЯ ДЛЯ {size=+15}{color=#606060}СОБАКИ{/color}{/size}", exclude={'[', ']', '{', '}'}, pixel_width=250)
    $ quick_menu = True
    $ music_info = True


    $ input_name_dog = input_name_dog.strip()

    if input_name_dog == input_name:
        I "...Nah, that's gonna get confusing. Let's try something else.{nw}"

        menu:
            extend ""
            "Enter a new name":
                jump dogname_entry
            "Go back to the lame names":
                jump dogname_select
    elif input_name_dog == "" or input_name_dog == "Dog":
        I "...I guess if I can't be original, I should stick with one of the existing options.{nw}"
        menu:
            extend ""
            "Enter a new name":
                jump dogname_entry
            "Go back to the lame names":
                jump dogname_select
        jump dogname_entry
    else:
        $ name_dog = "{color=#606060}"+input_name_dog+"{/color}"
        I "...[name_dog]..."
        I "Will [name_dog] be good?{nw}"
        menu:
            extend ""
            "\"Yep.\"":
                jump dogname_confirmed
            "\"No, let's pick something else...\"":
                I "Nah, let's try another name...{nw}"
                menu:
                    extend ""
                    "Enter a new name":
                        jump dogname_entry
                    "Go back to the lame names":
                        jump dogname_select
label dogname_confirmed:
    scene bg diningroom
    show cecilia at mycenter
    with fade
    Y default "Right, it was \"[name_dog]\"."
    if name_dog == "{color=#606060}Cerberus{/color}":
        play ctc_sfx sfx_emotesigh
        show cecilia sweatdrop at shrink
        C "Eh? Really? Isn't that kind of a cringey name for a dog?"
        I "You were the one who came up with that name..."
        show cecilia at mycenter_to_myright
        show oriana happy at myleft with dissolve
    elif name_dog == "{color=#606060}Shaggy{/color}":
        play ctc_sfx sfx_whooshlow
        show oriana overjoyed at myleft
        show cecilia surprised at myright
        O "[name_dog]! What a spectacular name for a dog with such gorgeously curled fur! Excellent choice, [name_player]!" with shakeshort
        I "You were the one who came up with that name..."
    else:
        C thinking "...[name_player]?"
        C smug "You thought of that name just now, didn't you?"
        Y sad "N-no, that's definitely the name we all came up with." with hpunch
        C smile "Hmmmmmmmmmm...?"
        C blink "Alrighty, then~"
        $ _last_say_who = None
        show cecilia at mycenter_to_myright
        show oriana happy at myleft with dissolve

    Y blink "Anyways, now that [name_dog] is here..."
    $ fadein_sideimage = False
    Y thinking "[name_oriana], you noticed that he's cold to the touch, right?"
    $ fadein_sideimage = True
    if not d1a4_questioning_clue2AA:
        show cecilia smile at reset, myright
        C "Pst, [name_player]. You can just call her \"Ria\"."
        C wink "I mean, isn't \"Oriana\" kinda fancy for a girl shoving her face into a dog belly?"
        Y surprised "...I mean, I guess if you insist..."
        O "...?"
        Y thinking "Ria, you noticed that [name_dog]'s fur feels cold, right?"
        $ name_oriana = _("Ria")

    O surprised "Now that you mention it, I suppose so."
    O sobbing "It's not a bad sensation, though..." with hpunch
    Y worried "That's...not my point."
    stop music fadeout 3.0
    $ fadein_sideimage = False
    Y leering "My point is that it's possible [name_dog] came in from the outside."
    $ fadein_sideimage = True
    show cecilia surprised at reset, myright
    C "Oh?"
    O thinking "Just because he's cold? There are plenty of other possible explanations for that..."
    Y blink "It's not just that. There's also the fact that the dog's here in the first place."
    C blink "Ooooh, I see where you're going with this."
    C smile "If this dog belongs to the culprit, why would they leave it here...right?"
    play music bgm_discussion
    Y default "Exactly."
    O confused "Come to think of it... [name_player], you mentioned that I would always find a hidden [t_clue]key[t_cluee] in the master bedroom upstairs, right?"
    O default "If it isn't for any of the other locked doors, and considering its smaller size..."
    C thinking "Are you thinking the key is related to some pet door?"
    O blink "No, I can't imagine anyone ever needing a lock involving a key for something pet-related."
    O thinking "I'm just thinking if [name_dog] snuck inside this house somehow..."
    O default "This house might have at least one secret passageway. Perhaps even one hidden with a tiny keyhole...?"
    Y blink "I see... So you're saying we should check every surface carefully for keyholes."
    C sad "Uh, guys? Not that I don't love your optimism or anything, but..."
    C thinking "It's totally possible that [name_dog] snuck in through a passageway only a dog could fit through."
    O confused "That's fine. If we can just find that passageway, we'll send [name_dog] through it with a message for help."
    play ctc_sfx sfx_emotesigh
    show cecilia sweatdrop at shrink
    C "A-a message...? Are you serious?"
    O sideeyeblink "But ultimately... I think in order for us to get out of here for good..."
    O sideeye "We'll need to get inside the locked room next to this one."
    play sound sfx_flashback
    scene bg foyer at grayscale_on with custom_flashbulblong()
    pause 1.0
    scene bg foyer at grayscale_on:
        zoom 1.2 xalign 0.25 yalign 1.0
        easein 9.0 zoom 1.5
    with dissolve
    pause 1.0
    Y surprised "The one that's most likely a [t_clue]living room[t_cluee] or something, right?"
    $ fadein_sideimage = False
    $ show_side_oriana = True
    $ show_side_cecilia = True
    O default "Yes. You said that you never saw the inside of that room."
    O thinking "There must be something important being kept from us in there. Who knows, we might even find the culprit."
    C thinking "If that room's so important, can't we just bust the door down?"
    O disappointed "You already tried that, and it didn't work."
    C grin "Hrm... Then how about we burn it down?"
    Y thinking "The stove doesn't work, and there aren't any lighters."
    O irritated "More importantly, we'd burn the whole house down, and us with it."
    play ctc_sfx sfx_emotehappy
    C happy "But also the culprit! Sure, we'd all die, but it'd be a real explosive ending! Don't you think, [name_player]?" with vpunch
    play ctc_sfx sfx_emotesigh
    Y worried "I mean... I have no plans to burn to death anytime soon..." with hpunch
    O annoyed2 "Will it kill you to take this seriously for a moment?" with shakeonce
    $ _last_say_who = None
    $ fadein_sideimage = True
    $ show_side_oriana = False
    $ show_side_cecilia = False
    stop music fadeout 3.0
    scene bg black with dissolvemed
    scene bg diningroom
    show oriana at myleft
    show cecilia at myright
    with dissolvemed
    O "In any case, let's not waste any more time and start searching."
    show dog at mycenter with moveinbottom
    D "....." with shakeonce
    O surprised "Er, wait, actually, let's eat first. [name_dog] probably came here because he's hungry."
    show cecilia
    C happy "Yeah, that sounds good to me. How about you, [name_player]?"
    Y relaxed "Yeah, that's...{w=0.8}{nw}"
    play ctc_sfx sfx_heartbeat_single
    window auto hide None
    $ fadein_sideimage = False
    scene bg diningroom dark at wobble, blurring with custom_flashquick()
    window auto show None
    extend pained " Nrgh!" with shakeshort
    $ show_side_oriana = True
    $ show_side_cecilia = True
    C surprised "[name_player]! Oh no, I think you've reached your limit..."
    O leering2 "It must be mental fatigue from all that time traveling..."
    Y troubled "I'm...fine..." with shakeonce
    C pout "Nope, you're definitely not fine. Let's get you to bed."
    O thinking "Just go upstairs and use the master bedroom to sleep. We'll take care of everything else."
    play ctc_sfx sfx_heartbeat_single
    show bg diningroom dark at wobble:
        blur 30
    I "...Argh..." with shakeshort
    I "Y-yeah, I'd better just do as they say..."
    window auto hide
    $ fadein_sideimage = True
    $ show_side_oriana = False
    $ show_side_cecilia = False
    scene bg black with dissolvemed
    scene bg diningroom
    show oriana at myleft_fadein
    show cecilia smug at myright_fadein
    with dissolvemed
    C "I'll handle dinner, Ria. We wouldn't want you getting anywhere near our food..."
    O irritated "Sure, and I can hold on to the knife. Who knows, I might find a use for it later..."
    Y worried "...Um... Maybe I should stick around after all...?" with hpunch
    C happy "We're just joking around, [name_player]! Seriously, go get some sleep~"
    O sideeyeblink "We'll be fine. Go take a well-deserved rest."
    Y worried "...Okay. Good night..."
    C smile "Night, [name_player]!"
    O sideeye "Good night."
    scene bg black with dissolvemed
    pause 0.5
    scene bg foyer with dissolvemed
    pause 1.0
    I "....."
    I "We still haven't solved anything but..."
    I "At least this time, I'm pretty sure that [t_clue]no one will die tonight[t_cluee]."
    I "Let's hope...we can keep it that way..."
    I "....."
    scene bg frontdoor with dissolvemed
    pause 1.0
    Y troubled "...Yep... The writing...updated..."
    I "We have less than [t_clue]20 hours[t_cluee]..."
    window auto hide
    pause 1.0
    scene bg black with dissolveslow
    pause 1.0
    I "....."
    I "If we run out of time..."
    I "If we end up in real danger... What would I do...?{nw}"

    menu:
        extend ""
        "Kill one of them":
            I "....."
            I "I...don't want to die..."
            I "I...I hope it doesn't come down to that..."
        "Sacrifice myself":
            I "....."
            window auto hide
            show cecilia_raw at myright
            show oriana_raw at myleft
            with dissolvemed
            I "...If it comes down to that, then..."
            show cecilia_raw blush
            show oriana_raw thinking
            I "I'll do it. And...I'm sure I'll have no regrets."
            scene bg black with dissolveslow
        "Have everyone die together":
            I "....."
            I "...No..." with hpunch
            I "We can't lose hope. Either all of us get out, or..."
            I "...Or..."
    I "......."
    I "I'm...so tired..."
    I "I guess...I'll sleep after all..."
    I "It's okay... [t_clue]Morning[t_cluee]...will definitely come this time..."
    play ctc_sfx "<silence 1.0>"
    I "...I'm winning this [t_clue]killing game[t_cluee]...{w=0.5}{nw}"
    play ctc_sfx "<silence 1.0>"
    $ this_inst_is_demo = is_demo_version()
    extend " No matter what." with hpunch
    scene bg black
    pause 3.0
    play sound [sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime, sfx_clockchime]
    show screen lock_hotkeys
    $ quick_menu = False
    pause 3.0
    scene cg eyecatch cecilia bloody:
        xalign 0.5 yalign 0.5 zoom 1.1
        easein 3.0 zoom 1.0
    with dissolvemed
    pause 1.0
    scene cg eyecatch cecilia with dissolvemed
    show chaptertitle1_end_text:
        xpos 1300 xanchor 0.5 yalign 0.5 alpha 0.0 zoom 1.0
        linear 1.0 alpha 1.0
    show chaptertitle1_end_subtext:
        xpos 1300 xanchor 0.5 yalign 0.57 alpha 0.0
        linear 1.0 alpha 1.0
    pause 4.0
    scene bg black with dissolveslow
    pause 1.0
    hide screen lock_hotkeys
    $ quick_menu = True

label day1_end:
    pause 1.0
    if this_inst_is_demo:
        stop sound
        show cg keyvisual side with dissolve
        call screen end_of_demo() 

        pause 1.0
        if is_demo_version():
            jump day1_end
    $ this_inst_day1_clear = True
    $ this_inst_is_demo = False
    S "Continuing [name_player]'s [t_clue]killing game[t_cluee] to {color=#fff}Part II{/color}.{w=1.0}\nPlease remember to save your progress regularly.{nw}"

    menu:
        extend ""
        "Continue":
            window auto hide
            $ renpy.block_rollback()
            show screen lock_hotkeys
            $ quick_menu = False
            $ music_info = False
            pause 2.0
            play sound sfx_chapterintro
            scene cg eyecatch oriana bloody at wobble
            show chaptertitle2_text:
                xpos 550 xanchor 0.5 yalign 0.5 alpha 0.0 zoom 1.0
                pause 3.0
                parallel:
                    linear 1.0 alpha 1.0
                parallel:
                    linear 1.5 matrixcolor BrightnessMatrix(0.0)
                    linear 1.5 matrixcolor BrightnessMatrix(0.5)
                    repeat
            show chaptertitle2_subtext:
                xpos 550 xanchor 0.5 yalign 0.57 alpha 0.0
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
            jump d2a1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
