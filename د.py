import sys
import sqlite3

from PyQt5.QtCore import Qt, QSize, QRect, QTimer
from PyQt5.QtGui import QPixmap, QFontDatabase, QPainter, QPen, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QSpacerItem,
    QSizePolicy, QLabel, QPushButton, QLineEdit, QComboBox, QDialog, QFrame,
    QScrollArea, QStackedWidget, QRadioButton, QButtonGroup, QMessageBox, QInputDialog
)
class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle('ورود')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)

        self.background_label = QLabel(self)
        self.set_background_image()
        layout.addWidget(self.background_label, 0, Qt.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # ایجاد کادر دور دکمه‌ها
        self.button_frame = QFrame(self)
        self.button_frame.setStyleSheet("QFrame { border: 5px solid #628B35; border-radius: 10px; padding: 20px; }")
        button_layout = QVBoxLayout(self.button_frame)

        self.button_login = QPushButton('ورود به حساب کاربری', self)
        self.button_login.setStyleSheet(self.button_style())
        self.button_login.setFixedHeight(70)
        self.button_login.setFixedWidth(350)
        self.button_login.clicked.connect(self.show_home_page)  # اتصال دکمه به متد نمایش صفحه خانه
        button_layout.addWidget(self.button_login, 0, Qt.AlignCenter)

        self.button_create_account = QPushButton('ایجاد حساب کاربری', self)
        self.button_create_account.setStyleSheet(self.button_style())
        self.button_create_account.setFixedHeight(70)
        self.button_create_account.setFixedWidth(350)
        self.button_create_account.clicked.connect(self.show_user_registration_page)  # تغییر نام این متد
        button_layout.addWidget(self.button_create_account, 0, Qt.AlignCenter)

        self.button_frame.setLayout(button_layout)
        layout.addWidget(self.button_frame, 0, Qt.AlignCenter)

        layout.addStretch()
        self.setLayout(layout)

    def set_background_image(self):
        pixmap = QPixmap(r"C:\Users\User\Desktop\5.png")
        new_size = QSize(1800, 700)
        self.background_label.setPixmap(pixmap.scaled(new_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setFixedSize(new_size)

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 20px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif; 
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
            transform: translateY(-2px);
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
            transform: translateY(1px);
        }
        """

    def show_home_page(self):
        home_page = HomePage(self.stacked_widget)  # صفحه‌ای که باید باز شود
        self.stacked_widget.addWidget(home_page)
        self.stacked_widget.setCurrentWidget(home_page)

    def show_user_registration_page(self):
        user_registration_page = UserRegistration(self)  # ایجاد یک نمونه از UserRegistration با ارجاع به LoginWindow
        self.stacked_widget.addWidget(user_registration_page)  # افزودن صفحه به stacked_widget
        self.stacked_widget.setCurrentWidget(user_registration_page)  # نمایش صفحه UserRegistration
class HomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("صفحه اصلی")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # ایجاد یک ویجت برای قرار دادن فیلدها و لیبل‌ها در وسط
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignCenter)  # برای مرکز چین کردن فیلدها و لیبل‌ها

        # عنوان صفحه داخل form_layout قرار می‌گیرد
        self.title_label = QLabel("خوش آمدید !", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet(self.title_style())
        form_layout.addWidget(self.title_label)

        # ایجاد فیلدهای ورودی برای ایمیل و رمز عبور
        self.email_label = QLabel("ایمیل:", self)
        self.email_label.setStyleSheet(self.label_style())
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("ایمیل خود را وارد کنید")
        self.email_input.setStyleSheet(self.input_style())  # کادر ورودی ایمیل
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)

        self.password_label = QLabel("رمز عبور:", self)
        self.password_label.setStyleSheet(self.label_style())
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # مخفی کردن رمز عبور
        self.password_input.setPlaceholderText("رمز عبور خود را وارد کنید")
        self.password_input.setStyleSheet(self.input_style())  # کادر ورودی رمز عبور
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)

        # ایجاد یک QWidget برای فرم
        frame = QWidget(self)
        frame.setStyleSheet("""
            QWidget {
                background-color: #f4f9f4;
                border-radius: 10px;
                padding: 20px;
            }
        """)

        # اضافه کردن فرم به داخل فریم
        frame.setLayout(form_layout)

        # تنظیم QSizePolicy برای تغییر اندازه فریم
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # اجازه تغییر اندازه افقی و عمودی

        # اضافه کردن فریم به Layout اصلی
        layout.addWidget(frame)

        # دکمه‌ها را به پایین صفحه منتقل می‌کنیم
        self.button_layout = QHBoxLayout()

        self.button_logout = QPushButton("بازگشت", self)
        self.button_logout.setStyleSheet(self.button_style())
        self.button_logout.clicked.connect(self.logout)
        self.button_layout.addWidget(self.button_logout)

        self.button_login = QPushButton("ورود", self)
        self.button_login.setStyleSheet(self.button_style())
        self.button_login.clicked.connect(self.login_user)  # متصل کردن دکمه ورود به متد login_user
        self.button_layout.addWidget(self.button_login)

        # اضافه کردن دکمه‌ها در پایین صفحه
        layout.addLayout(self.button_layout)


        self.setLayout(layout)

    def title_style(self):
        return """
        font-size: 24px; 
        font-weight: bold; 
        color: #344C3D; 
        font-family: 'Vazir', sans-serif; 
        margin: 20px; 
        text-align: center;
        """

    def label_style(self):
        return """
        font-size: 16px; 
        font-weight: bold; 
        color: #344C3D; 
        font-family: 'Vazir', sans-serif; 
        margin-right: 10px; 
        """

    def input_style(self):
        return """
        QLineEdit {
            font-size: 16px; 
            padding: 10px; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            font-family: 'Vazir', sans-serif; 
            text-align: right;
            min-width: 400px;  
            max-width: 500px;  
            height: 45px;  
            background-color: #f1f1f1;
        }
        QLineEdit:focus {
            border-color: #738A6E;
            background-color: #e5f3e5;
        }
        """

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E;
            color: #ffffff;
            border: 2px solid #8EA58C;
            border-radius: 15px;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            font-family: 'Vazir', sans-serif;
            margin: 10px;
        }
        QPushButton:hover {
            background-color: #8EA58C;
            color: #344C3D;
        }
        QPushButton:pressed {
            background-color: #BFCFBB;
            color: #344C3D;
        }
        """

    def login_user(self):
        email = self.email_input.text()
        password = self.password_input.text()

        # اتصال به دیتابیس
        connection = sqlite3.connect("create.db")
        cursor = connection.cursor()

        # جستجو برای ایمیل و رمز عبور
        cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()  # اگر کاربر پیدا شد، داده‌ها را بر می‌گرداند

        connection.close()

        if user:
            # انتقال به صفحه پروفایل
            user_data = {
                'name': user[1],
                'age': user[2],
                'weight': user[3],
                'height': user[4],
                'gender': user[5],
                'activity_level': user[6],
                'email': user[7],
                'daily_calories': user[9]
            }
            profile_page = ProfilePage(user_data, self)
            self.stacked_widget.addWidget(profile_page)
            self.stacked_widget.setCurrentWidget(profile_page)
        else:
            QMessageBox.warning(self, "خطا", "ایمیل یا رمز عبور اشتباه است.")


    def logout(self):
        # برای خارج شدن از حساب کاربری و بازگشت به صفحه ورود
        self.stacked_widget.setCurrentIndex(3)
class EditProfileWindow(QDialog):
    def __init__(self, user_data, update_callback, profile_page):
        super().__init__()

        self.setWindowTitle("ویرایش اطلاعات پروفایل")
        self.setGeometry(600, 250, 700, 700)  # تنظیم ابعاد پنجره

        self.user_data = user_data  # اطلاعات کاربر که قرار است ویرایش شود
        self.update_callback = update_callback  # تابعی برای به‌روزرسانی اطلاعات در صفحه پروفایل
        self.profile_page = profile_page  # ارجاع به ProfilePage برای دسترسی به متدهای محاسبه BMI و کالری

        # ایجاد ویجت‌ها و فرم ویرایش
        self.create_widgets()
    def create_widgets(self):
        # چیدمان اصلی فرم
        form_layout = QFormLayout()
        form_layout.setSpacing(50)

        # ورودی‌ها برای ویرایش
        self.name_input = QLineEdit(self.user_data['name'])
        self.age_input = QLineEdit(str(self.user_data['age']))
        self.weight_input = QLineEdit(str(self.user_data['weight']))
        self.height_input = QLineEdit(str(self.user_data['height']))

        # لیست انتخاب جنسیت
        self.gender_input = QComboBox()
        self.gender_input.addItems(['مرد', 'زن'])
        self.gender_input.setCurrentText(self.user_data['gender'])

        # لیست انتخاب سطح فعالیت
        self.activity_level_input = QComboBox()
        self.activity_level_input.addItems(['کم تحرک', 'متوسط', 'پر تحرک'])
        self.activity_level_input.setCurrentText(self.user_data['activity_level'])

        # اضافه کردن فیلدهای ورودی به فرم
        form_layout.addRow("اسم", self.name_input)
        form_layout.addRow("سن", self.age_input)
        form_layout.addRow("وزن (kg)", self.weight_input)
        form_layout.addRow("قد (cm)", self.height_input)
        form_layout.addRow("جنسیت", self.gender_input)
        form_layout.addRow("سطح فعالیت", self.activity_level_input)

        # دکمه ذخیره تغییرات
        self.save_button = QPushButton("ذخیره تغییرات")
        self.save_button.clicked.connect(self.save_changes)

        # دکمه لغو برای بازگشت به صفحه پروفایل بدون ذخیره تغییرات
        self.cancel_button = QPushButton("لغو")
        self.cancel_button.clicked.connect(self.close)

        # چیدمان دکمه‌ها (ذخیره و لغو)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)

        # چیدمان اصلی پنجره
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # اعمال استایل‌ها
        self.apply_styles()

        # تنظیم اندازه یکسان برای فیلدها
        self.set_field_widths()

    def set_field_widths(self):
        """ تنظیم عرض یکسان برای همه فیلدها """
        fixed_width = 250  # عرض ثابت برای فیلدها

        # تنظیم عرض فیلدها
        self.name_input.setMinimumWidth(fixed_width)
        self.age_input.setMinimumWidth(fixed_width)
        self.weight_input.setMinimumWidth(fixed_width)
        self.height_input.setMinimumWidth(fixed_width)
        self.gender_input.setMinimumWidth(fixed_width)
        self.activity_level_input.setMinimumWidth(fixed_width)

    def apply_styles(self):
        # استایل‌دهی به ورودی‌ها (QLineEdit)
        self.name_input.setStyleSheet(self.input_style())
        self.age_input.setStyleSheet(self.input_style())
        self.weight_input.setStyleSheet(self.input_style())
        self.height_input.setStyleSheet(self.input_style())

        # استایل‌دهی به لیست‌های کشویی (QComboBox)
        self.gender_input.setStyleSheet(self.combo_box_style())
        self.activity_level_input.setStyleSheet(self.combo_box_style())

        # استایل‌دهی به دکمه‌ها (QPushButton)
        self.save_button.setStyleSheet(self.save_button_style())
        self.cancel_button.setStyleSheet(self.cancel_button_style())

        # استایل‌دهی به لیبل‌ها
        self.setStyleSheet(self.label_style())

        # استایل‌دهی به پنجره
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f4;
                font-family: 'Vazir', sans-serif;
            }
        """)

    def input_style(self):
        return """
        QLineEdit {
            font-size: 16px; 
            padding: 5px; 
            border: 2px solid #8EA58C; 
            border-radius: 5px; 
            font-family: 'Vazir', sans-serif;
        }
        """

    def combo_box_style(self):
        return """
        QComboBox {
            font-size: 16px; 
            padding: 5px; 
            border: 2px solid #8EA58C; 
            border-radius: 5px; 
            font-family: 'Vazir', sans-serif;
        }
        """

    def save_button_style(self):
        return """
        QPushButton {
            background-color: #3A8232;
            color: #ffffff;
            border: 2px solid #8EA58C;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            font-family: 'Vazir', sans-serif;
        }
        QPushButton:hover {
            background-color: #4B9D3D;
            color: #ffffff;
        }
        QPushButton:pressed {
            background-color: #2F6A25;
            color: #ffffff;
        }
        """

    def cancel_button_style(self):
        return """
        QPushButton {
            background-color: #7A1008;
            color: #ffffff;
            border: 2px solid #8EA58C;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            font-family: 'Vazir', sans-serif;
        }
        QPushButton:hover {
            background-color: #9B1410;
            color: #ffffff;
        }
        QPushButton:pressed {
            background-color: #5C0A07;
            color: #ffffff;
        }
        """

    def label_style(self):
        return """
        QLabel {
            font-size: 16px;
            font-weight: bold;
            color: #344C3D;
            font-family: 'Vazir', sans-serif;
            margin-right: 10px;
        }
        """

    from PyQt5.QtCore import QTimer

    from PyQt5.QtCore import QTimer

    def save_changes(self):
        try:
            # گرفتن مقادیر جدید از ورودی‌ها
            new_data = {
                'name': self.name_input.text(),
                'age': int(self.age_input.text()),  # تبدیل سن به عدد صحیح
                'weight': float(self.weight_input.text()),  # تبدیل وزن به عدد اعشاری
                'height': float(self.height_input.text()),  # تبدیل قد به عدد اعشاری
                'gender': self.gender_input.currentText(),
                'activity_level': self.activity_level_input.currentText(),
                'email': self.user_data['email']  # ایمیل ثابت باقی می‌ماند
            }

            # محاسبه BMI جدید از طریق ProfilePage
            bmi_value = self.profile_page.calculate_bmi(new_data['weight'], new_data['height'])

            # محاسبه کالری جدید از طریق ProfilePage
            new_calories, calories_message = self.profile_page.calculate_daily_calories(
                new_data['weight'],
                new_data['height'],
                new_data['age'],
                new_data['gender'],
                new_data['activity_level'],
                bmi_value
            )

            # ذخیره تغییرات در دیتابیس
            self.update_user_data_in_db(new_data, new_calories)

            # به‌روزرسانی اطلاعات در صفحه پروفایل
            self.update_callback(new_data)

            # استفاده از QTimer برای بسته شدن پنجره بعد از 100 میلی‌ثانیه
            QTimer.singleShot(100, self.close)

        except ValueError as e:
            # اگر خطای ورودی بود، به‌کاربر اطلاع بدهید
            print(f"Error: {e}")
            error_message = QLabel(f"خطا: {str(e)}")
            error_message.setStyleSheet("color: red; font-weight: bold;")
            self.layout().addWidget(error_message)

        except Exception as e:
            # در صورت بروز خطای غیرمنتظره
            print(f"Unexpected error: {e}")
            error_message = QLabel(f"خطای غیرمنتظره: {str(e)}")
            error_message.setStyleSheet("color: red; font-weight: bold;")
            self.layout().addWidget(error_message)

    def update_user_data_in_db(self, new_data, new_calories):
        """ این متد برای ذخیره اطلاعات جدید کاربر و کالری‌های جدید در دیتابیس است. """
        try:
            # اتصال به دیتابیس
            connection = sqlite3.connect("create.db")
            cursor = connection.cursor()

            # آپدیت اطلاعات کاربر در دیتابیس
            cursor.execute('''
                  UPDATE users
                  SET name = ?, age = ?, weight = ?, height = ?, gender = ?, activity_level = ?, daily_calories = ?
                  WHERE email = ?
              ''', (new_data['name'], new_data['age'], new_data['weight'], new_data['height'],
                    new_data['gender'], new_data['activity_level'], new_calories, new_data['email']))

            # ذخیره تغییرات
            connection.commit()
            connection.close()

        except sqlite3.Error as e:
            # در صورت بروز خطا در ارتباط با دیتابیس، پیام خطا نمایش داده می‌شود
            print(f"Error updating user data in database: {e}")
            raise e
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QWidget

class CalorieProgressCircle(QWidget):
    def __init__(self, target_calories=1628):
        super().__init__()
        self.consumed_calories = 0  # کالری مصرف شده فعلی
        self.target_calories = target_calories  # هدف کالری
        self.setMinimumSize(200, 200)  # اندازه دایره
        self.setWindowTitle("دایره پیشرفت کالری")
        self.saved_calories = 0  # متغیر برای ذخیره کالری‌ها

    def setCalories(self, calories):
        self.consumed_calories = calories
        self.saved_calories = calories  # ذخیره کالری‌های جدید در متغیر
        self.update()  # بروزرسانی ویجت و بازخوانی paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # دایره بیرونی با رنگ و ضخامت جدید
        outer_pen = QPen(Qt.lightGray, 20)  # رنگ روشن و ضخامت 20 برای دایره بیرونی
        outer_pen.setCapStyle(Qt.RoundCap)  # ایجاد گوشه‌های گرد
        painter.setPen(outer_pen)
        rect = QRect(20, 20, 160, 160)
        painter.drawEllipse(rect)

        # محاسبه درصد
        percent = self.consumed_calories / self.target_calories if self.target_calories else 0
        angle = int(360 * percent * 16)

        # تغییر رنگ دایره پیشرفت بر اساس درصد
        if percent <= 0.5:
            # رنگ سبز برای درصد کمتر از 50
            progress_color = Qt.green
        else:
            # رنگ قرمز برای درصد بیشتر از 50
            progress_color = Qt.red

        # دایره پیشرفت با رنگ پویا و ضخامت بیشتر
        progress_pen = QPen(progress_color, 20)  # رنگ پویا و ضخامت بیشتر
        progress_pen.setCapStyle(Qt.RoundCap)  # گوشه‌های گرد برای دایره پیشرفت
        painter.setPen(progress_pen)
        painter.drawArc(rect, 90 * 16, -angle)

        # اضافه کردن متن با فونت و رنگ جدید
        painter.setPen(Qt.black)
        font = QFont("Verdana", 8, QFont.Bold)  # تغییر فونت به Verdana
        painter.setFont(font)
        text = f"{self.consumed_calories} / {self.target_calories} کالری"
        painter.drawText(rect, Qt.AlignCenter, text)

    def getSavedCalories(self):
        return self.saved_calories  # متد برای بازگرداندن کالری ذخیره شده

class FoodInfoDialog(QDialog):
    def __init__(self, food_name, food_weight, calories, sugar, carbs, fat, user_weight, parent=None):
        super().__init__(parent)
        self.user_weight = user_weight  # دریافت وزن کاربر
        self.setWindowTitle(f"اطلاعات غذا: {food_name}")
        self.setLayout(QVBoxLayout())

        # تنظیم سایز ثابت پنجره
        self.setFixedSize(700, 700)

        # نمایش نام غذا و حجم
        self.name_label = QLabel(f"نام غذا: {food_name}", self)
        self.name_label.setStyleSheet(self.value_label_style())
        self.layout().addWidget(self.create_styled_box(self.name_label))

        self.weight_label = QLabel(f"حجم وارد شده: {food_weight} گرم", self)
        self.weight_label.setStyleSheet(self.value_label_style())
        self.layout().addWidget(self.create_styled_box(self.weight_label))

        # نمایش مقادیر تغذیه‌ای
        self.calories_label = QLabel(f"کالری: {calories:.2f} کیلوکالری", self)
        self.calories_label.setStyleSheet(self.value_label_style())
        self.layout().addWidget(self.create_styled_box(self.calories_label))

        self.sugar_label = QLabel(f"قند: {sugar:.2f} گرم", self)
        self.sugar_label.setStyleSheet(self.value_label_style())
        self.layout().addWidget(self.create_styled_box(self.sugar_label))

        self.carbs_label = QLabel(f"کربوهیدرات: {carbs:.2f} گرم", self)
        self.carbs_label.setStyleSheet(self.value_label_style())
        self.layout().addWidget(self.create_styled_box(self.carbs_label))

        self.fat_label = QLabel(f"چربی: {fat:.2f} گرم", self)
        self.fat_label.setStyleSheet(self.value_label_style())
        self.layout().addWidget(self.create_styled_box(self.fat_label))

        walking_time = self.calculate_walking_time(calories)
        self.walking_time_label = QLabel(
            f"برای سوزاندن {calories:.2f} کیلوکالری، به طور تقریبی به {walking_time:.1f} دقیقه پیاده‌روی نیاز است.",
            self)
        self.walking_time_label.setStyleSheet(self.walking_time_label_style())  # تغییر استایل متن پیاده‌روی
        self.layout().addWidget(self.create_styled_box(self.walking_time_label))

        # دکمه‌ها: بازگشت و ثبت
        self.button_layout = QHBoxLayout()

        self.back_button = QPushButton("بازگشت", self)
        self.back_button.setStyleSheet(self.button_style())
        self.back_button.clicked.connect(self.close)  # بسته شدن دیالوگ
        self.button_layout.addWidget(self.back_button)

        self.submit_button = QPushButton("ثبت", self)
        self.submit_button.setStyleSheet(self.button_style())
        self.submit_button.clicked.connect(self.submit_food)  # ثبت غذا
        self.button_layout.addWidget(self.submit_button)

        self.layout().addLayout(self.button_layout)

    def create_styled_box(self, widget):
        """Create a styled container box with a light background and padding around the widget"""
        container = QWidget(self)
        container_layout = QVBoxLayout(container)
        container_layout.addWidget(widget)
        container.setStyleSheet("""
            background-color: #F7F7F7;  /* پس‌زمینه شیری */
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 20px;  /* فاصله بین هر بخش */
        """)
        return container

    def calculate_walking_time(self, calories):
        # فرض می‌کنیم که یک فرد به طور متوسط 5 کیلوکالری در هر دقیقه پیاده‌روی مصرف می‌کند
        calories_per_minute = 5

        # زمان پیاده‌روی با توجه به وزن کاربر و کالری مصرفی
        walking_time = (calories / calories_per_minute) * (self.user_weight / 70)  # فرض بر اینکه وزن متوسط 70 کیلوگرم است
        return walking_time

    def submit_food(self):
        # ارسال اطلاعات غذا به صفحه MealInputDialog
        food_name = self.name_label.text().split(":")[1].strip()
        calories = float(self.calories_label.text().split(":")[1].strip().split()[0])  # استخراج کالری
        sugar = float(self.sugar_label.text().split(":")[1].strip().split()[0])  # استخراج قند
        carbs = float(self.carbs_label.text().split(":")[1].strip().split()[0])  # استخراج کربوهیدرات
        fat = float(self.fat_label.text().split(":")[1].strip().split()[0])  # استخراج چربی

        # به روز رسانی لیست غذاهای وارد شده در MealInputDialog
        if hasattr(self.parent(), "add_food_to_list"):
            self.parent().add_food_to_list(food_name, calories, sugar, carbs, fat)

        self.close()

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif; 
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
        }
        """

    def value_label_style(self):
        return """
        font-size: 16px; 
        color: #000000;  /* رنگ سیاه برای همه مقادیر */
        font-family: 'Vazir', sans-serif; 
        margin: 0;
        """

    def walking_time_label_style(self):
        return """
        font-size: 16px;  /* سایز بزرگتر برای تاکید */
        color: #006400;  /* رنگ سبز پررنگ */
        font-family: 'Vazir', sans-serif;
        font-weight: bold;  /* بولد بودن فونت */
        margin: 0;
        """
class MealInputDialog(QDialog):
    def __init__(self, meal_name, user_weight, parent=None):
        super().__init__(parent)
        self.meal_name = meal_name
        self.user_weight = user_weight  # ذخیره وزن کاربر
        self.setWindowTitle(f"وارد کردن غذای {meal_name}")
        self.setLayout(QVBoxLayout())

        # تنظیم اندازه صفحه به 700x700 پیکسل
        self.resize(700, 700)  # تنظیم اندازه پنجره

        # لیست غذاهای وارد شده (حاوی نام غذا و کالری)
        self.food_list = []  # لیستی برای ذخیره غذاها (با کالری‌ها)
        self.food_counter = 1  # شمارنده برای شماره‌گذاری غذاها

        # ورودی نام غذا
        self.food_input = QLineEdit(self)
        self.food_input.setPlaceholderText("نام غذای خورده شده را وارد کنید...")
        self.food_input.setStyleSheet(self.input_style())  # Style for QLineEdit
        self.layout().addWidget(self.food_input)

        # ورودی حجم غذا
        self.food_weight_input = QLineEdit(self)
        self.food_weight_input.setPlaceholderText("حجم غذا را وارد کنید...")
        self.food_weight_input.setStyleSheet(self.input_style())  # Style for QLineEdit
        self.layout().addWidget(self.food_weight_input)

        # انتخاب واحد اندازه‌گیری
        self.unit_selector = QComboBox(self)
        self.unit_selector.addItem("گرم")
        self.unit_selector.addItem("کف دست")
        self.unit_selector.addItem("پیمانه")
        self.unit_selector.addItem("قاشق غذاخوری")  # اضافه کردن واحد "قاشق"
        self.unit_selector.addItem("لیوان")  # اضافه کردن واحد "لیوان"
        self.unit_selector.setStyleSheet(self.input_style())  # Apply same style to ComboBox
        self.layout().addWidget(self.unit_selector)

        # تیتر "فهرست غذاهای اضافه شده" (بدون فاصله از فیلد ورودی)
        self.food_list_label = QLabel("فهرست غذاهای اضافه شده:", self)
        self.food_list_label.setStyleSheet(self.label_style())  # Apply label style
        self.layout().addWidget(self.food_list_label)

        # خط افقی برای جداسازی تیتر از لیست غذاها
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.layout().addWidget(self.line)

        # ایجاد یک ویجت برای نگهداری غذاها
        self.food_display_widget = QWidget(self)
        self.food_display_layout = QVBoxLayout(self.food_display_widget)

        # نمایش غذاها داخل کادر
        self.food_display = QLabel("", self.food_display_widget)  # نمایش غذاها
        self.food_display.setStyleSheet(self.food_display_style())  # اعمال استایل کادر به نمایش غذاها
        self.food_display_layout.addWidget(self.food_display)

        # افزودن Scroll Area برای جلوگیری از overflow
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.food_display_widget)
        self.scroll_area.setWidgetResizable(True)  # اجازه تغییر اندازه به محتوا
        self.layout().addWidget(self.scroll_area)

        # دکمه برای نمایش اطلاعات غذا
        self.submit_button = QPushButton("نمایش اطلاعات غذا", self)
        self.submit_button.setStyleSheet(self.button_style())  # Apply button style
        self.submit_button.clicked.connect(self.show_food_info)
        self.layout().addWidget(self.submit_button)

        # دکمه ثبت برای افزودن کالری‌ها به وعده غذایی
        self.save_button = QPushButton("ثبت کالری‌ها", self)
        self.save_button.setStyleSheet(self.button_style())  # Apply button style
        self.save_button.clicked.connect(self.save_meal_calories)
        self.layout().addWidget(self.save_button)

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif; 
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
        }
        """

    def label_style(self):
        return """
        font-size: 16px; 
        font-weight: bold; 
        color: #344C3D; 
        font-family: 'Vazir', sans-serif; 
        margin-right: 10px; 
        margin-top: 0px;  /* حذف فاصله بالای تیتر */
        """

    def input_style(self):
        return """
        QLineEdit, QComboBox {
            font-size: 16px; 
            font-family: 'Vazir', sans-serif; 
            padding: 10px; 
            border: 2px solid #8EA58C; 
            border-radius: 5px; 
            background-color: #F4F4F4; 
        }
        QLineEdit:focus, QComboBox:focus {
            border: 2px solid #738A6E;
        }
        """

    def food_display_style(self):
        return """
        QLabel {
            border: 2px solid #8EA58C;
            border-radius: 10px;
            padding: 20px;  /* افزایش فضای داخلی */
            background-color: #F9F9F9;
            font-size: 14px;
            font-family: 'Vazir', sans-serif;
            color: #344C3D;
            min-height: 200px;  /* حداقل ارتفاع برای کادر غذاها */
            max-height: 400px;  /* حداکثر ارتفاع */
            overflow-y: auto;  /* اجازه پیمایش عمودی */
        }
        """

    def show_food_info(self):
        food_name = self.food_input.text().strip()
        food_weight_str = self.food_weight_input.text().strip()
        selected_unit = self.unit_selector.currentText()

        # بررسی صحت ورودی‌ها
        if not food_name:
            self.show_error_message("لطفا نام غذا را وارد کنید!")
            return
        if not food_weight_str.isdigit():
            self.show_error_message("لطفا حجم غذا را وارد کنید و از اعداد صحیح استفاده کنید!")
            return

        food_weight = int(food_weight_str)

        # تبدیل وزن به گرم در صورت نیاز
        # تبدیل وزن به گرم در صورت نیا
        if selected_unit == "کف دست":
            food_weight *= 45
        elif selected_unit == "پیمانه":
            food_weight *= 200
        elif selected_unit == "قاشق غذاخوری":
            food_weight *= 15  # فرض کنید که 1 قاشق معادل 15 گرم است
        elif selected_unit == "لیوان":
            food_weight *= 240  # فرض کنید که 1 لیوان معادل 240 گرم است

        # اتصال به پایگاه داده و جستجو در جدول غذاها
        conn = sqlite3.connect('calorie_counter.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM foods WHERE name LIKE ?", (f"%{food_name}%",))
        result = cursor.fetchone()
        conn.close()

        if result:
            food_name, calories, sugar, carbs, fat = result[1], result[2], result[3], result[4], result[5]
            base_weight = 100
            scale_factor = food_weight / base_weight

            total_calories = calories * scale_factor
            total_sugar = sugar * scale_factor
            total_carbs = carbs * scale_factor
            total_fat = fat * scale_factor

            self.show_food_info_dialog(food_name, food_weight, total_calories, total_sugar, total_carbs, total_fat)

            # Clear the input fields after displaying food information
            self.food_input.clear()  # Clear the food name input
            self.food_weight_input.clear()  # Clear the food weight input
            self.unit_selector.setCurrentIndex(0)  # Reset the unit selector to the first item ("گرم")
        else:
            self.show_error_message("غذا در پایگاه داده یافت نشد!")

    def show_error_message(self, message):
        """نمایش پیغام خطا"""
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("خطا")
        error_dialog.setText(message)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.exec_()

    def show_food_info_dialog(self, food_name, food_weight, calories, sugar, carbs, fat):
        # ارسال وزن به صفحه FoodInfoDialog برای محاسبه دقیق زمان پیاده‌روی
        dialog = FoodInfoDialog(food_name, food_weight, calories, sugar, carbs, fat, self.user_weight, self)
        dialog.exec_()

    def add_food_to_list(self, food_name, calories, sugar, carbs, fat):
        """اضافه کردن غذا به لیست غذاهای وارد شده با شماره‌گذاری"""
        food_entry = f"{self.food_counter}. {food_name} - {calories:.2f} کیلوکالری, قند: {sugar:.2f} گرم, کربوهیدرات: {carbs:.2f} گرم, چربی: {fat:.2f} گرم"
        self.food_list.append(food_entry)
        self.food_counter += 1  # افزایش شمارنده غذاها
        self.update_food_display()

    def update_food_display(self):
        """به روز رسانی نمایش لیست غذاها"""
        food_list_text = "\n".join(self.food_list)
        self.food_display.setText(food_list_text)

    def save_meal_calories(self):
        """محاسبه و ذخیره مجموع کالری‌ها و مقادیر دیگر برای وعده غذایی"""
        total_calories = sum(float(food.split('-')[1].split()[0]) for food in self.food_list)
        total_sugar = sum(float(food.split("قند:")[1].split()[0]) for food in self.food_list)
        total_fat = sum(float(food.split("چربی:")[1].split()[0]) for food in self.food_list)
        total_carbs = sum(float(food.split("کربوهیدرات:")[1].split()[0]) for food in self.food_list)

        if hasattr(self.parent(), 'update_meal_data'):
            self.parent().update_meal_data(total_calories, total_sugar, total_carbs, total_fat)

        # بروزرسانی دکمه وعده غذایی در DietPlanPage
        if hasattr(self.parent(), 'update_meal_button'):
            self.parent().update_meal_button(self.meal_name, total_calories)

        self.close()
class WaterIntakeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("نوشیدن آب")
        self.setFixedSize(700, 700)  # تنظیم سایز دیالوگ به 700x700 پیکسل

        self.label = QLabel("میزان آب نوشیدنی خود را وارد کنید:")
        self.label.setStyleSheet("""
            font-size: 18px;
            color: #000000;
            font-family: 'Vazir', sans-serif;
        """)

        # تصاویر لیوان خالی و پر
        self.empty_glass_pixmap = QPixmap(r"C:\Users\User\Downloads\icons8-empty-glass-50.png")  # مسیر تصویر لیوان خالی
        self.full_glass_pixmap = QPixmap(r"C:\Users\User\Downloads\icons8-empty-glass-50(1).png")  # مسیر تصویر لیوان پر

        # ایجاد 8 لیوان به صورت QLabel
        self.glass_labels = []
        self.glass_status = [False] * 8  # وضعیت پر بودن لیوان‌ها (False برای خالی، True برای پر)

        # ایجاد لیوان‌ها و اتصال به رویداد کلیک
        for i in range(8):
            glass_label = QLabel(self)
            glass_label.setPixmap(self.empty_glass_pixmap)  # نمایش تصویر لیوان خالی
            glass_label.setFixedSize(50, 100)  # اندازه لیوان‌ها
            glass_label.setAlignment(Qt.AlignCenter)
            glass_label.mousePressEvent = lambda event, idx=i: self.toggle_glass(event, idx)
            self.glass_labels.append(glass_label)

        # چیدمان برای دو سطر و چهار ستونی
        main_layout = QVBoxLayout()

        # اضافه کردن اسپیس برای قرار دادن محتوای مرکزی در وسط
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # اضافه کردن متن در وسط
        main_layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # اضافه کردن اسپیس برای فاصله بین متن و لیوان‌ها
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # سطر اول (4 لیوان اول)
        first_row_layout = QHBoxLayout()
        for i in range(4):
            first_row_layout.addWidget(self.glass_labels[i])

        # سطر دوم (4 لیوان دوم)
        second_row_layout = QHBoxLayout()
        for i in range(4, 8):
            second_row_layout.addWidget(self.glass_labels[i])

        # اضافه کردن سطرها به چیدمان اصلی
        main_layout.addLayout(first_row_layout)  # اضافه کردن سطر اول
        main_layout.addLayout(second_row_layout)  # اضافه کردن سطر دوم

        # اضافه کردن اسپیس در انتهای چیدمان برای فضا دادن به پایین صفحه
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # حذف بخش پیام خطا (self.error_message)

        # دکمه‌ها
        self.back_button = QPushButton("بازگشت")
        self.submit_button = QPushButton("ثبت")

        # اعمال استایل به دکمه‌ها با استفاده از متد button_style
        self.back_button.setStyleSheet(self.button_style())
        self.submit_button.setStyleSheet(self.button_style())

        self.back_button.clicked.connect(self.reject)  # بستن دیالوگ بدون تایید
        self.submit_button.clicked.connect(self.submit_action)  # عمل ثبت

        # چیدمان افقی برای دکمه‌ها (بازگشت و ثبت)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.submit_button)
        button_layout.setSpacing(20)  # فاصله بین دکمه‌ها

        # اضافه کردن چیدمان دکمه‌ها به چیدمان اصلی
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def button_style(self):
        """استایل دکمه‌ها"""
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif;
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
        }
        """

    def toggle_glass(self, event, index):
        """تغییر وضعیت لیوان با کلیک"""
        if self.glass_status[index]:
            # اگر لیوان پر بود، آن را خالی می‌کنیم
            self.glass_labels[index].setPixmap(self.empty_glass_pixmap)
            self.glass_status[index] = False
        else:
            # اگر لیوان خالی بود، آن را پر می‌کنیم
            self.glass_labels[index].setPixmap(self.full_glass_pixmap)
            self.glass_status[index] = True

    def submit_action(self):
        """عملکرد برای دکمه ثبت"""
        filled_glasses = sum(self.glass_status)  # تعداد لیوان‌های پر شده

        # بروزرسانی آب مصرفی در صفحه رژیم غذایی
        if self.parent():
            self.parent().update_water_intake(filled_glasses)

        # در غیر این صورت ثبت را انجام می‌دهیم
        print("عملیات ثبت انجام شد")
        self.accept()  # بستن دیالوگ


