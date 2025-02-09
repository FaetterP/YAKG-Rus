define tutorials = [
    {
        "index": "controls",
        "title": _("Controls"),
        "desc": _("This game can be played with a mouse, a keyboard, or a gamepad.\nVisit {a=showmenu:help}{color=#3366CC}{u}Help{/u}{/color}{/a} ([t_hotkey]F1[t_hotkeye] or [t_ctrlkey]Back/-[t_ctrlkeye]) to learn all controls and shortcuts!"),
        "thumbnail_file": "tutorial_controls_thumbnail",
        "button_text": _("NEXT")
    },
    {
        "index": "save1",
        "title": _("The Game Menu"),
        "desc": _("[t_hotkey]Esc[t_hotkeye], [t_hotkey]Right Click[t_hotkeye], or [t_ctrlkey]Start/+[t_ctrlkeye] will open the game menu. From\nhere, you can [t_clue]save your progress[t_cluee] and view various other screens."),
        "thumbnail_file": "thumbnails/tutorial_save.png",
        "button_text": _("CLOSE")
    },
    {
        "index": "save2",
        "title": _("Saving and Loading"),
        "desc": _("Use [t_clue]Save[t_cluee] to bookmark moments in the story you'd like to revisit.\nUse [t_clue]Load[t_cluee] to resume the story from your manual saves and [t_clue]autosaves[t_cluee]."),
        "thumbnail_file": "thumbnails/tutorial_save2.png",
        "button_text": _("CLOSE")
    },
    {
        "index": "autosaves",
        "title": _("Autosaves"),
        "desc": _("[t_clue]Autosaves[t_cluee] are usually created before you make choices. Only the\nmost recent are available, so don't neglect your manual saves!"),
        "thumbnail_file": "thumbnails/tutorial_autosaves.png",
        "button_text": _("CLOSE")
    },
    {
        "index": "investigations",
        "title": _("Investigations"),
        "desc": _("Move the cursor to search your surroundings for important clues.\nOnce you find enough, you will be able to advance the story."),
        "thumbnail_file": "thumbnails/tutorial_investigations.png",
        "button_text": _("CLOSE")
    },
    {
        "index": "anotherkillinggame",
        "title": _("Another Killing Game"),
        "desc": _("By rejecting a bloody fate, you have started [t_clue]another killing game[t_cluee].\nWitness every fate on a [t_clue]single save file[t_cluee] to uncover the truth..."),
        "thumbnail_file": "thumbnails/tutorial_anotherkillinggame.png",
        "button_text": _("CLOSE")
    },
    {
        "index": "rollback",
        "title": _("Rollback Unlocked (1/2)"),
        "desc": _("You feel a mysterious power surging from deep within... Use the\nBack button ([t_hotkey]R[t_hotkeye] or [t_ctrlkey]Left Trigger[t_ctrlkeye]) to rewind the current scene."),
        "thumbnail_file": "thumbnails/tutorial_rollback.png",
        "button_text": _("NEXT")
    },
    {
        "index": "rollback2",
        "title": _("Rollback Unlocked (2/2)"),
        "desc": _("The power of Rollback lets you quickly explore other dialogue\nroutes and [t_clue]undo any selections[t_cluee] you make by mistake!"),
        "thumbnail_file": "thumbnails/tutorial_rollback2.png",
        "button_text": _("CLOSE")
    },
    {
        "index": "skip",
        "title": _("Skipping Read Text"),
        "desc": _("Any text already seen can be skipped with the Skip button. You\ncan also use [t_hotkey]Ctrl[t_hotkeye], [t_ctrlkey]Right Trigger[t_ctrlkeye], and other shortcuts (see {a=showmenu:help}{color=#3366CC}{u}Help{/u}{/color}{/a})."),
        "thumbnail_file": "thumbnails/tutorial_skip.png",
        "button_text": _("CLOSE")
    },
    {
        "index": "support",
        "title": _("THANK YOU!"),
        "desc": _("A webpage has been opened on your browser!"),
        "thumbnail_file": None,
        "button_text": _("CLOSE")
    }
]
image tutorial_controls_thumbnail = ConditionSwitch("rollback_unlocked", "thumbnails/tutorial_controls.png", "not rollback_unlocked", "thumbnails/tutorial_controls_locked.png")

