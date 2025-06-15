transform pac_prompt_transform:
    xalign 0.5 yalign 1.0
    ease 1.5 yalign 0.98
    ease 1.5 yalign 1.0
    repeat

transform pac_title_transform:
    xalign 0.5 yalign 0.02
    ease 1.5 yalign 0.05
    ease 1.5 yalign 0.02
    repeat

transform pac_endbutton_transform:
    xalign 0.94 yalign 1.0 zoom 0.8
    easein 0.5 xalign 0.95 yalign 0.96 zoom 1.02
    linear 0.1 zoom 1.0
    block:
        yalign 0.96
        pause 1.0
        ease 0.2 yalign 0.97 matrixcolor BrightnessMatrix(0.0)
        ease 0.2 yalign 0.95 matrixcolor BrightnessMatrix(0.5)
        ease 0.2 yalign 0.96 matrixcolor BrightnessMatrix(0.0)
        pause 4.0
        repeat

transform pac_sprite_transform:
    on idle:
        matrixcolor BrightnessMatrix(-0.15)
    on hover:
        matrixcolor BrightnessMatrix(0.0)

style pac_image_button:
    mouse "pac"
    hover_sound "sound/sfx_pac_hover.ogg"
    activate_sound "sound/sfx_pac_select.ogg"

style pac_endbutton_style:
    idle_color '#fff'
    hover_color gui.accent_color
    font "fonts/Changa-SemiBold.ttf"
    size 60

screen pac_progress_gui(pac_name=""):
    on "show" action [SetVariable("pac_screen_active", True), Function(set_mouse_cursor_type, use_default=False)]
    on "hide" action [SetVariable("pac_screen_active", False), Function(set_mouse_cursor_type)]




    if investigation_progress_percent() < 1.0:
        vbox:
            at pac_title_transform
            text _("Ищите {image=gui/pac/pac_hint_embed.png} зацепки!"):
                size 48
    else:
        vbox:
            xalign 0.5
            text _("[u_check]{color=#cccc00}РАССЛЕДОВАНИЕ ЗАВЕРШЕНО{/color}"):
                size 48
    vbox:
        style_prefix "pacgui"
        spacing 10
        xalign 0.05 yalign 0.95
        if config.developer:
            text "x: " + str(renpy.get_mouse_pos()[0] - 37) + ", y: " + str(renpy.get_mouse_pos()[1] - 37):
                color "#ffffff22"
                yoffset 140

        if investigation_progress_percent() < 1.0:
            text _("ПРОГРЕСС РАССЛЕДОВАНИЯ:")+" {size=+15}[round(investigation_progress_percent() * 100)]%{/size}":
                size 18
        else:
            text _("ПРОГРЕСС РАССЛЕДОВАНИЯ:")+" {size=+25}{color=#cccc00}100%{/color}{/size}":
                size 18
        bar:
            xmaximum 350
            value investigation_progress_percent()
            range 1.0

screen pac_end_button(confirm_end_label, skip_bool=None):
    if investigation_complete:
        button:
            at pac_endbutton_transform
            xalign 0.5
            xsize 300 ysize 80
            background "gui/button/confirm_idle_background.png"
            hover_background "gui/button/confirm_hover_background.png"
            text _("END"):
                style "confirm_button_text"
            action Call(confirm_end_label)
    elif skip_bool != None:
        if skip_bool:
            button:
                at pac_endbutton_transform
                xalign 0.5
                xsize 300 ysize 80
                background "gui/button/confirm_yellow_idle_background.png"
                hover_background "gui/button/confirm_yellow_hover_background.png"
                text _("SKIP"):
                    style "confirm_button_text"
                action Call(confirm_end_label)

screen pac_return_button(confirm_return_label, btn_text):
    button:
        at pac_endbutton_transform
        xalign 0.5
        xsize 300 ysize 80
        background "gui/button/confirm_idle_background.png"
        hover_background "gui/button/confirm_hover_background.png"
        text btn_text:
            style "confirm_button_text"
        action Call(confirm_return_label)

screen pac_label:
    style_prefix "pac"
    default label_text = ""
    default x_pos = 0
    default y_pos = 0
    default checked = True

    vbox:
        at pac_label_transform()
        xpos x_pos
        ypos y_pos
        frame:
            has hbox
            xalign 0.5
            if checked:
                add "gui/pac/pac_check.png":
                    xsize 50 ysize 50
                    xpos 10 yoffset 10
                text label_text:
                    xoffset -10
            else:
                text label_text

