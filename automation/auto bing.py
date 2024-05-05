import pyautogui, random, requests, time 
screenWidth, screenHeight = pyautogui.size()
print(screenWidth,screenHeight)
# pyautogui.moveTo(200, 1750)
# pyautogui.click()  

# pyautogui.click('search') # wnats image file




response = requests.get(
    'https://www.mit.edu/~ecprice/wordlist.10000',
    timeout=10)

# Here we are decoding the response and storing it in a variable for further use 
randomWords = response.content.decode('utf-8')
# Getting a list of all the words without spaces basically 
words = randomWords.splitlines()
# Choosing a random word from the list every time
# random_word = random.choice(words)

# open edge
pyautogui.click(200, 1750)  
pyautogui.write('edge', interval=.25)
time.sleep(.5)
pyautogui.write('\n', interval=.25)
time.sleep(2)
# start e's
# pyautogui.write('e\n', interval=0.25)

# more ees
for i in range(150//5 ):
    
    pyautogui.write(f'{random.choice(words)}\n', interval=0.25)


    pyautogui.moveTo(400+random.randrange(-40,401), 165+random.randrange(-20,21))  
    pyautogui.doubleClick() 
    time.sleep(random.randrange(15,20)+random.randrange(100)/100)
pyautogui.alert('done!')








