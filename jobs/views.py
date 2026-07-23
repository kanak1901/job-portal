from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import UserProfile

from .forms import ApplicationForm, JobForm
from .models import Application, Job


def home(request):
    featured_jobs = Job.objects.filter(is_active=True)[:6]
    total_jobs = Job.objects.filter(is_active=True).count()
    context = {
        'featured_jobs': featured_jobs,
        'total_jobs': total_jobs,
    }
    return render(request, 'home.html', context)


def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    query = request.GET.get('q', '').strip()
    location = request.GET.get('location', '').strip()
    job_type = request.GET.get('job_type', '').strip()

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query)
            | Q(company__icontains=query)
            | Q(description__icontains=query)
        )
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    context = {
        'jobs': jobs,
        'query': query,
        'location': location,
        'job_type': job_type,
        'job_type_choices': Job.JOB_TYPE_CHOICES,
    }
    return render(request, 'jobs/job_list.html', context)


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    has_applied = False
    if request.user.is_authenticated:
        has_applied = Application.objects.filter(job=job, applicant=request.user).exists()

    context = {
        'job': job,
        'has_applied': has_applied,
    }
    return render(request, 'jobs/job_detail.html', context)


@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    profile = getattr(request.user, 'profile', None)

    if profile and profile.is_employer:
        messages.error(request, 'Employers cannot apply for jobs.')
        return redirect('job_detail', pk=pk)

    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.info(request, 'You have already applied for this job.')
        return redirect('job_detail', pk=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job_detail', pk=pk)
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})


@login_required
def employer_dashboard(request):
    profile = getattr(request.user, 'profile', None)
    if not profile or not profile.is_employer:
        messages.error(request, 'Access denied. Employer account required.')
        return redirect('home')

    jobs = Job.objects.filter(posted_by=request.user)
    applications = Application.objects.filter(job__posted_by=request.user)

    context = {
        'jobs': jobs,
        'applications': applications,
        'profile': profile,
    }
    return render(request, 'jobs/employer_dashboard.html', context)


@login_required
def post_job(request):
    profile = getattr(request.user, 'profile', None)
    if not profile or not profile.is_employer:
        messages.error(request, 'Access denied. Employer account required.')
        return redirect('home')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            if not job.company:
                job.company = profile.company_name
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('employer_dashboard')
    else:
        initial = {'company': profile.company_name} if profile.company_name else {}
        form = JobForm(initial=initial)

    return render(request, 'jobs/post_job.html', {'form': form})
