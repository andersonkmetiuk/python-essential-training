from datetime import datetime

wait_until= datetime.now().second + 2

while datetime.now().second != wait_until:
    pass #print('still waiting...') - pass is just statement to do nothing
print(f'we are at {wait_until} seconds...')

print('\n\n')
wait_until= datetime.now().second + 2
while True:
    if datetime.now().second < wait_until:
        print('hey')
        continue
    break

print('end')