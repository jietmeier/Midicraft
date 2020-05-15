

def playsound(tick,note):

    file = open(f'ticknote/{tick}.mcfunction',mode='a')

    
    cmd = f'execute as @p at @s run playsound minecraft:piano.{note} record @a ~ ~ ~'

    file.write(cmd+'\n')

    file.close()