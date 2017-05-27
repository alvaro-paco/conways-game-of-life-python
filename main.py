from game import Game

ECOSYSTEM = {
    (2, 2),
    (1, 2),
    (0, 2),
    (2, 1),
}


def main():
    game = Game(20, 20, ECOSYSTEM)
    print(game)
    game.next_generation()
    i = 0
    for char in str(game):
        if char == "*":
            print(i, char)
        i += 1

if __name__ == '__main__':
    main()