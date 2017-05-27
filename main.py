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
    #game.next_generation()
    i = count = 0
    for char in str(game):
        if char == "*":
            count += 1
            print(i, char)
        i += 1
    print(str(game).count("*"))

if __name__ == '__main__':
    main()