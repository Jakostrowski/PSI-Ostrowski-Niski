class FileManager:
    def __init__(self, file_name):
        self.file_name=file_name
    def update_file(self, text_data):
        plik=open(self.file_name, 'a' ,encoding='utf-8')
        plik.write(text_data)
    def read_file(self):
        uchwyt = open(self.file_name, 'r', encoding='utf-8')
        while True:
            dane = uchwyt.read(1024)
            print(dane, end='')
            if not dane:
                uchwyt.close()
                break
