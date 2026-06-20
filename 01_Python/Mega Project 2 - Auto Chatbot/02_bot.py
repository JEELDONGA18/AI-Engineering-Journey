import pyautogui
import time
import pyperclip

# Wait for 3 seconds to give you time to switch to the correct window
time.sleep(7)

# Click on the icon at (1153, 1043)
pyautogui.click(822, 1041) 

# Wait for a short duration to ensure the click is registered
time.sleep(0.5)

# Move to the start position (672, 258)
pyautogui.moveTo(672, 258)

# Click and hold the mouse button down
pyautogui.mouseDown()

# Drag to the end position (1866, 885)
pyautogui.moveTo(1866, 885, duration=1)  # duration is optional, for a smoother movement

# Release the mouse button
pyautogui.mouseUp()

# Wait for a short duration to ensure the selection is made
time.sleep(0.5)

# Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(672,258)

# Wait for a short duration to ensure the text is copied
time.sleep(0.5)

# Get the copied text from the clipboard
copied_text = pyperclip.paste()

# Print the copied text (for verification)
print(copied_text)
