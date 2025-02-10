





define u_heart = "{font=DejaVuSans.ttf}\u2665{/font}"
define u_star = "{font=DejaVuSans.ttf}\u2605{/font}"
define u_music_note = "{font=DejaVuSans.ttf}\u266B{/font}"
define u_check = "{color=#44b817}{font=DejaVuSans.ttf}\u2714{/font}{/color}"
define u_loop = "{font=DejaVuSans.ttf}{size=-2}\u21BA{/size}{/font}"
define u_copyright = "{font=DejaVuSans.ttf}\u00A9{/font}"

image ctc_blink:
    ConditionSwitch("preferences.afm_enable == True", "ctc_auto", "preferences.afm_enable == False", "ctc_normal")

image ctc_normal:
    xsize 60 ysize 60 yanchor 0.15 ypos 0
    contains:
        im.Scale("gui/ctc/0.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/1.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/2.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/3.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/4.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/5.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/6.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/7.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/8.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/9.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/10.png", 60, 60)
        pause 1.0
        im.Scale("gui/ctc/11.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/12.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/13.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/14.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/15.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/16.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/17.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/18.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/19.png", 60, 60)
        pause 0.035
        im.Scale("gui/ctc/20.png", 60, 60)
        pause 0.035
        repeat

image ctc_auto:
    xsize 60 ysize 60 yanchor 0.15 ypos 0
    contains:
        im.Scale("gui/ctc_auto/0.png", 60, 60)
        pause 2.5
        im.Scale("gui/ctc_auto/1.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/2.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/3.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/4.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/5.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/6.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/7.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/8.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/9.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/10.png", 60, 60)
        pause 0.06
        im.Scale("gui/ctc_auto/11.png", 60, 60)
        pause 0.06
        repeat

image intext_iconback = im.Scale("gui/quick/icon_back.png", 62, 37)




define Y = DynamicCharacter("input_name", color="#cccc00", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound, image="player")
define YV = DynamicCharacter("input_name", color="#44b817", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound, image="playervillain")
define YD = DynamicCharacter("input_name", color="#44b817", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound, image="playerdog")
define I = Character(None, what_color="#4cbdff", what_prefix="(", what_suffix=")", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound)


define C = DynamicCharacter("name_cecilia", color="#508ef2", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound, image="cecilia")
define O = DynamicCharacter("name_oriana", color="#d93838", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound, image="oriana")
define K = DynamicCharacter("name_karma", color="#cccc00", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound, image="karma")
define D = DynamicCharacter("name_dog", color="#606060", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound, image="dog")
define V = DynamicCharacter("name_villain", color="#cc00bb", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound, image="villain")


define X = DynamicCharacter("name_npc", color="#ff3eff", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound)
define S = Character(None, color="#ffffff", what_color="#44b817", what_font="fonts/AveriaLibre-Regular.ttf",  ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound)
define P = Character(None, color="#d93838", what_color="#ff0000", what_font="fonts/AveriaLibre-Regular.ttf", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound)
define KI = Character(None, color="#cccc00", what_color="#cccc00", what_font="fonts/AveriaLibre-Regular.ttf", ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound)
define U = Character(ctc="ctc_blink", ctc_position="nestled-close", callback=ctc_sound)

image chaptertitle1_text = Text(_("{size=+30}PART {/size}{size=+50}I{/size}"), style='chaptertitle_text_style')
image chaptertitle1_subtext = Text(_("wELcOme 2 KILLING GAME"), style='chaptertitle_text_style')

image chaptertitle1_end_text = Text(_("{size=+30}END of PART {/size}{size=+50}I{/size}"), style='chaptertitle_end_text_style')
image chaptertitle1_end_subtext = Text(_("To be continued in Part II..."), style='chaptertitle_end_text_style')

image chaptertitle2_text = Text(_("{size=+30}PART {/size}{size=+50}II{/size}"), style='chaptertitle_text_style')
image chaptertitle2_subtext = Text(_("eND 0f KILLING GAME"), style='chaptertitle_text_style')

image chaptertitle2_end_text = Text(_("{size=+30}END of PART {/size}{size=+50}II{/size}"), style='chaptertitle_end_text_style')
image chaptertitle2_end_subtext = Text(_("To be {color=#ff0000}CONCLUDED{/color} in Part III..."), style='chaptertitle_end_text_style')

image chaptertitle3_text = Text(_("{size=+30}PART {/size}{size=+50}III{/size}"), style='chaptertitle_text_style')
image chaptertitle3_subtext = Text(_("{size=+30}{color=#ff0000}YET ANOTHER KILLING GAME{/color}{/size}"), style='chaptertitle_text_style')

style chaptertitle_text_style:
    font "fonts/AveriaSerifLibre-Regular.ttf"
    size 40
    text_align 0.5
    outlines [ (5, "#500", absolute(0), absolute(0)) ]

style chaptertitle_end_text_style:
    font "fonts/AveriaSerifLibre-Regular.ttf"
    size 40
    text_align 0.5
    color "#000000"

image ghostmessage_1 = Text(_("{color=#cccc00}[t_ghost]{size=+5}Will you reject this Ending too...?{/size}[t_ghoste]{/color}"), style='add_outlines_text_style')
image ghostmessage_2 = Text(_("{color=#cccc00}[t_ghost]{size=+5}Then this time... Tell [t_clue]them[t_cluee] the truth... The WHOLE truth...{/size}[t_ghoste]{/color}"), style='add_outlines_text_style')

style add_outlines_text_style:
    outlines [ (5, "#000", absolute(0), absolute(0)) ]

transform chaptertitle_text_transform:
    linear 0.5 xoffset -1 yoffset 1
    linear 0.5 xoffset -1 yoffset -1
    linear 0.5 xoffset 2 yoffset -2
    linear 0.5 xoffset 1 yoffset -1
    linear 0.5 xoffset 2 yoffset 2
    linear 0.5 xoffset -2 yoffset 2
    linear 0.5 xoffset 0 yoffset 0
    repeat

image shard_chaos = dynamic_shard_png("seen_ending_chaos", "shard_chaos")
image shard_order = dynamic_shard_png("seen_ending_order", "shard_order")
image shard_karma = dynamic_shard_png("seen_ending_karma", "shard_karma")

