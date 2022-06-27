#切片
players = ['abc', 'bcd', 'cde', 'def', 'efg']
print(players[1:3])

print(players[3:4])

print(players[:3])

print([players[2:]])

print(players[-2:])

print(players[0::2])

#遍历切片
print('===============')
for player in players[:3]:
    print(player.title())

#复制列表
players1 = players[:]
print(players1)
#验证是复制
players.append('aaa')
print(players)
print(players1)

#非切片
players3 = players
players.append('bbb')
print(players)
print(players3)

















