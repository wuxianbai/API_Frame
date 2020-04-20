import random

class UserVars():

    # 生成orderNo随机数
    def createRandomNum(self, length):
        random_str = []
        for i in range(length):
            random_str.append(str(random.randint(1, 9)))
        return ''.join(random_str)

    def createRandomNums(self, length, a):
        random_str = []
        for i in range(length):
            random_str.append(str(random.randint(1, 9)))
        return ''.join(random_str)