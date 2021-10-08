


class ParkingGarage:
    def __init__(self, tickets=10, parkingSpaces=10, currentTicket={}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        
    def takeInput(self):
        action = input("Would you like to: Park, Pay or Leave? ")
        
        if action.lower()=='park':
            self.takeTicket()
        elif action.lower()=='pay':
            self.payForParking()
        elif action.lower()=='leave':
            self.leaveGarage()
        else:
            print('I do not recognize that word. ')
            
    def takeTicket(self):
        if self.tickets > 0 and self.parkingSpaces > 0:
            self.currentTicket[self.tickets] = ""
            print(f"Here is ticket number {self.tickets}")
            self.tickets -= 1
            self.parkingSpaces -= 1
        else:
            print("Parking lot is full, please come again later.")
        self.takeInput()    
        
    def payForParking(self):
        ticketNum = int(input("Enter your ticket number: "))
        
        if ticketNum in self.currentTicket.keys():
            input("Type 'pay' to pay. ")
            del self.currentTicket[ticketNum]
            print("Leave Garage: ")
            self.leaveGarage()
            
        else:
            self.leaveGarage(True)
            
    def leaveGarage(self, cleared=False):
        if not cleared:
            ticketNum = int(input("Enter your ticket number: "))
            if ticketNum not in self.currentTicket:
                self.tickets += 1
                self.parkingSpaces += 1
                print('All clear, goodbye.')
            else:
                print('looks like you forgot to pay...')
                self.payForParking()
        else:
            print('Already payed, have a nice day.')
        self.takeInput()
            
def runGarage():
    ParkingGarage().takeInput()

# runGarage()