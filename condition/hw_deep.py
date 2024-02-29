answer=input("what's is the answer to the great question of life,the universe,and everything? ").strip().lower()
match answer:
    case "42"|"forty two"|"forty-two"|42:
        print("Yes")
    case _:
        print("No")
