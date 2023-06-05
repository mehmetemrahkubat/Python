import csv
import datetime 

filename="Orders_Database.csv"

menu = {}
ekmalzeme = {}
with open("menu.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            name, price= line.split(":")
            menu[name] = float(price)

with open("malzemeler.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            name, price= line.split(":")
            ekmalzeme[name] = float(price)

class Pizza:
    def __init__(self):
        self.description = "description"
        self.price = 0.0
        self.id = 0

    def get_totaldescription(self):
        return f"{self.get_description()}"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price

    def get_id(self):
        return self.id

class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description="Klasik Pizza"
        self.price = menu["Klasik Pizza"]
        self.id = 1

class MargheritaPizza(Pizza):  
    def __init__(self):
        super().__init__()
        self.description="Margarita Pizza"
        self.price = menu["Margarita Pizza"]
        self.id = 2

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description="Turk Pizza"
        self.price = menu["Turk Pizza"]
        self.id = 3

class SimplePizza(Pizza):  
    def __init__(self):
        super().__init__()
        self.description="Sade Pizza"
        self.price = menu["Sade Pizza"]
        self.id = 4


class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_totaldescription(self):
        return f"{self.pizza.get_totaldescription()}, {self.description}"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.price
        
    def get_id(self):
        return self.id

class OliveSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.price = ekmalzeme["Zeytin"]
        self.id = 1

class MushroomSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar"
        self.price = ekmalzeme["Mantar"]
        self.id = 2

class GoatCheeseSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keci Peyniri"
        self.price = ekmalzeme["Keci Peyniri"]
        self.id = 3

class MeatSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
        self.price = ekmalzeme["Et"]
        self.id = 4

class OnionSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Sogan"
        self.price = ekmalzeme["Sogan"]
        self.id = 5

class CornSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Misir"
        self.price = ekmalzeme["Misir"]
        self.id = 6

def sosdetaysec(selected_soslar,newpizza):
                if int(selected_soslar[0])==OliveSauce(newpizza).get_id():
                    newsos=OliveSauce(newpizza)
                    return newsos
                elif int(selected_soslar[0])==MushroomSauce(newpizza).get_id():
                    newsos=MushroomSauce(newpizza)
                    return newsos
                elif int(selected_soslar[0])==GoatCheeseSauce(newpizza).get_id():
                    newsos=GoatCheeseSauce(newpizza)
                    return newsos
                elif int(selected_soslar[0])==MeatSauce(newpizza).get_id():
                    newsos=MeatSauce(newpizza)
                    return newsos
                elif int(selected_soslar[0])==OnionSauce(newpizza).get_id():
                    newsos=OnionSauce(newpizza)
                    return newsos
                elif int(selected_soslar[0])==CornSauce(newpizza).get_id():
                    newsos=CornSauce(newpizza)
                    return newsos
                else:
                    print("Yanlış sos girdiniz.")    

def pizzasecim():
    print("Pizzalar:")
    for index,a in enumerate(menu.keys()):
        print(index+1,".",a)
        

    pizza_choice = int(input("Lütfen bir pizza seçin: "))

    if pizza_choice == ClassicPizza().get_id():
        return sossecimi(ClassicPizza())
        

    elif pizza_choice == MargheritaPizza().get_id():
        return sossecimi(MargheritaPizza())


    elif pizza_choice == TurkishPizza().get_id():
        return sossecimi(TurkishPizza())

        
    elif pizza_choice == SimplePizza().get_id():
        return sossecimi(SimplePizza())
   
        
    else:
        print("Yanlış pizza seçtiniz...") 
        return

def sossecimi(newpizza):
        print("Soslar:")
        for index,a in enumerate(ekmalzeme.keys()):
            print(index+1,".",a)

        sos_choice = input("Lütfen bir veya daha fazla sos seçin (virgülle ayırın): ")
        if sos_choice:       
            selected_soslar = sos_choice.split(",")

            if len(selected_soslar)==1:
                newsos=sosdetaysec(selected_soslar,newpizza)

            elif len(selected_soslar)>=2:               
                newsos=sosdetaysec(selected_soslar ,newpizza)
                
                del selected_soslar[0]
                for i in selected_soslar:
                    newsos=sosdetaysec(i,newsos)

            return newsos.get_totaldescription() , newsos.get_cost()
            
        else:
            print("Sos seçmediniz")
            return newpizza.get_totaldescription() , newpizza.get_cost()

def sipariskaydet(siparis) :
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(siparis)

    print("Siparis Oluşturuldu.")
    exit()

def main():
    sepet=[]
    price=0
    while True: 
        siparis=pizzasecim()      
        sepet.append(siparis)
        print(siparis)
        price=price+ siparis[1]      

        print("\n")
        
        while True:
            secim=input("Devam Etmek İstiyor musunuz? E/H ")
            print("\n")
            if(secim== "H"):
                print("        Sepet:",sepet)
                print(" Toplam Ücret:",price)
                Not=input("          Not: ")
                print("\n")

                secim2=input("Kabul Ediyor Musunuz? E/H ")
                print("\n")

                if(secim2== "E"):
                   print("          Bilgilerinizi Giriniz       ")
                   isim         =input("        Adınız Soyadınız:")
                   Tc_no        =input("            TC Numaranız:")
                   Kredi_No     =input("   Kredi Kartı Numaranız:")
                   Kredi_sifre  =input("    Kredi Kartı Sifreniz:")

                   print("\n") 
                   secim3=input("Kabul Ediyor Musunuz? E/H ")
                   print("\n")
                   if(secim3== "E"):
                        sipariskaydet([[sepet],[price],[Not],[isim],[Tc_no],[Kredi_No],[Kredi_sifre],datetime.datetime.now()])


                else:
                    break

            elif secim == "E" :
                print("         Yeni Pizzanızı Seçin           ")
                break

            else:
                print("Yanlış giriş yaptınız. Bir daha deneyin")
                continue


        
    
if __name__ == "__main__": 
    main()
