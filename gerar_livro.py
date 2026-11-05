from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

def criar_livro(nome_crianca, pasta_desenhos, arquivo_saida):
    c = canvas.Canvas(arquivo_saida, pagesize=A4)
    
    # 1. Capa
    c.setFont("Helvetica-Bold", 30)
    c.drawString(100, 700, f"As Aventuras de {nome_crianca}")
    c.setFont("Helvetica", 16)
    c.drawString(100, 650, "Um livro colorido com amor.")
    c.showPage()
    
    # 2. Páginas com os desenhos
    if os.path.exists(pasta_desenhos):
        for imagem in os.listdir(pasta_desenhos):
            if imagem.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(pasta_desenhos, imagem)
                try:
                    img = ImageReader(img_path)
                    # Desenha a imagem centralizada (ajuste conforme necessário)
                    c.drawImage(img, 50, 100, width=500, height=600, preserveAspectRatio=True)
                    c.showPage()
                except Exception as e:
                    print(f"Erro ao ler {imagem}: {e}")
    
    c.save()
    print(f"Livro gerado com sucesso: {arquivo_saida}")

# Para testar, crie uma pasta chamada 'desenhos' e coloque imagens nela
# criar_livro("Alice", "desenhos", "livro_alice.pdf")
