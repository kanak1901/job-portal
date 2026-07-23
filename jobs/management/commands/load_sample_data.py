from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from accounts.models import UserProfile
from jobs.models import Job


class Command(BaseCommand):
    help = 'Populate the database with sample jobs and demo accounts'

    def handle(self, *args, **options):
        employer, created = User.objects.get_or_create(
            username='employer_demo',
            defaults={
                'email': 'employer@demo.com',
                'first_name': 'Demo',
                'last_name': 'Employer',
            },
        )
        if created:
            employer.set_password('demo1234')
            employer.save()
            self.stdout.write(self.style.SUCCESS('Created employer: employer_demo / demo1234'))

        profile, _ = UserProfile.objects.get_or_create(user=employer)
        profile.user_type = UserProfile.USER_TYPE_EMPLOYER
        profile.company_name = 'TechCorp India'
        profile.phone = '9876543210'
        profile.save()

        seeker, created = User.objects.get_or_create(
            username='seeker_demo',
            defaults={
                'email': 'seeker@demo.com',
                'first_name': 'Demo',
                'last_name': 'Seeker',
            },
        )
        if created:
            seeker.set_password('demo1234')
            seeker.save()
            self.stdout.write(self.style.SUCCESS('Created seeker: seeker_demo / demo1234'))

        sample_jobs = [
            {
                'title': 'Python Developer',
                'company': 'TechCorp India',
                'location': 'Bangalore',
                'job_type': Job.JOB_TYPE_FULL_TIME,
                'salary': '₹8,00,000 - ₹12,00,000',
                'description': 'We are looking for a skilled Python Developer to join our backend team. You will work on building scalable web applications using Django and REST APIs.',
                'requirements': '- 2+ years Python experience\n- Django/Flask knowledge\n- REST API development\n- Git version control',
            },
            {
                'title': 'Frontend Developer',
                'company': 'WebSolutions Pvt Ltd',
                'location': 'Mumbai',
                'job_type': Job.JOB_TYPE_FULL_TIME,
                'salary': '₹6,00,000 - ₹10,00,000',
                'description': 'Join our frontend team to build beautiful, responsive user interfaces using React and modern JavaScript.',
                'requirements': '- HTML, CSS, JavaScript\n- React.js experience\n- Bootstrap/Tailwind CSS\n- Good communication skills',
            },
            {
                'title': 'Data Analyst Intern',
                'company': 'Analytics Hub',
                'location': 'Hyderabad',
                'job_type': Job.JOB_TYPE_INTERN,
                'salary': '₹15,000/month',
                'description': 'Internship opportunity for fresh graduates interested in data analysis. Work with real datasets and learn SQL, Python, and visualization tools.',
                'requirements': '- Pursuing or completed B.Tech/BCA\n- Basic Python and SQL\n- Excel proficiency\n- Eagerness to learn',
            },
            {
                'title': 'Remote UI/UX Designer',
                'company': 'DesignStudio',
                'location': 'Remote',
                'job_type': Job.JOB_TYPE_REMOTE,
                'salary': '₹5,00,000 - ₹8,00,000',
                'description': 'Create intuitive and visually appealing designs for web and mobile applications. Collaborate with developers and product managers.',
                'requirements': '- Figma/Adobe XD proficiency\n- Portfolio of past work\n- User research experience\n- 1+ year design experience',
            },
            {
                'title': 'HR Executive',
                'company': 'PeopleFirst HR',
                'location': 'Delhi NCR',
                'job_type': Job.JOB_TYPE_PART_TIME,
                'salary': '₹3,00,000 - ₹4,50,000',
                'description': 'Handle recruitment, onboarding, and employee engagement activities for our growing team.',
                'requirements': '- MBA in HR preferred\n- Recruitment experience\n- Good interpersonal skills\n- MS Office proficiency',
            },
            {
                'title': 'DevOps Engineer',
                'company': 'CloudNine Systems',
                'location': 'Pune',
                'job_type': Job.JOB_TYPE_FULL_TIME,
                'salary': '₹10,00,000 - ₹15,00,000',
                'description': 'Manage CI/CD pipelines, cloud infrastructure on AWS, and ensure high availability of production systems.',
                'requirements': '- AWS/Azure experience\n- Docker & Kubernetes\n- Linux administration\n- 3+ years DevOps experience',
            },
        ]

        for job_data in sample_jobs:
            job, created = Job.objects.get_or_create(
                title=job_data['title'],
                company=job_data['company'],
                defaults={**job_data, 'posted_by': employer},
            )
            if created:
                self.stdout.write(f'  Created job: {job.title}')

        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!'))
