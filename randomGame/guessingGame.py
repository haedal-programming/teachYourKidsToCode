import random
the_number = random.randint(1,10)
guess = int(input("1부터 10사이의 숫자를 맞춰보세요: "))
while guess != the_number:
    if guess > the_number:
        print(guess, "너무 높습니다. 다시 시도해주세요.")
    if guess < the_number:
        print(guess, "너무 낮습니다. 다시 시도해주세요.")
    guess = int(input("다시 맞춰보세요: "))
print(guess, "맞습니다! 당신이 이겼습니다!")

# 1에서 10 사이 임의의 수를 뽑고
# 사용자가 맞추도록 반복해 입력받자
