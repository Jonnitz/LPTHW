from sys import exit
import time
from random import randint

class Scene(object):

    flowers = False
    gave_flowers = False
    shovel = False
    fish = False
    your_catch = 0
    lamp = False
    fishing_rod = False
    give_fish = False
    artifact = False
    casket = False
    bridge = False
    treasure_map = False
    visited_woman = False
    visited_man = False
    visited_old_man = False
    visited_blacksmith = False

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class SceneChoice(Scene):
    def enter(self):
        if Scene.shovel == True and Scene.treasure_map == True:
            while True:
                    print "\tWhere do you want to go?"
                    print """
                        village
                        cave
                        beach
                        graveyard
                        forest
                        """
                    choice = raw_input("> ")

                    if choice == 'village':
                        print "\tYou go to the village."
                        return 'village'
                    elif choice == 'cave':
                        print "\tYou go to the cave."
                        return 'cave'
                    elif choice == 'beach':
                        print "\tYou go to the beach."
                        return 'beach_final'
                    elif choice == 'graveyard':
                        print "\tYou go to the graveyard."
                        return 'graveyard'
                    elif choice == 'forest':
                        print "\tYou got the forest."
                        return 'forest'
                    else:
                        print "\tChoose between those options."

        else:
            while True:
                print "\tWhere do you want to go?"
                print """
                    village
                    cave
                    beach
                    graveyard
                    forest
                    """
                choice = raw_input("> ")

                if choice == 'village':
                    print "\tYou go to the village."
                    return 'village'
                elif choice == 'cave':
                    print "\tYou go to the cave."
                    return 'cave'
                elif choice == 'beach':
                    print "\tYou go to the beach."
                    return 'beach'
                elif choice == 'graveyard':
                    print "\tYou go to the graveyard."
                    return 'graveyard'
                elif choice == 'forest':
                    print "\tYou got the forest."
                    return 'forest'
                else:
                    print "\tChoose between those options."

class OpeningScene(Scene):

    def enter(self):
        print """
        \n\tAs you leave the boat you came with, you see the small island that your father told you about.
        You don't know much about him but he used to go to the sea often and one day he didn't come
        back. Now you followed your father's footstep and reach this small island in the middle of
        the ocean.
        Despite being small the island has a big hill on the oppisite side of your landing stage and
        as you look closely you can see the stone fence of a graveyard on top of the hill. The tops
        of the trees on its feet accumalate to a big forest and what appears to be the middle of the
        island you can see the rooftops of a village, surrounded by fields and meadows.
        To your right a small path leads down to what looks like a beach and to your right you can make
        out a interesting stone formation that could be something like a cave.
        """
        return 'scene_choice'

