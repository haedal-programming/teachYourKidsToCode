# 법적으로 운전 가능한 나이를 검색하여 찾아봅시다
driving_age = eval(input("법적으로 운전이 가능한 나이는 몇 살입니까?"))
# 자신의 나이를 입력합니다
your_age = eval(input("당신은 몇 살입니까? "))
# 조건을 판단하여 올바른 결과를 보여줍니다
if your_age >= driving_age:
    print("당신은 운전을 할 수 있는 나이입니다!")
if your_age < driving_age:
    print("죄송합니다. ", driving_age - your_age, "년을 더 기다려야 운전할 수 있습니다")

# 법적으로 운전 가능한 나이를 입력받자
# 자신의 나이를 입력받자
# 조건을 판단하여 올바른 결과를 보여줍니다
