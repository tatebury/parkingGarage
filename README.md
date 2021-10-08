## Parking Garage Ticket Machine Program
#### Plan:
1. Framework: ParkingGarage class which contains an init constructor with variables tickets, parkingSpaces, and currentTicket. And the following 4 class methods:
2. takeInput: this method should be run upon importing/calling the class and ask the user what they want to do(park, pay, or leave).
3. takeTicket: this method is called if the user enters 'park'. If there are any tickets, it first prompts the user to take a ticket, then adds the ticket number to currentTicket and subtracts 1 from tickets and parking spaces.
4. payForParking: this method is called when the user either enters it or the leave method determines that they have not yet payed. Upon receiving the ticket number it looks up that number in the currentTicket dictionary, if not payed, promts the user to input something to simulate paying, then edits currentTicket to show that the ticket is now payed. Once this is all done the leave method is called, passing in the current input.
5. leaveGarage: this method is called either manually by the user or upon completion of the pay method. It checks the input with the dictionary to determine if it has been payed, if not calls payForParking, if so leaves the user a message and adds 1 to tickets and parkingSpaces.