class Village(Scene):

    def enter(self):

        print """
        The village is lively and people are dealing with their businesses. From the fire places comes
        smoke. Women chitchat near the well while doing the laundry and kids run around playing tag.
        Three people notice your arrival and look at you. One woman sitting on a bench knitting. One
        young man stealing glances at the woman on the bench and sighing now and then. And a blacksmith
        working on a piece of metal.
        Who do you want to talk with?

        woman
        man
        blacksmith
        leave
        """

        choice = raw_input("> ")
        while True:
            if choice == "woman":
                if Scene.visited_woman == False:
                    Scene.visited_woman = True
                    print """
                    \n\tAs you approach the woman she looks at you and smiles:
                    \n\t\t\t'You're not from here, are you? Welcome to our small village. I hope you will have a
                    nice stay here. It is seldom that people visit our island. And you are quite handsome
                    I have to say. Hahaha, no need to blush.
                    You look like you want to know about the island. I will tell you something:
                    Somewhere in the forest is a shrine where beautiful flowers grow. I'd love to have some
                    for my home. I really love them. But the forest is tricky. If you don't know where to
                    go you can easily find yourself back at the entrance.
                    But it is really simple. Just go left, left, straight, right and stright again and
                    there you are. But I'm not allowed to go there anymore... since the lost incident..
                    I hope that helped you a bit. See you around!'
                    """
                    choice = raw_input("press enter")

                    return 'village'

                elif Scene.visited_woman == True:
                    print """
                    \n\tDid you find something or did you got lost?
                    Just remember: left, left, straight, right, and straight again. Good luck.
                    """
                    choice = raw_input("press enter")
                    return 'village'

            elif choice == "man":
                if Scene.visited_man == False and Scene.flowers == False:
                    Scene.visited_man = True
                    print """
                    \n\tAs you approach the he greets you:
                    \t'Oh, hello. Haven't seen your face around here. A traveller, aren't you?
                    """
                    if Scene.visited_woman == True:
                        print """\t\t'I've seen you talking to Miria. The lovely lady sitting there.
                        I need your help concerning her. It is a mission of love, you see.'"""
                    elif Scene.visited_woman == False:
                        print """\t\t'I need your help in a matter of love. See that knitting beauty over
                        there? This is Miria... Hey, don't look so obvious in her direction!'"""

                    print """\t\tIt would be great if you could help me out. I need to find out what kind of thing she
                    likes and then give it to me as a present for her. Maybe then she will see what I feel
                    for her.
                    Will you help me out? I will give you something in return!'
                    Without waiting for your answer he smiles and pats your shoulder.
                    """
                    choice = raw_input("press enter")
                    return 'village'

                elif Scene.visited_man == True and Scene.flowers == False:
                    print """
                    'Hello traveller! Have you made any progress? If you find something, come back to me.
                    I'll make sure that you will get something nice in return.
                    """
                    choice = raw_input("press enter")
                    return 'village'


                elif Scene.visited_man == True and Scene.flowers == True:
                    print """
                    'Hello traveller! Hey, are those.. flowers? They are beautiful. Seriously. Is that the
                    thing Miria likes? Nice, good job, pal. Here take this!'

                    \tYou got 'Lamp'.

                    'I'll will go now and confess to her. Thank you again!'

                    The man takes the flowers from you and goes to the woman calles Miria. He stutters and
                    blushes hiding the flowers behind his back. Then he presents them to her and she is
                    overjoyed. Let's give them some privacy.
                    """
                    Scene.lamp = True
                    Scene.flowers = False
                    Scene.gave_flowers = True

                    choice = raw_input("press enter")
                    return 'village'

                elif Scene.gave_flowers == True:
                    print """
                    As you check on the man you helped out earlier you find him depressed sitting next
                    to the well. He notices you and sighes deeply:
                    'Oh, hello, traveller... What? Me? She rejected me... Would you mind leaving? I wanne be alone
                    right now...'
                    """
                    choice = raw_input("press enter")
                    return 'village'

            elif choice == "blacksmith":
                if Scene.visited_blacksmith == False:
                    Scene.visited_blacksmith = True

                    print """
                    You go to the blacksmith who looks up form his work and greets you:
                    'Oh, boy. Ya ain't from here, are ya? What brings ya to this damn lone island? Ey, but what
                    am I asking ya. Ya have ya reason, aye? If ya look for someone to do some heavy work come to
                    me. I'll help if I find the time. Though I need to go fishin'. Hmmm... Let's make a deal, boy.
                    When ya catch me a fish, I'll help ya with something. Sounds good?
                    Ya ain't have to use your hands though, take this rod.'

                    You got 'Fishing Rod'

                    'See ya around, boy.'
                    """
                    Scene.fishing_rod = True
                    choice = raw_input("press enter")
                    return 'village'

                elif Scene.visited_blacksmith == True and Scene.fish == False:
                    print"""
                    'Oy, boy! How ya doin'? Got no fish, do ya, hahaha. Don't worry. Those are slippy bastards.
                    Ya have to wait for the right timin', ya hear. If ya got one to bite you have to count to
                    5 before reelin' it in. That should work... most of the time. Good fishin'!''
                    """
                    choice = raw_input("press enter")
                    return 'village'

                elif Scene.visited_blacksmith == True and Scene.fish == True:
                    print """
                    'Oy, boy! How ya doin'? Ohhh, that is a big fish, ya've there. Thanks, boy. Now, if ya got
                    somethin' for me to do, just tell me.'
                    """
                    choice = raw_input("press enter")
                    Scene.fish = False
                    Scene.give_fish = True

                    if Scene.casket == True:
                        print """
                        'Oy, boy! How ya doin'? What? Ya want me to open that casket for ya? Sure thing. Just
                        give me a sec'.'
                        The blacksmith takes the casket from you and breaks the lock with some precise hits.
                        'There ya go. Come back if ya want something else. A nail or horse shoe maybe. See ya.!'

                        You got 'Treasure Map'.
                        """
                        Scene.treasure_map = True
                        Scene.casket = False

                        choice = raw_input("press enter")
                        return 'letter'

                elif Scene.casket == True and Scene.give_fish == True:
                    print"""
                    Oy, boy! How ya doin'? What? Ya want me to open that casket for ya? Sure thing. Just
                    give me a sec'.'
                    The blacksmith takes the casket from you and breaks the lock with some precise hits.
                    'There ya go. Come back if ya want something else. A nail or horse shoe maybe. See ya!'

                    You got 'Treasure Map'.
                    """
                    Scene.treasure_map = True
                    Scene.casket = False

                    choice = raw_input("press enter")
                    return 'letter'

            elif choice == "leave":
                return 'scene_choice'
            else:
                print"Choose between those options."
                return 'village'

