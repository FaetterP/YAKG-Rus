default persistent.unlock_cg_wakeup = False
default persistent.unlock_cg_mirror = False
default persistent.unlock_cg_mirror2 = False
default persistent.unlock_cg_chaos = False
default persistent.unlock_cg_chaos1 = False
default persistent.unlock_cg_chaos2 = False
default persistent.unlock_cg_order = False
default persistent.unlock_cg_karma = False
default persistent.unlock_cg_shower = False
default persistent.unlock_cg_despair = False
default persistent.unlock_cg_judgement = False
default persistent.unlock_cg_origin_cecilia = False
default persistent.unlock_cg_cece_hearttoheart = False
default persistent.unlock_cg_origin_oriana = False
default persistent.unlock_cg_ria_hearttoheart = False
default persistent.unlock_cg_deaddog = False
default persistent.unlock_cg_hope = False
default persistent.unlock_cg_trueend = False

default persistent.unlock_cg_floordiagram = False
default persistent.unlock_gameclear_cgs = False

default persistent.unlock_bg_foyer = False
default persistent.unlock_bg_foyer_dark = False
default persistent.unlock_bg_frontdoor_incomplete = False
default persistent.unlock_bg_frontdoor = False
default persistent.unlock_bg_frontdoor_open = False
default persistent.unlock_bg_diningroom_withchair = False
default persistent.unlock_bg_diningroom_withchair_dark = False
default persistent.unlock_bg_diningroom = False
default persistent.unlock_bg_diningroom_dark = False

default persistent.unlock_bg_kitchen_fullknives = False
default persistent.unlock_bg_kitchen = False
default persistent.unlock_bg_kitchen_twoknives = False
default persistent.unlock_bg_bathroom = False
default persistent.unlock_bg_bathroom_sinkon = False
default persistent.unlock_bg_hallway = False
default persistent.unlock_bg_hallway_dark = False
default persistent.unlock_bg_hallwayend = False
default persistent.unlock_bg_hallwayend_dark = False
default persistent.unlock_bg_hallwayend_withladder = False
default persistent.unlock_bg_bedroom = False
default persistent.unlock_bg_bedroom_dark = False
default persistent.unlock_bg_bedroom_corpse = False
default persistent.unlock_bg_emptybedroom = False
default persistent.unlock_bg_emptybedroom_dark_chaos = False
default persistent.unlock_bg_emptybedroom_dark_chaos2 = False
default persistent.unlock_bg_emptybedroom_dark = False
default persistent.unlock_bg_masterbedroom = False
default persistent.unlock_bg_masterbedroom_dark = False
default persistent.unlock_bg_masterbathroom = False


default persistent.unlock_bg_attic = False
default persistent.unlock_bg_attic_nobottle = False
default persistent.unlock_bg_attic_dark = False
default persistent.unlock_bg_lounge = False
default persistent.unlock_bg_lounge_dark = False
default persistent.unlock_bg_basement_entrance = False
default persistent.unlock_bg_basement_entrance_light = False
default persistent.unlock_bg_basement = False
default persistent.unlock_bg_basement_nocorpse = False
default persistent.unlock_bg_basement_hatch = False
default persistent.unlock_bg_bloodpool = False
default persistent.unlock_bg_flamewall = False
default persistent.unlock_bg_library = False
default persistent.unlock_bg_library_dark = False
default persistent.unlock_bg_basement_stairway = False
default persistent.unlock_bg_secretending = False
















screen _gallery(locked, displayables, index, count, gallery, **properties):

    if locked:
        add "#000"
        text _("Image [index]/[count] locked.") align (0.5, 0.5)
    else:
        for d in displayables:
            add d

    if gallery.slideshow:
        timer gallery.slideshow_delay action Return("next") repeat True

    key "game_menu" action gallery.Return()

    if gallery.navigation:
        use gallery_navigation(gallery=gallery)

screen gallery_navigation(gallery):
    hbox:
        spacing 20

        style_group "gallery"
        align (.98, .98)

        textbutton _("Prev") action gallery.Previous(unlocked=gallery.unlocked_advance)
        textbutton _("Next") action gallery.Next(unlocked=gallery.unlocked_advance)
        textbutton _("Slideshow") action gallery.ToggleSlideshow()
        textbutton _("Return") action gallery.Return()


