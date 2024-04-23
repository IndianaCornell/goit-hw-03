import random

def get_numbers_ticket(min, max, quantity):  

    if min >= 0 and 0 < max <= 999 and quantity > 0: 

        ticket_numbers = set()

        while len(ticket_numbers) != quantity: 
            random_number = random.randint(min,max)
            ticket_numbers.add(random_number)

        return ticket_numbers
    
    else: 
      return "Numbers cannot be negative. Also the maximum number allowed in the lottery is less than 1000. "

res = get_numbers_ticket(0, 180, 5)
print(res)