class Letter(Scene):
    def enter(self):
        if Scene.treasure_map == True:
            print """
            You can open the casket now. Inside is folded piece of paper. Its content
            tells you something about a treasure that is buried deep on the beach on
            this island. A little map is drawn with the typical X on the point where
            you should dig.
            The letter is signed off with your father's name.
            Maybe the content of the treasure can help you on your search...
            """
            choice = raw_input("press enter")
            return 'scene_choice'

class Beach(Scene):

    def enter(self):
        print"""
        You walk down the path to beach.  White sand with some rocks lie before your feet.
        Algea and shells wash ashore and sea gulls cry as they fly away from you circlying
        in the air.
        A sole gangplank decends from some rocks into the sea and a lonely hut stands in
        the shadows of the cliffs behind it. A old man sits in front of the hut carving a
        wooden stick.
        Where do want to go?

        old man
        gangplank
        leave

        """

        choice = raw_input("> ")
        while True:
            if choice == "old man":
                if Scene.visited_old_man == False:
                    Scene.visited_old_man = True
                    print"""
                    You approach the old man sitting on a trunk and chewing something. As
                    he sees you he spits it out and barks to you:
                    'What do you want here, stranger? Here is nothing for someone as young
                    as you to do here.'
                    You explain that you are looking for your father to the old man.
                    'Really? You are his son? Hmm... He came here a long time ago and said
                    something about a thing in the cave...
                    But hey, did you see the collapsed bridge leading to the graveyard?
                    Actually it would be my job to repair it but my back aches so badly
                    and they don't have any medicine for this year. Still, I know that
                    a flask of this medicine is stored in the shrine for some religious
                    nonsense. Bring me the medicine and I can repair the bridge for you.
                    Well, then, see you around!'
                    """
                    choice = raw_input("press enter")
                    return 'beach'

                elif Scene.visited_old_man == True and Scene.artifact == False:
                    print """
                    The old man still sits on his trunk carving a stick.
                    'Did you find anything yet? No? How unfortunate. But it has to be in
                    the shrine. It has to. If its not then the bridge won't be repaired
                    until my backache is gone.'
                    """
                    choice = raw_input("press enter")
                    return 'beach'

                elif Scene.visited_old_man == True and Scene.artifact == True:
                    print """
                    The old man still sits on his trunk carving a stick.
                    'Did you find anything yet? You did, really? Great. Give it to me!'
                    You hand over the small flask and he empties it in one go. He looks
                    disgusted but relieved afterwards.
                    'This stuff is really awful. But I feel like I was born anew.
                    The bridge will be repaired in no time. You can go ahead. Once you
                    are there the bridge will be finished. Won't believe me? Oh, you
                    better do, hahaha. In this old bones is still much energy!'
                    """
                    Scene.artifact = False
                    Scene.bridge = True
                    choice = raw_input("press enter")
                    return 'beach'
                elif Scene.visited_old_man == True and Scene.bridge == True:
                    print """
                    The old man stands on a ladder and works on his roof with a lot of
                    energy and a smooth tune on his lips. When he notices you he shouts:
                    'Did you see the bridge? A true master piece if I may say so. Now that
                    my pain is gone I can finally finish my preparations for the winter.
                    Thanks again and good luck!'
                    """
                    choice = raw_input("press enter")
                    return 'beach'

            elif choice == "gangplank":
                if Scene.fishing_rod == False:
                    print """
                    What a beautiful view on the sea. You could be here and watch the dawn
                    without any worry in life. On the gangplank you find a bucket that smells
                    like fish. Looks like this is used as fishing spot.
                    If you had a fishing rod you could probably catch something. But right
                    now, here is nothing to do.
                    """
                    choice = raw_input("press enter")
                    return 'beach'
                elif Scene.fishing_rod == True:
                    print """
                    What a beautiful view on the sea. You could be here and watch the dawn
                    without any worry in life. On the gangplank you find a bucket that smells
                    like fish. Looks like this is used as fishing spot.
                    Fortunately, you have a fishing rod on you, so why don't you try to catch
                    a fish?

                    yes
                    no
                    """
                    choice = raw_input("> ")
                    while True:
                        if choice == "yes":
                            return 'fishing'
                        elif choice == "no":
                            return 'beach'
                        else:
                            print "Choose."
                            return 'beach'

            elif choice == "leave":
                choice = raw_input("press enter")
                return 'scene_choice'
            else:
                print "Choose between those options."
                return 'beach'