init python:

    g = Gallery()

    g.unlocked_advance = True
    g.transition = Dissolve(0.25)
    g.locked_button = "thumbnails/tn_locked.png"
    g.idle_border = "thumbnails/tn_idle.png"
    g.hover_border = "thumbnails/tn_hover.png"



    g.button("wakeup")
    g.condition("persistent.unlock_cg_wakeup")
    g.image("cg wakeup")

    g.button("mirror")
    g.condition("persistent.unlock_cg_mirror")
    g.image("cg mirror")
    g.image("cg mirror2")
    g.condition("persistent.unlock_cg_mirror2")

    g.button("chaos")
    g.condition("persistent.unlock_cg_chaos")
    g.image("cg chaos")
    g.image("cg chaos1")
    g.condition("persistent.unlock_cg_chaos1")
    g.image("cg chaos2")
    g.condition("persistent.unlock_cg_chaos2")

    g.button("order")
    g.condition("persistent.unlock_cg_order")
    g.image("cg order")

    g.button("karma")
    g.condition("persistent.unlock_cg_karma")
    g.image("cg karma1")
    g.image("cg karma2")
    g.image("cg karma")

    g.button("karma4")
    g.condition("persistent.unlock_cg_karma")
    g.image("cg karma4")

    g.button("shower")
    g.condition("persistent.unlock_cg_shower")
    g.image("cg shower2")
    g.image("cg shower")

    g.button("despair")
    g.condition("persistent.unlock_cg_despair")
    g.image("cg despair")

    g.button("judgement")
    g.condition("persistent.unlock_cg_judgement")
    g.image("cg judgement")

    g.button("origin cecilia")
    g.condition("persistent.unlock_cg_origin_cecilia")
    g.image("cg origin cecilia")
    g.image("cg origin cecilia1")

    g.button("origin cecilia2")
    g.condition("persistent.unlock_cg_origin_cecilia")
    g.image("cg origin cecilia2")
    g.image("cg origin cecilia3")

    g.button("cece hearttoheart")
    g.condition("persistent.unlock_cg_cece_hearttoheart")
    g.image("cg cece hearttoheart")
    g.image("cg cece hearttoheart2")

    g.button("origin oriana")
    g.condition("persistent.unlock_cg_origin_oriana")
    g.image("cg origin oriana")

    g.button("origin oriana1")
    g.condition("persistent.unlock_cg_origin_oriana")
    g.image("cg origin oriana1")

    g.button("ria hearttoheart")
    g.condition("persistent.unlock_cg_ria_hearttoheart")
    g.image("cg ria hearttoheart")
    g.image("cg ria hearttoheart2")

    g.button("deaddog")
    g.condition("persistent.unlock_cg_deaddog")
    g.image("cg deaddog")

    g.button("hope")
    g.condition("persistent.unlock_cg_hope")
    g.image("cg hope")

    g.button("trueend")
    g.condition("persistent.unlock_cg_trueend")
    g.image("cg trueend")

    g.button("floordiagram")
    g.condition("persistent.unlock_cg_floordiagram")
    g.image("cg floordiagram")


    g.button("allshards")
    g.condition("persistent.unlock_gameclear_cgs")
    g.image("cg allshards")

    g.button("naming player")
    g.condition("persistent.unlock_gameclear_cgs")
    g.image("cg naming player")

    g.button("eyecatch cecilia")
    g.condition("persistent.unlock_gameclear_cgs")
    g.image("cg eyecatch cecilia bloody")
    g.image("cg eyecatch cecilia")

    g.button("eyecatch oriana")
    g.condition("persistent.unlock_gameclear_cgs")
    g.image("cg eyecatch oriana bloody")
    g.image("cg eyecatch oriana")

    g.button("eyecatch empty")
    g.condition("persistent.unlock_gameclear_cgs")
    g.image("cg eyecatch empty")

    g.button("keyvisual side")
    g.condition("persistent.unlock_gameclear_cgs")
    g.image("cg keyvisual side")


    g.button("foyer")
    g.condition("persistent.unlock_bg_foyer")
    g.image("bg foyer")
    g.image("bg foyer dark")
    g.condition("persistent.unlock_bg_foyer_dark")

    g.button("frontdoor")
    g.condition("persistent.unlock_bg_frontdoor_incomplete")
    g.image("bg frontdoor incomplete")
    g.image("bg frontdoor")
    g.condition("persistent.unlock_bg_frontdoor")
    g.image("bg frontdoor open")
    g.condition("persistent.unlock_bg_frontdoor_open")

    g.button("diningroom")
    g.condition("persistent.unlock_bg_diningroom_withchair")
    g.image("bg diningroom withchair")
    g.image("bg diningroom withchair dark")
    g.condition("persistent.unlock_bg_diningroom_withchair_dark")
    g.image("bg diningroom")
    g.condition("persistent.unlock_bg_diningroom")
    g.image("bg diningroom dark")
    g.condition("persistent.unlock_bg_diningroom_dark")

    g.button("kitchen")
    g.condition("persistent.unlock_bg_kitchen_fullknives")
    g.image("bg kitchen fullknives")
    g.image("bg kitchen")
    g.condition("persistent.unlock_bg_kitchen")
    g.image("bg kitchen twoknives")
    g.condition("persistent.unlock_bg_kitchen_twoknives")

    g.button("bathroom")
    g.condition("persistent.unlock_bg_bathroom")
    g.image("bg bathroom")
    g.image("bg bathroom sinkon")
    g.condition("persistent.unlock_bg_bathroom_sinkon")

    g.button("hallway")
    g.condition("persistent.unlock_bg_hallway")
    g.image("bg hallway")
    g.image("bg hallway dark")
    g.condition("persistent.unlock_bg_hallway_dark")

    g.button("hallwayend")
    g.condition("persistent.unlock_bg_hallwayend")
    g.image("bg hallwayend")
    g.image("bg hallwayend dark")
    g.condition("persistent.unlock_bg_hallwayend_dark")
    g.image("bg hallwayend withladder")
    g.condition("persistent.unlock_bg_hallwayend_withladder")

    g.button("bedroom")
    g.condition("persistent.unlock_bg_bedroom")
    g.image("bg bedroom")
    g.image("bg bedroom dark")
    g.condition("persistent.unlock_bg_bedroom_dark")
    g.image("bg bedroom corpse")
    g.condition("persistent.unlock_bg_bedroom_corpse")

    g.button("emptybedroom")
    g.condition("persistent.unlock_bg_emptybedroom")
    g.image("bg emptybedroom")
    g.image("bg emptybedroom dark chaos")
    g.condition("persistent.unlock_bg_emptybedroom_dark_chaos")
    g.image("bg emptybedroom dark chaos2")
    g.condition("persistent.unlock_bg_emptybedroom_dark_chaos2")
    g.image("bg emptybedroom dark")
    g.condition("persistent.unlock_bg_emptybedroom_dark")

    g.button("masterbedroom")
    g.condition("persistent.unlock_bg_masterbedroom")
    g.image("bg masterbedroom")
    g.image("bg masterbedroom dark")
    g.condition("persistent.unlock_bg_masterbedroom_dark")

    g.button("masterbathroom")
    g.condition("persistent.unlock_bg_masterbathroom")
    g.image("bg masterbathroom")

    g.button("attic")
    g.condition("persistent.unlock_bg_attic")
    g.image("bg attic")
    g.image("bg attic nobottle")
    g.condition("persistent.unlock_bg_attic_nobottle")
    g.image("bg attic dark")
    g.condition("persistent.unlock_bg_attic_dark")

    g.button("lounge")
    g.condition("persistent.unlock_bg_lounge")
    g.image("bg lounge")
    g.image("bg lounge dark")
    g.condition("persistent.unlock_bg_lounge_dark")

    g.button("basement entrance")
    g.condition("persistent.unlock_bg_basement_entrance")
    g.image("bg basement entrance")
    g.image("bg basement entrance light")
    g.condition("persistent.unlock_bg_basement_entrance_light")

    g.button("basement")
    g.condition("persistent.unlock_bg_basement")
    g.image("bg basement")
    g.image("bg basement nocorpse")
    g.condition("persistent.unlock_bg_basement_nocorpse")

    g.button("basement hatch")
    g.condition("persistent.unlock_bg_basement_hatch")
    g.image("bg basement hatch")

    g.button("bloodpool")
    g.condition("persistent.unlock_bg_bloodpool")
    g.image("bg bloodpool 1")
    g.image("bg bloodpool 2")
    g.image("bg bloodpool 3")

    g.button("flamewall")
    g.condition("persistent.unlock_bg_flamewall")
    g.image("bg flamewall1")
    g.image("bg flamewall2")
    g.image("bg flamewall3")

    g.button("library")
    g.condition("persistent.unlock_bg_library")
    g.image("bg library zoomedout")
    g.image("bg library right")
    g.image("bg library left")
    g.image("bg library dark zoomedout")
    g.condition("persistent.unlock_bg_library_dark")
    g.image("bg library dark right")
    g.condition("persistent.unlock_bg_library_dark")
    g.image("bg library dark left")
    g.condition("persistent.unlock_bg_library_dark")

    g.button("basement stairway")
    g.condition("persistent.unlock_bg_basement_stairway")
    g.image("bg basement stairway")

    g.button("secretending")
    g.condition("persistent.unlock_bg_secretending")
    g.image("bg secretending2")

