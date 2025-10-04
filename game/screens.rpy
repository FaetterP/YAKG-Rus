init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    activate_sound "sound/sfx_select.ogg"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

    activate_sound "audio/sound/sfx_select.ogg"
    selected_base_bar Frame("gui/scrollbar/vertical_selected_bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    selected_thumb Frame("gui/scrollbar/vertical_selected_thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

    activate_sound "audio/sound/sfx_select.ogg"
    selected_base_bar Frame("gui/slider/horizontal_selected_bar.png", gui.slider_borders, tile=gui.slider_tile)
    selected_thumb "gui/slider/horizontal_selected_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "say"



    window:
        id "window"

        if who is not None:

            window:

                at namebox
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"














    on "show" action [Function(set_mouse_cursor_type), SetVariable('ctc_timer', 0), SetVariable("show_quick_menu", False), SetVariable("mouse_on_music_info", False)]





    if not renpy.variant("small"):
        if grayscale_sideimage:
            if fadein_sideimage:
                add SideImage() at sideimage_fadein, grayscale_on
            else:
                add SideImage() at sideimage, grayscale_on
        else:
            if fadein_sideimage:
                add SideImage() at sideimage_fadein
            else:
                add SideImage() at sideimage

    if GamepadExists() and show_quick_menu and quick_menu:
        vbox:
            at transform_dissolvein(0.3, 0.0)
            style_prefix "gamepad_help_ui"
            xalign 1.0 yalign 1.0
            hbox:
                xalign 1.0
                spacing 12
                if config.rollback_enabled and renpy.can_rollback():
                    text _("{outlinecolor=#cccc00}(LS/LT) Back{/outlinecolor}")
                text _("(RS) Music")
                if renpy.is_seen():
                    text _("(RT) Skip")
                else:
                    text _("{outlinecolor=#0000007f}{color=#8888887f}(RT) Skip{/color}{/outlinecolor}")
                null width 6
            null height -14
            hbox:
                xalign 1.0
                spacing 12
                text _("(X) Auto")
                text _("(Y) Log")
                text _("(-) Help")
                text _("(+) Menu")
                null width 6
            null height 10




style gamepad_help_ui_text:
    yalign 0.5
    font "fonts/Changa-SemiBold.ttf"
    color "#000"
    outlines [(2, "#888")]
    size 24

style data_hider_outlines:
    outlines [(2, "#000000")]

transform date_hider:
    alpha 1.0
    pause 5.0
    linear 1.0 alpha 0.0

transform namebox:
    rotate -3 zoom 0.95 alpha 0.75 ypos -138 xpos 520
    easein 0.25 zoom 1.0 alpha 1.0 ypos -143 xpos 520

transform sideimage:
    xalign 0.0 yalign 1.0
    xsize 450 ysize 450
    alpha 1.0
transform sideimage_fadein:
    xalign 0.01 yalign 1.0
    xsize 450 ysize 450
    alpha 0.0 zoom 0.95
    easein 0.3 xalign 0.0 alpha 1.0 zoom 1.0


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default:
    line_leading 8
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True

    yalign 1.0
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

image namebox_dynamic = ConditionSwitch(
    "renpy.is_seen()", "gui/namebox seen.png",
    
    "not renpy.is_seen()", "gui/namebox.png")

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("namebox_dynamic", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")


    xpos 412
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False











screen input(prompt):
    style_prefix "input"

    window:
        at show_hide_dissolve
        style "nvl_window"
        style_prefix "choice"
        has vbox
        xsize 1000
        xalign 0.5 yalign 0.5
        spacing 70
        text prompt xalign 0.5 yalign 0.5
        input id "input" xalign 0.5 yalign 0.5
        button:
            xalign 0.5 yalign 0.5
            xsize 300 ysize 80
            background "gui/button/confirm_idle_background.png"
            hover_background "gui/button/confirm_hover_background.png"
            text _("PROCEED"):
                yoffset -4
                style "confirm_button_text"
            action GetText("input","input")











style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width









default choice_sensitive = False

screen choice(items):
    sensitive choice_sensitive
    timer 0.5 action SetVariable("choice_sensitive", True)

    if show_choicegrand:
        if mute_choice:
            on "show" action Play("ctc_sfx", "<silence 1.0>")
        if config.developer:
            on "show" action SetVariable("choice_sensitive", True)
        else:
            on "show" action SetVariable("choice_sensitive", False)
        style_prefix "choicegrand"
        vbox:
            at transform_dissolvein(0.5, 0.0)
            yalign 0.5
            spacing 5
            if show_choicekarma:
                for i in items:
                    textbutton i.caption action [i.action, Function(narrator.add_history, kind="adv", who=__(""), what=__("{font=fonts/Alkalami-Regular.ttf}< {/font}" + __(i.caption) + "{font=fonts/Alkalami-Regular.ttf} >{/font}"))] at anim_choice_button:
                        idle_background "gui/button/choicekarma_idle_background.png"
                        hover_background "gui/button/choicekarma_hover_background.png"
            else:
                for i in items:
                    textbutton i.caption action [i.action, Function(narrator.add_history, kind="adv", who=__(""), what=__("{font=fonts/Alkalami-Regular.ttf}< {/font}" + __(i.caption) + "{font=fonts/Alkalami-Regular.ttf} >{/font}"))] at anim_choice_button:
                        idle_background "gui/button/choicegrand_idle_background.png"
                        hover_background "gui/button/choicegrand_hover_background.png"
                        if not mute_choice:
                            activate_sound "sound/sfx_choicegrand.ogg"
    else:
        if config.developer:
            on "show" action [Play("ctc_sfx", ("sound/sfx_menu_appear.ogg" if not mute_choice else "<silence 1.0>")), SetVariable("choice_sensitive", True)]
        else:
            on "show" action [Play("ctc_sfx", ("sound/sfx_menu_appear.ogg" if not mute_choice else "<silence 1.0>")), SetVariable("choice_sensitive", False)]
        style_prefix "choice"



        vbox:
            at transform_dissolvein(0.5, 0.0)
            yalign 0.5
            spacing 5
            for i in items:
                if " (disabled)" in i.caption:
                    $ caption = i.caption.replace(" (disabled)", "")
                    textbutton caption action None at disabled_choice_button
                else:
                    textbutton i.caption action [i.action, Function(narrator.add_history, kind="adv", who=__(""), what=__("{font=fonts/Alkalami-Regular.ttf}< {/font}" + __(i.caption) + "{font=fonts/Alkalami-Regular.ttf} >{/font}"))]:
                        if choice_sensitive:
                            at anim_choice_button
                        else:
                            at disabled_choice_button
                        if i == items[0]:
                            default_focus True
                        if not mute_choice:
                            activate_sound "sound/sfx_choice.ogg"

transform anim_choice_button:
    xalign 0.5
    on hover:
        easein 0.2 zoom 1.0
    on idle:
        linear 0.1 zoom 0.9
transform disabled_choice_button:
    xalign 0.5 zoom 0.9

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 105
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    xsize 1313
    ysize 120

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    yalign 0.7

style choicegrand_vbox is vbox
style choicegrand_button is button
style choicegrand_button_text is button_text

style choicegrand_vbox:
    xalign 0.5
    ypos 105
    yanchor 0.5

    spacing gui.choice_spacing

style choicegrand_button is default:
    properties gui.button_properties("choice_button")
    xsize 1576
    ysize 144

style choicegrand_button_text is default:
    properties gui.text_properties("choice_button")
    font "fonts/AveriaLibre-Regular.ttf"
    size 48
    yalign 0.4






transform quick_menu_custom_button_transform:
    alpha 0.0
    on insensitive:
        matrixcolor BrightnessMatrix(-0.3)
        yoffset 0



        block:
            pause (0.0 if show_idle_quick_menu() else 9.0)
            easein 0.3 alpha (1.0 if show_idle_quick_menu() else 0.0)






            repeat
    on idle:
        matrixcolor BrightnessMatrix(-0.3)
        yoffset 0
        block:
            pause (0.0 if show_idle_quick_menu() else 9.0)
            easein 0.3 alpha (1.0 if show_idle_quick_menu() else 0.0)
            repeat
    on hover:
        matrixcolor BrightnessMatrix(0.0)
        alpha 1.0
        yoffset 0
        easein 0.1 yoffset -12
        linear 0.1 yoffset -10
screen quick_menu_custom_button(btn_text, btn_action, icon_name, special=None):
    if special == "log":
        textbutton btn_text action btn_action alternate [MouseMove(renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1])] at quick_menu_custom_button_transform:
            keysym ["mousedown_4", "K_l"]
            if not mouse_on_quick_menu and not preferences.afm_enable == True and not renpy.is_skipping():
                hovered SetVariable("show_quick_menu", True)
                if show_quick_menu:
                    unhovered [SetVariable('ctc_timer', 0), SetVariable("show_quick_menu", False)]
            idle_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
            hover_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
    elif special == "skip" or special == "back":
        textbutton btn_text action btn_action alternate MouseMove(renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1]) at quick_menu_custom_button_transform:
            activate_sound "sound/sfx_select.ogg"
            if not mouse_on_quick_menu and not preferences.afm_enable == True and not renpy.is_skipping():
                hovered SetVariable("show_quick_menu", True)
                if show_quick_menu:
                    unhovered [SetVariable('ctc_timer', 0), SetVariable("show_quick_menu", False)]
            idle_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
            hover_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
            insensitive_background im.Scale("gui/quick/"+icon_name+"_insensitive.png", 62, 37)
    else:
        textbutton btn_text action btn_action alternate MouseMove(renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1]) at quick_menu_custom_button_transform:
            if special == "auto":
                activate_sound "sound/sfx_select.ogg"
            if not mouse_on_quick_menu and not preferences.afm_enable == True and not renpy.is_skipping():
                hovered SetVariable("show_quick_menu", True)
                if show_quick_menu:
                    unhovered [SetVariable('ctc_timer', 0), SetVariable("show_quick_menu", False)]
            idle_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
            hover_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
            insensitive_background im.Scale("gui/quick/icon_quickload_insensitive.png", 62, 37)