class Fishing(Scene):

    def enter(self):
        print """
        With a eager swing the fishing rod and the hook sinks down. No you have to
        wait...
        """
        time.sleep(1)
        print "\n\tWait..."
        time.sleep(1)
        print"\n\tWait..."
        time.sleep(1)
        print "\n\tWait..."
        time.sleep(1)
        print "\tSomething bit!"
        while True:
            Scene.your_catch = randint(1, 5)
            if Scene.your_catch < 3:
                print """
                It is... \t a shoe?
                What does that do in here?
                Maybe next time!
                """
                choice = raw_input("press enter")
                return 'fishing'
            elif Scene.your_catch > 3:
                print """
                It is... \t a can?
                What does that do in here?
                Maybe next time!
                """
                choice = raw_input("press enter")
                return 'fishing'
            elif Scene.your_catch == 3:
                print """
                It is... \t a fish!
                And a big one! The blacksmith will be happy!
                """
                Scene.fish = True
                choice = raw_input("press enter")
                return 'beach'

class BeachFinal(Scene):
    def enter(self):
        print"""
        You walk down the path to beach.  White sand with some rocks lie before your feet.
        Algea and shells wash ashore and sea gulls cry as they fly away from you circlying
        in the air.
        A sole gangplank decends from some rocks into the sea and a lonely hut stands in
        the shadows of the cliffs behind it. A old man sits in front of the hut carving a
        wooden stick.
        But somewhere around here should be the treasure chest!
        Where do want to go?

        old man
        gangplank
        treasure
        leave

        """

        choice = raw_input("> ")
        while True:
            if choice == "old man":
                if Scene.visited_old_man == False:
                    Scene.visited_old_man = True
                    print"""
                    You approach the old man sitting on a trunk and chewing something. As
                    he sees you he spits it out and barks to you:
                    'What do you want here, stranger? Here is nothing for someone as young
                    as you to do here.'
                    You explain that you are looking for your father to the old man.
                    'Really? You are his son? Hmm... He came here a long time ago and said
                    something about a thing in the cave...
                    But hey, did you see the collapsed bridge leading to the graveyard?
                    Actually it would be my job to repair it but my back aches so badly
                    and they don't have any medicine for this year. Still, I know that
                    a flask of this medicine is stored in the shrine for some religious
                    nonsense. Bring me the medicine and I can repair the bridge for you.
                    Well, then, see you around!'
                    """
                    choice = raw_input("press enter")
                    return 'beach'

                elif Scene.visited_old_man == True and Scene.artifact == False:
                    print """
                    The old man still sits on his trunk carving a stick.
                    'Did you find anything yet? No? How unfortunate. But it has to be in
                    the shrine. It has to. If its not then the bridge won't be repaired
                    until my backache is gone.'
                    """
                    choice = raw_input("press enter")
                    return 'beach'

                elif Scene.visited_old_man == True and Scene.artifact == True:
                    print """
                    The old man still sits on his trunk carving a stick.
                    'Did you find anything yet? You did, really? Great. Give it to me!'
                    You hand over the small flask and he empties it in one go. He looks
                    disgusted but relieved afterwards.
                    'This stuff is really awful. But I feel like I was born anew.
                    The bridge will be repaired in no time. You can go ahead. Once you
                    are there the bridge will be finished. Won't believe me? Oh, you
                    better do, hahaha. In this old bones is still much energy!'
                    """
                    Scene.artifact = False
                    Scene.bridge = True
                    choice = raw_input("press enter")
                    return 'beach'
                elif Scene.visited_old_man == True and Scene.bridge == True:
                    print """
                    The old man stands on a ladder and works on his roof with a lot of
                    energy and a smooth tune on his lips. When he notices you he shouts:
                    'Did you see the bridge? A true master piece if I may say so. Now that
                    my pain is gone I can finally finish my preparations for the winter.
                    Thanks again and good luck!'
                    """
                    choice = raw_input("press enter")
                    return 'beach'

            elif choice == "gangplank":
                if Scene.fishing_rod == False:
                    print """
                    What a beautiful view on the sea. You could be here and watch the dawn
                    without any worry in life. On the gangplank you find a bucket that smells
                    like fish. Looks like this is used as fishing spot.
                    If you had a fishing rod you could probably catch something. But right
                    now, here is nothing to do.
                    """
                    choice = raw_input("press enter")
                    return 'beach'
                elif Scene.fishing_rod == True:
                    print """
                    What a beautiful view on the sea. You could be here and watch the dawn
                    without any worry in life. On the gangplank you find a bucket that smells
                    like fish. Looks like this is used as fishing spot.
                    Fortunately, you have a fishing rod on you, so why don't you try to catch
                    a fish?

                    yes
                    no
                    """
                    choice = raw_input("> ")
                    while True:
                        if choice == "yes":
                            return 'fishing'
                        elif choice == "no":
                            return 'beach'
                        else:
                            print "Choose."
                            return 'beach'

            elif choice == "leave":
                choice = raw_input("press enter")
                return 'scene_choice'

            elif Scene.shovel == True and Scene.treasure_map == True and choice == "treasure":
                print """
                You look for the spot on the map and follow the instructions.
                Then you find the spot and you begin to dig.
                """
                dig = raw_input("press enter to dig")
                dig = raw_input("press enter to dig")
                dig = raw_input("press enter to dig")
                dig = raw_input("press enter to dig")
                dig = raw_input("press enter to dig")
                dig = raw_input("press enter to dig")

                print """
                After plenty of sand and a bit of a sweat your shovel hits something
                wooden. Exited you wipe all the sand from the chest's lid. It was a
                real treasure chest!
                You pull it out. Use the shovel to open the lid!
                """
                hit = raw_input("press enter to lock-pick")
                hit = raw_input("press enter to lock-pick")
                hit = raw_input("press enter to lock-pick")

                print """
                With a sharp noise the lock snaps and you can open the lid.
                Inside the chest is... nothing. No gold. No jewelry. No pirate
                treasure.
                But as you look more carefully you see a piece of paper. A letter
                to be precise. You take it and open it.
                """
                choice = raw_input("pres enter")
                return 'finished'
            else:
                print "Choose between those options."
                return 'beach'

