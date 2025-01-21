import json

class Bankomat:
    def __init__(self, balans=0):
        self.balans = balans
        self.password = "1234"
        self.sms_xabar = False  # SMS xabar ulash
        self.til = self.tilni_tanlash()
        self.messages = self.load_messages()

    def load_messages(self):
        with open("messeges.json", "r", encoding="utf-8") as file:
            return json.load(file)


    def tilni_tanlash(self):
        print("Tilni tanlang:")
        print("1. English")
        print("2. Русский язык")
        print("3. O'zbek tili")
        n = int(input("Tilni tanlang (1/2/3): "))
        if n in [1, 2, 3]:
            return n
        else:
            print("Noto'g'ri tanlov, iltimos qaytadan urinib ko'ring.")
            return self.tilni_tanlash()

    def password_check(self):
        for i in range(3):
            parol = input(self.get_message("Enter password: "))
            if parol == self.password:
                print(self.get_message("Correct!"))
                return True
            else:
                print(self.get_message("Invalid password."))
        print(self.get_message("The password is incorrect!"))
        return False

    def menu(self):
        if self.til == 1:
            print("\n1. Check balance")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Change password")
            print("5. Exit")
            print("6. Enable/Disable SMS Notification")
            print("7. Pay for Mobile Services")
            print("8. Pay for Credit")
            print("9. Pay for Utilities")
        elif self.til == 2:
            print("\n1. Проверка баланса")
            print("2. Добавить деньги")
            print("3. Снять деньги")
            print("4. Изменить пароль")
            print("5. Выход")
            print("6. Включить/выключить SMS уведомления")
            print("7. Оплатить мобильные услуги")
            print("8. Оплатить кредит")
            print("9. Оплатить коммунальные услуги")
        else:
            print("\n1. Balansni tekshirish")
            print("2. Pul qo'shish")
            print("3. Pul yechish")
            print("4. Parolni o'zgartirish")
            print("5. Chiqish")
            print("6. SMS Xabar ulash yoki o'chirish")
            print("7. Mobil aloqa uchun to'lov")
            print("8. Kredit to'lovi")
            print("9. Kommunal to'lov")

    def handle_choice(self, choice):
        if choice == '1':
            self.balansni_tekshirish()
        elif choice == '2':
            s = float(input(self.get_message("Enter amount to deposit: ")))
            self.pul_qoshish(s)
        elif choice == '3':
            s = float(input(self.get_message("Enter amount to withdraw: ")))
            self.pul_yechish(s)
        elif choice == '4':
            self.change_password()
        elif choice == '5':
            print(self.get_message("Program ended."))
            return False
        elif choice == '6':
            if self.sms_xabar:
                self.sms_xabar_ochirish()
            else:
                self.sms_xabar_ulash()
        elif choice == '7':
            self.mobil_aloqa_tolovi()
        elif choice == '8':
            self.kredit_tolovi()
        elif choice == '9':
            self.kommunal_tolov()
        else:
            print(self.get_message("Invalid choice, please try again."))
        return True
    def get_message(self, message):
        if message in self.messages:
            return self.messages[message][self.til - 1]
        else:
            return message 

    def balansni_tekshirish(self):
        print(self.get_message("Your balance is: ") + f"{self.balans} so'm")

    def pul_qoshish(self, s):
        if s > 0:
            self.balans += s
            print(self.get_message("Amount added: ") + f"{s} so'm")
        else:
            print(self.get_message("Insufficient funds or invalid amount."))

    def pul_yechish(self, s):
        if 0 < s <= self.balans:
            self.balans -= s
            print(self.get_message("Amount withdrawn: ") + f"{s} so'm")
        else:
            print(self.get_message("Insufficient funds or invalid amount."))

    def change_password(self):
        eski_parol = input(self.get_message("Enter old password: "))
        if eski_parol == self.password:
            yangi_parol = input(self.get_message("Enter new password: "))
            self.password = yangi_parol
            print(self.get_message("Password successfully changed."))
        else:
            print(self.get_message("Invalid password."))

    def sms_xabar_ulash(self):
        self.sms_xabar = True
        print(self.get_message("SMS notification enabled."))

    def sms_xabar_ochirish(self):
        self.sms_xabar = False
        print(self.get_message("SMS notification disabled."))

    def mobil_aloqa_tolovi(self):
        print(self.get_message("Choose mobile operator: "))
        operators = ["Uzmobayl", "Beeline", "Usell", "UMS", "Perfectum"]
        for i, operator in enumerate(operators, 1):
            print(f"{i}. {operator}")
        tanlov = int(input(self.get_message("Enter choice: ")))
        if 1 <= tanlov <= len(operators):
            summa = float(input(self.get_message("Enter amount to pay: ")))
            if 0 < summa <= self.balans:
                self.balans -= summa
                print(self.get_message("Amount withdrawn: ") + f"{summa} so'm")
            else:
                print(self.get_message("Insufficient funds or invalid amount."))
        else:
            print(self.get_message("Invalid choice."))

    def kredit_tolovi(self):
        kredit_raqami = input(self.get_message("Enter credit number: "))
        summa = float(input(self.get_message("Enter amount to pay: ")))
        if 0 < summa <= self.balans:
            self.balans -= summa
            print(self.get_message("Amount withdrawn: ") + f"{summa} so'm")
        else:
            print(self.get_message("Insufficient funds or invalid amount."))

    def kommunal_tolov(self):
        print(self.get_message("Choose utility service: "))
        services = ["Elektr energiyasi", "Gaz", "Suv", "Jarimalar"]
        for i, service in enumerate(services, 1):
            print(f"{i}. {service}")
        tanlov = int(input(self.get_message("Enter choice: ")))
        if 1 <= tanlov <= len(services):
            summa = float(input(self.get_message("Enter amount to pay: ")))
            if 0 < summa <= self.balans:
                self.balans -= summa
                print(self.get_message("Amount withdrawn: ") + f"{summa} so'm")
            else:
                print(self.get_message("Insufficient funds or invalid amount."))
        else:
            print(self.get_message("Invalid choice."))

    def run(self):
        while True:
            self.menu()
            tanlov = input(self.get_message("Enter your choice: "))
            if not self.handle_choice(tanlov):
                break

def main():
    bankomat = Bankomat()
    if bankomat.password_check():
        bankomat.run()

if __name__ == "__main__":
    main()
