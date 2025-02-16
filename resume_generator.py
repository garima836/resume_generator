import streamlit as st

# Set page configuration
st.set_page_config(page_title='Resume Generator', page_icon=':briefcase:', layout='centered')

# Main function
def main():
    st.title('Resume Generator :briefcase:')
    st.subheader('Craft your professional resume effortlessly!')

    # Personal Information
    st.header('Personal Information')
    name = st.text_input('Full Name')
    phone = st.text_input('Phone Number')
    email = st.text_input('Email')
    address = st.text_input('Address')
    linkedin = st.text_input('LinkedIn Profile URL')

    # Professional Summary
    st.header('Professional Summary')
    summary = st.text_area('Summarize your professional background and expertise.')

    # Education
    st.header('Academic Qualifications / Education')
    education_list = []
    edu_count = st.number_input('Number of Educational Qualifications', min_value=0, step=1)

    for i in range(int(edu_count)):
        st.subheader(f'Education {i + 1}')
        degree = st.text_input('Degree', key=f'degree_{i}')
        school = st.text_input('School/University', key=f'school_{i}')
        edu_duration = st.text_input('Duration (e.g., Sep 2015 - Jun 2019)', key=f'edu_duration_{i}')
        edu_details = st.text_area('Additional Details', key=f'edu_details_{i}')
        education_list.append({
            'degree': degree,
            'school': school,
            'duration': edu_duration,
            'details': edu_details
        })

    # Technical Skills
    st.header('Technical Skills')
    skills = st.text_area('List your technical skills separated by commas (e.g., Python, Data Analysis, Project Management)')

    # Projects
    st.header('Projects')
    project_list = []
    proj_count = st.number_input('Number of Projects', min_value=0, step=1)

    for i in range(int(proj_count)):
        st.subheader(f'Project {i + 1}')
        proj_name = st.text_input('Project Name', key=f'proj_name_{i}')
        proj_description = st.text_area('Project Description', key=f'proj_desc_{i}')
        project_list.append({
            'name': proj_name,
            'description': proj_description
        })

    # Internships
    st.header('Internships')
    internship_list = []
    intern_count = st.number_input('Number of Internships', min_value=0, step=1)

    for i in range(int(intern_count)):
        st.subheader(f'Internship {i + 1}')
        intern_role = st.text_input('Internship Role', key=f'intern_role_{i}')
        intern_company = st.text_input('Company', key=f'intern_company_{i}')
        intern_duration = st.text_input('Duration', key=f'intern_duration_{i}')
        intern_details = st.text_area('Internship Details', key=f'intern_details_{i}')
        internship_list.append({
            'role': intern_role,
            'company': intern_company,
            'duration': intern_duration,
            'details': intern_details
        })

    # Trainings
    st.header('Trainings')
    training_list = []
    train_count = st.number_input('Number of Trainings', min_value=0, step=1)

    for i in range(int(train_count)):
        st.subheader(f'Training {i + 1}')
        train_title = st.text_input('Training Title', key=f'train_title_{i}')
        train_institution = st.text_input('Institution', key=f'train_inst_{i}')
        train_duration = st.text_input('Duration', key=f'train_duration_{i}')
        train_details = st.text_area('Training Details', key=f'train_details_{i}')
        training_list.append({
            'title': train_title,
            'institution': train_institution,
            'duration': train_duration,
            'details': train_details
        })

    # Achievements
    st.header('Achievements')
    achievements = st.text_area('List your achievements (separate with commas)')

    # Extracurricular Activities
    st.header('Extracurricular Activities')
    activities = st.text_area('List your extracurricular activities (separate with commas)')

    # Strengths
    st.header('Strengths')
    strengths = st.text_area('List your strengths (separate with commas)')

    # Hobbies
    st.header('Hobbies')
    hobbies = st.text_area('List your hobbies (separate with commas)')

    # Generate Resume
    if st.button('Generate Resume'):
        st.success('Here is your generated resume:')
        # Display personal information
        if name:
            st.write(f"## {name}")
        contact_info = ''
        if phone:
            contact_info += f"**Phone:** {phone}  "
        if email:
            contact_info += f"**Email:** {email}  "
        if address:
            contact_info += f"**Address:** {address}  "
        if linkedin:
            contact_info += f"**LinkedIn:** [Profile]({linkedin})  "
        if contact_info:
            st.write(contact_info)
            st.markdown('---')
    
        # Professional Summary
        if summary:
            st.write('### Professional Summary')
            st.write(summary)
            st.markdown('---')
    
        # Education
        if any(edu['degree'] or edu['school'] for edu in education_list):
            st.write('### Academic Qualifications / Education')
            for edu in education_list:
                if edu['degree'] or edu['school']:
                    st.write(f"**{edu['degree']} | {edu['school']}**")
                    if edu['duration']:
                        st.write(f"*{edu['duration']}*")
                    if edu['details']:
                        st.write(edu['details'])
                    st.write('---')
    
        # Technical Skills
        if skills.strip():
            st.write('### Technical Skills')
            skill_list = [skill.strip() for skill in skills.split(',') if skill.strip()]
            st.write(', '.join(skill_list))
            st.write('---')
    
        # Projects
        if any(proj['name'] for proj in project_list):
            st.write('### Projects')
            for proj in project_list:
                if proj['name']:
                    st.write(f"**{proj['name']}**")
                    if proj['description']:
                        st.write(proj['description'])
                    st.write('---')
    
        # Internships
        if any(intern['role'] or intern['company'] for intern in internship_list):
            st.write('### Internships')
            for intern in internship_list:
                if intern['role'] or intern['company']:
                    st.write(f"**{intern['role']} | {intern['company']}**")
                    if intern['duration']:
                        st.write(f"*{intern['duration']}*")
                    if intern['details']:
                        st.write(intern['details'])
                    st.write('---')
    
        # Trainings
        if any(train['title'] or train['institution'] for train in training_list):
            st.write('### Trainings')
            for train in training_list:
                if train['title'] or train['institution']:
                    st.write(f"**{train['title']} | {train['institution']}**")
                    if train['duration']:
                        st.write(f"*{train['duration']}*")
                    if train['details']:
                        st.write(train['details'])
                    st.write('---')
    
        # Achievements
        if achievements.strip():
            st.write('### Achievements')
            achievement_list = [ach.strip() for ach in achievements.split(',') if ach.strip()]
            for ach in achievement_list:
                st.write(f"- {ach}")
            st.write('---')
    
        # Extracurricular Activities
        if activities.strip():
            st.write('### Extracurricular Activities')
            activity_list = [act.strip() for act in activities.split(',') if act.strip()]
            for act in activity_list:
                st.write(f"- {act}")
            st.write('---')
    
        # Strengths
        if strengths.strip():
            st.write('### Strengths')
            strengths_list = [strg.strip() for strg in strengths.split(',') if strg.strip()]
            st.write(', '.join(strengths_list))
            st.write('---')
    
        # Hobbies
        if hobbies.strip():
            st.write('### Hobbies')
            hobbies_list = [hobby.strip() for hobby in hobbies.split(',') if hobby.strip()]
            st.write(', '.join(hobbies_list))
            st.write('---')
    
        # Prompt to download or save the resume
        st.info('You can now save this page as a PDF or copy the content to your preferred word processor.')

if __name__ == '__main__':
    main()

    