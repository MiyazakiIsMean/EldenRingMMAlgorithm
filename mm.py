#!/usr/bin/python

# To be clear: this is satire. This python may not be fully syntactically
# correct; no one cares about your nitpicking complaints. Just have a laugh.

# We at FromSoft use Python for matchmaking because C++ is too hard for us :D

# NOTES FROM MEETINGS
#
# FROM Hidetaka Miyazaki: 
# We do not want invaders to have fun, we do not want them
# to succeed. They cannot succeed. They killed me so many times in Demon's
# Souls. I am so mad about it still, I hate the scraping spear.
# We must protect hosts at all costs. They cannot be allowed to fail.
# Do not make them earn anything. Let them be carried through the game.

# Update (2 days before 1.04):
# FROM Hidetaka Miyazaki:
# 1. Introduce networking bug, make invaders lose connection after roughly 2
# minutes. We cannot let them get to the host.
#
# 2. Severely reduce hostility of mobs for host and supporting phantoms
# when invader is present. This is to ensure maximum safety for host and
# phantoms. If you can, enable 'statue' mode for mobs- I do not want them
# to move if invader is nearby. We cannot let them get to the host.
#
# 3. Also just nerf boss aggression in general because game too hard for
# dumb people.

class Player:

    # TODO: Add supporting phantom "successful kills on invaders" so we can
    # match hosts with the best supporting phantoms the game has to offer
    # Reminder, this is our datastructure representation of the 
    # host!!! (updated 1.07, I think. Pls check git history)
    #
    # host = {
    #   'level': 14,
    #   'white_ring_cihper': True,
    #   'supporting_phantoms': [
    #        {'level': 150, 'weapons': ['Rivers of Blood'], 'spells': ['SPAM SPAM SPAM'],'stats': {'int': -25, 'arc': 999}}
    #    ]
    # }

    # We hate invaders so much >:(
    def match_angry_person_invader_to_host_player_who_is_most_valuable_must_never_let_die(rune_level,weapon_level):
        match = False
        enter_queue(rune_level, weapon_level)
        
        # To begin with, we try to ensure overwhelming odds in favor of the
        # host. It is unacceptable for a host to not win. We want at least 2
        # supporting phantoms present.
        #
        # We also LOVE the idea of gank squads hehehehe it's so fun and enjoyable
        # this is exactly what we wanted this game to be. Nothing like that mean
        # old demon's souls.
        if len(host['supporting_phantoms']) >= 2:
            
            # We must ensure the host has at least one over-leveled phantom via
            # password matchmaking. We want the invader to die in 1 or 2 hits.
            # We know downscaling does not work lol, of course we do- it's
            # how we designed it :D
            if host['supporting_phantoms'][0]['level'] > (host['level'] + 50) or host['supporting_phantoms'][1]['level'] > (host['level'] + 50):

                # We should try to ensure the host has at least one phantom
                # that can sit in the back and spam spells. This is to ensure
                # maximum fairness and safety for the host
                #
                # We want to encourage these types of phantoms because in 1.04
                # WE ABSOLUTELY FUCKING RUINED the Carian Retaliation AoW. This
                # is because we suck at balancing this game and instead of
                # fixing it so players could no longer self-proc, we just said
                # 'lol nope' and set each projectile to a static 150 dmg.
                #
                # This is great for brain dead hosts and phantoms because now
                # they can spam spells without fear- carian retaliation will
                # no longer punish them for their dog shit gameplay.
                for supporting_phantom in host['supporting_phantoms']:
                    if supporting_phantom['stats']['int'] > 40:
                        spells_we_want_supporting_phantoms_protecting_most_valuable_host_with = [
                            'Stars of Ruin',
                            'Glintstone Cometshard',
                            "Loretta's Mastery",
                            'Collapsing Stars'
                            'Ancient Death Rancor'
                        ]

                        # Finally we can verify a phantom has spammable spells and can sit in the back
                        # being a totally helpful awesome person 100 reddit karma for this phantom :D
                        for spells in supporting_phantom['spells']:
                            if spell in spells_we_want_supporting_phantoms_protecting_most_valuable_host_with:
                                match = True

                    # We also must ensure *at least* one of the supporting phantoms is running a spammable, 
                    # ideally bleed-inflicting, weapon
                    # We also only want phantoms we actually know will proc the hemmorage
                    if supporting_phantom['stats']['arc'] > 999:
                        weapons_we_want_supporting_phantoms_protecting_most_valuable_host_with = [
                            'Rivers of Blood',
                            'Godskin Peeler',
                            "Eleonora's Poleblade",
                            'Reduvia',
                            'Uchigatana'
                        ]
                    
                        for weapon in supporting_phantom['weapons']:

                            # Finally we can verify a phantom has an overpowered bleed weapon
                            if weapon in weapons_we_want_supporting_phantoms_protecting_most_valuable_host_with:
                                match = True

        # Our host only has one phantom, we absolutely have to ensure it is over-leveled                         
        elif len(host['supporting_phantoms']) = 1:
            if host['supporting_phantoms'][0]['level'] >= (host['level'] + 100):

                # We should also make sure the host can be joined by a hunter to immediately
                # even the odds. I wish we could have 5 hunters join at once but our rudamentary
                # netcode can't handle that.
                #
                # If these criteria are not met, we cannot verify a host will be protected
                # This is unacceptable!!!
                if host['white_ring_cipher']:
                    match = True
        else:
            # We double triple ensure match is false because we don't want no
            # pesky invaders
            match = False
        
        if match:
            # We have verified this invasion will be incredibly fair and balanced, providing
            # a safe pvp experience for the host
            match_invader_to_host(match)
        else:
            # At this point we could not verify the following:
            # - the host has at least one over leveled phantom
            # - the host has a phantom with at least one broken meta weapon
            # - the host has at least one phantom with spammable spells
            # - the host has the white cipher ring on so hunters can save them
            #   and their 1 phantom
            #
            # To that end, we make the invader think there was a timeout.
            # this will make the invader non-stop google for network fixes
            # and it protects the host from losing :)))
            send_tcp_reset(msg='Invasion aborted due to time-out')
