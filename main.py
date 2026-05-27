import time
import subprocess
from pywinauto import Application

def main():
    print("Starting Notepad...")
    # Start Notepad application. subprocess.Popen is a robust way to launch.
    subprocess.Popen("notepad.exe")
    time.sleep(2) # Give Notepad some time to open

    try:
        # Connect to the Notepad application using the UIA backend.
        # UIA allows finding windows by their title or class name, making it robust.
        app = Application(backend="uia").connect(title_re=".*Notepad", class_name="Notepad")
        notepad_window = app.window(title_re=".*Notepad")

        print("Notepad window found. Maximizing...")
        notepad_window.maximize()
        time.sleep(1)

        # Find the text edit control within Notepad.
        # UIA identifies controls by their type, which is more reliable than coordinates.
        edit_control = notepad_window.child_window(control_type="Edit")
        print("Typing text into Notepad...")
        edit_control.type_keys("Hello from Windows UI Automation!{ENTER}This text was typed by an AI agent using UIA.{ENTER}")
        time.sleep(2)

        # Click the "File" menu.
        # UIA uses the 'Name' property (the displayed text) to find menu items.
        print("Clicking 'File' menu...")
        file_menu = notepad_window.child_window(title="File", control_type="MenuItem")
        file_menu.click_input()
        time.sleep(1)

        # Click the "Exit" menu item.
        print("Clicking 'Exit' menu item...")
        exit_menu_item = notepad_window.child_window(title="Exit", control_type="MenuItem")
        exit_menu_item.click_input()
        time.sleep(1)

        # Handle the "Save Changes" dialog.
        # UIA can connect to new dialog windows that appear, again using title/class.
        print("Handling 'Save Changes' dialog...")
        save_dialog = app.window(title="Notepad", class_name="#32770") # #32770 is a common class for dialogs

        # Click the "Don't Save" button.
        # Buttons are found by their 'Name' property, ensuring interaction even if position shifts.
        dont_save_button = save_dialog.child_window(title="Don't Save", control_type="Button")
        dont_save_button.click_input()
        print("Clicked 'Don't Save'. Notepad should close.")

    except Exception as e:
        print(f"An error occurred during automation: {e}")
        # Attempt to close Notepad if it's still open after an error
        try:
            app = Application(backend="uia").connect(title_re=".*Notepad", class_name="Notepad")
            notepad_window = app.window(title_re=".*Notepad")
            notepad_window.close()
        except:
            pass # Notepad might already be closed or not found

    print("Windows UI Automation demonstration finished.")

if __name__ == "__main__":
    main()
