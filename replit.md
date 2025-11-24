# MealMap - Smart Restaurant Finder

## Overview
MealMap is a full-stack restaurant discovery platform designed to connect users with dining experiences. It features a Framer-based frontend and a Flask REST API backend. The platform enables users to search for restaurants, view menus, make reservations, save favorites, discover promotions, and receive personalized recommendations. Key capabilities include location-based searching, user account management, and a dedicated dashboard for restaurant owners to manage their listings and operations. The project aims to provide a comprehensive and intuitive solution for both diners and restaurant businesses.

## User Preferences
- **Communication Style**: Clear, concise, and direct.
- **Coding Style**: Adherence to established patterns, with a preference for modular and readable code.
- **Workflow**: Iterative development with a focus on core functionality first.
- **Interaction**: Prioritize core tasks and avoid unnecessary dialogue. Ask for clarification if ambiguity arises.
- **General Working Preferences**:
    - **No changes to `server.py`**: This file contains critical proxy logic for Replit and should not be modified.
    - **No changes to `.replit`**: This file contains Replit-specific configuration and should not be modified.
    - **Security**: Highlight any security implications or shortcuts taken for development purposes, especially regarding authentication.

## System Architecture

### Frontend
- **Framework/Styling**: Static HTML served by a Python HTTP server, utilizing custom CSS with DM Sans & Playfair Display fonts. The design aesthetic is heavily influenced by a Framer template, which is integrated with functional pages.
- **API Client**: Vanilla JavaScript is used for all API communication.
- **Pages**:
    - **Functional**: Restaurants search/browse, Login, Sign Up, Favorites, Promotions, Owner Dashboard, My Reservations, Restaurant Detail. These pages are integrated with the backend API.
    - **Template (Framer Showcase)**: Home, About, Menu, Blog, Contact, Book. These serve as visual templates.
- **UI/UX Decisions**: Redesigned homepage for restaurant discovery, enhanced restaurant listing and detail pages with features like favorite buttons, and an integrated booking section that requires user authentication. Image management includes cuisine-specific stock images.

### Backend
- **Framework**: Flask 3.1.2, serving as a REST API.
- **Database**: MySQL, configured for external hosting (e.g., Railway, AWS RDS).
- **CORS**: Enabled for seamless frontend communication.
- **Modules**: Organized into `models` (database schemas), `routes` (API endpoints for various features like restaurants, users, reservations, menus, favorites, promotions, photos, and recommendations), `utils` (utility functions).
- **Key Features**:
    - **Restaurant Discovery**: Search, filter, and browse.
    - **Location-Based**: Find nearby restaurants.
    - **User Accounts**: Registration, login, profile management.
    - **Reservations**: Table booking.
    - **Favorites**: Save and manage preferred restaurants.
    - **Promotions**: View active deals.
    - **Menu Browsing**: View restaurant menus.
    - **Recommendations**: Personalized suggestions.
    - **Reviews & Ratings**: (MVP with security limitations) Customers can rate and review.
    - **Restaurant Owner Dashboard**: Manage restaurants, reservations, and menus (includes ownership verification).

### Integration Architecture
- **Proxy Server**: `server.py` acts as a proxy, forwarding `/api/*` requests from the frontend (port 5000) to the internal Flask backend (port 8000). This setup addresses CORS issues, works within the Replit environment, and ensures a clean separation of concerns.
- **Dual Server Workflow**: `start.sh` script concurrently runs the Flask backend on port 8000 and the frontend HTTP server on port 5000.

### Environment Configuration
- **Secrets**: Database credentials (`MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE`, `MYSQL_PORT`) are stored as Replit Secrets.

## External Dependencies
- **Database**: MySQL (configured for external hosting like Railway or AWS RDS).
- **Backend Libraries**: Flask, Flask-CORS.
- **Frontend Libraries**: None explicitly listed beyond Vanilla JavaScript and custom CSS, implying self-contained static assets.