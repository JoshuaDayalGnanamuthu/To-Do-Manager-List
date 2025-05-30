from PIL import Image, ImageFilter, ImageEnhance
import PIL.Image
import customtkinter
import datetime
import os
import tkinter as tk
from tkinter import messagebox
import pickle

background_path = r"\wallpapersden.com_the-foggy-forest-and-misty-pathway_3840x2150.jpg"

def load_tasks():
    default_tasks = [
        ("🛁 Have a relaxing bath", False),
        ("📧 Send important emails", False),
        ("🏃‍♂️ 30-minute workout", False),
        ("🛒 Buy fresh groceries", False),
        ("🐍 Study Python programming", False),
        ("📚 Read for 20 minutes", False)
    ]
    try:
        with open('tasks.dat', 'rb') as file:
            loaded_tasks = pickle.load(file)
            return loaded_tasks
        
    except (pickle.UnpicklingError, EOFError, FileNotFoundError) as e:
        return default_tasks

def save_tasks():
    try:
        tasks_to_save = [(task['text'], task['completed']) for task in tasks_data]
        with open('tasks.dat', 'wb') as file:
            pickle.dump(tasks_to_save, file)
    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save tasks: {e}")

sample_tasks = load_tasks()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def process_background_image(image_path):
    base_image = Image.open(image_path).convert("RGBA")
    blurred = base_image.filter(ImageFilter.GaussianBlur(radius=3))
    enhancer = ImageEnhance.Brightness(blurred)
    darkened = enhancer.enhance(0.3)    
    return darkened

processed_bg = process_background_image(background_path)

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("To-Do Manager List")
app.iconbitmap(r"\checklist.ico")
app.resizable(True, True)

tasks_data = []
animation_running = False

def create_gradient_overlay():
    overlay = Image.new('RGBA', (1000, 700), (0, 0, 0, 0))
    for y in range(700):
        alpha = int(60 * (y / 700))
        for x in range(1000):
            overlay.putpixel((x, y), (0, 0, 0, alpha))
    return overlay

def bg_resizer(e):
    if e.widget is app:
        resized_bg = processed_bg.resize((e.width, e.height), Image.Resampling.LANCZOS)
        gradient = create_gradient_overlay()
        gradient_resized = gradient.resize((e.width, e.height), Image.Resampling.LANCZOS)
        final_image = Image.alpha_composite(resized_bg, gradient_resized)
        i = customtkinter.CTkImage(final_image, size=(e.width, e.height))
        bg_lbl.configure(text="", image=i)

background_ctk_image = customtkinter.CTkImage(light_image=processed_bg, size=(1000, 700))
bg_lbl = customtkinter.CTkLabel(app, text="", image=background_ctk_image)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

main_container = customtkinter.CTkFrame(
    app,
    fg_color=("#1a1a1a", "#2d2d2d"),
    corner_radius=20,
    border_width=2,
    border_color=("#404040", "#505050")
)
main_container.pack(fill="both", expand=True, padx=30, pady=30)


header_frame = customtkinter.CTkFrame(
    main_container,
    fg_color="transparent",
    height=100
)
header_frame.pack(fill="x", padx=20, pady=(20, 10))

title_label = customtkinter.CTkLabel(
    header_frame,
    text=" My Tasks",
    font=customtkinter.CTkFont(family="Segoe UI", size=32, weight="bold"),
    text_color=("#ffffff", "#ffffff")
)
title_label.pack(side="left", padx=10)

def get_formatted_date():
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d • %I:%M %p")

date_button = customtkinter.CTkLabel(
    header_frame,
    text=get_formatted_date(),
    font=customtkinter.CTkFont(family="Segoe UI", size=16, weight="normal"),
    text_color=("#e0e0e0", "#b0b0b0")
)
date_button.pack(side="right", padx=10)

input_frame = customtkinter.CTkFrame(
    main_container,
    fg_color=("#0f0f0f", "#1f1f1f"),
    corner_radius=15,
    height=80
)
input_frame.pack(fill="x", padx=20, pady=10)

input_box = customtkinter.CTkEntry(
    input_frame,
    placeholder_text="✍️ What needs to be done?",
    font=customtkinter.CTkFont(family="Segoe UI", size=14),
    height=45,
    corner_radius=12,
    border_width=2,
    border_color=("#404040", "#505050"),
    fg_color=("#2a2a2a", "#3a3a3a")
)
input_box.pack(side="left", fill="x", expand=True, padx=15, pady=17)

def add_task():
    task_text = input_box.get().strip()
    if task_text:
        create_task_item(task_text, completed=False)
        input_box.delete(0, tk.END)
        add_btn.configure(text="✅ Added!")
        app.after(1000, lambda: add_btn.configure(text="➕ Add"))      
        save_tasks()

add_btn = customtkinter.CTkButton(
    input_frame,
    text="➕ Add",
    font=customtkinter.CTkFont(family="Segoe UI", size=14, weight="bold"),
    width=100,
    height=45,
    corner_radius=12,
    fg_color=("#3b82f6", "#2563eb"),
    hover_color=("#2563eb", "#1d4ed8"),
    command=add_task
)
add_btn.pack(side="right", padx=15, pady=17)

