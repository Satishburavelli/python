class File:
    def __init__(self,name,size):
        self.name=name
        self.size=size
class Document(File):
        pass
class Pdf(Document):
        pass
class Word(Document):
        pass
class Image(File):
        pass
class PNG(Image):
        pass
class JPG(Image):
        pass
class Video(File):
        pass
class MP4(Video):
        pass
class MOV(Video):
        pass
class Renderer():
        def render(self,file):
                if isinstance(file,Document):
                        print(f"The file of the document is printed with name and size:")
                elif isinstance(file,Image):
                        print(f"The file of the image is printed with name and size:")
                elif isinstance(file,Video):
                        print(f"The file of the video is printed with name and size:")
                else:
                        print("The render file is printed with name and size:")
        def run(self,files):
                for file in files:
                        self.render(file)
        file_objects =(
        PNG("Image1","2mb"),
        JPG("Image2","3mb"),
        File("File12","4mb"),
        MP4("Video1","10mb"),
        MOV("Video2","50mb"),
        Image("image_file","1mb"),
        Video("video_file","8mb"),
        Pdf("pdf3","250kb"),
        Word("word1","500kb"),
        Document("doc1","10kb"),    
)
renderer=Renderer()
renderer.run(file_objects)

