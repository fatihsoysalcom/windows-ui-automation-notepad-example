# Windows UI Automation Notepad Example

This example demonstrates how to use Windows UI Automation (UIA) via the `pywinauto` library to interact with desktop applications. It opens Notepad, types text into its editor, navigates the 'File' menu to 'Exit', and then handles the 'Save Changes' dialog by clicking 'Don't Save'. This approach is more robust than coordinate-based automation, as it identifies UI elements by their properties (like name or control type) rather than their pixel location.

## Language

`python`

## How to Run

1. Ensure Python is installed on your Windows machine.
2. Install the `pywinauto` library: `pip install pywinauto`
3. Run the script from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Yapay Zeka Ajanım Düğmeleri Kaçırınca: Windows UI Otomasyonu ile Çözüm](https://fatihsoysal.com/blog/yapay-zeka-ajanim-dugmeleri-kacirinca-windows-ui-otomasyonu-ile-cozum/).

## License

MIT — see [LICENSE](LICENSE).
