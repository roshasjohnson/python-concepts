from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def add_section(self, text):
        pass

class Resume(Document):
    def create_header(self):
        print("Resume Header: Name, Contact Info")

    def add_section(self, text):
        print(f"Resume Section: {text}")

class Report(Document):
    def create_header(self):
        print("Report Header: Title, Date")

    def add_section(self, text):
        print(f"Report Section: {text}")

class DocumentFactory:
    def create_document(self, doc_type):
        if doc_type == "resume":
            return Resume()
        elif doc_type == "report":
            return Report()
        else:
            raise ValueError("Unknown document type")

# Usage:
factory = DocumentFactory()

# Create a Resume
resume = factory.create_document("resume")
resume.create_header()  # Output: "Resume Header: Name, Contact Info"

# Create a Report
report = factory.create_document("report")
report.add_section("Introduction")  # Output: "Report Section: Introduction"