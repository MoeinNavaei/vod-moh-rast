def Migration_cameraman(sima_cameraman, khanegi_cameraman):
    sima_cameraman.insert(8, 'migrate', 0)
    khanegi_cameraman.insert(8, 'migrate', 0)
    for i in range(0, len(sima_cameraman)):
        print(i)
        for j in range(0, len(khanegi_cameraman)):
            if sima_cameraman.loc[i, 'cameraman'] == khanegi_cameraman.loc[j, 'cameraman']:
                if sima_cameraman.loc[i, '1395'] == 1 and sima_cameraman.loc[i, '1396'] == 0 and sima_cameraman.loc[i, '1397'] == 0 and \
                   sima_cameraman.loc[i, '1398'] == 0 and sima_cameraman.loc[i, '1399'] == 0 and sima_cameraman.loc[i, '1400'] == 0:
                       if khanegi_cameraman.loc[j, '1395'] == 0 and (khanegi_cameraman.loc[j, '1396'] == 1 or \
                       khanegi_cameraman.loc[j, '1397'] == 1 or khanegi_cameraman.loc[j, '1398'] == 1 or \
                        khanegi_cameraman.loc[j, '1399'] == 1 or khanegi_cameraman.loc[j, '1400'] == 1):
                           sima_cameraman.loc[i, 'migrate'] = 1
                elif (sima_cameraman.loc[i, '1395'] == 1 or sima_cameraman.loc[i, '1396'] == 1) and sima_cameraman.loc[i, '1397'] == 0 and \
                   sima_cameraman.loc[i, '1398'] == 0 and sima_cameraman.loc[i, '1399'] == 0 and sima_cameraman.loc[i, '1400'] == 0:
                       if khanegi_cameraman.loc[j, '1395'] == 0 and khanegi_cameraman.loc[j, '1396'] == 0 and \
                       (khanegi_cameraman.loc[j, '1397'] == 1 or khanegi_cameraman.loc[j, '1398'] == 1 or \
                        khanegi_cameraman.loc[j, '1399'] == 1 or khanegi_cameraman.loc[j, '1400'] == 1):
                           sima_cameraman.loc[i, 'migrate'] = 1
                elif (sima_cameraman.loc[i, '1395'] == 1 or sima_cameraman.loc[i, '1396'] == 1 or sima_cameraman.loc[i, '1397'] == 1) and \
                   sima_cameraman.loc[i, '1398'] == 0 and sima_cameraman.loc[i, '1399'] == 0 and sima_cameraman.loc[i, '1400'] == 0:
                       if khanegi_cameraman.loc[j, '1395'] == 0 and khanegi_cameraman.loc[j, '1396'] == 0 and \
                       khanegi_cameraman.loc[j, '1397'] == 0 and (khanegi_cameraman.loc[j, '1398'] == 1 or \
                        khanegi_cameraman.loc[j, '1399'] == 1 or khanegi_cameraman.loc[j, '1400'] == 1):
                           sima_cameraman.loc[i, 'migrate'] = 1
                elif (sima_cameraman.loc[i, '1395'] == 1 or sima_cameraman.loc[i, '1396'] == 1 or sima_cameraman.loc[i, '1397'] == 1 or \
                   sima_cameraman.loc[i, '1398'] == 1) and sima_cameraman.loc[i, '1399'] == 0 and sima_cameraman.loc[i, '1400'] == 0:
                       if khanegi_cameraman.loc[j, '1395'] == 0 and khanegi_cameraman.loc[j, '1396'] == 0 and \
                       khanegi_cameraman.loc[j, '1397'] == 0 and khanegi_cameraman.loc[j, '1398'] == 0 and \
                        (khanegi_cameraman.loc[j, '1399'] == 1 or khanegi_cameraman.loc[j, '1400'] == 1):
                           sima_cameraman.loc[i, 'migrate'] = 1
                    
    for i in range(0, len(khanegi_cameraman)):
        print(i)
        for j in range(0, len(sima_cameraman)):
            if khanegi_cameraman.loc[i, 'cameraman'] == sima_cameraman.loc[j, 'cameraman']:
                if khanegi_cameraman.loc[i, '1395'] == 1 and khanegi_cameraman.loc[i, '1396'] == 0 and khanegi_cameraman.loc[i, '1397'] == 0 and \
                   khanegi_cameraman.loc[i, '1398'] == 0 and khanegi_cameraman.loc[i, '1399'] == 0 and khanegi_cameraman.loc[i, '1400'] == 0:
                       if sima_cameraman.loc[j, '1395'] == 0 and (sima_cameraman.loc[j, '1396'] == 1 or \
                       sima_cameraman.loc[j, '1397'] == 1 or sima_cameraman.loc[j, '1398'] == 1 or \
                        sima_cameraman.loc[j, '1399'] == 1 or sima_cameraman.loc[j, '1400'] == 1):
                           khanegi_cameraman.loc[i, 'migrate'] = 1
                if (khanegi_cameraman.loc[i, '1395'] == 1 or khanegi_cameraman.loc[i, '1396'] == 1) and khanegi_cameraman.loc[i, '1397'] == 0 and \
                   khanegi_cameraman.loc[i, '1398'] == 0 and khanegi_cameraman.loc[i, '1399'] == 0 and khanegi_cameraman.loc[i, '1400'] == 0:
                       if sima_cameraman.loc[j, '1395'] == 0 and sima_cameraman.loc[j, '1396'] == 0 and \
                       (sima_cameraman.loc[j, '1397'] == 1 or sima_cameraman.loc[j, '1398'] == 1 or \
                        sima_cameraman.loc[j, '1399'] == 1 or sima_cameraman.loc[j, '1400'] == 1):
                           sima_cameraman.loc[i, 'migrate'] = 1
                if (khanegi_cameraman.loc[i, '1395'] == 1 or khanegi_cameraman.loc[i, '1396'] == 1 or khanegi_cameraman.loc[i, '1397'] == 1) and \
                   khanegi_cameraman.loc[i, '1398'] == 0 and khanegi_cameraman.loc[i, '1399'] == 0 and khanegi_cameraman.loc[i, '1400'] == 0:
                       if sima_cameraman.loc[j, '1395'] == 0 and sima_cameraman.loc[j, '1396'] == 0 and \
                       sima_cameraman.loc[j, '1397'] == 0 and (sima_cameraman.loc[j, '1398'] == 1 or \
                        sima_cameraman.loc[j, '1399'] == 1 or sima_cameraman.loc[j, '1400'] == 1):
                           sima_cameraman.loc[i, 'migrate'] = 1
                if (khanegi_cameraman.loc[i, '1395'] == 1 or khanegi_cameraman.loc[i, '1396'] == 1 or khanegi_cameraman.loc[i, '1397'] == 1 or \
                   khanegi_cameraman.loc[i, '1398'] == 1) and khanegi_cameraman.loc[i, '1399'] == 0 and khanegi_cameraman.loc[i, '1400'] == 0:
                       if sima_cameraman.loc[j, '1395'] == 0 and sima_cameraman.loc[j, '1396'] == 0 and \
                       sima_cameraman.loc[j, '1397'] == 0 and sima_cameraman.loc[j, '1398'] == 0 and \
                        (sima_cameraman.loc[j, '1399'] == 1 or sima_cameraman.loc[j, '1400'] == 1):
                           sima_cameraman.loc[i, 'migrate'] = 1
    return sima_cameraman,  khanegi_cameraman                         
