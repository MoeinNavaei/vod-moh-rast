def Migration_director(sima_director, khanegi_director):
    sima_director.insert(8, 'migrate', 0)
    khanegi_director.insert(8, 'migrate', 0)
    for i in range(0, len(sima_director)):
        print(i)
        for j in range(0, len(khanegi_director)):
            if sima_director.loc[i, 'director'] == khanegi_director.loc[j, 'director']:
                if sima_director.loc[i, '1395'] == 1 and sima_director.loc[i, '1396'] == 0 and sima_director.loc[i, '1397'] == 0 and \
                   sima_director.loc[i, '1398'] == 0 and sima_director.loc[i, '1399'] == 0 and sima_director.loc[i, '1400'] == 0:
                       if khanegi_director.loc[j, '1395'] == 0 and (khanegi_director.loc[j, '1396'] == 1 or \
                       khanegi_director.loc[j, '1397'] == 1 or khanegi_director.loc[j, '1398'] == 1 or \
                        khanegi_director.loc[j, '1399'] == 1 or khanegi_director.loc[j, '1400'] == 1):
                           sima_director.loc[i, 'migrate'] = 1
                elif (sima_director.loc[i, '1395'] == 1 or sima_director.loc[i, '1396'] == 1) and sima_director.loc[i, '1397'] == 0 and \
                   sima_director.loc[i, '1398'] == 0 and sima_director.loc[i, '1399'] == 0 and sima_director.loc[i, '1400'] == 0:
                       if khanegi_director.loc[j, '1395'] == 0 and khanegi_director.loc[j, '1396'] == 0 and \
                       (khanegi_director.loc[j, '1397'] == 1 or khanegi_director.loc[j, '1398'] == 1 or \
                        khanegi_director.loc[j, '1399'] == 1 or khanegi_director.loc[j, '1400'] == 1):
                           sima_director.loc[i, 'migrate'] = 1
                elif (sima_director.loc[i, '1395'] == 1 or sima_director.loc[i, '1396'] == 1 or sima_director.loc[i, '1397'] == 1) and \
                   sima_director.loc[i, '1398'] == 0 and sima_director.loc[i, '1399'] == 0 and sima_director.loc[i, '1400'] == 0:
                       if khanegi_director.loc[j, '1395'] == 0 and khanegi_director.loc[j, '1396'] == 0 and \
                       khanegi_director.loc[j, '1397'] == 0 and (khanegi_director.loc[j, '1398'] == 1 or \
                        khanegi_director.loc[j, '1399'] == 1 or khanegi_director.loc[j, '1400'] == 1):
                           sima_director.loc[i, 'migrate'] = 1
                elif (sima_director.loc[i, '1395'] == 1 or sima_director.loc[i, '1396'] == 1 or sima_director.loc[i, '1397'] == 1 or \
                   sima_director.loc[i, '1398'] == 1) and sima_director.loc[i, '1399'] == 0 and sima_director.loc[i, '1400'] == 0:
                       if khanegi_director.loc[j, '1395'] == 0 and khanegi_director.loc[j, '1396'] == 0 and \
                       khanegi_director.loc[j, '1397'] == 0 and khanegi_director.loc[j, '1398'] == 0 and \
                        (khanegi_director.loc[j, '1399'] == 1 or khanegi_director.loc[j, '1400'] == 1):
                           sima_director.loc[i, 'migrate'] = 1
                    
    for i in range(0, len(khanegi_director)):
        print(i)
        for j in range(0, len(sima_director)):
            if khanegi_director.loc[i, 'director'] == sima_director.loc[j, 'director']:
                if khanegi_director.loc[i, '1395'] == 1 and khanegi_director.loc[i, '1396'] == 0 and khanegi_director.loc[i, '1397'] == 0 and \
                   khanegi_director.loc[i, '1398'] == 0 and khanegi_director.loc[i, '1399'] == 0 and khanegi_director.loc[i, '1400'] == 0:
                       if sima_director.loc[j, '1395'] == 0 and (sima_director.loc[j, '1396'] == 1 or \
                       sima_director.loc[j, '1397'] == 1 or sima_director.loc[j, '1398'] == 1 or \
                        sima_director.loc[j, '1399'] == 1 or sima_director.loc[j, '1400'] == 1):
                           khanegi_director.loc[i, 'migrate'] = 1
                if (khanegi_director.loc[i, '1395'] == 1 or khanegi_director.loc[i, '1396'] == 1) and khanegi_director.loc[i, '1397'] == 0 and \
                   khanegi_director.loc[i, '1398'] == 0 and khanegi_director.loc[i, '1399'] == 0 and khanegi_director.loc[i, '1400'] == 0:
                       if sima_director.loc[j, '1395'] == 0 and sima_director.loc[j, '1396'] == 0 and \
                       (sima_director.loc[j, '1397'] == 1 or sima_director.loc[j, '1398'] == 1 or \
                        sima_director.loc[j, '1399'] == 1 or sima_director.loc[j, '1400'] == 1):
                           sima_director.loc[i, 'migrate'] = 1
                if (khanegi_director.loc[i, '1395'] == 1 or khanegi_director.loc[i, '1396'] == 1 or khanegi_director.loc[i, '1397'] == 1) and \
                   khanegi_director.loc[i, '1398'] == 0 and khanegi_director.loc[i, '1399'] == 0 and khanegi_director.loc[i, '1400'] == 0:
                       if sima_director.loc[j, '1395'] == 0 and sima_director.loc[j, '1396'] == 0 and \
                       sima_director.loc[j, '1397'] == 0 and (sima_director.loc[j, '1398'] == 1 or \
                        sima_director.loc[j, '1399'] == 1 or sima_director.loc[j, '1400'] == 1):
                           sima_director.loc[i, 'migrate'] = 1
                if (khanegi_director.loc[i, '1395'] == 1 or khanegi_director.loc[i, '1396'] == 1 or khanegi_director.loc[i, '1397'] == 1 or \
                   khanegi_director.loc[i, '1398'] == 1) and khanegi_director.loc[i, '1399'] == 0 and khanegi_director.loc[i, '1400'] == 0:
                       if sima_director.loc[j, '1395'] == 0 and sima_director.loc[j, '1396'] == 0 and \
                       sima_director.loc[j, '1397'] == 0 and sima_director.loc[j, '1398'] == 0 and \
                        (sima_director.loc[j, '1399'] == 1 or sima_director.loc[j, '1400'] == 1):
                           sima_director.loc[i, 'migrate'] = 1
    return sima_director,  khanegi_director                         
