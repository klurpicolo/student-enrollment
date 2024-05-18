import tkinter as tk
from tkinter import ttk, messagebox
from model import Grade


class AdminPage(tk.Frame):
    def __init__(self, parent, controller, student_repository):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.student_repository = student_repository
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)
        self.notebook = notebook

        self.show = self.create_show_tab(notebook)
        self.group = self.create_group_tab(notebook)
        self.partition = self.create_partition_tab(notebook)
        self.remove = self.create_remove_tab(notebook)
        self.clean = self.create_clean_tab(notebook)
        self.all_frame = [self.show, self.group, self.partition, self.remove, self.clean]

    def re_render(self):
        for widget in self.notebook.winfo_children():
            widget.destroy()
        self.show = self.create_show_tab(self.notebook)
        self.group = self.create_group_tab(self.notebook)
        self.partition = self.create_partition_tab(self.notebook)
        self.remove = self.create_remove_tab(self.notebook)
        self.clean = self.create_clean_tab(self.notebook)

    def create_show_tab(self, notebook):
        show_frame = ttk.Frame(notebook)
        notebook.add(show_frame, text="Show")

        tree = ttk.Treeview(show_frame, columns=("ID", "Name", "Email"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Email", text="Email")
        tree.pack(fill="both", expand=True)

        students = self.student_repository.get_all_students()
        for student in students:
            tree.insert("", "end", values=(student.id, student.name, student.email))
        return show_frame

    def create_group_tab(self, notebook):
        group_frame = ttk.Frame(notebook)
        notebook.add(group_frame, text="Group")
        group_label = ttk.Label(group_frame, text="Group students by grade", font=("Verdana", 20))
        group_label.pack()

        # Create a Treeview widget
        tree = ttk.Treeview(group_frame, columns=("grade", "id", "name"), show="headings")
        tree.heading("grade", text="Grade")
        tree.heading("id", text="ID")
        tree.heading("name", text="Name")
        tree.pack()

        grade_to_student = {}
        for student in self.student_repository.get_all_students():
            if len(student.enrolled_subjects) == 0:
                continue
            sum_mark = sum(sub.mark for sub in student.enrolled_subjects)
            grade = Grade.from_mark(sum_mark / len(student.enrolled_subjects))
            if grade not in grade_to_student:
                grade_to_student[grade] = []
            grade_to_student[grade].append(student)

        # Populate the treeview with data
        for grade, students in grade_to_student.items():
            for student in students:
                tree.insert("", "end", values=(str(grade), student.id, student.name))

        return group_frame

    def create_partition_tab(self, notebook):
        partition_frame = ttk.Frame(notebook)
        notebook.add(partition_frame, text="Partition")
        partition_label = ttk.Label(partition_frame, text="Partition student by pass/fail", font=("Verdana", 20))
        partition_label.pack()

        pass_student = []
        failed_student = []
        for student in self.student_repository.get_all_students():
            if len(student.enrolled_subjects) == 0:
                continue
            sum_mark = sum(sub.mark for sub in student.enrolled_subjects)
            grade = Grade.from_mark(sum_mark / len(student.enrolled_subjects))
            if grade == Grade.Z:
                failed_student.append(student)
            else:
                pass_student.append(student)

        # Create a Treeview widget
        tree = ttk.Treeview(partition_frame, columns=("grade", "id", "name"), show="headings")
        tree.heading("grade", text="Grade")
        tree.heading("id", text="ID")
        tree.heading("name", text="Name")
        tree.pack()

        for student in pass_student:
            tree.insert("", "end", values=("Pass", student.id, student.name))
        for student in failed_student:
            tree.insert("", "end", values=("Failed", student.id, student.name))

        return partition_frame

    def create_remove_tab(self, notebook):
        remove_frame = ttk.Frame(notebook)
        notebook.add(remove_frame, text="Remove")
        remove_label = ttk.Label(remove_frame, text="Remove student", font=("Verdana", 20))
        remove_label.pack()

        # Function to handle removal of a student
        def remove_student(event):
            item = tree.selection()[0]  # Get the selected item
            student_id = tree.item(item, "values")[0]  # Get the student ID
            student_name = tree.item(item, "values")[1]
            confirmation = messagebox.askyesno("Confirmation",
                                               f"Are you sure you want to remove {student_name} student?")
            if confirmation:
                if self.student_repository.remove_student(student_id):
                    tree.delete(item)  # Remove the selected item from the Treeview
                    messagebox.showinfo("Success", f"Student with ID {student_id} has been removed.")
                    self.re_render()
                else:
                    messagebox.showerror("Error", "Failed to remove student.")

        # Populate Treeview with student data
        tree = ttk.Treeview(remove_frame, columns=("ID", "Name", "Email"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Email", text="Email")
        tree.pack(fill="both", expand=True)

        students = self.student_repository.get_all_students()
        for student in students:
            tree.insert("", "end", values=(student.id, student.name, student.email))

        # Bind the remove_student function to the Button-1 event (left-click) on the Treeview
        tree.bind("<Button-1>", remove_student)

        return remove_frame

    def create_clean_tab(self, notebook):
        clean_frame = ttk.Frame(notebook)
        notebook.add(clean_frame, text="Clean Database")

        clean_button = ttk.Button(clean_frame, text="Clean All Data", command=self.clean_database)
        clean_button.pack(pady=20)

        return clean_frame

    def clean_database(self):
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to clean all data?")
        if confirmation:
            try:
                self.student_repository.clean_database()
                messagebox.showinfo("Success", "All data has been cleaned.")
                self.re_render()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to clean data: {str(e)}")