image shard chaos:
    "objects/shard_chaos.png"
    zoom 1.5 xanchor 0.19 yanchor 0.33
    xpos 0.5 ypos 0.5

image shard order:
    "objects/shard_order.png"
    zoom 1.5 xanchor 0.79 yanchor 0.71
    xpos 0.5 ypos 0.5

image shard karma:
    "objects/shard_karma.png"
    zoom 1.5 xanchor 0.5 yanchor 0.48
    xpos 0.5 ypos 0.5

image shard despair:
    "objects/shard_despair.png"
    zoom 1.5 xanchor 0.73 yanchor 0.19
    xpos 0.5 ypos 0.5

image shard judgement:
    "objects/shard_judgement.png"
    zoom 1.5 xanchor 0.24 yanchor 0.76
    xpos 0.5 ypos 0.5

image shard light:
    "objects/shard_light.png"
    zoom 1.5 xanchor 0.63 yanchor 0.77
    xpos 0.5 ypos 0.5

image shard darkness:
    "objects/shard_darkness.png"
    zoom 1.5 xanchor 0.48 yanchor 0.20
    xpos 0.5 ypos 0.5

transform appearing_shard:
    parallel:
        zoom 0.1 matrixcolor BrightnessMatrix(1.0)
        easein 0.8 zoom 1.05 matrixcolor BrightnessMatrix(0.8)
        linear 0.1 zoom 1.0 matrixcolor BrightnessMatrix(0.5)
        linear 0.1 matrixcolor BrightnessMatrix(0.0)
        pause 0.8
        linear 0.2 matrixcolor BrightnessMatrix(0.8)
        linear 0.2 matrixcolor BrightnessMatrix(0.0)
        pause 2.4
        linear 0.2 matrixcolor BrightnessMatrix(0.8)
        linear 0.2 matrixcolor BrightnessMatrix(0.0)
        pause 2.4
        linear 0.2 matrixcolor BrightnessMatrix(0.8)
        linear 0.2 matrixcolor BrightnessMatrix(0.0)
    parallel:
        yoffset -10
        ease 1.5 yoffset 10
        ease 1.5 yoffset -10
        repeat

image logo:
    "objects/logo.png"
    zoom 0.75 xalign 0.5 yalign 0.25

transform slideacrossup:
    xalign 1.0
    yanchor -1.0
    linear 140.0 yanchor 1.0
transform slideacrossdown:
    xalign 0.0
    yanchor 1.0
    linear 140.0 yanchor -1.0





image bg black = "#000000"
image bg white = ConditionSwitch("persistent.darken_flashes == True", "#424242", "persistent.darken_flashes == False", "#ffffff")
image bg red = ConditionSwitch("persistent.darken_flashes == True", "#700000", "persistent.darken_flashes == False", "#ff0000")
image bg flamewall:
    "backgrounds/bg flamewall1.png" with Dissolve(1.0, alpha=True)
    pause 1.0
    "backgrounds/bg flamewall2.png" with Dissolve(1.0, alpha=True)
    pause 1.0
    "backgrounds/bg flamewall3.png" with Dissolve(1.0, alpha=True)
    pause 1.0
    repeat

image bg splashscreen:
    "backgrounds/bg foyer.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "backgrounds/bg kitchen.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "backgrounds/bg bedroom.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "backgrounds/bg hallway.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "backgrounds/bg diningroom.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "backgrounds/bg lounge.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    "backgrounds/bg attic.png" with Dissolve(0.3, alpha=True)
    pause 0.3
    repeat

image bg library right:
    "backgrounds/bg library.png"
    crop (960, 0, 1920, 1080)
image bg library left:
    "backgrounds/bg library.png"
    crop (0, 0, 1920, 1080)
image bg library zoomedout:
    "backgrounds/bg library.png"
    zoom 0.66 yoffset -183
image bg library dark right:
    "backgrounds/bg library dark.png"
    crop (960, 0, 1920, 1080)
image bg library dark left:
    "backgrounds/bg library dark.png"
    crop (0, 0, 1920, 1080)
image bg library dark zoomedout:
    "backgrounds/bg library dark.png"
    zoom 0.66 yoffset -183

image bg bedroom corpse pac:
    "backgrounds/bg bedroom corpse.png"
    xalign 0.7 yalign 0.8 zoom 1.8

define t_clue = "{color=#ff3eff}"
define t_cluee = "{/color}"
define t_hotkey = "{color=#44b817}{font=DejaVuSans.ttf}{size=24}{b}["
define t_hotkeye = "]{/b}{/size}{/font}{/color}"
define t_ctrlkey = "{color=#000}{font=DejaVuSans.ttf}{size=24}{b}{outlinecolor=#888}("
define t_ctrlkeye = "){/outlinecolor}{/b}{/size}{/font}{/color}"
define t_pacclue = "{color=#d78121}"
define t_paccluee = "{/color}"
define t_ghost = "{font=fonts/LovecraftsDiary.ttf}"
define t_ghoste = "{/font}"


default _game_menu_screen = "pause"

default save_name = ""
default current_part_name = ""
default current_chapter_number = ""
default current_chapter_name = ""

default this_inst_name = config.name
default this_inst_version = config.version
default this_inst_day1_clear = False
default this_inst_is_demo = False


default input_name = _("You")
default input_name_true = "Jun"
default placeholder_name = ""
default name_player = "{color=#cccc00}"+input_name+"{/color}"
default name_player_true = "{color=#44b817}Jun{/color}"
default name_cecilia = _("Cecilia")
default name_oriana = _("Oriana")
default input_name_dog = _("Dog")
default name_dog = "{color=#606060}"+input_name_dog+"{/color}"
default name_villain = _("Corpse")
default name_npc = _("???")
default name_karma = _("???")


default show_choicegrand = False
default show_choicekarma = False
default mute_choice = False
default fadein_sideimage = False
default grayscale_sideimage = False
default show_side_player = False
default show_side_cecilia = False
default show_side_oriana = False
default show_side_dog = False
default show_side_villain = False
default show_side_karma = False


default shard_string = ""
default backshard_layers = 0

