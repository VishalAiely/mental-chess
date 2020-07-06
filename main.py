from audio import speak, get_audio, get_move
import chess
import chess.svg
import playsound
from stockfish import Stockfish
from datetime import datetime
import random

#Gets player move and makes sure it is valid
def playermove(boardstate):
    move = get_move()

    if 'quit' in move:
        speak('Thanks for playing, here is the board')
        print(boardstate)
        exit()

    while True:
        try:
            if chess.Move.from_uci(move) in boardstate.legal_moves:
                return move
            else:
                #playsound.playsound('audio/invalid.mp3')
                speak('Invalid move, try again')
        except:
            #playsound.playsound('audio/nohear.mp3')
            speak("I didn't hear that")
            #print(f'I heard: {move}')


        move = get_move()

        if 'quit' in move:
            speak('Thanks for playing, here is the board')
            print(boardstate)
            exit() 
    
    
    return move

def main():
    #Deteremine start
    random.seed(datetime.now())
    white = random.randint(0,1)

    #initialize board and stockfish
    board = chess.Board()
    fishy = Stockfish('/Users/vishalaiely/Downloads/stockfish-11-mac/Mac/stockfish-11-64')

    if white:
        #playsound.playsound('audio/WhiteStart.mp3')
        speak('Hello, you have the white pieces')
    else:
        #playsound.playsound('audio/BlackStart.mp3')
        speak('Hello, you have the black pieces')

    #Game executes and breaks when over
    while not board.is_game_over():
        if white:
            board.push_uci(playermove(board))

            fishy.set_fen_position(board.fen())
            compMove = fishy.get_best_move()
            board.push_uci(compMove)

            speak(compMove)

        else:
           fishy.set_fen_position(board.fen())
           compMove = fishy.get_best_move()
           board.push_uci(compMove)

           speak(compMove)

           board.push_uci(playermove(board))

    #Determines end state of game
    if board.result() is '1-0':
        #playsound.playsound('audio/WhiteWin.mp3')
        speak('White wins')
    elif board.reset() is '0-1':
       #playsound.playsound('audio/BlackWin.mp3')
       speak('Black wins')
    elif board.is_stalemate():
        speak('Stalemate')
    else:
        speak('Draw')

    speak('Thank you for playing!')
    
if __name__ == '__main__':
    main()