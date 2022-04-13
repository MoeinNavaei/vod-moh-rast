def Migration_produc_manager(sima_produc_manager, khanegi_produc_manager):
    sima_produc_manager.insert(8, 'migrate', 0)
    khanegi_produc_manager.insert(8, 'migrate', 0)
    for i in range(0, len(sima_produc_manager)):
        print(i)
        for j in range(0, len(khanegi_produc_manager)):
            if sima_produc_manager.loc[i, 'produce_manager'] == khanegi_produc_manager.loc[j, 'produce_manager']:
                if sima_produc_manager.loc[i, '1395'] == 1 and sima_produc_manager.loc[i, '1396'] == 0 and sima_produc_manager.loc[i, '1397'] == 0 and \
                   sima_produc_manager.loc[i, '1398'] == 0 and sima_produc_manager.loc[i, '1399'] == 0 and sima_produc_manager.loc[i, '1400'] == 0:
                       if khanegi_produc_manager.loc[j, '1395'] == 0 and (khanegi_produc_manager.loc[j, '1396'] == 1 or \
                       khanegi_produc_manager.loc[j, '1397'] == 1 or khanegi_produc_manager.loc[j, '1398'] == 1 or \
                        khanegi_produc_manager.loc[j, '1399'] == 1 or khanegi_produc_manager.loc[j, '1400'] == 1):
                           sima_produc_manager.loc[i, 'migrate'] = 1
                elif (sima_produc_manager.loc[i, '1395'] == 1 or sima_produc_manager.loc[i, '1396'] == 1) and sima_produc_manager.loc[i, '1397'] == 0 and \
                   sima_produc_manager.loc[i, '1398'] == 0 and sima_produc_manager.loc[i, '1399'] == 0 and sima_produc_manager.loc[i, '1400'] == 0:
                       if khanegi_produc_manager.loc[j, '1395'] == 0 and khanegi_produc_manager.loc[j, '1396'] == 0 and \
                       (khanegi_produc_manager.loc[j, '1397'] == 1 or khanegi_produc_manager.loc[j, '1398'] == 1 or \
                        khanegi_produc_manager.loc[j, '1399'] == 1 or khanegi_produc_manager.loc[j, '1400'] == 1):
                           sima_produc_manager.loc[i, 'migrate'] = 1
                elif (sima_produc_manager.loc[i, '1395'] == 1 or sima_produc_manager.loc[i, '1396'] == 1 or sima_produc_manager.loc[i, '1397'] == 1) and \
                   sima_produc_manager.loc[i, '1398'] == 0 and sima_produc_manager.loc[i, '1399'] == 0 and sima_produc_manager.loc[i, '1400'] == 0:
                       if khanegi_produc_manager.loc[j, '1395'] == 0 and khanegi_produc_manager.loc[j, '1396'] == 0 and \
                       khanegi_produc_manager.loc[j, '1397'] == 0 and (khanegi_produc_manager.loc[j, '1398'] == 1 or \
                        khanegi_produc_manager.loc[j, '1399'] == 1 or khanegi_produc_manager.loc[j, '1400'] == 1):
                           sima_produc_manager.loc[i, 'migrate'] = 1
                elif (sima_produc_manager.loc[i, '1395'] == 1 or sima_produc_manager.loc[i, '1396'] == 1 or sima_produc_manager.loc[i, '1397'] == 1 or \
                   sima_produc_manager.loc[i, '1398'] == 1) and sima_produc_manager.loc[i, '1399'] == 0 and sima_produc_manager.loc[i, '1400'] == 0:
                       if khanegi_produc_manager.loc[j, '1395'] == 0 and khanegi_produc_manager.loc[j, '1396'] == 0 and \
                       khanegi_produc_manager.loc[j, '1397'] == 0 and khanegi_produc_manager.loc[j, '1398'] == 0 and \
                        (khanegi_produc_manager.loc[j, '1399'] == 1 or khanegi_produc_manager.loc[j, '1400'] == 1):
                           sima_produc_manager.loc[i, 'migrate'] = 1
                    
    for i in range(0, len(khanegi_produc_manager)):
        print(i)
        for j in range(0, len(sima_produc_manager)):
            if khanegi_produc_manager.loc[i, 'produce_manager'] == sima_produc_manager.loc[j, 'produce_manager']:
                if khanegi_produc_manager.loc[i, '1395'] == 1 and khanegi_produc_manager.loc[i, '1396'] == 0 and khanegi_produc_manager.loc[i, '1397'] == 0 and \
                   khanegi_produc_manager.loc[i, '1398'] == 0 and khanegi_produc_manager.loc[i, '1399'] == 0 and khanegi_produc_manager.loc[i, '1400'] == 0:
                       if sima_produc_manager.loc[j, '1395'] == 0 and (sima_produc_manager.loc[j, '1396'] == 1 or \
                       sima_produc_manager.loc[j, '1397'] == 1 or sima_produc_manager.loc[j, '1398'] == 1 or \
                        sima_produc_manager.loc[j, '1399'] == 1 or sima_produc_manager.loc[j, '1400'] == 1):
                           khanegi_produc_manager.loc[i, 'migrate'] = 1
                if (khanegi_produc_manager.loc[i, '1395'] == 1 or khanegi_produc_manager.loc[i, '1396'] == 1) and khanegi_produc_manager.loc[i, '1397'] == 0 and \
                   khanegi_produc_manager.loc[i, '1398'] == 0 and khanegi_produc_manager.loc[i, '1399'] == 0 and khanegi_produc_manager.loc[i, '1400'] == 0:
                       if sima_produc_manager.loc[j, '1395'] == 0 and sima_produc_manager.loc[j, '1396'] == 0 and \
                       (sima_produc_manager.loc[j, '1397'] == 1 or sima_produc_manager.loc[j, '1398'] == 1 or \
                        sima_produc_manager.loc[j, '1399'] == 1 or sima_produc_manager.loc[j, '1400'] == 1):
                           sima_produc_manager.loc[i, 'migrate'] = 1
                if (khanegi_produc_manager.loc[i, '1395'] == 1 or khanegi_produc_manager.loc[i, '1396'] == 1 or khanegi_produc_manager.loc[i, '1397'] == 1) and \
                   khanegi_produc_manager.loc[i, '1398'] == 0 and khanegi_produc_manager.loc[i, '1399'] == 0 and khanegi_produc_manager.loc[i, '1400'] == 0:
                       if sima_produc_manager.loc[j, '1395'] == 0 and sima_produc_manager.loc[j, '1396'] == 0 and \
                       sima_produc_manager.loc[j, '1397'] == 0 and (sima_produc_manager.loc[j, '1398'] == 1 or \
                        sima_produc_manager.loc[j, '1399'] == 1 or sima_produc_manager.loc[j, '1400'] == 1):
                           sima_produc_manager.loc[i, 'migrate'] = 1
                if (khanegi_produc_manager.loc[i, '1395'] == 1 or khanegi_produc_manager.loc[i, '1396'] == 1 or khanegi_produc_manager.loc[i, '1397'] == 1 or \
                   khanegi_produc_manager.loc[i, '1398'] == 1) and khanegi_produc_manager.loc[i, '1399'] == 0 and khanegi_produc_manager.loc[i, '1400'] == 0:
                       if sima_produc_manager.loc[j, '1395'] == 0 and sima_produc_manager.loc[j, '1396'] == 0 and \
                       sima_produc_manager.loc[j, '1397'] == 0 and sima_produc_manager.loc[j, '1398'] == 0 and \
                        (sima_produc_manager.loc[j, '1399'] == 1 or sima_produc_manager.loc[j, '1400'] == 1):
                           sima_produc_manager.loc[i, 'migrate'] = 1
    return sima_produc_manager,  khanegi_produc_manager                         
