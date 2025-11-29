import re

# Read the current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new About section
new_about = '''    <!-- About Section -->
    <section id="About" style="background-color: #000; padding: 70px 10%; min-height: auto;">
        <h1 class="subtitle">About <span>Me</span></h1>
        
        <div style="max-width: 1000px; margin: 50px auto; padding: 30px; border: 2px solid #0ef; border-radius: 10px;">
            <p style="color: aliceblue; font-size: 18px; line-height: 2; margin-bottom: 20px;">
                <strong>Lead Software Engineer</strong> with <strong>12+ years of Python expertise</strong>, specializing in AWS serverless architecture, data engineering, solving big data problems, and onboarding AI solutions. Currently serving as <strong>Technical Project Manager managing a 30+ member team</strong> at Quinnox Consulting.
            </p>
            <p style="color: aliceblue; font-size: 18px; line-height: 2; margin-bottom: 20px;">
                Holding a <strong>Master of Science in Computer Science from Washington State University (GPA 3.9/4.0)</strong> and <strong>AWS Certified Solutions Architect</strong>, I have delivered measurable impact at Fortune 500 companies including Fannie Mae, Bank of America, and Neiman Marcus.
            </p>
            <p style="color: aliceblue; font-size: 18px; line-height: 2; margin-bottom: 25px;">
                <strong>Key Achievements:</strong> 75% processing time reduction through automation, 70% data processing efficiency improvements, and $200K+ cost savings through innovative Python solutions.
            </p>
            <div style="text-align: center;">
                <a href="latest-resume.pdf" class="abtbtn-box" target="_blank">Download Resume</a>
            </div>
        </div>
    </section>

    <!-- Education Section -->'''

# Replace the old About section with the new one
new_content = re.sub(
    r'    <!-- About Section -->.*?    <!-- Education Section -->',
    new_about,
    content,
    flags=re.DOTALL
)

# Write the corrected content back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed About section layout successfully!")
