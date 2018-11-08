import random, shelve

score = shelve.open('MathHS')
try:
    print('CURRENT HIGH SCORE: ' + str(score['score']))
except:
    print('CURRENT HIGH SCORE: 0')
    score['score'] = 0
    
currentScore = 0
print('TIMES TABLE TESTER'.center(30,'*'))
print('Enter Q as an answer at any time to quit.')

valid = True
while valid:
    try:
        low = int(input('[To test numbers 1-5 enter 1 here and 5 in the next prompt]\nEnter lower end of range to test: '))
        high = int(input('Enter higher limit of range to test: '))
        valid = False
    except:
        print('Invalid entry, please enter a number.')

if low> high:
    low, high = high,low

while True:
    
    x= random.randint(low,high)
    y= random.randint(low,high)
    answer = x * y
    userAnswer = input('%s * %s = ' % (x,y))
	
    if userAnswer.lower() == 'q':
        print('Ending program...')
        break
    while type(userAnswer) != int:
        try:
            userAnswer = int(userAnswer)
            
        except ValueError:
            print('Not a valid answer, lets try that again.')
            userAnswer = input('%s * %s = ' % (x,y))
        
    if int(userAnswer) == answer:
        print('Correct')
        currentScore += 1
    else:
        print('[X]%s * %s = %s\n' % (x,y,answer))
        if currentScore > score['score']:
            score['score'] = currentScore
        print('Streak lost! %s points.' % (currentScore))
        print('Current high score: %s' % (score['score']))
        currentScore = 0