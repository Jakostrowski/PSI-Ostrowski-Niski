class FileManager:
    def __init__(self, file_name):
        self.plik = file_name
    def read_file(self):
        file = open(self.plik, 'r', encoding='utf-8')
        while True:
            dane = file.read(1024)
            print(dane, end='')
            if not dane:
                file.close()
                break
    def update_file(self, text_data):
        file=open(self.plik, 'a' ,encoding='utf-8')
        file.write(text_data)