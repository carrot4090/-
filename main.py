

"""
Программа для диагностики систем водоснабжения
"""


import tkinter as tk
from tkinter import messagebox
import os



#ФУНКЦИИ ДИАГНОСТИКИ (ЛОГИКА ПРОВЕРКИ)


def check_vbr():
    """Функция диагностики Башни Рожновского"""
    # Опрашиваем пользователя через окна Да/Нет
    q1 = messagebox.askyesno("Диагностика ВБР", "Бак течет или заржавел?")
    q2 = messagebox.askyesno("Диагностика ВБР", "Зимой на башне много льда?")
    q3 = messagebox.askyesno("Диагностика ВБР", "Башня стоит криво или наклонилась?")

    # Логика вердиктов
    if q3:
        res = "ВЕРДИКТ: Опасно! Проблема с фундаментом ВБР.\nСОВЕТ: Срочно прекратите эксплуатацию и вызовите геодезистов."
        messagebox.showerror("Результат диагностики ВБР", res)
    elif q1 or q2:
        res = "ВЕРДИКТ: Нужен текущий ремонт конструкции.\nСОВЕТ: Проведите сварочные работы и обновите теплоизоляцию."
        messagebox.showwarning("Результат диагностики ВБР", res)
    else:
        res = "ВЕРДИКТ: ВБР в хорошем состоянии!\nСОВЕТ: Проводите плановый осмотр раз в полгода."
        messagebox.showinfo("Результат диагностики ВБР", res)


def check_vns():
    """Функция диагностики Насосной Станции"""
    q1 = messagebox.askyesno("Диагностика ВНС", "Насос гудит, но вода не идет?")
    q2 = messagebox.askyesno("Диагностика ВНС", "Выбивает электричество при включении?")
    q3 = messagebox.askyesno("Диагностика ВНС", "Насос включается слишком часто?")

    if q2:
        res = "ВЕРДИКТ: Критическая поломка электрики ВНС.\nСОВЕТ: Проверьте обмотки двигателя на пробой и состояние пускателей."
        messagebox.showerror("Результат диагностики ВНС", res)
    elif q1 or q3:
        res = "ВЕРДИКТ: Проверьте клапаны и фильтры ВНС.\nСОВЕТ: Очистите входной фильтр и проверьте исправность обратного клапана."
        messagebox.showwarning("Результат диагностики ВНС", res)
    else:
        res = "ВЕРДИКТ: ВНС работает исправно!\nСОВЕТ: Проверьте давление в гидроаккумуляторе."
        messagebox.showinfo("Результат диагностики ВНС", res)


def check_tp():
    """Функция проверки соответствия Типовому Проекту"""
    q1 = messagebox.askyesno("Сверка с ТП", "Напор воды ниже проектного?")
    q2 = messagebox.askyesno("Сверка с ТП", "Оборудование не совпадает с ТП?")
    q3 = messagebox.askyesno("Сверка с ТП", "Нагрузка выше проектной?")

    if q3:
        res = "ВЕРДИКТ: ТП устарел, система перегружена.\nСОВЕТ: Необходимо заказать проект модернизации и увеличить мощность насосов."
        messagebox.showerror("Результат сверки ТП", res)
    elif q1 or q2:
        res = "ВЕРДИКТ: Выявлено несоответствие нормам ТП.\nСОВЕТ: Замените нештатное оборудование на рекомендованное проектом."
        messagebox.showwarning("Результат сверки ТП", res)
    else:
        res = "ВЕРДИКТ: Объект полностью соответствует ТП.\nСОВЕТ: При замене узлов используйте только запчасти из спецификации."
        messagebox.showinfo("Результат сверки ТП", res)


def check_pipes():
    """Функция диагностики Трубопровода"""
    q1 = messagebox.askyesno("Диагностика Сетей", "Есть ли мокрые пятна на грунте над трассой?")
    q2 = messagebox.askyesno("Диагностика Сетей", "Давление падает без видимых причин?")
    q3 = messagebox.askyesno("Диагностика Сетей", "Вода идет грязная или с песком?")

    if q1:
        res = "ВЕРДИКТ: Срочно! Обнаружен явный порыв сети.\nСОВЕТ: Перекройте участок задвижками и вызывайте аварийную бригаду."
        messagebox.showerror("Результат диагностики Сетей", res)
    elif q2 or q3:
        res = "ВЕРДИКТ: Возможна скрытая утечка или износ труб.\nСОВЕТ: Проведите акустический поиск утечек или промойте сеть."
        messagebox.showwarning("Результат диагностики Сетей", res)
    else:
        res = "ВЕРДИКТ: Трубопровод в норме.\nСОВЕТ: Контролируйте расход воды на наличие скрытых потерь."
        messagebox.showinfo("Результат диагностики Сетей", res)