screen navigation_gallery:
    hbox:
        xalign 0.5 spacing 10
        button:
            text _("CGs"):
                style "gallery_navigation_button_text"
                insensitive_color gui.accent_color
            action ([SetScreenVariable("gallery_type", "cgs"), SetScreenVariable("gallery_page", 1)] if gallery_type != "cgs" else None)
        textbutton "|" action None
        button:
            text _("Backgrounds"):
                style "gallery_navigation_button_text"
                insensitive_color gui.accent_color
            action ([SetScreenVariable("gallery_type", "backgrounds"), SetScreenVariable("gallery_page", 1)] if gallery_type != "backgrounds" else None)
        textbutton "|" action None
        button:
            text _("Music Room"):
                style "gallery_navigation_button_text"
                insensitive_color gui.accent_color
            action (SetScreenVariable("gallery_type", "music_room") if gallery_type != "music_room" else None)

screen navigation_gallery_page:
    hbox:

        xalign 0.5 spacing 10
        button:
            text _("<"):
                style "gallery_navigation_button_text"
            action (SetScreenVariable("gallery_page", max(gallery_page - 1, 1)) if gallery_page > 1 else None)
        button:
            text _("1"):
                style "gallery_navigation_button_text"
                insensitive_color gui.accent_color
            action (SetScreenVariable("gallery_page", 1) if gallery_page != 1 else None)
        button:
            text _("2"):
                style "gallery_navigation_button_text"
                insensitive_color gui.accent_color
            action (SetScreenVariable("gallery_page", 2) if gallery_page != 2 else None)
        button:
            text _("3"):
                style "gallery_navigation_button_text"
                insensitive_color gui.accent_color
            action (SetScreenVariable("gallery_page", 3) if gallery_page != 3 else None)
        button:
            text _(">"):
                style "gallery_navigation_button_text"
            action (SetScreenVariable("gallery_page", min(gallery_page + 1, 3)) if gallery_page < 3 else None)