default seen_ending_chaos = False
default seen_ending_order = False
default seen_ending_karma = False
default seen_ending_despair = False
default seen_ending_judgement = False
default seen_ending_light = False
default seen_ending_darkness = False
default credits_type = "bad"

default seen_tutorial_investigations = False
default persistent.seen_tutorial_autosaves = False

default day1_loop_count = 0
default day1_dinner_skipped = False
default d1a1_chaos_flag = ""
default d1a1_order_flag = ""

default investigation_location = None
default investigation_complete = False
default investigation_perfect = False
default investigation_clues_required = 1
default investigation_clues_required_found = 0
default investigation_clues_optional = 1
default investigation_clues_optional_found = 0

default pac_clickpos_x = 0
default pac_clickpos_y = 0

default d1a1_checked_kitchen = False
default d1a1_kitchen_clue1 = False
default d1a1_kitchen_clue2 = False
default d1a1_kitchen_clue3 = False
default d1a1_kitchen_clue4 = False
default d1a1_kitchen_clue5 = False
default d1a1_kitchen_clue6 = False
default d1a1_kitchen_clue7 = False
default d1a1_kitchen_clue8 = False
default d1a1_kitchen_clue9 = False
default d1a1_kitchen_clue10 = False

default d1a1_visited_diningroom = False
default d1a1_diningroom_clue1 = False
default d1a1_diningroom_clue2 = False
default d1a1_diningroom_clue3 = False
default d1a1_diningroom_clue4 = False
default d1a1_diningroom_clue5 = False
default d1a1_diningroom_clue6 = False
default d1a1_diningroom_clue7 = False
default d1a1_diningroom_clue8 = False
default d1a1_diningroom_clue9 = False
default d1a1_diningroom_clue10 = False
default d1a1_diningroom_clue11 = False
default preferred_pet = ""

default d1a1_checked_bathroom = False
default d1a1_bathroom_clue0 = False
default d1a1_bathroom_clue1 = False
default d1a1_bathroom_clue2 = False
default d1a1_bathroom_clue3 = False
default d1a1_bathroom_clue4 = False
default d1a1_bathroom_clue5 = False
default d1a1_bathroom_clue6 = False
default d1a1_bathroom_clue7 = False
default d1a1_bathroom_clue8 = False
default d1a1_bathroom_clue9 = False
default d1a1_bathroom_clue10 = False
default d1a1_bathroom_clue11 = False

default d1a1_sink_on = False
default d1a1_checked_trash = False
default rng_min = 1
default rng = renpy.random.randint(rng_min, 21)
default d1a1_treasure_found = False

default d1a1_checked_upstairs = False
default d1a1_upstairs_clue1 = False
default d1a1_upstairs_clue2 = False
default d1a1_upstairs_clue3 = False
default d1a1_upstairs_clue4 = False
default d1a1_upstairs_clue5 = False
default d1a1_upstairs_clue6 = False
default d1a1_upstairs_clue7 = False
default d1a1_upstairs_clue8 = False
default d1a1_upstairs_clue9 = False
default d1a1_upstairs_clue10 = False

default d1a1_bedroom_clue1 = False
default d1a1_bedroom_clue2 = False
default d1a1_bedroom_clue3 = False
default d1a1_bedroom_clue4 = False
default d1a1_bedroom_clue5 = False
default d1a1_bedroom_clue6 = False
default d1a1_bedroom_clue7 = False
default d1a1_bedroom_clue8 = False
default d1a1_bedroom_clue9 = False
default d1a1_bedroom_clue10 = False
default d1a1_bedroom_clue11 = False
default d1a1_bedroom_clue12 = False
default d1a1_bedroom_clue13 = False
default d1a1_bedroom_clue14 = False
default d1a1_bedroom_clue15 = False
default d1a1_bedroom_clue16 = False
default d1a1_bedroom_clue17 = False

default d1a1_visited_masterbedroom = False
default d1a1_masterbedroom_clue1 = False
default d1a1_masterbedroom_clue2 = False
default d1a1_masterbedroom_clue3 = False
default d1a1_masterbedroom_clue4 = False
default d1a1_masterbedroom_clue5 = False
default d1a1_masterbedroom_clue6 = False
default d1a1_masterbedroom_clue7 = False
default d1a1_masterbedroom_clue8 = False
default d1a1_masterbedroom_clue9 = False
default d1a1_masterbedroom_clue10 = False
default d1a1_masterbedroom_clue11 = False
default d1a1_jumped_bed = False


default investigated_kitchen = False
default investigated_bathroom = False
default investigated_upstairs = False

default d1a4_questioning_clue1 = False
default d1a4_questioning_clue2 = False
default d1a4_questioning_clue2A = False
default d1a4_questioning_clue2AA = False
default d1a4_questioning_clue2AB = False
default d1a4_questioning_clue2B = False
default d1a4_questioning_clue3 = False
default d1a4_third_member_mentioned = False


default d2a1_shower_reaction = ""

default d2a1_attic_clue1 = False
default d2a1_attic_clue2 = False
default d2a1_attic_clue3 = False
default d2a1_attic_clue4 = False
default d2a1_attic_clue5 = False
default d2a1_attic_clue6 = False
default d2a1_attic_clue7 = False
default d2a1_attic_clue8 = False
default d2a1_attic_clue9 = False
default d2a1_attic_clue10 = False
default d2a1_attic_clue11 = False
default d2a1_attic_clue12 = False
default d2a1_attic_clue13 = False
default d2a1_attic_clue14 = False
default d2a1_attic_clue15 = False

default d2a1_lounge_clue1 = False
default d2a1_lounge_clue2 = False
default d2a1_lounge_clue3 = False
default d2a1_lounge_clue4 = False
default d2a1_lounge_clue5 = False
default d2a1_lounge_clue6 = False
default d2a1_lounge_clue7 = False
default d2a1_lounge_clue8 = False
default d2a1_lounge_clue9 = False
default d2a1_lounge_clue10 = False
default d2a1_lounge_clue11 = False
default d2a1_lounge_clue12 = False
default d2a1_lounge_clue13 = False
default d2a1_lounge_clue14 = False

