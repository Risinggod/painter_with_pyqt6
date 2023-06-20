from PyQt6.QtGui import QPaintEvent, QPainter, QColor, QPen, QFont
from PyQt6.QtWidgets import QWidget, QStylePainter
from PyQt6.QtCore import pyqtSlot, QPoint, Qt

class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        #painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Fülle den Kreis mit schwarzer Farbe
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(50, 50, 100, 100)

        # Ändere die Zeichenfarbe auf Grün
        painter.setPen(QPen(Qt.GlobalColor.green))

        # Zeichne eine Ellipse
        painter.drawEllipse(200, 50, 150, 100)

        # Zeichne einen Kreis
        painter.drawEllipse(50, 200, 100, 100)

        # Zeichne ein Quadrat
        painter.drawRect(200, 200, 100, 100)

        # Zeichne eine Linie
        painter.drawLine(50, 350, 350, 350)

        # Gib den Text "Zeichenprogramm" aus
        painter.setFont(QFont("Arial", 12))
        painter.drawText(180, 380, "Zeichenprogramm")





