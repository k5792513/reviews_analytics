data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 10000 == 0: # %是餘數
			print(len(data))
print('終於印完了！總共有', len(data), '筆資料')


sun_len = 0
for line in data:
	sun_len = sun_len + len(line)
print('留言的平均長度是', sun_len/1000000)


x = 0
for line in data:
	if len(line) < 100:
		x += 1
print('一共有', x, '則留言長度小於100')


new = [] #製造一個新清單，即是new
for line in data:
	if len(line) < 100:
		new.append(line)
print('一共有', len(new), '則留言長度小於100')


x = 0
for line in data:
	if 'good' in line:
		x += 1
print('一共有', x, '則留言提到good')


good = []
for line in data:
	if 'good' in line:
		good.append(line)
print('一共有', len(good), '則留言提到good')


#快寫法
good = [line for line in data if 'good' in line]
print(good)

good = [1 for line in data if 'good' in line]
print(good)

good = ['good' in line for line in data]
print(good)


#文字計數
wc = {} # wc = word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else: 
			wc[word] = 1

for word in wc:
	if wc[word] > 200:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請輸入想查詢單字： ')
	if word == 'q':
		break
	elif word in wc:
		print(word, '這個字出現過', wc[word], '次')
	else:
		print('沒有', word, '這個字')
print('感謝您使用本查詢功能')