# 피자 주문하며 간단한 수학 문제 풀어보자

# 주석을 보고 학생이 코드를 짜게 해보고
# 10~20분 정도 고민을 하게한 후 설명하며 가르쳐봅시다.

# 주문자에게 몇 판의 피자를 주문할 것인지 묻습니다.
# eval()을 이용해 input으로 들어오는 문자열을 정수로 바꿉니다.
numbers_of_pizzas = eval(input("피자 몇 판을 주문하겠습니까?: "))

# 피자 한 판당 가격을 입력합니다.
cost_per_pizza = eval(input("피자 한 판은 얼마입니까?: "))

# 주문한 전체 피자의 가격을 계산합니다.
subtotal = numbers_of_pizzas * cost_per_pizza

# 전체 피자 가격의 8%를 세금으로 계산합니다.
tax_rate = 0.08 # 8%를 0.08이라는 숫자로 저장합니다.
sales_tax = subtotal * tax_rate

# 전체 피자 가격과 세금을 더해서 최종 금액을 계산합니다.
total = subtotal + sales_tax

# 주문자에게 세금을 포함한 최종 금액을 보여줍니다.
print("최종 가격은", total)
print("이 가격에는 피자 가격", subtotal,"과 함께")
print("세금",sales_tax, "이 포함돼 있습니다.")
