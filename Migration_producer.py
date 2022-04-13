def Migration_producer(sima_producer, khanegi_producer):
    sima_producer.insert(8, 'migrate', 0)
    khanegi_producer.insert(8, 'migrate', 0)
    for i in range(0, len(sima_producer)):
        print(i)
        for j in range(0, len(khanegi_producer)):
            if sima_producer.loc[i, 'producer'] == khanegi_producer.loc[j, 'producer']:
                if sima_producer.loc[i, '1395'] == 1 and sima_producer.loc[i, '1396'] == 0 and sima_producer.loc[i, '1397'] == 0 and \
                   sima_producer.loc[i, '1398'] == 0 and sima_producer.loc[i, '1399'] == 0 and sima_producer.loc[i, '1400'] == 0:
                       if khanegi_producer.loc[j, '1395'] == 0 and (khanegi_producer.loc[j, '1396'] == 1 or \
                       khanegi_producer.loc[j, '1397'] == 1 or khanegi_producer.loc[j, '1398'] == 1 or \
                        khanegi_producer.loc[j, '1399'] == 1 or khanegi_producer.loc[j, '1400'] == 1):
                           sima_producer.loc[i, 'migrate'] = 1
                elif (sima_producer.loc[i, '1395'] == 1 or sima_producer.loc[i, '1396'] == 1) and sima_producer.loc[i, '1397'] == 0 and \
                   sima_producer.loc[i, '1398'] == 0 and sima_producer.loc[i, '1399'] == 0 and sima_producer.loc[i, '1400'] == 0:
                       if khanegi_producer.loc[j, '1395'] == 0 and khanegi_producer.loc[j, '1396'] == 0 and \
                       (khanegi_producer.loc[j, '1397'] == 1 or khanegi_producer.loc[j, '1398'] == 1 or \
                        khanegi_producer.loc[j, '1399'] == 1 or khanegi_producer.loc[j, '1400'] == 1):
                           sima_producer.loc[i, 'migrate'] = 1
                elif (sima_producer.loc[i, '1395'] == 1 or sima_producer.loc[i, '1396'] == 1 or sima_producer.loc[i, '1397'] == 1) and \
                   sima_producer.loc[i, '1398'] == 0 and sima_producer.loc[i, '1399'] == 0 and sima_producer.loc[i, '1400'] == 0:
                       if khanegi_producer.loc[j, '1395'] == 0 and khanegi_producer.loc[j, '1396'] == 0 and \
                       khanegi_producer.loc[j, '1397'] == 0 and (khanegi_producer.loc[j, '1398'] == 1 or \
                        khanegi_producer.loc[j, '1399'] == 1 or khanegi_producer.loc[j, '1400'] == 1):
                           sima_producer.loc[i, 'migrate'] = 1
                elif (sima_producer.loc[i, '1395'] == 1 or sima_producer.loc[i, '1396'] == 1 or sima_producer.loc[i, '1397'] == 1 or \
                   sima_producer.loc[i, '1398'] == 1) and sima_producer.loc[i, '1399'] == 0 and sima_producer.loc[i, '1400'] == 0:
                       if khanegi_producer.loc[j, '1395'] == 0 and khanegi_producer.loc[j, '1396'] == 0 and \
                       khanegi_producer.loc[j, '1397'] == 0 and khanegi_producer.loc[j, '1398'] == 0 and \
                        (khanegi_producer.loc[j, '1399'] == 1 or khanegi_producer.loc[j, '1400'] == 1):
                           sima_producer.loc[i, 'migrate'] = 1
                    
    for i in range(0, len(khanegi_producer)):
        print(i)
        for j in range(0, len(sima_producer)):
            if khanegi_producer.loc[i, 'producer'] == sima_producer.loc[j, 'producer']:
                if khanegi_producer.loc[i, '1395'] == 1 and khanegi_producer.loc[i, '1396'] == 0 and khanegi_producer.loc[i, '1397'] == 0 and \
                   khanegi_producer.loc[i, '1398'] == 0 and khanegi_producer.loc[i, '1399'] == 0 and khanegi_producer.loc[i, '1400'] == 0:
                       if sima_producer.loc[j, '1395'] == 0 and (sima_producer.loc[j, '1396'] == 1 or \
                       sima_producer.loc[j, '1397'] == 1 or sima_producer.loc[j, '1398'] == 1 or \
                        sima_producer.loc[j, '1399'] == 1 or sima_producer.loc[j, '1400'] == 1):
                           khanegi_producer.loc[i, 'migrate'] = 1
                if (khanegi_producer.loc[i, '1395'] == 1 or khanegi_producer.loc[i, '1396'] == 1) and khanegi_producer.loc[i, '1397'] == 0 and \
                   khanegi_producer.loc[i, '1398'] == 0 and khanegi_producer.loc[i, '1399'] == 0 and khanegi_producer.loc[i, '1400'] == 0:
                       if sima_producer.loc[j, '1395'] == 0 and sima_producer.loc[j, '1396'] == 0 and \
                       (sima_producer.loc[j, '1397'] == 1 or sima_producer.loc[j, '1398'] == 1 or \
                        sima_producer.loc[j, '1399'] == 1 or sima_producer.loc[j, '1400'] == 1):
                           sima_producer.loc[i, 'migrate'] = 1
                if (khanegi_producer.loc[i, '1395'] == 1 or khanegi_producer.loc[i, '1396'] == 1 or khanegi_producer.loc[i, '1397'] == 1) and \
                   khanegi_producer.loc[i, '1398'] == 0 and khanegi_producer.loc[i, '1399'] == 0 and khanegi_producer.loc[i, '1400'] == 0:
                       if sima_producer.loc[j, '1395'] == 0 and sima_producer.loc[j, '1396'] == 0 and \
                       sima_producer.loc[j, '1397'] == 0 and (sima_producer.loc[j, '1398'] == 1 or \
                        sima_producer.loc[j, '1399'] == 1 or sima_producer.loc[j, '1400'] == 1):
                           sima_producer.loc[i, 'migrate'] = 1
                if (khanegi_producer.loc[i, '1395'] == 1 or khanegi_producer.loc[i, '1396'] == 1 or khanegi_producer.loc[i, '1397'] == 1 or \
                   khanegi_producer.loc[i, '1398'] == 1) and khanegi_producer.loc[i, '1399'] == 0 and khanegi_producer.loc[i, '1400'] == 0:
                       if sima_producer.loc[j, '1395'] == 0 and sima_producer.loc[j, '1396'] == 0 and \
                       sima_producer.loc[j, '1397'] == 0 and sima_producer.loc[j, '1398'] == 0 and \
                        (sima_producer.loc[j, '1399'] == 1 or sima_producer.loc[j, '1400'] == 1):
                           sima_producer.loc[i, 'migrate'] = 1
    return sima_producer,  khanegi_producer                         
