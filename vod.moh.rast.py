import pandas as pd

khanegi=pd.read_excel(r'E:\python codes\vod moh rast\khanegi.xlsx')
sima=pd.read_excel(r'E:\python codes\vod moh rast\sima.xlsx')

########################### khanegi_sima_title ############################
from KhanegiSimaTitle import *

########################### Casts ############################
######### khanegi_casts #########
from KhanegiCasts import * 
######### sima_casts #########
from SimaCasts import *
######### migrate_casts #########
from Migration_casts import *

########################### Director ############################
######### khanegi_director #########
from KhanegiDirector import * 
######### sima_director #########
from SimaDirector import * 
######### migrate_director #########
from Migration_director import *

########################### Producer ############################
######### khanegi_producer #########
from KhanegiProducer import *
######### sima_producer #########
from SimaProducer import *
######### migrate_producer #########
from Migration_producer import *

########################### Writer ############################
######### khanegi_writer #########
from KhanegiWriter import *
######### sima_writer #########
from SimaWriter import *
######### migrate_writer #########
from Migration_writer import *

########################### ProducManager ############################
######### khanegi_ProducManager #########
from KhanegiProducManager import * 
######### sima_ProducManager #########
from SimaProducManager import *
######### migrate_ProducManager #########
from Migration_produc_manager import *

########################### Cameraman ############################
######### khanegi_Cameraman #########
from KhanegiCameraman import * 
######### sima_Cameraman #########
from SimaCameraman import *
######### migrate_Cameraman #########
from Migration_cameraman import *

########################### Editor ############################
######### khanegi_Editor #########
from KhanegiEditor import * 
######### sima_Editor #########
from SimaEditor import *
######### migrate_Editor #########
from Migration_editor import *

########################### RESULTS ############################
[khanegi_title_count, sima_title_count] = KhanegiSimaTitle(khanegi, sima)

khanegi_casts = KhanegiCasts(khanegi)
sima_casts = SimaCasts(sima)
[sima_casts,  khanegi_casts] = Migration_casts(sima_casts, khanegi_casts)

khanegi_director = KhanegiDirector(khanegi)
sima_director = SimaDirector(sima)
[sima_director,  khanegi_director] = Migration_director(sima_director, khanegi_director)

khanegi_producer = KhanegiProducer(khanegi)
sima_producer = SimaProducer(sima)
[sima_producer,  khanegi_producer] = Migration_producer(sima_producer, khanegi_producer)

khanegi_writer = KhanegiWriter(khanegi)
sima_writer = SimaWriter(sima)
[sima_writer,  khanegi_writer] = Migration_writer(sima_writer, khanegi_writer)

khanegi_produce_manager = KhanegiProducManager(khanegi)
sima_produce_manager = SimaProducManager(sima)
[sima_produce_manager,  khanegi_produce_manager] = Migration_produc_manager(sima_produce_manager, khanegi_produce_manager)

khanegi_cameraman = KhanegiCameraman(khanegi)
sima_cameraman = SimaCameraman(sima)
[sima_cameraman,  khanegi_cameraman] = Migration_cameraman(sima_cameraman, khanegi_cameraman)

khanegi_editor = KhanegiEditor(khanegi)
sima_editor = SimaEditor(sima)
[sima_editor,  khanegi_editor] = Migration_editor(sima_editor, khanegi_editor)
############################################################################


results = pd.DataFrame()
results.insert(0, 'x', '')
results.insert(1, 'سیما', '')
results.insert(2, 'نمایش خانگی', '')

results.loc[0, 'x'] = 'تعداد محتوا'

results.loc[1, 'x'] = 'تعداد بازیگران'
#results.loc[2, 'x'] = 'درصد ماندگاری بازیگران با درجه 1'
#results.loc[3, 'x'] = 'درصد ماندگاری بازیگران با درجه 2'
#results.loc[4, 'x'] = 'درصد ماندگاری بازیگران با درجه 3'
#results.loc[5, 'x'] = 'درصد ماندگاری بازیگران با درجه 4'
results.loc[2, 'x'] = 'درصد ماندگاری بازیگران'
results.loc[3, 'x'] = 'درصد کوچ بازیگران'
results.loc[4, 'x'] = 'درصد بازیگران دوزیست'

