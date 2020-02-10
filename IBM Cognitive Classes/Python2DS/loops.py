Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print (Genre)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
while PlayListRatings[i]>=6:
    print (PlayListRatings[i])
    i=i+1

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

i=0 
while (squares[i]=='orange'):
    new_squares.append(squares[i])
    i=i+1
print (new_squares)