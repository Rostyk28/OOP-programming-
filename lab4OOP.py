from abc import ABC, abstractmethod

# === Composite Pattern ===

# Абстрактний базовий клас
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf — файл
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(' ' * indent + f"📄 File: {self.name}")

# Composite — папка
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def display(self, indent=0):
        print(' ' * indent + f"📁 Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)

# === Facade Pattern ===

class FileSystemFacade:
    def __init__(self):
        self.root = Folder("Root")

    def create_sample_structure(self):
        docs = Folder("Documents")
        pics = Folder("Pictures")
        self.root.add(docs)
        self.root.add(pics)

        docs.add(File("resume.docx"))
        docs.add(File("project.pdf"))

        pics.add(File("vacation.jpg"))
        pics.add(File("birthday.png"))

    def show_file_system(self):
        self.root.display()

# === Основна програма ===

def main():
    fs = FileSystemFacade()
    fs.create_sample_structure()
    fs.show_file_system()

if __name__ == "__main__":
    main()
