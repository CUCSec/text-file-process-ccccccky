
n = 0
with open('C:/Users/陈可悦/Desktop/文件/Python/in anjing class/week 10/text-file-process-ccccccky/text-file-process/log_files/201811113019.log', encoding = 'utf8') as f:
    for line in f :
        line = line.split('：' , 3)
        # print(line[2])
        if( line[2] == '201811113019, 时间' ):
            n += 1
print(n)