results.loc[5, 'x'] = 'تعداد کارگردانان'
#results.loc[9, 'x'] = 'درصد ماندگاری کارگردانان با درجه 1'
#results.loc[10, 'x'] = 'درصد ماندگاری کارگردانان با درجه 2'
#results.loc[11, 'x'] = 'درصد ماندگاری کارگردانان با درجه 3'
#results.loc[12, 'x'] = 'درصد ماندگاری کارگردانان با درجه 4'
results.loc[6, 'x'] = 'درصد ماندگاری کارگردانان'
results.loc[7, 'x'] = 'درصد کوچ کارگردنان'
results.loc[8, 'x'] = 'درصد کارگردانان دوزیست'

results.loc[9, 'x'] = 'تعداد تهیه کنندگان'
#results.loc[16, 'x'] = 'درصد ماندگاری تهیه کنندگان با درجه 1'
#results.loc[17, 'x'] = 'درصد ماندگاری تهیه کنندگان با درجه 2'
#results.loc[18, 'x'] = 'درصد ماندگاری تهیه کنندگان با درجه 3'
#results.loc[19, 'x'] = 'درصد ماندگاری تهیه کنندگان با درجه 4'
results.loc[10, 'x'] = 'درصد ماندگاری تهیه کنندگان'
results.loc[11, 'x'] = 'درصد کوچ تهیه کنندگان'
results.loc[12, 'x'] = 'درصد تهیه کنندگان دوزیست'

results.loc[13, 'x'] = 'تعداد نویسندگان'
#results.loc[23, 'x'] = 'درصد ماندگاری نویسندگان با درجه 1'
#results.loc[24, 'x'] = 'درصد ماندگاری نویسندگان با درجه 2'
#results.loc[25, 'x'] = 'درصد ماندگاری نویسندگان با درجه 3'
#results.loc[26, 'x'] = 'درصد ماندگاری نویسندگان با درجه 4'
results.loc[14, 'x'] = 'درصد ماندگاری نویسندگان'
results.loc[15, 'x'] = 'درصد کوچ نویسندگان'
results.loc[16, 'x'] = 'درصد نویسندگان دوزیست'

results.loc[17, 'x'] = 'تعداد مدیران تولید'
#results.loc[30, 'x'] = 'درصد ماندگاری مدیر تولید با درجه 1'
#results.loc[31, 'x'] = 'درصد ماندگاری مدیر تولید با درجه 2'
#results.loc[32, 'x'] = 'درصد ماندگاری مدیر تولید با درجه 3'
#results.loc[33, 'x'] = 'درصد ماندگاری مدیر تولید با درجه 4'
results.loc[18, 'x'] = 'درصد ماندگاری مدیر تولید'
results.loc[19, 'x'] = 'درصد کوچ مدیر تولید'
results.loc[20, 'x'] = 'درصد مدیران تولید دوزیست'

results.loc[21, 'x'] = 'تعداد فیلمبرداران'
#results.loc[37, 'x'] = 'درصد ماندگاری فیلمبردار با درجه 1'
#results.loc[38, 'x'] = 'درصد ماندگاری فیلمبردار با درجه 2'
#results.loc[39, 'x'] = 'درصد ماندگاری فیلمبردار با درجه 3'
#results.loc[40, 'x'] = 'درصد ماندگاری فیلمبردار با درجه 4'
results.loc[22, 'x'] = 'درصد ماندگاری فیلمبردار'
results.loc[23, 'x'] = 'درصد کوچ فیلمبردار'
results.loc[24, 'x'] = 'درصد فیلمبرداران دوزیست'

