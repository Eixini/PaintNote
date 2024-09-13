import sys
from PySide6.QtWidgets import QApplication
from PaintNote.PaintNote.PaintNote.PaintWindow import PaintWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Notessa')

    window = PaintWindow()
    window.show()

    app.exec()

if __name__ == '__main__':
    main()