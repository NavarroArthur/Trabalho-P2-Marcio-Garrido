import tkinter as tk
from tkinter import ttk, messagebox
from grafico_escala_maior import Grafico_intervalo_maior
from note1 import Notas

class EscalaMaiorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escala Maior - Interface Gráfica")
        self.root.geometry("400x250")
        self.grafico = Grafico_intervalo_maior()
        
        # Label
        label = tk.Label(root, text="Selecione uma nota:", font=("Arial", 12))
        label.pack(pady=10)

        # Combobox para seleção de nota
        self.nota_var = tk.StringVar()
        self.combo = ttk.Combobox(root, textvariable=self.nota_var, state="readonly", font=("Arial", 12))
        self.combo['values'] = [nota.value.strip() for nota in Notas]
        self.combo.pack(pady=5)

        # Botão para mostrar escala
        btn = tk.Button(root, text="Mostrar Escala Maior", command=self.mostrar_escala, font=("Arial", 12))
        btn.pack(pady=10)

        # Label para mostrar resultado
        self.result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="center")
        self.result_label.pack(pady=10)

    def mostrar_escala(self):
        nota_selecionada = self.nota_var.get()
        if not nota_selecionada:
            messagebox.showwarning("Aviso", "Por favor, selecione uma nota musical.")
            return
        # Encontrar o Enum correspondente
        nota_enum = None
        for nota in Notas:
            if nota.value.strip() == nota_selecionada:
                nota_enum = nota
                break
        if nota_enum is None:
            self.result_label.config(text="Nota inválida.")
            return
        escala = self.grafico.obter_escala_maior_nota(nota_enum)
        # Formatar para exibir os nomes das notas
        escala_str = ' → '.join([n.value.strip() for n in escala])
        self.result_label.config(text=f"Escala maior de {nota_selecionada}:\n{escala_str}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EscalaMaiorApp(root)
    root.mainloop() 