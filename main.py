
'''
  Script: Begin a Quest 
  Date: 3/28/22 
  Developers: 
      Arabella McEntire(main menu, swamp, choice function, color)
      Malia Sweet(hierarchy)
      Brian Walters(catacombs and all fight modules)            Kaleb Crume (prompt lair, prompt fortress, item functions)
      Ganon Mabrey(ending, plaque)
  Purpose: The user creates a character and embarks on a quest for loot in order to defeat a dragon and save the kingdom
'''

# Import random so we can generate a random number
import random

#prints the witches hat
def hat():
    h = ["        /\\","       /  \\","      /    \\","     /      \\","_----------------_"," ----------------"]
    for hat in h:
      print(color.RED + hat + color.END)
#prints the gem
def gem():
  h = 5
  for i in range(h):
      print(color.PURPLE + " "*(h-i), "*"*(i*2+1) + color.END)
  for i in range(h-2, -1, -1):
      print(color.PURPLE + " "*(h-i), "*"*(i*2+1) + color.END)
    
#prints the sword
def sword():
    s = ["    /\\","    ||","    ||","    ||","    ||","    ||", "  +====+","    ||","   <-->"]
    for sword in s:
      print(color.GREEN + sword + color.END)
#prints the shield
def shield():
    b = ["|\__/\__/|","|   ++   |","\ ==++== /"," \==++==/",  "  \ ++ /","   \++/","    \/"]
    for shield in b:
      print(color.CYAN + shield + color.END)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# categories for multiple accepted inputs
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]
optionABCD = ("\n\n*** Use only A, B, C, or D ***\n")
optionYN = ("\n\n*** Use only Y/N, y/n, Yes/No, or yes/no ***\n")

global luckyNumber
luckyNumber = random.randint(20,80)
bossNumber = random.randint(0, 50)

def tenmore():
  global luckyNumber
  luckyNumber += 10
  print(color.BLUE + "\nYour Lucky Number is now: " + str(luckyNumber) + color.END)
  return True
  
def getName():  # Get Name Module - asks the user name and generates their lucky number
  print("Princess: What is your name, great hero?\n")
  global userName
  global luckyNumber
  userName = input(">>> ")
  print("\nPrincess: \"Thank you for agreeing to embark on a quest to save our kingdom, " + userName + ". Let us ask the oracles to determine your luck... ", luckyNumber, "\n\nA day passes, and you return to the princess's castle with your strongest armor and your trusty steed. You are ready to embark on the quest!\n")


def intro():  # Intro Module - Introduces them to the goal of the quest and asks if they would like to begin.
  print("[The Castle]\n" + color.BLUE + "Your Lucky Number is: " + str(luckyNumber) + color.END + "\n\nPrincess: \"In order to save the kingdom from being conquered by the dragons, we must retrieve the Sacred Emerald from the Queen Dragon's lair! However, you cannot go without some trusty items to help protect you. There are magical lands in the dangerous areas of our kingdom that if you venture to with a pure heart and a good intentions, you will come out victorious and stronger.\"\n Are you up for the quest to save the Sacred Emerald? \n\n[Y/N]\n\n")
  userChoice = input(">>> ")
  if userChoice in no: 
    print("\nYou return to your home defeated, and days later your kingdom falls to ruin while you stand idly by. Hope you enjoyed not taking any risks...")
    exit()
  if userChoice in yes:
    print("Onward!\n")
# defensive programming else clause
  else: 
    print(optionYN)
    intro()


def mainMenu(luckyNumber):  # Main Menu Module - User can choose the next location (module) to venture to to get loot
    print("\n[The Hero's Base]\n" + color.BLUE + "Your Lucky Number is: " + str(luckyNumber) + color.END + "\n\nChoose a location to venture to: The Hazy Swamp, The Bottomless Catacombs, The Impenetrable Fortress, or the Dragon's Lair.\n\nA: The Hazy Swamp\nB: The Bottomless Catacombs\nC: The Impenetrable Fortress\nD: The Dragon's Lair\n")
    userLocation = input(">>> ")
    if userLocation in answer_A:
      swamp()
    elif userLocation in answer_B:
      catacombs()
    elif userLocation in answer_C:
      fortress()
    elif userLocation in answer_D:
      lair(luckyNumber)
# defensive programming else clause
    else:
      print(optionABCD)
      mainMenu()


def swamp():  # Swamp Module - Location 1 where the user gets one loot option and upped stats
  print("\n[The Hazy Swamp]\n\nYou journey over perilous mountains and through turmultuous caverns to reach the Hazy Swamp. When you arrive there you see a house on stilts in a murky area of the swamp. Do you approach?\n\n[Y/N]\n\n")
  userChoice = input(">>> ")
  bossNumber = random.randint(0, 50)
  if userChoice in yes:
    print("\nYou approach the mysterious house and scale the side. You see a witch crouched over a cauldron, stirring menacingly. She spots you peering through the window and shoots a spell at you! How do you attack?\n\nA: Sword\nB: Magic Wand\nC: Fists\nD: Run Away\n\nBoss strength: " + str(bossNumber) + "\n")
    userFight = input(">>> ")
