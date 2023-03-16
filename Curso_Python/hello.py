#print("Welcome to the greeter program")
#name = input("Enter your name: ")
#print("Greetings " + name)

# print("Wlecome to my calculator")
# num1= input("Dame el no. 1 a sumar ")
# num2= input("Dame el no. 2 a sumar ")
# print(int(num1) + int(num2))

#b= "esta es una prueba"
#print(b)
#c= b + "cadena1"
#print (c)

#multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
#print(multiline)

#multiline = """Facts about the Moon:
#There is no atmosphere.
#There is no sound."""
#print(multiline)

#heading = "temperatures and facts about the moon"
#heading.title()
#print (heading)

temperatures = """Daylight: 260 F
 Nighttime: -280 F"""
temperatures2 = temperatures .split()
print(temperatures2[0])
print(temperatures2[1]+temperatures2[2])
#print(temperatures2[3])
#print(temperatures2[4]+temperatures2[5])

seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)

# Output: 17


seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Output:
# 17
# 22

result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
# The answer is the same in both cases - 1084

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# Output:
# 215
# 215.3

print(abs(39 - 16))
print(abs(16 - 39))

# Output
# 23
# 23

print(round(14.5))

# Output: 15

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Output
# 13
# 12



