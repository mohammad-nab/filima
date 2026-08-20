# 🎬 Movie Streaming Platform

A **backend REST API for a modern movie streaming platform**, built with **Django** and **Django REST Framework**.

The project provides the core backend infrastructure required for a streaming service, including movie and content management, user authentication, subscriptions, media management, categorization, and a foundation for scalable video streaming.

---

## 📌 Overview

This project is a backend implementation of a movie streaming service inspired by platforms such as Netflix and other modern OTT services.

The main goal of the project is to build a **clean, scalable, and production-oriented REST API** while applying real-world backend development concepts.

The platform is designed around several main areas:

* 👤 User & customer management
* 🔐 Authentication & authorization
* 🎬 Movie/content management
* 🏷️ Content categorization and tagging
* 🖼️ Image and media management
* 💳 Subscription management
* 🔎 Content discovery
* 🛡️ Role-based permissions
* 📡 RESTful API architecture

---

## ✨ Features

### 🔐 Authentication & Authorization

The API provides secure authentication and authorization mechanisms.

Features include:

* JWT-based authentication
* Access and refresh tokens
* Token expiration
* Refresh-token based authentication
* Logout and token invalidation
* Protected API endpoints
* Permission-based access control
* Admin-only management endpoints

Authentication is designed to keep access tokens short-lived while allowing users to maintain their authenticated session through refresh tokens.

---

### 👤 User & Customer Management

The platform supports user/customer management for the streaming service.

Users can:

* Create an account
* Authenticate securely
* Access protected resources
* Manage their account
* Access subscription-related functionality
* Interact with content according to their permissions

Different levels of access can be enforced through Django REST Framework permissions.

---

### 🎬 Movie & Content Management

The core of the platform is the content management system.

Movies and other content can contain information such as:

* English title
* Persian title
* Description
* Release information
* Content metadata
* Categories
* Tags
* Images
* Streaming-related information

The API is designed so that content can be extended with additional metadata without requiring major changes to the overall architecture.

---

### 🏷️ Tags & Categorization

Content can be organized using reusable tags and categories.

For example:

```text
Action
Drama
Comedy
Horror
Sci-Fi
Thriller
Animation
```

A movie can have multiple tags, allowing users to discover content through different categories.

The project uses Django's relationship system to efficiently manage many-to-many relationships between content and tags.

---

### 🖼️ Image Management

The platform includes a dedicated image management system.

Images are stored separately from the main content model, allowing a movie to have multiple images.

Possible image types include:

* Poster
* Backdrop
* Thumbnail
* Banner
* Other content-specific images

Each image can contain metadata such as:

* UUID
* Image type
* Related content
* Creation timestamp
* Last update timestamp
* Creator
* Last updater
* Soft-delete status

This separation makes the media system easier to extend and maintain.

---

### 💳 Subscription System

The project includes a subscription architecture for controlling access to premium content.

Subscriptions can be used to represent different plans and access levels.

For example:

```text
Free
Basic
Standard
Premium
```

The subscription system can be extended to support:

* Different subscription plans
* Subscription duration
* Start/end dates
* Active/inactive subscriptions
* Premium content
* Subscription-based access control

This provides the foundation for implementing a real-world paid streaming service.

---

## 🗑️ Soft Delete

The project uses soft deletion for certain resources.

Instead of immediately removing an object from the database, a deletion flag can be used:

```python
is_deleted = models.BooleanField(default=False)
```

This provides several advantages:

* Prevents accidental permanent deletion
* Allows historical data to remain available
* Makes recovery possible
* Helps maintain relationships and audit information

---

## 🕒 Auditing

Important resources can contain information about when and by whom they were created or modified.

Typical audit fields include:

```text
created_at
updated_at
created_by
updated_by
```

This makes it easier to track changes made to content and other administrative resources.

---

## 🏗️ Project Architecture

The project follows a modular Django architecture.

A simplified structure:

```text
movie-stream/
│
├── apps/
│   ├── authentication/
│   ├── customers/
│   ├── content/
│   ├── tags/
│   ├── images/
│   ├── subscriptions/

│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── media/
│
├── requirements.txt
├── manage.py
└── README.md
```