screen auto_active_custom_button(btn_text, btn_action, icon_name):
    textbutton btn_text action btn_action alternate MouseMove(renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1]):
        yoffset -10
        activate_sound "sound/sfx_select.ogg"
        text_style "quick_button_auto_text"
        idle_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
        hover_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
screen skip_active_custom_button(btn_text, btn_action, icon_name):
    textbutton btn_text action btn_action alternate MouseMove(renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1]):
        yoffset -10
        activate_sound "sound/sfx_select.ogg"
        text_style "quick_button_skip_text"
        idle_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
        hover_background im.Scale("gui/quick/"+icon_name+".png", 62, 37)
        insensitive_background im.Scale("gui/quick/"+icon_name+"_insensitive.png", 62, 37)
screen quick_menu():
    zorder 100
    mousearea:
        xysize (1000, 150)
        xalign 0.5 yalign 1.0
        hovered [SetVariable("show_quick_menu", True), SetVariable("mouse_on_quick_menu", True)]
        unhovered [SetVariable('ctc_timer', 0), SetVariable("show_quick_menu", False), SetVariable("mouse_on_quick_menu", False)]
    if quick_menu:
        key "pad_y_press" action ShowMenu('history')

        hbox:
            style_prefix "quick"
            xalign 0.5 yalign 1.0 spacing 20 yoffset 20
            if persistent.legacy_renpy:
                use quick_menu_custom_button(_("BACK"), Rollback(), "icon_back", special="back")
                use quick_menu_custom_button(_("LOG"), ShowMenu('history'), "icon_log", special="log")
                if renpy.is_skipping() == False:
                    use quick_menu_custom_button(_("SKIP"), Skip(), "icon_skip", special="skip")
                else:
                    use skip_active_custom_button(_("SKIP"), Skip(), "icon_skip")
                if preferences.afm_enable == False:
                    use quick_menu_custom_button(_("AUTO"), Preference("auto-forward", "toggle"), "icon_auto", special="auto")
                else:
                    use auto_active_custom_button(_("AUTO"), Preference("auto-forward", "toggle"), "icon_auto")
                use quick_menu_custom_button(_("SAVE"), ShowMenu('save'), "icon_save")
                use quick_menu_custom_button(_("LOAD"), ShowMenu('load'), "icon_load")
                use quick_menu_custom_button(_("Q.SAVE"), QuickSave(), "icon_quicksave")
                use quick_menu_custom_button(_("Q.LOAD"), QuickLoad(), "icon_quickload")
                use quick_menu_custom_button(_("CONFIG"), ShowMenu('preferences'), "icon_config")
            else:
                use quick_menu_custom_button(_("LOG"), ShowMenu('history'), "icon_log", special="log")
                use quick_menu_custom_button(_("SAVE"), ShowMenu('save'), "icon_save")
                use quick_menu_custom_button(_("LOAD"), ShowMenu('load'), "icon_load")
                use quick_menu_custom_button(_("CONFIG"), ShowMenu('preferences'), "icon_config")
                if preferences.afm_enable == False:
                    use quick_menu_custom_button(_("AUTO"), Preference("auto-forward", "toggle"), "icon_auto", special="auto")
                else:
                    use auto_active_custom_button(_("AUTO"), Preference("auto-forward", "toggle"), "icon_auto")
                if renpy.is_skipping() == False:
                    use quick_menu_custom_button(_("SKIP"), Skip(), "icon_skip", special="skip")
                else:
                    use skip_active_custom_button(_("SKIP"), Skip(), "icon_skip")
                use quick_menu_custom_button(_("BACK"), Rollback(), "icon_back", special="back")


        timer 1.0 repeat True action SetVariable('ctc_timer', ctc_timer + 1.0)
        if ctc_timer >= 20.0:
            timer 1.0 repeat True action SetVariable("show_quick_menu",True)


















