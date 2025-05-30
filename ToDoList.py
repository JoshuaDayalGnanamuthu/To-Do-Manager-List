from PIL import Image
import PIL.Image
import customtkinter
import datetime
import os

# Set file paths
background_path = r"C:\Users\joshu\Downloads\wallpapersden.com_the-foggy-forest-and-misty-pathway_3840x2150.jpg"
icon_path = r"C:\Users\joshu\Downloads\checklist.ico"

# File validation
if not os.path.exists(background_path):
    raise FileNotFoundError(f"Background image not found: {background_path}")
if not os.path.exists(icon_path):
    raise FileNotFoundError(f"Icon file not found: {icon_path}")

# Initialize app
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

base_image = Image.open(background_path).convert("RGBA")

app = customtkinter.CTk()
app.geometry("900x650")
app.title("To-Do List")
app.iconbitmap(icon_path)

# Function to resize background

def bg_resizer(e):
    if e.widget is app:
        resized_image = customtkinter.CTkImage(image, size=(e.width, e.height))
        bg_lbl.configure(text="", image=resized_image)

# Set up background
image = PIL.Image.open(background_path)
background_ctk_image = customtkinter.CTkImage(light_image=base_image, size=(900, 650))
bg_lbl = customtkinter.CTkLabel(app, text="", image=background_ctk_image)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

# Date display button
def update_date():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%A, %d %B  %I:%M %p")
    date_button.configure(text=formatted_date)
    app.after(1000, update_date)

date_button = customtkinter.CTkButton(
    app,
    font=customtkinter.CTkFont(weight="bold", family='Segoe UI', size=24),
    text_color='#ffffff',
    fg_color='transparent',
    border_spacing=30,
    height=50,
    corner_radius=10,
    border_width=3,
    hover='disabled',
    anchor='center')
date_button.pack(fill='x', padx=25, pady=(20, 10))
update_date()

# Input box for new tasks
input_box = customtkinter.CTkEntry(
    app,
    width=800,
    height=40,
    corner_radius=10,
    placeholder_text="Enter a task here...",
    font=customtkinter.CTkFont(family='Segoe UI', size=16)
)
input_box.pack(fill='x', padx=25, pady=(0, 20))

# Scrollable task container
frame = customtkinter.CTkScrollableFrame(
    app,
    width=800,
    height=400,
    corner_radius=15,
    border_width=3,
    fg_color='transparent'
)
frame.pack(fill="both", padx=25, pady=(0, 25), expand=True)

# Toggle function
def button_clicked(button):
    current_text = button.cget("text")
    if current_text.startswith('☐'):
        button.configure(text=current_text.replace('☐', '✅', 1), text_color='#90ee90')
    else:
        button.configure(text=current_text.replace('✅', '☐', 1), text_color='#ffffff')

# Predefined tasks
tasks = [
    "Have Bath",
    "Send Mail",
    "Exercise",
    "Buy Groceries",
    "Study Python",
    "Read Book"
]

# Render checkboxes
checkboxes = []

for task in tasks:
    checkbox = customtkinter.CTkButton(
        frame,
        font=customtkinter.CTkFont(weight="bold", family='Segoe UI', size=16),
        text=f'☐ {task}',
        text_color='#ffffff',
        fg_color='transparent',
        height=45,
        border_spacing=15,
        border_width=2,
        corner_radius=12,
        anchor='w'
    )
    checkbox.configure(command=lambda btn=checkbox: button_clicked(btn))
    checkbox.pack(fill='x', pady=8, padx=5)
    checkboxes.append(checkbox)

# Final bindings
app.bind("<Configure>", bg_resizer)
app.mainloop()
