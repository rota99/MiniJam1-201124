# Vous pouvez placer le script de votre jeu dans ce fichier.

# Declarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Declarez les personnages utilisés dans le jeu.
# define e = Character(color="#c8ffc8")


# Le jeu commence ici
label start:

    "God it's been a long day."

    "..."

    "I guess I'm just gonna sleep, it can't take it anymore."

    jump denial

label denial:

    "Oh my god, this thing keeps chasing me."

    $ run_time = 0

    label run_start:

        if run_time == 0:
            "I have to find an exit. There must be an exit somewhere."
        elif run_time == 1:
            "Why does it keeps following me ?"
        elif run_time == 2:
            "I can't breeze. I'm going to need to stop soon"

        menu:

            "Run":

                $ run_time += 1

                jump run_start

            "Face the creature" if run_time == 2:

                jump facing_fear

        jump run_start

    label facing_fear:

        "Ok, I'm done with running. Let's face thi shit."
        

    jump anger

label anger:

    "anger"

    jump denial

label bargaining:

    "bargaining"

    jump depression 

label depression:

    "depression"

    jump acceptance 

label acceptance:

    "acceptance"

    jump end

label end:

    return
