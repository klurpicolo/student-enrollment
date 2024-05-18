import tkinter as tk
from tkinter import ttk, messagebox

from model import Subject
from validator import validate_password

LARGEFONT = ("Verdana", 35)


class StudentCoursePage(tk.Frame):

    def __init__(self, parent, controller, student_repository):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.student_repository = student_repository

        label = ttk.Label(self, text="Student course page", font=LARGEFONT)
        label.pack()
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Show Tab
        show_frame = ttk.Frame(notebook)
        notebook.add(show_frame, text="Show")
        show_label = ttk.Label(show_frame, text="Show Courses", font=("Verdana", 20))
        show_label.pack()
        self.show_frame = show_frame

        # Enroll Tab
        enroll_frame = ttk.Frame(notebook)
        notebook.add(enroll_frame, text="Enroll")
        enroll_button = ttk.Button(enroll_frame, text="Enroll", command=self.enroll_subject)
        enroll_button.pack()

        # Remove Tab
        withdraw_frame = ttk.Frame(notebook)
        notebook.add(withdraw_frame, text="Remove")
        self.withdraw_frame = withdraw_frame
        login_label = ttk.Label(withdraw_frame, text="Enter subject id to withdraw", font=("Verdana", 20))
        login_label.grid(row=0, column=0, columnspan=2, pady=10)

        subject_id_label = ttk.Label(withdraw_frame, text="Subject Id:")
        subject_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.to_remove_subject = ttk.Entry(withdraw_frame)
        self.to_remove_subject.grid(row=1, column=1, padx=5, pady=5)

        def withdraw_subject():
            subjects = self.controller.logged_in_student.enrolled_subjects
            to_remove = self.to_remove_subject.get()
            is_found = False
            for subject in subjects:
                if subject.id == to_remove:
                    is_found = True
                    confirmation = messagebox.askyesno("Confirmation",
                                                       f"Are you sure you want to remove {to_remove} subject?")
                    if confirmation:
                        self.controller.logged_in_student.withdraw_subject(subject)
                        self.student_repository.update_student(self.controller.logged_in_student)
                        messagebox.showinfo("Success", f"Subject with ID {to_remove} has been removed.")
                self.re_render()
                break
            if not is_found:
                messagebox.showerror("Error", f"Subject {to_remove} is not found")

        withdraw_button = ttk.Button(withdraw_frame, text="withdraw", command=withdraw_subject)
        withdraw_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Change Password Tab
        change_password_frame = ttk.Frame(notebook)
        notebook.add(change_password_frame, text="Change Password")
        change_password_label = ttk.Label(change_password_frame, text="Change Password", font=("Verdana", 20))
        change_password_label.pack()

        new_password_label = ttk.Label(change_password_frame, text="New Password:")
        new_password_label.pack()
        new_password_entry = ttk.Entry(change_password_frame, show="*")  # Mask password entry
        new_password_entry.pack()

        confirm_password_label = ttk.Label(change_password_frame, text="Confirm Password:")
        confirm_password_label.pack()
        confirm_password_entry = ttk.Entry(change_password_frame, show="*")  # Mask password entry
        confirm_password_entry.pack()

        def change_password():
            new_password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()

            if not validate_password(new_password):
                messagebox.showerror("Error",
                                     "Invalid password format. Password should start with an uppercase letter, "
                                     "followed by at least 5 letters and end with at least 3 digits.")
                return

            if new_password == confirm_password:
                # Update student's password
                current_student = self.controller.logged_in_student
                current_student.password = new_password
                self.student_repository.update_student(current_student)
                messagebox.showinfo("Password Changed", "Your password has been changed successfully.")
            else:
                messagebox.showerror("Error", "New password and confirmed password do not match.")

        change_password_button = ttk.Button(change_password_frame, text="Change Password", command=change_password)
        change_password_button.pack()

    def enroll_subject(self):
        # Create a new subject and enroll it
        new_subject = Subject()
        current_student = self.controller.logged_in_student
        is_success = current_student.enroll(new_subject)
        if not is_success:
            messagebox.showerror("Error", "You already enroll 4 subjects")
        else:
            self.student_repository.update_student(current_student)
            self.re_render()
            messagebox.showinfo("Enrollment Successful", f"The subject has been enrolled successfully:\n"
                                                         f"ID: {new_subject.id}\n"
                                                         f"Mark: {new_subject.mark}\n"
                                                         f"Grade: {new_subject.grade}")

    def re_render(self):
        for widget in self.show_frame.winfo_children():
            widget.destroy()
        tree = ttk.Treeview(self.show_frame, columns=("ID", "Mark", "Grade"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Mark", text="Mark")
        tree.heading("Grade", text="Grade")
        tree.pack(fill="both", expand=True)
        enrolled_subjects = self.controller.logged_in_student.enrolled_subjects
        for subject in enrolled_subjects:
            tree.insert("", "end", values=(subject.id, subject.mark, subject.grade))
