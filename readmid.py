import mido
import json

midi_file = 'Home'




####################
midi_path = f'mid/{midi_file}.mid'
info_text_path = f'midi_info/{midi_file}.txt'

info_text_file = open(info_text_path,mode='w')#创建info_file对象
midi_object=mido.MidiFile(midi_path)#创建midi对象

####################





for i,track in enumerate(midi_object.tracks): #第i条音轨
    # print(f'track{i}')
    info_text_file.write(f'track{i}:\n')

    list_time = 0
    for msg in track: #音轨中的信息
        info = msg.dict()

        # if info['type'] == 'control_change':
        #     continue

        info['pertime']=info['time']
        info['time'] += list_time
        list_time = info['time']


        try:
            del info['velocity']
        except:
            pass

        try:
            del info['channel']
        except:
            pass

        
        
            
##################################################################################

            

        jsoninfo = json.dumps(info)
        info_text_file.write(jsoninfo+'\n')


        