transform pac_label_transform():
    alpha 0.0 yoffset 30
    easein 0.3 alpha 1.0 yoffset -5
    linear 0.05 yoffset 0

style pac_text is button_text:
    color "#fff"
    xalign 0.5
    size 36
    outlines [(5, "#000000")]

style pacgui_text:
    xalign 0.0

style pac_frame:
    xanchor 0.5 yanchor 1.0
    xoffset 37 yoffset -57
    xsize 400 ysize 100
    padding gui.frame_borders.padding
    background None

image pac_idle_animated:
    "gui/pac/pac_idle.png"
    alpha 0.5
    easeout 1.5 alpha 0.0
    choice:
        pause 1.6
    choice:
        pause 1.8
    choice:
        pause 2.0
    choice:
        pause 2.2
    choice:
        pause 2.4
    easein 1.5 alpha 0.5
    repeat

image pac_kira_idle:
    parallel:
        "gui/pac/pac_kira0.png" with Dissolve(0.5, alpha=True)
        choice:
            pause 0.6
        choice:
            pause 0.4
        "gui/pac/pac_kira1.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "gui/pac/pac_kira2.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "gui/pac/pac_kira3.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "gui/pac/pac_kira4.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        "gui/pac/pac_kira5.png" with Dissolve(0.5, alpha=True)
        pause 0.5
        repeat
    parallel:
        alpha 0.0
        choice:
            pause 1.2
        choice:
            pause 1.6
        choice:
            pause 2.0
        choice:
            pause 2.4
        choice:
            pause 2.8
        easein 1.0 alpha 0.5
        easeout 1.0 alpha 0.0
        repeat

image pac_kira_hovered:
    "gui/pac/pac_kira0.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "gui/pac/pac_kira1.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "gui/pac/pac_kira2.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "gui/pac/pac_kira3.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "gui/pac/pac_kira4.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "gui/pac/pac_kira5.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    repeat

image pac_hint:
    "gui/pac/pac_hint.png"
    xalign 0.5 yalign 0.5 rotate 0
    parallel:
        matrixcolor BrightnessMatrix(0.0)
        zoom 0.0 xoffset 30 yoffset 30
        easein 0.3 zoom 1.25 xoffset -30 yoffset -30
        linear 0.1 zoom 1.0 xoffset -15 yoffset -15 matrixcolor BrightnessMatrix(0.5)
        linear 0.1 matrixcolor BrightnessMatrix(0.0)
    parallel:
        easein 0.5 rotate 12
        easeout 0.5 rotate 0
        easein 0.5 rotate -12
        easeout 0.5 rotate 0
        repeat

image pac_hint_checked:
    "gui/pac/pac_hint.png"
    matrixcolor SaturationMatrix(0.0)
    xalign 0.5 yalign 0.5 rotate 0
    zoom 0.0 xoffset 30 yoffset 30
    easein 0.3 zoom 1.0 xoffset -15 yoffset -15

image pac_check:
    "gui/pac/pac_check.png"
    alpha 1.0
    linear 1.0 alpha 0.5

image pac_hovered = Composite(
    (75, 75),
    (0, 0), "pac_kira_hovered",
    (0, 0), "pac_hint")

image pac_hovered_checked = Composite(
    (75, 75),
    (0, 0), "pac_hint_checked")

image pac_assistant_cecilia_hovered:
    "gui/pac/pac_assistant_cecilia.png"
    yoffset 0
    easeout 0.1 yoffset -10
    easein 0.1 yoffset 0
    pause 5.0
    repeat

screen pac_assistant_button(_x, _y, _zoom, label_x, label_y, image_idle, image_hovered, call_label, prompt):
    add "gui/pac/pac_assistant_shadow.png":
        at show_hide_dissolve
        xanchor 0.5 yanchor 0.5 alpha 0.5
        xpos _x ypos _y zoom _zoom
    imagebutton:
        at pac_sprite_transform, show_hide_dissolve

        at transform:
            xanchor 0.5 yanchor 1.0
            xpos _x ypos _y zoom _zoom
        idle image_idle
        hover image_hovered
        mouse "talk"
        action [Hide("pac_label"), SetVariable("pac_clickpos_x", _x), SetVariable("pac_clickpos_y", _y), Call(call_label)]
        hovered Show("pac_label",  label_text = prompt, x_pos = label_x, y_pos = label_y, checked = False)
        unhovered Hide("pac_label")
        activate_sound "sound/sfx_pac_talk.ogg"