class Cave(Scene):
    def enter(self):
        print """
        You walk done the path down the coast to your left. The path is wild
        and full of sharp rocks. Signs warn of trespassing but you don't care.
        Following what looks like a path you find the entrance to the cave.
        """
        if Scene.lamp == False:
            print """
            The darkness in the cave is surprisingly thick. You enter a few steps
            but without a source of light you probably will slip somewhere and fall
            onto the sharp rocks or the water. It would be best to return for the
            moment and look for a source of light.
            """
            choice = raw_input("press enter")
            return 'scene_choice'
        elif Scene.lamp == True:
            print """
            The darkness swallows you but you have prepared the lamp the man in the
            village gave you. With its help you venture through the cave and find in
            a corner traces of a fire place. Besides it lays a casket. You pick it up
            and tries to open it, but the lock is stronger than one could have guessed.
            Maybe you'll find someone to open it for you.
            After searching every corner of the cave you don't find anything else and
            leave.
            """
            Scene.casket = True
            choice = raw_input("press enter")
            return 'scene_choice'

class Forest(Scene):
    def enter(self):
        print """
        The forest looks deeper then you thought. More, it looks like a maze where
        you had no point of orientation. So beware!
        You come to a fork. You can go left, right or straight.
        Where do want to go?

        left
        right
        straight
        """
        choice = raw_input("> ")

        if choice == "left":
            print """
            You come to another fork. Again, you can go left, right or straight.
            Where do want to go?

            left
            right
            straight
            """
            choice = raw_input("> ")

            if choice == "left":
                print """
                Again?! Another fork. You know the game by now:
                Where do want to go?

                left
                right
                straight
                """
                choice = raw_input("> ")

                if choice == "straight":
                    print """
                    Whelp... You know the game by now:

                    left
                    right
                    straight
                    """
                    choice = raw_input("> ")

                    if choice == "right":
                        print """
                        You can feel it.. Almost there!

                        left
                        right
                        straight
                        """
                        choice = raw_input("> ")

                        if choice == "straight":
                            print "\t\tYou did it!"
                            choice = raw_input("press enter")
                            return 'shrine'

                        else:
                            print """
                            You stray through the forest and then you see light...
                            But its just the entrace... Damn.
                            """
                            return 'forest'
                    else:
                        print """
                        You stray through the forest and then you see light...
                        But its just the entrace... Damn.
                        """
                        return 'forest'
                else:
                    print """
                    You stray through the forest and then you see light...
                    But its just the entrace... Damn.
                    """
                    return 'forest'
            else:
                print """
                You stray through the forest and then you see light...
                But its just the entrace... Damn.
                """
                return 'forest'
        else:
            print """
            You stray through the forest and then you see light...
            But its just the entrace... Damn.
            """
            return 'forest'