import sqlite3
from datetime import datetime
class DietPlanPage(QWidget):
    def __init__(self, user_data, daily_calories=None):
        super().__init__()
        self.user_data = user_data
        self.daily_calories = daily_calories  # دریافت کالری روزانه جدید
        self.setWindowTitle("رژیم غذایی")
        self.create_widgets()
        self.set_layout()

    def create_widgets(self):
        # دایره پیشرفت کالری
        self.circle_progress = CalorieProgressCircle(self.daily_calories)  # دایره پیشرفت کالری
        self.circle_progress.setCalories(0)  # مقدار اولیه مصرف کالری صفر است

        # نمایش وزن کاربر در کنار دایره پیشرفت
        self.weight_label = QLabel(f"وزن شما: {self.user_data['weight']} kg")
        self.weight_label.setStyleSheet("""
               font-size: 16px;
               font-weight: bold;
               color: #4CAF50;
               font-family: 'Vazir', sans-serif;
           """)

        # برچسب برنامه رژیم غذایی
        self.daily_calories_label = QLabel(
            f"کالری روزانه شما: {self.daily_calories} کیلوکالری" if self.daily_calories else "کالری روزانه محاسبه نشده است.")
        self.daily_calories_label.setStyleSheet("""
               font-size: 18px;
               font-weight: bold;
               color: #FF5722;
               font-family: 'Vazir', sans-serif;
           """)

        # اضافه کردن لیبل‌ها برای قند، چربی و کربوهیدرات
        self.sugar_label = QLabel("قند: 0 گرم", self)
        self.fat_label = QLabel("چربی: 0 گرم", self)
        self.carbs_label = QLabel("کربوهیدرات: 0 گرم", self)

        # ایجاد لیبل جدید برای آب مصرفی
        self.water_intake_label = QLabel("آب مصرفی: 0 لیوان")
        self.water_intake_label.setStyleSheet("""
                   font-size: 16px;
                   font-weight: bold;
                   color: #2196F3;  /* رنگ آبی برای لیبل آب مصرفی */
                   font-family: 'Vazir', sans-serif;
               """)

        # تنظیم استایل لیبل‌ها
        self.sugar_label.setStyleSheet("font-size: 14px; font-family: 'Vazir', sans-serif;")
        self.fat_label.setStyleSheet("font-size: 14px; font-family: 'Vazir', sans-serif;")
        self.carbs_label.setStyleSheet("font-size: 14px; font-family: 'Vazir', sans-serif;")

        # دکمه‌ها
        self.settings_button = QPushButton("تنظیمات")
        self.exercise_video_button = QPushButton("ویدیو ورزشی")
        self.diet_button = QPushButton("رژیم غذایی")
        self.calories_counter_button = QPushButton("کالری شمار")
        self.register_button = QPushButton("ثبت اطلاعات روز")
        self.register_button.clicked.connect(self.register_daily_data)  # اتصال عملکرد به دکمه

        # تنظیم استایل دکمه‌ها
        self.setup_button_styles()

        # متصل کردن دکمه‌ها به متدها
        self.settings_button.clicked.connect(self.settings_action)
        self.exercise_video_button.clicked.connect(self.exercise_video_action)
        self.diet_button.clicked.connect(self.diet_action)
        self.calories_counter_button.clicked.connect(self.calories_counter_action)

        # بخش وعده‌های غذایی و فعالیت‌ها
        self.meal_buttons = []
        meal_names = ["صبحانه", "ناهار", "میان وعده", "شام", "نوشیدن آب"]

        self.meal_calories = {
            "صبحانه": 0,
            "ناهار": 0,
            "میان وعده": 0,
            "شام": 0
        }

        # نمایش دکمه‌ها با کالری صفر
        for meal in meal_names:
            if meal == "نوشیدن آب":
                # برای دکمه نوشیدن آب کالری تقسیم نمی‌شود
                button = QPushButton(f"{meal}\n")
                button.clicked.connect(lambda _, m=meal: self.set_water_intake(m))
            else:
                # برای دیگر وعده‌ها کالری صفر نمایش داده می‌شود
                button = QPushButton(f"{meal}\n0 کالری")
                button.clicked.connect(lambda _, m=meal: self.open_meal_input_dialog(m))

            button.setStyleSheet("""
                background-color: #F5F5F5; 
                color: black; 
                border: 1px solid #ddd;
                padding: 10px;
                font-size: 14px;
                margin-bottom: 10px;
                font-family: 'Vazir', sans-serif;
            """)
            self.meal_buttons.append(button)

    def update_meal_data(self, total_calories, total_sugar, total_carbs, total_fat):
        """بروزرسانی مقادیر کالری، قند، چربی و کربوهیدرات"""
        # بروزرسانی کالری‌های دایره پیشرفت
        self.circle_progress.setCalories(total_calories)

        # بروزرسانی لیبل‌ها
        self.sugar_label.setText(f"قند: {total_sugar:.2f} گرم")
        self.fat_label.setText(f"چربی: {total_fat:.2f} گرم")
        self.carbs_label.setText(f"کربوهیدرات: {total_carbs:.2f} گرم")

        # بروزرسانی دایره پیشرفت با مجموع کالری‌های مصرفی
        total_consumed = total_calories  # فرض بر اینکه فقط کالری‌ها مهم هستند
        self.circle_progress.setCalories(total_consumed)

    def open_meal_input_dialog(self, meal_name):
        """باز کردن دیالوگ وارد کردن غذا برای وعده مشخص"""
        dialog = MealInputDialog(meal_name, self.user_data['weight'], self)
        dialog.exec_()
    def setup_button_styles(self):
        """تنظیم استایل دکمه‌ها"""
        for button in [self.settings_button, self.exercise_video_button, self.diet_button, self.calories_counter_button]:
            button.setStyleSheet("""
                background-color: #FF5722; 
                color: white; 
                padding: 10px;
                font-size: 14px;
                margin-bottom: 10px;
                font-family: 'Vazir', sans-serif;
            """)

    # تغییر در متد set_water_intake در DietPlanPage
    def set_water_intake(self, meal_name):
        """عملکرد برای نوشیدن آب"""
        dialog = WaterIntakeDialog(self)
        dialog.exec_()  # نمایش دیالوگ

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px; 
            font-weight: bold; /* بولد کردن متن دکمه */
            font-family: 'Vazir', sans-serif; /* استفاده از فونت وزیر */
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
        }
        """

    def register_button_style(self):
        """استایل اختصاصی برای دکمه ثبت اطلاعات روز"""
        return """
        QPushButton {
            background-color: #FF9800; /* رنگ نارنجی جذاب */
            color: white; 
            border: 2px solid #F57C00; /* رنگ مرزی مشابه رنگ پس‌زمینه */
            border-radius: 12px; 
            padding: 12px; 
            font-size: 16px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif;
        }
        QPushButton:hover {
            background-color: #F57C00; 
            color: white;
        }
        QPushButton:pressed {
            background-color: #FFB74D;
            color: white;
        }
        """

    def setup_button_styles(self):
        """تنظیم استایل دکمه‌ها"""
        button_style = self.button_style()  # استایل عمومی دکمه‌ها
        register_button_style = self.register_button_style()  # استایل اختصاصی برای دکمه ثبت

        # اعمال استایل به دکمه‌های مختلف
        for button in [self.settings_button, self.exercise_video_button, self.diet_button,
                       self.calories_counter_button]:
            button.setStyleSheet(button_style)

        # اعمال استایل اختصاصی به دکمه "ثبت اطلاعات روز"
        self.register_button.setStyleSheet(register_button_style)

    def update_water_intake(self, filled_glasses):
        """بروزرسانی تعداد لیوان‌های آب مصرفی"""
        # بروزرسانی متن لیبل آب مصرفی
        self.water_intake_label.setText(f"آب مصرفی: {filled_glasses} لیوان")

        # رنگ ثابت برای لیبل آب مصرفی
        self.water_intake_label.setStyleSheet("""
               font-size: 16px;
               font-weight: bold;
               color: #2196F3;  /* رنگ آبی برای لیبل آب مصرفی */
               font-family: 'Vazir', sans-serif;
           """)

    def register_daily_data(self):
        """عملکرد برای ثبت اطلاعات روز در پایگاه داده"""
        try:
            # گرفتن داده‌ها از ویجت‌ها
            water_intake = self.water_intake_label.text().split(" ")[2]  # استخراج تعداد لیوان‌ها از لیبل آب
            water_intake = int(water_intake) if water_intake.isdigit() else 0  # تبدیل به عدد صحیح

            sugar = float(self.sugar_label.text().split(":")[1].strip().split(" ")[0])  # استخراج قند از لیبل
            fat = float(self.fat_label.text().split(":")[1].strip().split(" ")[0])  # استخراج چربی از لیبل
            carbs = float(self.carbs_label.text().split(":")[1].strip().split(" ")[0])  # استخراج کربوهیدرات از لیبل
            total_calories = self.circle_progress.getSavedCalories()  # کالری کل مصرفی از دایره پیشرفت
            user_email = self.user_data['email']  # ایمیل کاربر

            # تاریخ امروز برای ذخیره‌سازی در دیتابیس
            today_date = datetime.now().strftime('%Y-%m-%d')

            # اتصال به پایگاه داده و ذخیره داده‌ها
            conn = sqlite3.connect('create.db')
            cursor = conn.cursor()

            # بررسی وجود اطلاعات برای تاریخ امروز
            cursor.execute('''
            SELECT * FROM daily_data WHERE date = ? AND user_email = ?
            ''', (today_date, user_email))

            result = cursor.fetchone()

            if result:
                # اگر اطلاعات برای تاریخ امروز وجود دارد، داده‌ها را به روز رسانی می‌کنیم
                cursor.execute('''
                UPDATE daily_data 
                SET water_intake = ?, sugar = ?, fat = ?, carbs = ?, total_calories = ?
                WHERE date = ? AND user_email = ?
                ''', (water_intake, sugar, fat, carbs, total_calories, today_date, user_email))
                print(f"اطلاعات روز برای تاریخ {today_date} به روز شد.")
            else:
                # اگر اطلاعات برای تاریخ امروز وجود نداشت، داده‌ها را اضافه می‌کنیم
                cursor.execute('''
                INSERT INTO daily_data (date, water_intake, sugar, fat, carbs, total_calories, user_email)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (today_date, water_intake, sugar, fat, carbs, total_calories, user_email))
                print(f"اطلاعات روز برای تاریخ {today_date} ثبت شد.")

            conn.commit()
            conn.close()

        except Exception as e:
            print(f"خطا در ثبت اطلاعات روز: {e}")

    def settings_action(self):
        """عملکرد برای تنظیمات"""
        print("تنظیمات clicked")

    def exercise_video_action(self):
        """عملکرد برای ویدیو ورزشی"""
        print("ویدیو ورزشی clicked")

    def diet_action(self):
        """عملکرد برای رژیم غذایی"""
        print("رژیم غذایی clicked")

    def calories_counter_action(self):
        """عملکرد برای کالری شمار"""
        print("کالری شمار clicked")

    def set_layout(self):
        # چیدمان اصلی
        layout = QVBoxLayout()

        # ایجاد یک QHBoxLayout برای قرار دادن لیبل‌ها در کنار دایره پیشرفت
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)  # فاصله‌ها به صفر کاهش می‌یابد
        top_layout.setSpacing(5)  # فاصله بین دایره پیشرفت و لیبل‌ها کم می‌شود

        # قرار دادن لیبل وزن در سمت چپ دایره
        top_layout.addWidget(self.weight_label, alignment=Qt.AlignCenter)

        # قرار دادن دایره پیشرفت در وسط
        top_layout.addWidget(self.circle_progress, alignment=Qt.AlignCenter)

        # قرار دادن لیبل آب مصرفی در سمت راست دایره
        top_layout.addWidget(self.water_intake_label, alignment=Qt.AlignCenter)

        # اضافه کردن QHBoxLayout که شامل لیبل‌های وزن و آب مصرفی است به چیدمان اصلی
        layout.addLayout(top_layout)

        # اضافه کردن لیبل کالری روزانه
        layout.addWidget(self.daily_calories_label, alignment=Qt.AlignCenter)

        # اضافه کردن لیبل‌های قند، چربی و کربوهیدرات به صورت افقی
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.sugar_label)
        horizontal_layout.addWidget(self.fat_label)
        horizontal_layout.addWidget(self.carbs_label)
        horizontal_layout.setAlignment(Qt.AlignCenter)
        horizontal_layout.setSpacing(20)  # فاصله بین لیبل‌ها به اندازه 20 پیکسل
        layout.addLayout(horizontal_layout)

        # اضافه کردن دکمه‌های وعده‌ها
        for button in self.meal_buttons:
            layout.addWidget(button)

        # اضافه کردن دکمه "ثبت اطلاعات روز" بین نوشیدن آب و دکمه‌های پایین
        layout.addWidget(self.register_button)  # دکمه جدید

        # دکمه‌های پایین صفحه را به صورت افقی قرار بده
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.settings_button)
        buttons_layout.addWidget(self.exercise_video_button)
        buttons_layout.addWidget(self.diet_button)
        buttons_layout.addWidget(self.calories_counter_button)

        # تنظیم فاصله بین دکمه‌ها
        buttons_layout.setSpacing(10)

        # اضافه کردن دکمه‌ها به چیدمان اصلی
        layout.addLayout(buttons_layout)

        # اضافه کردن یک SpacerItem برای تنظیم فاصله از پایین
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        self.setLayout(layout)

    def open_meal_input_dialog(self, meal_name):
        # ارسال وزن کاربر به MealInputDialog
        dialog = MealInputDialog(meal_name, self.user_data['weight'], self)
        dialog.exec_()

    def update_meal_button(self, meal_name, total_calories):
        """بروزرسانی دکمه‌های وعده غذایی با مجموع کالری‌ها"""
        for button in self.meal_buttons:
            if meal_name in button.text():
                button.setText(f"{meal_name}\n{total_calories} کالری")
                break
class ProfilePage(QWidget):
    def __init__(self, user_data, login_page):
        super().__init__()
        self.login_page = login_page
        self.setWindowTitle("پروفایل کاربری")
        self.user_data = user_data
        self.initial_calories = None  # متغیر برای ذخیره کالری اولیه
        self.new_calories = None  # متغیر برای ذخیره کالری جدید

        # ایجاد ویجت‌ها
        self.create_widgets()
        # تنظیم چیدمان
        self.set_layout()

        # ذخیره کالری اولیه در دیتابیس
        self.insert_initial_calories()

    def create_widgets(self):
        self.success_message_label = QLabel("اطلاعات حساب کاربری شما به شرح زیر است:")
        self.success_message_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #344C3D;
            font-family: 'Vazir', sans-serif;
            text-align: center;
            margin-bottom: 20px;
        """)
        self.success_message_label.setAlignment(Qt.AlignCenter)

        # اطلاعات کاربری
        self.name_label = QLabel(f"اسم: {self.user_data['name']}")
        self.age_label = QLabel(f"سن: {self.user_data['age']}")
        self.weight_label = QLabel(f"وزن: {self.user_data['weight']} kg")
        self.height_label = QLabel(f"قد: {self.user_data['height']} cm")
        self.gender_label = QLabel(f"جنسیت: {self.user_data['gender']}")
        self.activity_level_label = QLabel(f"سطح فعالیت: {self.user_data['activity_level']}")
        self.email_label = QLabel(f"ایمیل: {self.user_data['email']}")

        # محاسبه BMI
        bmi_value = self.calculate_bmi(self.user_data['weight'], self.user_data['height'])
        self.bmi_label = QLabel(f"شاخص توده بدنی: {bmi_value:.2f}")
        self.bmi_category_label = QLabel(self.get_bmi_category(bmi_value))

        # محاسبه کالری روزانه
        bmi_value = self.calculate_bmi(self.user_data['weight'], self.user_data['height'])
        self.initial_calories, calories_message = self.calculate_daily_calories(
            self.user_data['weight'],
            self.user_data['height'],
            self.user_data['age'],
            self.user_data['gender'],
            self.user_data['activity_level'],
            bmi_value
        )

        # ذخیره کالری اولیه
        self.user_data['daily_calories'] = self.initial_calories

        # نمایش کالری‌ها
        self.daily_calories_label = QLabel(f"{calories_message}: {self.initial_calories} کیلوکالری")

        # دکمه‌ها
        self.continue_button = QPushButton("ادامه و دریافت رژیم غذایی")
        self.edit_button = QPushButton("ویرایش اطلاعات")
        self.setup_button_styles()

        # اتصال دکمه‌ها به متدهای مربوطه
        self.continue_button.clicked.connect(self.continue_action)
        self.edit_button.clicked.connect(self.edit_action)

    def setup_button_styles(self):
        self.continue_button.setStyleSheet("""
            QPushButton {
                background-color: #738A6E; 
                color: #BFCFBB; 
                border: 2px solid #8EA58C; 
                border-radius: 10px; 
                padding: 10px; 
                font-size: 16px; 
                font-weight: bold; 
                font-family: 'Vazir', sans-serif; 
            }
            QPushButton:hover {
                background-color: #8EA58C; 
                color: #344C3D; 
            }
            QPushButton:pressed {
                background-color: #BFCFBB; 
                color: #344C3D; 
            }
        """)

        self.edit_button.setStyleSheet("""
            QPushButton {
                background-color: #FFB74D;
                color: #fff;
                border: 2px solid #FF8C00;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                font-family: 'Vazir', sans-serif;
            }
            QPushButton:hover {
                background-color: #FF8C00;
                color: #fff;
            }
            QPushButton:pressed {
                background-color: #FFB74D;
                color: #fff;
            }
        """)

    def set_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.success_message_label)
        layout.addWidget(self.create_widget_with_border(self.name_label))
        layout.addWidget(self.create_widget_with_border(self.age_label))
        layout.addWidget(self.create_widget_with_border(self.weight_label))
        layout.addWidget(self.create_widget_with_border(self.height_label))
        layout.addWidget(self.create_widget_with_border(self.gender_label))
        layout.addWidget(self.create_widget_with_border(self.activity_level_label))
        layout.addWidget(self.create_widget_with_border(self.email_label))
        layout.addWidget(self.create_widget_with_border(self.bmi_label))
        layout.addWidget(self.create_widget_with_border(self.bmi_category_label))
        layout.addWidget(self.create_widget_with_border(self.daily_calories_label))
        layout.addWidget(self.continue_button)
        layout.addWidget(self.edit_button)
        self.setLayout(layout)

    def create_widget_with_border(self, widget):
        widget.setStyleSheet("""
            QLabel {
                border: 2px solid #8EA58C;  
                border-radius: 5px;  
                padding: 5px;  
                margin-bottom: 10px;  
            }
        """)
        return widget

    def calculate_bmi(self, weight, height):
        height_in_meters = height / 100.0  # تبدیل قد از سانتی‌متر به متر
        bmi = weight / (height_in_meters ** 2)  # فرمول محاسبه BMI
        return bmi

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "کمبود وزن"
        elif 18.5 <= bmi < 24.9:
            return "وزن نرمال"
        elif 25 <= bmi < 29.9:
            return "اضافه وزن"
        else:
            return "چاقی"

    def calculate_daily_calories(self, weight, height, age, gender, activity_level, bmi):
        # محاسبه BMR (نرخ متابولیسم پایه) با توجه به جنسیت
        if gender == 'مرد':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        # تعیین فاکتور فعالیت
        activity_factor = 1.2 if activity_level == 'کم تحرک' else (1.55 if activity_level == 'متوسط' else 1.9)
        daily_calories = bmr * activity_factor

        # تنظیم کالری با توجه به BMI
        if bmi < 18.5:
            daily_calories += 500  # برای افزایش وزن
            calories_message = "کالری مورد نیاز برای افزایش وزن"
        elif 18.5 <= bmi < 24.9:
            calories_message = "کالری مورد نیاز برای تثبیت وزن"
        elif 25 <= bmi < 29.9:
            daily_calories -= 500  # برای کاهش وزن
            calories_message = "کالری مورد نیاز برای کاهش وزن"
        else:
            daily_calories -= 500  # برای کاهش وزن
            calories_message = "کالری مورد نیاز برای کاهش وزن"

        return round(daily_calories), calories_message

    def insert_initial_calories(self):
        # محاسبه BMI و کالری روزانه بر اساس اطلاعات کاربر
        bmi_value = self.calculate_bmi(self.user_data['weight'], self.user_data['height'])
        self.initial_calories, calories_message = self.calculate_daily_calories(
            self.user_data['weight'],
            self.user_data['height'],
            self.user_data['age'],
            self.user_data['gender'],
            self.user_data['activity_level'],
            bmi_value
        )

        # به روزرسانی مقدار کالری‌ها در دیتابیس
        connection = sqlite3.connect("create.db")
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE users
            SET daily_calories = ?
            WHERE email = ?
        ''', (self.initial_calories, self.user_data['email']))
        connection.commit()
        connection.close()

    def continue_action(self):
        # کالری که می‌خواهیم نشان دهیم (کالری جدید یا اولیه)
        calories_to_show = self.new_calories if self.new_calories is not None else self.initial_calories
        # ارسال داده‌ها به صفحه رژیم غذایی، شامل وزن کاربر
        self.diet_plan_page = DietPlanPage(self.user_data, calories_to_show)
        self.diet_plan_page.show()

    def edit_action(self):
        # در اینجا به EditProfileWindow ارجاع به self یعنی ProfilePage را ارسال می‌کنیم
        self.edit_window = EditProfileWindow(self.user_data, self.update_user_data, self)
        self.edit_window.show()

    def update_user_data(self, new_data):
        self.user_data = new_data

        # محاسبه مجدد BMI
        bmi_value = self.calculate_bmi(new_data['weight'], new_data['height'])
        self.bmi_label.setText(f"شاخص توده بدنی: {bmi_value:.2f}")  # به‌روزرسانی BMI
        self.bmi_category_label.setText(self.get_bmi_category(bmi_value))  # به‌روزرسانی دسته‌بندی BMI

        # محاسبه کالری مجدد
        self.new_calories, calories_message = self.calculate_daily_calories(
            new_data['weight'],
            new_data['height'],
            new_data['age'],
            new_data['gender'],
            new_data['activity_level'],
            bmi_value  # ارسال BMI جدید برای محاسبه کالری
        )

        # به‌روزرسانی کالری
        self.daily_calories_label.setText(f"{calories_message}: {self.new_calories} کیلوکالری")

        # به‌روزرسانی نمایش سایر اطلاعات
        self.name_label.setText(f"اسم: {new_data['name']}")
        self.age_label.setText(f"سن: {new_data['age']}")
        self.weight_label.setText(f"وزن: {new_data['weight']} kg")
        self.height_label.setText(f"قد: {new_data['height']} cm")
        self.gender_label.setText(f"جنسیت: {new_data['gender']}")
        self.activity_level_label.setText(f"سطح فعالیت: {new_data['activity_level']}")
        self.email_label.setText(f"ایمیل: {new_data['email']}")

        # ذخیره کالری جدید در دیتابیس
        self.update_daily_calories_in_db(self.new_calories)

    def update_daily_calories_in_db(self, daily_calories):
        connection = sqlite3.connect("create.db")
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE users
            SET daily_calories = ?
            WHERE email = ?
        ''', (daily_calories, self.user_data['email']))
        connection.commit()
        connection.close()

    def update_user_data_in_db(self, new_data, daily_calories):
        try:
            connection = sqlite3.connect("create.db")
            cursor = connection.cursor()

            cursor.execute('''
                UPDATE users
                SET name = ?, age = ?, weight = ?, height = ?, gender = ?, activity_level = ?, daily_calories = ?
                WHERE email = ?
            ''', (new_data['name'], new_data['age'], new_data['weight'], new_data['height'],
                  new_data['gender'], new_data['activity_level'], daily_calories, new_data['email']))

            connection.commit()
            connection.close()

            print("اطلاعات به‌روز شد.")
            # به‌روزرسانی صفحه پروفایل با مقادیر جدید
            self.update_user_data(new_data)

        except Exception as e:
            print(f"خطا در اتصال به دیتابیس: {str(e)}")
            raise e
