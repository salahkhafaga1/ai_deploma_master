import tkinter as tk  # Import tkinter for GUI
import numpy as np  # Import numpy for numerical operations

class SalaryPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AMIT - Machine Learning Diploma")
        self.root.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        # Header section
        header = tk.Label(self.root, text="AMIT - Machine Learning Diploma", 
                          bg="blue", fg="white", font=("Arial", 28, "bold"))
        header.pack(fill=tk.X)

        # Sidebar with project labels
        sidebar = tk.Frame(self.root, bg="lightgrey", width=150)
        sidebar.pack(fill=tk.Y, side=tk.LEFT)
        project_labels = ["Linear Regression", "Project2", "Project3", 
                          "Project4", "Project5", "Project6", 
                          "Project7", "Project8", "Project9"]
        for label in project_labels:
            lbl = tk.Label(sidebar, text=label, bg="lightgrey", anchor="w", 
                           padx=15, font=("Arial", 16))
            lbl.pack(fill=tk.X, padx=7, pady=7)

        # Main section for salary prediction
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20)
        title = tk.Label(main_frame, text="Salary Prediction", font=("Arial", 24))
        title.pack(pady=10)

        # Experience input
        label = tk.Label(main_frame, text="Enter years of experience:", font=("Arial", 18))
        label.pack()
        self.experience_entry = tk.Entry(main_frame, font=("Arial", 18))
        self.experience_entry.pack()

        # Execute button
        execute_button = tk.Button(main_frame, text="Execute", 
                                   command=self.predict_salary, 
                                   bg="grey", fg="black", font=("Arial", 18))
        execute_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(main_frame, text="", font=("Arial", 20, "bold"))
        self.result_label.pack()

    def predict_salary(self):
        try:
            experience = float(self.experience_entry.get())
            # Use the given linear equation instead of training a model
            predicted_salary = 9357 * experience + 26089
            self.result_label.config(text=f"Your Expected Salary is: {int(predicted_salary)}", fg="green")
        except ValueError:
            self.result_label.config(text="Please enter a valid number", fg="red")

# Run the app if this script is executed directly
if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryPredictionApp(root)
    root.mainloop()