style gallery_navigation_button_text is navigation_button_text:
    idle_color gui.idle_color
    hover_color gui.hover_color
    font "fonts/Changa-SemiBold.ttf"

screen gallery_main:
    tag menu



    default gallery_type = "cgs"
    default gallery_page = 1

    use game_menu(_("Gallery")):

        vbox:
            xfill True
            xalign 0.5 ypos -40
            use navigation_gallery

            if gallery_type == "cgs" or gallery_type == "backgrounds":
                use navigation_gallery_page
                null height 24
                grid 3 3:
                    xalign 0.5 yalign 0.5
                    spacing 10
                    yspacing -35

                    if gallery_type == "cgs":
                        if gallery_page == 1:
                            use gallery_cgs_pg1
                        elif gallery_page == 2:
                            use gallery_cgs_pg2
                        elif gallery_page == 3:
                            use gallery_cgs_pg3
                    elif gallery_type == "backgrounds":
                        if gallery_page == 1:
                            use gallery_bgs_pg1
                        elif gallery_page == 2:
                            use gallery_bgs_pg2
                        elif gallery_page == 3:
                            use gallery_bgs_pg3
            elif gallery_type == "music_room":
                use music_room

transform gallery_button_transform:
    alpha 0.5
    on hover:
        matrixcolor BrightnessMatrix(1.0)

style gallery_button_style:
    hover_sound "sound/sfx_pac_hover.ogg"
    activate_sound "sound/sfx_pac_select.ogg"

