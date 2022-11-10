print('welcome to my quiz game')
print('please answer the following questions')
print('lets start')
playing = lambda num: 'hello' if num == 1 else 'bye'
playing = input('do you want to play?')
if playing.lower() != 'yes':
    quit()
print('okay! lets play')
score = 0

answer = input('what does CPU stand for?')
if answer.lower() == 'central processing unit':
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input('what does GPU stand for?')
if answer.lower() == 'graphics processing unit':
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input('what does RAM stand for?')
if answer.lower() == 'random access memory':
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input('what does PSU stand for?')
if answer.lower() == 'power supply unit':
    print('correct')
    score += 1
else:
    print('incorrect')

print('You got' + str(score) + 'questions correct')
print('You got' + str((score/4) * 100) + '%')


import datetime
today = datetime.date.today()
print(today)
print(playing(2))
print(len(playing))