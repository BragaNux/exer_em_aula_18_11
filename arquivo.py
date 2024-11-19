class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho

    def __repr__(self):
        return f"{self.nome} ({self.tamanho}KB) em {self.caminho}"


class TabelaHash:
    def __init__(self, capacidade=7):
        self.capacidade = capacidade
        self.tabela = [[] for _ in range(capacidade)]

    def _funcao_hash(self, chave):
        return sum(ord(c) * (i + 1) for i, c in enumerate(chave)) % self.capacidade

    def inserir(self, arquivo):
        indice = self._funcao_hash(arquivo.nome)
        for item in self.tabela[indice]:
            if item.nome == arquivo.nome:
                return f"'{arquivo.nome}' já existe."
        self.tabela[indice].append(arquivo)
        return f"'{arquivo.nome}' adicionado."

    def buscar(self, nome_arquivo):
        indice = self._funcao_hash(nome_arquivo)
        for arquivo in self.tabela[indice]:
            if arquivo.nome == nome_arquivo:
                return arquivo
        return f"'{nome_arquivo}' não encontrado."

    def remover(self, nome_arquivo):
        indice = self._funcao_hash(nome_arquivo)
        for i, arquivo in enumerate(self.tabela[indice]):
            if arquivo.nome == nome_arquivo:
                self.tabela[indice].pop(i)
                return f"'{nome_arquivo}' removido."
        return f"'{nome_arquivo}' não existe."

    def listar_todos(self):
        return [arquivo for sublista in self.tabela for arquivo in sublista]


if __name__ == "__main__":
    tabela = TabelaHash(9)

    arquivos = [
        Arquivo("relatorio.pdf", "/docs/relatorio.pdf", 1024),
        Arquivo("foto.jpg", "/img/foto.jpg", 2048),
        Arquivo("dados.csv", "/planilhas/dados.csv", 512),
        Arquivo("backup.zip", "/backup/backup.zip", 4096)
    ]

    for arq in arquivos:
        print(tabela.inserir(arq))

    print("\nBusca: ", tabela.buscar("dados.csv"))
    print(tabela.buscar("inexistente.txt"))

    print("\n", tabela.remover("foto.jpg"))
    print(tabela.remover("foto.jpg"))

    print("\nArquivos:")
    for arquivo in tabela.listar_todos():
        print(arquivo)
