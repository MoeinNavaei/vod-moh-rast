def Migration_editor(sima_editor, khanegi_editor):
    sima_editor.insert(8, 'migrate', 0)
    khanegi_editor.insert(8, 'migrate', 0)
    for i in range(0, len(sima_editor)):
        print(i)
        for j in range(0, len(khanegi_editor)):
            if sima_editor.loc[i, 'editor'] == khanegi_editor.loc[j, 'editor']:
                if sima_editor.loc[i, '1395'] == 1 and sima_editor.loc[i, '1396'] == 0 and sima_editor.loc[i, '1397'] == 0 and \
                   sima_editor.loc[i, '1398'] == 0 and sima_editor.loc[i, '1399'] == 0 and sima_editor.loc[i, '1400'] == 0:
                       if khanegi_editor.loc[j, '1395'] == 0 and (khanegi_editor.loc[j, '1396'] == 1 or \
                       khanegi_editor.loc[j, '1397'] == 1 or khanegi_editor.loc[j, '1398'] == 1 or \
                        khanegi_editor.loc[j, '1399'] == 1 or khanegi_editor.loc[j, '1400'] == 1):
                           sima_editor.loc[i, 'migrate'] = 1
                elif (sima_editor.loc[i, '1395'] == 1 or sima_editor.loc[i, '1396'] == 1) and sima_editor.loc[i, '1397'] == 0 and \
                   sima_editor.loc[i, '1398'] == 0 and sima_editor.loc[i, '1399'] == 0 and sima_editor.loc[i, '1400'] == 0:
                       if khanegi_editor.loc[j, '1395'] == 0 and khanegi_editor.loc[j, '1396'] == 0 and \
                       (khanegi_editor.loc[j, '1397'] == 1 or khanegi_editor.loc[j, '1398'] == 1 or \
                        khanegi_editor.loc[j, '1399'] == 1 or khanegi_editor.loc[j, '1400'] == 1):
                           sima_editor.loc[i, 'migrate'] = 1
                elif (sima_editor.loc[i, '1395'] == 1 or sima_editor.loc[i, '1396'] == 1 or sima_editor.loc[i, '1397'] == 1) and \
                   sima_editor.loc[i, '1398'] == 0 and sima_editor.loc[i, '1399'] == 0 and sima_editor.loc[i, '1400'] == 0:
                       if khanegi_editor.loc[j, '1395'] == 0 and khanegi_editor.loc[j, '1396'] == 0 and \
                       khanegi_editor.loc[j, '1397'] == 0 and (khanegi_editor.loc[j, '1398'] == 1 or \
                        khanegi_editor.loc[j, '1399'] == 1 or khanegi_editor.loc[j, '1400'] == 1):
                           sima_editor.loc[i, 'migrate'] = 1
                elif (sima_editor.loc[i, '1395'] == 1 or sima_editor.loc[i, '1396'] == 1 or sima_editor.loc[i, '1397'] == 1 or \
                   sima_editor.loc[i, '1398'] == 1) and sima_editor.loc[i, '1399'] == 0 and sima_editor.loc[i, '1400'] == 0:
                       if khanegi_editor.loc[j, '1395'] == 0 and khanegi_editor.loc[j, '1396'] == 0 and \
                       khanegi_editor.loc[j, '1397'] == 0 and khanegi_editor.loc[j, '1398'] == 0 and \
                        (khanegi_editor.loc[j, '1399'] == 1 or khanegi_editor.loc[j, '1400'] == 1):
                           sima_editor.loc[i, 'migrate'] = 1
                    
    for i in range(0, len(khanegi_editor)):
        print(i)
        for j in range(0, len(sima_editor)):
            if khanegi_editor.loc[i, 'editor'] == sima_editor.loc[j, 'editor']:
                if khanegi_editor.loc[i, '1395'] == 1 and khanegi_editor.loc[i, '1396'] == 0 and khanegi_editor.loc[i, '1397'] == 0 and \
                   khanegi_editor.loc[i, '1398'] == 0 and khanegi_editor.loc[i, '1399'] == 0 and khanegi_editor.loc[i, '1400'] == 0:
                       if sima_editor.loc[j, '1395'] == 0 and (sima_editor.loc[j, '1396'] == 1 or \
                       sima_editor.loc[j, '1397'] == 1 or sima_editor.loc[j, '1398'] == 1 or \
                        sima_editor.loc[j, '1399'] == 1 or sima_editor.loc[j, '1400'] == 1):
                           khanegi_editor.loc[i, 'migrate'] = 1
                if (khanegi_editor.loc[i, '1395'] == 1 or khanegi_editor.loc[i, '1396'] == 1) and khanegi_editor.loc[i, '1397'] == 0 and \
                   khanegi_editor.loc[i, '1398'] == 0 and khanegi_editor.loc[i, '1399'] == 0 and khanegi_editor.loc[i, '1400'] == 0:
                       if sima_editor.loc[j, '1395'] == 0 and sima_editor.loc[j, '1396'] == 0 and \
                       (sima_editor.loc[j, '1397'] == 1 or sima_editor.loc[j, '1398'] == 1 or \
                        sima_editor.loc[j, '1399'] == 1 or sima_editor.loc[j, '1400'] == 1):
                           sima_editor.loc[i, 'migrate'] = 1
                if (khanegi_editor.loc[i, '1395'] == 1 or khanegi_editor.loc[i, '1396'] == 1 or khanegi_editor.loc[i, '1397'] == 1) and \
                   khanegi_editor.loc[i, '1398'] == 0 and khanegi_editor.loc[i, '1399'] == 0 and khanegi_editor.loc[i, '1400'] == 0:
                       if sima_editor.loc[j, '1395'] == 0 and sima_editor.loc[j, '1396'] == 0 and \
                       sima_editor.loc[j, '1397'] == 0 and (sima_editor.loc[j, '1398'] == 1 or \
                        sima_editor.loc[j, '1399'] == 1 or sima_editor.loc[j, '1400'] == 1):
                           sima_editor.loc[i, 'migrate'] = 1
                if (khanegi_editor.loc[i, '1395'] == 1 or khanegi_editor.loc[i, '1396'] == 1 or khanegi_editor.loc[i, '1397'] == 1 or \
                   khanegi_editor.loc[i, '1398'] == 1) and khanegi_editor.loc[i, '1399'] == 0 and khanegi_editor.loc[i, '1400'] == 0:
                       if sima_editor.loc[j, '1395'] == 0 and sima_editor.loc[j, '1396'] == 0 and \
                       sima_editor.loc[j, '1397'] == 0 and sima_editor.loc[j, '1398'] == 0 and \
                        (sima_editor.loc[j, '1399'] == 1 or sima_editor.loc[j, '1400'] == 1):
                           sima_editor.loc[i, 'migrate'] = 1
    return sima_editor,  khanegi_editor                         