class UserRegistration(QWidget):
    def __init__(self, login_page):
        super().__init__()
        self.login_page = login_page  # نگه‌داشتن ارجاع به صفحه ورود
        self.setWindowTitle("ایجاد حساب کاربری")

        # ایجاد ویجت‌ها
        self.create_widgets()

        # تنظیم چیدمان
        self.set_layout()

        # اعمال استایل
        self.apply_styles()

        # اتصال سیگنال‌ها
        self.name_input.textChanged.connect(self.validate_name)
        self.age_input.textChanged.connect(self.validate_age)
        self.weight_input.textChanged.connect(self.validate_weight)
        self.height_input.textChanged.connect(self.validate_height)
        self.email_input.textChanged.connect(self.validate_email)
        self.password_input.textChanged.connect(self.validate_password)
        self.submit_button.clicked.connect(self.check_fields)
        self.back_button.clicked.connect(self.go_to_login)  # اتصال دکمه بازگشت به متد

    def create_user_table(self):
        # اتصال به دیتابیس
        connection = sqlite3.connect("create.db", timeout=30)
        cursor = connection.cursor()

        # فعال کردن WAL
        cursor.execute('PRAGMA journal_mode=WAL;')
        connection.commit()

        # ادامه عملیات

    def create_widgets(self):
        # فیلدها
        self.name_label = QLabel("اسم:")
        self.name_input = QLineEdit()
        self.name_error_label = QLabel("")  # QLabel برای نمایش خطا

        self.age_label = QLabel("سن:")
        self.age_input = QLineEdit()
        self.age_error_label = QLabel("")  # QLabel برای نمایش خطا

        self.height_label = QLabel("قد (سانتی‌متر):")
        self.height_input = QLineEdit()
        self.height_error_label = QLabel("")  # QLabel برای نمایش خطا

        self.weight_label = QLabel("وزن (کیلوگرم):")
        self.weight_input = QLineEdit()
        self.weight_error_label = QLabel("")  # QLabel برای نمایش خطا

        self.gender_label = QLabel("جنسیت:")
        self.gender_input = QComboBox()
        self.gender_input.addItems(["", "زن", "مرد"])

        self.activity_level_label = QLabel("سطح فعالیت:")
        self.activity_level_input = QComboBox()
        self.activity_level_input.addItems(["","کم تحرک", "متوسط", "پر تحرک"])

        self.email_label = QLabel("ایمیل:")
        self.email_input = QLineEdit()
        self.email_error_label = QLabel("")  # QLabel برای نمایش خطا

        self.password_label = QLabel("رمز عبور:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_error_label = QLabel("")  # QLabel برای نمایش خطا

        # دکمه‌ها
        self.back_button = QPushButton("بازگشت")
        self.submit_button = QPushButton("ثبت")

    def set_layout(self):
        # تنظیم چیدمان عمودی
        layout = QVBoxLayout()

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.name_error_label)  # افزودن QLabel برای خطا

        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.age_error_label)  # افزودن QLabel برای خطا

        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.height_error_label)  # افزودن QLabel برای خطا

        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.weight_error_label)  # افزودن QLabel برای خطا

        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)

        layout.addWidget(self.activity_level_label)
        layout.addWidget(self.activity_level_input)

        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.email_error_label)  # افزودن QLabel برای خطا

        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.password_error_label)  # افزودن QLabel برای خطا

        # افزودن دکمه‌ها به چیدمان افقی
        button_layout = QHBoxLayout()  # چیدمان افقی برای دکمه‌ها
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.submit_button)

        layout.addLayout(button_layout)  # افزودن چیدمان دکمه‌ها به چیدمان اصلی

        self.setLayout(layout)

    def apply_styles(self):
        self.setStyleSheet(self.input_style())  # استایل برای QLineEdit و QComboBox
        self.name_label.setStyleSheet(self.label_style())  # استایل برای label
        self.age_label.setStyleSheet(self.label_style())
        self.height_label.setStyleSheet(self.label_style())
        self.weight_label.setStyleSheet(self.label_style())
        self.gender_label.setStyleSheet(self.label_style())
        self.activity_level_label.setStyleSheet(self.label_style())
        self.email_label.setStyleSheet(self.label_style())
        self.password_label.setStyleSheet(self.label_style())

        self.back_button.setStyleSheet(self.button_style())  # استایل برای QPushButton
        self.submit_button.setStyleSheet(self.button_style())

        # استایل برای QComboBox
        self.gender_input.setStyleSheet(self.combo_box_style())
        self.activity_level_input.setStyleSheet(self.combo_box_style())

    def input_style(self):
        return """
        QLineEdit {
            font-size: 16px; 
            padding: 5px; 
            border: 2px solid #8EA58C; 
            border-radius: 5px; 
            font-family: 'Vazir', sans-serif; 
        }
        """

    def combo_box_style(self):
        return """
        QComboBox {
            font-size: 16px; 
            padding: 5px; 
            border: 2px solid #8EA58C; 
            border-radius: 5px; 
            font-family: 'Vazir', sans-serif; 
        }
        """

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif; 
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
        }
        """

    def label_style(self):
        return """
        font-size: 16px; 
        font-weight: bold; 
        color: #344C3D; 
        font-family: 'Vazir', sans-serif; 
        margin-right: 10px; 
        """

    def validate_name(self, text):
        pattern = re.compile(r'^[a-zA-Zا-ی ]+$')
        if not pattern.match(text):
            self.name_input.setStyleSheet("QLineEdit { border: 2px solid red; }")
            self.name_error_label.setText("لطفاً فقط حروف فارسی و انگلیسی وارد کنید.")
        else:
            self.name_input.setStyleSheet("")
            self.name_error_label.setText("")

    def validate_age(self, text):
        pattern = re.compile(r'^\d*$')
        if not pattern.match(text) or (text and (int(text) < 1 or int(text) > 120)):
            self.age_input.setStyleSheet("QLineEdit { border: 2px solid red; }")
            self.age_error_label.setText("لطفاً سنی بین 1 تا 120 وارد کنید.")
        else:
            self.age_input.setStyleSheet("")
            self.age_error_label.setText("")

    def validate_weight(self, text):
        pattern = re.compile(r'^(0|[1-9]\d*|[1-9]\d*\.\d+)$')
        if not pattern.match(text) or (text and float(text) <= 0):
            self.weight_input.setStyleSheet("QLineEdit { border: 2px solid red; }")
            self.weight_error_label.setText("لطفاً وزنی بیشتر از 0 وارد کنید.")
        else:
            self.weight_input.setStyleSheet("")
            self.weight_error_label.setText("")

    def validate_height(self, text):
        pattern = re.compile(r'^(0|[1-9]\d*|[1-9]\d*\.\d+)$')
        if not pattern.match(text) or (text and float(text) <= 0):
            self.height_input.setStyleSheet("QLineEdit { border: 2px solid red; }")
            self.height_error_label.setText("لطفاً قدی بیشتر از 0 وارد کنید.")
        else:
            self.height_input.setStyleSheet("")
            self.height_error_label.setText("")

    def validate_email(self, text):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not pattern.match(text):
            self.email_input.setStyleSheet("QLineEdit { border: 2px solid red; }")
            self.email_error_label.setText("لطفاً ایمیل معتبر وارد کنید.")
        else:
            self.email_input.setStyleSheet("")
            self.email_error_label.setText("")

    def validate_password(self, text):
        if len(text) < 8 or not re.search(r'\d', text) or not re.search(r'[a-zA-Z]', text):
            self.password_input.setStyleSheet("QLineEdit { border: 2px solid red; }")
            self.password_error_label.setText("رمز عبور باید حداقل 8 کاراکتر و شامل حروف و اعداد باشد.")
        else:
            self.password_input.setStyleSheet("")
            self.password_error_label.setText("")

    def insert_user_to_db(self):
        name = self.name_input.text()
        age = int(self.age_input.text())
        weight = float(self.weight_input.text())
        height = float(self.height_input.text())
        gender = self.gender_input.currentText()
        activity_level = self.activity_level_input.currentText()
        email = self.email_input.text()
        password = self.password_input.text()

        try:
            # اتصال به دیتابیس
            connection = sqlite3.connect("create.db")
            cursor = connection.cursor()

            # وارد کردن اطلاعات به جدول
            cursor.execute('''
                INSERT INTO users (name, age, weight, height, gender, activity_level, email, password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, age, weight, height, gender, activity_level, email, password))

            connection.commit()
            connection.close()
            user_data = {
                'name': name,
                'age': age,
                'weight': weight,
                'height': height,
                'gender': gender,
                'activity_level': activity_level,
                'email': email
            }

            # نمایش صفحه پروفایل
            profile_page = ProfilePage(user_data, self.login_page)
            self.parent().addWidget(profile_page)  # افزودن صفحه پروفایل به parent widget
            self.parent().setCurrentWidget(profile_page)  # نمایش صفحه پروفایل

        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "خطا", "ایمیل وارد شده قبلاً ثبت شده است.")
        except Exception as e:
            QMessageBox.warning(self, "خطا", f"خطای نامشخصی رخ داده است: {e}")

    def check_fields(self):
        # بررسی اینکه آیا همه فیلدها پر شده‌اند
        if not (self.name_input.text() and self.age_input.text() and
                self.weight_input.text() and self.height_input.text() and
                self.email_input.text() and self.password_input.text()):
            QMessageBox.warning(self, "خطا", "لطفاً همه فیلدها را پر کنید.")  # نمایش پیغام خطا
            return

        # بررسی اعتبارسنجی فیلدها
        self.validate_name(self.name_input.text())
        self.validate_age(self.age_input.text())
        self.validate_weight(self.weight_input.text())
        self.validate_height(self.height_input.text())
        self.validate_email(self.email_input.text())
        self.validate_password(self.password_input.text())

        # اگر همه اعتبارسنجی‌ها موفق بود، اطلاعات را وارد دیتابیس می‌کنیم
        self.insert_user_to_db()

    def go_to_login(self):
        # مخفی کردن صفحه ثبت‌نام و نمایش صفحه ورود
        self.parent().setCurrentWidget(self.login_page)  # برگرداندن به صفحه ورود
class NewWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.setWindowTitle('صفحه سوم')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout(self)
        self.stacked_widget = stacked_widget

        self.background_label = QLabel(self)
        self.layout.addWidget(self.background_label, 0, Qt.AlignCenter)

        self.set_background_image()

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.open_new_window_button = QPushButton('بزن بریم', self)
        self.open_new_window_button.setStyleSheet(self.button_style())
        self.open_new_window_button.setFixedHeight(40)
        self.open_new_window_button.setFixedWidth(1800)
        self.open_new_window_button.clicked.connect(self.show_login_window)
        self.layout.addStretch()
        self.layout.addWidget(self.open_new_window_button, 0, Qt.AlignCenter)

        self.setLayout(self.layout)

    def show_login_window(self):
        login_window = LoginWindow(self.stacked_widget)
        self.stacked_widget.addWidget(login_window)
        self.stacked_widget.setCurrentWidget(login_window)

    def set_background_image(self):
        pixmap = QPixmap(r"C:\Users\User\Desktop\4.png")
        new_size = self.size() + QSize(1000, 450)
        self.background_label.setPixmap(pixmap.scaled(new_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setFixedSize(new_size)

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif; 
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
        }
        """