screen pac_button(_x, _y, clue_bool, call_label, name, special=None):
    if special==None:
        imagebutton:
            if clue_bool == False:
                idle "pac_kira_idle"
                hover "pac_hovered"
            else:
                idle "pac_check"
                hover "pac_hovered_checked"
            xpos _x ypos _y
            action [Hide("pac_label"), SetVariable("pac_clickpos_x", _x), SetVariable("pac_clickpos_y", _y), Call(call_label)]
            if clue_bool == True:
                hovered Show("pac_label", label_text = name, x_pos = _x, y_pos = _y + 60)
            unhovered Hide("pac_label")
    else:
        if special=="d1a1_visited_masterbedroom":
            imagebutton:
                if clue_bool == False:
                    if not d1a1_visited_masterbedroom:
                        idle "pac_kira_idle"
                    else:
                        idle "pac_hovered"
                    hover "pac_hovered"
                else:
                    idle "pac_check"
                    hover "pac_hovered_checked"
                xpos _x ypos _y
                action [Hide("pac_label"), SetVariable("pac_clickpos_x", _x), SetVariable("pac_clickpos_y", _y), Call(call_label)]
                if d1a1_visited_masterbedroom:
                    hovered Show("pac_label", label_text = name, x_pos = _x, y_pos = _y + 60, checked = clue_bool)
                unhovered Hide("pac_label")

transform pac_investigation_start_border_transform_top:
    yalign 0.0 yoffset -100
    easein 0.4 yoffset 0

transform pac_investigation_start_border_transform_bottom:
    yalign 1.0 yoffset 100
    easein 0.4 yoffset 0

transform pac_investigation_start_menu_transform:
    alpha 0.0 zoom 0.5
    pause 0.9
    easein 0.4 alpha 1.0 zoom 1.05
    linear 0.1 zoom 1.0

transform pac_investigation_start_logo_transform:
    parallel:
        alpha 0.0 xzoom 0.8 yzoom 0.0
        easein 0.3 alpha 1.0 xzoom 1.1 yzoom 1.1
        pause 0.5
        easeout 0.7 alpha 0.0 xzoom 1.0 yzoom 1.0
    parallel:
        rotate -2
        linear 2.0 rotate 2
    parallel:
        matrixcolor BrightnessMatrix(1.0)
        easein 0.8 matrixcolor BrightnessMatrix(0.0)
        easeout 0.2 matrixcolor BrightnessMatrix(1.0)

image pac_explode:
    "gui/pac/pac_explode_icon.png"
    xalign 0.5 yalign 0.5
    xoffset 35 yoffset 34
    zoom 2.5
    easein 0.15 zoom 0.9
    linear 0.1 zoom 1.1

image pac_explode_star:
    "gui/pac/pac_explode_star.png"
    xalign 0.5 yalign 0.5
    xoffset 65 yoffset 65
    alpha 0.2 zoom 1.0
    linear 0.25 zoom 1.25

transform pac_explode():
    xpos pac_clickpos_x ypos pac_clickpos_y
    alpha 1.0
    easeout 0.25 alpha 0.0

screen pac_investigation_start(name="New Investigation", desc="New Text"):
    frame xfill True ysize 100 background "#000" at pac_investigation_start_border_transform_top
    frame xfill True ysize 100 background "#000" at pac_investigation_start_border_transform_bottom

    frame at show_hide_dissolve:
        background None
        add "pac intrologo" at pac_investigation_start_logo_transform:
            xalign 0.5 yalign 0.5
        xfill True yfill True
        vbox at pac_investigation_start_menu_transform:
            spacing 50
            xalign 0.5 yalign 0.5
            text _("INVESTIGATION"):
                xalign 0.5
                font "fonts/Alkalami-Regular.ttf"
                color gui.accent_color
                outlines [(2, "#000000")]
                size 72
                yoffset 45
            text name:
                xalign 0.5
                outlines [(2, "#000000")]
                size 48
            text desc:
                xalign 0.5
                text_align 0.5
                outlines [(2, "#000000")]
                size 32
            button:
                xalign 0.5
                xsize 300 ysize 80
                background "gui/button/confirm_idle_background.png"
                hover_background "gui/button/confirm_hover_background.png"
                text _("START"):
                    style "confirm_button_text"
                action Return()