screen tutorial(tutorial_name, from_menu=False):
    modal True
    frame:
        at show_hide_dissolve
        xalign 0.5 yalign 0.5 xpadding 50 ypadding 25
        has vbox
        xalign 0.5
        spacing 20
        for tut in tutorials:
            if tut["index"] == tutorial_name:
                label tut["title"]:
                    text_style "tutorial_title"
                    xalign 0.5
                if tut["thumbnail_file"] is not None:
                    add tut["thumbnail_file"]
                else:
                    null height -50
                text tut["desc"]:
                    outlines [(2, "#000000")]
                    xalign 0.5
                    size 32
                button:
                    xalign 0.5
                    xsize 300 ysize 80
                    background "gui/button/confirm_idle_background.png"
                    hover_background "gui/button/confirm_hover_background.png"
                    text tut["button_text"]:
                        style "confirm_button_text"
                    if from_menu:
                        action Hide()
                    else:
                        action Return()
                null height 4
                break

style tutorial_title:
    font "fonts/Changa-SemiBold.ttf"
    color gui.accent_color
    outlines [(2, "#000000")]
    size 60
style tutorial_help_button:
    ysize 32
style tutorial_help_button_text:
    size 32

screen tutorials_help():
    default tutorial_to_display = "controls"
    hbox:
        style_prefix "tutorial_help"
        vbox:
            spacing 16

            textbutton _("Controls") action SetLocalVariable("tutorial_to_display", "controls")
            textbutton _("The Game Menu") action SetLocalVariable("tutorial_to_display", "save1")
            textbutton _("Saving and Loading") action SetLocalVariable("tutorial_to_display", "save2")
            textbutton _("Autosaves") action SetLocalVariable("tutorial_to_display", "autosaves")
            textbutton _("Investigations") action SetLocalVariable("tutorial_to_display", "investigations")
            if rollback_unlocked:
                textbutton _("Another Killing Game") action SetLocalVariable("tutorial_to_display", "anotherkillinggame")
                textbutton _("Rollback Unlocked (1/2)") action SetLocalVariable("tutorial_to_display", "rollback")
                textbutton _("Rollback Unlocked (2/2)") action SetLocalVariable("tutorial_to_display", "rollback2")
            textbutton _("Skipping Read Text") action SetLocalVariable("tutorial_to_display", "skip")
        null width 50
        use tutorial_to_display_content(tutorial_to_display)

screen tutorial_to_display_content(tutorial_to_display=""):
    vbox:
        if tutorial_to_display == "":
            xalign 0.5 yalign 0.5
            text _("Select a tutorial!"):
                outlines [(2, "#000000")]
        else:
            xalign 0.5 yoffset -30
            for tut in tutorials:
                if tut["index"] == tutorial_to_display:
                    text tut["title"]:
                        style "tutorial_title"
                        xalign 0.5
                    null height -12
                    text tut["desc"]:
                        font "fonts/AveriaSerifLibre-Regular.ttf"
                        outlines [(2, "#000000")]
                        xalign 0.5
                        size 30
                    null height 24
                    add tut["thumbnail_file"]
                    break

screen new_game_language():
    frame:
        at show_hide_dissolve
        xalign 0.5 yalign 0.5 xpadding 50 ypadding 25
        has vbox
        xalign 0.5
        spacing 20
        vbox:
            xalign 0.5

            label _("Choose Language")
            textbutton "English" action Language(None) xalign 0.5
            textbutton "Japanese" action None xalign 0.5
        button:
            xalign 0.5
            xsize 300 ysize 80
            background "gui/button/confirm_idle_background.png"
            hover_background "gui/button/confirm_hover_background.png"
            text _("PROCEED"):
                style "confirm_button_text"
            action Return()
        null height 20

