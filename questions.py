from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox, QMessageBox, QWidget, QScrollArea, QVBoxLayout

def modify_questions(questions):
    """
    Opens a dialog that allows users to modify existing questions.
    This dialog includes scroll functionality if there are many questions.
    """
    # Create the main dialog window
    dialog = QDialog()
    dialog.setWindowTitle("Modify Questions")

    # Create a QWidget to hold the form layout which will be placed in the scroll area
    form_widget = QWidget()
    form_layout = QFormLayout()
    
    # Create input fields for each question
    question_inputs = []  # List to hold input fields for each question
    for question in questions:
        # Create input fields for question text, options, and correct answer
        question_input = QLineEdit(question["question"])
        option_inputs = [QLineEdit(opt) for opt in question["options"]]
        correct_answer_input = QLineEdit(question["correct_answer"])
        question_inputs.append((question_input, option_inputs, correct_answer_input))
        
        # Add these fields to the form layout
        form_layout.addRow(f"Question: {question['question']}", question_input)
        for i, option_input in enumerate(option_inputs):
            form_layout.addRow(f"Option {i + 1}:", option_input)
        form_layout.addRow("Correct Answer:", correct_answer_input)

    # Create a scroll area to handle cases where the content exceeds the visible area
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    # Set the QWidget (with the form layout) as the widget inside the scroll area
    form_widget.setLayout(form_layout)
    scroll_area.setWidget(form_widget)

    # Create the layout for the dialog
    dialog_layout = QVBoxLayout()
    dialog_layout.addWidget(scroll_area)  # Add the scroll area to the dialog layout

    # Create buttons for 'Ok' and 'Cancel'
    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

    # Define what happens when the 'Ok' button is clicked
    def handle_modify():
        try:
            # Update the questions list with the modified values from input fields
            for i, (question_input, option_inputs, correct_answer_input) in enumerate(question_inputs):
                questions[i]["question"] = question_input.text()
                questions[i]["options"] = [opt.text() for opt in option_inputs]
                questions[i]["correct_answer"] = correct_answer_input.text()
            dialog.accept()  # Close the dialog with 'Ok' result
        except Exception as e:
            # Show an error message if something goes wrong
            QMessageBox.critical(dialog, "Error", f"An error occurred: {str(e)}")

    button_box.accepted.connect(handle_modify)  # Connect 'Ok' button to handle_modify function
    button_box.rejected.connect(dialog.reject)  # Connect 'Cancel' button to close the dialog

    # Add the button box to the dialog layout and set the layout for the dialog
    dialog_layout.addWidget(button_box)
    dialog.setLayout(dialog_layout)

    # Show the dialog and wait for user interaction
    dialog.exec_()

def create_question(questions, add_question_tab_callback):
    """
    Opens a dialog that allows users to create a new question.
    This dialog does not have scrolling as it assumes only one new question is added at a time.
    """
    # Create the main dialog window
    dialog = QDialog()
    dialog.setWindowTitle("Create New Question")

    # Create a form layout for the new question input fields
    form_layout = QFormLayout()

    # Create input fields for the new question's text, options, and correct answer
    question_input = QLineEdit()
    option_inputs = [QLineEdit() for _ in range(4)]  # Assuming 4 options for the new question
    correct_answer_input = QLineEdit()

    # Add these fields to the form layout
    form_layout.addRow("Question:", question_input)
    for i, option_input in enumerate(option_inputs):
        form_layout.addRow(f"Option {i + 1}:", option_input)
    form_layout.addRow("Correct Answer:", correct_answer_input)

    # Create buttons for 'Ok' and 'Cancel'
    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

    # Define what happens when the 'Ok' button is clicked
    def handle_create():
        try:
            # Create a new question dictionary from the input fields
            new_question = {
                "question": question_input.text(),
                "options": [opt.text() for opt in option_inputs],
                "correct_answer": correct_answer_input.text()
            }
            questions.append(new_question)  # Add the new question to the list
            add_question_tab_callback(len(questions) - 1)  # Call the callback to add a new tab for the new question
            dialog.accept()  # Close the dialog with 'Ok' result
        except Exception as e:
            # Show an error message if something goes wrong
            QMessageBox.critical(dialog, "Error", f"An error occurred: {str(e)}")

    button_box.accepted.connect(handle_create)  # Connect 'Ok' button to handle_create function
    button_box.rejected.connect(dialog.reject)  # Connect 'Cancel' button to close the dialog

    # Add the button box to the form layout and set the layout for the dialog
    form_layout.addRow(button_box)
    dialog.setLayout(form_layout)

    # Show the dialog and wait for user interaction
    dialog.exec_()
