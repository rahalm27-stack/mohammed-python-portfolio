from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
("Python Calculator","Python • Functions • Loops","A menu-based calculator with math operations, error handling, user input, and a step-by-step GCF algorithm.",["Functions","while loops","if/elif/else","input()","try/except"]),
("Math Operations Practice","Python • Operators • Data Types","Practice with division and remainders, rounding, ranges, averages, GCF, lists, and binary-to-decimal conversion.",["Operators","Lists","Built-ins","Data types","Functions"]),
("Cafeteria Receipt Project","Python • Real-world logic","A receipt program that converts prices to cents, reads different number formats, calculates totals, and handles a buy-4-get-5th-free rule.",["Functions","Numbers","String formatting","Integer math"]),
("CodeHS Python Work","Python • CodeHS","Coursework building skills with variables, functions, input, operators, conditions, loops, lists, and debugging.",["Variables","Functions","Input","Conditions","Loops","Debugging"]),
("Karel Projects","Python • Problem Solving","Practice with Karel and control structures such as if, if/else, and while.",["Control flow","while","if/else","Debugging"]),
("AI + Docker / Ollama","AI • Docker • Local Models","Worked with Docker and Ollama to run a local AI model and learn how AI tools can work on a computer.",["Docker","Ollama","AI","Local models"])
]

SKILLS = ["Python","CodeHS","Functions","Variables","Data Types","Input","Math Operators","Comparison Operators","Logical Operators","If Statements","Loops","Lists","Debugging","Karel","Error Handling","Docker","Ollama","AI"]

@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS, skills=SKILLS)

if __name__ == "__main__":
    app.run(debug=True)