def check_valves():
    """Функция диагностики Запорной Арматуры"""
    q1 = messagebox.askyesno("Диагностика Арматуры", "Задвижка закрывается не до конца?")
    q2 = messagebox.askyesno("Диагностика Арматуры", "Видна коррозия на штоке или штурвале?")
    q3 = messagebox.askyesno("Диагностика Арматуры", "Есть течь через сальниковое уплотнение?")

    if q1:
        res = "ВЕРДИКТ: Необходима ревизия или замена задвижки.\nСОВЕТ: Попробуйте 'промыть' седло или замените уплотнительный элемент."
        messagebox.showerror("Результат диагностики Арматуры", res)
    elif q3:
        res = "ВЕРДИКТ: Требуется подтяжка или замена сальника.\nСОВЕТ: Попробуйте подтянуть гайки сальника или замените набивку."
        messagebox.showwarning("Результат диагностики Арматуры", res)
    else:
        res = "ВЕРДИКТ: Арматура в рабочем состоянии!\nСОВЕТ: Смажьте шток графитовой смазкой для предотвращения коррозии."
        messagebox.showinfo("Результат диагностики Арматуры", res)

def check_well():
    """Функция диагностики Артезианской скважины"""
    q1 = messagebox.askyesno("Диагностика Скважины", "Снизился дебит (стало меньше воды)?")
    q2 = messagebox.askyesno("Диагностика Скважины", "В воде появился песок или мутность?")
    q3 = messagebox.askyesno("Диагностика Скважины", "Динамический уровень воды упал ниже насоса?")

    if q3:
        res = "ВЕРДИКТ: Критическое падение уровня!\nСОВЕТ: Срочно опустите насос ниже или ограничьте забор воды."
        messagebox.showerror("Результат диагностики Скважины", res)
    elif q1 or q2:
        res = "ВЕРДИКТ: Заиление или износ фильтра скважины.\nСОВЕТ: Рекомендуется промывка (эрлифт) или желонирование скважины."
        messagebox.showwarning("Результат диагностики Скважины", res)
    else:
        res = "ВЕРДИКТ: Скважина работает стабильно.\nСОВЕТ: Раз в год проводите замер статического уровня."
        messagebox.showinfo("Результат диагностики Скважины", res)

def check_rchv():
    """Функция диагностики Резервуара Чистой Воды (РЧВ)"""
    q1 = messagebox.askyesno("Диагностика РЧВ", "Нарушена герметичность люков или вентиляции?")
    q2 = messagebox.askyesno("Диагностика РЧВ", "В резервуаре появился осадок или налет?")
    q3 = messagebox.askyesno("Диагностика РЧВ", "Стенки имеют трещины или протечки?")

    if q3:
        res = "ВЕРДИКТ: Утечка ресурса!\nСОВЕТ: Опорожните резервуар и проведите гидроизоляцию швов."
        messagebox.showerror("Результат диагностики РЧВ", res)
    elif q1 or q2:
        res = "ВЕРДИКТ: Риск загрязнения воды.\nСОВЕТ: Проведите чистку и дезинфекцию хлорным раствором."
        messagebox.showwarning("Результат диагностики РЧВ", res)
    else:
        res = "ВЕРДИКТ: Резервуар в норме.\nСОВЕТ: Следите за исправностью поплавковых клапанов."
        messagebox.showinfo("Результат диагностики РЧВ", res)

def check_meter():
    """Функция диагностики Водомерного узла"""
    q1 = messagebox.askyesno("Диагностика Учета", "Счетчик запотел или внутри вода?")
    q2 = messagebox.askyesno("Диагностика Учета", "Истек срок государственной поверки?")
    q3 = messagebox.askyesno("Диагностика Учета", "Сорваны или повреждены пломбы?")

    if q3:
        res = "ВЕРДИКТ: Нарушение учета!\nСОВЕТ: Срочно вызовите инспектора для перепломбировки."
        messagebox.showerror("Результат диагностики Учета", res)
    elif q1 or q2:
        res = "ВЕРДИКТ: Прибор неисправен или нелегитимен.\nСОВЕТ: Замените счетчик или сдайте его в поверку."
        messagebox.showwarning("Результат диагностики Учета", res)
    else:
        res = "ВЕРДИКТ: Узел учета исправен.\nСОВЕТ: Снимайте показания в строго установленные сроки."
        messagebox.showinfo("Результат диагностики Учета", res)