init python:
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("music_info")


default quick_menu = True
default show_quick_menu = False
default mouse_on_quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:


    xsize 62
    ysize 75
    yalign 0.0

style quick_button_text:

    size 18
    xalign 0.5
    color "#ffffff00"
    hover_color "#ffffff"
    hover_outlines [(2, "#000000")]
    yoffset 10

style quick_button_auto_text is quick_button_text:
    color gui.accent_color
    hover_color gui.accent_color
    outlines [(2, "#000000")]
    yoffset 10

style quick_button_skip_text is quick_button_text:
    color gui.accent_color
    hover_color gui.accent_color
    outlines [(2, "#000000")]
    yoffset 10










screen navigation():
    on "show" action Function(set_mouse_cursor_type)
    on "hide" action Function(set_mouse_cursor_type, use_default=False)

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            if renpy.newest_slot() is not None:
                textbutton _("Continue{#menu}") action Confirm(_("{size=+20}WELCOME BACK!{/size}\nReady to [t_clue]CONTINUE[t_cluee] the killing game?"), yes=Continue()):
                    activate_sound "sound/sfx_save.ogg"
                textbutton _("New Game") action Confirm(_("{size=+10}Begin a [t_clue]NEW[t_cluee] killing game?{/size}\n{color=#ff0000}Your progress in {/color}Continue{color=#ff0000} may be lost.{/color}"), yes=Start()):
                    activate_sound "sound/sfx_save.ogg"
                textbutton _("Load") action ShowMenu("load")

            else:

                textbutton _("{size=+20}START{/size}") action Start()

        else:
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")

        null height 30

        if not main_menu:
            textbutton _("Status") action ShowMenu("pause")
            textbutton _("Log") action ShowMenu("history")




        textbutton _("Help") action ShowMenu("help")

        textbutton _("Config") action ShowMenu("preferences")

        textbutton _("About") action ShowMenu("about")

        if main_menu and renpy.newest_slot() is not None and not is_demo_version():
            textbutton _("Gallery") action ShowMenu("gallery_main")

        if renpy.newest_slot() is not None and not is_demo_version():
            textbutton _("Achievements") action ShowMenu("bobcachievements")

        if main_menu:
            null height 30
            textbutton _("Credits") action Confirm(_("View YAKG's [t_clue]Credits[t_cluee]?"), yes=Start("main_menu_credits"))
            textbutton _("Support YAKG!") action [OpenURL("https://linktr.ee/yakg"), Show("tutorial", tutorial_name="support", from_menu=True)]

        null height 30

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("Return to Title") action MainMenu()

        if renpy.variant("pc"):


            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    ysize 50

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    hover_color "#fff"
    outlines [(2, "#000000")]
    xalign 0.5








