from PySide6.QtWidgets import QMainWindow, QWidget, QColorDialog, QSizePolicy, QLabel, QSpinBox, QPushButton
from PySide6.QtGui import QIcon, QUndoStack
from PySide6.QtCore import Qt, QSize

from PaintNote.PaintNote.PaintNote.Ui_PaintWindow import Ui_PaintWindow
from PaintNote.PaintNote.PaintNote.PaintingArea import PaintingArea

from PaintNote.PaintNote.PaintNote.res import rc_icons


class PaintWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PaintWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Paint note')
        self.setWindowIcon(QIcon(':/icons/colors.png'))

        # Save
        self.save_button = QPushButton(QIcon(':/icons/save.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.save_button)

        # Spacer 1
        self.spacer1 = QWidget()
        self.spacer1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.spacer1)

        # Set pen color
        self.pen_color_button = QPushButton(QIcon(':/icons/colors.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.pen_color_button)

        # Set pen size
        self.pen_size_label = QLabel()
        self.pen_size_label.setText('Pen size:')
        self.ui.toolbar.addWidget(self.pen_size_label)

        self.pen_size_spinbox = QSpinBox()
        self.pen_size_spinbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.pen_size_spinbox.setMinimumSize(QSize(75, 24))
        self.pen_size_spinbox.setMinimum(1)
        self.ui.toolbar.addWidget(self.pen_size_spinbox)

        # Spacer 2
        self.spacer2 = QWidget()
        self.spacer2.setMinimumWidth(40)
        self.spacer2.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.spacer2)

        # Undo
        self.undo_button = QPushButton(QIcon(':/icons/back.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.undo_button)

        # Redo
        self.redo_button = QPushButton(QIcon(':/icons/forward.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.redo_button)

        # Spacer 3
        self.spacer3 = QWidget()
        self.spacer3.setMinimumWidth(40)
        self.spacer3.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.spacer3)

        # Clear canvas
        self.clear_button = QPushButton(QIcon(':/icons/garbage.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.clear_button)

        # ----------------- Undo/Redo -----------------
        self.undoStack = QUndoStack(self)
        self.undoStack.setUndoLimit(30)

        # ======================== StatusBar settings ========================

        self.cursor_coordinates_label = QLabel()
        self.ui.statusbar.addWidget(self.cursor_coordinates_label)

        # Signal - slot

        self.save_button.clicked.connect(self.save)
        self.pen_color_button.clicked.connect(self.set_pen_color)
        self.undo_button.clicked.connect(self.undo)
        self.redo_button.clicked.connect(self.redo)
        self.pen_size_spinbox.valueChanged.connect(self.set_pen_size)
        self.clear_button.clicked.connect(self.clear_canvas)

    def save(self):
        self.ui.canvas.image.save('.\\test.png', 'PNG', -1)

    def set_pen_size(self):
        self.ui.canvas.pen_size = self.pen_size_spinbox.value()

    def set_pen_color(self):
        color_dialog = QColorDialog()
        color = color_dialog.getColor()
        if color.isValid():
            self.ui.canvas.pen_color = color

    def undo(self):
        self.ui.canvas.undo()

    def redo(self):
        self.ui.canvas.redo()

    def clear_canvas(self):
        # Clear canvas
        self.ui.canvas.clear()
