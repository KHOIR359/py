import itertools
import threading
import time
import sys
import os


os.system('clear')
os.system('color 2')

print('''


    __ __ __          _         ______       __               __            
   / //_// /_  ____  (_)____   / __/ /_     / /_  ____ ______/ /_____  _____
  / ,<  / __ \/ __ \/ / ___/  / /_/ __ \   / __ \/ __ `/ ___/ //_/ _ \/ ___/
 / /| |/ / / / /_/ / / /     / __/ /_/ /  / / / / /_/ / /__/ ,< /  __/ /    
/_/ |_/_/ /_/\____/_/_/     /_/ /_.___/  /_/ /_/\__,_/\___/_/|_|\___/_/     
                                                                            
Peringatan sebelum menggunakan:
1. Hanya dapat digunakan untuk akun yang jarang aktif
2. Jika terdeteksi kemungkinan besar akun bisa dibanned
3. Pastikan untuk hapus activity log di facebook korban
4. Ubah activity privacy ke private untuk sementara                                                          
''')


input('Target >> ')

done = False
# here is the animation


def animate():
    for c in itertools.cycle(['|.', '/..', '-...', '\\....']):
        if done:
            break
        sys.stdout.write('\rHacking ' + c)
        # sys.stdout.flush()
        time.sleep(.1)
    # sys.stdout.write('\rDone!     ')
    sys.stdout.write('''\r+----------+----------------------------+
| Username  | khoir359                  |
+----------+----------------------------+
| Password  | testnantigantipassword    |
+----------+----------------------------+
| Email     | khoir359@gmail.com        |
+----------+----------------------------+
| Name      | Ini Khoir                 |
+----------+----------------------------+
''')


t = threading.Thread(target=animate)
t.start()

# long process here
time.sleep(5)
done = True
