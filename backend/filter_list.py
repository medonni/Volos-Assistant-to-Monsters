import json


user_input = '''1 An Offer You Can't Refuse
1 Arcane Signet
1 Army of the Damned
1 Bladestitched Skaab
1 Bojuka Bog
1 Carrion Feeder
1 Cemetery Reaper
1 Choked Estuary
1 Command Tower
1 Commander's Sphere
1 Corpse Augur
1 Corpse Cobble
1 Corpse Harvester
1 Crowded Crypt
1 Dark Ritual
1 Dark Salvation
1 Darkwater Catacombs
1 Death Baron
1 Death Tyrant
1 Dictate of Erebos
1 Dimir Aqueduct
1 Dimir Signet
1 Diregraf Captain
1 Diregraf Colossus
1 Distant Melody
1 Dreadhorde Invasion
1 Dregscape Zombie
1 Eaten Alive
1 Empty the Laboratory
1 Exotic Orchard
1 Feed the Swarm
1 Fleshbag Marauder
1 Foulmire Knight
1 Geralf, Visionary Stitcher
1 Ghouls' Night Out
1 Gisa and Geralf
1 Gleaming Overseer
1 Go for the Throat
1 Graf Reaver
1 Gravecrawler
1 Gray Merchant of Asphodel
1 Hordewing Skaab
9 Island
1 Jadar, Ghoulcaller of Nephalia
1 Lazotep Plating
1 Lazotep Reaver
1 Liliana, Death's Majesty
1 Liliana's Standard Bearer
1 Lord of the Accursed
1 Mana Drain
1 Master of Death
1 Midnight Reaper
1 Morbid Opportunist
1 Mortuary Mire
1 Murderous Rider
1 Myriad Landscape
1 Necroduality
1 Path of Ancestry
1 Phyrexian Delver
1 Port of Karfell
1 Raise the Draugr
1 Ravenous Rotbelly
1 Rise of the Dread Marn
1 Rooftop Storm
1 Shepherd of Rot
1 Sol Ring
1 Stitch Together
1 Sunken Hollow
14 Swamp
1 Tainted Isle
1 Talisman of Dominance
1 Temple of Deceit
1 Tomb Tyrant
1 Tormod, the Desecrator
1 Unclaimed Territory
1 Undead Augur
1 Unearth
1 Vengeful Dead
1 Victimize
1 Village Rites
1 Wilhelt, the Rotcleaver
1 Zombie Apocalypse

SIDEBOARD:
1 Charcoal Diamond
1 Shambling Ghast
1 Sky Diamond'''.splitlines()

user_input_filtered = [card[2:] for card in user_input]

print(user_input_filtered)