def check_hydrant():
    """Функция диагностики Пожарного гидранта"""
    q1 = messagebox.askyesno("Диагностика ПГ", "Стенд гидранта заполнен водой (не работает слив)?")
    q2 = messagebox.askyesno("Диагностика ПГ", "Квадрат штока стерт или поврежден?")
    q3 = messagebox.askyesno("Диагностика ПГ", "Подъезд к гидранту заблокирован?")

    if q2:
        res = "ВЕРДИКТ: Гидрант неработоспособен!\nСОВЕТ: Требуется замена головки или всего гидранта."
        messagebox.showerror("Результат диагностики ПГ", res)
    elif q1 or q3:
        res = "ВЕРДИКТ: Нарушение правил эксплуатации.\nСОВЕТ: Очистите дренаж и обеспечьте беспрепятственный доступ."
        messagebox.showwarning("Результат диагностики ПГ", res)
    else:
        res = "ВЕРДИКТ: Гидрант исправен.\nСОВЕТ: Проводите проверку на водоотдачу дважды в год."
        messagebox.showinfo("Результат диагностики ПГ", res)

def check_chamber():
    """Функция диагностики Колодца (камеры)"""
    q1 = messagebox.askyesno("Диагностика Колодца", "Плита перекрытия разрушена или сдвинута?")
    q2 = messagebox.askyesno("Диагностика Колодца", "В колодце скопился мусор или грунт?")
    q3 = messagebox.askyesno("Диагностика Колодца", "Лестница (скобы) заржавела и шатается?")

    if q1 or q3:
        res = "ВЕРДИКТ: Опасно для жизни персонала!\nСОВЕТ: Замените плиту и лестницу перед спуском внутрь."
        messagebox.showerror("Результат диагностики Колодца", res)
    elif q2:
        res = "ВЕРДИКТ: Колодец засорен.\nСОВЕТ: Организуйте очистку камеры от посторонних предметов."
        messagebox.showwarning("Результат диагностики Колодца", res)
    else:
        res = "ВЕРДИКТ: Состояние колодца удовлетворительное.\nСОВЕТ: Проверьте наличие крышки люка."
        messagebox.showinfo("Результат диагностики Колодца", res)

def check_filter():
    """Функция диагностики Системы фильтрации"""
    q1 = messagebox.askyesno("Диагностика Фильтров", "Давление на выходе упало?")
    q2 = messagebox.askyesno("Диагностика Фильтров", "Вода на выходе пахнет или изменила цвет?")
    q3 = messagebox.askyesno("Диагностика Фильтров", "Автоматика промывки выдает ошибку?")

    if q3:
        res = "ВЕРДИКТ: Сбой системы управления.\nСОВЕТ: Перезагрузите контроллер или замените управляющий клапан."
        messagebox.showerror("Результат диагностики Фильтров", res)
    elif q1 or q2:
        res = "ВЕРДИКТ: Истощение ресурса загрузки.\nСОВЕТ: Проведите принудительную промывку или замените фильтрующий сорбент."
        messagebox.showwarning("Результат диагностики Фильтров", res)
    else:
        res = "ВЕРДИКТ: Система очистки работает штатно.\nСОВЕТ: Следите за уровнем реагентов в баках."
        messagebox.showinfo("Результат диагностики Фильтров", res)


def check_panel():
    """Функция диагностики Электрощита"""
    q1 = messagebox.askyesno("Диагностика Щита", "Слышен сильный гул или треск внутри?")
    q2 = messagebox.askyesno("Диагностика Щита", "Чувствуется запах горелой изоляции?")
    q3 = messagebox.askyesno("Диагностика Щита", "Контакты автоматов потемнели от нагрева?")

    if q2 or q3:
        res = "ВЕРДИКТ: Критично! Опасность возгорания щита.\nСОВЕТ: Немедленно обесточьте щит и замените подгоревшие детали."
        messagebox.showerror("Результат диагностики Щита", res)
    elif q1:
        res = "ВЕРДИКТ: Проверьте затяжку контактов и пускатели.\nСОВЕТ: Протяните все винтовые соединения и проверьте плотность посадки."
        messagebox.showwarning("Результат диагностики Щита", res)
    else:
        res = "ВЕРДИКТ: Электрощит работает штатно!\nСОВЕТ: Проверьте отсутствие пыли и влаги внутри корпуса."
        messagebox.showinfo("Результат диагностики Щита", res)

def open_presentation():
    """Функция для открытия презентации лер.pptx"""
    try:
        # Пытаемся открыть файл стандартной программой Windows
        os.startfile("проект.pptx")
    except FileNotFoundError:
        # Если файла нет в папке с программой, выводим ошибку
        messagebox.showerror("Ошибка", "Файл 'проект.pptx' не найден в папке с программой!")

