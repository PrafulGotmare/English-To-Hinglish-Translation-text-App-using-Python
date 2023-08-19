import tkinter as tk
from mtranslate import translate

class HinglishTranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hinglish Translation App")
        
        self.input_label = tk.Label(root, text="Enter English text:")
        self.input_label.pack()

        self.input_text = tk.Text(root, height=5, width=40)
        self.input_text.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        self.result_label = tk.Label(root, text="Hinglish Translation:")
        self.result_label.pack()

        self.result_text = tk.Text(root, height=5, width=40)
        self.result_text.pack()

    def translate_text(self):
        input_text = self.input_text.get("1.0", "end-1c")
        hinglish_translation = translate(input_text, to_language='hi', from_language='en')
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", hinglish_translation)

def main():
    root = tk.Tk()
    app = HinglishTranslationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
