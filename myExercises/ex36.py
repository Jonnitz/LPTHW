from sys import exit
from random import randint

myStamina = 20

key = False
shovel = False
sword = False
armor = False

plundered = 0
first_plundered = False
second_plundered = False
third_plundered = False

def show_inventory():
    print "\n"
    print inventory

print """\n\n\tYou are an adventurer crawling through dungeon full of monsters, mysteries and treasures.
    But be aware that your stamina is limited and many have overexerted themselves in hope
    of undieing glory.
    Your stamina right now is: %d""" % myStamina


def entry_room():
    print """\n\tThis is the entry room of the dungeon. The air is old and dusty. Nothing
    appears to have set food into this complex. In front of you are two doors. The
    left one is a bit rotten and a proper kick should make it swing open.
    The right one, on the other hand, has a big, hefty lock in front of it that would
    need more force to break the door. What door do you want to kick open?
    'left' or 'right'?
    """
    while True:
        choice = raw_input("> ")
        if choice == "left":
            key_room(myStamina, key, shovel)
        elif choice == "right":
            locked_door(myStamina, key, shovel)
        else:
            print "Hesitation is infectious! Choose your path!"

def key_room(myStamina, key, shovel):
    print """\tThe new room is quite small but between pebble and sand you see a
    small key that could fit into the lock. Besides this key there is Nothing
    in this but rocks. But maybe underneath them could be some treasure. You
    could take the key and go back or search the room before, even though it
    may be tough to move those rocks.
    'take the key' or 'search the room'?"""

    while True:
        choice = raw_input("> ")
        if choice == "take the key":
            myStamina -= 1
            key = True

            print """\tYou take the key without much hesitation. No time to waste on
            some rocks. You head back to the entry room and unlock the right door.
            Forward!
            Your stamina sinks to %d\n.""" % myStamina

            locked_door(myStamina, key, shovel)

        elif choice == "search the room":
            myStamina -= 3
            key = True
            shovel = True

            print """\tYou lift the heavy rocks. You shed a bit of a sweat but found
            something! Beneath those rocks was a good looking shovel! Nice to have!
            Now you take the key and head to the locked door.
            Your stamina sinks to %d\n.""" % myStamina

            locked_door(myStamina, key, shovel)

        else:
            print "There are only two options. Decide, brave adventurer!"

def locked_door(myStamina, key, shovel):
    if key == False:
        myStamina -= 5
        print """\tWith all your might you kick the door. The door's hinges couldn't
        hold it anymore and with splintering wood the path is now open. Yet, you
        it took much of your strength to pull this of.
        Your stamina sinks to %d\n.""" % myStamina

        monster_room(myStamina, shovel)

    elif key == True:
        myStamina -= 1
        print """\tLuckily, you found the key, so you open the new path without much
        trouble. Though, it might not have been the most epic way but surely the most
        efficient.
        Your stamina sinks to %d\n.""" % myStamina

        monster_room(myStamina, shovel)

    else:
        print "What the fuck went wrong? You shouldn't even read this"



def monster_room(myStamina, shovel):
    print """\tAs you come near to the room you here the growling snoring of some-
    thing huge. On the other side of the room snores a beast of enourmous size.
    Sharp claw and long teeth glistering in the fair shine of your torch.
    As you look around you see that the monster blocks a door that leads further
    inside the dungeon. But another door branches of to the right. You might get
    past it without waking it up.
    Do you want to fight the beast or sneak past it? 'attack' or 'sneak'?"""

    choice = raw_input("> ")

    if choice == "attack" and shovel == False:
        myStamina -= 10
        print """\tThe battle was fierce and without a proper weapon you had to
        rely on your bare fists. You took some blows but at the end the monster
        lied on the ground. Defeated. As the rush of blood through your body sub-
        sided you start to feel the toll of your actions. But now you can pass
        through the door.
        Your stamina sinks to: %d""" % myStamina

        if myStamina <= 0:
            dead()

        armory_room(myStamina, armor, sword, first_plundered, second_plundered, third_plundered, plundered)

    elif choice == "attack" and shovel == True:
        myStamina -= 4
        print """\tThe battle was fierce but with a shovel as a weapon the beast
        stood no chance against your expertise. Unfortunately, your shovel broke
        in the process. A moment of silence for the fallen comrade...
        Then, you kick in the next door.
        Your stamina sinks to %d""" % myStamina

        if myStamina <= 0:
            dead()

        print "\n\t\t [You lost the shovel]"

        armory_room(myStamina, armor, sword, first_plundered, second_plundered, third_plundered, plundered)

    elif choice == "sneak":
        myStamina -= 1

        print "\tYou sneak by the snoring monster and open quietly the old door."

        chest_room(myStamina, shovel)

