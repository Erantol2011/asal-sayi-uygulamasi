while True:
    sayi1 = int(input('Sayi1: '))
    sayi2 = int(input('sayi2: '))
    print('------')
    def asal(x,y):
        for i in range(x,y):
            asal = 0
            notasal = 0

            sayi = i



            for i in range(2, sayi):
                if (sayi % i) == 0:
                    notasal += 1
                    break
                else:
                  asal += 1

            if notasal == 0 and sayi > 1:
                print(sayi, "asal bir sayıdır.")
    
    print('-----'*3)
    asal(sayi1,sayi2)
