#Based on Multiple Gift Card Generator 2.0

#setup
import time
import random

#functions
def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

def q(rolls1):
	data1 = "1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result1 = ""
	while rolls1 >= 1:
		c = random.choice(data1)
		result1 = c + result1
		rolls1 = rolls1 - 1
	return result1

def e(rolls2):
	data2 = "1234567890"
	result2 = ""
	while rolls2 >= 1:
		c = random.choice(data2)
		result2 = c + result2
		rolls2 = rolls2 - 1
	return result2

#interface
print("Joshys Multiple Gift Card Generator")
print("")
time.sleep(0.25)
print("""                               /$$
                              | $$
                              | $$                
       /$$  /$$$$$$   /$$$$$$$| $$$$$$$  /$$   /$$
      |__/ /$$__  $$ /$$_____/| $$__  $$| $$  | $$
       /$$| $$  \ $$|  $$$$$$ | $$  \ $$| $$  | $$
      | $$| $$  | $$ \____  $$| $$  | $$| $$  | $$
      | $$|  $$$$$$/ /$$$$$$$/| $$  | $$|  $$$$$$$
      | $$ \______/ |_______/ |__/  |__/ \____  $$
 /$$  | $$                               /$$  | $$
|  $$$$$$/                              |  $$$$$$/
 \______/                                \______/ """)
print("")
time.sleep(0.25)
print("What Giftcard you need to generate?")
print("------------[joshy#4621]--------------")
tt = input("\nAmazon\nRoblox\nWebkinz\nFortnite\nIMVU\nEbay\nNetflix\niTunes\nPaypal\nVisa\nPokemonTGC\nPlaystation\nSteam\nXbox\nPlayStore\nMinecraft\nPandaExpress\nBuild A Bear\nGamestop\nGoogle Play\n\n>")

t = tt.lower()
print("")
print("How many of them?")
nn = input(">")
print("")
n = int(nn)

if t == "minecraft":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "paypal":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "playstation":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "amazon":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))
		
if t == "netflix":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))
		
if t == "steam":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(5))
		
if t == "fortnite":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(4)+"-"+g(4))
		
if t == "roblox":
	for x in range(n):
		print("")
		print(g(3)+"-"+g(3)+"-"+g(4))
		
if t == "itunes":
	for x in range(n):
		print("")
		print(g(16))
		
if t == "ebay":
	for x in range(n):
		print("")
		print(g(10))
		
if t == "imvu":
	for x in range(n):
		print("")
		print(g(10))
		
if t == "webkinz":
	for x in range(n):
		print("")
		print(g(8))
		
if t == "pokemon":
	for x in range(n):
		print("")
		print(g(3)+"-"+g(4)+"-"+g(3)+"-"+g(3))
		
if t == "playstore":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4))
		
if t == "xbox":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5))
		
if t == "pandaexpress":
	for x in range(n):
		print("")
		print(g(9))

if t == "buildabear":
	for x in range(n):
		print("")
		print(e(9)+" pin:"+e(4))
		
if t == "gamestop":
	for x in range(n):
		print("")
		print(e(19)+" pin:"+e(4))
		
if t == "googleplay":
	for x in range(n):
		print("")
		print(q(4)+"-"+q(4)+"-"+q(4)+"-"+q(4)+"-"+q(4))
		

print("")
print("-----Generation completed-----")
print("-----WE LOVE YOU JOSHY <3----")
time.sleep(360)
