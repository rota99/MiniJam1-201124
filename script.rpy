# Questo è il file script.rpy per il tuo progetto Ren'Py
label start:
    # Introduzione alla storia
    scene bg room with fade
    show character luca happy
    "It has been a long and challenging day, filled with endless tasks and moments of tension. But now, as the day finally comes to an end, it's time to retreat to the comfort of bed. At last, I can close my eyes, let go of the day's worries, and embrace the peaceful rest I’ve been yearning for."
    
    # Menu di scelta
    menu:
        "Turn off the light":
            "You reach out and switch off the light. The room falls into a calming darkness, and you feel yourself drifting into sleep."
            jump next_scene

        "Leave the light on":
            "You decide to leave the light on, its faint glow offering a comforting presence as you close your eyes."
            jump next_scene
    


label next_scene:
    scene bg room with fade
    show character chiara neutral
    
    " Good night !!!"
    " zzzzzz  ... zzzz"
    "Chiara is deep asleep, her mind wandering into a strange, dark dream. Suddenly, she finds herself in a vast, shadowy forest. The air is heavy, and the silence is unsettling."

    "Out of the mist, a terrifying creature appears, its glowing eyes locking onto her. It's tall, monstrous, and moves with an unnatural speed."

    menu:
        "Run away":
            $ action = "run"
            "Chiara's heart races as she turns and runs through the dense forest, the sounds of the monster’s footsteps echoing behind her."
            jump monster_chase

        "Stand still and face the monster":
            $ action = "face"
            "Chiara takes a deep breath and stands still, glaring at the monster. It stops for a moment, then begins to growl menacingly."
            jump monster_faceoff

label monster_chase:
    scene bg forest_dark with dissolve
    "Chiara's legs burn as she sprints, branches whipping past her. The monster is gaining on her, its growl growing louder with each passing moment."
    "She can hear its breath behind her, hot and ragged."

    menu:
        "Climb a tree":
            $ action = "climb"
            "Chiara leaps toward a large tree, scrambling up the rough bark. She manages to get high enough to escape the monster's reach."
            jump escape_tree

        "Keep running":
            $ action = "run_more"
            "Chiara pushes herself even harder, her fear giving her strength. But the monster is right behind her now, almost within reach."
            jump final_chase

label monster_faceoff:
    scene bg forest_dark with dissolve
    "Chiara faces the monster, her heart pounding. It stares at her with glowing eyes, then snarls."
    "For a moment, everything is still. Chiara realizes that she has to make a choice if she’s going to survive."

    menu:
        "Charge at the monster":
            $ action = "charge"
            "With all her might, Chiara charges at the monster, hoping to catch it off guard. But it swipes at her with its sharp claws."
            jump final_faceoff

        "Try to talk to the monster":
            $ action = "talk"
            "Chiara takes a step forward and speaks to the creature, hoping to reason with it. The monster tilts its head, as if confused."
            jump strange_communication

label escape_tree:
    scene bg tree_top with dissolve
    "From the top of the tree, Chiara watches the monster below, frustrated and roaring. She breathes a sigh of relief."
    "The dream begins to fade, and Chiara feels herself waking up."
    jump end_dream

label final_chase:
    scene bg forest_dark with dissolve
    "The monster reaches out, grabbing Chiara by the arm. She screams, but with a burst of strength, she manages to break free and keep running."
    "She suddenly finds a cliff ahead and leaps over it, landing in a soft bed of leaves. The monster follows, but disappears as it reaches the edge."
    jump end_dream

label final_faceoff:
    scene bg forest_dark with dissolve
    "Chiara stumbles back as the monster claws at her, but she manages to dodge, running around it in circles."
    "With a final desperate move, she kicks it and it stumbles backward, vanishing into the darkness."
    jump end_dream

label strange_communication:
    scene bg forest_dark with dissolve
    "To her surprise, the monster doesn't attack. Instead, it takes a step back, as if understanding her words."
    "It slowly disappears into the mist, leaving Chiara standing alone in the forest."
    jump end_dream

label end_dream:
    scene bg bedroom_morning with fade
    show character chiara awake
    "Chiara wakes up with a start, her heart still pounding from the nightmare. She looks around, finding herself safe in her bedroom."
    "The dream was intense, but it's over now. She sighs in relief, though the eerie feeling lingers."

    "With a deep breath, Chiara tries to shake off the unsettling thoughts and starts her day."
    return