default d2a2_basement_clue1 = False
default d2a2_basement_clue2 = False
default d2a2_basement_clue3 = False
default d2a2_basement_clue4 = False
default d2a2_basement_clue5 = False
default d2a2_basement_clue6 = False
default d2a2_basement_clue7 = False
default d2a2_basement_clue8 = False
default d2a2_basement_clue9 = False
default d2a2_basement_clue10 = False
default d2a2_basement_clue11 = False
default d2a2_basement_clue12 = False

default investigated_basement = False

default died_with_regrets = False

default d2a3_library_clue1 = False
default d2a3_library_checkedcorpse = False
default d2a3_library_clue2 = False
default d2a3_library_clue3 = False
default d2a3_library_clue4 = False

default d2a3_library_clue5 = False
default d2a3_library_clue6 = False
default d2a3_library_clue7 = False
default d2a3_library_clue8 = False
default d2a3_library_clue9 = False
default d2a3_library_clue10 = False

default d2a3_library_clue11 = False
default d2a3_library_clue12 = False
default d2a3_library_clue13 = False
default d2a3_library_clue14 = False

default seen_cece_hearttoheart = False

default day3_checked_kitchen = False
default day3_checked_bathroom = False
default day3_checked_upstairs = False
default day3_checked_lounge = False

default seen_ria_hearttoheart = False
default chose_suspect = False

default d3a2_dog_clue1 = False
default d3a2_dog_clue2 = False
default d3a2_dog_clue3 = False
default d3a2_dog_clue4 = False
default d3a2_dog_clue5 = False
default d3a2_dog_clue6 = False
default d3a2_dog_clue7 = False

default d3a3_corpse_clue1 = False
default d3a3_corpse_clue2 = False
default d3a3_corpse_clue3 = False
default d3a3_corpse_clue4 = False
default d3a3_corpse_clue5 = False
default d3a3_corpse_clue6 = False
default d3a3_corpse_clue7 = False
default d3a3_corpse_clue8 = False
default d3a3_corpse_clue9 = False

default finalchoice_doubt = False
default menu_time_remaining = 15

default d3a6_questions_remaining = 3
default d3a6_questioning_clue1 = False
default d3a6_questioning_clue2 = False
default d3a6_questioning_clue3 = False
default d3a6_questioning_clue4 = False
default d3a6_questioning_clue5 = False
default d3a6_questioning_clue6 = False
default d3a6_questioning_clue7 = False

default d3a6_duel_hp = 3

default ctc_timer = 0


init:
    $ import time

    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()


label start:
    $ this_inst_name = config.name
    $ this_inst_version = config.version
    $ this_inst_day1_clear = False
    $ this_inst_is_demo = False

    $ _autosave = True
    $ toggle_rollback()
    call save_file_name_update (1, "d1a0")
    $ _game_menu_screen = "pause"


    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys

    play sound sfx_wail
    scene bg black
    show main_menu_bg at truecenter, titlezoom
    with custom_flash()
    $ renpy.pause(3.0, hard=True)
    stop music fadeout 3
    scene bg black with dissolveslow


    show text "{color=#ff0000}ПРЕДУПРЕЖДЕНИЕ О СОДЕРЖАНИИ{/color}\nЭта игра содержит жёсткий [t_clue]язык[t_cluee], наводящие на размышления темы, полноэкранные [t_clue]визуальные эффекты[t_cluee],\nтревожные звуки, [t_clue]кровь[t_cluee], изображения жестокости и текстовые описания крайнего\nнасилия, [t_clue]убийства[t_cluee] и [t_clue]суицида[t_cluee].\n\nЭто произведение является вымышленным. Любое сходство с реальными событиями и людьми, живыми\nили мёртвыми, является случайным. Мнения, выраженные персонажами этого\nпроизведения, не обязательно совпадают с мнением автора." with dissolvemed
    pause 5.0
    call screen proceed_button
    hide text with dissolvemed

    hide screen lock_hotkeys
    $ quick_menu = True
    $ music_info = True

    jump d1a0




label before_main_menu:
    if config.developer:
        pass
    else:
        stop music fadeout 1.0
        scene black with dissolve
        show logo at truecenter:
            alpha 0.0 zoom 0.5
            parallel:
                easein 5.0 zoom 1.2
            parallel:
                linear 1.5 alpha 1.0
        play music bgm_mainmenu fadein 3.0
        pause 1.0
        show bg splashscreen behind logo:
            alpha 0.0
            easein 3.5 alpha 1.0
        pause 2.0
        scene bg white with dissolvemed
        play sound sfx_introambiance_pentagramknife volume 0.5
        scene bg black
        show main_menu_bg at truecenter
        with shakeshort
    return

label after_load:
    $ _autosave = True
    $ toggle_rollback()

    if this_inst_is_demo and not is_demo_version():
        $ renpy.block_rollback()
        show cg keyvisual side with dissolve
        call screen end_of_demo()
        $ this_inst_is_demo = False
        $ renpy.block_rollback()
        scene bg black with dissolve
        pause 1.0
    if this_inst_day1_clear:
        if is_demo_version():
            call load_in_demo_error
    return

label load_in_demo_error:
    stop music
    stop loop_sfx
    scene bg black
    $ renpy.block_rollback()
    call screen load_in_demo_error_screen()
    $ renpy.full_restart()

