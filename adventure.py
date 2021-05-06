#name = input('What is your name? ')
#subject = input('What is your favorite color? ')

#text = ('%s\'s favorite color is %s.') % (name, subject)
# print(text)

encounter = input(
    'A giant serpent appears before you! What will you use to slay it? ')
damage = int(input('How much damage do you think it did? '))

prompt = ('You swipe the giant serpent with an %s for %d dmg' + "! " +
          'The serpent slithers away.') % (encounter, damage)

if damage == 0:
    print("You cower before the mighty serpent and flee.")
else:
    print(prompt.upper())
