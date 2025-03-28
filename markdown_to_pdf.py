import markdown2
import pdfkit

# Specify the path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

# Step 2: Read the Markdown file
with open('CV.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()

# Step 3: Convert Markdown to HTML with custom CSS
html_content = markdown2.markdown(md_content, extras=["tables"])
css = """
<style>
    body { font-family: 'Times New Roman', serif; margin: 30px; }
    h1, h2, h3, h4, h5, h6 { color: #2E4053; font-weight: bold; }
    p { line-height: 1.6; color: #333333; }
    table { width: 100%; border-collapse: collapse; }
    th, td { border: 1px solid #ddd; padding: 8px; }
    th { background-color: #f2f2f2; color: #2E4053; }
    .section-title { font-size: 1.5em; margin-top: 10px; color: #1A5276; }
    .job-title { font-size: 1.2em; font-weight: bold; color: #2874A6; }
    .job-duration { font-style: italic; color: #5D6D7E; }
    .skills-list { list-style-type: none; padding: 0; }
    .skills-list li { margin-bottom: 5px; color: #2E4053; }
</style>
"""
html_content = f"{css}\n{html_content}"

# Step 4: Convert HTML to PDF
pdfkit.from_string(html_content, 'CV.pdf', configuration=config)