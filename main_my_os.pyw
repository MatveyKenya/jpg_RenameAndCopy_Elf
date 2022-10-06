#---------------------------------------------------
# 21/05/2020 - начато
# программа по переименованию .jpg
# под нужды проги База Эльф
# 
#---------------------------------------------------
#
import os, configparser, fnmatch
from shutil import copyfile
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from main_os_form import Ui_MainWindow # главное окно программы

class Main_window(QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__() # super(Main_window, self).__init__()
        print('------class Main_window(QMainWindow) создан------')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.cs = CopyScans() # определение путей до сканов - откуда и куда скидывать     
        self.init_ui_dop_config()

    def closeEvent(self, QCloseEvent):
        '''действия при закрытии приложения'''
        # обновить файл cfg если произошли изменения в настройках путей
        if self.need_to_save_cfg:
            self.cs.save_cfg()                      

    def init_ui_dop_config(self): # set widgets to default position
        self.ui.pushB_close.clicked.connect(self.close_win)
        self.ui.pushB_new.clicked.connect(self.new_jpg)
        self.ui.pushB_open_jpg.clicked.connect(self.open_jpg)
        self.ui.pushB_rename.clicked.connect(self.new_date_rename)
        self.ui.path_glob.triggered.connect(self.set_path_glob)
        self.ui.path_local.triggered.connect(self.set_path_local)
        self.ui.instruction_pr.triggered.connect(self.instruction_pr)
        self.ui.about_pr.triggered.connect(self.win_about)        
        day_1 = QDate.currentDate() 
        self.ui.dateE_dost.setDateTime(QDateTime(day_1, QTime(0, 0, 0)))
        self.ui.dateE_dost_new.setDateTime(QDateTime(day_1, QTime(0, 0, 0)))
        self.ui.checkB_north.toggled.connect(self.checkB_north_changed)
        self.ui.checkB_got.toggled.connect(self.checkB_got_changed)        
        self.ui.dateE_got.setEnabled(False)
        self.set_label_path_glob()
        self.set_label_path_local()
        self.need_to_save_cfg = False        
        self.ui.lineE_number.setInputMask('0000/d') #поле ввода номера (ограничение по маске)
        # МАСКА: 0-числовые необязательные знаки [0-9] / d-необязательный знак [1-9]

    def read_data_from_win(self):
        ''' read data from win forms and translate to logical class CopyScans\n
            date_dost = QDateTime.dateTime() из формы ui.DateEdit\n
            date_got = QDateTime.dateTime() из формы ui.DateEdit\n
        '''
        number = self.format_number(self.ui.lineE_number.text())            
        fio = self.ui.lineE_fio.text()                 
        date_dost = self.ui.dateE_dost.dateTime()        
        date_got = None
        if self.ui.checkB_got.checkState(): date_got=self.ui.dateE_got.dateTime()
        north = self.ui.checkB_north.checkState()
        self.cs.data_set(north, date_dost, number, fio, date_got)

    def open_jpg(self):
        '''open file.jpg with number !OR! fio from server/scans'''
        print('зашел в опен джпег')        
        # собираем входные данные с окошка...
        if not self.cs.path_to_global_scans:
            QMessageBox.critical(self, 'Ошибка!', 'Не задан путь до сервера!')
            return
        self.read_data_from_win()
        # определить имя файла исходя из данных и открыть...
        file_name_full = self.cs.find_file_name()        
        os.system(f'start "" "{file_name_full}"')

    def win_about(self): # вывод инфы о проге
        '''info about prog'''             
        QMessageBox.about(self, 'о программе', 'Версия 1.0 (06.2020)\nmatveykenya@gmail.com')

    def instruction_pr(self):
        '''win with instuction and help for work with prog'''
        QMessageBox.about(self, 'справка', 'в разработке')

    def set_label_path_glob(self):
        self.ui.label_path_glob.setText('Путь к серверу сканов '+self.cs.path_to_global_scans)

    def set_label_path_local(self):
        self.ui.label_path_local.setText('Путь к локальной папке '+self.cs.path_to_local_scans)
    
    def set_path_glob(self):
        path_to_global_scans = QFileDialog.getExistingDirectory(self, caption='Выберите файлы jpg для переноса')
        if path_to_global_scans:
            self.cs.path_to_global_scans = path_to_global_scans
            self.set_label_path_glob()
            self.need_to_save_cfg = True

    def set_path_local(self):
        path_to_local_scans= QFileDialog.getExistingDirectory(self, caption='Выберите файлы jpg для переноса')
        if path_to_local_scans:
            self.cs.path_to_local_scans = path_to_local_scans
            self.set_label_path_local()
            self.need_to_save_cfg = True
    
    def close_win(self):        
        self.close()
    
    def new_jpg(self):
        '''переименовываем новые файлы jpg, копируем их из path_local в path_global'''        
        # собираем входные данные с окошка...
        if self.cs.path_to_global_scans:
            self.read_data_from_win()
            if self.cs.number and self.cs.fio:
                list_files = QFileDialog.getOpenFileNames(self, caption='Выберите файлы jpg для переноса',
                    dir=self.cs.path_to_local_scans, filter='*.jpg')
                files_jpg = list_files[0]
                if files_jpg:
                    # ... и собственно само действо по переносам и переименованиям
                    w = self.cs.new_rename_and_remove(files_jpg)                    
                    if w[0]: QMessageBox.information(self, 'Успешно', w[1])
                    elif w[1]: QMessageBox.critical(self, 'Копирование отменено!', w[1])# если сообщение W[1]='' пусто то сообщения нет
            else: QMessageBox.critical(self, 'Ошибка!', 'Нет номера или ФИО заказчика')
        else: QMessageBox.critical(self, 'Ошибка!', 'Не задан путь до сервера!')

    def new_date_rename(self):
        '''переименовываем файлы jpg и перносим по новой дате ВНУТРИ path_global'''
        # считывание данных и вызов self.cs.remove_with_new_date_dost
        #    
        # собираем входные данные с окошка...
        if not self.cs.path_to_global_scans:
            QMessageBox.critical(self, 'Ошибка!', 'Не задан путь до сервера!')
            return         
        self.read_data_from_win()
        # определить имена файлов исходя из данных
        files_jpg = self.cs.find_file_name()
        
        buttonYesNO = QMessageBox.question(self, 'Найдено', 'Столько-то файлов.\n Преносим?')        
        if (buttonYesNO == QMessageBox.StandardButton.Yes):
            
            print('перемещаем файлы...')


        
        print('the end')

        #


    def format_number(self, number) -> str:
        '''returns number for name file.jpg in the desired format'''        
        razdel = number.find('/')
        num = number[:razdel]
        if num == '': return ''
        doz = number[razdel+1:]
        
        if doz == '': doz = ''
        elif doz == '1': doz = ' доз'
        else: doz = ' доз' + doz

        print('возвращаемый номер', f'{num}{doz}')
        return f'{num}{doz}'

    def checkB_north_changed(self):
        if self.ui.checkB_north.isChecked():
            self.ui.checkB_got.setChecked(True)
            self.ui.checkB_got.setEnabled(False)
        else:
            self.ui.checkB_got.setChecked(False)
            self.ui.checkB_got.setEnabled(True)

    def checkB_got_changed(self):
        if self.ui.checkB_got.isChecked():
            self.ui.dateE_got.setEnabled(True)
            dateTime_1 = self.ui.dateE_dost.dateTime().addDays(-7)            
            #print(day_1)            
            self.ui.dateE_got.setDateTime(dateTime_1)
        else: self.ui.dateE_got.setEnabled(False)


class CopyScans(): # здесь реализована логика, а class Main_window отвечает за UI и сбор данных с окошек
    '''copy scans *.jpg from folder1 to folder2 and Rename its'''

    def __init__(self):
        self.path_to_global_scans = ''
        self.path_to_local_scans = ''        
        self.file_cfg = self.file_config_name()
        self.open_cfg()
        self.data_set()

    def data_set(self, north=False, date_dost=None, number='', fio='', date_got=None):
        ''' set parameters '''
        self.north=north
        self.date_dost=date_dost
        self.number=number
        self.fio=fio
        self.date_got=date_got

    def file_config_name(self) -> str:
        '''return full path to config.ini in curent dir with prog'''        
        file_config_name = 'config.ini'
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, file_config_name)
        return config_path                

    def save_cfg(self):
        '''save config.ini in dir with prog'''
        print('просто зашел')
        if os.path.isdir(self.path_to_global_scans) and os.path.isdir(self.path_to_local_scans):            
            config = configparser.ConfigParser()
            config.add_section("Settings")
            config.set('Settings', 'path_to_server_with_scans', self.path_to_global_scans)
            config.set('Settings', 'path_to_local_scans', self.path_to_local_scans)
            print('зашел в def save_cfg(self)')
            with open(self.file_cfg, "w") as f:                
                config.write(f)
                print('файл cfg создан/перезаписан')

    def open_cfg(self):
        '''Get paths from config.ini'''        
        if os.path.isfile(self.file_cfg):
            config = configparser.ConfigParser()                
            config.read(self.file_cfg)
            self.path_to_global_scans = config.get('Settings', 'path_to_server_with_scans')
            self.path_to_local_scans = config.get('Settings', 'path_to_local_scans')
            if not os.path.isdir(self.path_to_global_scans): self.path_to_global_scans = ''
            if not os.path.isdir(self.path_to_local_scans): self.path_to_local_scans = ''

    def new_rename_and_remove(self, files_jpg=list(), saveDuplicates=True):
        '''переименовать группу файлов files.jpg и копировать на Сервер path_global\n
        формат хх.хх №№№ fio-1, -2, -3 и т.д. (дата № ФИО)\n        
        files_jpg - список выбранных файлов с полными путями\n
        проверка условия корректности данных должна быть проведена до вызова этой подпрогр!
        saveDuplicates=True - оставить копию переименованных файлы в исходном месте
        '''        
        # новое имя файлов (без ".jpg") и путь на сервере        
        new_file_name = self.file_name()
        path_to_server = self.path_to_server()      
        # путь до локальной папки с файлами        
        path_to_file = os.path.dirname(files_jpg[0])

        textMessage = f'Файлы jpg будут перенесены по пути:\n{path_to_server}\n\n{new_file_name} - {len(files_jpg)} шт'
        if saveDuplicates: textMessage += f'\n\nДубликаты сохранены в {path_to_file}'
        buttonYesNO = QMessageBox.question(application, 'Проверь правильность данных', textMessage)        
        if (buttonYesNO == QMessageBox.StandardButton.Yes):     

            if not os.path.isdir(path_to_server):
                try: os.makedirs(path_to_server)
                except: return False, 'Создание папки на сервер не удалось!\nКопирование отменилось'
            
            for i in range(len(files_jpg)):
                ii_str = str(i+1)
                if len(ii_str)<2: ii_str = '0'+ii_str
                
                #Защита от дурака епта - чтобы ранее скопированные файлы не перезаписались
                file_name_to_sever = path_to_server +'/'+ new_file_name +'-'+ ii_str + '.jpg'
                if os.path.isfile(file_name_to_sever):
                    return False, f'файл {file_name_to_sever} уже есть на сервере'
                file_name = path_to_file +'/'+ new_file_name +'-'+ ii_str + '.jpg'
                if os.path.isfile(file_name):
                    return False, f'файл {file_name} уже есть здесь'    

                try:
                    copyfile(files_jpg[i], file_name_to_sever) # копия файлов на сервер
                except: return False, 'Копирование файлов на сервер не удалось!'

                if saveDuplicates:
                    try:
                        os.rename(files_jpg[i], file_name) # переименование в текущую директорию
                    except: return False, 'Переименование файлов в локал дир не удалось!'
                else:
                    try:
                        os.remove(files_jpg[i]) # удаление исходных файлов в текущей директории
                    except: return False, 'Удаление исходных файлов в локал дир не удалось!'       

            return True, f'Перенесено на сервер {path_to_server}\n\n{len(files_jpg)} файлов'

        return False, f''

    def file_name(self) -> str:
        '''local name(s) file.jpg on server (no dir path and without-".jpg")'''        
        if self.north:
            return self.date_got.toString('dd.MM') + ' (c) ' + self.number + ' ' + self.fio            
        else:
            return self.date_dost.toString('dd.MM') +' '+ self.number +' '+ self.fio 

    def file_name_mask(self) -> str:
        ''' возвращает маску имени файла по неполным параметрам '''
        return '*' + self.number + '*' + self.fio+ '*'        

    def path_to_server(self) -> str:
        '''dir path to scan server for curent file(s)'''        
        year = self.date_dost.toString('yyyy')
        month = self.date_dost.toString('MM')
        day_month = self.date_dost.toString('dd.MM')
        if self.north:            
            return self.path_to_global_scans + '/' + year +\
            '/СЕВЕР/(' + month + ') отгруз ' + day_month
        else:            
            day = self.date_dost.toString('dd')
            return self.path_to_global_scans+'/'+year+'/'+self.name_month(month)+'/'+day          

    def remove_with_new_date_dost(self):
        '''по пути path_global перенести файлы .jpg из 1 в 2 папки с переименованием даты в имени файла''' 

    def name_month(self, mm='00'):
        if mm=='01': mm='(01) январь'
        if mm=='02': mm='(02) февраль'
        if mm=='03': mm='(03) март'
        if mm=='04': mm='(04) апрель'
        if mm=='05': mm='(05) май'
        if mm=='06': mm='(06) июнь'
        if mm=='07': mm='(07) июль'
        if mm=='08': mm='(08) август'
        if mm=='09': mm='(09) сентябрь'
        if mm=='10': mm='(10) октябрь'
        if mm=='11': mm='(11) ноябрь'
        if mm=='12': mm='(12) декабрь'
        return mm        

    def find_file_name(self) -> str:
        ''' Возвращает полное имя файла на сервере по заданным параметрам.
            Проверяет его, и если не может найти, то передает
            путь до папки с date_dost
        '''
        file_path = self.path_to_server()
        if not(self.number or self.fio): return file_path # если нет номера и фио то открыть папку
        file_name = self.file_name_mask()
        file_name_full = os.path.join(file_path, file_name)
        print(file_name_full)
        if os.path.isdir(file_path):
            for file in os.listdir(file_path):
                if fnmatch.fnmatch(file, file_name):                
                    print (os.path.join(file_path, file))
                    return os.path.join(file_path, file)
            return file_path
        else: return ''
      
       

if __name__=='__main__':
    app = QApplication([])
    application = Main_window()
    application.show()    
    app.exec_()       