results.loc[25, 'x'] = 'تعداد تدوینگران'
#results.loc[44, 'x'] = 'درصد ماندگاری تدوینگر با درجه 1'
#results.loc[45, 'x'] = 'درصد ماندگاری تدوینگر با درجه 2'
#results.loc[46, 'x'] = 'درصد ماندگاری تدوینگر با درجه 3'
#results.loc[47, 'x'] = 'درصد ماندگاری تدوینگر با درجه 4'
results.loc[26, 'x'] = 'درصد ماندگاری تدوینگر'
results.loc[27, 'x'] = 'درصد کوچ تدوینگر'
results.loc[28, 'x'] = 'درصد تدوینگران دوزیست'




results.loc[0, 'سیما'] = len(sima_title_count)
#######################################################
results.loc[1, 'سیما'] = len(sima_casts)
k = 0
for i in range(0, len(sima_casts)):
    print(i)
    if sima_casts.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(khanegi_casts)):
            if sima_casts.loc[i, 'casts'] != khanegi_casts.loc[j, 'casts']:
                k1 = k1 + 1
        if k1 == len(khanegi_casts):
            k = k + 1
aaa = round(k*100/len(sima_casts), 1)
results.loc[2, 'سیما'] = aaa
aa = round(sima_casts['migrate'].sum()*100/len(sima_casts), 1)
results.loc[3, 'سیما'] = aa
a = 100 - aa - aaa
results.loc[4, 'سیما'] = round(a, 1)
#######################################################
results.loc[5, 'سیما'] = len(sima_director)
k = 0
for i in range(0, len(sima_director)):
    print(i)
    if sima_director.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(khanegi_director)):
            if sima_director.loc[i, 'director'] != khanegi_director.loc[j, 'director']:
                k1 = k1 + 1
        if k1 == len(khanegi_director):
            k = k + 1
aaa = round(k*100/len(sima_director), 1)
results.loc[6, 'سیما'] = aaa
aa = round(sima_director['migrate'].sum()*100/len(sima_director), 1)
results.loc[7, 'سیما'] = aa
a = 100 - aa - aaa
results.loc[8, 'سیما'] = round(a, 1)
#######################################################
results.loc[9, 'سیما'] = len(sima_producer)
k = 0
for i in range(0, len(sima_producer)):
    print(i)
    if sima_producer.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(khanegi_producer)):
            if sima_producer.loc[i, 'producer'] != khanegi_producer.loc[j, 'producer']:
                k1 = k1 + 1
        if k1 == len(khanegi_producer):
            k = k + 1
aaa = round(k*100/len(sima_producer), 1)
results.loc[10, 'سیما'] = aaa
aa = round(sima_producer['migrate'].sum()*100/len(sima_producer), 1)
results.loc[11, 'سیما'] = aa
a = 100 - aa - aaa
results.loc[12, 'سیما'] = round(a, 1)
#######################################################
results.loc[13, 'سیما'] = len(sima_writer)
k = 0
for i in range(0, len(sima_writer)):
    print(i)
    if sima_writer.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(khanegi_writer)):
            if sima_writer.loc[i, 'writer'] != khanegi_writer.loc[j, 'writer']:
                k1 = k1 + 1
        if k1 == len(khanegi_writer):
            k = k + 1
aaa = round(k*100/len(sima_writer), 1)
results.loc[14, 'سیما'] = aaa
aa = round(sima_writer['migrate'].sum()*100/len(sima_writer), 1)
results.loc[15, 'سیما'] = aa
a = 100 - aa - aaa
results.loc[16, 'سیما'] = round(a, 1)
#######################################################
results.loc[17, 'سیما'] = len(sima_produce_manager)
k = 0
for i in range(0, len(sima_produce_manager)):
    print(i)
    if sima_produce_manager.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(khanegi_produce_manager)):
            if sima_produce_manager.loc[i, 'produce_manager'] != khanegi_produce_manager.loc[j, 'produce_manager']:
                k1 = k1 + 1
        if k1 == len(khanegi_produce_manager):
            k = k + 1
