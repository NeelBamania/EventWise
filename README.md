# EventWise – Smart Event Management Platform

EventWise is a microservices-based event management system that allows users to register, track, and receive updates for various events (webinars, workshops, conferences). Organizers can manage events and monitor user engagement with real-time notifications and analytics.

## Project Features
- User registration, authentication, and profiles
- Event creation and discovery
- Event registration and waitlisting
- Email/SMS notifications
- Optional analytics dashboard
- Dockerized services and Kubernetes deployment
- CI/CD integration and observability with Prometheus/Grafana


## Microservices Overview

| Service Name      | Responsibilities                                       | Port  |
|-------------------|--------------------------------------------------------|-------|
| User Service       | Register/login users and manage profiles              | 8001  |
| Event Service      | Create, update, and list events                       | 8002  |
| Registration Service | Register users for events and list attendees         | 8003  |
| Notification Service | Send confirmation and reminder notifications         | 8004  |
| Analytics Service  | (Optional) Provide event engagement statistics        | 8005  |


## Tech Stack

- Backend: Node.js / Python / Express / FastAPI (customize as needed)
- Database: MongoDB / PostgreSQL (per service)
- Containerization: Docker, Docker Compose
- Orchestration: Kubernetes (Minikube)
- CI/CD: GitHub Actions
- Monitoring: Prometheus, Grafana
- Logging: Fluentd or ELK Stack (optional)

## CI/CD Pipeline
Build and test on every push using GitHub Actions

Docker images built and deployed to local Kubernetes

Sample pipeline file: .github/workflows/main.yml


## Team Members
Neel Rami
Neel Bamania
Nirmal Dhaduk
Dikshit Aryal

## Project Timeline
Week	  Milestone
6	      Define use case, APIs, and architecture
7	      Dockerize services and set up Compose
8	      Kubernetes YAMLs and deployment
9	      Implement tests (unit, integration)
10	    Set up CI/CD pipelines
11	    Add monitoring and logging
12	    Final testing and documentation
