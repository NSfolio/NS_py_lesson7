def personal_info(**kwargs):
    return ' '.join(kwargs.values())

print(personal_info(name=input("Enter your name: "), surname=input("Enter your surname: "),
                    birthday=input("Enter your birthday: "), city=input("Enter you city: "),
                    email=input("Enter your email: "),
                    phone_number=input("Enter your phone number: ")))