label save_file_name_update(chapter_number, day_act):
    $ new_save_name = ""
    if chapter_number == 1:
        $ current_part_name = _("Part I")
        if seen_ending_chaos:
            $ new_save_name = new_save_name + u_loop
        if seen_ending_order:
            $ new_save_name = new_save_name + u_loop
        if seen_ending_karma:
            $ new_save_name = new_save_name + u_loop

        if new_save_name != "":
            $ new_save_name = new_save_name + " " + _("Part I")
        else:
            $ new_save_name = _("Part I")

    if chapter_number == 2:
        $ current_part_name = _("Part II")
        if seen_ending_despair:
            $ new_save_name = new_save_name + u_loop
        if seen_ending_judgement:
            $ new_save_name = new_save_name + u_loop
        if seen_ending_light:
            $ new_save_name = new_save_name + u_loop
        if seen_ending_darkness:
            $ new_save_name = new_save_name + u_loop

        if new_save_name != "":
            $ new_save_name = new_save_name + " " + _("Part II")
        else:
            $ new_save_name = _("Part II")

    if chapter_number == 3:
        $ current_part_name = _("Part III")
        $ new_save_name = _("Part III")

    $ d1a1_investigated_count = 0
    if d1a1_checked_kitchen:
        $ d1a1_investigated_count += 2
    if d1a1_checked_bathroom:
        $ d1a1_investigated_count += 2
    if d1a1_checked_upstairs:
        $ d1a1_investigated_count += 2

    if day_act is "d1a0":
        $ current_chapter_number = _("Prologue")
        $ current_chapter_name = _("?????")
    elif day_act is "d1a1":
        $ current_chapter_number = _("Chapter 1")
        $ current_chapter_name = _("The Game Begins...?")
    elif day_act is "d1a1_start_investigation":
        $ current_chapter_number = _("Chapter ") + str(2 + d1a1_investigated_count)
        $ current_chapter_name = _("Seeking a Way Out")
    elif day_act is "d1a1_kitchen":
        $ current_chapter_number = _("Chapter ") + str(2 + d1a1_investigated_count)
        $ current_chapter_name = _("The Kitchen with Cecilia")
    elif day_act is "d1a1_kitchen_end":
        $ current_chapter_number = _("Chapter ") + str(3 + d1a1_investigated_count)
        $ current_chapter_name = _("Who Wants to Be a Murderer?")
    elif day_act is "d1a1_bathroom":
        $ current_chapter_number = _("Chapter ") + str(2 + d1a1_investigated_count)
        $ current_chapter_name = _("The Bathroom with...")
    elif day_act is "d1a1_bathroom_end":
        $ current_chapter_number = _("Chapter ") + str(3 + d1a1_investigated_count)
        $ current_chapter_name = _("A Wild Dog Chase")
    elif day_act is "d1a1_upstairs":
        $ current_chapter_number = _("Chapter ") + str(2 + d1a1_investigated_count)
        $ current_chapter_name = _("2F with Oriana")
    elif day_act is "d1a1_upstairs_end":
        $ current_chapter_number = _("Chapter ") + str(3 + d1a1_investigated_count)
        $ current_chapter_name = _("My Justice, Your Justice")
    elif day_act is "d1a2":
        $ current_chapter_number = _("Chapter 6")
        $ current_chapter_name = _("Rules Must Be Followed")
    elif day_act is "d1a2_part2":
        $ current_chapter_number = _("Chapter 7")
        $ current_chapter_name = _("Good Night")
    elif day_act is "d1a3_karma":
        $ current_chapter_number = _("Chapter 8")
        $ current_chapter_name = _("You Cannot Escape...Chaos?")
    elif day_act is "d1a3_order":
        $ current_chapter_number = _("Chapter 8")
        $ current_chapter_name = _("The Demon Condemned")
    elif day_act is "d1a3_chaos":
        $ current_chapter_number = _("Chapter 8")
        $ current_chapter_name = _("You Cannot Escape Chaos")
    elif day_act is "d1a4":
        $ current_chapter_number = _("Chapter 9")
        $ current_chapter_name = _("Nothing but the Truth")
    elif day_act is "d1a4_questioning_end":
        $ current_chapter_number = _("Chapter 10")
        $ current_chapter_name = _("A Hard-earned Ceasefire")
    elif day_act is "gameover":
        $ current_chapter_number = _("Chapter 0")
        $ current_chapter_name = _("BAD END")

    if day_act is "d2a1":
        $ current_chapter_number = _("Chapter 1")
        $ current_chapter_name = _("New Day, New Challenges")
    elif day_act is "d2a1_attic":
        $ current_chapter_number = _("Chapter 2")
        $ current_chapter_name = _("The Attic of Dark Secrets")
    elif day_act is "d2a1_despair":
        $ current_chapter_number = _("Chapter 3")
        $ current_chapter_name = _("Lost in the Depths of Despair")
    elif day_act is "d2a1_lounge":
        $ current_chapter_number = _("Chapter 2")
        $ current_chapter_name = _("The Lounge, Unsealed")
    elif day_act is "d2a1_judgement":
        $ current_chapter_number = _("Chapter 3")
        $ current_chapter_name = _("Hell is Where Demons Roam")
    elif day_act is "d2a2":
        $ current_chapter_number = _("Chapter 4")
        $ current_chapter_name = _("Same Day, Same Challenges")
    elif day_act is "d2a2_basement":
        $ current_chapter_number = _("Chapter 5")
        $ current_chapter_name = _("Basements Are Scary")
    elif day_act is "d2a2_basement_end":
        $ current_chapter_number = _("Chapter 6")
        $ current_chapter_name = _("The Only Escape is Death")
    elif day_act is "d2a2_light":
        $ current_chapter_number = _("Chapter 7")
        $ current_chapter_name = _("Ashen Memories")
    elif day_act is "d2a2_darkness":
        $ current_chapter_number = _("Chapter 7")
        $ current_chapter_name = _("Watch Your Back")
    elif day_act is "d2a3":
        $ current_chapter_number = _("Chapter 8")
        $ current_chapter_name = _("KYAAA!! ZOMBIES!!")
    elif day_act is "d2a3_library":
        $ current_chapter_number = _("Chapter 9")
        $ current_chapter_name = _("Taking Shelter Under Books")
    elif day_act is "d2a3_library_cece_hearttoheart":
        $ current_chapter_number = _("Chapter 10")
        $ current_chapter_name = _("A Quiet Moment with Cecilia")
    elif day_act is "gameover_day2":
        $ current_chapter_number = _("Chapter 0")
        $ current_chapter_name = _("BAD END")

    if day_act is "d3a1":
        $ current_chapter_number = _("Chapter 1")
        $ current_chapter_name = _("Climbing Out of the Abyss")
    elif day_act is "d3a1_masterbedroom_alone":
        $ current_chapter_number = _("Chapter 2")
        $ current_chapter_name = _("Loneliness")
    elif day_act is "d3a1_masterbedroom_ria_hearttoheart":
        $ current_chapter_number = _("Chapter 3")
        $ current_chapter_name = _("A Quiet Moment with Oriana")
    elif day_act is "d3a2":
        $ current_chapter_number = _("Chapter 4")
        $ current_chapter_name = _("The Worst Tragedy Imaginable")
    elif day_act is "d3a2_zombiehunt":
        $ current_chapter_number = _("Chapter 5")
        $ current_chapter_name = _("ZOMBIE HUNT! ZOMBIE HUNT!")
    elif day_act is "d3a3":
        $ current_chapter_number = _("Chapter 6")
        $ current_chapter_name = _("GAME OVER")
    elif day_act is "d3a3_trial":
        $ current_chapter_number = _("Chapter 7")
        $ current_chapter_name = _("The Final Choice")
    elif day_act is "d3a3_cecilia_ending":
        $ current_chapter_number = _("Epilogue")
        $ current_chapter_name = _("Cecilia")
    elif day_act is "d3a3_oriana_ending":
        $ current_chapter_number = _("Epilogue")
        $ current_chapter_name = _("Oriana")
    elif day_act is "d3a3_martyr_ending":
        $ current_chapter_number = _("Epilogue")
        $ current_chapter_name = _("The Path of No Regrets")
    elif day_act is "d3a4":
        $ current_chapter_number = _("Chapter 8")
        $ current_chapter_name = _("No Escaping Karma")
    elif day_act is "d3a4_salvation_ending":
        $ current_chapter_number = _("Epilogue")
        $ current_chapter_name = _("The True Ending")
    elif day_act is "d3a5":
        $ current_chapter_number = _("Chapter 9")
        $ current_chapter_name = _("Your Last Deduction")
    elif day_act is "d3a6":
        $ current_chapter_number = _("Chapter 10")
        $ current_chapter_name = _("The Professor")
    elif day_act is "d3a6_chasestart":
        $ current_chapter_number = _("Chapter 11")
        $ current_chapter_name = _("Run For Your Life")
    elif day_act is "d3a6_chase_finale":
        $ current_chapter_number = _("Chapter 12")
        $ current_chapter_name = _("Your Last Gambit")
    elif day_act is "d3a7":
        $ current_chapter_number = _("Chapter 13")
        $ current_chapter_name = _("Farewell, My Killing Game")
    elif day_act is "d3a8":
        $ current_chapter_number = _("Epilogue")
        $ current_chapter_name = _("The REAL Final Choice")
    elif day_act is "d3a8_secret":
        $ current_chapter_number = _("Epilogue")
        $ current_chapter_name = _("?????")


    $ save_name = new_save_name + " " + current_chapter_number + "\n" + current_chapter_name
    return