screen main_menu():
    tag menu



    add gui.main_menu_background
    add "logo" at titlefloat

    frame:
        style "main_menu_frame"



    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"
            spacing -18




            text _("Ver. [config.version]"):
                style "main_menu_version"
            text "{size=-12}[u_copyright] 2025 Jun Kakeru{/size}":
                style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    outlines [(2, "#000000")]

style main_menu_version:
    properties gui.text_properties("version")
    color "#fff"
    outlines [(2, "#000000")]











screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background



    on "show" action Play("audio", "sound/sfx_gamemenu_open.ogg")
    on "hide" action Play("audio", "sound/sfx_gamemenu_close.ogg")

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"






            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    spacing spacing

                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    spacing spacing

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Close"):
        style "return_button"
        activate_sound None
        keysym 'pad_b_press'
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            if _preferences.language == "japanese":
                null height 24
            text _("Ver. [config.version!t] | [u_copyright] 2025 Jun Kakeru\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text:
    size 24
    line_spacing 0
    font "fonts/AveriaSerifLibre-Regular.ttf"
    outlines [(1, "#000000")]

style about_label_text:
    size gui.label_text_size

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    color "#508ef2"










screen save():
    tag menu


    use file_slots(_("Save"))




screen load():
    tag menu


    use file_slots(_("Load"))



screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}: My Saves"), auto=_("Autosaves"), quick=_("Quick Saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                yoffset -24
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value
                    outlines [(2, "#000000")]

            if title == _("Save"):
                text _("Select a slot to {color=#508ef2}save{/color} your current progress in."):
                    xalign 0.5 yoffset 50
                    outlines [(2, "#000000")]
            elif title == _("Load"):
                text _("Choose a save to {color=#d93838}load{/color} and resume a playthrough."):
                    xalign 0.5 yoffset 50
                    outlines [(2, "#000000")]


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        activate_sound "sound/sfx_save.ogg"

                        has vbox

                        fixed:
                            fit_first True
                            add FileScreenshot(slot) xalign 0.5
                            if title == _("Load"):
                                add "gui/quick/icon_load.png" at load_hover_icon_transform
                            elif title == _("Save"):
                                add "gui/quick/icon_save.png" at save_hover_icon_transform
                        text FileSaveName(slot, empty=_("Empty Slot")):
                            style "slot_name_text"
                        text FileTime(slot, format=_("{#file_time}%B %d, %Y | %H:%M")):
                            style "slot_time_text"


                        key "save_delete" action FileDelete(slot)


            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    if persistent.legacy_renpy:
                        textbutton _("<") action FilePagePrevious()

                    if persistent.legacy_renpy:
                        if config.has_autosave:
                            textbutton _("{#auto_page}A") action FilePage("auto")

                        if config.has_quicksave:
                            textbutton _("{#quick_page}Q") action FilePage("quick")
                    else:
                        if config.has_autosave:
                            textbutton _("{#auto_page}Autosaves"):
                                if not persistent.seen_tutorial_autosaves:
                                    action [FilePage("auto"), Show("tutorial", tutorial_name="autosaves", from_menu=True), SetVariable("persistent.seen_tutorial_autosaves", True)]
                                else:
                                    action FilePage("auto")

                    textbutton " | " action None


                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    if persistent.legacy_renpy:
                        textbutton _(">") action FilePageNext(max=9)
                        textbutton " | " action None

                        if config.has_sync:
                            if CurrentScreenName() == "save":
                                textbutton _("Upload Sync"):
                                    action UploadSync()
                                    xalign 0.5
                            else:
                                textbutton _("Download Sync"):
                                    action DownloadSync()
                                    xalign 0.5

