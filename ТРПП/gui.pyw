from tkinter import *
from sort_info.type import *
from sort_info.method import  *
import sort as st
from tkinter import messagebox as mb


placeholder = 'Введите сюда массив формата: a, b, c'
trade_mark = 'TransInformation\u2122'    

class Cast:
    
# Приводит массив к нужному формату

    @staticmethod
    def get_arr(arr):
        if arr == '':
            return None
        arr = arr.replace(' ', '')
        arr = arr.split(',')
        array = []
        try:
            for i in arr:
                array.append(float(i))
            return array
        except:
            raise ValueError("Массив не соответствует требованиям! Элементы маccива должны быть перечисленны через запятую,не должны содержать букв и знаков кроме точки и запятой.")

    @staticmethod
    def set_arr(array):
        res = ''
        for i in array:
            if i - int(i) == 0:
                res+=str(int(i))+', '
            else:
                res+=str(i)+', '
        return res[:-2]
            
class Sort:
    
# Сортирует массив, согласно выбранному методу сортировки(задается параметром sorter)

    def __init__(self, sorter, array):
        self.sorter = sorter
        self.array = array
        
    def sort(self):
        return self.sorter(self.array)

class Description:

# Возвращяет описание выбранного метода сортировки из файла(path)

    @staticmethod
    def get_desc(path):
        res = ''
        f = open(path)
        for i in f:
            res+=i
        f.close()
        return res

class Matcher:

# Корректирует работу алгоритма, согласно выбранному методу и типу сортировки

    @staticmethod
    def match_method(method):
        desc = ''
        sorter = None
        if method == sort_method[0]:
            sorter = st.QuickSort()
            desc = Description.get_desc(r'Desription\quick.txt')
        elif method == sort_method[1]:
            sorter = st.MergeSort()
            desc = Description.get_desc(r'Desription\merge.txt')
        elif method == sort_method[2]:
            sorter = st.BubbleSort()
            desc = Description.get_desc(r'Desription\bubble.txt')
        elif method == sort_method[3]:
            sorter = st.SelectSort()
            desc = Description.get_desc(r'Desription\select.txt')
        return sorter, desc

    @staticmethod
    def match_type(t):
        if t == sort_type[0]:
            return TO_UP
        else:
            return TO_DOWN
        
class MainWindow(Tk):

# Основное окно приложения(tkinter)

    def __init__(self):
        Tk.__init__(self)
        self.geometry("800x600")
        self.initalize()

    def initalize(self):
        self.canvas = Canvas(self)
        self.canvas.create_line(0, 30, 800, 30 )
        self.canvas.create_text(90, 58, text='Введите размер массива:')
        self.canvas.create_text(85, 15, text='Выберете тип сортировки:')
        self.canvas.create_text(550, 15, text='Выберете метод сортировки:')
        self.canvas.place(relx=0.0, rely=0.0, height=600, width=800)
        
        self.count = StringVar(self)
        self.w_count = Entry(self, textvariable=self.count)        
        self.w_count.place(relx = 0.2, rely=0.08, height=22, width=200)

        self.srt_type = StringVar(self)
        self.srt_type.set(sort_type[0])
        
        self.srt_method = StringVar(self)
        self.srt_method.set(sort_method[0])

        self.w_sort_method = OptionMenu(self, self.srt_method, *sort_method)
        self.w_sort_method.place(relx=0.8, rely=0.0, height=30, width=150)
        
        self.w_sort_type = OptionMenu(self, self.srt_type, *sort_type)
        self.w_sort_type.place(relx=0.2, rely=0.0, height=30, width=150)

        self.resizable(width=False, height=False)
        
        self.enter_arr = Text(self)
        self.enter_arr.place(relx = 0.02, rely=0.2, height=400, width=380)
        self.print_arr = Text(self)
        self.enter_arr.bind('<FocusIn>', self.focus_in)
        self.enter_arr.bind('<FocusOut>', self.focus_out)
        self.print_arr.place(relx = 0.51, rely=0.1, height=250, width=380)
        
        self.print_desc = Text(self)
        self.print_desc.place(relx = 0.51, rely=0.54, height=197, width=380)
        
        self.sort = Button(self, text='Отсортировать', command = self.run)
        self.sort.place(relx = 0.345, rely=0.9, height=30, width=120)
       
        self.clear = Button(self, text='Очистить')
        self.clear.bind('<Button - 1>', self.clear_t)
        self.clear.place(relx = 0.51, rely=0.9, height=30, width=120)
        
        self.comp = Button(self, text='?', command=self.about_prog)
        self.comp.place(relx = 0.9, rely=0.9, height=30, width=30)

        self.focus_out(None)
        
        self.title('Программа сортировки одномерного массива - СОМ')
        
        self.company = Label(self, text = 'Powered by ' + trade_mark, foreground='gray')
        self.company.place(relx = 0.34, rely=0.95, height=30, width=300)
        
        self.mainloop()

    def about_prog(self):
        mb.showinfo('О программе', 'Версия: 1.0\nЯзык интерфейса: Русский\nПроизводитель:'+trade_mark+'\nСредства разработки: язык Python(библиотека tkinter)')
    def is_arr(self):
        text = self.enter_arr.get(1.0, END).replace('\n', '')
        if text =='':
            return False
        elif text == placeholder:
            return False
        else:
            return True
        
    def focus_in(self, event):
        if not self.is_arr():
            self.enter_arr.delete(1.0, END)
        

    def focus_out(self, event):
        if not self.is_arr():
            self.enter_arr.insert(1.0, placeholder)
    
    def get_arr(self):
        return self.enter_arr.get(1.0, END)

    def set_description(self, desc):
        self.print_desc.insert(1.0,  desc)

    def get_size_arr(self):
        return self.count.get()

    def set_sorted_arr(self, arr):
        self.print_arr.delete(1.0, END)
        self.print_arr.insert(1.0,  arr)

    def get_srt_type(self):
        return self.srt_type.get()

    def get_srt_method(self):
        return self.srt_method.get()

    def error(self, err):
        mb.showerror('Error!', err)

    def run(self):     
        array = self.get_arr()
        method = self.get_srt_method()
        sorter, desc = Matcher.match_method(method)
        try:
            norm = Cast.get_arr(array)
            size = self.get_size_arr()
            if int(size) != len(norm):
                mb.showwarning('Warning!', 'Введенный размер массива не совпадает с настоящим. Вы ввели размер: '+str(size)+', но его реальный размер: '+str(len(norm)))
            srt = Sort(sorter, norm)
            res = srt.sort()
            srt_type = self.get_srt_type()
            if Matcher.match_type(srt_type) == TO_UP:
                a = Cast.set_arr(res)
                self.set_sorted_arr(a)
            else:
                b = Cast.set_arr(res[::-1])
                self.set_sorted_arr(b)
            self.set_description(desc)
        except ValueError:
            mb.showerror('Error!', 'Пожалуйста, проверьте введенные данные.')
        
            
    def clear_t(self, event):
        self.enter_arr.delete(1.0, END)
        self.print_arr.delete(1.0, END)
        self.print_desc.delete(1.0, END)
        self.count.set('')
        self.srt_type.set(sort_type[0])
        self.srt_method.set(sort_method[0])
        self.focus_out(None)

if __name__ == "__main__":
    mw = MainWindow()

