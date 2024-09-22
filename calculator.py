from RPA.Windows import Windows
import time

library = Windows()

def test_do_some_calculations():
    library.windows_run("calc.exe")
    try:
        library.control_window("name:Calculator")
        library.click("id:clearButton")
        library.send_keys(keys="96+4=")
        
        # Wait for a moment to see the calculation happen
        time.sleep(1)  
        
        result = library.get_attribute("id:CalculatorResults", "Name")
        print(f"Result: {result}")
        time.sleep(1)
        
        # Print out the buttons on the number pad
        buttons = library.get_elements('type:Group and name:"Number pad" > type:Button')
        for button in buttons:
            print(button)
        library.close_current_window()
    finally:
        library.close_current_window()

if __name__ == "__main__":
    test_do_some_calculations()