class SecondWindow(QWidget):
    def __init__(self, open_new_window_callback):
        super().__init__()
        self.setWindowTitle('صفحه دوم')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)

        self.background_label = QLabel(self)
        layout.addWidget(self.background_label, 0, Qt.AlignCenter)

        self.set_background_image()

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.open_new_window_button = QPushButton('ادامه', self)
        self.open_new_window_button.setStyleSheet(self.button_style())
        self.open_new_window_button.setFixedHeight(40)
        self.open_new_window_button.setFixedWidth(1800)
        self.open_new_window_button.clicked.connect(open_new_window_callback)
        layout.addStretch()
        layout.addWidget(self.open_new_window_button, 0, Qt.AlignCenter)

        self.setLayout(layout)

    def set_background_image(self):
        pixmap = QPixmap(r"C:\Users\User\Desktop\3.png")
        new_size = self.size() + QSize(1000, 480)
        self.background_label.setPixmap(pixmap.scaled(new_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setFixedSize(new_size)

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif; 
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
        }
        """
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('صفحه اول')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout(self)

        self.stacked_widget = QStackedWidget(self)
        self.layout.addWidget(self.stacked_widget)

        self.first_page = self.create_first_page()
        self.stacked_widget.addWidget(self.first_page)

        self.second_page = SecondWindow(self.open_new_window)
        self.stacked_widget.addWidget(self.second_page)

        self.setLayout(self.layout)

    def create_first_page(self):
        first_page = QWidget()
        layout = QVBoxLayout(first_page)

        self.background_label = QLabel(first_page)
        layout.addWidget(self.background_label, 0, Qt.AlignCenter)

        self.set_background_image()

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.button = QPushButton('ادامه', first_page)
        self.button.setStyleSheet(self.button_style())
        self.button.setFixedHeight(40)
        self.button.setFixedWidth(1865)
        self.button.clicked.connect(self.show_second_window)
        layout.addWidget(self.button, 0, Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.button)

        return first_page

    def set_background_image(self):
        pixmap = QPixmap(r"C:\Users\User\Desktop\2.png")
        new_size = self.size() + QSize(1000, 450)
        self.background_label.setPixmap(pixmap.scaled(new_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.background_label.setFixedSize(new_size)

    def show_second_window(self):
        self.stacked_widget.setCurrentWidget(self.second_page)

    def open_new_window(self):
        new_window = NewWindow(self.stacked_widget)
        self.stacked_widget.addWidget(new_window)
        self.stacked_widget.setCurrentWidget(new_window)

    def button_style(self):
        return """
        QPushButton {
            background-color: #738A6E; 
            color: #BFCFBB; 
            border: 2px solid #8EA58C; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px; 
            font-weight: bold; 
            font-family: 'Vazir', sans-serif; 
        }
        QPushButton:hover {
            background-color: #8EA58C; 
            color: #344C3D; 
        }
        QPushButton:pressed {
            background-color: #BFCFBB; 
            color: #344C3D; 
        }
        """
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
