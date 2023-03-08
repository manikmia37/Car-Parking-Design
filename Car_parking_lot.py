class Car:
    def __init__(self,license, model, color):
        self.license=license
        self.model=model
        self.color=color

    def __repr__(self):
        return f"{self.license},{self.model},{self.color}"

class Garage:
    def __init__(self):
        self.car_added=[]
        self.spot=10
        self.car_infos={}
        self.bill=0
        self.ticket=[]

    def spot_available(self):
        if self.spot > 0:
            return self.spot
     
    def car_added_to_Garage(self,car):
        self.spot_name=["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1"]
        if self.spot_available()>0:
           user_data=str(car).split(",")
           #print(user_data)
           self.spot -= 1
           self.car_added.append(user_data)
           self.car_infos={"Ticket":[], "license":[], "Model":[], "Color":[]}

           for i, value in enumerate(self.car_added):
               #print(i,value)
               #print("\n\n")
               ticket=self.spot_name[i] + value[0]
               #print(ticket)
               self.car_infos["Ticket"].append(ticket)
               self.car_infos["license"].append(value[0])
               self.car_infos["Model"].append(value[1])
               self.car_infos["Color"].append(value[2])
           print(f"Successfully parked! You ticket is {ticket}\n")
        else:
            print("No space available\n")

    def remove_car(self, ticket, hour):
        #spot_len=len(self.car_infos["Ticket"])
        found=False
        if ticket not in self.car_infos['Ticket']:
            print("Your car not found")
        else:
            for i, val in enumerate(self.car_infos["Ticket"]):
                #print(i,val)
                if val==ticket:
                    print(f"Your license is : {self.car_infos['license'][i]}")
                    print(f"Your Model is : {self.car_infos['Model'][i]}")
                    print(f"Your Color is : {self.car_infos['Color'][i]}")

                    self.car_infos["Ticket"].pop(i)
                    self.car_infos["license"].pop(i)
                    self.car_infos["Model"].pop(i)
                    self.car_infos["Color"].pop(i)
                    self.spot += 1
            found=True
        if found == True:
            if hour > 20:
                print(f"Total bill = {hour*5 + 100} dollar\n")
            else:
                print(f"Total bill = {hour*5} dollar\n")


    def total_cars(self):
        count=0
        for i in self.car_infos['Ticket']:
            #print(i)
            count += 1
        print("Total Car : \n",count)
            

                    
    
        

my_garage=Garage()
while True:
    print("________Welcome Our Parking Lot________\n")
    print("1.Check available Parking Lot\n2. Park Your Car\n3. Remove Your car\n4. Show Toatl Cars")
    option=int(input("Choose Option: "))
    if option==1:
        spot=my_garage.spot_available()
        print(f"Available Spot is {spot}\n")

    elif option==2:
        license=input("Give Car License: ")
        Model=input("Give Car Model: ")
        Color=input("Give Car Color: ")
        user_car_1=Car(license,Model,Color)
        my_garage.car_added_to_Garage(user_car_1)
    elif option==3:
        if my_garage.spot_available()==10:
            continue
        else:
            ticket=input("Give Your Ticket: ")
            hour=int(input("Enter Your Spending Time: "))
            my_garage.remove_car(ticket,hour)
    elif option==4:
         my_garage.total_cars()




#print(my_garage.car_infos)