def chest_room(myStamina, shovel):
    myStamina -= 1

    if myStamina <= 0:
        dead()

    print """\tEven before you set foot into the room in front of you, you smell
    a horrific stink. But as you come closer to the room the smell subsides.
    As you enter the room your adventurer's heart skips a beat. You see a big
    treasure chest on a little platue. To your right awaits you another door to
    be opened.
    What do want to do? 'open the chest' or 'go'?
    Your stamina is now %d""" % myStamina

    while True:
        choice = raw_input("> ")
        if choice == 'open the chest' and shovel == True:
            myStamina -= 2
            shovel = False
            print """\tAs you put your hands on the chest's lid it sprung open. Razor
            sharp teeth around the lid tried to snap of your arms but you're fast
            enough to flinch back. But the creature in front of you, a Mimic, was
            ready attack once more. Fortunately, you had this shovel which made a
            superb weapon and the Mimic was defeated after a short exchange of blows.
            But your shovel broke. A moment of silence for a lost comrade...
            Your stamina sinks to %d""" % myStamina

            if myStamina <= 0:
                dead()

            print "\n\t\t [You lost the shovel]"
            print"""\n\tThere is nothing else in this room. You go through the next
            door."""

            boss_room(myStamina, sword, armor)

        if choice == 'open the chest' and shovel == False:
            myStamina -= 6
            print """\tAs you put your hands on the chest's lid it sprung open. Razor
            sharp teeth around the lid tried to snap of your arms but you're fast
            enough to flinch back. But the creature in front of you, a Mimic, was
            ready attack once more. But without a weapon those sharp teeth hurt a lot.
            Even though the Mimic was defeated by your enourmous skill, your body
            took quite a toll.
            Your stamina sinks to %d""" % myStamina

            if myStamina <= 0:
                dead()

            print"""\n\tThere is nothing else in this room. You go through the next
            door."""

            boss_room(myStamina, sword, armor)


def armory_room(myStamina, armor, sword, first_plundered, second_plundered, third_plundered, plundered):
    myStamina -= 1

    if myStamina <= 0:
        dead()

    print """\tThe room was narrow. Lots of shelves stood here once organised
    but now only broken wood remained. In midst of these junk all kinds of
    metallic objects. Old and rusty armor and swords thrown together. Most of
    them are more rust then steel. Worthless and with no use for you. But maybe
    you will find some equipment that could help you. Or you venture further
    through the next door.
    'search the room' or 'forward'
    Heed your body condition, though. Your stamina is now: %d""" % myStamina


    while True:
        choice = raw_input("> ")
        if choice == 'search the room':
            print """\tThere are three piles you could plunder.
            '1', next to the entrance.
            '2', by two broken shelves.
            '3', besides the exit.
            '1', '2', '3' or 'leave'? """
            while plundered <= 3:
                choice = raw_input("> ")
                if choice == '1' and first_plundered == False:
                    myStamina -= randint(1, 3)
                    first_plundered = True
                    plundered += 1

                    if myStamina <= 0:
                        dead()

                    print """\tYou rummage through the rusted iron and steel. You cut
                    yourself on the sharp edges.
                    Your stamina sinks to %d
                    But it was for:\n""" % myStamina
                    if randint(1, 3) < 2 and sword == False:
                        print "A sturdy longsword! Worth it."
                        sword = True
                    elif randint(1, 3) > 2 and armor == False:
                        print "A heavy chainmail! It will protect you but it looks heavy..."
                        armor = True
                    else:
                        print "Nothing! How unsatisfying!"

                elif choice == '1' and first_plundered == True:
                    print "You already looked here. Try another pile or leave this room."


                elif choice == '2' and second_plundered == False:
                    myStamina -= randint(1, 4)
                    second_plundered = True
                    plundered += 1

                    if myStamina <= 0:
                        dead()

                    print """\tYou rummage through the rusted iron and steel. You cut
                    yourself on the sharp edges. Your stamina sinks to %d
                    But it was for:\n""" % myStamina
                    if randint(1, 3) < 2 and sword == False:
                        print "A sturdy longsword! Worth it."
                        sword = True
                    elif randint(1, 3) > 2 and armor == False:
                        print "A heavy chainmail! It will protect you but it looks heavy..."
                        armor = True
                    else:
                        print "Nothing! How unsatisfying!"

                elif choice == '2' and second_plundered == True:
                    print "You already looked here. Try another pile or leave this room."

                elif choice == '3' and third_plundered == False:
                    myStamina -= randint(1, 4)
                    third_plundered = True
                    plundered += 1

                    if myStamina <= 0:
                        dead()

                    print """\tYou rummage through the rusted iron and steel. You cut
                    yourself on the sharp edges. Your stamina sinks to %d
                    But it was for:\n""" % myStamina
                    if randint(1, 3) < 2 and sword == False:
                        print "A sturdy longsword! Worth it."
                        sword = True
                    elif randint(1, 3) > 2 and armor == False:
                        print "A heavy chainmail! It will protect you but it looks heavy..."
                        armor = True

                    elif choice == '3' and third_plundered == True:
                        print "You already looked here. Try another pile or leave this room."

                    else:
                        print "Nothing! How unsatisfying!"

                elif choice == 'leave':
                    print "You decide to explore more of the dungeon. Loot can wait!"
                    boss_room(myStamina, sword, armor)

                else:
                    print "Thy options are four!"

        if choice == 'forward':
                print "You decide to explore more of the dungeon. Loot can wait!"
                boss_room(myStamina, sword, armor)

