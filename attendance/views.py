# attendance/views.py

from django.shortcuts import redirect, render
from django.http import JsonResponse
import face_recognition
import numpy as np
from employees.models import Employee
from .models import AttendanceRecord
from datetime import datetime, date
from PIL import Image
import base64
from io import BytesIO
import json

def mark_attendance(request):
    if request.method == "POST":
        image_data = request.POST.get('image_data')
        if not image_data:
            return JsonResponse({'error': 'No image data provided'}, status=400)

        # Decode the base64 image
        format, imgstr = image_data.split(';base64,')
        img_data = base64.b64decode(imgstr)
        image = Image.open(BytesIO(img_data))

        # Convert image to RGB if it is not
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Convert image to numpy array
        image_array = np.array(image)

        # Extract face encodings from the image
        face_encodings = face_recognition.face_encodings(image_array)

        if not face_encodings:
            return JsonResponse({'error': 'No face found in the image'}, status=400)

        # Debug: Print the captured face encoding
        print(f"Captured Face Encoding: {face_encodings}")

        # Match the face encodings with stored employee face encodings
        found_match = False
        for face_encoding in face_encodings:
            employees = Employee.objects.exclude(face_encoding__isnull=True).exclude(face_encoding__exact='')

            for employee in employees:
                stored_encoding_str = employee.face_encoding
                if not stored_encoding_str:
                    print(f"Skipping employee {employee.employee_id}: No stored encoding")
                    continue

                # Ensure stored_encoding_str is not empty before attempting to parse as JSON
                if stored_encoding_str.strip() == '':
                    print(f"Skipping employee {employee.employee_id}: Empty stored encoding string")
                    continue

                # Attempt to parse stored_encoding_str as JSON
                stored_encoding_list = json.loads(stored_encoding_str)

                if not isinstance(stored_encoding_list, list):
                    print(f"Invalid face encoding format for employee {employee.employee_id}")
                    continue

                # Convert to numpy array
                stored_encoding = np.array(stored_encoding_list)

                # Debug: Print the stored face encoding
                print(f"Stored Encoding for {employee.employee_id}: {stored_encoding}")

                # Compare faces with a tolerance level
                results = face_recognition.compare_faces([stored_encoding], face_encoding, tolerance=1)

                # Debug: Print the comparison result
                print(f"Comparison result for {employee.employee_id}: {results[0]}")

                if results[0]:
                    # Face matched, mark attendance
                    found_match = True
                    today = date.today()
                    attendance_record, created = AttendanceRecord.objects.get_or_create(
                        user=employee.user,
                        date=today
                    )
                    if created:
                        # Mark the current time as check-in if no record exists for today
                        attendance_record.check_in_time = datetime.now().time()
                        attendance_record.status = 'present'
                        attendance_record.save()
                        #code to redirct to dashboard after marking attendance with a notification of attendance of employee marked succesfully
                        request.session['message'] = f"Attendance for {employee.first_name} {employee.last_name} has been successfully marked."
                        return redirect('dashboard')
                    else:
                        return JsonResponse({'info': 'Attendance already marked for today'}, status=200)

        if not found_match:
            return JsonResponse({'error': 'No matching employee found'}, status=404)

    return render(request, 'attendance_capture.html')
