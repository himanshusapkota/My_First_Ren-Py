
define The_Knight = Character("Knight", color="#E03B8B")
define Unknown = Character("Unknown", color="#AAAAAA")



image knight neutral1 = "images/Neutral 1.png"
image knight neutral2 = "images/Neutral 2.png"
image knight angry = "images/Angry.png"
image knight sad = "images/Sad.png"
image knight shock = "images/Shock.png"
image knight smile1 = "images/Smile 1.png"
image knight smile2 = "images/Smile 2.png"
image knight smirk1 = "images/Smirk 1.png"
image knight smirk2 = "images/Smirk 2.png"




image bg room = "images/bg room.jpg"
image phone = "images/phone.png"



default picked_phone = False




label start:

    scene bg room:
        fit "cover"

    with fade

    show knight neutral1:
        zoom 1.5
        xalign 0.5
        yalign 1.0

    The_Knight "Where am I?"

    The_Knight "..."

    show knight shock:
        zoom 1.5
        xalign 0.5
        yalign 1.0

    The_Knight "What am I even doing here?!"

    The_Knight "Is anybody here?!"

    show knight angry:
        zoom 1.5
        xalign 0.5
        yalign 1.0

    The_Knight "Seriously... where is everyone?"

    show knight sad:
        zoom 1.5
        xalign 0.5
        yalign 1.0

    The_Knight "I don't remember anything..."

    show knight neutral1:
        zoom 1.5
        xalign 0.5
        yalign 1.0

    The_Knight "I guess I'll have to figure this out myself."


  

    show phone:
        zoom 0.5
        xalign 0.82
        yalign 0.72

    with dissolve

    play sound "audio/phone_ring.wav"

    The_Knight "Wait..."

    The_Knight "What's that?"

    The_Knight "A phone?"

    show knight shock:
        zoom 1.5
        xalign 0.5
        yalign 1.0

    The_Knight "Why is there a phone here?"

    The_Knight "And why is it ringing?"


  

    menu:

        "Pick up the phone":

            $ picked_phone = True

        "Don't pick up the phone":

            $ picked_phone = False



    if picked_phone:

        stop sound

        hide phone

        show knight neutral2:
            zoom 1.5
            xalign 0.5
            yalign 1.0

        The_Knight "Okay..."

        The_Knight "I'm picking it up."

        play sound "audio/phone_pickup.wav"

        The_Knight "Hello?"

        play sound "audio/footstep.wav"

        Unknown "You shouldn't have answered."

        show knight shock:
            zoom 1.5
            xalign 0.5
            yalign 1.0

        The_Knight "Who are you?!"

        Unknown "You have made a mistake."

        The_Knight "What do you mean?!"

        play sound "audio/horror_hit.wav"

        scene black with fade

        The_Knight "Oh no..."

        Unknown "You should have listened."

        "..."

        "ENDING 1: THE CALL"

        return



    else:

        stop sound

        hide phone

        show knight neutral1:
            zoom 1.5
            xalign 0.5
            yalign 1.0

        The_Knight "Nope."

        The_Knight "I'm not picking that up."

        The_Knight "Something feels really wrong."

        The_Knight "I'm going to leave it alone."

        show knight smile1:
            zoom 1.5
            xalign 0.5
            yalign 1.0

        The_Knight "Yeah..."

        The_Knight "That was definitely the right decision."

        "The phone suddenly stops ringing."

        show knight shock:
            zoom 1.5
            xalign 0.5
            yalign 1.0

        The_Knight "Wait..."

        The_Knight "What was that sound?"

        play sound "audio/footstep.wav"

        The_Knight "..."

        play sound "audio/footstep.wav"

        The_Knight "Who's there?"

        play sound "audio/horror_hit.wav"

        scene black with fade

        Unknown "You should have answered."

        The_Knight "..."

        "ENDING 2: THE SILENCE"

        return