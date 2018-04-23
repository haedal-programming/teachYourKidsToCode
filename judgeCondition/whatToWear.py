rainy = input("날씨는 어때? 비가 오니? (y/n)").lower()
cold = input("밖이 추워? (y/n)").lower()
if(rainy == 'y' and cold == 'y'):         # 비오고 춥다
    print("비옷을 입는 게 좋아.")
elif(rainy == 'y' and cold != 'y'):       # 비가 오지만 따뜻하다
    print("우산을 가져가도록 해.")
elif(rainy != 'y' and cold == 'y'):       # 맑지만 춥다
    print("재킷을 입어. 밖이 추워!")
elif(rainy != 'y' and cold != 'y'):       # 따뜻하고 맑다
    print("원하는 옷을 입어. 날씨가 너무 좋아!")


#