transform load_hover_icon_transform:
    xsize 100 ysize 60 xoffset 0 alpha 0.0
    xalign 1.0
    on insensitive:
        linear 0.2 alpha 0.0
    on idle:
        linear 0.2 alpha 0.0
    on hover:
        yalign 0.5 alpha 0.0
        easein 0.35 yalign 0.05 alpha 0.75
transform save_hover_icon_transform:
    xsize 100 ysize 60 xoffset 0 alpha 0.0
    xalign 1.0
    on insensitive:
        linear 0.2 alpha 0.0
    on idle:
        linear 0.2 alpha 0.0
    on hover:
        yalign 0.5 alpha 0.0
        easeout 0.2 yalign 0.95 alpha 0.75
        linear 0.075 xsize 120 ysize 40 xoffset 10
        linear 0.075 xsize 100 ysize 60 xoffset 0
style page_label is gui_label:
    xpadding 75
style page_label_text:
    font "fonts/Alkalami-Regular.ttf"
    size 48
    layout "subtitle"
    hover_color "#cccc00"
    color "#fff"
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text:

    hover_color "#fff"
    size 15
    yoffset -10
style slot_name_text is slot_button_text:
    hover_color "#fff"
    size 25
    line_spacing -20

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")
    hover_color "#fff"
    outlines [(2, "#000000")]

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")