aaa = round(k*100/len(sima_produce_manager), 1)
results.loc[18, 'سیما'] = aaa
aa = round(sima_produce_manager['migrate'].sum()*100/len(sima_produce_manager), 1)
results.loc[19, 'سیما'] = aa
a = 100 - aa - aaa
results.loc[20, 'سیما'] = round(a, 1)
#######################################################
results.loc[21, 'سیما'] = len(sima_cameraman)
k = 0
for i in range(0, len(sima_cameraman)):
#    print(i)
    if sima_cameraman.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(khanegi_cameraman)):
            if sima_cameraman.loc[i, 'cameraman'] != khanegi_cameraman.loc[j, 'cameraman']:
                k1 = k1 + 1
        if k1 == len(khanegi_cameraman):
            print(sima_cameraman.loc[i, 'cameraman'])
            k = k + 1
aaa = round(k*100/len(sima_cameraman), 1)
results.loc[22, 'سیما'] = aaa
aa = round(sima_cameraman['migrate'].sum()*100/len(sima_cameraman), 1)
results.loc[23, 'سیما'] = aa
a = 100 - aa - aaa
results.loc[24, 'سیما'] = round(a, 1)
#######################################################
results.loc[25, 'سیما'] = len(sima_editor)
k = 0
for i in range(0, len(sima_editor)):
    print(i)
    if sima_editor.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(khanegi_editor)):
            if sima_editor.loc[i, 'editor'] != khanegi_editor.loc[j, 'editor']:
                k1 = k1 + 1
        if k1 == len(khanegi_editor):
            k = k + 1
aaa = round(k*100/len(sima_editor), 1)
results.loc[26, 'سیما'] = aaa
aa = round(sima_editor['migrate'].sum()*100/len(sima_editor), 1)
results.loc[27, 'سیما'] = aa
a = 100 - aa - aaa
results.loc[28, 'سیما'] = round(a, 1)
#######################################################
#######################################################
#######################################################
results.loc[0, 'نمایش خانگی'] = len(khanegi_title_count)
#######################################################
results.loc[1, 'نمایش خانگی'] = len(khanegi_casts)
k = 0
for i in range(0, len(khanegi_casts)):
    print(i)
    if khanegi_casts.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(sima_casts)):
            if khanegi_casts.loc[i, 'casts'] != sima_casts.loc[j, 'casts']:
                k1 = k1 + 1
        if k1 == len(sima_casts):
            k = k + 1
aaa = round(k*100/len(khanegi_casts), 1)
results.loc[2, 'نمایش خانگی'] = aaa
aa = round(khanegi_casts['migrate'].sum()*100/len(khanegi_casts), 1)
results.loc[3, 'نمایش خانگی'] = aa
a = 100 - aa - aaa
results.loc[4, 'نمایش خانگی'] = round(a, 1)
#######################################################
results.loc[5, 'نمایش خانگی'] = len(khanegi_director)
k = 0
for i in range(0, len(khanegi_director)):
    print(i)
    if khanegi_director.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(sima_director)):
            if khanegi_director.loc[i, 'director'] != sima_director.loc[j, 'director']:
                k1 = k1 + 1
        if k1 == len(sima_director):
            k = k + 1
aaa = round(k*100/len(khanegi_director), 1)
results.loc[6, 'نمایش خانگی'] = aaa
aa = round(khanegi_director['migrate'].sum()*100/len(khanegi_director), 1)
results.loc[7, 'نمایش خانگی'] = aa
a = 100 - aa - aaa
results.loc[8, 'نمایش خانگی'] = round(a, 1)
#######################################################
results.loc[9, 'نمایش خانگی'] = len(khanegi_producer)
k = 0
for i in range(0, len(khanegi_producer)):
    print(i)
    if khanegi_producer.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(sima_producer)):
            if khanegi_producer.loc[i, 'producer'] != sima_producer.loc[j, 'producer']:
                k1 = k1 + 1
        if k1 == len(sima_producer):
            k = k + 1
