from datetime import date
from tkinter import *
from math import *
from numpy import *
from wonderwords import RandomSentence
import time
import sys
import turtle
import random
import pygame
import calendar
    
def monthcalendar(): 
    y = int(input("Enter year: "))  
    m = int(input("Enter month: "))  
    print(calendar.month(y,m))      
    
def datecalculator():
    fdate = date(*list(reversed(list(map(int, input("Enter your first date in the form DD/MM/YYYY: ").split("/"))))))
    ldate = date(*list(reversed(list(map(int, input("Enter your second date in the form DD/MM/YYYY: ").split("/"))))))
    print("The second date is " + str((ldate - fdate).days) + " days after the first date")
    
def simplecalculator():
    operations = {'+':(lambda x, y: x+y), '-':(lambda x, y: x-y), '/':(lambda x, y: x/y), '*':(lambda x, y: x*y)}
    try:
        number_1 = int(input("Please enter your first number: "))
        operation = input("Please enter the symbol for the operation you would like to complete(+-/*): ")
        number_2 = int(input("Please enter the second number: "))
        
    except:
        sys.exit("There was an error processing your inputs. Pleae try again")
    print(f"{number_1} {operation} {number_2} = {operations[operation](number_1, number_2)}")

def scicalc():
    class SciCalc:
        global functions, ans, l_key_func
        functions = {'=' : lambda x: eval(x), 'sin': lambda x: sin(radians(float(x))), 'cos': lambda x: cos(radians(float(x))), 'tan':lambda x: tan(radians(float(x))), 'x²':lambda x: float(x)**2,'x³': lambda x: float(x)**3, 
                     'log(x)': lambda x: log(float(x)), '1/x': lambda x: 1/float(x), 'x!': lambda x: factorial(int(float(x))), '√': lambda x: sqrt(float(x)), '³√':lambda x: cbrt(float(x)), '10^x': lambda x:10**float(x)}
        ans = 0
        l_key_func = False
        def __init__(self, master):
            self.master = master
            master.title("Scientific Calculator")
            self.total = StringVar()
            self.entry = Entry(master, textvariable=self.total, borderwidth=5)
            self.entry.grid(row=0, column=0, columnspan=6, pady=6)
            self.button_creator()

        def button_creator(self):
            b_list = [
                [ 'sin', 'cos', 'tan', 'x²', 'x³'],
                ['log(x)', '1/x', 'x!', '√', '³√'],
                ['7', '8', '9', 'C', 'Ans'],
                ['4', '5', '6', '*', '/'],
                ['1', '2', '3', '+', '-'],
                ['0', '.', '10^x', '=', 'Del']
            ]
            for i, row in enumerate(b_list):
                for j, b_text in enumerate(row):
                    button = Button(self.master, text=b_text, width=5, height=3, command=lambda text=b_text: self.click(text))
                    button.grid(row=i + 1, column=j, sticky="nsew")
                self.master.rowconfigure(i + 1, weight=1)
            self.master.columnconfigure(0, weight=1)
            self.master.columnconfigure(1, weight=1)
            self.master.columnconfigure(2, weight=1)
            self.master.columnconfigure(3, weight=1)
            self.master.columnconfigure(4, weight=1)
            self.master.columnconfigure(5, weight=1)

        def click(self, b_text):
            global l_key_func, ans
            if b_text == 'C':
                self.total.set("")
            elif b_text == 'Ans':
                l_key_func = False
                self.total.set(self.entry.get() + str(ans))
            elif b_text == 'Del':
                l_key_func = False
                self.total.set(self.entry.get()[:-1])
            elif b_text in functions:
                l_key_func = True
                try:
                    ans = functions[b_text](self.entry.get())
                    self.total.set(ans)
                except:
                    self.total.set("Error!")
            else:
                if l_key_func == True and b_text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                    self.total.set('')
                l_key_func = False
                self.total.set(self.entry.get() + b_text)

    if __name__ == "__main__":
        root = Tk()
        root.attributes("-topmost", True)
        calc = SciCalc(root)
        root.mainloop()

def typingtest():
    sent_list = []
    sent_para = ""
    for i in range(5):
        sent = RandomSentence()
        random_sent = sent.sentence()
        sent_list.append(random_sent)
        sent_para += random_sent +  " "
    
    def errorrate(sent_para, typed_para):
        errorcount = 0
        length = len(sent_para)
        for character in range(length):
            try: 
                if sent_para[character] != typed_para[character]:
                errorcount += 1
            except:
                errorcount += 1
        errorpercent = errorcount/length * 100
        return errorpercent

    print("Your typing test paragraph: \n")
    print(sent_para)
    print("\n")
    start_time = time.time()
    typed_para = input()
    end_time = time.time()
    time_taken = end_time - start_time
    errorpercent = errorrate(sent_para, typed_para)
    print("\n")

    if errorpercent > 35:
        print(f"Your error rate {error_percent} was fairly high, hence your accurate speed could not be computed.")

    else:
        speed = len(typed_para)/time_taken
        print("Score Report: ")
        print(f"Your typing speed was {speed} words/second.")
        print(f"Your error rate was {errorpercent}.")
     
def tictactoe():    
    pygame.init()
    WIDTH = 600
    HEIGHT = 600
    LINE_WIDTH = 15
    WIN_LINE_WIDTH = 15
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = 200
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 55
    RED = (255, 0, 0)
    BG_COLOR = (20, 200, 160)
    LINE_COLOR = (23, 145, 135)
    CIRCLE_COLOR = (239, 231, 200)
    CROSS_COLOR = (66, 66, 66)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill( BG_COLOR)
    board = zeros((BOARD_ROWS, BOARD_COLS))

    def draw_lines():
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif board[row][col] == 2:
                    pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)	
                    pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

    def mark_square(row, col, player):
        board[row][col] = player

    def available_square(row, col):
        return board[row][col] == 0

    def is_board_full():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    return False
        return True

    def check_win(player):
        for col in range(BOARD_COLS):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                draw_vertical_winning_line(col, player)
                return True
        for row in range(BOARD_ROWS):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                draw_horizontal_winning_line(row, player)
                return True
            if board[2][0] == player and board[1][1] == player and board[0][2] == player:
                draw_asc_diagonal(player)
                return True
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                draw_desc_diagonal(player)
                return True
        return False

    def draw_vertical_winning_line(col, player):
        posX = col * SQUARE_SIZE + SQUARE_SIZE//2
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR
        pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

    def draw_horizontal_winning_line(row, player):
        posY = row * SQUARE_SIZE + SQUARE_SIZE//2
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR
        pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)

    def draw_asc_diagonal(player):
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR
        pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)

    def draw_desc_diagonal(player):
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR
        pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

    def restart():
        screen.fill( BG_COLOR )
        draw_lines()
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                board[row][col] = 0

    draw_lines()
    player = 1
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0] 
                mouseY = event.pos[1] 
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = player % 2 + 1
                    draw_figures()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False
        pygame.display.update()
