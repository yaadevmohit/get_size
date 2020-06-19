
import pandas as pd
from statistics import mean
import os.path

brandName = [] #0
nameSpecific = []#1
typeTable = []
garmentType = []
brandSize = []
bodyPart = []
bustMin = []
bustMax = []
waistBottomMin = []
waistBottomMax = []
waistMin = []
waistMax = []
hipsMin = []
hipsMax = []
bustMin2 = []
bustMax2 = []
waistBottomMin2 = []
waistBottomMax2 = []
waistMin2 = []
waistMax2 = []
hipsMin2 = []
hipsMax2 = []
email = []
allBustMin = []
allBustMin2 = []
allBustMax = []
allBustMax2 = []
allWaistMin = []
allWaistMin2 = []
allWaistMax = []
allWaistMax2 = []
allBottomWaistMin = []
allBottomWaistMin2 = []
allBottomWaistMax = []
allBottomWaistMax2 = []
allHipsMin = []
allHipsMin2 = []
allHipsMax = []
allHipsMax2 = []

if os.path.exists('availablestores.csv'):
    print("file here")
else:
    print("file not here")
userFile = pd.read_csv('normalized_profiles.csv')
print(userFile.shape)
brandFile = pd.read_csv('storesfileInterval.csv')
print(brandFile.shape)


def get_user_sizeValues(store1, store2, upperSize1, bottomSize1, upperSize2, bottomSize2):
    for l in brandFile.itertuples():
        if store1 == getattr(l,('store_specification')).upper():
            if upperSize1 != 'missingdata': # if there's a value for a uppersize
                topSizes = upperSize1.split(';')
                for size in topSizes:
                    if size.upper() in getattr(l,('store_size')).upper():
                        if getattr(l,('type')) == 'BUST':
                            bustMin.append(getattr(l,('Min')))
                            bustMax.append(getattr(l,('Max')))
                        if getattr(l,('type')) == 'WAIST':
                            waistMin.append(getattr(l,('Min')))
                            waistMax.append(getattr(l,('Max')))
                        # else:
                        #     print('find this size: ' + size)
                        #     print('store is:' + store1)
                        #     bustMin = input("Bust min: ")
                        #     bustMax = input("Bust max: ")
                        #     waistMin = input("Waist min: ")
                        #     waistMax = input("Waist max: ")
            if not upperSize1:
                print('no top size')

            if bottomSize1 != 'missingdata':
                bottomSizes = bottomSize1.split(';')
                for size in bottomSizes:
                    if size.upper() in getattr(l,('store_size')).upper():
                        if getattr(l,('type')) == 'WAIST':
                            waistBottomMin.append(getattr(l,('Min')))
                            waistBottomMax.append(getattr(l,('Max')))
                        if getattr(l,('type')) == 'HIP':
                            hipsMin.append(getattr(l,('Min')))
                            hipsMax.append(getattr(l,('Max')))
            if not bottomSize1:
                print('no bottom size')




        if store2 == getattr(l,('store_specification')).upper():
            if upperSize2 != 'missingdata':
                topSizes = upperSize2.split(';')
                for size in topSizes:
                    if size.upper() in getattr(l,('store_size')).upper():
                        if getattr(l,('type')) == 'BUST':
                            bustMin2.append(getattr(l,('Min')))
                            bustMax2.append(getattr(l,('Max')))
                        if getattr(l,('type')) == 'WAIST':
                            waistMin2.append(getattr(l,('Min')))
                            waistMax2.append(getattr(l,('Max')))


            if not upperSize2:
                print('no top size2')

            if bottomSize2 != 'missingdata':
                bottomSizes = bottomSize2.split(';')
                for size in bottomSizes:
                    if size.upper() in getattr(l,('store_size')).upper():
                        if getattr(l,('type')) == 'WAIST':
                            waistBottomMin2.append(getattr(l,('Min')))
                            waistBottomMax2.append(getattr(l,('Max')))
                        if getattr(l,('type')) == 'HIP':
                            hipsMin2.append(getattr(l,('Min')))
                            hipsMax2.append(getattr(l,('Max')))
                    # else:
                    #     print('find this size: ' + size)
                    #     print('store is:' + store2)
                    #     waistBottomMin2 = input("Waist Bottom min: ")
                    #     waistBottomMax2 = input("Waist Bottom max: ")
                    #     hipsMin2 = input("Hips min: ")
                    #     hipsMax2 = input("Hips max: ")
            if not bottomSize2:
                print('no bottom size2')


    userBustMin = bustMin
    if len(bustMin) != 0:
        userBustMin = mean(bustMin)
    userWaistMin = waistMin
    if len(waistMin) != 0:
        userWaistMin = mean(waistMin)
    userBottomWaistMin = waistBottomMin
    if len(waistBottomMin) != 0:
        userBottomWaistMin = mean(waistBottomMin)
    userHipsMin = hipsMin
    if len(hipsMin) != 0:
        userHipsMin = mean(hipsMin)

    userBustMax = bustMax
    if len(bustMax) != 0:
        userBustMax = mean(bustMax)
    userWaistMax = waistMax
    if len(waistMax) != 0:
        userWaistMax = mean(waistMax)
    userBottomWaistMax = waistBottomMax
    if len(waistBottomMax) != 0:
        userBottomWaistMax = mean(waistBottomMax)
    userHipsMax = hipsMax
    if len(hipsMax) != 0:
        userHipsMax = mean(hipsMax)

    userBustMin2 = bustMin2
    if len(bustMin2) != 0:
        userBustMin2 = mean(bustMin2)
    userWaistMin2 = waistMin2
    if len(waistMin2) != 0:
        userWaistMin2 = mean(waistMin2)
    userBottomWaistMin2 = waistBottomMin2
    if len(waistBottomMin2) != 0:
        userBottomWaistMin2 = mean(waistBottomMin2)
    userHipsMin2 = hipsMin2
    if len(hipsMin2) != 0:
        userHipsMin2 = mean(hipsMin2)

    userBustMax2 = bustMax2
    if len(bustMax2) != 0:
        userBustMax2 = mean(bustMax2)
    userWaistMax2 = waistMax2
    if len(waistMax2) != 0:
        userWaistMax2 = mean(waistMax2)
    userBottomWaistMax2 = waistBottomMax2
    if len(waistBottomMax2) != 0:
        userBottomWaistMax2 = mean(waistBottomMax2)
    userHipsMax2 = hipsMax2
    if len(hipsMax2) != 0:
        userHipsMax2 = mean(hipsMax2)

    allBustMin.append(userBustMin)
    allBustMin2.append(userBustMin2)
    allBustMax.append(userBustMax)
    allBustMax2.append(userBustMax2)

    allWaistMin.append(userWaistMin)
    allWaistMin2.append(userWaistMin2)
    allWaistMax.append(userWaistMax)
    allWaistMax2.append(userWaistMax2)

    allBottomWaistMin.append(userBottomWaistMin)
    allBottomWaistMin2.append(userBottomWaistMin2)
    allBottomWaistMax.append(userBottomWaistMax)
    allBottomWaistMax2.append(userBottomWaistMax2)

    allHipsMin.append(userHipsMin)
    allHipsMin2.append(userHipsMin2)
    allHipsMax.append(userHipsMax)
    allHipsMax2.append(userHipsMax2)

