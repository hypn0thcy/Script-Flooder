try:
	import time
	import pyautogui
	import pyautogui as youtube
	import os
except exception:
	os.system('pip install pyautogui')

print("\n    -> @Created BY: hypn0thcy <- ")
print("               #AoGiri"            )

frase = str(input("\n\n[!] Oque você deseja floodar?: "))

tmp = float(input("\n[!] A cada quanto tempo?(RECOMENDADO 0.3): "))

loop = 10

try:
    while loop > 9:
        pyautogui.write(frase)
        time.sleep(tmp)
        pyautogui.press('enter')
        print("[*] -> Flodando!...")
except KeyboardInterrupt:
    print("\n        [=] Até Mais! ^^ [=]")
