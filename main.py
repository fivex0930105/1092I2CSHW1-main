''' main '''
# 使用自建的套件 myMath 來計算使用者輸入的五個數的平均值
from myMath import myStatistics
N = []
N.append(int(input("輸入第一個數:")))
N.append(int(input("輸入第二個數:")))
N.append(int(input("輸入第三個數:")))
N.append(int(input("輸入第四個數:")))
N.append(int(input("輸入第五個數:")))

print("平均值為:",myStatistics.myMean(N))
