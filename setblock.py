(x,y,z)=(0,20,0)

file = open('cmd.mcfunction',mode='w')
i=0
while i<=5264:
    i+=1
    if(i%2==0):
        cmd = f'setblock {int(x+i/2)} {y} {z} chain_command_block[facing=down,conditional=false]{{auto:1,Command:"execute as @p run function custom:ticknote/{i}"}}'
        movec = f'setblock {int(x+i/2)} {y+1} {z} command_block[facing=down,conditional=false]{{Command:"clone ~ ~1 ~ ~ ~1 ~ ~ ~1 ~1 replace move"}}'
    else:
        cmd = f'setblock {int(x+(i-1)/2)} {y} {z+1} chain_command_block[facing=down,conditional=false]{{auto:1,Command:"execute as @p run function custom:ticknote/{i}"}}'
        movec = f'setblock {int(x+i/2)} {y+1} {z+1} command_block[facing=down,conditional=false]{{Command:"clone ~ ~1 ~ ~ ~1 ~ ~1 ~1 ~-1 replace move"}}'
    file.write(movec+'\n')
    file.write(cmd+'\n')
file.close()