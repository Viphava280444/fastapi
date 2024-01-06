from thaistock import SET

#สร้างตัวแปร stock (object)
stock = SET()

#เช็คราคา ณ ปัจจุบัน (ใช้ขณะตลาดเปิดได้)
current = stock.current('TEAMG',show=True,header=True)