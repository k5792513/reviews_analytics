data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: # %是餘數
			print(len(data))
print('終於印完了！總共有', len(data), '筆資料')

sun_len = 0
for line in data:
	sun_len = sun_len + len(line)
print('留言的平均長度是', sun_len/1000000)
