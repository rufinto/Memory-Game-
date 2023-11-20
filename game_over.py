import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to be called when the user clicks on the image


def game_over(result:bool):
    if result:
        image_path = 
    else:
        image_path=play_again.PNG
    def on_image_click(event):
        if event.x < 495:
            main()
        else:
            window.close()

# Function to be called when the top part of the image is clicked
# Main function to create the Tkinter GUI

    def create_gui():
        # Create the main window
        window = tk.Tk()
        window.title("Clickable Image")

        # Load the image from the current directory
        image = Image.open(image_path)

        # Convert the image to Tkinter PhotoImage format
        tk_image = ImageTk.PhotoImage(image)

        # Create a canvas to display the image
        canvas = tk.Canvas(window, width=tk_image.width(),
                           height=tk_image.height())
        canvas.pack()

        # Display the image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

        # Bind click events on the canvas to the on_image_click function
        canvas.bind("<Button-1>", on_image_click)

        # Run the Tkinter main loop
        window.mainloop()

    # Run the GUI
    create_gui()
