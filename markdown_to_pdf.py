import markdown
from weasyprint import HTML

MARKDOWN_FILE = 'CV_purely_technical.md'
OUTPUT_FILE = 'Joseph_Walton_CV_2025_04_10.pdf'

# Read the Markdown file
with open(MARKDOWN_FILE, 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()

# Convert Markdown to HTML with custom CSS
html_content = markdown.markdown(md_content)
css = """
<style>
    body { font-family: 'Times New Roman', serif; margin: 30px; font-size: 14px; }
    h1 { font-size: 1.8em; }
    h2 { font-size: 1.6em; }
    h3 { font-size: 1.4em; }
    h4 { font-size: 1.2em; }
    h5 { font-size: 1.1em; }
    h6 { font-size: 1em; }
    p { font-size: 0.9em; line-height: 1.5; color: #333333; }
    table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
    th, td { border: 1px solid #ddd; padding: 6px; }
    th { background-color: #f2f2f2; color: #2E4053; }
    .section-title { font-size: 1.2em; margin-top: 10px; color: #1A5276; }
    .job-title { font-size: 1em; font-weight: bold; color: #2874A6; }
    .job-duration { font-size: 0.9em; font-style: italic; color: #5D6D7E; }
    .skills-list { list-style-type: none; padding: 0; font-size: 0.9em; }
    .skills-list li { margin-bottom: 4px; color: #2E4053; }
</style>
"""
html_content = f"{css}\n{html_content}"

# Step 4: Convert HTML to PDF
HTML(string=html_content).write_pdf(OUTPUT_FILE)