aaa = round(k*100/len(khanegi_producer), 1)
results.loc[10, 'نمایش خانگی'] = aaa
aa = round(khanegi_producer['migrate'].sum()*100/len(khanegi_producer), 1)
results.loc[11, 'نمایش خانگی'] = aa
a = 100 - aa - aaa
results.loc[12, 'نمایش خانگی'] = round(a, 1)
#######################################################
results.loc[13, 'نمایش خانگی'] = len(khanegi_writer)
k = 0
for i in range(0, len(khanegi_writer)):
    print(i)
    if khanegi_writer.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(sima_writer)):
            if khanegi_writer.loc[i, 'writer'] != sima_writer.loc[j, 'writer']:
                k1 = k1 + 1
        if k1 == len(sima_writer):
            k = k + 1
aaa = round(k*100/len(khanegi_writer), 1)
results.loc[14, 'نمایش خانگی'] = aaa
aa = round(khanegi_writer['migrate'].sum()*100/len(khanegi_writer), 1)
results.loc[15, 'نمایش خانگی'] = aa
a = 100 - aa - aaa
results.loc[16, 'نمایش خانگی'] = round(a, 1)
#######################################################
results.loc[17, 'نمایش خانگی'] = len(khanegi_produce_manager)
k = 0
for i in range(0, len(khanegi_produce_manager)):
    print(i)
    if khanegi_produce_manager.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(sima_produce_manager)):
            if khanegi_produce_manager.loc[i, 'produce_manager'] != sima_produce_manager.loc[j, 'produce_manager']:
                k1 = k1 + 1
        if k1 == len(sima_produce_manager):
            k = k + 1
aaa = round(k*100/len(khanegi_produce_manager), 1)
results.loc[18, 'نمایش خانگی'] = aaa
aa = round(khanegi_produce_manager['migrate'].sum()*100/len(khanegi_produce_manager), 1)
results.loc[19, 'نمایش خانگی'] = aa
a = 100 - aa - aaa
results.loc[20, 'نمایش خانگی'] = round(a, 1)
#######################################################
results.loc[21, 'نمایش خانگی'] = len(khanegi_cameraman)
k = 0
for i in range(0, len(khanegi_cameraman)):
    print(i)
    if khanegi_cameraman.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(sima_cameraman)):
            if khanegi_cameraman.loc[i, 'cameraman'] != sima_cameraman.loc[j, 'cameraman']:
                k1 = k1 + 1
        if k1 == len(sima_cameraman):
            k = k + 1
aaa = round(k*100/len(khanegi_cameraman), 1)
results.loc[22, 'نمایش خانگی'] = aaa
aa = round(khanegi_cameraman['migrate'].sum()*100/len(khanegi_cameraman), 1)
results.loc[23, 'نمایش خانگی'] = aa
a = 100 - aa - aaa
results.loc[24, 'نمایش خانگی'] = round(a, 1)
#######################################################
results.loc[25, 'نمایش خانگی'] = len(khanegi_editor)
k = 0
for i in range(0, len(khanegi_editor)):
    print(i)
    if khanegi_editor.loc[i, 'score'] > 1:
        k1 = 0
        for j in range(0, len(sima_editor)):
            if khanegi_editor.loc[i, 'editor'] != sima_editor.loc[j, 'editor']:
                k1 = k1 + 1
        if k1 == len(sima_editor):
            k = k + 1
aaa = round(k*100/len(khanegi_editor), 1)
results.loc[26, 'نمایش خانگی'] = aaa
aa = round(khanegi_editor['migrate'].sum()*100/len(khanegi_editor), 1)
results.loc[27, 'نمایش خانگی'] = aa
a = 100 - aa - aaa
results.loc[28, 'نمایش خانگی'] = round(a, 1)
#######################################################

results.to_excel('results_new.xlsx', index=False)






















