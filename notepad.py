from RPA.Windows import Windows
import time

# Initialize the Windows library
windows = Windows()

# Open Notepad
windows.windows_run('notepad.exe')

# Type the desired text using send_keys
text_to_enter = "Hello, this is a sample text."
windows.send_keys("name: Text editor", text_to_enter)


# Save the text using Ctrl + S
windows.send_keys("name: Text editor", "{CTRL}s")
time.sleep(1)  # Wait for the save dialog to open

windows.control_window("name: Save as")
windows.send_keys(locator="id:1001", keys="{CTRL}a{DEL}")

name="presentation1"
print(name)

windows.send_keys(locator='id:1001', keys=name,wait_time=1,send_enter=True)

# Wait a moment for the file to be saved
time.sleep(1)
windows.control_window("class:Notepad")

# Take a screenshot
screenshot_path = 'notepad_screenshot.png'
windows.screenshot("name: Text editor",screenshot_path)


# Close Notepad
windows.close_current_window()

print(f'Screenshot saved as: {screenshot_path}')
