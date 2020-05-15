import mido
import json

midi_file = 'cerebrawl1'
tick_accuracy = 60 #最小能识别的tick，480精度时，60为32分音符 




####################
midi_path = f'mid/{midi_file}.mid'
info_text_path = f'midi_info/{midi_file}_cmd.txt'

info_text_file = open(info_text_path,mode='w')#创建info_file对象
midi_object=mido.MidiFile(midi_path)#创建midi对象

####################









for i,track in enumerate(midi_object.tracks): #第i条音轨
    # print(f'track{i}')
    info_text_file.write(f'track{i}:\n')

    last_time = 0
    last_on = 0

    for msg in track: #音轨中的信息

        info = msg.dict()

        if info['type'] == 'control_change':
            continue

        try:
            del info['velocity']
        except:
            pass

        try:
            del info['channel']
        except:
            pass


        info['time'] += last_time
        last_time = info['time']
        info['time'] = round(info['time']/tick_accuracy)

        info['pertime'] = info['time'] - last_on
        last_on = info['time']

            
        #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑处理midi信息↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
        #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓转换为command↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓


        


        jsoninfo = json.dumps(info)
        info_text_file.write(jsoninfo+'\n')




