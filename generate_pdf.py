import sys
import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (Only on page 2+)
        if self._pageNumber > 1:
            self.drawString(54, 11 * inch - 36, "Case Study 10: Login Form & Successful Screen Viva Guide")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(54, 11 * inch - 42, 8.5 * inch - 54, 11 * inch - 42)
        
        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 54, 36, footer_text)
        self.drawString(54, 36, "Full Stack Web Development - Viva Preparation Document")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 8.5 * inch - 54, 48)
        
        self.restoreState()

def build_pdf(filename="Case_Study_10_Login_Form_Viva_Guide.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=12
    )
    
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1A365D"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=5
    )
    
    th_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.white,
        spaceAfter=2
    )

    th_light_style = ParagraphStyle(
        'TableLightHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#2B6CB0"),
        spaceAfter=2
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#1A202C"),
        backColor=colors.HexColor("#EDF2F7"),
        borderColor=colors.HexColor("#CBD5E0"),
        borderWidth=0.5,
        borderPadding=5,
        spaceBefore=4,
        spaceAfter=6
    )
    
    qa_q_style = ParagraphStyle(
        'QA_Q',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13.5,
        textColor=colors.HexColor("#2C5282"),
        spaceBefore=7,
        spaceAfter=2,
        keepWithNext=True
    )
    
    qa_a_style = ParagraphStyle(
        'QA_A',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#1A202C"),
        leftIndent=10,
        spaceAfter=6
    )
    
    tip_box_style = ParagraphStyle(
        'TipText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#742A2A")
    )
    
    story = []
    
    # Header Title
    story.append(Paragraph("CASE STUDY 10: LOGIN FORM &amp; SUCCESSFUL LOGIN SCREEN", title_style))
    story.append(Paragraph("<b>Complete Code Explanation &amp; Viva Examination Master Guide</b>", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#3182CE"), spaceAfter=10))
    
    # 1. Overview
    story.append(Paragraph("1. Project Overview &amp; Complete Application Flow", h1_style))
    story.append(Paragraph(
        "<b>Objective:</b> Build a responsive Login Form using HTML, CSS, and JavaScript. Enforce two mandatory validation rules and dynamically transition to a <b>Welcome Dashboard Screen</b> upon successful login:",
        body_style
    ))
    story.append(Paragraph("• <b>Validation Rule 1:</b> The Username field must not be left empty.", bullet_style))
    story.append(Paragraph("• <b>Validation Rule 2:</b> The Password field must contain at least 6 characters.", bullet_style))
    story.append(Paragraph("• <b>Success Screen Transition:</b> When validation passes, JavaScript hides the login form and displays a green <b>Login Successful Welcome Dashboard</b> showing the user's name and a Logout button.", bullet_style))
    story.append(Paragraph("• <b>Logout Functionality:</b> Clicking 'Logout' clears the form inputs and returns the user to the login screen.", bullet_style))
    story.append(Spacer(1, 6))
    
    # 2. Architecture Table
    story.append(Paragraph("2. Project Architecture &amp; Technologies", h1_style))
    table_data = [
        [Paragraph("File Name", th_light_style), Paragraph("Technology", th_light_style), Paragraph("Role / Purpose", th_light_style)],
        [Paragraph("<b>index.html</b>", body_style), Paragraph("HTML5", body_style), Paragraph("Defines 2 cards: Login Screen (#loginCard) and Welcome Screen (#welcomeCard).", body_style)],
        [Paragraph("<b>style.css</b>", body_style), Paragraph("CSS3", body_style), Paragraph("Centers layout with Flexbox, styles inputs, and defines .hidden class for screen switching.", body_style)],
        [Paragraph("<b>script.js</b>", body_style), Paragraph("JavaScript (ES6)", body_style), Paragraph("Handles submit event, validates inputs, switches DOM screens (.classList.add/remove), and handles logout.", body_style)]
    ]
    t = Table(table_data, colWidths=[1.1*inch, 1.2*inch, 4.4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EBF8FF")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))
    
    # 3. Source Code Breakdown
    story.append(Paragraph("3. Complete Source Code &amp; Breakdown", h1_style))
    
    story.append(Paragraph("A. HTML Dual-Screen Layout (index.html)", h2_style))
    html_code = """&lt;div id="loginCard" class="card"&gt;
  &lt;h2&gt;Account Login&lt;/h2&gt;
  &lt;div id="message-box" class="message-box hidden"&gt;&lt;/div&gt;
  &lt;form id="loginForm" novalidate&gt;
    &lt;input type="text" id="username" placeholder="Enter username"&gt;
    &lt;input type="password" id="password" placeholder="Enter password (min 6 chars)"&gt;
    &lt;button type="submit"&gt;Login&lt;/button&gt;
  &lt;/form&gt;
&lt;/div&gt;

&lt;!-- Welcome Dashboard (Hidden by default) --&gt;
&lt;div id="welcomeCard" class="card hidden"&gt;
  &lt;div class="success-badge"&gt;✓&lt;/div&gt;
  &lt;h2&gt;Login Successful!&lt;/h2&gt;
  &lt;p&gt;Welcome back, &lt;span id="userDisplayName"&gt;User&lt;/span&gt;!&lt;/p&gt;
  &lt;button type="button" id="logoutBtn" class="logout-btn"&gt;Logout&lt;/button&gt;
&lt;/div&gt;"""
    story.append(Paragraph(html_code, code_style))
    
    story.append(Paragraph("<b>Key HTML Highlights for Viva:</b>", body_style))
    story.append(Paragraph("• <b>Dual Card Structure:</b> Both <code>#loginCard</code> and <code>#welcomeCard</code> reside in the HTML body.", bullet_style))
    story.append(Paragraph("• <b>.hidden Utility Class:</b> <code>#welcomeCard</code> has <code>class=\"card hidden\"</code> so it starts hidden on page load.", bullet_style))
    
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("B. CSS Screen Toggling &amp; Styling (style.css)", h2_style))
    css_code = """/* Hides elements from layout */
.hidden { display: none !important; }

/* Centered layout */
body { display: flex; justify-content: center; align-items: center; min-height: 100vh; }
.card { width: 100%; max-width: 400px; padding: 30px; border-radius: 12px; }

/* Success badge styling */
.success-badge {
  width: 60px; height: 60px; background-color: #def7ec; color: #03543f;
  border-radius: 50%; font-size: 32px; font-weight: bold;
}"""
    story.append(Paragraph(css_code, code_style))
    
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("C. JavaScript Screen Switcher Logic (script.js)", h2_style))
    js_code = """const loginCard = document.getElementById('loginCard');
const welcomeCard = document.getElementById('welcomeCard');
const loginForm = document.getElementById('loginForm');
const userDisplayName = document.getElementById('userDisplayName');
const logoutBtn = document.getElementById('logoutBtn');

loginForm.addEventListener('submit', function (event) {
  event.preventDefault(); // Stop page reload

  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim();

  if (username === '') { showError('Username cannot be empty!'); return; }
  if (password.length &lt; 6) { showError('Password must be at least 6 chars!'); return; }

  // Successful Login -&gt; Switch screens!
  userDisplayName.textContent = username;
  loginCard.classList.add('hidden');
  welcomeCard.classList.remove('hidden');
});

logoutBtn.addEventListener('click', function () {
  welcomeCard.classList.add('hidden');
  loginCard.classList.remove('hidden');
  loginForm.reset();
});"""
    story.append(Paragraph(js_code, code_style))
    
    story.append(Spacer(1, 10))
    story.append(PageBreak())
    
    # 4. Master Viva Q&A
    story.append(Paragraph("4. Master Viva Questions &amp; Answers (Top 20)", h1_style))
    story.append(Paragraph("Memorize these exact answers for your oral examination:", body_style))
    story.append(Spacer(1, 4))
    
    viva_qa = [
        ("Q1: What happens after the user successfully logs in?",
         "Ans: Upon successful validation (non-empty username and password &gt;= 6 chars), JavaScript updates the welcome text with the user's name, adds the '.hidden' CSS class to the login form card, and removes '.hidden' from the Welcome Dashboard card."),
        
        ("Q2: How is the screen transition between Login and Welcome Dashboard accomplished?",
         "Ans: By toggling the CSS class '.hidden' (which has 'display: none !important') using JavaScript DOM methods: loginCard.classList.add('hidden') and welcomeCard.classList.remove('hidden')."),
        
        ("Q3: Why do we call event.preventDefault() on form submission?",
         "Ans: By default, submitting a form reloads the browser. event.preventDefault() cancels page reload so JavaScript can validate input and display the Welcome Screen dynamically."),
        
        ("Q4: How does the Logout button work?",
         "Ans: The Logout button has a 'click' event listener that hides the Welcome Card (classList.add('hidden')), shows the Login Card (classList.remove('hidden')), and resets all form fields using loginForm.reset()."),
        
        ("Q5: What is the purpose of .trim() on input values?",
         "Ans: .trim() removes leading and trailing whitespace characters so users cannot bypass empty username validation by typing space characters."),
        
        ("Q6: How do you display dynamic text like 'Welcome, [Username]' in JavaScript?",
         "Ans: By selecting the target HTML element using document.getElementById('userDisplayName') and updating its text content via userDisplayName.textContent = username."),
        
        ("Q7: What is the difference between client-side and server-side validation?",
         "Ans: Client-side runs instantly in the user's browser via JavaScript to improve user experience. Server-side validation runs on the backend server for security."),
        
        ("Q8: Why is novalidate used on the &lt;form&gt; tag?",
         "Ans: novalidate disables default browser HTML5 validation bubbles, allowing custom JavaScript error messages and styled alert boxes to display uniformly across all browsers."),
        
        ("Q9: What is DOM in web development?",
         "Ans: DOM (Document Object Model) is a tree-like programming interface created by the browser representing HTML elements as objects that JavaScript can inspect, modify, and style."),
        
        ("Q10: Why place the &lt;script&gt; tag at the bottom of the body tag?",
         "Ans: To ensure all HTML DOM nodes are fully parsed and rendered before JavaScript attempts to attach event listeners or select elements."),
        
        ("Q11: What is box-sizing: border-box in CSS?",
         "Ans: It forces elements to include padding and border within their specified width and height, preventing layout breaks and overflow."),
        
        ("Q12: What does classList.toggle() or classList.add() do in JavaScript?",
         "Ans: classList provides methods to manipulate CSS classes on an HTML element. .add('hidden') attaches a class while .remove('hidden') detaches it."),
        
        ("Q13: Why use input type=\"password\"?",
         "Ans: It automatically masks typed characters as dots/asterisks, protecting sensitive passwords from being visible on screen."),
        
        ("Q14: How is Flexbox used in this project?",
         "Ans: Flexbox (display: flex; justify-content: center; align-items: center;) on the body element centers the active card horizontally and vertically on screen."),
        
        ("Q15: What is textContent vs innerHTML?",
         "Ans: textContent sets raw plain text (safe from XSS security risks). innerHTML parses strings as HTML code. We use textContent for displaying usernames safely."),
        
        ("Q16: What is an Event Listener in JavaScript?",
         "Ans: An event listener is a method attached to a DOM node (like a form or button) that monitors user events ('submit', 'click') and executes a callback function when triggered."),
        
        ("Q17: How is password length checked in JavaScript?",
         "Ans: By evaluating password.length &lt; 6. If true, an error message 'Password must be at least 6 characters long!' is shown."),
        
        ("Q18: What is the difference between '==' and '===' in JavaScript?",
         "Ans: '==' performs type coercion before comparison. '===' compares both value AND data type strictly. We use '===' for safe evaluation."),
        
        ("Q19: How does the application reset error states?",
         "Ans: A resetMessages() function runs before validation, hiding error boxes and removing red border outline classes (.input-error) from input elements."),
        
        ("Q20: How would you connect this to a real backend database?",
         "Ans: By making an asynchronous HTTP request using fetch() or axios to send JSON credentials to a backend API (Node.js/Python/Java), receiving an authentication token (JWT), and storing it in localStorage.")
    ]
    
    for q, a in viva_qa:
        story.append(Paragraph(f"<b>{q}</b>", qa_q_style))
        story.append(Paragraph(a, qa_a_style))
    
    story.append(Spacer(1, 10))
    story.append(PageBreak())
    
    # 5. Cheat Sheet
    story.append(Paragraph("5. Viva Day 5-Minute Quick Revision Cheat Sheet", h1_style))
    story.append(Paragraph("Review this table 5 minutes before entering your viva:", body_style))
    story.append(Spacer(1, 6))
    
    cheatsheet_data = [
        [Paragraph("Concept", th_style), Paragraph("1-Line Quick Explanation", th_style)],
        [Paragraph("<b>Validation Goal</b>", body_style), Paragraph("Username != empty AND Password &gt;= 6 characters.", body_style)],
        [Paragraph("<b>Success Screen</b>", body_style), Paragraph("Hides Login Card &amp; reveals Welcome Dashboard with user's name.", body_style)],
        [Paragraph("<b>event.preventDefault()</b>", body_style), Paragraph("Stops form submit from reloading the browser page.", body_style)],
        [Paragraph("<b>.classList.add('hidden')</b>", body_style), Paragraph("Applies display: none to hide an HTML card dynamically.", body_style)],
        [Paragraph("<b>Logout Action</b>", body_style), Paragraph("Resets form inputs and returns user to the login screen.", body_style)],
        [Paragraph("<b>.trim()</b>", body_style), Paragraph("Strips blank spaces from start &amp; end of input text.", body_style)],
        [Paragraph("<b>textContent</b>", body_style), Paragraph("Safely updates user name on the welcome screen without XSS risk.", body_style)],
        [Paragraph("<b>Flexbox Centering</b>", body_style), Paragraph("<code>display: flex; justify-content: center; align-items: center;</code>", body_style)]
    ]
    
    cs_table = Table(cheatsheet_data, colWidths=[2.0*inch, 4.7*inch])
    cs_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1A365D")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(cs_table)
    
    story.append(Spacer(1, 15))
    
    advice_text = "<b>GOLDEN DEMONSTRATION STEPS:</b> Open <code>index.html</code> in a browser.<br/>1. Click <b>Login</b> with blank fields -&gt; Shows <i>'Username cannot be empty!'</i> error.<br/>2. Enter Username 'alex' &amp; Password '123' -&gt; Shows <i>'Password must be at least 6 characters long!'</i> error.<br/>3. Enter Password '123456' -&gt; Card smoothly transitions to <b>Login Successful Welcome Dashboard</b> displaying <b>'Welcome back, alex!'</b>.<br/>4. Click <b>Logout</b> -&gt; Resets and returns to login form! Examiners love this 2-screen transition!"
    
    advice_box = Table([[Paragraph(advice_text, tip_box_style)]], colWidths=[6.7*inch])
    advice_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFF5F5")),
        ('BORDER', (0,0), (-1,-1), 1, colors.HexColor("#FEB2B2")),
        ('PADDING', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(advice_box)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generated successfully: {filename}")

if __name__ == '__main__':
    build_pdf()
