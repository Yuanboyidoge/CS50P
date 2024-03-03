# Prompts the user for a level, 
# . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
#  digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
import random


def main():
   l=get_level()
   times=0
   score=0
   while 1:
        try:
            a=generate_integer(l)
            b=generate_integer(l)
            ans=a+b
            rep=int(input(f"{a} + {b} = "))
            if rep==ans:
                score+=1
            else:
                raise ValueError
            times+=1
            if times==9:
                print("Score:",score)
                break
        except ValueError:
            print("EEE")
            tt=1
            while 1:
                rep1=int(input(f"{a} + {b} = "))
                if rep1 == ans:
                    score+=1
                    break
                else:
                    print("EEE")
                tt += 1
                if tt==3:
                    print(f"{a} + {b} =",ans)
                    break

def get_level():
    while 1:
        try:
            level=int(input("Level:"))
            if level == 1 or level==2 or level==3:
                break
            else:
                raise ValueError
        except ValueError:
            pass

    return level

def generate_integer(level):
    if level==1:
        n=random.randint(0,9)
    elif level==2:
        n=random.randint(10,99)
    elif level==3:
        n=random.randint(100,999)
    else:
        raise ValueError
    return n
    


if __name__ == "__main__":
    main()