> The exact application structure may differ depending on the current implementation.

---

## 🛠️ Tech Stack

| Technology               | Purpose                             |
| ------------------------ | ----------------------------------- |
| 🐍 Python                | Backend programming language        |
| 🟢 Django                | Web framework                       |
| 🔵 Django REST Framework | REST API development                |
| 🔐 JWT                   | Authentication                      |
| 🗄️ PostgreSQL           | Relational database                 |
| 🐳 Docker                | Containerization                    |
| 🔴 Redis                 | Caching / background infrastructure |


---

## 🔑 Authentication Flow

The authentication system uses access and refresh tokens.

```text
                 Login
                   │
                   ▼
          ┌─────────────────┐
          │  Django API     │
          └────────┬────────┘
                   │
             Access Token
             Refresh Token
                   │
                   ▼
               Client
                   │
                   │
        ┌──────────┴──────────┐
        │                     │
 Access Token valid      Access Token expired
        │                     │
        ▼                     ▼
    API Request          Refresh Token
                              │
                              ▼
                       New Access Token
```

The access token is intentionally short-lived, while the refresh token allows the client to obtain a new access token without requiring the user to log in again.

---

## 🔒 Permissions

Different resources require different levels of access.

For example:

| Resource             |   User  | Admin |
| -------------------- | :-----: | :---: |
| View content         |    ✅    |   ✅   |
| View images          |    ✅    |   ✅   |
| Create content       |    ❌    |   ✅   |
| Update content       |    ❌    |   ✅   |
| Delete content       |    ❌    |   ✅   |
| Manage subscriptions | Limited |   ✅   |
| Manage users         |    ❌    |   ✅   |

The exact permission rules can evolve as the project grows.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohammad-nab/filima.git

```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DEBUG=True

SECRET_KEY=your-secret-key

DATABASE_NAME=movie_stream
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

> Never commit your `.env` file or production secrets to GitHub.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will then be available at:

```text
http://127.0.0.1:8000/
```

---


Tests should cover important parts of the application, including:

* Authentication
* Permissions
* Content creation
* Content updates
* Content deletion
* Relationships
* Subscriptions
* API validation

---

## 🚀 Future Improvements

The project is designed to evolve into a more complete streaming platform.

Planned improvements include:

* [ ] HLS video processing pipeline
* [ ] CDN integration
* [ ] Adaptive bitrate streaming
* [ ] Watch history
* [ ] Continue watching
* [ ] User favorites
* [ ] Movie ratings
* [ ] Movie reviews
* [ ] Search
* [ ] Advanced filtering
* [ ] Recommendation system
* [ ] Subscription payment integration
* [ ] Subscription expiration handling
* [ ] Email notifications
* [ ] Redis caching
* [ ] Background tasks with Celery
* [ ] API documentation
* [ ] Docker production setup
* [ ] Automated testing
* [ ] CI/CD pipeline
* [ ] Monitoring and logging

---

## 🎯 Project Goals

The main purpose of this project is not simply to create a CRUD API.

It is intended to demonstrate how a **real-world backend service** can be designed and developed.

The project focuses on:

* Clean API design
* Database relationships
* Authentication and authorization
* Scalable architecture
* Media management
* Subscription-based access
* REST API development
* Performance optimization
* Production-oriented backend practices

---

## 📚 What This Project Demonstrates

By working on this project, the following backend concepts are covered:

```text
Django
   │
   ├── Models
   ├── Relationships
   ├── Migrations
   └── Admin
        │
        ▼
Django REST Framework
   │
   ├── Serializers
   ├── ViewSets
   ├── Routers
   ├── Permissions
   └── API Validation
        │
        ▼
Authentication
   │
   ├── JWT
   ├── Access Tokens
   ├── Refresh Tokens
   └── Token Revocation
        │
        ▼
Business Logic
   │
   ├── Content
   ├── Tags
   ├── Images
   └── Subscriptions
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you want to contribute:

```bash
git checkout -b feature/my-feature

git add .

git commit -m "Add my feature"

git push origin feature/my-feature
```

Then open a pull request.

---

### ⭐ If you find this project interesting

Feel free to ⭐ the repository and explore the source code.
