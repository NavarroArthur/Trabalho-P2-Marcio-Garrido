import tkinter as tk
from tkinter import messagebox, simpledialog
from binaria import BSTNode

class BSTApp:
    def __init__(self, master):
        self.master = master
        master.title("Árvore Binária de Busca (BST)")
        self.tree = None

        # Frame de entrada
        self.entry_frame = tk.Frame(master)
        self.entry_frame.pack(pady=10)

        self.key_label = tk.Label(self.entry_frame, text="Chave:")
        self.key_label.pack(side=tk.LEFT)
        self.key_entry = tk.Entry(self.entry_frame, width=10)
        self.key_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.entry_frame, text="Inserir", command=self.add_key)
        self.add_button.pack(side=tk.LEFT, padx=2)
        self.remove_button = tk.Button(self.entry_frame, text="Remover", command=self.remove_key)
        self.remove_button.pack(side=tk.LEFT, padx=2)
        self.search_button = tk.Button(self.entry_frame, text="Buscar", command=self.search_key)
        self.search_button.pack(side=tk.LEFT, padx=2)

        # Área de exibição da árvore
        self.tree_text = tk.Text(master, height=20, width=50, font=("Courier", 10))
        self.tree_text.pack(pady=10)
        self.update_tree_display()

    def add_key(self):
        key = self.key_entry.get().strip()
        if not key:
            messagebox.showwarning("Aviso", "Digite uma chave para inserir.")
            return
        if self.tree is None:
            self.tree = BSTNode(key)
        else:
            self.tree.add(key)
        self.update_tree_display()
        self.key_entry.delete(0, tk.END)

    def remove_key(self):
        key = self.key_entry.get().strip()
        if not key:
            messagebox.showwarning("Aviso", "Digite uma chave para remover.")
            return
        if self.tree is None:
            messagebox.showinfo("Info", "A árvore está vazia.")
            return
        self.tree = self.tree.remove(key)
        self.update_tree_display()
        self.key_entry.delete(0, tk.END)

    def search_key(self):
        key = self.key_entry.get().strip()
        if not key:
            messagebox.showwarning("Aviso", "Digite uma chave para buscar.")
            return
        if self.tree is None:
            messagebox.showinfo("Info", "A árvore está vazia.")
            return
        node = self.tree.get(key)
        if node:
            messagebox.showinfo("Encontrado", f"Chave '{key}' encontrada na árvore.")
        else:
            messagebox.showinfo("Não encontrado", f"Chave '{key}' não está na árvore.")

    def update_tree_display(self):
        self.tree_text.delete(1.0, tk.END)
        if self.tree is None:
            self.tree_text.insert(tk.END, "Árvore vazia.")
        else:
            lines = []
            self._build_tree_lines(self.tree, 0, "Root: ", lines)
            self.tree_text.insert(tk.END, "\n".join(lines))

    def _build_tree_lines(self, node, level, prefix, lines):
        if node.right:
            self._build_tree_lines(node.right, level + 1, "R--- ", lines)
        lines.append("     " * level + prefix + str(node.key))
        if node.left:
            self._build_tree_lines(node.left, level + 1, "L--- ", lines)

if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop() 

    