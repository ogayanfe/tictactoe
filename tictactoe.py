import time


class TicTacToe:
    def __init__(self):
        self.dictionary = {
            '1': ' ',
            '2': ' ',
            '3': ' ',
            '4': ' ',
            '5': ' ',
            '6': ' ',
            '7': ' ',
            '8': ' ',
            '9': ' '
        }
        self.message1 = 'Player 1 wins!!'
        self.message2 = 'Player 2 wins!!'

    def display_board(self):
        print(f'''
    _____________                      
    | {self.dictionary["1"]} | {self.dictionary["2"]} | {self.dictionary["3"]} |
    |___|___|___|
    | {self.dictionary["4"]} | {self.dictionary["5"]} | {self.dictionary["6"]} |
    |___|___|___|
    | {self.dictionary["7"]} | {self.dictionary["8"]} | {self.dictionary["9"]} |
    |___|___|___|
        ''')

    def player1(self):
        while True:
            intake = input('Player 1 play (x): ')
            if self.dictionary.get(intake) == ' ':
                self.dictionary[intake] = 'x'
                break
            else:
                try:
                    int(intake)
                    if int(intake) > 0:
                        print('Position occupied!!')
                    else:
                        print('Numbers Zero or less are invalid inputs')
                except ValueError:
                    print('Enter a valid position (1-9)')

    def player2(self):
        while True:
            intake = input('Player 2 play (o): ')
            if self.dictionary.get(intake) == ' ':
                self.dictionary[intake] = 'o'
                break
            else:
                try:
                    int(intake)
                    if int(intake) > 0:
                        print('Position occupied!!')
                    else:
                        print('Numbers Zero or less are invalid inputs')
                except ValueError:
                    print('Enter a valid position')

    def win_checker(self):
        if self.dictionary['1'] == self.dictionary['2'] == self.dictionary['3'] != ' ':
            if self.dictionary['1'] == 'x':
                print(self.message1)
            else:
                print(self.message2)
            time.sleep(10)
            quit()

        if self.dictionary['4'] == self.dictionary['5'] == self.dictionary['6'] != ' ':
            if self.dictionary['4'] == 'x':
                print(self.message1)
            else:
                print(self.message2)
            time.sleep(10)
            quit()

        if self.dictionary['7'] == self.dictionary['8'] == self.dictionary['9'] != ' ':
            if self.dictionary['8'] == 'x':
                print(self.message1)
            else:
                print(self.message2)
            time.sleep(10)
            quit()

        if self.dictionary['1'] == self.dictionary['4'] == self.dictionary['7'] != ' ':
            if self.dictionary['1'] == 'x':
                print(self.message1)
            else:
                print(self.message2)
            time.sleep(10)
            quit()

        if self.dictionary['2'] == self.dictionary['5'] == self.dictionary['8'] != ' ':
            if self.dictionary['2'] == 'x':
                print(self.message1)
            else:
                print(self.message2)
            time.sleep(10)
            quit()

        if self.dictionary['3'] == self.dictionary['6'] == self.dictionary['9'] != ' ':
            if self.dictionary['3'] == 'x':
                print(self.message1)
            else:
                print(self.message2)
            time.sleep(10)
            quit()

        if self.dictionary['1'] == self.dictionary['5'] == self.dictionary['9'] != ' ':
            if self.dictionary['1'] == 'x':
                print(self.message1)
            else:
                print(self.message2)
            time.sleep(10)
            quit()

        if self.dictionary['7'] == self.dictionary['5'] == self.dictionary['3'] != ' ':
            if self.dictionary['7'] == 'x':
                print(self.message1)
            else:
                print(self.message2)
            time.sleep(5)
            quit()

    def main(self):
        print("Xs and Os by @O.A.G")
        print('Enter a position between (1-9)')
        print('Decimal numbers like 1.0, 1.4, 3.7 is not a valid position')
        player = 1
        self.display_board()
        count = 1
        while count <= 9:
            self.win_checker()
            if player == 1:
                self.player1()
                self.display_board()
                player = 2
            else:
                self.player2()
                self.display_board()
                player = 1
            count += 1

        else:
            print("It's a draw")
            time.sleep(10)


game = TicTacToe()
game.main()
