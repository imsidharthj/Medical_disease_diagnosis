from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Disease, Symptom
from .forms import PatientForm
from fuzzywuzzy import fuzz
from tabulate import tabulate

def patient_data(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            symptoms = [s.strip().lower().replace('_', ' ') for s in form.cleaned_data['symptoms'].split(',')]
            
            matched_diseases = match_symptoms(symptoms)
            return render(request, 'patients/patient_data.html', {
                'name': name,
                'age': age,
                'symptoms': symptoms,
                'matched_diseases': matched_diseases
            })
    else:
        form = PatientForm()
    
    return render(request, 'patients/patient_form.html', {'form': form})

def match_symptoms(symptoms_to_match, threshold=80):
    matched_diseases = []
    diseases = Disease.objects.all()
    for disease in diseases:
        disease_symptoms = disease.symptoms.values_list('name', flat=True)
        matched = all(any(fuzz.ratio(symptom, s) >= threshold for s in disease_symptoms) for symptom in symptoms_to_match)
        if matched:
            matched_diseases.append(disease.name)
    return matched_diseases
