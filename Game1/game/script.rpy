# Questo è il file script.rpy per il tuo progetto Ren'Py
# Definizione dei personaggi
define luca = Character("Luca")
define chiara = Character("Chiara")

label start:
    # Introduzione alla storia
    scene bg room with fade
    show character luca happy
    "It has been a long and challenging day, filled with endless tasks and moments of tension. But now, as the day finally comes to an end, it's time to retreat to the comfort of bed. At last, I can close my eyes, let go of the day's worries, and embrace the peaceful rest I’ve been yearning for."
    
    # Menu di scelta
    menu:
        "Turn off the light":
            "You reach out and switch off the light. The room falls into a calming darkness, and you feel yourself drifting into sleep."
            jump dream_intro

        "Leave the light on":
            "You decide to leave the light on, its faint glow offering a comforting presence as you close your eyes."
            jump dream_intro

label dream_intro:
    scene bg room with fade
    show character chiara neutral
    
    "Good night..."
    "zzzz... zzzz..."
    "Chiara is deep asleep, her mind wandering into a strange, dark dream. Suddenly, she finds herself in a vast, shadowy forest. The air is heavy, and the silence is unsettling."

    "Out of the mist, a terrifying creature appears, its glowing eyes locking onto her. It's tall, monstrous, and moves with an unnatural speed."
    jump denial_stage

# Stage 1: Denial
label denial_stage:
    scene bg dream_forest with fade
    "Chiara is in the dark forest, surrounded by tall trees and a strange mist. She hears a growl behind her."
    "Her chest tightens, but she shakes her head. 'This isn’t real,' she whispers. 'It’s just a dream.'"
    "The monster’s growl gets louder, and its shadow moves closer. Chiara doesn’t want to believe it. She keeps walking forward."

    menu:
        "Keep ignoring the sound":
            "Chiara walks faster, pretending everything is fine. But her heart starts beating faster."
            jump anger_stage

        "Look back at the sound":
            "Chiara turns her head, and she sees glowing eyes staring at her. She freezes in fear."
            jump anger_stage

# Stage 2: Anger
label anger_stage:
    scene bg dream_forest_dark with fade
    "The shadow becomes a monster. It steps out from the trees, growling louder. Its claws scrape the ground as it moves closer."
    chiara "Why is this happening to me? What did I do to deserve this?!"
    "She feels angry, her fists clenching, but the monster doesn’t stop. It roars, making the ground shake."
    
    menu:
        "Scream at the monster":
            "Chiara yells, her voice echoing through the forest. But the monster only roars back, even louder."
            jump bargaining_stage

        "Run away":
            "Chiara turns and runs, her anger turning into fear. The monster chases her, its heavy footsteps shaking the earth."
            jump bargaining_stage

# Stage 3: Bargaining
label bargaining_stage:
    scene bg dream_bridge with fade
    "Chiara runs until she reaches a broken bridge. Below, a dark river rushes by, and the monster is getting closer."
    chiara "Please, just let me wake up! I’ll do anything!"
    "She looks at the monster, hoping it will stop. But it doesn’t. It keeps coming, growling louder."
    
    menu:
        "Try to jump across the bridge":
            "Chiara leaps, her heart racing. She grabs the edge on the other side, pulling herself up. But the monster is still behind her."
            jump depression_stage

        "Stay and face the monster":
            "Chiara stands still, shaking. 'Maybe if I stop, it will go away,' she thinks. The monster stops, but its glowing eyes watch her closely."
            jump depression_stage

# Stage 4: Depression
label depression_stage:
    scene bg dream_valley with fade
    "Chiara finds herself in a valley. The sky is grey, and rain starts to fall. She feels tired, like she can’t run anymore."
    chiara "I can’t do this. It’s too much. Maybe I should just give up."
    "The monster stands in the distance, watching her but not moving. Its presence feels heavy, like a dark cloud over her."
    
    menu:
        "Sit down and cry":
            "Chiara sits in the rain, her tears mixing with the water. She feels small and powerless."
            jump acceptance_stage

        "Keep walking, slowly":
            "Chiara drags her feet forward, the rain soaking her clothes. Each step feels harder, but she doesn’t stop."
            jump acceptance_stage

# Stage 5: Acceptance
label acceptance_stage:
    scene bg dream_light with fade
    "The rain stops, and Chiara looks up. A soft light breaks through the clouds. She stands up, feeling a little stronger."
    "The monster steps closer, but this time, it looks less scary. She realizes it isn’t chasing her anymore."
    chiara "You’re a part of me, aren’t you? My fear, my sadness… but I’m not afraid of you now."
    "The monster slowly fades away, and the light becomes brighter. Chiara feels calm, ready to move forward."

    return
