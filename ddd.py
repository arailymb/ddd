def check_ratio(num):
    digits = [int(d) for d in str(num)]
    if digits[0] + digits[3] == digits[1] - digits[2]:
        return "yes"
    else:
        return "no"

def check_access(age):
    if age >= 18:
        return "Access is allowed"
    else:
        return "Access denied"

def is_arithmetic_progression(a, b, c):
    if b - a == c - b:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    try:
        # Task 1: Ratio
        number = int(input("Enter a four-digit number for the Ratio task: "))
        if 1000 <= number <= 9999:
            print(check_ratio(number))
        else:
            raise ValueError("Not a four-digit number")
        
        # Task 2: Roskomnadzor
        user_age = int(input("Enter your age for the Roskomnadzor task: "))
        print(check_access(user_age))
        
        # Task 3: Arithmetic progression
        print("Enter three numbers for the Arithmetic progression task:")
        num1 = int(input())
        num2 = int(input())
        num3 = int(input())
        print(is_arithmetic_progression(num1, num2, num3))
    
    except ValueError as e:
        print(f"Error: {e}")
