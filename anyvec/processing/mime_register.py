import mimetypes

# Register OOXML Word formats for all platforms
mimetypes.add_type("application/vnd.openxmlformats-officedocument.wordprocessingml.document", ".docx")
mimetypes.add_type("application/vnd.openxmlformats-officedocument.wordprocessingml.template", ".dotx")
mimetypes.add_type("application/vnd.ms-word.template.macroenabled.12", ".dotm")
mimetypes.add_type("application/vnd.ms-word.document.macroenabled.12", ".docm")