label name_entry:
    $ input_name = "You"
    I "What is...my name?"
    scene bg black
    show cg naming player:
        alpha 0.0
        pause 0.75
        linear 0.5 alpha 1.0
    $ quick_menu = False
    $ music_info = False
    $ input_name = renpy.input("ВВЕДИТЕ ВАШЕ {size=+15}{color=#cccc00}ИМЯ{/color}{/size}", exclude={'[', ']', '{', '}'}, default=placeholder_name, pixel_width=250)
    $ quick_menu = True
    $ music_info = True
    scene bg black with dissolve

    $ input_name = input_name.strip()

    if input_name == "" or input_name == "You":
        if input_name == "":
            $ placeholder_name = "PLAYER"
        $ input_name = "You"
        I "...I'm...having trouble remembering but..."
        I "I think I can at least think of a name to use for now..."
        jump name_entry
    else:
        $ placeholder_name = ""
        $ name_player = "{color=#cccc00}"+input_name+"{/color}"
        Y "...[name_player]..."
        I "My name is [name_player]...{w=0.5}right...?{nw}"

        menu:
            extend ""
            "\"Yes, it is.\"":
                scene bg foyer
                show oriana at myleft
                show cecilia at myright
                with fade
                return
            "\"No, my name is...\"":
                jump name_entry

label gameover:
    if not config.developer:
        $ renpy.block_rollback()
    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys

    call save_file_name_update (1, "gameover")
    scene bg black
    if shard_string == "Chaos":
        show shard chaos at appearing_shard
    if shard_string == "Order":
        show shard order at appearing_shard
    if shard_string == "Karma":
        show shard karma at appearing_shard
    with dissolve
    pause 1.5
    show text "{font=fonts/Changa-SemiBold.ttf}{size=+18}GET{/size}{/font}{image=gui/shard_arrow.png}":
        xalign 0.1 yalign 0.5
        linear 15.0 xalign 0.2
    with dissolve
    pause 10.0
    play sound sfx_shardobtain
    scene bg black
    show shard_chaos
    show shard_order
    show shard_karma
    with custom_flashbulb()
    pause 2.0

    if seen_ending_chaos and seen_ending_order and seen_ending_karma:
        $ quick_menu = True
        $ music_info = True
        hide screen lock_hotkeys
        show bg white with dissolveslow
        play loop_sfx sfx_heartbeat
        show ghostmessage_1 at truecenter with dissolvemed
        KI "Will you reject this Ending too...?"
        window auto hide
        hide ghostmessage_1 with dissolvemed
        pause 0.5
        show ghostmessage_2 at truecenter with dissolvemed
        KI "Then this time... Tell [t_clue]them[t_cluee] the truth... The WHOLE truth..."
        window auto hide
        hide ghostmessage_2 with dissolvemed
        show bg black with dissolvemed
        $ show_choicegrand = True
        $ show_choicekarma = True
        menu:
            "SEEK THE TRUTH":
                $ show_choicegrand = False
                $ show_choicekarma = False
                show shard_chaos at reset:
                    matrixcolor BrightnessMatrix(0.0) yoffset 0
                    easein 0.3 matrixcolor BrightnessMatrix(1.0)
                    easeout 0.8 yoffset -2000
                show shard_order at reset:
                    matrixcolor BrightnessMatrix(0.0) yoffset 0
                    pause 0.2
                    easein 0.3 matrixcolor BrightnessMatrix(1.0)
                    easeout 0.8 yoffset -2000
                show shard_karma at reset:
                    matrixcolor BrightnessMatrix(0.0) yoffset 0
                    pause 0.4
                    easein 0.3 matrixcolor BrightnessMatrix(1.0)
                    easeout 0.8 yoffset -2000
                stop loop_sfx
                pause 0.6
                play sound2 sfx_wail
                pause 0.6
                play sound sfx_rewind
                scene bg black with custom_flashbulblong()
                pause 3.0
                jump d1a1
    else:
        show shard_chaos:
            matrixcolor BrightnessMatrix(0.0) yoffset 0
            linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset -10
            block:
                yoffset -10
                ease 1.5 yoffset 10
                ease 1.5 yoffset -10
                repeat
        show shard_order:
            matrixcolor BrightnessMatrix(0.0) yoffset 0
            linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset 5
            block:
                yoffset 5
                ease 0.75 yoffset 10
                ease 1.5 yoffset -10
                ease 0.75 yoffset 5
                repeat
        show shard_karma:
            matrixcolor BrightnessMatrix(0.0) yoffset 0
            linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset -5
            block:
                yoffset -5
                ease 0.75 yoffset -10
                ease 1.5 yoffset 10
                ease 0.75 yoffset -5
                repeat
        pause 3.0
        play music bgm_badend
        show logo at truecenter
        with dissolvemed
        pause 3.0
        show screen credits()
        hide logo
        with dissolvemed
        pause 9.0
        menu:
            "Reject this Ending":
                pause 1.0
                hide screen credits with custom_flashquickred()
                show shard_chaos at reset:
                    matrixcolor InvertMatrix(1.0)
                show shard_order at reset:
                    matrixcolor InvertMatrix(1.0)
                show shard_karma at reset:
                    matrixcolor InvertMatrix(1.0)
                stop music
                play ctc_sfx sfx_heartbeat_single
                S "You have successfully rejected this ending.{w=0.5}\nSending [name_player] to the start of another [t_clue]killing game[t_cluee]...{w=0.5}{nw}"
                play ctc_sfx "<silence 1.0>"
                $ show_choicegrand = True
                $ mute_choice = True

                menu:
                    extend ""
                    "START ANOTHER KILLING GAME":
                        $ show_choicegrand = False
                        $ mute_choice = False
                        play audio sfx_choicegrand
                        pause 0.5
                        play sound sfx_rewind
                        scene bg black with pixellate
                        pause 6.0
                        $ quick_menu = True
                        $ music_info = True
                        hide screen lock_hotkeys
                        $ day1_loop_count = day1_loop_count + 1
                        jump d1a1
