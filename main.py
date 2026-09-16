import tkinter as tk
import requests
import json

def fetch_data():
    post_id = id_entry.get()
    
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    data = response.json()

    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, json.dumps(data, indent=4))

def save_data():
    content = text_area.get(1.0, tk.END)
    
    with open("saved_data.json", "w", encoding="utf-8") as file:
        file.write(content)
    
    save_btn.config(text="Сохранено!")

root = tk.Tk()
root.title("JSON API")
root.geometry("400x450")

tk.Label(root, text="Введите ID:").pack(pady=5)
id_entry = tk.Entry(root)
id_entry.pack(pady=5)

tk.Button(root, text="Получить данные", command=fetch_data).pack(pady=10)

text_area = tk.Text(root, height=15, width=40)
text_area.pack(pady=5)

save_btn = tk.Button(root, text="Сохранить в папку", command=save_data)
save_btn.pack(pady=10)

root.mainloop()