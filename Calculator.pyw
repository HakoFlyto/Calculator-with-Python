# Made By Hakoflyto
# --------------------------------------------------
# Tkinter kullanarak basit bir hesap makinesi oluşturma
# Creating a simple calculator using Tkinter
# --------------------------------------------------

import tkinter as tk                # Tkinter modülünü içe aktarıyoruz // Import the tkinter module
from tkinter import font            # Font modülünü içe aktarıyoruz // Import the font module from tkinter
import webbrowser                   # Web tarayıcısını açmak için webbrowser modülünü içe aktarıyoruz // Import the webbrowser module for opening web links

# Ana pencereyi oluşturma
# Create the main window
pencere = tk.Tk()                   # Tkinter ana pencere nesnesini oluşturuyoruz // Create the main Tkinter window object
pencere.title("Hesap Makinesi")     # Pencere başlığını ayarlıyoruz // Set the window title to "Hesap Makinesi" (Calculator)
pencere.geometry("400x600")         # Pencere boyutunu 400x600 piksel olarak sabitliyoruz // Fix the window size to 400x600 pixels
pencere.config(bg="black")          # Arka plan rengini siyah yapıyoruz // Set the background color to black
pencere.resizable(False, False)     # Pencerenin yatay ve dikey olarak yeniden boyutlandırılmasını engelliyoruz // Prevent the window from being resizable horizontally and vertically

# Font objesini tanımlama
# Define the font object
font_comic = font.Font(family="Comic Sans MS", size=28)  # "Comic Sans MS" fontunu, boyutu 28 olarak tanımlıyoruz // Define the "Comic Sans MS" font with size 28

# Ekranı (giriş alanı) oluşturma
# Create the display (input field)
ekran = tk.Entry(pencere, font=font_comic, fg="white", bg="black", bd=10, relief="sunken", justify="right")
ekran.grid(row=0, column=0, columnspan=4, sticky="nsew", ipadx=10, ipady=15)
# Entry widget’ını grid düzeni ile yerleştiriyoruz, 4 sütun kaplar // Place the Entry widget using grid layout, spanning 4 columns

# Fonksiyonlar (Functions)
def buton_tikla(deger):
    # Butona tıklandığında değeri ekrana ekler // Appends the button's value to the display when clicked
    ekran.insert(tk.END, deger)

def temizle():
    # Ekranı temizler // Clears the display
    ekran.delete(0, tk.END)

def hesapla():
    # Ekranda girilen ifadeyi hesaplar // Evaluates the expression entered in the display
    try:
        ifade = ekran.get()          # Ekrandaki ifadeyi alıyoruz // Retrieve the expression from the display
        sonuc = eval(ifade)           # Python’un eval fonksiyonu ile ifadeyi hesaplıyoruz // Calculate the expression using Python's eval function
        ekran.delete(0, tk.END)       # Önceki ifadeyi temizliyoruz // Clear the display before showing the result
        ekran.insert(tk.END, str(sonuc))  # Hesaplanan sonucu ekrana yazdırıyoruz // Insert the calculated result into the display
    except Exception:
        ekran.delete(0, tk.END)
        ekran.insert(tk.END, "Hata")  # Hata durumunda "Hata" mesajını gösteriyoruz // Display "Hata" (Error) in case of an exception

def enter_basi(event=None):
    # Enter tuşuna basıldığında hesapla fonksiyonunu çalıştırır // Triggers the calculate function when the Enter key is pressed
    hesapla()

def backspace(event=None):
    # Backspace tuşuyla son karakteri siler // Deletes the last character when Backspace is pressed
    ekran.delete(len(ekran.get()) - 1, tk.END)

def klavye_tusla(event):
    # Klavyeden basılan tuşları ekrana yansıtır // Reflects keyboard key presses on the display
    tus = event.char             # Basılan tuşu alıyoruz // Get the character of the key pressed
    if tus.isdigit() or tus in "+-*/.":
        # Eğer tuş rakam veya matematiksel operatör ise ekrana ekle // If the key is a digit or a mathematical operator, append it to the display
        buton_tikla(tus)

# Butonları oluşturma ve yerleştirme (Creating and placing buttons)
butonlar = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)  # Temizle butonu // Clear button
]

for (metin, satir, sutun) in butonlar:
    # Her buton için işlemleri tanımlıyoruz // Define actions for each button
    if metin == '=':
        # "=" butonuna basıldığında hesapla fonksiyonunu çağırır // The "=" button calls the calculate function
        buton = tk.Button(pencere, text=metin, font=font_comic, fg="white", bg="black", command=hesapla)
    elif metin == 'C':
        # "C" butonuna basıldığında temizle fonksiyonunu çağırır // The "C" button calls the clear function
        buton = tk.Button(pencere, text=metin, font=font_comic, fg="white", bg="black", command=temizle)
    else:
        # Diğer butonlar için ilgili karakteri ekrana ekleyecek fonksiyonu çağırır // For other buttons, calls the function to append the character to the display
        buton = tk.Button(pencere, text=metin, font=font_comic, fg="white", bg="black",
                          command=lambda metin=metin: buton_tikla(metin))
    buton.grid(row=satir, column=sutun, padx=5, pady=5, sticky="nsew")
    # Butonları grid düzeni ile yerleştiriyoruz, her birine padding ekliyoruz // Place each button in the grid layout with padding

# Alt yazı (Footer/Label) oluşturma - Tıklanınca YouTube Linkine Gitsin
# Create a footer label that opens a YouTube link when clicked
def hakoFlyto_linki(event=None):
    # Web tarayıcısını açarak YouTube kanalına yönlendirir // Opens the web browser and navigates to the YouTube channel
    webbrowser.open("https://www.youtube.com/@hakoflyto")

alt_yazi = tk.Label(pencere, text="Created By HakoFlyto", font=font_comic, fg="white", bg="black", cursor="hand2")
alt_yazi.grid(row=6, column=0, columnspan=4, sticky="nsew")
# Label’ı grid düzeni ile yerleştiriyoruz, 4 sütun kaplar // Place the label in the grid layout, spanning 4 columns
alt_yazi.bind("<Button-1>", hakoFlyto_linki)  # Label’e tıklanırsa YouTube linkini açar // Bind a mouse click on the label to open the YouTube link

# Grid Ayarları (Grid Configuration)
for i in range(6):
    pencere.grid_rowconfigure(i, weight=1)   # Her satıra eşit genişleme payı veriyoruz // Give each row an equal expansion weight
for i in range(4):
    pencere.grid_columnconfigure(i, weight=1)  # Her sütuna eşit genişleme payı veriyoruz // Give each column an equal expansion weight

# Klavye Tuşlarını Bağlama (Keyboard Bindings)
pencere.bind("<Return>", enter_basi)       # Enter tuşuna basıldığında hesapla fonksiyonunu çağırır // Bind the Enter key to the calculate function
pencere.bind("<BackSpace>", backspace)       # Backspace tuşuna basıldığında son karakteri siler // Bind the Backspace key to delete the last character
pencere.bind("<Delete>", lambda event: temizle())  # Delete tuşuna basıldığında ekranı temizler // Bind the Delete key to clear the display
pencere.bind("<Key>", klavye_tusla)          # Diğer klavye tuşlarına basıldığında klavye_tusla fonksiyonunu çalıştırır // Bind other key presses to the klavye_tusla function

# Uygulamayı Başlatma (Start the Application)
pencere.mainloop()  # Tkinter döngüsünü başlatarak uygulamayı çalıştırır // Start the Tkinter main loop to run the application