# defensive programming if-else statment
    if userFight in answer_A or userFight in answer_B or userFight in answer_C or userFight in answer_D:
      sFight(userFight, bossNumber)
    else:
      print(optionABCD)
      swamp()
  if userChoice in no:
    input("\nWelp, you did nothing and you retrieved no loot. Maybe next time you should be a little less cowardly. Press Enter to return to base.")
    mainMenu()
# defensive programming else clause
  else: 
    print(optionYN)
    swamp()


def catacombs():  # Catacomb Module - Location 2 where user gets another loot option
  print("\n[The Bottomless Catacombs]\n\n'Welcome to the bottomless catacombs,' proclaimed an eerie voice in the shadows. 'It's a risky mission... considering what happened to the pervious adventurer. Do you wish seek the bottom?'\n\n[Y/N]\n\n")
  userChoice = input(">>> ")
  bossNumber = random.randint(0, 50)
  if userChoice in yes:
    print("\nYou enter and start down the perceivingly endless, and dimly lit tunnel. Near the end you notice movement but cannot make out what it is. A violent storm approaches along with a loud scream. The sound of the wind is so strong that you feel your chest might burst, and that you cannot move your arms and legs. On the other end of the storm is a stout drougr awaiting your arrival. What would you like to use in this battle against the undead?\n\nA: One-Handed Sword\nB: Bow and Arrow\nC: Destruction Spell\nD: Run Away\n\nBoss strength: " + str(bossNumber) + "\n\n")
    userFight = input(">>> ")
# defensive programming if-else statment
    if userFight in answer_A or userFight in answer_B or userFight in answer_C or userFight in answer_D:
      cFight(userFight, bossNumber)
    else:
      print(optionABCD)
      catacombs()
  if userChoice in no:
    input("\nWelp, you did nothing and you retrieved no loot. Maybe next time you should be a little less cowardly. Press Enter to return to base.")
    mainMenu()
# defensive programming else clause
  else: 
    print(optionYN)
    catacombs()
  

def fortress():  # Fortress Module - Location 3 where user gets a gem
  print("\n[The Fortress]\n\nThe fortress stands tall above you even from a distance. You wait till night to make your approach to the fortress. When you arrive you notice a dranige tunnel with bars just wide enough apart to slip through. Do you wish to enter?\n\n[Y/N]\n\n")
  userChoice = input(">>> ")
  bossNumber = random.randint(0, 50)
  if userChoice in yes:
    print("\nAfter sometime navigating the drainige tunnel you find away in to the fortress above. As you cautiously make your way through the fortress you happen upon the armory. As you look through armory you find a shield of such quality you have never seen before. You start to make your way over to the shield, then you catch movment off the reflection of a sword hanging in front of you. You dodge just as a guard tries to lop your head off with a greatsword. What weapon do you want to use?\n\nA: Sword\nB: Magic Wand\nC: Fists\nD: Run Away\n\nBoss strength: " + str(bossNumber) + "\n\n")
    userFight = input(">>> ")
# defensive programming if-else statment
    if userFight in answer_A or userFight in answer_B or userFight in answer_C or userFight in answer_D:
      fFight(userFight, bossNumber)
    else:
      print(optionABCD)
      fortress()
  if userChoice in no:
    input("\nWelp, you did nothing and you retrieved no loot. Maybe next time you should be a little less cowardly. Press Enter to return to base.")
    mainMenu()
# defensive programming else clause
  else: 
    print(optionYN)
    fortress()
    

def lair(luckyNumber):  # Lair Module - End of game boss fight that displays their loot after they defeat the boss.
  if luckyNumber >= 100: 
    print("\n[The Dragon's Lair]\n\nYou made it to The Dragon's Lair! After scaling the faces of a mountain you stand at the maw of a large cave. A slight breeze picks up and carrries the scent of burnt flesh out from the depths of the cave. Do you wish to proceed?\n\n[Y/N]\n\n")
    userChoice = input(">>> ")
    bossNumber = random.randint(0, 50)
    if userChoice in yes:
      print("\n As you make your way into the cave you step over the crushed bones and the mangled armor of the unfortunate souls who came before you. While you move deeper and deeper into the cave you can hear the dragon breathing in and out. You draw closer and closer to the beast until the breathing  stops. The Dragon opens its eyes and gets to its feet. The beast is now towering above you. What weapon do you want to use?\n\nA: Sword\nB: Magic Wand\nC: Fists\nD: Run Away\n\nBoss strength: " + str(bossNumber) + "\n\n")
      userFight = input(">>> ")
# defensive programming if-else statment
      if userFight in answer_A or userFight in answer_B or userFight in answer_C or userFight in answer_D:
        lFight(userFight, bossNumber)
      else:
        print(optionABCD)
        lair(luckyNumber)
    if userChoice in no:
      input("\nWelp, you did nothing and you retrieved no loot. Maybe next time you should be a little less cowardly. Press Enter to return to base.")
      mainMenu()
