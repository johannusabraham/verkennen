import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
player_ruby = 0
heeft_sleutel = False

zombie_attack = 1
zombie_defense = 0
zombie_health = 2


print('')
time.sleep(1)
# === [kamer 1] === #
print('in het graaf van heer necrus zie je twee grote deuren.')
print('Door de twee grote deuren loop je een donkere gang binnen.')
print('Het ruikt hier muf, vochtig en het is hier zeer koud.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)
# === [kamer 7] === #
ruby_kans = (random.randrange (1,10))
if ruby_kans == 1:
  print('je gaat door de deur en komt een lege kamer binnen')
else:
 print('je gaat door de deur en op de grond ligt een ruby')
 player_ruby += 1
print('er is veder niks in deze kamer dus besluit je naar de volgende deur te gaan')
print('')
time.sleep(1)

kant2 = input('je kan twee kanten op, wil je links of rechtdoor ')
if kant2 == 'links':
 sleutel =('sleutel')
 rando1 =(random.randrange (10,25))
 rando2 =(random.randrange (-75,-5))
 print('Je stapt door de deur heen en je ziet een standbeeld van heer necrus voor je.')
 print('Het standbeeld heeft een ruby vast.')
 print('Op zijn borst zit een numpad met de toesten 25 t/m -75.')
 print(f'Daarboven zie je een som staan {rando1}+{rando2}=? ')
 antwoord = int(input('Wat toest je in? '))
 if antwoord == rando1 + rando2 :
    print('Het stadbeeld laat de ruby vallen en je pakt het op')
    player_ruby += 1
 else:
    print('Er gebeurt niets....')


 print('Je zie een deur achter het standbeeld.')
 print('')
 time.sleep(1)
 kant = input('je kan twee kanten op, wil je links of rechtdoor ')
 if kant == 'links':
   print('Je loopt tegen een zombie aan die naast de grafsteen van de zoon van heer necrus staat.')

   zombie_hit_damage = (zombie_attack - player_defense)
   if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
   else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
      print(f'In {player_attack_amount} rondes versla je de zombie.')
      print(f'Je health is nu {player_health - zombie_attack}.')
    else:
      print('Helaas is de zombie te sterk voor je.')
      print('Game over.')
      exit()
   print('')
   time.sleep(1)
   print()
   print('je duwt de deur open en ziet een grote ruby gokmachine')
   wilt = input('wil je gokken met je ruby(s)[ja/nee] ')
   if wilt == 'ja':
     rand1 =(random.randrange (1,6))
     rand2 =(random.randrange (1,6))
     if rand1 + rand2 > 7:
      print('je gokt goed en je ruby aantal verdubbelt')
      player_ruby += 1
     elif rand1 + rand2 == 7:
      print('je gokt presies goed genoeg en wint 1 ruby en 4 health')
      player_health += 4
      player_ruby += 1
     else:
      print('je gokt fout en de gokmachine bijt je en je verliest 1 health')
      player_health -= 1
      print(f'Je health is nu {player_health}')
      if player_health == 0:
        print('doordat je zo zwak bent eet de gokmachine je op en ga je dood')
        print('Game over')
      else:
       print()  
   else:
    print('je wilt niet gokken en is hier dus niks voor jouw en ga je naar de volgende deur')
 else:
  print('je duwt de deur open en ziet een grote ruby gokmachine')
  wilt = input('wil je gokken met je ruby(s)[ja/nee] ')
  if wilt == 'ja':
    rand1 =(random.randrange (1,6))
    rand2 =(random.randrange (1,6))
    if rand1 + rand2 > 7:
     print('je gokt goed en je ruby aantal verdubbelt')
     player_ruby += 1
    elif rand1 + rand2 == 7:
     print('je gokt presies goed genoeg en wint 1 ruby en 4 health')
     player_health += 4
     player_ruby += 1
    else:
     print('je gokt fout en de gokmachine bijt je en je verliest 1 health')
     player_health -= 1
     print(f'Je health is nu {player_health}')
     if player_health == 0:
       print('doordat je zo zwak bent eet de gokmachine je op en ga je dood')
       print('Game over')
     else:
      print()  
  else:
   print('je wilt niet gokken en is hier dus niks voor jouw en ga je naar de volgende deur')

 print('')
 time.sleep(1)
else:
  print('je duwt de deur open en ziet een grote ruby gokmachine')
  wilt2 = input('wil je gokken met je ruby(s)[ja/nee] ')
  if wilt2 == 'ja':
     rand1 =(random.randrange (1,6))
     rand2 =(random.randrange (1,6))
     if rand1 + rand2 > 7:
      print('je gokt goed en je ruby aantal verdubbelt')
      player_ruby *= 2
     elif rand1 + rand2 == 7:
      print('je gokt presies goed genoeg en wint 1 ruby en 4 health')
      player_health += 4
      player_ruby += 1
     else:
      print('je gokt fout en de gokmachine bijt je en je verliest 1 health')
      player_health -= 1
      print(f'Je health is nu {player_health}')
      if player_health == 0:
        print('doordat je zo zwak bent eet de gokmachine je op en ga je dood')
        print('Game over')
      else:
       print()  
  else:
   print('je wilt niet gokken en is hier dus niks voor jouw en ga je naar de volgende deur')

print('')
time.sleep(1)

print('het moment dat je de kamer binnenkomt voel je dat je sterker ben')
buff = (random.randrange (1,2))
if buff == 1:
  print('je krijgt +1 defense')
  player_defense += 1
else:
  print('je krijgt 2 health')
  player_health += 2
print('je voelt je geweldig maar je weet ook dat je verder moet en ga naar de deur om naar de volgende kamer te gaan')
print('')
time.sleep(1)
#== kamer3 ==#
print('Je duwt de deur open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarachter een goblin en daarom een zwaard, een schild, een boog, een toverstok en een sleutel.')
while player_ruby > 0:
    if player_ruby > 1:
        item2 = input('wat wil je?[schild = 1,zwaard = 1,boog = 1,toverstok = 1,sleutel = 2] ')
        if item2 == 'schild':
            player_defense += 1
            player_ruby -= 1
        elif item2 == 'boog':
            player_attack += 3
            player_ruby -= 1
        elif item2 == 'toverstok':
            player_attack += 4
            player_defense -= 1
            player_health -= 1
            player_ruby -= 1
        elif item2 == 'sleutel':
            heeft_sleutel = True
            player_ruby -= 2
        else:
            player_attack += 2
            player_health += 1
            player_ruby -= 1    
    if player_ruby > 0:
        item = input('wat wil je?[schild = 1,zwaard = 1,boog = 1,toverstok = 1] ')
        if item == 'schild':
            player_defense += 1
            player_ruby -= 1
        elif item == 'boog':
            player_attack += 3
            player_ruby -= 1
        elif item == 'toverstok':
            player_attack += 4
            player_defense -= 1
            player_health -= 1
            player_ruby -= 1
        else:
            player_attack += 2
            player_health += 1
            player_ruby -= 1
if player_ruby <= 0:
    print('maar nu je geen rubys meer hebt/hebt vraagt de goblin je vriendelijk te verlaten')
kamer = 4
print('')
time.sleep(1)
# === [kamer 4] === #
mega_zombie_attack = 2
mega_zombie_defense = 0
mega_zombie_health = 3
print(f'Dapper loop je de kamer binnen.')
print('Je loopt tegen een mega zombie aan die naast de grafsteen van heer necrus staat.')

mega_zombie_hit_damage = (mega_zombie_attack - player_defense)
if mega_zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de mega zombie, hij kan je geen schade doen.')
else:
    mega_zombie_attack_amount = math.ceil(player_health / mega_zombie_hit_damage)
    
    player_hit_damage = (player_attack - mega_zombie_defense)
    player_attack_amount = math.ceil(mega_zombie_health / player_hit_damage)

    if player_attack_amount < mega_zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health - mega_zombie_attack}.')
    else:
        print('Helaas is de mega zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de lege kamer staan.')
print('Je loopt er naartoe.')
if heeft_sleutel == True:
  print('je ziet dat je met de sleutel de kist kan openen en vind daarin spullen en win je het spel')
  print('EINDE')
else:
   print('je ziet dat de schatkist alleen met een sleutel kan openen die je niet hebt en verleis je het spel')
   print('Game over')  
