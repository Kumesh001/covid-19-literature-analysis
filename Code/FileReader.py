
class FileReader:
    def __init__(self,file_path):
        with open(file_path) as file:
            content = json.load(file)
            self.paper_id = content['paper_id'].strip()
            self.title = content['metadata']['title'].strip()
            self.abstract = []
            self.body_text = []
            self.references = []

            # Abstract
            for entry in content['abstract']:
                self.abstract.append(entry['text'])
            # Body text
            for entry in content['body_text']:
                self.body_text.append(entry['text'])

            # add the each reference name in the reference list
            for key,value in enumerate(content['bib_entries']):
                self.references.append(content['bib_entries'][value]['title'])

            self.abstract= '\n'.join(self.abstract)
            self.body_text = '\n'.join(self.body_text)
    
    def __repr__(self):
        return f'{self.paper_id}: {self.title[:200]}...'
