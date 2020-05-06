text = open('history.txt')
text = text.read()

count = 0 #количество историй
count1 = 0
for s in text:
    if text[count1] == '=':
        count += 1
        count1 += 1
    else :
        count1 += 1
ogo = False
def position(fd):
    if fd == 1:
        ogo = True
    elif fd == 2:
        ogo = False

now = 0
text = text.split('=')
