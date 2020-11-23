import os
from pathlib import Path

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [
        ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
        ".heif", ".psd"
    ],
    "VIDEOS": [
        ".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt",
        ".mpg", ".mpeg", ".3gp"
    ],
    "DOCUMENTS": [
        ".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt",
        ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf",
        ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"
    ],
    "ARCHIVES": [
        ".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg",
        ".rar", ".xar", ".zip"
    ],
    "AUDIO": [
        ".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv",
        "ogg", "oga", ".raw", ".vox", ".wav", ".wma"
    ],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}


def read_files():
    f = open("/Users/mintukrishnan/Downloads/spec.txt", "r")
    print(f.readline())
    f.close()


read_files()