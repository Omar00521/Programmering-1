

siffror= [13, 69, 41, 30, -55, 11, 50, 60, 100]



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