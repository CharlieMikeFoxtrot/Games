import random,time

def checkhand(hand):
    adj = 0
    handsum = 0
    for n in hand:
        if n == 11:
            adj += 1
        if n == 12:
            adj += 2
        if n == 13:
            adj += 3		
    	
    if 1 in hand:
        handsum = sum(hand)
        for n in hand:
            if n == 1:
                if handsum + 9 - adj <= 21:
                    handsum += 9
        return handsum - adj
    else:
        return sum(hand) - adj
	


def displaycards(hand):
    displayhand=''
    for card in hand:
        if card in [1,10,11,12,13]:
            if card == 1:
                card = 'A'
            elif card == 10:
                card = 'T'
            elif card == 11:
                card = 'J'
            elif card == 12:
                card = 'Q'
            else:
                card = 'K'
        displayhand += '[%s]' % card
    return displayhand

def printhand(dealer, hand , dp ='dealer'):
    if dp == 'player':
        print('Dealers hand %s[ ]\nPlayers hand %s \nPlayer Total: %s' % (displaycards(dealer)[0:3],displaycards(hand),checkhand(hand)))
    else:
        print('``````````````````````````````````````````````````````')
        print('Dealers hand %s\nDealer Total: %s \nPlayers hand %s \nPlayer Total: %s' % (displaycards(dealer),checkhand(dealer),displaycards(hand),checkhand(hand)))
        print('``````````````````````````````````````````````````````')
        
def blackjack():
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]*4
    random.shuffle(deck)
    
    playerhand = []
    dealerhand = []
    
    dealerhand.append(deck.pop())
    dealerhand.append(deck.pop())
    playerhand.append(deck.pop())
    playerhand.append(deck.pop())
    
    printhand(dealerhand,playerhand,'player')
    
    stayhit = input('Would you like to hit or stay?[Stay/Hit]')
    while stayhit.lower() not in ['stay','hit']:
        print('Please select to stay or hit')
        stayhit = input('Would you like to hit or stay?[Stay/Hit]')
	
    while stayhit.lower() != 'stay' and checkhand(playerhand) < 22:
        playerhand.append(deck.pop())
        printhand(dealerhand,playerhand,'player')
        if checkhand(playerhand) < 22:
            stayhit = input('Would you like to hit or stay?[Stay/Hit]')

	
    playerhandvalue = checkhand(playerhand)
    


    if playerhandvalue > 21:
        print('Bust! You lose, Game Over!')
        return
	
    printhand(dealerhand,playerhand,'dealer')
    while checkhand(dealerhand) <= playerhandvalue:
        print('Dealer Draws')
        time.sleep(1)
        dealerhand.append(deck.pop())
        printhand(dealerhand,playerhand)
        time.sleep(2)
        

    print('Final Board')
    if checkhand(dealerhand) > 21:
        printhand(dealerhand,playerhand)
        print('Dealer Bust! You Win!')


    elif checkhand(dealerhand) > playerhandvalue:
        printhand(dealerhand,playerhand)
        print('Dealer wins!')

def main():
    play = True
    while play:
        blackjack()
        response = input('Would you like to play again? (Y/N)')
        while response.lower() not in ['y','n']:
            print('Invalid input.')
            response = input('Would you like to play again? (Y/N)')
        if response.lower() == 'n':
            play = False
main()