class Day:
    def maopao(a):
        for i in range(len(a)-1):
            for j in range (len(a)-1-i):
                if a[j] > a[j+1]:
                    b = a[j]
                    a[j] = a[j+1]
                    a[j+1]=b

        return a
if __name__ == '__main__':
    c = [18,12,16,44,22]
    print(Day.maopao(c))