screen new_game_darken_flashes():
    frame:
        at show_hide_dissolve
        xalign 0.5 yalign 0.5 xpadding 50 ypadding 25
        has vbox
        xalign 0.5
        spacing 20
        null height 20
        text _("This game has mild flashing visual effects."):
            xalign 0.5
            size 32
        text _("You can reduce their brightness by turning on \"Darken Flashes\"."):
            xalign 0.5
            size 24
        button:
            xalign 0.5
            style "check_button"
            if persistent.darken_flashes:
                text _("Darken Flashes - ON"):
                    color gui.accent_color
                    size 36
            else:
                text _("Darken Flashes - OFF"):
                    color gui.idle_color
                    hover_color gui.hover_color
                    size 36
            action ToggleField(persistent, "darken_flashes")
        text _("You can change this setting and others at any time in {size=+10}{a=showmenu:preferences}Config{/a}{/size}."):
            xalign 0.5
            size 24
        button:
            xalign 0.5
            xsize 300 ysize 80
            background "gui/button/confirm_idle_background.png"
            hover_background "gui/button/confirm_hover_background.png"
            text _("PROCEED"):
                style "confirm_button_text"
            action Return()
        null height 4

screen end_of_demo():
    frame:
        at show_hide_dissolve
        xalign 0.85 yalign 0.5 xpadding 50 ypadding 25
        xsize 700
        has vbox
        xalign 0.5
        if is_demo_version():
            text _("DEMO CLEAR!"):
                font "fonts/Changa-SemiBold.ttf"
                color gui.accent_color
                size 60
                xalign 0.5
            text _("Thank you for playing the demo of\nYet Another Killing Game!"):
                xalign 0.5
                text_align 0.5
                size 32
            null height 24
            text _("Any save files created in this demo can be loaded in the full version of the game."):
                xalign 0.5
                text_align 0.5
                size 32
            null height 24
            text _("For information on how to play the full version, visit this {a=https://linktr.ee/yakg}{color=#3366CC}{u}webpage{/u}{/color}{/a}."):
                xalign 0.5
                text_align 0.5
                size 32
            null height 24
            text _("Please remember to {size=+10}{a=showmenu:save}Save{/a}{/size}\nbefore closing this demo."):
                xalign 0.5
                text_align 0.5
                size 32
        else:
            text _("DEMO CLEAR!"):
                font "fonts/Changa-SemiBold.ttf"
                color gui.accent_color
                size 60
                xalign 0.5
            text _("Thank you for purchasing the full version of YAKG!"):
                xalign 0.5
                text_align 0.5
                size 32
            null height 24
            text _("Are you ready to continue the story?"):
                xalign 0.5
                text_align 0.5
                size 32
            null height 24
            button:
                xalign 0.5
                xsize 300 ysize 80
                background "gui/button/confirm_idle_background.png"
                hover_background "gui/button/confirm_hover_background.png"
                text _("LET'S GO!"):
                    style "confirm_button_text"
                action Return()
        null height 24

screen load_in_demo_error_screen():
    frame:
        at show_hide_dissolve
        xalign 0.5 yalign 0.5 xpadding 50 ypadding 25
        has vbox
        xalign 0.5
        text _("WHOOPS!"):
            font "fonts/Changa-SemiBold.ttf"
            color gui.accent_color
            size 60
            xalign 0.5
        text _("You're trying to load a save file from the full version of the game..."):
            xalign 0.5
            text_align 0.5
            size 32
        null height 24
        text _("Please exit this demo and load this file with the full version of the game."):
            xalign 0.5
            text_align 0.5
            size 32
        null height 24
        button:
            xalign 0.5
            xsize 300 ysize 80
            background "gui/button/confirm_idle_background.png"
            hover_background "gui/button/confirm_hover_background.png"
            text _("MAIN MENU"):
                style "confirm_button_text"
            action Return()
        null height 24
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