def calc_repair():
    """Функция калькулятора стоимости ремонта"""
    # Создаем новое окно поверх основного
    calc_window = tk.Toplevel(root)
    calc_window.title("Калькулятор ремонта")
    calc_window.geometry("300x250")

    # Устанавливаем иконку именно для этого окна
    try:
        # Можно использовать ту же иконку или другую, например 'calc.ico'
        calc_window.iconbitmap("calc.ico")
    except:
        # Если иконки нет, окно просто откроется со стандартным значком
        pass

    tk.Label(calc_window, text="Введите количество часов работы:").pack(pady=5)
    entry_trips = tk.Entry(calc_window)
    entry_trips.pack()

    tk.Label(calc_window, text="Стоимость часа (руб):").pack(pady=5)
    entry_price = tk.Entry(calc_window)
    entry_price.pack()

    def calculate():
        try:
            # Считаем итог
            res = float(entry_trips.get()) * float(entry_price.get())
            messagebox.showinfo("Расчет", f"Ориентировочная стоимость: {res} руб.")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, вводите только числа!")

    tk.Button(calc_window, text="Рассчитать итог", command=calculate, bg="lightgreen").pack(pady=15)







# РАЗДЕЛ 2: ГРАФИЧЕСКИЙ ИНТЕРФЕЙС (GUI)

root = tk.Tk()
root.title("Water Equipment Diagnostics")
root.geometry("620x800")

try:
    root.iconbitmap("my_icon.ico")
except:
    pass

# Самая верхняя надпись
label_top = tk.Label(root, text="ВЫБЕРИТЕ ФУНКЦИЮ", font=("Arial", 12, "bold"), fg="blue", pady=5)
label_top.pack()

# ОСНОВНОЙ ЗАГОЛОВОК ДИАГНОСТИКИ
label_diag = tk.Label(root, text="ДИАГНОСТИКА ОБОРУДОВАНИЯ", font=("Arial", 14, "bold"), pady=10)
label_diag.pack()

# Контейнер для кнопок диагностики (СЕТКА)
frame_diag = tk.Frame(root)
frame_diag.pack(pady=5)

# --- ЛЕВАЯ КОЛОНКА ---
tk.Button(frame_diag, text="Диагностика ВБР", width=25, height=2, command=check_vbr).grid(row=0, column=0, padx=10, pady=5)
tk.Button(frame_diag, text="Диагностика ВНС", width=25, height=2, command=check_vns).grid(row=1, column=0, padx=10, pady=5)
tk.Button(frame_diag, text="Соответствие ТП", width=25, height=2, command=check_tp).grid(row=2, column=0, padx=10, pady=5)
tk.Button(frame_diag, text="Диагностика Сетей", width=25, height=2, command=check_pipes).grid(row=3, column=0, padx=10, pady=5)
tk.Button(frame_diag, text="Запорная Арматура", width=25, height=2, command=check_valves).grid(row=4, column=0, padx=10, pady=5)
tk.Button(frame_diag, text="Электрощитовая", width=25, height=2, command=check_panel).grid(row=5, column=0, padx=10, pady=5)

# --- ПРАВАЯ КОЛОНКА ---
tk.Button(frame_diag, text="Артскважина", width=25, height=2, command=check_well).grid(row=0, column=1, padx=10, pady=5)
tk.Button(frame_diag, text="Резервуар РЧВ", width=25, height=2, command=check_rchv).grid(row=1, column=1, padx=10, pady=5)
tk.Button(frame_diag, text="Водомерный узел", width=25, height=2, command=check_meter).grid(row=2, column=1, padx=10, pady=5)
tk.Button(frame_diag, text="Пожарный гидрант", width=25, height=2, command=check_hydrant).grid(row=3, column=1, padx=10, pady=5)
tk.Button(frame_diag, text="Водопроводный колодец", width=25, height=2, command=check_chamber).grid(row=4, column=1, padx=10, pady=5)
tk.Button(frame_diag, text="Система фильтрации", width=25, height=2, command=check_filter).grid(row=5, column=1, padx=10, pady=5)

# --- ОТДЕЛЬНЫЙ ЗАГОЛОВОК ДЛЯ ПРОЧИХ ФУНКЦИЙ ---
label_other = tk.Label(root, text="ПРОЧИЕ ФУНКЦИИ", font=("Arial", 12, "bold"), fg="black", pady=15)
label_other.pack()

# Блок сервисных кнопок
frame_service = tk.Frame(root)
frame_service.pack(pady=5)

tk.Button(frame_service, text="КАЛЬКУЛЯТОР РЕМОНТА", width=54, height=1, command=calc_repair, font=("Arial", 10, "bold")).pack(pady=3)
tk.Button(frame_service, text="ОТКРЫТЬ ПРЕЗЕНТАЦИЮ", width=54, height=1, command=open_presentation, font=("Arial", 10, "bold")).pack(pady=3)
tk.Button(frame_service, text="ВЫХОД", width=54, height=1, command=root.quit, font=("Arial", 10, "bold"), fg="red").pack(pady=10)

root.mainloop()
