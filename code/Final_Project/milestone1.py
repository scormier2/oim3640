import os
from flask import Flask, render_template, request, jsonify, send_file
import openai  # Assuming using OpenAI API as placeholder
from dotenv import load_dotenv
from io import BytesIO
from weasyprint import HTML

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('ANTHROPIC_API_KEY')  # or your Claude API key

# Placeholder for Claude API call
def generate_bullet_point(description):
    # You need to replace this with your actual Claude API call and prompt engineering
    # For demonstration, using a dummy response
    return f"Generated bullet point for: {description}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    experience_texts = data['experiences']
    bullet_points = []

    for desc in experience_texts:
        # Call Claude API here
        bullet = generate_bullet_point(desc)
        bullet_points.append(bullet)

    # Format résumé HTML (simple)
    résumé_html = render_template('résumé.html', bullet_points=bullet_points)
    return jsonify({'résumé_html': résumé_html})

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    html_content = request.json['html']
    pdf = BytesIO()
    HTML(string=html_content).write_pdf(pdf)
    pdf.seek(0)
    return send_file(pdf, attachment_filename='résumé.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Best Resume</title>
<style>
  body { font-family: Arial, sans-serif; margin: 20px; background-color: #f0f4f8; }
  h1 { text-align: center; }
  textarea { width: 100%; height: 100px; margin-bottom: 10px; }
  button { padding: 10px 20px; margin-top: 10px; }
  #résumé-preview { border: 1px solid #ccc; padding: 20px; margin-top: 20px; background: #fff; }
</style>
</head>
<body>
<h1>Best Resume Builder</h1>
<p>Enter your experiences below, one per line:</p>
<textarea id="experiences"></textarea>
<br/>
<button onclick="generateRésumé()">Generate Résumé</button>
<button onclick="downloadPDF()">Download PDF</button>

<div id="résumé-preview"></div>

<script>
function generateRésumé() {
    const experiences = document.getElementById('experiences').value.split('\n').filter(line => line.trim() !== '');
    fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ experiences: experiences })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('résumé-preview').innerHTML = data.résumé_html;
    });
}

function downloadPDF() {
    const htmlContent = document.getElementById('résumé-preview').innerHTML;
    fetch('/download_pdf', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ html: htmlContent })
    })
    .then(res => res.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'résumé.pdf';
        document.body.appendChild(a);
        a.click();
        a.remove();
    });
}
</script>
</body>
</html>

<div style="width: 8.5in; padding: 0.5in; font-family: Times New Roman, serif; font-size: 12pt;">
  <h2 style="text-align:center;">Maria Reyes</h2>
  <p style="text-align:center;">347-555-5555 | mariareyes@williams.edu</p>
  <hr/>
  <h3>Experience</h3>
  <ul>
    {% for bullet in bullet_points %}
      <li>{{ bullet }}</li>
    {% endfor %}
  </ul>
</div>