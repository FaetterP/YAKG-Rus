






































define BOBCACHIVEMENTS_SPACING = 10
define BOBCACHIVEMENTS_HIDDEN_ACHIEVEMENT_TEXT = _("?????")
define BOBCACHIEVEMENTS_SPACING_CHAR = _(":")
define BOBCACHIEVEMENTS_GRANTED_COLOR = gui.text_color
define BOBCACHIEVEMENTS_UNGRANTED_COLOR = gui.idle_color

style achievements_text:
    color BOBCACHIEVEMENTS_GRANTED_COLOR
    size 24

style achievements_labeltext:
    font "fonts/Changa-SemiBold.ttf"
    size 28
    line_spacing -16
    line_leading 4





image achieved_icon:
    "gui/pac/pac_check.png"
    zoom 1.5

image unachieved_icon:
    "gui/pac/pac_hint.png"
    matrixcolor SaturationMatrix(0.0) zoom 1.5

image unachieved_frame:
    matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(0.1)
    "gui/frame.png"

style unachieved_frame:
    background Frame("unachieved_frame", gui.frame_borders, tile=gui.frame_tile)

style achievement_deletebtn:
    font "fonts/Changa-SemiBold.ttf"
    size 28
    color "#ff7777"
    hover_color "#ff2222"
    outlines [(2, "#000000")]





transform achievement_hover:
    on hover:
        matrixcolor BrightnessMatrix(0.0)
    on idle:
        matrixcolor BrightnessMatrix(-0.25)

screen achievement_box(i, achievement_id):
    vbox:
        hover_alt BOBCACHIEVEMENTS_MAP[achievement_id][0]


        frame:
            if not achievement.has(achievement_id):
                style "unachieved_frame"
            xsize 670 ysize 200
            hbox:
                yalign 0.5
                if achievement.has(achievement_id):
                    add "achieved_icon" yalign 0.5
                else:
                    add "unachieved_icon" yalign 0.5
                null width 0
                button at achievement_hover:
                    action NullAction()
                    mouse "default"
                    activate_sound None
                    has vbox
                    if achievement.has(achievement_id):
                        text "#[i] | " + __(BOBCACHIEVEMENTS_MAP[achievement_id][0]) style "achievements_labeltext"
                        text BOBCACHIEVEMENTS_MAP[achievement_id][1]
                    else:
                        text "#[i] | " + BOBCACHIVEMENTS_HIDDEN_ACHIEVEMENT_TEXT style "achievements_labeltext"
                        if persistent.unlock_gameclear_cgs:
                            text BOBCACHIEVEMENTS_MAP[achievement_id][1]
                        else:
                            text _("-LOCKED ACHIEVEMENT-")

screen bobcachievements():
    tag menu
    default numachievements = len(persistent._achievements)

    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "achievements"
        vbox:
            vbox:
                xalign 0.5
                if numachievements >= BOBCACHIEVEMENTS_NUMACHIEVEMENTS:
                    text _("Got all {color=#cccc00}{size=+24}{font=DejaVuSans.ttf}\u2605{/font}[BOBCACHIEVEMENTS_NUMACHIEVEMENTS]{/size}{/color} Achievements! Way to go~ [u_music_note]"):
                        font "fonts/Changa-SemiBold.ttf"
                        size 42
                        outlines [(2, "#000000")]
                else:
                    text _("Got {color=#cccc00}{size=+24}{font=DejaVuSans.ttf}\u2605{/font}[numachievements]{/size}{/color}/[BOBCACHIEVEMENTS_NUMACHIEVEMENTS] Achievements! [t_clue][BOBCACHIEVEMENTS_NUMACHIEVEMENTS - numachievements][t_cluee] more to go!"):
                        font "fonts/Changa-SemiBold.ttf"
                        size 42
                        outlines [(2, "#000000")]
                if config.developer:
                    textbutton "clear achievements" action Function(achievement.clear_all)
                null height BOBCACHIVEMENTS_SPACING
            hbox:
                vbox:
                    xsize 650 ysize 300
                    for i, achievement_id in enumerate(BOBCACHIEVEMENTS_MAP, start = 1):
                        if i % 2 != 0:
                            use achievement_box(i, achievement_id)
                vbox:
                    xsize 650 ysize 300
                    for i, achievement_id in enumerate(BOBCACHIEVEMENTS_MAP, start = 1):
                        if i % 2 == 0:
                            use achievement_box(i, achievement_id)
            if numachievements >= BOBCACHIEVEMENTS_NUMACHIEVEMENTS:
                vbox:
                    xalign 0.5
                    null height 24
                    text _("Now... Will you DELETE your Achievement data and collect them all again?"):
                        font "fonts/Changa-SemiBold.ttf"
                        size 32
                        outlines [(2, "#000000")]
                    textbutton _("DELETE ACHIEVEMENT DATA") action Confirm(_("{color=#ff0000}DELETE{/color} your Achievement data?\nThis will not affect your [t_clue]Steam[t_cluee] account."), yes=Function(achievement.clear_all)):
                        xalign 0.5
                        text_style "achievement_deletebtn"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
