from keyboard_master import keyboard
from sentences import Sen,Emo,emo_i,sen_i

import random
import time

keyboard.wait('esc') # trigger to start the bottom script. After placing cursor in the chat box, press 'esc' and wait for the magic.

loop = 30 ## runs the loop for 30 mins approx

for n in range(loop):
	# print(n+1)
	# randint(i,j) gives a random integer between i and j-1.
	r = random.randint(0,2) # triggers one of the if statements
	e = random.randint(3,7) # controls the number of emotes or sentences to type
	t = random.randint(57,64) # twitch can know when you have a bot typing the chat for you. Hence random the time gap between types.

	# emotes
	if r==0:
		e_i = random.randint(0,emo_i-1)
		for _ in range(e):
			keyboard.write(Emo[e_i],delay=0.08)
	
	# random emotes
	elif r==1:
		for _ in range(e):
			e_i = random.randint(0,emo_i-1)
			keyboard.write(Emo[e_i],delay=0.08)
	
	# sentence
	else:
		s_i = random.randint(0,sen_i-1)
		keyboard.write(Sen[s_i],delay=0.08)

	if keyboard.is_pressed('q'):
		break
	time.sleep(random.randint(6,10)/10) # presses enter after 0.6-1 sec. Any thing in between 0.6-1.
	
	keyboard.press('enter')

	time.sleep(t) # runs the loop after 't' seconds.
		
print("Done")
