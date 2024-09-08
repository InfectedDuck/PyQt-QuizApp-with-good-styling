import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QPushButton, QVBoxLayout, QWidget, \
    QTabWidget, QDialog, QFormLayout, QLineEdit, QDialogButtonBox, QMessageBox
from questions import modify_questions, create_question


class Quiz(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define the list of questions with options and correct answers
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"],
             "correct_answer": "Paris"},
            {"question": "What is 2+2?", "options": ["3", "4", "5", "6"], "correct_answer": "4"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Mercury"],
             "correct_answer": "Mars"},
            {"question": "Who painted the Mona Lisa?",
             "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
             "correct_answer": "Leonardo da Vinci"},
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "NaCl", "O2"],
             "correct_answer": "H2O"},
            {"question": "Which country is famous for its tulips?",
             "options": ["Netherlands", "Italy", "France", "Spain"], "correct_answer": "Netherlands"},
            {"question": "Who wrote 'Romeo and Juliet'?",
             "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
             "correct_answer": "William Shakespeare"},
            {"question": "What is the tallest mammal?", "options": ["Giraffe", "Elephant", "Hippo", "Kangaroo"],
             "correct_answer": "Giraffe"},
            {"question": "What is the currency of Japan?", "options": ["Yen", "Euro", "Dollar", "Pound"],
             "correct_answer": "Yen"},
            {"question": "Which gas do plants absorb from the atmosphere?",
             "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "correct_answer": "Carbon dioxide"},
            {"question": "Who developed the theory of relativity?",
             "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
             "correct_answer": "Albert Einstein"},
            {"question": "Which element has the chemical symbol 'Fe'?", "options": ["Iron", "Gold", "Silver", "Copper"],
             "correct_answer": "Iron"},
            {"question": "In which year did World War I begin?", "options": ["1914", "1918", "1920", "1905"],
             "correct_answer": "1914"},
            {"question": "What is the capital city of Australia?",
             "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "correct_answer": "Canberra"},
            {"question": "Who wrote the novel 'To Kill a Mockingbird'?",
             "options": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "F. Scott Fitzgerald"],
             "correct_answer": "Harper Lee"},
            {"question": "What is the largest organ in the human body?", "options": ["Liver", "Heart", "Skin", "Brain"],
             "correct_answer": "Skin"},
            {"question": "What is the deepest part of the ocean called?",
             "options": ["Mariana Trench", "Sunda Trench", "Puerto Rico Trench", "Java Trench"],
             "correct_answer": "Mariana Trench"},
            {"question": "Which artist painted 'The Starry Night'?",
             "options": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Salvador Dali"],
             "correct_answer": "Vincent van Gogh"},
            {"question": "What is the chemical formula for ozone?", "options": ["O3", "CO2", "H2O", "N2"],
             "correct_answer": "O3"},
            {"question": "Who discovered penicillin?",
             "options": ["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Jonas Salk"],
             "correct_answer": "Alexander Fleming"},
            {"question": "Which planet is known as the 'Morning Star'?",
             "options": ["Mercury", "Venus", "Mars", "Jupiter"], "correct_answer": "Venus"},
            {"question": "Who was the first woman to win a Nobel Prize?",
             "options": ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Emmy Noether"],
             "correct_answer": "Marie Curie"},
            {"question": "Which country is known as the 'Land of the Rising Sun'?",
             "options": ["China", "Japan", "South Korea", "Vietnam"], "correct_answer": "Japan"},
            {"question": "Who composed the 'Moonlight Sonata'?",
             "options": ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Frederic Chopin"],
             "correct_answer": "Ludwig van Beethoven"},
            {"question": "What is the world's largest ocean?",
             "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
             "correct_answer": "Pacific Ocean"},
            {"question": "Who is known as the 'Father of Computing'?",
             "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"],
             "correct_answer": "Charles Babbage"},
            {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Fe", "Cu"],
             "correct_answer": "Au"},
            {"question": "What is the tallest mountain in the world?",
             "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "correct_answer": "Mount Everest"},
            {"question": "Which city is known as the 'City of Love'?",
             "options": ["Paris", "Venice", "Rome", "Florence"], "correct_answer": "Paris"},
            {"question": "Who was the first person to step on the moon?",
             "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"],
             "correct_answer": "Neil Armstrong"}
        ]

        # Initialize variables to keep track of quiz progress
        self.current_question_index = 0
        self.correct_answers = 0
        self.selected_options = [""] * len(self.questions)
        self.radio_buttons = []  # List to store radio buttons for each question

        # Set up the user interface
        self.initUI()

        # Apply styles to the UI elements
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 18px;
                color: #333333;
            }
            QRadioButton {
                font-size: 16px;
                color: #444444;
                padding-left: 10px;
            }
            QPushButton {
                font-size: 16px;
                color: #FFFFFF;
                background-color: #007BFF;
                border: 2px solid #007BFF;
                border-radius: 5px;
                padding: 10px 20px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #0056b3;
                border-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004080;
                border-color: #004080;
            }
            QTabWidget::pane {
                border: 2px solid #007BFF;
                border-radius: 10px;
                padding: 20px;
                background-color: #FFFFFF;
            }
            QTabBar::tab {
                background-color: #f0f0f0;
                color: #333333;
                border: 2px solid #007BFF;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                padding: 8px 16px;
                margin-top: 10px;
            }
            QTabBar::tab:selected {
                background-color: #007BFF;
                color: #FFFFFF;
            }
            QTabBar::tab:!selected {
                margin-top: 2px;
            }
            QTabBar::tab:hover {
                background-color: #0056b3;
            }
            QTabWidget::tab-bar {
                alignment: center;
            }
            QTabWidget::tab-bar:top {
                top: -2px;
            }
            QTabWidget::tab-bar:bottom {
                bottom: -2px;
            }
            QTabWidget::tab-bar:left {
                left: -2px;
            }
            QTabWidget::tab-bar:right {
                right: -2px;
            }
            QWidget#Quiz_Result {
                background-color: #f0f0f0;
            }
            QLabel#Result_Label {
                font-size: 24px;
                color: #333333;
                margin: 20px;
            }
        """)

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Quiz Program")
        self.setGeometry(100, 100, 500, 400)

        # Set up the tab widget to hold questions and results
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Add tabs for each question
        for i, question in enumerate(self.questions):
            self.add_question_tab(i)

        # Add Modify and Create New buttons
        modify_button = QPushButton("Modify Questions")
        modify_button.clicked.connect(self.modify_questions)
        create_button = QPushButton("Create New Question")
        create_button.clicked.connect(self.create_question)

        button_layout = QVBoxLayout()
        button_layout.addWidget(modify_button)
        button_layout.addWidget(create_button)
        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        
        self.tab_widget.addTab(button_widget, "Modify/Create")

        # Show the main window
        self.show()

    def add_question_tab(self, index):
        # Create a new tab for a question
        question = self.questions[index]
        question_tab = QWidget()
        layout = QVBoxLayout()

        # Add the question label
        question_label = QLabel(question["question"])
        layout.addWidget(question_label)

        # Add radio buttons for options
        options = []
        for option in question["options"]:
            radio_button = QRadioButton(option)
            options.append(radio_button)
            layout.addWidget(radio_button)

        self.radio_buttons.append(options)

        # Add submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.check_answer)
        layout.addWidget(submit_button)

        question_tab.setLayout(layout)
        self.tab_widget.addTab(question_tab, f"Question {index + 1}")

    def check_answer(self):
        # Check which radio button is selected for the current question
        selected_button = None
        for button in self.radio_buttons[self.current_question_index]:
            if button.isChecked():
                selected_button = button
                break

        if selected_button:
            selected_option = selected_button.text()
            # Check if the selected option is correct
            if selected_option == self.questions[self.current_question_index]["correct_answer"]:
                self.correct_answers += 1

            # Move to the next question
            self.current_question_index += 1
            if self.current_question_index < len(self.questions):
                self.tab_widget.setCurrentIndex(self.current_question_index)
            else:
                self.show_result()

    def show_result(self):
        # Display the final result after all questions are answered
        result_widget = QWidget()
        result_layout = QVBoxLayout()
        result_label = QLabel(f"You got {self.correct_answers} out of {len(self.questions)} questions right!")
        result_label.setObjectName("Result_Label")
        result_layout.addWidget(result_label)
        result_widget.setLayout(result_layout)
        self.tab_widget.addTab(result_widget, "Result")
        self.tab_widget.setCurrentWidget(result_widget)

    def modify_questions(self):
        # Open the dialog to modify existing questions
        modify_questions(self.questions)

    def create_question(self):
        # Open the dialog to create a new question
        create_question(self.questions, self.add_question_tab)


def main():
    # Initialize Pygame and create the quiz application
    pygame.init()
    app = QApplication(sys.argv)
    quiz = Quiz()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
