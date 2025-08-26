class VectorStore:
    def __init__(self):
        self.documents = {}

    def load_documents(self, file_paths):
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                content = file.read()
                self.documents[file_path] = content

    def query(self, query_text):
        results = {}
        for file_path, content in self.documents.items():
            if query_text.lower() in content.lower():
                results[file_path] = content
        return results

    def add_document(self, file_path, content):
        self.documents[file_path] = content

    def get_documents(self):
        return self.documents