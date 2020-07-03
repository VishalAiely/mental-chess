from audio import speak, get_audio
import chess
import chess.svg

def main():
    board = chess.Board()
    print(board)
    board.push_san('e4')
    print(board)

if __name__ == '__main__':
    main()