# To-Do-Manager-List

Modern Dark Theme with sleek styling
Dynamic Background with blur and gradient effects that resize with the window
Smooth Animations and hover effects
Custom Icons throughout the interface (📝✅🗑️📊)

Task Management

Add Tasks quickly with the input field or Enter key
Toggle Completion with visual checkboxes (⭕ → ✅)
Delete Tasks with confirmation dialog
Visual Feedback - completed tasks are grayed out and struck through
Persistent Storage - tasks automatically save and load

Progress Tracking

Real-time Statistics showing completion percentage
Task Counter displaying completed vs total tasks
Motivational Messages to keep you going
Live Date/Time display that updates every minute

Data Management

Auto-save every 30 seconds
Manual Save button for immediate backup
Automatic Loading of previous tasks on startup
Default Sample Tasks for new users
Safe Exit - saves tasks when closing the app

Getting Started
Prerequisites
Make sure you have Python 3.7+ installed on your system.
Required Dependencies
bashpip install customtkinter pillow
Installation

Clone or download this repository
Install dependencies using the command above
Add your background image at the specified path
Add your icon file


Run the application:
bashpython To-Do Manager List.py

Customization
Background Image
Replace the image path in the code:
pythonbackground_path = r"YOUR_IMAGE_PATH_HERE"
Window Icon
Update the icon path:
pythonapp.iconbitmap(r"YOUR_ICON_PATH_HERE")

How to Use
Adding Tasks

Type your task in the input field
Press Enter or click the "➕ Add" button
The button will briefly show "✅ Added!" as confirmation

Managing Tasks

Complete a task: Click the ⭕ circle to mark as done ✅
Undo completion: Click the ✅ checkmark to mark as pending ⭕
Delete a task: Click the 🗑️ trash icon (with confirmation)

Monitoring Progress

View completion statistics at the bottom
Track your progress percentage
Get motivated by the encouraging messages!

Technical Details
Built With

Python 3.7+
CustomTkinter - Modern UI framework
Pillow (PIL) - Image processing for background effects
Pickle - Data serialization for task storage
Tkinter - Base GUI framework

Key Components

Dynamic Background Processing with blur and brightness adjustment
Gradient Overlay for better text readability
Responsive Design that adapts to window resizing
Persistent Data Storage using pickle serialization
Real-time Updates for time, statistics, and auto-saving

File Structure
📁 Project Folder
├── 📄 todo_app.py          # Main application file
├── 📄 tasks.dat            # Auto-generated task storage file
├── 🖼️ background.jpg       # Your background image
└── 🔲 checklist.ico       # Window icon
🎛️ Default Settings

Window Size: 1000x700 pixels (resizable)
Theme: Dark mode with blue accents
Auto-save Interval: 30 seconds
Time Update: Every 10 minutes for display
Stats Update: Every second

Troubleshooting
Common Issues
"File not found" errors:

Ensure background image and icon files exist at specified paths
Update file paths in the code to match your system

Tasks not saving:

Check write permissions in the application directory
Ensure the tasks.dat file isn't locked by another process

Background not displaying:

Verify the background image path is correct
Ensure the image file is a supported format (JPG, PNG, etc.)

 Sample Tasks
The app comes with 6 sample tasks to get you started:

🛁 Have a relaxing bath
📧 Send important emails
🏃‍♂️ 30-minute workout
🛒 Buy fresh groceries
🐍 Study Python programming
📚 Read for 20 minutes

Contributing
Feel free to fork this project and submit pull requests for improvements! Some ideas for enhancement:

Task categories and filtering
Due dates and reminders
Export/import functionality
Themes and customization options
Task priority levels

License
This project is open source and available under the MIT License.
Acknowledgments

CustomTkinter team for the amazing modern UI framework
Pillow developers for powerful image processing capabilities
The Python community for excellent documentation and support


Tips for Best Experience

Use a high-resolution background image for best visual quality
Keep task descriptions concise for better readability
Regularly review your completed tasks for motivation
Use emojis in task names to make them more visually appealing
Resize the window to fit your workflow and screen size

Happy task managing! 
