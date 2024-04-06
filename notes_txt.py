#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу

#затем запрограммируй демо-версию функционала
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


app = QApplication([])













'''Интерфейс приложения'''
#параметры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)


#обработка событий
list_notes.ItemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)


#запуск приложения
notes_win.show()

#виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')




button_note_create = QPushButton('Создать заметку') #появляется окно с полем "Введите имя заметки"
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')




field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')




#расположение виджетов по лэйаутам
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)




col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)




col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)




col_2.addLayout(row_3)
col_2.addLayout(row_4)




layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)




'''Функционал приложения'''
def show_note():
    #получаем текст из заметки с выделенным названием и отображаем его в поле редактирования
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])




'''Запуск приложения'''
#подключение обработки событий
list_notes.itemClicked.connect(show_note)


#запуск приложения
notes_win.show()


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

def add_note():
    note_name , result = QInputDialog.getText(notes_win, 'Добавит заметку' , 'Название заметки:')
    if ok and note_name != "":
        notes[note_name] = {"текст" : "", "теги" :[]}
        list_notes.addItems(note_name)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes_data.json' , 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для сохраниения не выбрана!')


def del_note():
    if list_notes.selectedItems():
        key - list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json' , 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')



    def search_tag():
        tag = field_tag.text()
        if button_tag_search.text() == 'искать заметки по тегу' and tag:
            notes_filtered = {}
            for note in notes:
                if tag in notes[note]['теги']:
                    notes_filtered[note]=notes[note]
            button_tag_search.setText('Сбросите поиск')
            list_notes.clear()
            list_tags.clear()
            list_notes.addItems(notes_filtered)
        elif button_tag_search.text() == 'Сбросить поиск':
            field_tag.clear()
            list_notes.clear()
            list_tags.clear()
            list_notes.addItems(notes)
            button_tag_search.setText('Искать заметки по тегу')
        else:
            pass

def add_note():
    if ok and note name != "":
        note = list()
        note= [note_name,'',[]]
        notes.append(note)
        list_notes.addItem(note[0])
        filename = str(len(nates)-1)+".txt"
        with open(filename, "w") as file:
            file.write(note[0]+'\n')

def save_note():
    key = list_notes.selectedItems()[0].text()
    i = 0
    for note in notes:
        if note[0] == key:
            note[1] = field_text.toPlainText()
            filename = str(i)+".txt"
            with open(filename, "w") as file:
                file.write(note[0]+'\n')
                file.write(note[1]+'\n')
                for tag in note[2]:
                    file.write(tag+'')
                    file.write('\n')
i += 1
app.exec_()

while True:
    filename = str(name)+".txt"
    try:
        with open(filename, "r") as file:
#чтение и добавление
#Изаметки в notes
    except I0Error:
        break