screen preferences():
    tag menu


    use game_menu(_("Config"), scroll="viewport"):

        vbox:

            hbox:

                spacing 0
                vbox:
                    style_prefix "check"
                    label _("Gameplay")
                    if _preferences.language == "japanese":
                        null height 12
                    textbutton _("Skip Unseen Text") action Preference("skip", "toggle") tooltip __("{size=+10}Skip Unseen Text{/size}\nAllows \"Skip\" controls to skip through text you have {color=#ff0000}NOT{/color} read yet.")
                    textbutton _("Skip After Choices") action Preference("after choices", "toggle") tooltip __("{size=+10}Skip After Choices{/size}\nAllows \"Skip\" to stay active after selecting choices or clues in Investigations.")
                    textbutton _("Skip Transitions") action InvertSelected(Preference("transitions", "toggle")) tooltip __("{size=+10}Skip Transitions{/size}\nSkips all transitions and most image animations.")
                vbox:
                    if _preferences.language == "japanese":
                        null height 12
                    style_prefix "check"
                    label ""
                    textbutton _("Darken Flashes") action ToggleField(persistent, "darken_flashes") tooltip __("{size=+10}Darken Flashes{/size}\nLowers the brightness of flash transitions and effects.")
                    textbutton _("Use Ren'Py Features") action [ToggleField(persistent, "legacy_renpy"), Function(toggle_rollback)] tooltip __("{size=+10}Use Ren'Py Features{/size}\nEnables Rollback, Quick Saves, Sync, and a familiar quick menu layout {color=#ff3eff}for players used to Ren'Py{/color}.")
                null width 76
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        if _preferences.language == "japanese":
                            null height 12
                        textbutton _("Window{#preference}") action Preference("display", "window") selected not preferences.fullscreen
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    if _preferences.language == "japanese":
                        null height 12
                    textbutton "English" action Confirm(_("{font=fonts/Changa-SemiBold.ttf}Switch the game language to English?{/font}\n{font=tl/japanese/fonts/Corporate-Logo-Bold-ver3.otf}言語を英語に変更しますか？{/font}\n{font=fonts/Changa-SemiBold.ttf}This might cause {color=#ff0000}text glitches{/color} on old saves.{/font}\n{font=tl/japanese/fonts/Corporate-Logo-Bold-ver3.otf}古いセーブでは{color=#ff0000}テキストの不具合{/color}が起きる可能性があります。{/font}"), yes=Language(None))
                    textbutton "{font=tl/japanese/fonts/05HomuraM-SemiBold.otf}日本語{/font}" action Confirm(_("{font=fonts/Changa-SemiBold.ttf}Switch the game language to Japanese?{/font}\n{font=tl/japanese/fonts/Corporate-Logo-Bold-ver3.otf}言語を日本語に変更しますか？{/font}\n{font=fonts/Changa-SemiBold.ttf}This might cause {color=#ff0000}text glitches{/color} on old saves.{/font}\n{font=tl/japanese/fonts/Corporate-Logo-Bold-ver3.otf}古いセーブでは{color=#ff0000}テキストの不具合{/color}が起きる可能性があります。{/font}"), yes=Language("japanese"))
                    textbutton "Русский" action Confirm(_("{font=fonts/Changa-SemiBold.ttf}Изменить язык игры на русский?{/font}\n{font=fonts/Changa-SemiBold.ttf}This might cause {color=#ff0000}text glitches{/color} on old saves.{/font}\n{font=fonts/Changa-SemiBold.ttf}Это может вызвать {color=#ff0000}проблемы с текстом{/color} в старых сохранениях.{/font}"), yes=Language("russian"))



            null height (1 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    spacing 0
                    label _("Text Speed")
                    hbox:
                        label _("Slow"):
                            xsize 80 right_margin 10
                            text_style "slider_label_left"
                        bar value Preference("text speed") tooltip __("{size=+10}Text Speed{/size}\nAdjust the speed at which normal dialogue text prints on the screen.")
                        label _("Fast"):
                            xsize 80 left_margin 10
                            text_style "slider_label_right"

                    label _("Auto-Forward Delay")
                    hbox:
                        label _("Short"):
                            xsize 80 right_margin 10
                            text_style "slider_label_left"
                        bar value Preference("auto-forward time") tooltip __("{size=+10}Auto-Forward Delay{/size}\nAdjust the amount of time before dialogue advances while using \"Auto\".")
                        label _("Long"):
                            xsize 80 left_margin 10
                            text_style "slider_label_right"

                    label _("Skip Speed")
                    hbox:
                        label _("Slow"):
                            xsize 80 right_margin 10
                            text_style "slider_label_left"
                        bar value FieldValue(persistent,"skip_delay",step=1.0,offset=10,range=150,action=SetField(config,"skip_delay",persistent.skip_delay)) bar_invert True alt _("Skip Speed"):
                            style "slider_slider"
                            tooltip __("{size=+10}Skip Speed{/size}\nAdjust the speed at which \"Skip\" controls advance through dialogue text.")
                        label _("Fast"):
                            xsize 80 left_margin 10
                            text_style "slider_label_right"

                vbox:
                    if config.has_music:
                        if _preferences.get_volume('music') > 0.0:
                            label _("Music Volume")
                        else:
                            label _("Music Volume{image=gui/icon_mute.png}")

                        hbox:
                            bar value Preference("music volume")
                    if _preferences.language == "japanese":
                        null height 24
                    if config.has_sound:

                        if _preferences.get_volume('sfx') > 0.0:
                            label _("Sound Volume")
                        else:
                            label _("Sound Volume{image=gui/icon_mute.png}")

                        hbox:
                            bar value Preference("sound volume") released Play("sound", config.sample_sound)





                    if _preferences.language == "japanese":
                        null height 24
                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                    textbutton _("Restore Defaults") tooltip __("{size=+10}Restore Defaults{/size}\nRevert all text and volume sliders to default values."):
                        foreground None
                        action Confirm(_("Restore all sliders to their default values?"), yes=Function(restore_default_sliderprefs))
                        style "mute_all_button"


            null height 80

            hbox:
                $ tooltip = GetTooltip()
                xfill True
                xalign 0.5
                if tooltip:
                    text "[tooltip]":
                        size 28
                        text_align 0.5
                        xalign 0.5
                        outlines [(2, "#000000")]

style slider_label_left:
    font "fonts/Alkalami-Regular.ttf"
    size 24
    xalign 1.0
    color gui.accent_color
    outlines [(2, "#000000")]

style slider_label_right:
    font "fonts/Alkalami-Regular.ttf"
    size 24
    xalign 0.0
    color gui.accent_color
    outlines [(2, "#000000")]

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text:
    outlines [(2, "#000000")]
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text:
    outlines [(2, "#000000")]
style check_button is gui_button
style check_button_text is gui_button_text:
    size 28
    yoffset 5
style check_vbox is pref_vbox

style slider_label is pref_label:
    bottom_margin 0
style slider_label_text is pref_label_text:
    outlines [(2, "#000000")]
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    size 32
    yalign 1.0

style pref_vbox:

    xsize 300

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")
    font "fonts/AveriaSerifLibre-Regular.ttf"
    hover_color "#fff"
    outlines [(2, "#000000")]
    size 34

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")
    font "fonts/AveriaSerifLibre-Regular.ttf"
    hover_color "#fff"
    outlines [(2, "#000000")]

style slider_slider:
    xsize 385
    yoffset 12

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675










screen history():
    tag menu



    predict False

    use game_menu(_("Log"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                label what:
                    style "history_text"
                    if "color" in h.what_args:
                        text_color h.what_args["color"]
                    elif h.who == "":
                        style "history_choice_text"
                        text_color gui.accent_color





        if not _history_list:
            label _("The dialogue log is empty.")




define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art", "i", "font", "size", "color", "style_clue" }


style history_window is empty

style history_name is gui_label

style history_name_text:
    font "fonts/Alkalami-Regular.ttf"
    size 36
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


style history_choice_text:
    xalign 0.5
    ypos 20
style history_choice_text_text:
    font "fonts/Alkalami-Regular.ttf"







screen help():
    tag menu


    default device = "tutorials"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            if _preferences.language == "japanese":
                spacing 18
            else:
                spacing 6

            hbox:

                textbutton _("Tutorials") action SetScreenVariable("device", "tutorials") default_focus True
                textbutton "|" action None

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
            if _preferences.language == "japanese":
                null height 10
            if device == "tutorials":
                use tutorials_help
            elif device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates selected buttons.")

    hbox:
        label _("Space")
        text _("Advances dialogue only.")

    if config.rollback_enabled:
        hbox:
            label _("R, Page Up"):
                text_color "cccc00"
            text _("Uses the power of Rollback to turn back time.")

    hbox:
        label _("Arrow Keys")
        text _("Navigates visible buttons.")

    hbox:
        label _("Escape")
        text _("Pauses the game by opening the game menu.")

    hbox:
        label "F1"
        text _("Opens the Help screen.")

    hbox:
        label "L"
        text _("Opens the Log screen.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")





    hbox:
        label "A"
        text _("Toggles auto-forward.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "M"
        text _("Toggles the music information panel.")

    hbox:
        label "F, F11"
        text _("Toggle fullscreen or windowed mode.")

    hbox:
        label "Del"
        text _("Delete the currently selected save file.")

    hbox:
        label "Alt+V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Alt+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates hovered buttons.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Pauses the game by opening the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Opens the Log screen.")










screen gamepad_help():

    hbox:
        label _("A / Bottom Button")
        text _("Advances dialogue and activates selected buttons.")

    hbox:
        label _("B / Right Button")
        text _("Advances dialogue only. Skips dialogue while held down.")

    hbox:
        label _("X / Left Button")
        text _("Toggles auto-forward.")

    hbox:
        label _("Y / Top Button")
        text _("Opens the Log screen.")

    hbox:
        label _("Right Trigger")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Right Shoulder")
        text _("Toggles the music information panel.")

    if config.rollback_enabled:
        hbox:
            label _("Left Trigger,\nLeft Shoulder"):
                text_color "cccc00"
            text _("Uses the power of Rollback to turn back time.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigates visible buttons.")

    hbox:
        label _("Left Stick Click,\nRight Stick Click")
        text _("Hides the user interface.")

    hbox:
        label _("Start (+), Guide")
        text _("Pauses the game by opening the game menu.")

    hbox:
        label _("Back (-)")
        text _("Opens the Help screen.")





    textbutton _("Calibrate Gamepad") action GamepadCalibrate():
        xalign 0.5


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text:
    outlines [(2, "#000000")]
style help_text is gui_text:
    outlines [(2, "#000000")]

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")
    hover_color "#fff"
    outlines [(2, "#000000")]

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0















screen confirm(message, yes_action, no_action):

    on "show" action Function(set_mouse_cursor_type)
    on "hide" action Function(set_mouse_cursor_type, use_default=False)


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png" at show_hide_dissolve

    frame at show_hide_dissolve:

        has vbox
        xalign .5
        yalign .5
        spacing 25

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        vbox:
            xalign 0.5

            textbutton _("YES") action yes_action:
                xsize 300 ysize 80
                idle_background "gui/button/confirm_green_idle_background.png"
                hover_background "gui/button/confirm_green_hover_background.png"
            null height 10

            textbutton _("NO") action no_action:
                xsize 300 ysize 80
                idle_background "gui/button/confirm_red_idle_background.png"
                hover_background "gui/button/confirm_red_hover_background.png"


    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")
    size 32
    hover_size 36









screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        has hbox
        spacing 9
        null width 4
        text _("SKIPPING"):
            if _preferences.language == "japanese":
                yoffset 4
        null width 4

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle":
            if _preferences.language == "japanese":
                yoffset -16
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle":
            if _preferences.language == "japanese":
                yoffset -16
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle":
            if _preferences.language == "japanese":
                yoffset -16


transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size 48

style skip_triangle:


    font "DejaVuSans.ttf"
    ypos 12









screen notify_location(message, unlocked=True):
    vbox:
        at show_hide_dissolve
        style_prefix "notify_location"

        xalign 0.5
        if _preferences.language == "japanese":
            null height 18
        if not unlocked:
            text _("{color=#cccc00}Новая локация{/color}") at notify_new_location_transform
            if _preferences.language == "japanese":
                null height 8
            else:
                null height -40
        else:
            null height 12
        text "{size=+20}[message!tq]{/size}" at notify_location_transform

    timer 6.5 action Hide('notify_location')

style notify_location_text:
    font "fonts/Changa-SemiBold.ttf"
    outlines [(2, "#000000")]

transform notify_location_transform:
    alpha 0.0 yoffset -30
    easein 1.0 alpha 1.0 yoffset 5
    pause 5.0
    linear 0.5 alpha 0.0

transform notify_new_location_transform:
    xalign 0.5 yalign 0.5
    matrixcolor BrightnessMatrix(0.0)
    alpha 0.0
    pause 1.0
    easein 0.5 alpha 1.0
    linear 0.25 matrixcolor BrightnessMatrix(1.0)
    linear 0.75 matrixcolor BrightnessMatrix(0.0)
    pause 3.5
    linear 0.5 alpha 0.0


screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 2.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")











screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}







style pref_vbox:
    variant "medium"
    xsize 675



screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