label gameover_day2:
    if not config.developer:
        $ renpy.block_rollback()
    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys
    call save_file_name_update (2, "gameover_day2")
    scene bg black
    if shard_string == "Despair":
        show shard despair at appearing_shard
    if shard_string == "Judgement":
        show shard judgement at appearing_shard
    if shard_string == "Light":
        show shard light at appearing_shard
    if shard_string == "Darkness":
        show shard darkness at appearing_shard
    with dissolve
    pause 1.5
    show text "{font=fonts/Changa-SemiBold.ttf}{size=+18}GET{/size}{/font}{image=gui/shard_arrow.png}":
        xalign 0.1 yalign 0.5
        linear 15.0 xalign 0.2
    with dissolve
    pause 10.0
    play sound sfx_shardobtain
    scene bg black
    $ backshard_layers = 0
    if seen_ending_despair:
        $ backshard_layers += 1
    if seen_ending_judgement:
        $ backshard_layers += 1
    if seen_ending_light:
        $ backshard_layers += 1
    if seen_ending_darkness:
        $ backshard_layers += 1
    call show_backshards
    show shard_chaos
    show shard_order
    show shard_karma
    if seen_ending_despair:
        show shard_despair
    if seen_ending_judgement:
        show shard_judgement
    if seen_ending_light:
        show shard_light
    if seen_ending_darkness:
        show shard_darkness
    with custom_flashbulb()
    pause 2.0

    show shard_chaos:
        matrixcolor BrightnessMatrix(0.0) yoffset 0
        linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat
    show shard_order:
        matrixcolor BrightnessMatrix(0.0) yoffset 0
        linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset 5
        block:
            yoffset 5
            ease 0.75 yoffset 10
            ease 1.5 yoffset -10
            ease 0.75 yoffset 5
            repeat
    show shard_karma:
        matrixcolor BrightnessMatrix(0.0) yoffset 0
        linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset -5
        block:
            yoffset -5
            ease 0.75 yoffset -10
            ease 1.5 yoffset 10
            ease 0.75 yoffset -5
            repeat
    if seen_ending_despair:
        show shard_despair:
            matrixcolor BrightnessMatrix(0.0) yoffset 0
            linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset -10
            block:
                yoffset -10
                ease 1.5 yoffset 10
                ease 1.5 yoffset -10
                repeat
    if seen_ending_judgement:
        show shard_judgement:
            matrixcolor BrightnessMatrix(0.0) yoffset 0
            linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset 5
            block:
                yoffset 5
                ease 0.75 yoffset 10
                ease 1.5 yoffset -10
                ease 0.75 yoffset 5
                repeat
    if seen_ending_light:
        show shard_light:
            matrixcolor BrightnessMatrix(0.0) yoffset 0
            linear 2.5 matrixcolor BrightnessMatrix(-0.15) yoffset 5
            block:
                yoffset 5
                ease 0.75 yoffset 10
                ease 1.5 yoffset -10
                ease 0.75 yoffset 5
                repeat
    if seen_ending_darkness:
        show shard_darkness:
            matrixcolor BrightnessMatrix(0.0) yoffset 0
            linear 2.0 matrixcolor BrightnessMatrix(-0.15) yoffset 5
            block:
                yoffset 5
                ease 0.75 yoffset 10
                ease 1.5 yoffset -10
                ease 0.75 yoffset 5
                repeat
    pause 3.0
    play music bgm_badend
    show logo at truecenter
    with dissolvemed
    pause 3.0
    show screen credits()
    hide logo
    with dissolvemed
    pause 9.0
    menu:
        "Reject this Ending":
            pause 1.0
            hide screen credits with custom_flashquickred()
            show shard_chaos at reset:
                matrixcolor InvertMatrix(1.0)
            show shard_order at reset:
                matrixcolor InvertMatrix(1.0)
            show shard_karma at reset:
                matrixcolor InvertMatrix(1.0)
            if seen_ending_despair:
                show shard_despair at reset:
                    matrixcolor InvertMatrix(1.0)
            if seen_ending_judgement:
                show shard_judgement at reset:
                    matrixcolor InvertMatrix(1.0)
            if seen_ending_light:
                show shard_light at reset:
                    matrixcolor InvertMatrix(1.0)
            if seen_ending_darkness:
                show shard_darkness at reset:
                    matrixcolor InvertMatrix(1.0)
            hide backshards_1
            hide backshards_2
            hide backshards_3
            hide backshards_4
            stop music
            play ctc_sfx sfx_heartbeat_single
            S "You have successfully rejected this ending.{w=0.5}\nSending [name_player] to {color=#fff}Part II{/color} of another [t_clue]killing game[t_cluee]...{w=0.5}{nw}"
            play ctc_sfx "<silence 1.0>"
            $ show_choicegrand = True
            $ mute_choice = True

            menu:
                "I WANT MORE KILLING GAMES" if seen_ending_darkness:
                    pass
                "ON TO THE NEXT KILLING GAME" if seen_ending_judgement:
                    pass
                "START ANOTHER KILLING GAME":
                    pass
                "LET'S PLAY ANOTHER KILLING GAME" if seen_ending_despair:
                    pass
                "ENJOYING THE KILLING GAMES?" if seen_ending_light:
                    pass
                extend ""
            $ show_choicegrand = False
            $ mute_choice = False
            play audio sfx_choicegrand
            pause 0.5
            play sound sfx_rewind
            scene bg black with pixellate
            pause 6.0
            $ quick_menu = True
            $ music_info = True
            hide screen lock_hotkeys
            if seen_ending_despair and seen_ending_judgement:
                jump d2a2
            else:
                jump d2a1
