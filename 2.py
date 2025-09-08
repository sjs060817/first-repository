# 52장 카드 한 덱을 섞고 플레이어 4명에게 5장씩 나눠 주는 코드를 작성하세요.
import random

suits = ['스페이드', '하트', '다이아', '클로버']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [f'{rank} {suit}' for suit in suits for rank in ranks]

random.shuffle(deck)

p1 = deck[0], deck[1], deck[2], deck[3], deck[4]
p2 = deck[5], deck[6], deck[7], deck[8], deck[9]
p3 = deck[10], deck[11], deck[12], deck[13], deck[14]
p4 = deck[15], deck[16], deck[17], deck[18], deck[19]

print(p1)
print(p2)
print(p3)
print(p4)
