import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer App")

        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.prev_button = tk.Button(root, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(root, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT)

        self.zoom_in_button = tk.Button(root, text="Zoom In", command=self.zoom_in)
        self.zoom_in_button.pack(side=tk.LEFT)

        self.zoom_out_button = tk.Button(root, text="Zoom Out", command=self.zoom_out)
        self.zoom_out_button.pack(side=tk.RIGHT)

        self.current_image_index = -1
        self.image_list = []
        self.zoom_factor = 1.0

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            self.image_list.append(image)
            self.current_image_index = len(self.image_list) - 1
            self.display_image(image)

    def display_image(self, image):
        self.canvas.delete("all")  # Clear previous image
        width = int(image.width * self.zoom_factor)
        height = int(image.height * self.zoom_factor)
        image = image.resize((width, height))
        self.img = ImageTk.PhotoImage(image=image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def show_previous_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.display_image(self.image_list[self.current_image_index])

    def show_next_image(self):
        if self.current_image_index < len(self.image_list) - 1:
            self.current_image_index += 1
            self.display_image(self.image_list[self.current_image_index])

    def zoom_in(self):
        self.zoom_factor += 0.1
        self.update_zoom()

    def zoom_out(self):
        if self.zoom_factor > 0.1:
            self.zoom_factor -= 0.1
            self.update_zoom()

    def update_zoom(self):
        if self.current_image_index != -1:
            image = self.image_list[self.current_image_index]
            self.display_image(image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()
