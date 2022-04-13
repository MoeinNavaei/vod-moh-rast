def Migration_casts(sima_casts, khanegi_casts):
    sima_casts.insert(8, 'migrate', 0)
    khanegi_casts.insert(8, 'migrate', 0)
    for i in range(0, len(sima_casts)):
        print(i)
        for j in range(0, len(khanegi_casts)):
            if sima_casts.loc[i, 'casts'] == khanegi_casts.loc[j, 'casts']:
                if sima_casts.loc[i, '1395'] == 1 and sima_casts.loc[i, '1396'] == 0 and sima_casts.loc[i, '1397'] == 0 and \
                   sima_casts.loc[i, '1398'] == 0 and sima_casts.loc[i, '1399'] == 0 and sima_casts.loc[i, '1400'] == 0:
                       if khanegi_casts.loc[j, '1395'] == 0 and (khanegi_casts.loc[j, '1396'] == 1 or \
                       khanegi_casts.loc[j, '1397'] == 1 or khanegi_casts.loc[j, '1398'] == 1 or \
                        khanegi_casts.loc[j, '1399'] == 1 or khanegi_casts.loc[j, '1400'] == 1):
                           sima_casts.loc[i, 'migrate'] = 1
                elif (sima_casts.loc[i, '1395'] == 1 or sima_casts.loc[i, '1396'] == 1) and sima_casts.loc[i, '1397'] == 0 and \
                   sima_casts.loc[i, '1398'] == 0 and sima_casts.loc[i, '1399'] == 0 and sima_casts.loc[i, '1400'] == 0:
                       if khanegi_casts.loc[j, '1395'] == 0 and khanegi_casts.loc[j, '1396'] == 0 and \
                       (khanegi_casts.loc[j, '1397'] == 1 or khanegi_casts.loc[j, '1398'] == 1 or \
                        khanegi_casts.loc[j, '1399'] == 1 or khanegi_casts.loc[j, '1400'] == 1):
                           sima_casts.loc[i, 'migrate'] = 1
                elif (sima_casts.loc[i, '1395'] == 1 or sima_casts.loc[i, '1396'] == 1 or sima_casts.loc[i, '1397'] == 1) and \
                   sima_casts.loc[i, '1398'] == 0 and sima_casts.loc[i, '1399'] == 0 and sima_casts.loc[i, '1400'] == 0:
                       if khanegi_casts.loc[j, '1395'] == 0 and khanegi_casts.loc[j, '1396'] == 0 and \
                       khanegi_casts.loc[j, '1397'] == 0 and (khanegi_casts.loc[j, '1398'] == 1 or \
                        khanegi_casts.loc[j, '1399'] == 1 or khanegi_casts.loc[j, '1400'] == 1):
                           sima_casts.loc[i, 'migrate'] = 1
                elif (sima_casts.loc[i, '1395'] == 1 or sima_casts.loc[i, '1396'] == 1 or sima_casts.loc[i, '1397'] == 1 or \
                   sima_casts.loc[i, '1398'] == 1) and sima_casts.loc[i, '1399'] == 0 and sima_casts.loc[i, '1400'] == 0:
                       if khanegi_casts.loc[j, '1395'] == 0 and khanegi_casts.loc[j, '1396'] == 0 and \
                       khanegi_casts.loc[j, '1397'] == 0 and khanegi_casts.loc[j, '1398'] == 0 and \
                        (khanegi_casts.loc[j, '1399'] == 1 or khanegi_casts.loc[j, '1400'] == 1):
                           sima_casts.loc[i, 'migrate'] = 1
                    
    for i in range(0, len(khanegi_casts)):
        print(i)
        for j in range(0, len(sima_casts)):
            if khanegi_casts.loc[i, 'casts'] == sima_casts.loc[j, 'casts']:
                if khanegi_casts.loc[i, '1395'] == 1 and khanegi_casts.loc[i, '1396'] == 0 and khanegi_casts.loc[i, '1397'] == 0 and \
                   khanegi_casts.loc[i, '1398'] == 0 and khanegi_casts.loc[i, '1399'] == 0 and khanegi_casts.loc[i, '1400'] == 0:
                       if sima_casts.loc[j, '1395'] == 0 and (sima_casts.loc[j, '1396'] == 1 or \
                       sima_casts.loc[j, '1397'] == 1 or sima_casts.loc[j, '1398'] == 1 or \
                        sima_casts.loc[j, '1399'] == 1 or sima_casts.loc[j, '1400'] == 1):
                           khanegi_casts.loc[i, 'migrate'] = 1
                if (khanegi_casts.loc[i, '1395'] == 1 or khanegi_casts.loc[i, '1396'] == 1) and khanegi_casts.loc[i, '1397'] == 0 and \
                   khanegi_casts.loc[i, '1398'] == 0 and khanegi_casts.loc[i, '1399'] == 0 and khanegi_casts.loc[i, '1400'] == 0:
                       if sima_casts.loc[j, '1395'] == 0 and sima_casts.loc[j, '1396'] == 0 and \
                       (sima_casts.loc[j, '1397'] == 1 or sima_casts.loc[j, '1398'] == 1 or \
                        sima_casts.loc[j, '1399'] == 1 or sima_casts.loc[j, '1400'] == 1):
                           sima_casts.loc[i, 'migrate'] = 1
                if (khanegi_casts.loc[i, '1395'] == 1 or khanegi_casts.loc[i, '1396'] == 1 or khanegi_casts.loc[i, '1397'] == 1) and \
                   khanegi_casts.loc[i, '1398'] == 0 and khanegi_casts.loc[i, '1399'] == 0 and khanegi_casts.loc[i, '1400'] == 0:
                       if sima_casts.loc[j, '1395'] == 0 and sima_casts.loc[j, '1396'] == 0 and \
                       sima_casts.loc[j, '1397'] == 0 and (sima_casts.loc[j, '1398'] == 1 or \
                        sima_casts.loc[j, '1399'] == 1 or sima_casts.loc[j, '1400'] == 1):
                           sima_casts.loc[i, 'migrate'] = 1
                if (khanegi_casts.loc[i, '1395'] == 1 or khanegi_casts.loc[i, '1396'] == 1 or khanegi_casts.loc[i, '1397'] == 1 or \
                   khanegi_casts.loc[i, '1398'] == 1) and khanegi_casts.loc[i, '1399'] == 0 and khanegi_casts.loc[i, '1400'] == 0:
                       if sima_casts.loc[j, '1395'] == 0 and sima_casts.loc[j, '1396'] == 0 and \
                       sima_casts.loc[j, '1397'] == 0 and sima_casts.loc[j, '1398'] == 0 and \
                        (sima_casts.loc[j, '1399'] == 1 or sima_casts.loc[j, '1400'] == 1):
                           sima_casts.loc[i, 'migrate'] = 1
    return sima_casts,  khanegi_casts                         
