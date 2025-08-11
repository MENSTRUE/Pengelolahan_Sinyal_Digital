import cv2
import numpy as np
from tkinter import filedialog, Tk, Button, Label
from PIL import Image, ImageTk

class ImageProcessor:
    def __init__(self):
        self.root = Tk()
        self.root.title("Operasi Penjumlahan dan Perbesaran Citra")

        self.image1 = None
        self.image2 = None
        self.result = None

        Button(self.root, text="Pilih Gambar 1", command=self.load_image1).pack(pady=5)
        Button(self.root, text="Pilih Gambar 2", command=self.load_image2).pack(pady=5)
        Button(self.root, text="Jumlahkan Gambar", command=self.add_images).pack(pady=5)
        Button(self.root, text="Perbesar Gambar Hasil", command=self.zoom_image).pack(pady=5)

        self.label = Label(self.root)
        self.label.pack()

        print("GUI dijalankan...")

        
        self.root.mainloop()

    def load_image1(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if path:
            self.image1 = cv2.imread(path)
            self.image1 = cv2.resize(self.image1, (300, 300))
            self.display_image(self.image1, "Gambar 1")

    def load_image2(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if path:
            self.image2 = cv2.imread(path)
            self.image2 = cv2.resize(self.image2, (300, 300))
            self.display_image(self.image2, "Gambar 2")

    def add_images(self):
        if self.image1 is not None and self.image2 is not None:
            self.result = cv2.addWeighted(self.image1, 0.5, self.image2, 0.5, 0)
            self.display_image(self.result, "Hasil Penjumlahan")

    def zoom_image(self, scale=2):
        if self.result is not None:
            height, width = self.result.shape[:2]
            zoomed = cv2.resize(self.result, (width * scale, height * scale), interpolation=cv2.INTER_LINEAR)
            self.display_image(zoomed, "Hasil Perbesaran")

    def display_image(self, img, title="Image"):
        # Konversi BGR ke RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img_rgb)
        imgtk = ImageTk.PhotoImage(image=im)
        self.label.config(image=imgtk)
        self.label.image = imgtk
        self.root.title(title)

# Jalankan aplikasi GUI
if __name__ == "__main__":
    ImageProcessor()
