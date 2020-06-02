import random
import wordshm
import keyboard
from playsound import playsound

rand = random.choice(wordshm.words)
secret = list(rand)
secret1 = rand
sec = list(secret1)
for k in sec:
    if sec.count(k) > 1:
        sec.remove(k)
hidden = list('*' * len(secret))
correctly_guessed = []
wrongly_guessed = []
isOn = False
attemptc = 0
attemptsm = 4
guessed_already = []
h = 0

print("Press any key to start HANGMAN or backspace to exit!")
while True:
    if keyboard.read_key() == "backspace":
        print('\nOK! Remember to come back later.')
        playsound('exit.wav')
        break
    else:
        isOn = True
        keyboard.press_and_release('backspace')
        break


while isOn:
    h += 1
    if h == 1:
        playsound('welcome.mp3')
        guess = input('\nWELCOME! Guess a letter or word')

    else:
        guess = input('\nGuess a letter or word')
    isWord = False
    if len(guess) > 1:
        isWord = True
    if isWord:
        if guess == secret1:
            print('You win!')
            print(f"\nRevealed Word: {''.join(hidden).upper()}")
            playsound('win.mp3')
            isOn = False
            break
        else:
            attemptc += 1
            print('\nTry again, wrong guess.')
            print('|------------')
            print('|           |')
            print('|           ' + ('O' if guess in wrongly_guessed or guessed_already and attemptc >= 1 else ''))
            print('|          ' + ('/ \\' if guess in wrongly_guessed or guessed_already and attemptc >= 2 else '')),
            print('|           ' + ('|' if guess in wrongly_guessed or guessed_already and attemptc >= 3 else '')),
            print('|          ' + ('/ \\' if guess in wrongly_guessed or guessed_already and attemptc == 4 else '')),
            print('|')
            print('|_____________')
            playsound('wrong.wav')
            print(f'\nattempts left: {attemptsm - attemptc}')
            isWord = False

    if len(guess) == 1:
        if guess not in guessed_already:
            if guess in secret:
                print("\nCorrectly guessed!")
                playsound('correct.wav')
                guessed_already.append(guess)
                count = secret.count(guess)
                correctly_guessed.append(guess)
                if count >= 1:
                    for ele in range(len(hidden)):
                        ind = secret.index(guess)
                        if ele == ind:
                            hidden[ele] = guess
                        if count == 2:
                            ind2 = secret.index(guess, ind + 1)
                            if ele == ind2:
                                hidden[ele] = guess
                        if count == 3:
                            ind2 = secret.index(guess, ind + 1)
                            ind3 = secret.index(guess, ind2 + 1)
                            if ele == ind2:
                                hidden[ele] = guess
                            if ele == ind3:
                                hidden[ele] = guess
                        if count == 4:
                            ind2 = secret.index(guess, ind + 1)
                            ind3 = secret.index(guess, ind2 + 1)
                            ind4 = secret.index(guess, ind3 + 1)
                            if ele == ind2:
                                hidden[ele] = guess
                            if ele == ind3:
                                hidden[ele] = guess
                            if ele == ind4:
                                hidden[ele] = guess
                        if count == 5:
                            ind2 = secret.index(guess, ind + 1)
                            ind3 = secret.index(guess, ind2 + 1)
                            ind4 = secret.index(guess, ind3 + 1)
                            ind5 = secret.index(guess, ind4 + 1)
                            if ele == ind2:
                                hidden[ele] = guess
                            if ele == ind3:
                                hidden[ele] = guess
                            if ele == ind4:
                                hidden[ele] = guess
                            if ele == ind5:
                                hidden[ele] = guess
                        if count == 6:
                            ind2 = secret.index(guess, ind + 1)
                            ind3 = secret.index(guess, ind2 + 1)
                            ind4 = secret.index(guess, ind3 + 1)
                            ind5 = secret.index(guess, ind4 + 1)
                            ind6 = secret.index(guess, ind5 + 1)
                            if ele == ind2:
                                hidden[ele] = guess
                            if ele == ind3:
                                hidden[ele] = guess
                            if ele == ind4:
                                hidden[ele] = guess
                            if ele == ind5:
                                hidden[ele] = guess
                            if ele == ind6:
                                hidden[ele] = guess
            elif guess not in secret:
                guessed_already.append(guess)
                print("\nThis letter doesn't appear in the word.")
                attemptc += 1
                playsound('wrong.wav')
                print(f'\nattempts left: {attemptsm - attemptc}')
        else:
            if guess in guessed_already:
                print("\nYou've tried this already")
                attemptc += 1
                playsound('wrong.wav')
                print(f'\nattempts left: {attemptsm - attemptc}')

        correctly_guessed.sort()
        sec.sort()
        if correctly_guessed == sec:
            print('\nYou won!')
            isOn = False
            print(f"\nRevealed Word: {''.join(hidden).upper()}")
            playsound('win.mp3')
            break
        print('|------------')
        print('|           |')
        print('|           ' + ('O' if guess in wrongly_guessed or guessed_already and attemptc >= 1 else ''))
        print('|          ' + ('/ \\' if guess in wrongly_guessed or guessed_already and attemptc >= 2 else '')),
        print('|           ' + ('|' if guess in wrongly_guessed or guessed_already and attemptc >= 3 else '')),
        print('|          ' + ('/ \\' if guess in wrongly_guessed or guessed_already and attemptc == 4 else '')),
        print('|')
        print('|_____________')

        if attemptc == attemptsm:
            print(f'\nYou lost :(\nThe word to be guessed was: {str(secret1).upper()}')
            playsound('lose.wav')
            break

        print(f"\nRevealed Word: {''.join(hidden).upper()}")




















