import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit
from collections import Counter

alphabet_en = "abcdefghijklmnopqrstuvwxyz"

# Шифрование текста
def encrypt(alph, text, shift):
    new_text = ''
    # Поиск соответствующего символа из алфавита и из текста
    for i in range(len(text)):
        for j in range(len(alph)):
            # Проверяем: если символа нет в данном алфавите
            if text[i].lower() not in alph:
                new_text += text[i]
                break
            # Проверяем: если символ нижнего регистра
            if text[i] == alph[j]:
                new_text += (alph[(j + shift) % len(alph)])
            # Проверяем: если символ верхнего регистра
            if text[i] == alph[j].upper():
                new_text += (alph[(j + shift) % len(alph)]).upper()
    return new_text

# Дешифрование текста
def decrypt(alph, text, shift):
    new_text = ''
    # Поиск соответствующего символа из алфавита и из текста
    for i in range(len(text)):
        for j in range(len(alph)):
            # Проверяем: если символа нет в данном алфавите
            if text[i].lower() not in alph:
                new_text += text[i]
                break
            # Проверяем: если буква нижнего регистра
            if text[i] == alph[j]:
                new_text += (alph[(j - shift) % len(alph)])
            # Проверяем: если буква верхнего регистра
            if text[i] == alph[j].upper():
                new_text += (alph[(j - shift) % len(alph)]).upper()
    return new_text

# Взлом текста
def hack(alph, text):
    frequency = Counter()
    # Подсчет частоты букв
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in alph:
            frequency[lower_letter] += 1
    # Находим букву встречающуюся чаще всего в данном тексте
    sorted_alph = frequency.most_common()
    if sorted_alph:
        most_frequent_letter = sorted_alph[0][0]
        # Пусть эта буква соответствует 'e' из английского алфавита(alphabet_en)
        if most_frequent_letter:
            expected_shift = (alph.index(most_frequent_letter) - alph.index('e') + len(alph)) % len(alph)
            new_text = decrypt(alph, text, expected_shift)
            return (str(expected_shift), new_text)
    return ("error", text)


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Шифр Цезаря")
        self.setGeometry(100, 100, 400, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.text_input = QTextEdit(self)
        self.text_input.setPlaceholderText("Введите текст")

        self.shift_input = QLineEdit(self)
        self.shift_input.setPlaceholderText("Введите сдвиг")

        self.text_output = QTextEdit(self)
        self.text_output.setPlaceholderText("Результат")
        self.text_output.setReadOnly(True)

        encrypt_button = QPushButton("Зашифровать", self)
        encrypt_button.clicked.connect(self.encrypt)

        decrypt_button = QPushButton("Расшифровать", self)
        decrypt_button.clicked.connect(self.decrypt)

        hack_button = QPushButton("Взломать", self)
        hack_button.clicked.connect(self.hack)

        layout.addWidget(QLabel("Текст:"))
        layout.addWidget(self.text_input)
        layout.addWidget(QLabel("Сдвиг:"))
        layout.addWidget(self.shift_input)
        layout.addWidget(QLabel("Результат:"))
        layout.addWidget(self.text_output)
        layout.addWidget(encrypt_button)
        layout.addWidget(decrypt_button)
        layout.addWidget(hack_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def encrypt(self):
        text = self.text_input.toPlainText()
        shift = self.shift_input.text()
        if shift:
            shift = int(shift)
            if text:
                encrypted = encrypt(alphabet_en, text, shift)
                self.text_output.setPlainText(encrypted)
            else:
                self.text_output.setPlainText("Введите текст в поле ввода")
        else:
            self.text_output.setPlainText("Введите сдвиг в поле ввода")

    def decrypt(self):
        text = self.text_input.toPlainText()
        shift = self.shift_input.text()
        if shift:
            shift = int(shift)
            if text:
                decrypted = decrypt(alphabet_en, text, shift)
                self.text_output.setPlainText(decrypted)
            else:
                self.text_output.setPlainText("Введите текст в поле ввода")
        else:
            self.text_output.setPlainText("Введите сдвиг в поле ввода или нажмите кнопку «Взломать»")

    def hack(self):
        text = self.text_input.toPlainText()
        if text:
            shift, hacked = hack(alphabet_en, text)
            if shift!='error':
                outputText = f"Предполагаемый сдвиг: {shift}\n{hacked}"
                self.text_output.setPlainText(outputText)
            else:
                self.text_output.setPlainText("Нет возможности взломать текст")
        else:
            self.text_output.setPlainText("Введите текст в поле ввода")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = App()
    mainWin.show()
    sys.exit(app.exec_())