label main_menu_credits:
    $ _autosave = False
    $ _skipping = False
    $ renpy.block_rollback()
    $ quick_menu = False
    $ music_info = False
    show screen lock_hotkeys
    call screen credits(90, True, True)
    $ quick_menu = True
    $ music_info = True
    hide screen lock_hotkeys
    $ _skipping = True
    $ _autosave = True
    return

label show_backshards:
    if backshard_layers == 4:
        show backshards_1:
            alpha 0.0
            linear 4.0 alpha 1.0
            linear 2.0 yoffset -5
            block:
                yoffset -5
                ease 1.5 yoffset 5
                ease 1.5 yoffset -5
                repeat
        show backshards_2:
            alpha 0.0
            linear 4.0 alpha 1.0
            linear 2.5 yoffset -8
            block:
                yoffset -8
                ease 1.5 yoffset 8
                ease 1.5 yoffset -8
                repeat
        show backshards_3:
            alpha 0.0
            linear 4.0 alpha 1.0
            linear 3.0 yoffset -10
            block:
                yoffset -10
                ease 1.5 yoffset 10
                ease 1.5 yoffset -10
                repeat
        show backshards_4:
            alpha 0.0
            linear 4.0 alpha 1.0
            linear 3.5 yoffset -12
            block:
                yoffset -12
                ease 1.5 yoffset 12
                ease 1.5 yoffset -12
                repeat
    elif backshard_layers == 3:
        show backshards_1:
            alpha 0.0
            linear 4.0 alpha 0.8
            linear 2.0 yoffset -5
            block:
                yoffset -5
                ease 1.5 yoffset 5
                ease 1.5 yoffset -5
                repeat
        show backshards_2:
            alpha 0.0
            linear 4.0 alpha 0.8
            linear 2.5 yoffset -8
            block:
                yoffset -8
                ease 1.5 yoffset 8
                ease 1.5 yoffset -8
                repeat
        show backshards_3:
            alpha 0.0
            linear 4.0 alpha 0.8
            linear 3.0 yoffset -10
            block:
                yoffset -10
                ease 1.5 yoffset 10
                ease 1.5 yoffset -10
                repeat
    elif backshard_layers == 2:
        show backshards_1:
            alpha 0.0
            linear 4.0 alpha 0.4
            linear 2.0 yoffset -5
            block:
                yoffset -5
                ease 1.5 yoffset 5
                ease 1.5 yoffset -5
                repeat
        show backshards_2:
            alpha 0.0
            linear 4.0 alpha 0.4
            linear 3.0 yoffset -8
            block:
                yoffset -8
                ease 1.5 yoffset 8
                ease 1.5 yoffset -8
                repeat
    elif backshard_layers == 1:
        show backshards_1:
            alpha 0.0
            linear 4.0 alpha 0.2
            linear 2.0 yoffset -5
            block:
                yoffset -5
                ease 1.5 yoffset 5
                ease 1.5 yoffset -5
                repeat
    return

label ending_test:
    scene bg black
    show shard_chaos
    show shard_order
    show shard_karma
    "no layers"
    scene bg black

    show backshards_1:
        alpha 0.2
        linear 2.0 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat

    show shard_chaos
    show shard_order
    show shard_karma
    show shard_despair
    "1 layer"
    scene bg black

    show backshards_1:
        alpha 0.4
        linear 2.0 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat
    show backshards_2:
        alpha 0.4
        linear 3.0 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat

    show shard_chaos
    show shard_order
    show shard_karma
    show shard_despair
    show shard_judgement
    "2 layers"
    scene bg black

    show backshards_1:
        alpha 0.8
        linear 2.0 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat
    show backshards_2:
        alpha 0.8
        linear 2.5 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat
    show backshards_3:
        alpha 0.8
        linear 3.0 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat

    show shard_chaos
    show shard_order
    show shard_karma
    show shard_despair
    show shard_judgement
    show shard_light
    "3 layers"
    scene bg black

    show backshards_1:
        linear 2.0 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat
    show backshards_2:
        linear 2.5 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat
    show backshards_3:
        linear 3.0 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat
    show backshards_4:
        linear 3.5 yoffset -10
        block:
            yoffset -10
            ease 1.5 yoffset 10
            ease 1.5 yoffset -10
            repeat

    show shard_chaos
    show shard_order
    show shard_karma
    show shard_despair
    show shard_judgement
    show shard_light
    show shard_darkness
    "4 layers"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
