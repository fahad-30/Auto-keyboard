from keyboard_master import keyboard
from sentences import Sen,Emo,emo_i,sen_i

import random
import time

keyboard.wait('esc')

loop = 30
for n in range(loop):
	print(n+1)
	r = random.randint(0,2)
	e = random.randint(3,7)
	t = random.randint(57,64)

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
	time.sleep(1)
	
	keyboard.press('enter')

	time.sleep(t)
		
print("Done")