screen gallery_cgs_pg1:
    use gallery_button("wakeup", "backgrounds/cg wakeup.png")
    use gallery_button("mirror", "backgrounds/cg mirror.png")
    use gallery_button("chaos", "backgrounds/cg chaos.png")

    use gallery_button("order", "backgrounds/cg order.png")
    use gallery_button("karma", "backgrounds/cg karma.png")
    use gallery_button("karma4", "backgrounds/cg karma4.png")

    use gallery_button("shower", "backgrounds/cg shower.png")
    use gallery_button("despair", "backgrounds/cg despair.png")
    use gallery_button("judgement", "backgrounds/cg judgement.png")

screen gallery_cgs_pg2:
    use gallery_button("origin cecilia", "backgrounds/cg origin cecilia.png")
    use gallery_button("origin cecilia2", "backgrounds/cg origin cecilia2.png")
    use gallery_button("cece hearttoheart", "backgrounds/cg cece hearttoheart.png")

    use gallery_button("origin oriana", "backgrounds/cg origin oriana.png")
    use gallery_button("origin oriana1", "backgrounds/cg origin oriana1.png")
    use gallery_button("ria hearttoheart", "backgrounds/cg ria hearttoheart.png")

    use gallery_button("deaddog", "backgrounds/cg deaddog.png")
    use gallery_button("hope", "backgrounds/cg hope.png")
    use gallery_button("trueend", "backgrounds/cg trueend.png")

screen gallery_cgs_pg3:
    use gallery_button("floordiagram", "backgrounds/cg floordiagram.png")
    use gallery_button("allshards", "backgrounds/cg allshards.png")
    use gallery_button("naming player", "backgrounds/cg naming player.png")

    use gallery_button("eyecatch cecilia", "backgrounds/cg eyecatch cecilia.png")
    use gallery_button("eyecatch oriana", "backgrounds/cg eyecatch oriana.png")
    use gallery_button("eyecatch empty", "backgrounds/cg eyecatch empty.png")

    use gallery_button("keyvisual side", "backgrounds/cg keyvisual side.png")

screen gallery_bgs_pg1:
    use gallery_button("foyer", "backgrounds/bg foyer.png")
    use gallery_button("frontdoor", "backgrounds/bg frontdoor incomplete.png")
    use gallery_button("diningroom", "backgrounds/bg diningroom withchair.png")

    use gallery_button("kitchen", "backgrounds/bg kitchen.png")
    use gallery_button("bathroom", "backgrounds/bg bathroom.png")
    use gallery_button("hallway", "backgrounds/bg hallway.png")

    use gallery_button("hallwayend", "backgrounds/bg hallwayend.png")
    use gallery_button("bedroom", "backgrounds/bg bedroom.png")
    use gallery_button("emptybedroom", "backgrounds/bg emptybedroom.png")

screen gallery_bgs_pg2:
    use gallery_button("masterbedroom", "backgrounds/bg masterbedroom.png")
    use gallery_button("masterbathroom", "backgrounds/bg masterbathroom.png")
    use gallery_button("lounge", "backgrounds/bg lounge.png")

    use gallery_button("attic", "backgrounds/bg attic.png")
    use gallery_button("basement entrance", "backgrounds/bg basement entrance.png")
    use gallery_button("basement", "backgrounds/bg basement.png")

    use gallery_button("basement hatch", "backgrounds/bg basement hatch.png")
    use gallery_button("bloodpool", "backgrounds/bg bloodpool 2.png")
    use gallery_button("flamewall", "backgrounds/bg flamewall1.png")

screen gallery_bgs_pg3:
    use gallery_button("library", "backgrounds/bg library gallery.png")
    use gallery_button("basement stairway", "backgrounds/bg basement stairway.png")
    use gallery_button("secretending", "backgrounds/bg secretending.png")

screen gallery_button(name, thumbnail_filename):
    vbox:
        add g.make_button(name, unlocked=im.Scale(thumbnail_filename, 384, 216), style="gallery_button_style", transform="gallery_button_transform", mouse="examine")
        if g.get_fraction(name, format=u'{total}') != '1' and g.buttons[name].check_unlock():
            text g.get_fraction(name, format=u'{seen}/{total}') xalign 0.97 yanchor 0.0 ypos -1.1 color ("#44b817" if g.get_fraction(name, format=u'{seen}') is g.get_fraction(name, format=u'{total}') else "#fff") outlines [(2, "#000", 0, 0)]
        else:
            text "" xalign 0.97 yanchor 0.0 ypos -1.1 color "#fff" outlines [(2, "#000", 0, 0)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
