Sorteringsalgoritmer.py

nummer = [3, 5, 3, 6, 2, 9, 1, 12]



def sort_nmr(nummer):

    sorted = True 




    while(sorted):

        sorted = False

        for i in range (len(nummer)):

            for j in range(len(nummer)- 1):

                if nummer [j] > nummer[j + 1]:




                    nummer[j], nummer[j + 1] = nummer[j + 1], nummer[j]

                    sorted = True




sort_nmr(nummer)

print(nummer)