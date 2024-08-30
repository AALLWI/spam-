import pyautogui
import pyperclip
import random
import time

print("Tool Spam 1.0")
msg = input("Masukkan konten yang akan di-spam: ").split(" || ")
n = int(input("Masukkan jumlah spam: "))
m = float(input("Masukkan waktu delay (dalam detik): "))

print("Persiapan")
# Hitung mundur 5 detik
for i in range(5, 0, -1):
    print(i, end="...", flush=True)
    time.sleep(1)
print("Mulai")

# SPAM
for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(m)  # Delay