for j in userFile.itertuples(): 
    email.append(getattr(j,'Email'))
    upperSize1 = getattr(j,('topsize1'))
    bottomSize1 = getattr(j,'bottomsize1')
    upperSize2 = getattr(j,('topsize2'))
    bottomSize2 = getattr(j,'bottomsize2')
    store1 = getattr(j,('store1'))
    store2 = getattr(j,('store2'))

    #
    get_user_sizeValues(store1, store2, upperSize1, bottomSize1, upperSize2, bottomSize2)

    #clear all the arrays associated with each user
    bustMin = []
    bustMax = []
    waistBottomMin = []
    waistBottomMax = []
    waistMin = []
    waistMax = []
    hipsMin = []
    hipsMax = []
    bustMin2 = []
    bustMax2 = []
    waistBottomMin2 = []
    waistBottomMax2 = []
    waistMin2 = []
    waistMax2 = []
    hipsMin2 = []
    hipsMax2 = []

pd.DataFrame(list(zip(email, allBustMin, allBustMax, allBustMin2, allBustMax2, allWaistMin, allWaistMax, allBottomWaistMin, allBottomWaistMin2, allBottomWaistMax, allBottomWaistMax2, allHipsMin, allHipsMin2, allHipsMax, allHipsMax2)),
             columns=['email', 'bust min', 'bust max', 'bust min 2', 'bust max 2', 'waist min', 'waist max', 'botwaist min', 'botwaist min 2', 'bottom waist max', 'bottom waist max 2', 'hips min', 'hips min 2', 'hips max', 'hips max 2']).to_csv(
    "export_sizing.csv")
