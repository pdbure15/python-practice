# Complete the playRPS function below.
def playRPS(player1Throw, player2Throw):
    
    beats = {
        'scissors' : 'rock',
        'rock' : 'paper',
        'paper' : 'scissors'
    }
    
    if player1Throw == player2Throw:
        return 'Tie'
    elif player1Throw == beats[player2Throw]:
        return 'Player 1 Wins'
    elif player2Throw == beats[player1Throw]:
        return 'Player 2 Wins'

if __name__ == '__main__':
    result = playRPS('scissors', 'paper')
    print(result)