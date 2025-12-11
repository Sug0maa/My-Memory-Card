# подключение библеотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout,  QLabel,QMessageBox, QRadioButton
from random import shuffle
from random import randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Столица Франции', 'париж','Мадрид','Рим','Лондон'))
questions_list.append(Question('Какой химический элемент обозначается символом O?', 'Азот','Кислород','Золото','Серебро'))
questions_list.append(Question('Какой язык считается самым распространённым по количеству носителей?', 'Японский','Английский','Китайский','Испанский'))
questions_list.append(Question('Кто написал роман "Преступление и наказание"?', 'Лев Толстой','Федор Достоевский','Николай Гоголь','Антон Чехов'))
questions_list.append(Question('Как называется самая длинная река в мире?', 'Мисисиппи','Нил','Янцзы','Амазонка'))
questions_list.append(Question('Сколько дней в високосном году?', '364','366','367','365'))
questions_list.append(Question('Кто написал произведение "Ревизор"?', 'Антон Чехов','Николай гоголь','Максим Горький','Лев Толстой'))
questions_list.append(Question('В каком море находится Крымский полуостров', 'Средиземное','Балтийское','Азовское','Черное'))
questions_list.append(Question('Кто написал музыку к балету «Лебединое озеро»?', 'Бетховен','Чайковский','Моцарт','Шопен'))
questions_list.append(Question('Кто был первым президентом России?', 'Горбачев','Медведев','Борис Ельцин','Путин'))
questions_list.append(Question('В какой стране находится город Венеция?', 'Италия','Франция','Португалия','Испания'))

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question1 = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Чульмицы')
btn_answer3 = QRadioButton('Смурфы')
btn_answer4 = QRadioButton('Алеуты')
btn_ok = QPushButton('Ответить')

AnsGroupBox = QGroupBox('Результаты теста')
answerResult = QLabel('Правильно/Неправильно')
answerCorrect = QLabel('Ответ будет тут')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Следующий вопрос")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText("Ответить")
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def test():
    if 'Ответить' ==btn_ok.text():
        show_result()
    else:
        show_question()

    
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question1.setText(q.question)
    answerCorrect.setText(q.right_answer)
    show_question()

def show_correct(res):
    answerResult.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        main_win.score += 1
        print('Статистика\n-всего вопросов', main_win.total, '\n-Правильных ответов: ', main_win.score)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно")


def next_question():
    main_win.total += 1
    print('Статистика\n-всего вопросов', main_win.total, '\n-Правильных ответов: ', main_win.score)
    cur_question = randint(0,len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)


def click_ok():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()



layoutRes = QVBoxLayout()
layoutRes.addWidget(answerResult,alignment=(Qt.AlignHCenter | Qt.AlignTop))
layoutRes.addWidget(answerCorrect,alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layoutRes)

layoutH1 = QHBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()

layoutH2.addWidget(btn_answer1)
layoutH2.addWidget(btn_answer2)
layoutH3.addWidget(btn_answer3)
layoutH3.addWidget(btn_answer4)

layoutH1.addLayout(layoutH2)
layoutH1.addLayout(layoutH3)

RadioGroupBox.setLayout(layoutH1)

layoutLine1 = QHBoxLayout()
layoutLine2 = QHBoxLayout()
layoutLine3 = QHBoxLayout()

layoutLine1.addWidget(question1,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layoutLine2.addWidget(RadioGroupBox)
layoutLine2.addWidget(AnsGroupBox)

AnsGroupBox.hide()
#RadioGroupBox.hide()

layoutLine3.addStretch(1)
layoutLine3.addWidget(btn_ok,stretch=2)
layoutLine3.addStretch(1)


Layout_main = QVBoxLayout()
Layout_main.addLayout(layoutLine1, stretch=2)
Layout_main.addLayout(layoutLine2,stretch=8)
Layout_main.addStretch(1)
Layout_main.addLayout(layoutLine3,stretch=1)
Layout_main.addStretch(1)
Layout_main.setSpacing(5)
#создание виджетов главного окна
main_win.setLayout(Layout_main)


btn_ok.clicked.connect(click_ok)
main_win.score = 0
main_win.total = 0
next_question()
main_win.show()
app.exec()


