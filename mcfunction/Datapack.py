from os import makedirs

def create(name):

    data_pack = name
    path=f'{data_pack}/data/custom/functions/test'

    try:
        makedirs(path)
    except:
        pass

    file = open(f'{data_pack}/pack.mcmeta','w')
    file.write(f'''{{
    "pack": {{
        "pack_format": 5,
        "description": "JietMeier's {data_pack} datapack!"
        }}
    }}''')
    file.close()

create('rsm')






