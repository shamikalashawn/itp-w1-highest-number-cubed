"""This is the entry point of the program."""


def highest_number_cubed(limit):
    answer = 0
    for num in range(limit):
        if num**3 > limit:
            answer = num - 1
            return answer
            
print(highest_number_cubed(30))