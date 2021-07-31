import time

while True:
    a = input("nhap ngay sinh cua ban: ")
    if a == '1/3/2000':
        break;
    else:
   	  print("sai rồi bạn ơi  ")
arrays = ['0','10','20','30','40','50','60','70','80','90','100']
for array in arrays :
	time.sleep(0.5)
	print ("dang xu li ............." + array +"%" );
print("anh cua ban day  ")
file1 = open('duc1.txt', 'r')
file2 = open('duc2.txt', 'r')
file3 = open('duc3.txt', 'r')
Lines = file1.readlines()
Lines2 = file2.readlines();
Lines3 = file3.readlines()
# Strips the newline character
for line in Lines :
	time.sleep(0.05)
	print (line.rstrip() )
for line in Lines2 :
	time.sleep(0.05)
	print (line.rstrip() )
for line in Lines3 :
	time.sleep(0.05)
	print (line.rstrip() )



    