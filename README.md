# ProU - Job Readiness Portal

A comprehensive full-stack web application for managing student placement activities, job applications, and skill assessments.

## 🚀 Tech Stack
- **Backend:** Python (FastAPI), SQLite, SQLAlchemy
- **Frontend:** HTML, CSS (Bootstrap 5), JavaScript (Fetch API), Chart.js, TomSelect
- **Deployment:** Render (Backend), Netlify (Frontend)

## 👥 Demo Credentials

### Admin Account
- **Email:** `admin@example.com`
- **Password:** `admin123`

### Student Accounts
| Name | Email | Password |
|------|-------|----------|
| Ajay | ajay@example.com | ajay@123 |
| Vijay | vijay@example.com | vijay |
| Sanjay | sanjay@example.com | sanjay |

## 📖 How to Use the Application

### For Students

#### 1. **Login**
- Visit the application URL
- Select "Student Login" tab
- Enter your credentials (e.g., `ajay@example.com` / `ajay@123`)
- Click "Login"

#### 2. **My Profile**
- View and update your personal information
- Update phone number and resume URL
- **Note:** Your placement status is read-only (only admins can change it)
- If you're placed, you'll see a congratulations banner! 🎉

#### 3. **Job Openings**
- Browse all available job postings
- View job details (company, location, type, description)
- Click "Apply Now" to opt-in for a job
- Already applied jobs show "Applied" status

#### 4. **My Applications**
- View all jobs you've applied to
- Track application status:
  - **OPTED_IN:** Application submitted
  - **INTERVIEW_SCHEDULED:** Interview scheduled
  - **OFFERED:** Congratulations! You got an offer
  - **REJECTED:** Application rejected
  - **WITHDRAWN:** You withdrew the application
- Withdraw applications if needed

#### 5. **Assessments**
- View all assessments assigned to you
- Check assessment status (ASSIGNED/COMPLETED)
- View your scores
- Take pending assessments

#### 6. **Change Password**
- Click "Change Password" in the sidebar
- Enter your new password
- Click "Update Password"

#### 7. **Logout**
- Click "Logout" in the sidebar to safely exit

---

### For Admins

#### 1. **Login**
- Visit the application URL
- Select "Admin Login" tab
- Enter admin credentials (`admin@example.com` / `admin123`)
- Click "Login"

#### 2. **Dashboard**
- View key metrics:
  - Total Students
  - Placed Students
  - Active Jobs
  - Total Applications
- Visualize data with interactive charts:
  - Application Funnel (Bar Chart)
  - Placement Rate (Doughnut Chart)

#### 3. **Manage Students**
- **View Students:** See all registered students with their status
- **Add Student:**
  - Click "+ Add Student"
  - Fill in name, email, password, and status
  - Click "Save"
- **Edit Student:**
  - Click "Edit" button on any student
  - Update information
  - Click "Save"
- **Student Status:**
  - "Looking for job" - Actively searching
  - "Placed" - Successfully placed

#### 4. **Manage Job Openings**
- **View Jobs:** See all posted job openings
- **Add Job:**
  - Click "+ Add Job"
  - Fill in title, company, location, type, and description
  - Click "Save"
- **View Applications:**
  - Click "Apps" button on any job
  - See all students who applied
  - Update application status (Interview Scheduled, Offered, Rejected, etc.)
- **Delete Job:** Click "Delete" to remove a job posting

#### 5. **Manage Assessments**
- **View Assessments:** See all created assessments
- **Add Assessment:**
  - Click "+ Add Assessment"
  - Enter title, description, and max score
  - Click "Save"
- **Assign to Students:**
  - Use the "Assign Assessment" form
  - Select student and assessment from dropdowns
  - Click "Assign"
- **View Assignments:** See all student-assessment assignments with scores
- **Delete:** Remove assessments or assignments

#### 6. **Manage Admins**
- View all admin users
- Add new admin accounts
- **Note:** Admin passwords can be changed via "Change Password"

#### 7. **Database Management**
- Advanced feature for direct database manipulation
- Select table from dropdown (Students, Jobs, Assessments, etc.)
- Add, edit, or delete records directly
- **Available Tables:**
  - Students
  - Job Openings
  - Assessments
  - Admin Users
  - Student Assessments
  - Job Opt-ins

#### 8. **Change Password**
- Click "Change Password" in the sidebar
- Enter new password
- Click "Update Password"

#### 9. **Logout**
- Click "Logout" to safely exit the admin panel

## 🎯 Key Features

### Student Features
✅ Profile management  
✅ Browse and apply for jobs  
✅ Track application status in real-time  
✅ View assigned assessments  
✅ Take assessments and view scores  
✅ Congratulations section for placed students  
✅ Secure password management  
✅ Read-only placement status (admin controlled)

### Admin Features
✅ Comprehensive dashboard with analytics  
✅ Student management (CRUD operations)  
✅ Job posting management  
✅ Assessment creation and assignment  
✅ Application status tracking and updates  
✅ Visual data representation with Chart.js  
✅ Database management interface  
✅ Multi-admin support  
✅ Real-time statistics and metrics

## 📁 Project Structure
```
ProU_v1/
├── backend/
│   ├── routers/          # API route handlers
│   │   ├── students.py
│   │   ├── admins.py
│   │   ├── job_openings.py
│   │   ├── job_optins.py
│   │   ├── assessments.py
│   │   └── student_assessments.py
│   ├── models.py         # Database models
│   ├── schemas.py        # Pydantic schemas
│   ├── db.py            # Database configuration
│   └── main.py          # FastAPI application
├── frontend/
│   ├── index.html       # Unified login page
│   ├── admin.html       # Admin dashboard
│   ├── student.html     # Student dashboard
│   └── config.js        # API configuration
└── README.md
```

## 🔒 Security Notes

⚠️ **Important:** This is an educational project created for assignment purposes. For production use, the following security enhancements would be needed:
- Implement proper password hashing (bcrypt)
- Add JWT authentication with token expiration
- Enable HTTPS
- Add input validation and sanitization
- Implement rate limiting
- Add CORS configuration
- Use environment variables for sensitive data
- Add SQL injection protection
- Implement session management

## � API Endpoints

### Students
- `GET /students/` - Get all students
- `POST /students/` - Create student
- `PUT /students/{id}` - Update student
- `PUT /students/{id}/password` - Update password

### Job Openings
- `GET /job-openings/` - Get all jobs
- `POST /job-openings/` - Create job
- `DELETE /job-openings/{id}` - Delete job

### Job Applications
- `POST /job-optins/opt-in` - Apply for job
- `GET /job-optins/student/{id}` - Get student applications
- `GET /job-optins/job/{id}` - Get job applications
- `PUT /job-optins/{id}/status` - Update application status

### Assessments
- `GET /assessments/` - Get all assessments
- `POST /assessments/` - Create assessment
- `DELETE /assessments/{id}` - Delete assessment

### Student Assessments
- `POST /student-assessments/assign` - Assign assessment
- `GET /student-assessments/students/{id}` - Get student assessments
- `PUT /student-assessments/{id}` - Update assessment
- `DELETE /student-assessments/{id}` - Delete assignment

### Analytics
- `GET /analytics/dashboard` - Get dashboard statistics

## 👨‍💻 Developer

**Jayanth Srinivas**  
GitHub: [JayanthSrinivas06](https://github.com/JayanthSrinivas06)
