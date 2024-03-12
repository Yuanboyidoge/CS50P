import validators


# email = input("What's your email? ").strip()
if validators.email(input("What's your email? ").strip())==1:
    print("Valid")
else:
    print("Invalid")