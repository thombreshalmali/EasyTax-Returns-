from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import webbrowser
import sqlite3

class TaxCalculatorApp:
    
    def __init__(self, root):
        self.root = root                            # Assigns the passed root window to the class attribute 'root'
        self.root.title("Income Tax Calculator")    # Sets the title of the main window

        # Set the size of the main window
        self.root.geometry("900x600")  # Width x Height     
        
        # Initialize variables with empty strings
        self.salary = StringVar(value="")
        self.rent_income = StringVar(value="")
        self.home_loan_interest_80eea = StringVar(value="")
        self.medical_insurance_premium = StringVar(value="")
        self.education_loan_interest = StringVar(value="")
        self.charity_donations_80g_a = StringVar(value="")
        self.charity_donations_80g_b = StringVar(value="")
        self.house_rent_paid = StringVar(value="")
        self.age_var = StringVar(value="0-60")     # Default selection when initially opened
        
        # Variables for investment deductions
        self.ded80c = StringVar(value="")
        self.ded80ccc = StringVar(value="")
        self.ded80ccd1 = StringVar(value="")
        self.ded80ccd1b = StringVar(value="")
        self.ded80ccd2 = StringVar(value="")
        self.ded80tt = StringVar(value="")

        # Variables for Database
        self.email_id_for_login_page = StringVar(value="")
        self.password_for_login_page = StringVar(value="")
        self.email_id_for_new_user_page = StringVar(value="")
        self.password_for_new_user_page = StringVar(value="")

        # Create frames for pages
        self.page0 = Frame(self.root)
        self.page1 = Frame(self.root)
        self.page2 = Frame(self.root)
        self.page3 = Frame(self.root)
        self.page4 = Frame(self.root)
        self.login_page = Frame(self.root)
        self.new_user_page = Frame(self.root)
        self.help_page = Frame(self.root)
        self.notice_page = Frame(self.root)

        # image paths
        self.home_page_bg_path = PhotoImage(file=r"C:\Users\Nancy\Downloads\bgimage.png")
        self.other_pages_bg_path = PhotoImage(file=r"C:\Users\Nancy\Downloads\bgotherpg.png")
        
        # constructor creates UI for Pages when excecuted
        # functions for creating each pages
        self.create_page0()
        self.create_page1()
        self.create_page2()
        self.create_page3()
        self.create_page4()
        self.create_login_page()
        self.create_new_user_page()
        self.create_help_page()
        self.create_notice_page()

        # Show the first page initially
        self.current_page = self.page0
        self.page0.pack(fill=BOTH, expand=True)     # 'pack' arranges the widget, 'fill=BOTH' allows it to expand both horizontally and vertically, 'expand=True' lets it take up any extra space

        # Database connection setup
        self.conn = sqlite3.connect('DBproject.db', timeout=10)  # Added timeout to prevent "database locked" error
        self.connect = self.conn.cursor()
        self.create_table()
        self.create_income_table()
        
    def create_table(self):
        self.connect.execute('''
        CREATE TABLE IF NOT EXISTS LoginCredentials (
            mail TEXT PRIMARY KEY,
            password TEXT
        )
        ''')
        self.conn.commit() 

    def create_income_table(self):
        # Drop the table if it exists
        self.connect.execute("DROP TABLE IF EXISTS FinancialData")
        
        # Create the table with the correct structure
        self.connect.execute('''
            CREATE TABLE IF NOT EXISTS FinancialData (
                id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                annual_salary REAL,
                rent_income REAL,
                savings_acc_interest REAL,
                taxable_income REAL,
                tax REAL,
                PRIMARY KEY (id, timestamp)  -- Composite primary key
        )''')
        self.conn.commit()

    def create_page0(self):                 # Create the UI for Page 0(home page).
        home_page_bg_label = Label(self.page0, image = self.home_page_bg_path)               # Create a label to hold the background image
        home_page_bg_label.place(relwidth=1, relheight=1)                   # relheight and relwidth have values from 0.0 to 1.0, defining how much percent of geometry it would take

        Button(self.page0, text="Login", command=self.go_to_login_page, font=("Arial", 15), padx=15, pady=5, bg="#EECACA", fg="black",activeforeground = "black", activebackground="#EECACA", relief=FLAT).place(x=310,y=350)
        Button(self.page0, text="New User", command=self.go_to_new_user_page, font=("Arial", 15), pady=5, bg="#EECACA", fg="black",activeforeground = "black", activebackground="#EECACA", relief=FLAT).place(x=490,y=350)

        Button(self.page0, text="Home", command=self.go_to_home_page, font=("Arial", 15), bg="#0B001A", fg="white",activeforeground = "white", activebackground="#0B001A", relief=FLAT).place(x=508,y=70)
        Button(self.page0, text="Notice", command=self.show_notice_page, font=("Arial", 15), bg="#0B001A", fg="white",activeforeground = "white", activebackground="#0B001A", relief=FLAT).place(x=591,y=70)
        Button(self.page0, text="About", command=self.show_about, font=("Arial", 15), bg="#0B001A", fg="white",activeforeground = "white", activebackground="#0B001A", relief=FLAT).place(x=681,y=70)
        Button(self.page0, text="FAQ", command=self.show_help_page, font=("Arial", 15), bg="#0B001A", fg="white",activeforeground = "white", activebackground="#0B001A", relief=FLAT).place(x=768,y=70)

        Label(self.page0, text="Welcome to EasyTax Returns", font=("Arial", 19, "bold"), bg="#534569", fg="white").place(x=274,y=235)
        Label(self.page0, text="Taxes made simple", font=("Arial", 17, "bold"), bg="#534569", fg="white").place(x=348,y=268)

        Button(self.page0, text="Exit", command=self.exit_app, font=("Arial", 15), bg="red", fg="white",activeforeground = "white", activebackground="#0B001A", relief=FLAT).place(x=10,y=552)

    def exit_app(self):
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            self.root.destroy()
        
    def show_about(self):
        about_message = ("Tax Calculator App\nVersion 1.0\nThis application helps you calculate your income tax based on inputs.\nDeveloped by Nancy Verma , Raina Girish, Shalmali Thombre, Saniya Mohan\nContact: snrs@gmail.com")
        messagebox.showinfo("About",about_message)

    def create_help_page(self):
        self.create_bg_image(self.help_page)          
        help_texts = [
            "1. What is an Income Tax Return (ITR)?\n   An ITR is a form that taxpayers use to report their income, expenses, and tax liabilities to the tax authorities.",
            "2. Who needs to file an ITR?\n   Individuals whose income exceeds the basic exemption limit, those claiming deductions,\n and certain categories of taxpayers must file.",
            "3. What are the different types of ITR forms?\n   There are several ITR forms (e.g., ITR-1, ITR-2, ITR-3) designed for different types of taxpayers and income sources.",
            "4. What documents are required to file an ITR?\n   Common documents include Form 16, bank statements, investment proofs, and details of deductions.",
            "5. What is the deadline for filing an ITR?\n   The deadline for individual taxpayers is usually July 31st of the assessment year, but it may vary based on circumstances.",
            "6. Can I file my ITR online?\n   Yes, taxpayers can file their returns online through the Income Tax Department's e-filing portal.",
            "7. What are the penalties for late filing?\n   Late filing can incur penalties, and taxpayers may also miss out on certain deductions.",
            "8. How do I check the status of my filed ITR?\n   The status can be checked on the Income Tax Department's e-filing website by entering the acknowledgment number.",
            "9. What should I do if I make a mistake in my ITR?\n   You can file a revised return to correct any mistakes made in the original filing.",
            "10. What is a tax refund, and how can I claim it?\n   A tax refund occurs when the taxpayer has paid more tax than their liability. You can claim it during the ITR filing process.",
        ]
        for idx, text in enumerate(help_texts):                                  # Add help texts to the help page
            help_label = Label(self.help_page, text=text, justify="left", font=("Arial", 12), bg="#0B001A", fg="white")
            help_label.grid(row=idx + 1, column=0, padx=20, pady=5, sticky="w")  # Add padding for better visibility

        # Create Back to Home Page button
        back_button = Button(self.help_page, text="Back to Home Page", command=self.go_to_home_page, font=("Arial", 12, "bold"), bg="#007BFF", fg="black", activeforeground="white", activebackground="#007BFF", relief=FLAT)
        back_button.grid(row=len(help_texts) + 1, column=0, padx=20, pady=20, sticky="w")  # Place the button below the help texts

    def create_notice_page(self):
        self.create_bg_image(self.notice_page)

        # Create a clickable link
        link = Label(self.notice_page, text="Click this to visit official government site", bg="#0B001A", fg="light blue", cursor="hand2")
        link.grid(row=0, column=0, padx=20, pady=10, sticky="w")  # Position the link at the start
        link.bind("<Button-1>", lambda e: self.open_link("https://www.incometax.gov.in/iec/foportal/"))

        tax_updates = [
            "1. New Tax Regime :\n Introduced with lower tax rates but fewer exemptions and deductions.\n Taxpayers can choose between the old and new regimes.",
            "2. Amendments to Deductions :\n Changes in specific deductions, such as those related to home loans, health insurance,\n and investments in specified savings schemes.",
            "3. Reporting of Digital Assets :\n Mandating disclosure of income from cryptocurrencies and other digital assets,\n along with applicable tax rates.",
            "4. TDS Changes :\n Modifications in Tax Deducted at Source (TDS) rates for various income types.",
            "5. Faceless Assessments and Appeals :\n Continuation of faceless assessments to streamline tax processes and reduce disputes.",
            "6. Updated Compliance Requirements :\n Stricter norms for high-value transactions, including the requirement for detailed reporting.",
            "7. Changes in Penalties and Provisions :\n Revised penalty structures for non-compliance or late filing of returns."
        ]
        for idx, text in enumerate(tax_updates):                                  # Add help texts to the help page
            help_label = Label(self.notice_page, text=text, justify="left", font=("Arial", 12), bg="#0B001A", fg="white")
            help_label.grid(row=idx + 1, column=0, padx=20, pady=5, sticky="w")  # Add padding for better visibility

        # Create Back to Home Page button
        back_button = Button(self.notice_page, text="Back to Home Page", command=self.go_to_home_page, font=("Arial", 12, "bold"), bg="#007BFF", fg="black", activeforeground="white", activebackground="#007BFF", relief=FLAT)
        back_button.grid(row=len(tax_updates) + 1, column=0, padx=20, pady=20, sticky="w")  # Place the button below the help texts

    def open_link(self, url):
        webbrowser.open_new(url)
        
    def create_login_page(self):            # Create the UI for login page.
        self.create_bg_image(self.login_page)

        title = Label(self.login_page, text="Login Page", font=("Arial", 16, "bold"), bg="#0B001A", fg="white").grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        Label(self.login_page, text="Enter email id and password", font=("Arial", 14), bg="#0B001A", fg="white").grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        self.create_labeled_entry(self.login_page, "Email:", self.email_id_for_login_page, 3)
        self.create_labeled_entry(self.login_page, "Password", self.password_for_login_page, 4)
        
        previous_button = Button(self.login_page, text="Back to Home Page", command=self.go_to_home_page, font=("Arial", 12, "bold"), bg="#007BFF", fg="black",activeforeground = "white", activebackground="#007BFF", relief=FLAT).grid(row=100, column=0, padx=20, pady=20, sticky="w")   
        submit_button = Button(self.login_page, text="Login", command=self.login_page_entry, font=("Arial", 12, "bold"), bg="#28A745", fg="black",activeforeground = "white", activebackground="#28A745", relief=FLAT).grid(row=100, column=1, padx=20, pady=20, sticky="e")

    def create_new_user_page(self):         # Create the UI for new user page.
        self.create_bg_image(self.new_user_page)

        title = Label(self.new_user_page, text="New User Registration", font=("Arial", 16, "bold"), bg="#0B001A", fg="white").grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        Label(self.new_user_page, text="Enter email id and password", font=("Arial", 14), bg="#0B001A", fg="white").grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        self.create_labeled_entry(self.new_user_page, "Email:", self.email_id_for_new_user_page, 3)
        self.create_labeled_entry(self.new_user_page, "Password", self.password_for_new_user_page, 4)

        previous_button = Button(self.new_user_page, text="Back to Home Page", command=self.go_to_home_page, font=("Arial", 12, "bold"), bg="#007BFF", fg="black",activeforeground = "white", activebackground="#007BFF", relief=FLAT).grid(row=100, column=0, padx=20, pady=20, sticky="w")   
        submit_button = Button(self.new_user_page, text="Register", command=self.new_user_entry, font=("Arial", 12, "bold"), bg="#28A745", activeforeground = "white", activebackground="#28A745", fg="black", relief=FLAT).grid(row=100, column=1, padx=20, pady=20, sticky="e")

    def create_page1(self):                 # Create the UI for Page 1.
        self.create_bg_image(self.page1)

        # Create the UI for Page 1.
        title = Label(self.page1, text="Income Details", font=("Arial", 17, "bold"), bg="#0B001A", fg="white").grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        Label(self.page1, text="Select Age Range :", font=("Arial", 14), bg="#0B001A", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        Radiobutton(self.page1, text="0-60", variable=self.age_var, value="0-60", font=("Arial", 14,), bg="#0B001A", fg="white", activeforeground = "white", activebackground="#0B001A", selectcolor="#0B001A").grid(row=2, column=1, padx=10, pady=5, sticky="w")
        Radiobutton(self.page1, text="60-80", variable=self.age_var, value="60-80", font=("Arial", 14), bg="#0B001A", fg="white", activeforeground = "white", activebackground="#0B001A", selectcolor="#0B001A").grid(row=3, column=1, padx=10, pady=5, sticky="w")
        Radiobutton(self.page1, text="80+", variable=self.age_var, value="80+", font=("Arial", 14), bg="#0B001A", fg="white", activeforeground = "white", activebackground="#0B001A", selectcolor="#0B001A").grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.create_labeled_entry(self.page1, "Annual Salary :", self.salary, 5)
        self.create_labeled_entry(self.page1, "Rent Income :", self.rent_income, 6)
        self.create_deduction_entry(self.page1, "80TTA / 80TTB (interest income on savings account) :", self.ded80tt, 7)
        
        self.create_navigation_buttons(self.page1, is_first_page=False)

    def create_page2(self):                 # Create the UI for Page 2.
        self.create_bg_image(self.page2)

        title = Label(self.page2, text="Deductions", font=("Arial", 18, "bold"), bg="#0B001A", fg="white").grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Explanatory text for deductions
        Label(self.page2, text="Enter the amount for the following deductions (if applicable):", font=("Arial", 15), bg="#0B001A", fg="white").grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        self.create_deduction_entry(self.page2, "80EEA - Home Loan Interest :", self.home_loan_interest_80eea, 2, "Interest paid on home loan under section 80EEA")
        self.create_deduction_entry(self.page2, "80D - Medical Insurance Premium :", self.medical_insurance_premium, 5, "Premiums paid for medical insurance under section 80D")
        self.create_deduction_entry(self.page2, "80E - Education Loan Interest :", self.education_loan_interest, 8, "Interest paid on education loan under section 80E")
        self.create_deduction_entry(self.page2, "80G(a) - Charity Donations (100% Deductible) :", self.charity_donations_80g_a, 11, "Donations made to registered charities under section 80G(a)")
        self.create_deduction_entry(self.page2, "80G(b) - Charity Donations (50% Deductible) :", self.charity_donations_80g_b, 14, "Donations made to registered charities under section 80G(b)")

        self.create_navigation_buttons(self.page2, is_first_page=False)

    def create_page3(self):                 # Create the UI for Page 3.
        self.create_bg_image(self.page3)
        
        title = Label(self.page3, text="Deductions on Investment", font=("Arial", 16, "bold"), bg="#0B001A", fg="white").grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Explanatory text for investment deductions
        Label(self.page3, text="Enter the amount for the following investment deductions (if applicable):", font=("Arial", 15), bg="#0B001A", fg="white").grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        self.create_deduction_entry(self.page3, "80C Investment :", self.ded80c, 2, "Investment made in ELSS, PPF, life insurance, etc. (Rs 1,50,000 limit)")
        self.create_deduction_entry(self.page3, "80CCC Payment :", self.ded80ccc, 5, "Payment made towards pension funds (Rs 1,50,000 limit)")
        self.create_deduction_entry(self.page3, "80CCD(1) Payment :", self.ded80ccd1, 8, "Payments towards pension schemes: 10% of basic salary + DA (employed), 20% of gross income (self-employed)")
        self.create_deduction_entry(self.page3, "80CCD(1B) Investment :", self.ded80ccd1b, 11, "Investments in NPS beyond Rs 1,50,000 limit under 80CCE (Rs 50,000 limit)")
        self.create_deduction_entry(self.page3, "80CCD(2) Contribution :", self.ded80ccd2, 14, "Employer’s contribution to NPS: 14% of basic salary + DA (central govt), 10% otherwise")

        self.create_navigation_buttons(self.page3, is_first_page=False)

    def create_page4(self):                 # Create the UI for Page 4.
        self.create_bg_image(self.page4)

        title = Label(self.page4, text="Summary", font=("Arial", 18, "bold"), bg="#0B001A", fg="white").grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Explanatory text for summary
        Label(self.page4, text="Review your details and calculate your tax", font=("Arial", 15), bg="#0B001A", fg="white").grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        self.create_navigation_buttons(self.page4, is_final_page=True)

        Button(self.page4, text="Exit", command=self.exit_app, font=("Arial", 15), bg="red", fg="white",activeforeground = "white", activebackground="#0B001A", relief=FLAT).place(x=10,y=552)

    # function for creating bg image for other pages
    def create_bg_image(self, parent):
        other_pages_bg_label = Label(parent, image=self.other_pages_bg_path)                # Create a label to hold the background image
        other_pages_bg_label.place(relwidth=1, relheight=1)                 # relheight and relwidth have values from 0.0 to 1.0, defining how much percent of geometry it would take

    # function to create labeled entry fields for Page 1, create_login_page, create_new_user_page.
    def create_labeled_entry(self, parent, label_text, variable, row):
        Label(parent, text=label_text, font=("Arial", 14), bg="#0B001A", fg="white").grid(row=row, column=0, padx=20, pady=10, sticky="e")
        entry = Entry(parent, textvariable=variable, font=("Arial", 14), bd=0, relief=GROOVE, highlightthickness=2, highlightbackground="#534569", bg="#EECACA")
        entry.grid(row=row, column=1, padx=20, pady=10, sticky="w")

    # function to create a deduction entry fields for Pages 2, 3, and 4.
    def create_deduction_entry(self, parent, label_text, variable, row, additional_info=""):
        Label(parent, text=label_text, font=("Arial", 14), bg="#0B001A", fg="white").grid(row=row, column=0, padx=20, pady=10, sticky="e")
        entry = Entry(parent, textvariable=variable, font=("Arial", 14), bd=0, relief=GROOVE, highlightthickness=2, highlightbackground="#534569", bg="#EECACA")
        entry.grid(row=row, column=1, padx=20, pady=10, sticky="w")
        if additional_info:
            Label(parent, text=additional_info, font=("Arial", 10), bg="#0B001A", fg="white").grid(row=row + 1, column=0, columnspan=2, padx=20, pady=5)

    # Creates navigation buttons for each page.
    def create_navigation_buttons(self, parent, is_first_page=False, is_final_page=False):
        if not is_first_page:
            prev_button = Button(parent, text="Previous", command=self.go_to_previous_page, font=("Arial", 12, "bold"), bg="#007BFF", activeforeground = "white", activebackground="#007bff", fg="black", relief=FLAT).grid(row=100, column=0, padx=20, pady=20, sticky="w")
        
        if not is_final_page:
            next_button = Button(parent, text="Next", command=self.go_to_next_page, font=("Arial", 12, "bold"), bg="#28A745", fg="black", activeforeground = "white", activebackground="#28A745", relief=FLAT).grid(row=100, column=1, padx=20, pady=20, sticky="e")
        else:
            submit_button = Button(parent, text="Calculate Tax", command=self.calculate_tax, font=("Arial", 12, "bold"), bg="#F44336", fg="black", activeforeground = "white", activebackground="#F44336", relief=FLAT).grid(row=100, column=1, padx=20, pady=20, sticky="e")

    # Navigate to the previous page.
    def go_to_previous_page(self):
        # Navigate to the previous page.
        current_index = [self.page0,self.page1, self.page2, self.page3, self.page4].index(self.current_page)    # Find the index of the current page in the list of pages
        if current_index > 0:                               # Check if the current page is not the first page (index > 0)
            self.current_page.pack_forget()                 # Hide the current page
            self.current_page = [self.page0,self.page1, self.page2, self.page3, self.page4][current_index - 1]  # Move to the previous page by accessing the page list at the current index - 1, and also updates current page to previous page
            self.current_page.pack(fill=BOTH, expand=True)  # Now display the previous page

    def go_to_next_page(self):
        # Navigate to the next page.
        current_index = [self.page0,self.page1, self.page2, self.page3, self.page4].index(self.current_page)    # Find the index of the current page in the list of pages
        if current_index < 4:                               # Check if the current page is not the last page (index < 4)
            self.current_page.pack_forget()
            self.current_page = [self.page0,self.page1, self.page2, self.page3, self.page4][current_index + 1]  # Move to the next page by accessing the page list at the current index + 1, and also updates current page to next page
            self.current_page.pack(fill=BOTH, expand=True)  # Now display the next page

    def go_to_login_page(self):
        self.current_page.pack_forget()
        self.current_page = self.login_page
        self.current_page.pack(fill=BOTH, expand=True)

    def go_to_new_user_page(self):
        self.current_page.pack_forget()
        self.current_page = self.new_user_page
        self.current_page.pack(fill=BOTH, expand=True)
            
    def go_to_home_page(self):
        self.current_page.pack_forget()
        self.current_page = self.page0
        self.current_page.pack(fill=BOTH, expand=True)

    def show_help_page(self):
        self.current_page.pack_forget()  # Hide the current page
        self.current_page = self.help_page
        self.current_page.pack(fill=BOTH, expand=True)

    def show_notice_page(self):
        self.current_page.pack_forget()  # Hide the current page
        self.current_page = self.notice_page
        self.current_page.pack(fill=BOTH, expand=True)

    def parse_optional_float(self, value):
        # Parse a string to a float, returning None if the string is empty.
        try:
            return float(value.strip()) if value.strip() else 0
        except ValueError:
            return 0
        
    def login_page_entry(self):
        # Retrieve the email and password entered by the user
        email = self.email_id_for_login_page.get()
        password = self.password_for_login_page.get()

        # Check if both email and password fields are filled
        if not email or not password:
            messagebox.showwarning("Input Error", "Please provide both email and password.")
            return

        # 'execute' method is called on the connection object to execute a SQL command, '?' is a placeholder for a parameter
        # in (email,) comma is necessary to treat it as tuple and not as a simple expression
        self.connect.execute('SELECT password FROM LoginCredentials WHERE mail = ?', (email,))
        result = self.connect.fetchone()                # Fetch the first row from the query result

        # Check if the email does not exist in the database
        if result is None:
            messagebox.showerror("Error", "No user associated with this email.")
        elif result[0] == password: # Access the first element of the result tuple, which contains the password associated with the provided email; if no user is found, result will be None.
            messagebox.showinfo("Login Success", "Login successful!")
            self.current_page.pack_forget()         # if password matches with mail, go to page1
            self.current_page = self.page1
            self.current_page.pack(fill=BOTH, expand=True)
        else:
            messagebox.showerror("Error", "Incorrect password.")     # Show an error message if the entered password is incorrect
        
    def new_user_entry(self):
        # Retrieve the email and password entered by the new user
        email = self.email_id_for_new_user_page.get()
        password = self.password_for_new_user_page.get()

        # Check if both email and password fields are filled
        if not email or not password:
            messagebox.showwarning("Input Error", "Please provide both email and password.")
            return

        # Validate the email against a list of allowed domains
        if not ( email.endswith('@gmail.com') or email.endswith('@student.mes.ac.in') or
                 email.endswith('@mes.ac.in') or email.endswith('@yahoo.com') or
                 email.endswith('@hotmail.com') or email.endswith('@outlook.com') or email.endswith('@protonmail.com') ):
            messagebox.showerror("Invalid Email", "Please use a valid email address.")
            return
        
        try:
            # Insert the new user's email and password into the LoginCredentials table
            self.connect.execute('INSERT INTO LoginCredentials (mail, password) VALUES (?, ?)', (email, password)) # This operation might fail if the email is already in use (a violation of the database's unique constraint).
            self.conn.commit()                                          # Commit the transaction to save changes(new user details) to the database
            messagebox.showinfo("Registration Successful", "New user registered. Please login with your credentials.")
            self.go_to_login_page()                                     # Redirect the user to the login page after successful registration

        except sqlite3.IntegrityError:
            # If an IntegrityError is raised during the INSERT operation (for instance, if the email already exists in the database), the program jumps to the corresponding except block
            # This block handles the case where the email is already registered in the database
            # If the INSERT fails due to a unique constraint violation (email already exists), show an error message
            messagebox.showerror("Error", "This email is already registered. Please use another email.")
        
    def calculate_tax(self):
        # Calculate and display the tax based on the inputs.
        salary_str = self.salary.get().strip()
        
        if not salary_str:
            messagebox.showerror("Input Error", "Please enter your salary.")
            return
        
        try:
            # Convert salary input from string to float
            salary = float(salary_str)
            
            # Parse optional fields, converting their values from string to float.
            # If the input is invalid or empty, a default value (usually None or 0.0) will be returned by the parse_optional_float method.
            rent_income = self.parse_optional_float(self.rent_income.get())
            home_loan_interest_80eea = self.parse_optional_float(self.home_loan_interest_80eea.get())
            medical_insurance_premium = self.parse_optional_float(self.medical_insurance_premium.get())
            education_loan_interest = self.parse_optional_float(self.education_loan_interest.get())
            charity_donations_80g_a = self.parse_optional_float(self.charity_donations_80g_a.get())
            charity_donations_80g_b = self.parse_optional_float(self.charity_donations_80g_b.get())
            house_rent_paid = self.parse_optional_float(self.house_rent_paid.get())
            ded80c = self.parse_optional_float(self.ded80c.get())
            ded80ccc = self.parse_optional_float(self.ded80ccc.get())
            ded80ccd1 = self.parse_optional_float(self.ded80ccd1.get())
            ded80ccd1b = self.parse_optional_float(self.ded80ccd1b.get())
            ded80ccd2 = self.parse_optional_float(self.ded80ccd2.get())

            ded80tta=0
            ded80ttb=0
            if self.age_var.get()== "0-60":
                ded80tta = self.parse_optional_float(self.ded80tt.get())
            else:
                ded80ttb = self.parse_optional_float(self.ded80tt.get())
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")
            return

        taxable_income=0
        tax=0
            
        # for age group 0-60
        if self.age_var.get() == "0-60":

            # initially assigning 0 to variables
            taxable_income=0
            tax=0
            total_deductions=0
            
            if ded80tta > 10000:                    # Section 80TTA: Max ₹10,000 deduction on interest from savings accounts
                ded80tta = 10000
            
            if rent_income > 250000:                # Rent income is tax-free up to ₹2,50,000
                rent_income =rent_income- 250000
            else:
                rent_income = 0
                
            if (ded80c + ded80ccc + ded80ccd1) > 150000:    # Deductions under section 80C, 80CCC, and 80CCD1 have a combined limit of ₹1,50,000
                ded80cce = 150000
            else:
                ded80cce = ded80c + ded80ccc + ded80ccd1

            if ded80ccd1b > 50000:                  # Section 80CCD(1B): Extra ₹50,000 deduction for NPS contributions
                ded80ccd1b = 50000
                
            if ded80ccd2 > (salary * 0.1):          # Section 80CCD(2): Employer's NPS contribution is deductible, but capped at 10% of salary, If the contribution exceeds this cap, it is limited to 10% of the salary.
                ded80ccd2 = salary * 0.1
                
            if home_loan_interest_80eea > 50000:    # Section 80EEA: Home loan interest for first-time buyers, max ₹50,000
                home_loan_interest_80eea = 50000
                
            if medical_insurance_premium > 25000:   # Section 80D: Medical insurance premiums, max ₹25,000 for individual (under 60)
                medical_insurance_premium = 25000

            # Calculate total deductions allowed
            total_deductions = (ded80cce or 0) + (ded80ccd1b or 0) + (ded80ccd2 or 0) + (home_loan_interest_80eea or 0) + \
                               (medical_insurance_premium or 0) + (education_loan_interest or 0) + (charity_donations_80g_a or 0) + \
                               (charity_donations_80g_b / 2 or 0)

            # Taxable income is salary + rent income + 80TTA deductions - ₹50,000 (standard deduction) - other deductions
            taxable_income = salary + (rent_income or 0) + (ded80tta or 0) - 50000 - total_deductions

            # Ensure taxable income doesn't go negative
            if taxable_income < 0:
                taxable_income = 0
        
            # Tax calculation
            if taxable_income > 250000 and taxable_income <= 500000:
                tax = (taxable_income - 250000) * 0.05
            elif taxable_income > 500000 and taxable_income <= 1000000:
                tax = (250000 * 0.05) + ((taxable_income - 500000) * 0.2)
            elif taxable_income > 1000000:
                tax = (250000 * 0.05) + (500000 * 0.2) + ((taxable_income - 1000000) * 0.3)
            elif taxable_income <= 250000:
                tax = 0
                taxable_income = 0

        # for age group 60-80
        if self.age_var.get() == "60-80":

            # initially assigning 0 to variables
            taxable_income=0
            tax=0
            total_deductions=0
            
            if ded80ttb > 50000:                    # Section 80TTB: Max ₹50,000 deduction on interest from savings accounts
                ded80ttb = 50000
            
            if rent_income > 250000:                # Rent income is tax-free up to ₹2,50,000
                rent_income =rent_income- 250000
            else:
                rent_income = 0
                
            if (ded80c + ded80ccc + ded80ccd1) > 150000:    # Deductions under section 80C, 80CCC, and 80CCD1 have a combined limit of ₹1,50,000
                ded80cce = 150000
            else:
                ded80cce = ded80c + ded80ccc + ded80ccd1

            if ded80ccd1b > 50000:                  # Section 80CCD(1B): Extra ₹50,000 deduction for NPS contributions
                ded80ccd1b = 50000
                
            if ded80ccd2 > (salary * 0.1):          # Section 80CCD(2): Employer's NPS contribution is deductible, but capped at 10% of salary, If the contribution exceeds this cap, it is limited to 10% of the salary.
                ded80ccd2 = salary * 0.1
                
            if home_loan_interest_80eea > 50000:    # Section 80EEA: Home loan interest for first-time buyers, max ₹50,000
                home_loan_interest_80eea = 50000
                
            if medical_insurance_premium > 50000:   # Section 80D: Medical insurance premiums, max ₹50,000 for individual (60-80)
                medical_insurance_premium = 50000

            # Calculate total deductions allowed
            total_deductions = (ded80cce or 0) + (ded80ccd1b or 0) + (ded80ccd2 or 0) + (home_loan_interest_80eea or 0) + \
                               (medical_insurance_premium or 0) + (education_loan_interest or 0) + (charity_donations_80g_a or 0) + \
                               (charity_donations_80g_b / 2 or 0)

            # Taxable income is salary + rent income + 80TTA deductions - ₹50,000 (standard deduction) - other deductions
            taxable_income = salary + (rent_income or 0) + (ded80ttb or 0) - 50000 - total_deductions

            # Ensure taxable income doesn't go negative
            if taxable_income < 0:
                taxable_income = 0
        
            # Tax calculation for age group 60-80
            if taxable_income > 300000 and taxable_income <= 500000:
                tax = (taxable_income - 300000) * 0.05                                       # 5% on income exceeding ₹3,00,000
            elif taxable_income > 500000 and taxable_income <= 1000000:
                tax = (200000 * 0.05) + ((taxable_income - 500000) * 0.2)                    # 5% on ₹2,00,000 + 20% on income exceeding ₹5,00,000
            elif taxable_income > 1000000:
                tax = (200000 * 0.05) + (500000 * 0.2) + ((taxable_income - 1000000) * 0.3)  # 5% on ₹2,00,000 + 20% on ₹5,00,000 + 30% on income exceeding ₹10,00,000
            elif taxable_income <= 300000:
                tax = 0                                                                      # No tax for income up to ₹3,00,000
                taxable_income = 0
        
        # for age group 80+
        if self.age_var.get() == "80+":
            
            # initially assigning 0 to variables
            taxable_income=0
            tax=0
            total_deductions=0
            
            if ded80ttb > 50000:                    # Section 80TTB: Max ₹50,000 deduction on interest from savings accounts
                ded80ttb = 50000
            
            if rent_income > 250000:                # Rent income is tax-free up to ₹2,50,000
                rent_income =rent_income- 250000
            else:
                rent_income = 0
                
            if (ded80c + ded80ccc + ded80ccd1) > 150000:    # Deductions under section 80C, 80CCC, and 80CCD1 have a combined limit of ₹1,50,000
                ded80cce = 150000
            else:
                ded80cce = ded80c + ded80ccc + ded80ccd1

            if ded80ccd1b > 50000:                  # Section 80CCD(1B): Extra ₹50,000 deduction for NPS contributions
                ded80ccd1b = 50000
                
            if ded80ccd2 > (salary * 0.1):          # Section 80CCD(2): Employer's NPS contribution is deductible, but capped at 10% of salary, If the contribution exceeds this cap, it is limited to 10% of the salary.
                ded80ccd2 = salary * 0.1
                
            if home_loan_interest_80eea > 50000:    # Section 80EEA: Home loan interest for first-time buyers, max ₹50,000
                home_loan_interest_80eea = 50000
                
            if medical_insurance_premium > 50000:   # Section 80D: Medical insurance premiums, max ₹1,00,000 for individual (80+)
                medical_insurance_premium = 50000

            # Calculate total deductions allowed
            total_deductions = (ded80cce or 0) + (ded80ccd1b or 0) + (ded80ccd2 or 0) + (home_loan_interest_80eea or 0) + \
                               (medical_insurance_premium or 0) + (education_loan_interest or 0) + (charity_donations_80g_a or 0) + \
                               (charity_donations_80g_b / 2 or 0)

            # Taxable income is salary + rent income + 80TTA deductions - ₹50,000 (standard deduction) - other deductions
            taxable_income = salary + (rent_income or 0) + (ded80ttb or 0) - 50000 - total_deductions

            # Ensure taxable income doesn't go negative
            if taxable_income < 0:
                taxable_income = 0
        
            # Tax calculation for age group 80+
            if taxable_income > 500000 and taxable_income <= 1000000:
                tax = (taxable_income - 500000) * 0.2                       # 20% on income between ₹5,00,000 and ₹10,00,000
            elif taxable_income > 1000000:
                tax = (500000 * 0.2) + ((taxable_income - 1000000) * 0.3)   # 20% on ₹5,00,000 + 30% on income exceeding ₹10,00,000
            elif taxable_income <= 500000:
                tax = 0                                                     # No tax for income up to ₹5,00,000
                taxable_income = 0

        email_id = self.email_id_for_login_page.get()       # Retrieve the email ID from the StringVar for use as a primary key in the database.

        # Using replace : Check if the email_id already exists in the database as it is primary key
        self.connect.execute('''INSERT OR REPLACE INTO FinancialData (id, annual_salary, rent_income, savings_acc_interest, taxable_income, tax)
                            VALUES (?, ?, ?, ?, ?, ?)''', (email_id, salary, rent_income, ded80tta or ded80ttb, taxable_income, tax))
        self.conn.commit()
            
        messagebox.showinfo("Tax Calculation Result",
                            f"Taxable Income: ₹ {taxable_income:,.2f}\n"          # Using f-strings to format the output and .2f for upto 2 decimals
                            f"Tax: ₹ {tax:,.2f}\n"
                            f"Deductions: ₹ {total_deductions:,.2f}")

if __name__ == "__main__":  # Checks if the script is being run directly, not imported as a module

    root = Tk()  # Creates the main window for the application using Tkinter

    # object of TaxCalculator app
    # Initializes the TaxCalculatorApp class, passing the main window (root) as an argument
    # This sets up the GUI components of the application, allowing the user to interact with the tax calculator
    app = TaxCalculatorApp(root)  

    # Starts the Tkinter event loop, waiting for user interaction and keeping the application running
    # Without this line, the window would open and close immediately, not allowing the user to see or interact with the app.
    root.mainloop()