class Graveyard(Scene):

    def enter(self):
        print """
        The path up the hill is steep you make it to the top. You already see the
        graveyard but a deep canyon has to be crossed to get there.
        """
        if Scene.bridge == False:
            print """
            Unfortunately, this bridge is completely broken and any attempt
            to cross the canyon in another way would be practically suicide. Better
            find a way to repair the bridge!
            """
            choice = raw_input("press enter")
            return 'scene_choice'
        elif Scene.bridge == True:
            print """
            The bridge was repaired. How did the old man was here before you AND
            repaired the bridge in no time? A mystery, really. But hey, you can
            go to the graveyard now.
            Besides plenty of old stone you find a shovel. This will be useful.
            Certainly. Shovels are great and you know that! Pleased you can return.

            \tYou get 'Shovel'.
            """
            Scene.shovel = True
            choice = raw_input("press enter")
            return 'scene_choice'

class Shrine(Scene):

    def enter(self):
        print """
        You leave the forest behind and with it the anxious feeling of repetition.
        Right now, you stand in front of an ancient looking shrine with an altar in the
        middle of the room. Water is running from some sort of source into a little pound
        behind the altar. It was so quiet here besides the sound of water and birds.
        Peaceful.
        After you took a deep breath you look around. On the alter sits a little flask.
        Around the altar bloom beautiful little flowers.
        """
        if Scene.visited_woman == True:
            print """
            Those look like the flowers you were supposed to get for the woman in the
            village.
            """
        if Scene.visited_old_man == True:
            print """
            This flask should be the medicine the old man talked about!
            """
        print """
        What do you want to do?

        take flask
        take flowers
        take all
        leave
        """

        choice = raw_input("> ")
        while True:
            if choice == "take flask":
                print"""
                You take the flask.

                \t You get 'Flask'
                """
                Scene.artifact == True

                choice = raw_input("press enter")
                return 'shrine'

            elif choice == "take flowers":
                print"""
                You take the flowers.

                \t You get 'Flowers'
                """
                Scene.flowers == True
                choice = raw_input("press enter")
                return 'shrine'
            elif choice == "take all":
                print"""
                You take the flask.

                \t You get 'Flask'

                You take the flowers.

                \t You get 'Flowers'
                """
                Scene.flowers == True
                Scene.artifact == True

                time.sleep(1)
                print """
                You got everything. You should leave now.
                """
                choice = raw_input("press enter")
                return 'scene_choice'
            elif choice == "leave":
                print "You leave."
                choice = raw_input("press enter")
                return 'scene_choice'
            else:
                print "Decide between those options"
                return 'shrine'

class Finished(Scene):

    def enter(self):
        print """
        The letter was not old. So wasn't its content. Your father wrote it. He
        knew you would come to look for him. So he arrange this little paperchase
        for you. But since you are reading this letter you have passed all his tests.
        You may find him on another island to the west.
        'Go my boy! Let the wind guide you, hahaha!'
        And so you set sail to the west. To find your father.

        ##############################################

        The End (?)

        ##############################################

        Thanks for playing. Watch out for possible sequels!
        """
        choice = raw_input("press enter")
        return 'finished'

class Map(object):

    scenes = {
        'scene_choice': SceneChoice(),
        'opening_scene': OpeningScene(),
        'village': Village(),
        'beach': Beach(),
        'cave': Cave(),
        'fishing': Fishing(),
        'graveyard': Graveyard(),
        'forest': Forest(),
        'shrine': Shrine(),
        'beach_final': BeachFinal(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('opening_scene')
a_game = Engine(a_map)
a_game.play()
