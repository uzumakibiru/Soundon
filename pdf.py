import PyPDF2
class PDF():
  

    def reader(self,path):
        with open(path,"rb") as file:
            reader=PyPDF2.PdfReader(file)
            text=""
            for page_num in range(reader._get_num_pages()):
                page=reader.pages[page_num]
                text+=page.extract_text()
        
        return text
            