# defensive programming else clause
    else: 
      print(optionYN)
      lair(luckyNumber)
  else:
    input("You aren't strong enough to fight the dragon! Why don't you check out the other locations to see if you can pick up some loot that will help you defeat the dragon.\n Press Enter to return to base.")
    mainMenu(luckyNumber)


def sFight(userFight, bossNumber):  # Fight Module - swamp fight module
  global luckyNumber
  if userFight in answer_A or userFight in answer_B or userFight in answer_C or userFight and luckyNumber > bossNumber:
    print("\nThe fight is grueling, but in the end you defeat the witch! You retrieve her Witch's Hat and put it on. Suddenly you are embued with the power of magic.\n")
    hat()
    print("\nPress Enter to return to base.")
    input(">>> ")
    tenmore()
    mainMenu(luckyNumber)
  if userFight in answer_D:
    print("\nWelp, you did nothing and you retrieved no loot. Maybe next time you should be a little less cowardly.\n\nPress Enter to return to base.")
    input(">>> ")
    mainMenu(luckyNumber)
  else: 
    print("\nThe boss was too strong! Looks like you are going to have to try again.\n\nPress Enter to return to base.")
    input(">>> ")
    tenmore()
    mainMenu(luckyNumber)


def cFight(userFight, bossNumber):  # Fight Module - catacombs fight module
  global luckyNumber
  if userFight in answer_A or userFight in answer_B or userFight in answer_C or userFight and luckyNumber > bossNumber:
    print("\nThe fight is grueling, but in the end you defeat the drougr! You retrieve his Ancient sword and weild his might. Suddenly you are embued with power of the undead.\n")
    sword()
    print("\nPress Enter to return to base.")
    input(">>> ")
    tenmore()
    mainMenu(luckyNumber)
  if userFight in answer_D:
    print("\nWelp, you did nothing and you retrieved no loot. Maybe next time you should be a little less cowardly.\n\nPress Enter to return to base.")
    input(">>> ")
    mainMenu(luckyNumber)
  else: 
    print("\nThe boss was too strong! Looks like you are going to have to try again.\n\nPress Enter to return to base.")
    input(">>> ")
    tenmore()
    mainMenu(luckyNumber)


def fFight(userFight, bossNumber):  # Fight Module - fortress fight module
  global luckyNumber
  if userFight in answer_A or userFight in answer_B or userFight in answer_C or userFight and luckyNumber > bossNumber:
    print("\nThe fight is grueling but with some difficulty you dispatch the guard. You grab the shield and leave before more guards show up.\n")
    shield()
    print("\nPress Enter to return to base.\n")
    input(">>> ")
    tenmore()
    mainMenu(luckyNumber)
  if userFight in answer_D:
    print("\nWelp, you did nothing and you retrieved no loot. Maybe next time you should be a little less cowardly.\n\nPress Enter to return to base.")
    input(">>> ")
    mainMenu(luckyNumber)
  else: 
    print("\nThe boss was too strong! Looks like you are going to have to try again.\n\nPress Enter to return to base.")
    input(">>> ")
    tenmore()
    mainMenu(luckyNumber)


def lFight(userFight, bossNumber):  # Fight Module - lair fight module
  global luckyNumber
  if userFight in answer_A or userFight in answer_B or userFight in answer_C or userFight and luckyNumber >= bossNumber:
    print("\nThe fight is grueling, but in the end you vanquish the Dragon! Among the other treasures the Dragon was hoarding you recover the Sacred Emerald.\n")
    gem()
    print ("\nPress Enter to return to show the princess you have saved the kingdom!\n")
    input(">>> ")
    ending()
  if userFight in answer_D:
    print("\nWelp, you did nothing and you retrieved no loot. Maybe next time you should be a little less cowardly.\n\nPress Enter to return to base.")
    input(">>> ")
    mainMenu(luckyNumber)
  else: 
    print("\nThe boss was too strong! Looks like you are going to have to try again.\n\nPress Enter to return to base.")
    input(">>> ")
    tenmore()
    mainMenu(luckyNumber)
    
def ending():
  global userName
  easteregg = ""
  print("\n[The Castle]\n\nYou return to the Princess after defeating The Dragon and recovering the Sacred Emerald.\n\n[Princess]: \"Thank you for saving the Kingdom great hero!\"")
  gem()
# Plaque generator 
  lengthName = len(userName)
  print("~" + "~" * lengthName + "~")
  print("~" + userName + "~")
  easteregg = input("~" + "~" * lengthName + "~")
  if easteregg.upper() == "EGG":
    print("\n\n",
    "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n",
    "───█▒▒░░░░░░░░░▒▒█───\n",
    "────█░░█░░░░░█░░█────\n",
    "─▄▄──█░░░▀█▀░░░█──▄▄─\n",
    "█░░█─▀▄░░░░░░░▄▀─█░░█\n",
    "\n\n")
    exit()
  else:
    exit()

def mainModule():  # Main Module - contains submodules
  getName()
  intro()
  mainMenu(luckyNumber)
  ending()
  
mainModule()