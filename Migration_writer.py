def Migration_writer(sima_writer, khanegi_writer):
    sima_writer.insert(8, 'migrate', 0)
    khanegi_writer.insert(8, 'migrate', 0)
    for i in range(0, len(sima_writer)):
        print(i)
        for j in range(0, len(khanegi_writer)):
            if sima_writer.loc[i, 'writer'] == khanegi_writer.loc[j, 'writer']:
                if sima_writer.loc[i, '1395'] == 1 and sima_writer.loc[i, '1396'] == 0 and sima_writer.loc[i, '1397'] == 0 and \
                   sima_writer.loc[i, '1398'] == 0 and sima_writer.loc[i, '1399'] == 0 and sima_writer.loc[i, '1400'] == 0:
                       if khanegi_writer.loc[j, '1395'] == 0 and (khanegi_writer.loc[j, '1396'] == 1 or \
                       khanegi_writer.loc[j, '1397'] == 1 or khanegi_writer.loc[j, '1398'] == 1 or \
                        khanegi_writer.loc[j, '1399'] == 1 or khanegi_writer.loc[j, '1400'] == 1):
                           sima_writer.loc[i, 'migrate'] = 1
                elif (sima_writer.loc[i, '1395'] == 1 or sima_writer.loc[i, '1396'] == 1) and sima_writer.loc[i, '1397'] == 0 and \
                   sima_writer.loc[i, '1398'] == 0 and sima_writer.loc[i, '1399'] == 0 and sima_writer.loc[i, '1400'] == 0:
                       if khanegi_writer.loc[j, '1395'] == 0 and khanegi_writer.loc[j, '1396'] == 0 and \
                       (khanegi_writer.loc[j, '1397'] == 1 or khanegi_writer.loc[j, '1398'] == 1 or \
                        khanegi_writer.loc[j, '1399'] == 1 or khanegi_writer.loc[j, '1400'] == 1):
                           sima_writer.loc[i, 'migrate'] = 1
                elif (sima_writer.loc[i, '1395'] == 1 or sima_writer.loc[i, '1396'] == 1 or sima_writer.loc[i, '1397'] == 1) and \
                   sima_writer.loc[i, '1398'] == 0 and sima_writer.loc[i, '1399'] == 0 and sima_writer.loc[i, '1400'] == 0:
                       if khanegi_writer.loc[j, '1395'] == 0 and khanegi_writer.loc[j, '1396'] == 0 and \
                       khanegi_writer.loc[j, '1397'] == 0 and (khanegi_writer.loc[j, '1398'] == 1 or \
                        khanegi_writer.loc[j, '1399'] == 1 or khanegi_writer.loc[j, '1400'] == 1):
                           sima_writer.loc[i, 'migrate'] = 1
                elif (sima_writer.loc[i, '1395'] == 1 or sima_writer.loc[i, '1396'] == 1 or sima_writer.loc[i, '1397'] == 1 or \
                   sima_writer.loc[i, '1398'] == 1) and sima_writer.loc[i, '1399'] == 0 and sima_writer.loc[i, '1400'] == 0:
                       if khanegi_writer.loc[j, '1395'] == 0 and khanegi_writer.loc[j, '1396'] == 0 and \
                       khanegi_writer.loc[j, '1397'] == 0 and khanegi_writer.loc[j, '1398'] == 0 and \
                        (khanegi_writer.loc[j, '1399'] == 1 or khanegi_writer.loc[j, '1400'] == 1):
                           sima_writer.loc[i, 'migrate'] = 1
                    
    for i in range(0, len(khanegi_writer)):
        print(i)
        for j in range(0, len(sima_writer)):
            if khanegi_writer.loc[i, 'writer'] == sima_writer.loc[j, 'writer']:
                if khanegi_writer.loc[i, '1395'] == 1 and khanegi_writer.loc[i, '1396'] == 0 and khanegi_writer.loc[i, '1397'] == 0 and \
                   khanegi_writer.loc[i, '1398'] == 0 and khanegi_writer.loc[i, '1399'] == 0 and khanegi_writer.loc[i, '1400'] == 0:
                       if sima_writer.loc[j, '1395'] == 0 and (sima_writer.loc[j, '1396'] == 1 or \
                       sima_writer.loc[j, '1397'] == 1 or sima_writer.loc[j, '1398'] == 1 or \
                        sima_writer.loc[j, '1399'] == 1 or sima_writer.loc[j, '1400'] == 1):
                           khanegi_writer.loc[i, 'migrate'] = 1
                if (khanegi_writer.loc[i, '1395'] == 1 or khanegi_writer.loc[i, '1396'] == 1) and khanegi_writer.loc[i, '1397'] == 0 and \
                   khanegi_writer.loc[i, '1398'] == 0 and khanegi_writer.loc[i, '1399'] == 0 and khanegi_writer.loc[i, '1400'] == 0:
                       if sima_writer.loc[j, '1395'] == 0 and sima_writer.loc[j, '1396'] == 0 and \
                       (sima_writer.loc[j, '1397'] == 1 or sima_writer.loc[j, '1398'] == 1 or \
                        sima_writer.loc[j, '1399'] == 1 or sima_writer.loc[j, '1400'] == 1):
                           sima_writer.loc[i, 'migrate'] = 1
                if (khanegi_writer.loc[i, '1395'] == 1 or khanegi_writer.loc[i, '1396'] == 1 or khanegi_writer.loc[i, '1397'] == 1) and \
                   khanegi_writer.loc[i, '1398'] == 0 and khanegi_writer.loc[i, '1399'] == 0 and khanegi_writer.loc[i, '1400'] == 0:
                       if sima_writer.loc[j, '1395'] == 0 and sima_writer.loc[j, '1396'] == 0 and \
                       sima_writer.loc[j, '1397'] == 0 and (sima_writer.loc[j, '1398'] == 1 or \
                        sima_writer.loc[j, '1399'] == 1 or sima_writer.loc[j, '1400'] == 1):
                           sima_writer.loc[i, 'migrate'] = 1
                if (khanegi_writer.loc[i, '1395'] == 1 or khanegi_writer.loc[i, '1396'] == 1 or khanegi_writer.loc[i, '1397'] == 1 or \
                   khanegi_writer.loc[i, '1398'] == 1) and khanegi_writer.loc[i, '1399'] == 0 and khanegi_writer.loc[i, '1400'] == 0:
                       if sima_writer.loc[j, '1395'] == 0 and sima_writer.loc[j, '1396'] == 0 and \
                       sima_writer.loc[j, '1397'] == 0 and sima_writer.loc[j, '1398'] == 0 and \
                        (sima_writer.loc[j, '1399'] == 1 or sima_writer.loc[j, '1400'] == 1):
                           sima_writer.loc[i, 'migrate'] = 1
    return sima_writer,  khanegi_writer                         
