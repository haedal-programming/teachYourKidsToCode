import random
# 카드 패입니다
faces = ["two","three","four","five","six","seven","eight","nine",
         "ten","jack","queen","king","ace"]
# 나와 상대방의 패를 뽑습니다
my_face = random.choice(faces)
your_face = random.choice(faces)
# 나와 상대방의 패를 이야기합니다
print("내 카드는 ", my_face)
print("당신 카드는 ", your_face)
# 승무패를 결정합니다
if faces.index(my_face) > faces.index(your_face):
    print("내가 이겼어요!")
elif faces.index(my_face) < faces.index(your_face):
    print("당신이 이겼어요!")
else:
    print("비겼어요!")

# # 카드 패입니다
# faces = ["two","three","four","five","six","seven","eight","nine","ten",
#          "jack","queen","king","ace"]
# # 나와 상대방의 패를 뽑습니다
# # 나와 상대방의 패를 이야기합니다
# # 승무패를 결정합니다