tasks_frame = customtkinter.CTkScrollableFrame(
    main_container,
    fg_color="transparent",
    corner_radius=15,
    scrollbar_button_color="#4a5568",
    scrollbar_button_hover_color="#718096"
)
tasks_frame.pack(fill="both", expand=True, padx=20, pady=10)

def create_task_item(task_text, completed=False):
    task_container = customtkinter.CTkFrame(
        tasks_frame,
        fg_color=("#1a1a1a", "#2a2a2a"),
        corner_radius=12,
        height=60,
        border_width=1,
        border_color=("#3a3a3a", "#4a4a4a")
    )
    task_container.pack(fill="x", pady=5, padx=5)

    task_data = {
        'text': task_text,
        'completed': completed,
        'container': task_container
    }
    tasks_data.append(task_data)
    
    checkbox_text = "✅" if completed else "⭕"
    checkbox = customtkinter.CTkButton(
        task_container,
        text=checkbox_text,
        font=customtkinter.CTkFont(size=20),
        width=40,
        height=40,
        corner_radius=20,
        fg_color="transparent",
        hover_color=("#2a2a2a", "#3a3a3a"),
        command=lambda: toggle_task(task_data)
    )
    checkbox.pack(side="left", padx=15, pady=10)
    
    text_color = "#a0a0a0" if completed else "#ffffff"
    font_weight = "normal" if completed else "bold"  
    display_text = f"~~{task_text}~~" if completed else task_text
    
    task_label = customtkinter.CTkLabel(
        task_container,
        text=display_text,
        font=customtkinter.CTkFont(family="Segoe UI", size=14, weight=font_weight),
        text_color=text_color,
        anchor="w"
    )
    task_label.pack(side="left", fill="x", expand=True, padx=10, pady=10)
    
    delete_btn = customtkinter.CTkButton(
        task_container,
        text="🗑️",
        font=customtkinter.CTkFont(size=16),
        width=35,
        height=35,
        corner_radius=17,
        fg_color="transparent",
        hover_color=("#ef4444", "#dc2626"),
        command=lambda: delete_task(task_data)
    )
    delete_btn.pack(side="right", padx=15, pady=12)
    
    task_data['checkbox'] = checkbox
    task_data['label'] = task_label
    task_data['delete_btn'] = delete_btn

def toggle_task(task_data):
    task_data['completed'] = not task_data['completed']
    
    checkbox_text = "✅" if task_data['completed'] else "⭕"
    task_data['checkbox'].configure(text=checkbox_text)
    
    text_color = "#a0a0a0" if task_data['completed'] else "#ffffff"
    font_weight = "normal" if task_data['completed'] else "bold"
    
    display_text = f"~~{task_data['text']}~~" if task_data['completed'] else task_data['text']
    
    task_data['label'].configure(
        text=display_text,
        text_color=text_color,
        font=customtkinter.CTkFont(family="Segoe UI", size=14, weight=font_weight)
    )
    save_tasks()

def delete_task(task_data):
    result = messagebox.askyesno("Delete Task", f"Are you sure you want to delete '{task_data['text']}'?")
    if result:
        task_data['container'].destroy()
        tasks_data.remove(task_data)  
        save_tasks()

def update_date_time():
    date_button.configure(text=get_formatted_date())
    app.after(600, update_date_time)

for task_text, completed in sample_tasks:
    create_task_item(task_text, completed)

input_box.bind("<Return>", lambda e: add_task())
app.after(0, update_date_time)
app.bind("<Configure>", bg_resizer)
stats_frame = customtkinter.CTkFrame(
    main_container,
    fg_color="transparent",
    height=40
)
stats_frame.pack(fill="x", padx=20, pady=(10, 20))

def update_stats():
    total_tasks = len(tasks_data)
    completed_tasks = sum(1 for task in tasks_data if task['completed'])
    stats_text = f"📊 {completed_tasks}/{total_tasks} tasks completed"
    if total_tasks > 0:
        percentage = (completed_tasks / total_tasks) * 100
        stats_text += f" • {percentage:.0f}% done"
    try:
        stats_label.configure(text=stats_text)
    except:
        pass
    app.after(1000, update_stats)

stats_label = customtkinter.CTkLabel(
    stats_frame,
    text="📊 0/0 tasks completed",
    font=customtkinter.CTkFont(family="Segoe UI", size=12),
    text_color=("#c0c0c0", "#808080")
)
stats_label.pack(side="left", padx=10)

motivation_label = customtkinter.CTkLabel(
    stats_frame,
    text=" You've got this!",
    font=customtkinter.CTkFont(family="Segoe UI", size=12, weight="bold"),
    text_color=("#60a5fa", "#3b82f6")
)
motivation_label.pack(side="right", padx=10)

app.after(1000, update_stats)

def manual_save():
    save_tasks()
    messagebox.showinfo("Saved", "Tasks saved successfully!")

save_btn = customtkinter.CTkButton(
    stats_frame,
    text="💾 Save",
    font=customtkinter.CTkFont(family="Segoe UI", size=12, weight="bold"),
    width=80,
    height=30,
    corner_radius=8,
    fg_color=("#16a34a", "#15803d"),
    hover_color=("#15803d", "#166534"),
    command=manual_save
)
save_btn.pack(side="right", padx=10)

def on_closing():
    save_tasks()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)

def auto_save():
    save_tasks()
    app.after(30000, auto_save)

app.after(30000, auto_save)
app.mainloop()


