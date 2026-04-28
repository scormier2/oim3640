**What is strictly Python:**  
- The Flask web server handling routes and API logic  
- The Claude API call using the Anthropic SDK or HTTP request with prompt engineering  
- The PDF generation using WeasyPrint  
- Environment variable management with `python-dotenv`  
- String processing to parse user input

**What is not strictly Python:**  
- HTML, CSS, and JavaScript for the frontend interface and user interaction  
- The Canvas API or visual layout rendering (if used for precise resume layout)

**AI Methods:**  
- The core method involves sending a structured prompt to the Claude API to generate impactful, formatted bullet points based on user descriptions. The prompt guides Claude to act as an expert resume writer trained on specific formats, ensuring outputs align with program standards.