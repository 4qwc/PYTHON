
product = ['Apple', 'Banaan', 'Mango']

print(len(product)) #  len นับจำนวน

product.append('Durian') #เพิ่มของ
print(product)

product.append('Coconut')
print(product)

print(product[0]) # แสดงผล index 0

print('index:',product[-1]) # แสดงผล index 0

del product[1] # ลบ index 1
print(product)

product[2] = 'กล้วย' # เพิ่มเข้า index 2
print(product)

product.insert(1, 'มะพร้าว') # แทรกเข้า index 1
print(product)
print('-----------------------')


# การใช้ for รันสิ่งที่อยู่ใน list
for pd in product:
	print(pd)


for i in range(10):
	print('จำนวน:',i)


for i in [20, 30, 100]:
	print(i)

print('-----------------------')

### แบบ tuple คือแก้ไขข้อมูลใน list ไม่ได้
### ใช้ () ตัวอย่าง
position = (500,900)
print('position = ', position[0])
print('position = ', position[1])

# ลองเพิ่มค่าเข้าใน list
#position.append(100)
#AttributeError: 'tuple' object has no attribute 'append'
# ไม้สามารถเพิ่มได้ เป็นข้อมูลที่ไม่ให้แก้ไข
x,y = (100,200)
print(x,y)

print('-----------------------')

# ดิกชันนารี

product = {'มะม่วง':'ป้าสมศรี', 'ทุเรียน':'สวนจันทบุรี', 'ส้ม':'สวนเชียงราย',}
print(product['ทุเรียน'])
print(product['ส้ม'])

# การซ้อน list
product = {'มะม่วง':['ป้าสมศรี','ป้าปวีณา'], 'ทุเรียน':'สวนจันทบุรี', 'ส้ม':'สวนเชียงราย',}
print(product['มะม่วง'])
print(product['มะม่วง'][1])# แสดงผล index 1



print('-----------------------')

# การใช้ key ซ้อน key
print('การใช้ key ซ้อน key') 

product = {'มะม่วง':['ป้าสมศรี','ป้าปวีณา'], 'ทุเรียน':'สวนจันทบุรี', 'ส้ม':{'99':'สวนเชียงราย', '88':'เชียงใหม่'}}
print(product['ส้ม']['88'])

print(product['ส้ม']['99'])


print('-----------------------')


