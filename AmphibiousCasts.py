
def AmphibiousCasts(sima_casts, khanegi_casts):
    import pandas as pd
    sima_casts = sima_casts.query('migrate != 1')
    khanegi_casts = khanegi_casts.query('migrate != 1')
    for i in range(0, len(sima_casts)):
        print(i)
        cast = sima_casts.loc[i, 'casts']
        for j in range(0, len(khanegi_casts)):
            if khanegi_casts.loc[i, 'casts'] == cast:
                sum_score_sima = sima_casts.loc[i, '1395']+sima_casts.loc[i, '1396']+sima_casts.loc[i, '1397']+sima_casts.loc[i, '1398']+sima_casts.loc[i, '1399']+sima_casts.loc[i, '1400']
                sum_score_khanegi = khanegi_casts.loc[i, '1395']+khanegi_casts.loc[i, '1396']+khanegi_casts.loc[i, '1397']+khanegi_casts.loc[i, '1398']+khanegi_casts.loc[i, '1399']+khanegi_casts.loc[i, '1400']
                if sum_score_sima > 1 or sum_score_khanegi > 1:
                    sima_casts.iloc[i, ]
                    
        