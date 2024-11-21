from typing import List, Tuple
import re

class DocumentProcessor:
    def __init__(self):
        self.documents = {}

    def add_document(self, doc_id: str, content: str):
        """Add a document to the processor."""
        self.documents[doc_id] = content

    def search_text(self, query: str) -> List[Tuple[str, str]]:
        """Search for documents containing the query string."""
        results = []
        query = query.lower()
        
        for doc_id, content in self.documents.items():
            if query in content.lower():
                results.append((doc_id, content))
        
        return results