# Задание 1

durations = [59, 62, 125, 3601]  # Промежутки времени в секундах

for dur in durations:
    if dur < 60:
        print('duration =', dur)
        print(dur, 'seconds\n')
    else:
        if 60 <= dur:
            print('duration =', dur)
            print(dur // 60, 'minutes', dur % 60, 'seconds\n')
