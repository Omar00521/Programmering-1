

siffror= [3, 5, 3, 6, 1, 9, 2, 12]



def sort_siffror(siffror):

    sorted = True 




    while(sorted):

        sorted = False

        for o in range (len(siffror)):

            for h  in range(len(siffror)- 1):

                if siffror [h] > siffror[h + 1]:




                    siffror[h], siffror[h + 1] = siffror[h + 1], siffror[h]

                    sorted = True




sort_siffror(siffror)

print(siffror)