# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]
seats = 0
def seats_total(seats):
   
   for row in cinema_seats:
      for seat in row:
            seats +=1
   return seats

def seats_available(seats):
   for row in cinema_seats:
       for seat in row:
           if seat == 'A':
                seats+=1
   return seats

def seats_booked(seats):
   for row in cinema_seats:
       for seat in row:
           if seat == 'B':
                seats+=1
   return seats

def seat_status(seats, row, place):
    for row in cinema_seats[row-1:row]:
        for seat in row[place-1:place]:
            if seat == 'A':
                return 'Seat availabe'
            elif seat == 'B':
                return 'Seat booked'
            

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(seats))
print('Seats available:',seats_available(seats))
print('Seats booked:',seats_booked(seats))
print('Seat in row 1, place 1:',seat_status(seats,1,1))
print('Seat in row 5, place 5:',seat_status(seats,5,5))
print('Seat in row 3, place 5:',seat_status(seats,3,5))