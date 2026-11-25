from PyQt6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QInputDialog,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_signals()
        self.update_counter()

    def init_ui(self):
        self.setWindowTitle("Task Manager")
        self.resize(550, 400)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # labels
        self.label_title = QLabel("New Task")
        self.label_count = QLabel()
        # buttons
        self.btn_add = QPushButton("ADD")
        self.btn_done = QPushButton("DONE")
        self.btn_clear_done = QPushButton("CLEAR DONE")
        self.btn_edit = QPushButton("EDIT")
        self.btn_remove = QPushButton("REMOVE")
        self.btn_clear = QPushButton("CLEAR ALL")
        # other
        self.input_task = QLineEdit()
        self.input_task.setPlaceholderText("Task Name")
        self.task_list = QListWidget()

        layout_adding = QHBoxLayout()
        layout_adding.addWidget(self.input_task)
        layout_adding.addWidget(self.btn_add)
        layout_actions = QHBoxLayout()

        # actions
        # EDIT
        layout_actions.addWidget(self.btn_edit)
        # DONE / CLEAR DONE
        layout_done_col = QVBoxLayout()
        layout_done_col.addWidget(self.btn_done)
        layout_done_col.addWidget(self.btn_clear_done)
        layout_actions.addLayout(layout_done_col)
        # REMOVE / CLEAR ALL
        layout_remove_col = QVBoxLayout()
        layout_remove_col.addWidget(self.btn_remove)
        layout_remove_col.addWidget(self.btn_clear)
        layout_actions.addLayout(layout_remove_col)

        layout.addWidget(self.label_title)  # title
        layout.addLayout(layout_adding)     # text & ADD
        layout.addWidget(self.task_list)    # list
        layout.addLayout(layout_actions)    # actions
        layout.addWidget(self.label_count)  # count

        self.statusBar().showMessage("Ready")

    def connect_signals(self):
        self.btn_add.clicked.connect(self.add_task)
        self.btn_done.clicked.connect(self.mark_done)
        self.btn_clear_done.clicked.connect(self.clear_completed_tasks)
        self.btn_edit.clicked.connect(self.edit_task)
        self.btn_remove.clicked.connect(self.delete_task)
        self.btn_clear.clicked.connect(self.clear_tasks)
        self.input_task.returnPressed.connect(self.add_task)
        self.task_list.itemDoubleClicked.connect(self.edit_task)

    def add_task(self):
        task = self.input_task.text().strip()
        if task:
            self.task_list.addItem(task)
            self.input_task.clear()
            self.update_counter()
            self.statusBar().showMessage(f"Task '{task}' added", 3000)
        else:
            QMessageBox.warning(
                self,
                "I hate you!",
                "Enter task name, otherwise kill yourself."
            )

    def mark_done(self):
        row = self.task_list.currentRow()
        if row >= 0:
            item = self.task_list.item(row)
            font = item.font()
            is_done = not font.strikeOut()
            font.setStrikeOut(is_done)
            item.setFont(font)
            status_text = "completed" if is_done else "marked active"
            self.statusBar().showMessage(f"Task '{item.text()}' {status_text}", 3000)
        else:
            QMessageBox.warning(
                self,
                "I hate you!",
                "Select a task to mark, otherwise kill yourself."
            )

    def clear_completed_tasks(self):
        completed_rows = [
            i for i in range(self.task_list.count())
            if self.task_list.item(i).font().strikeOut()
        ]

        if not completed_rows:
            QMessageBox.warning(
                self,
                "I hate you!",
                "No completed tasks to remove, otherwise kill yourself."
            )
            return

        count = len(completed_rows)
        answer = QMessageBox.question(
            self,
            "Killing completed tasks (and yourself)",
            f"You're killing all {count} completed tasks, continue?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            for row in reversed(completed_rows):
                self.task_list.takeItem(row)
            self.update_counter()
            self.statusBar().showMessage(f"Removed {count} completed task(s)", 3000)

    def edit_task(self):
        row = self.task_list.currentRow()
        if row >= 0:
            item = self.task_list.item(row)
            new_text, ok = QInputDialog.getText(
                self,
                "Edit Task",
                "New task name:",
                text=item.text()
            )
            if ok and new_text.strip():
                old_text = item.text()
                item.setText(new_text.strip())
                self.statusBar().showMessage(f"Task '{old_text}' updated to '{new_text.strip()}'", 3000)
        else:
            QMessageBox.warning(
                self,
                "I hate you!",
                "Select a task to edit, otherwise kill yourself."
            )

    def delete_task(self):
        row = self.task_list.currentRow()
        if row >= 0:
            answer = QMessageBox.question(
                self,
                "Killing task (and yourself)",
                f"You're killing task '{self.task_list.item(row).text()}', continue?"
            )
            if answer == QMessageBox.StandardButton.Yes:
                self.task_list.takeItem(row)
                self.update_counter()
                self.statusBar().showMessage("Task deleted", 3000)
        else:
            QMessageBox.warning(
                self,
                "I hate you!",
                "Select a task to remove, otherwise kill yourself."
            )

    def clear_tasks(self):
        answer = QMessageBox.question(
            self,
            "Killing ALL tasks (and yourself)",
            "Do you really want to kill yourself.. sorry.. all tasks?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()
            self.statusBar().showMessage("All tasks cleared", 3000)

    def update_counter(self):
        self.label_count.setText(f"Task Count: {self.task_list.count()}")