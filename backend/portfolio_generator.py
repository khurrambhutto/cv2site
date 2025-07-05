import json
from datetime import datetime

def generate_portfolio(data: dict) -> str:
    """
    Generates a single-file HTML portfolio from a JSON resume dictionary using a Tailwind CSS template.

    Args:
        data (dict): The dictionary containing the resume data.

    Returns:
        A string containing the HTML portfolio.
    """
    try:
        # --- Helper functions to generate dynamic HTML sections ---

        def get_header_section(data):
            name = data.get('name', 'Your Name')
            
            # Use the first job title as a tagline, or a default
            experience = data.get('experience')
            if experience and isinstance(experience, list) and len(experience) > 0:
                tagline = experience[0].get('job_title', 'Professional Profile')
            else:
                tagline = 'Professional Profile'

            contact = data.get('contact_information', {})
            email = contact.get('email')
            phone = contact.get('phone')
            linkedin = contact.get('linkedin')
            github = contact.get('github')

            contact_html = ""
            if email:
                contact_html += f"""
                <a href="mailto:{email}" class="flex items-center space-x-2 link-hover">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" /><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" /></svg>
                    <span>{email}</span>
                </a>"""
            if phone:
                contact_html += f"""
                <a href="tel:{phone}" class="flex items-center space-x-2 link-hover">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.774a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" /></svg>
                    <span>{phone}</span>
                </a>"""
            if linkedin:
                contact_html += f"""
                <a href="{linkedin}" target="_blank" rel="noopener noreferrer" class="flex items-center space-x-2 link-hover">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-5 w-5"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.27V9.773h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.462 2.462 0 01-2.462-2.465c0-1.366.992-2.465 2.462-2.465 1.473 0 2.466 1.099 2.466 2.465 0 1.367-.993 2.465-2.466 2.465zm1.785 13.019H3.55v-11.66h3.572v11.66zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.453c.979 0 1.776-.773 1.776-1.729V1.729C24 .774 23.203 0 22.225 0z"/></svg>
                    <span>LinkedIn</span>
                </a>"""
            if github:
                contact_html += f"""
                <a href="{github}" target="_blank" rel="noopener noreferrer" class="flex items-center space-x-2 link-hover">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-5 w-5"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.529 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.953 0-1.098.392-1.998 1.03-2.704-.103-.254-.446-1.284.098-2.67 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.026 2.747-1.026.546 1.386.202 2.416.099 2.67.638.706 1.029 1.606 1.029 2.704 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.579.688.482C21.137 20.175 24 16.42 24 12.017 24 6.484 19.522 2 12 2z" clip-rule="evenodd" /></svg>
                    <span>GitHub</span>
                </a>"""

            return f"""
            <header class="text-center mb-12">
                <h1 class="text-5xl md:text-6xl font-extrabold text-gray-900 mb-4">{name}</h1>
                <p class="text-xl md:text-2xl text-gray-600 mb-6">{tagline}</p>
                <div class="flex flex-wrap justify-center gap-x-6 gap-y-3 text-lg text-gray-700">
                    {contact_html}
                </div>
            </header>
            """

        def get_summary_section(summary):
            if not summary: return ""
            return f"""
            <section class="mb-12">
                <h2 class="section-title">Summary</h2>
                <p class="text-lg leading-relaxed text-gray-700">{summary}</p>
            </section>
            """

        def get_experience_section(experience):
            if not experience: return ""
            items_html = ""
            for item in experience:
                desc_html = "".join(f"<li>{d}</li>" for d in item.get('description', []))
                items_html += f"""
                <div class="card">
                    <h3 class="text-xl font-semibold text-gray-800">{item.get('job_title', 'N/A')} at {item.get('company', 'N/A')}</h3>
                    <p class="text-indigo-600 font-medium">{item.get('location', '')}</p>
                    <p class="text-gray-600 text-sm">{item.get('dates', 'N/A')}</p>
                    <ul class="list-disc list-inside mt-3 text-gray-700 leading-relaxed space-y-1">
                        {desc_html}
                    </ul>
                </div>
                """
            return f"""
            <section class="mb-12">
                <h2 class="section-title">Experience</h2>
                <div class="space-y-6">{items_html}</div>
            </section>
            """

        def get_education_section(education):
            if not education: return ""
            items_html = ""
            for item in education:
                items_html += f"""
                <div class="card">
                    <h3 class="text-xl font-semibold text-gray-800">{item.get('institution', 'N/A')}</h3>
                    <p class="text-indigo-600 font-medium">{item.get('degree', 'N/A')}</p>
                    <p class="text-gray-600 text-sm">{item.get('dates', 'N/A')}</p>
                </div>
                """
            return f"""
            <section class="mb-12">
                <h2 class="section-title">Education</h2>
                <div class="space-y-6">{items_html}</div>
            </section>
            """

        def get_projects_section(projects):
            if not projects: return ""
            items_html = ""
            for item in projects:
                tech = ", ".join(item.get('technologies', []))
                desc_html = "".join(f"<li>{d}</li>" for d in item.get('description', []))
                items_html += f"""
                <div class="card">
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">{item.get('name', 'N/A')}</h3>
                    <p class="text-indigo-600 text-sm mb-3">
                        <span class="font-medium">Technologies:</span> {tech}
                    </p>
                    <ul class="list-disc list-inside mt-3 text-gray-700 leading-relaxed space-y-1">
                        {desc_html}
                    </ul>
                </div>
                """
            return f"""
            <section class="mb-12">
                <h2 class="section-title">Projects</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">{items_html}</div>
            </section>
            """
        
        def get_certifications_section(certifications):
            if not certifications: return ""
            items_html = ""
            for cert in certifications:
                items_html += f"""
                <div class="card">
                    <h3 class="text-xl font-semibold text-gray-800">{cert.get('name', 'N/A')}</h3>
                    <p class="text-indigo-600 font-medium">{cert.get('issuer', 'N/A')}</p>
                    <p class="text-gray-600 text-sm">{cert.get('date', 'N/A')}</p>
                    <p class="text-gray-700 leading-relaxed mt-3">{cert.get('description', '')}</p>
                </div>
                """
            return f"""
            <section class="mb-12">
                <h2 class="section-title">Certifications</h2>
                <div class="space-y-6">{items_html}</div>
            </section>
            """

        def get_skills_section(skills):
            if not skills: return ""
            items_html = "".join(f'<span class="bg-indigo-100 text-indigo-800 px-4 py-2 rounded-full font-medium">{skill}</span>' for skill in skills)
            return f"""
            <section class="mb-12">
                <h2 class="section-title">Skills</h2>
                <div class="flex flex-wrap gap-3 text-lg">{items_html}</div>
            </section>
            """

        # --- Main HTML Template ---
        html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
            color: #334155;
        }}
        .section-title {{
            font-size: 1.875rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 1.5rem;
            border-bottom-width: 2px;
            border-color: #6366f1;
            padding-bottom: 0.5rem;
        }}
        .card {{
            background-color: white;
            padding: 1.5rem;
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            transition: box-shadow 0.3s ease-in-out;
        }}
        .card:hover {{
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        }}
        .link-hover:hover {{
            color: #4f46e5;
            text-decoration: underline;
        }}
    </style>
</head>
<body class="antialiased">
    <div class="container mx-auto px-4 py-8 md:py-16 max-w-4xl">

        {header_section}
        {summary_section}
        {experience_section}
        {education_section}
        {projects_section}
        {certifications_section}
        {skills_section}

        <footer class="text-center text-gray-500 text-sm mt-12 pt-8 border-t border-gray-200">
            &copy; {current_year} {name}. All rights reserved.
        </footer>

    </div>
</body>
</html>
        """

        # --- Populate and generate the final HTML ---
        populated_html = html_template.format(
            name=data.get('name', 'Your Name'),
            current_year=datetime.now().year,
            header_section=get_header_section(data),
            summary_section=get_summary_section(data.get('summary')),
            experience_section=get_experience_section(data.get('experience')),
            education_section=get_education_section(data.get('education')),
            projects_section=get_projects_section(data.get('projects')),
            certifications_section=get_certifications_section(data.get('certifications')),
            skills_section=get_skills_section(data.get('skills'))
        )

        return populated_html

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""