screen pac_switch_button(direction, call_label, prompt):
    imagebutton at show_hide_dissolve:
        if direction == "left":
            xalign 0.0 yalign 0.5 xoffset 50
            idle "direction_button_left_idle"
            hover "direction_button_left_hovered"
        else:
            xalign 1.0 yalign 0.5 xoffset -50
            idle "direction_button_right_idle"
            hover "direction_button_right_hovered"
        mouse "button"
        action [Hide("pac_label"), Call(call_label)]
        hovered Show("pac_label", label_text = prompt, x_pos = (1790 if direction == "right" else 80), y_pos = 570, checked = False)
        unhovered Hide("pac_label")
        activate_sound "sound/sfx_pac_talk.ogg"

image direction_button_right_idle:
    xsize 100 ysize 100
    "gui/ctc/10.png"
    parallel:
        yoffset 0
        easein 1.0 yoffset -10
        easeout 1.0 yoffset 0
        easein 1.0 yoffset 10
        easeout 1.0 yoffset 0
        repeat
    parallel:
        matrixcolor BrightnessMatrix(-0.25)
        linear 0.1 matrixcolor BrightnessMatrix(0.75)
        easein 0.3 matrixcolor BrightnessMatrix(-0.25)
        pause 4.5
        repeat

image direction_button_right_hovered:
    xsize 100 ysize 100
    contains:
        "gui/ctc/10.png"
        pause 0.5
        "gui/ctc/11.png"
        pause 0.035
        "gui/ctc/12.png"
        pause 0.035
        "gui/ctc/13.png"
        pause 0.035
        "gui/ctc/14.png"
        pause 0.035
        "gui/ctc/15.png"
        pause 0.035
        "gui/ctc/16.png"
        pause 0.035
        "gui/ctc/17.png"
        pause 0.035
        "gui/ctc/18.png"
        pause 0.035
        "gui/ctc/19.png"
        pause 0.035
        "gui/ctc/20.png"
        pause 0.035
        "gui/ctc/0.png"
        pause 0.035
        "gui/ctc/1.png"
        pause 0.035
        "gui/ctc/2.png"
        pause 0.035
        "gui/ctc/3.png"
        pause 0.035
        "gui/ctc/4.png"
        pause 0.035
        "gui/ctc/5.png"
        pause 0.035
        "gui/ctc/6.png"
        pause 0.035
        "gui/ctc/7.png"
        pause 0.035
        "gui/ctc/8.png"
        pause 0.035
        "gui/ctc/9.png"
        pause 0.035
        repeat

image direction_button_left_idle:
    xsize 100 ysize 100 rotate 180
    "gui/ctc/10.png"
    parallel:
        yoffset 0
        easein 1.0 yoffset -10
        easeout 1.0 yoffset 0
        easein 1.0 yoffset 10
        easeout 1.0 yoffset 0
        repeat
    parallel:
        matrixcolor BrightnessMatrix(-0.25)
        linear 0.1 matrixcolor BrightnessMatrix(0.75)
        easein 0.3 matrixcolor BrightnessMatrix(-0.25)
        pause 4.5
        repeat

image direction_button_left_hovered:
    xsize 100 ysize 100 rotate 180
    contains:
        "gui/ctc/10.png"
        pause 0.5
        "gui/ctc/11.png"
        pause 0.035
        "gui/ctc/12.png"
        pause 0.035
        "gui/ctc/13.png"
        pause 0.035
        "gui/ctc/14.png"
        pause 0.035
        "gui/ctc/15.png"
        pause 0.035
        "gui/ctc/16.png"
        pause 0.035
        "gui/ctc/17.png"
        pause 0.035
        "gui/ctc/18.png"
        pause 0.035
        "gui/ctc/19.png"
        pause 0.035
        "gui/ctc/20.png"
        pause 0.035
        "gui/ctc/0.png"
        pause 0.035
        "gui/ctc/1.png"
        pause 0.035
        "gui/ctc/2.png"
        pause 0.035
        "gui/ctc/3.png"
        pause 0.035
        "gui/ctc/4.png"
        pause 0.035
        "gui/ctc/5.png"
        pause 0.035
        "gui/ctc/6.png"
        pause 0.035
        "gui/ctc/7.png"
        pause 0.035
        "gui/ctc/8.png"
        pause 0.035
        "gui/ctc/9.png"
        pause 0.035
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