def boss_room(myStamina, sword, armor):
    print """\tThe corridor widens and a last big door has to be kicked open. You
    can practically smell the treasure and glory that await you.
    \n\tIn a golden throne sits a humanlike shape. As it lifts itself up,
    you can feel the temperature of the room declining and your breath becomes
    visible. The figure pulls a sword from its scabbard and walks slowly towards you."""
    if myStamina <= 5:
        print """\tYour body is near its limit but you don't give up. Not, when you're
            so close."""
    elif myStamina >=5 <= 9:
        print """\tYou feel the exertions of your crawl but here you stand, facing
        your destiny!"""
    else:
        print """\tHere you are. Feeling alive and full of energy. Let's rock!"""

    if sword == True and armor == True:
        myStamina -= 3
        if myStamina <= 0:
            dead()
        print """\n\tYou are well equipped and has nothing to fear. As you face your
        opponent excel all your bodily limits. You strike your foe done. As the evil
        spirit disappears treasure rain from the ceiling and you achieved all your
        dreams.
        You win!"""

    elif sword == True or armor == True:
        myStamina -= 6

        if myStamina <= 0:
            dead()

        print """\n\tWith your equipment you fight with all your might. Your oppenent
        appears not to have anymore bodily restrictions, so you have to rely on your
        wits. Ruse after ruse you deal the deadly blow and strike your foe down.
        As the evil spirit disappears treasure rain from the ceiling and you achieved
        all your dreams.
        You win!"""

    while True:
        if myStamina <= 5 and sword == False and armor == False:
            print """\n\tThe evil spririt puts its sword away and looks at you with pity.
            You are merely able to stand. It fishes around in a chest besides its throne
            and fetches a bottle and a two cups. Then it come to you and offers you a cup.
            Do you accept? 'yes' or 'no'?"""

            choice = raw_input("> ")
            if choice == 'yes':
                print """\n\tYou take the drink and sip. The cold fluid runs down your throat.
                You get dizzy and lose your conciousness.\n
                You awake in the local inn. It all felt like a dream... Maybe you were just
                dreaming. Maybe you should try again."""
            elif choice == 'no':
                print """\n\tInstead of accepting the offer you attack the spirit with bare fists.
                It shakes its head and stick its hand right in your chest. You feel the icy
                grip around your heart as the exhaustion paralyzes your body.
                You lose all your stamina."""
                myStamina = 0

                if myStamina <= 0:
                    dead()

            else:
                print "Decide!"

        else:
            print """\n\tYou stand your ground against your foe but you are overwhelmed
            by this unhuman power. After a few exchanges of blows the exertion of the
            dungeon takes its toll and you lose your balance. Your opponent uses its
            advantage."""
            myStamina = 0

            if myStamina <= 0:
                dead()

def dead():
    print """\tThe exhaustion crept up your body until you collapsed. You share
    the fate of some many adventurer before you: Death.\n"""
    print "\t\t G A M E   O V E R"
    exit()


entry_room()
