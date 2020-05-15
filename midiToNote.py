import mido
import json
import mcfunction.Block as bl
import mcfunction.Playsound as ps


midi_file = 'Home'

midi_path = f'mid/{midi_file}.mid'
info_text_path = f'midi_info/{midi_file}_nbs.txt'

info_text_file = open(info_text_path,mode='w')#创建info_file对象
midi_object=mido.MidiFile(midi_path)#创建midi对象

type=['note_on','note_off'] #需要的音符起止信息

tick_accuracy = 60 #最小能识别的tick
'''
30 ---- 64
60 ---- 32
120 ---- 16
240 ---- 8
480 ----4
'''


for i,track in enumerate(midi_object.tracks): #第i条音轨
    # print(f'track{i}')
    info_text_file.write(f'track{i}\n')

    last_time = 0
    last_on = 0

    for msg in track: #音轨中的信息

        #####累加时间轴
        info = msg.dict()
        info['pertime']=info['time']
        info['time'] += last_time
        last_time = info['time']
        #####


        
        if (info['type'] in type): #type is needed

            #####
            del info['velocity']
            del info['channel']
            #####转换成音符时间
            info['time'] = round(info['time']/tick_accuracy)
            #####

            if info['type'] == 'note_on': # 音符盒只处理note_on
                
                #####
                del info['type']
                # del info['time']
                #####转换成时间差
                info['pertime'] = info['time'] - last_on
                last_on = info['time']
                #####
                
                #####


            
                ps.playsound(info['time'],info['note'])
                bl.block(info['time']/2,25,info['note'],info['time'],'end_rod')
                


                # jsoninfo = json.dumps(info)
                # info_text_file.write(jsoninfo+'\n')







        

