from playingField import PlayingField

game = PlayingField()
player = 1
while True:
    print(game)
    player_input = int(input(f"Player {player}: Select column\n"))
    move_result = game.make_move(player_input, player)

    if move_result == 2:
        print(game)
        print(f"PLAYER {player} WON THE GAME!")
        break

    if player == 1 and move_result != -1:
        player = 2
    elif move_result != -1:
        player = 1
