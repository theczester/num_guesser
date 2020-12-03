import random
import time

def main():
    num_of_guesses = 0

    num_range = input('Wybierz maksymalną liczbe która może zostać wylosowana (od 0 do...): ')
    try:
        num_range = int(num_range)
        if num_range < 0:
            print('Wybierz liczbę większą od zera!')
            return main()
    except:
        print('Wpisz liczbę!')
        return main()

    random_num = random.randint(0, num_range)
    print(random_num)
    while True:
        guess = input('Wpisz zgadywaną liczbę: ')
        print('\n')
        try:
            guess = int(guess)
            if guess > num_range:
                print('Twoja liczba nie może być większa od zakresu, który wybrałeś!', end='\n'*2)
                continue
            elif guess < 0:
                print('Twoja liczba nie może być mniejsza od zera!', end='\n'*2)
                continue
        except:
            print('Wpisz liczbę!', end='\n'*2)
            continue
        if guess == random_num:
            print('Brawo!!! Zgadłeś liczbę w ', num_of_guesses+1, ' próbach')
            print('\n')
            print('Następna runda rozpocznie się za...', end='\n'*2)
            for i in range(3, -1, -1):
                print(i)
                time.sleep(1)
            print('\n'*2)
            main()
        elif guess > random_num:
            print('Wylosowana liczba jest mniejsza od tej którą wpisałeś!')
        elif guess < random_num:
            print('Wylosowana liczba jest większa od tej którą wpisałeś!')
        print('\n')
        num_of_guesses += 1

main()
