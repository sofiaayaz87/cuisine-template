# Smart Restaurant Finder

## Overview
A full-stack restaurant discovery platform combining a beautiful Framer-based frontend with a Flask REST API backend. Users can search for restaurants, view menus, make reservations, save favorites, and discover promotions.

## Project Structure

```
/
├── backend/                   # Flask API Backend
│   ├── models/               # Database models
│   ├── routes/               # API route handlers
│   │   ├── restaurants.py    # Restaurant endpoints
│   │   ├── users.py          # User authentication
│   │   ├── reservations.py   # Booking system
│   │   ├── menu.py           # Menu management
│   │   ├── favorites.py      # User favorites
│   │   ├── promotions.py     # Deals and offers
│   │   ├── photos.py         # Restaurant photos
│   │   └── recommend.py      # AI recommendations
│   ├── utils/                # Utility functions
│   ├── app.py                # Flask application
│   ├── config.py             # Database configuration
│   └── requirements.txt      # Python dependencies
│
├── frontend/                 # Static Frontend
│   ├── js/
│   │   └── api-client.js     # API communication layer
│   ├── index.html            # Original Framer template homepage
│   ├── restaurants.html      # Restaurant search & listing
│   ├── login.html            # User login
│   ├── signup.html           # User registration
│   ├── favorites.html        # Saved restaurants
│   ├── promotions.html       # Active deals
│   ├── about/                # About page (Framer)
│   ├── menu/                 # Menu showcase (Framer)
│   ├── book/                 # Booking page (Framer)
│   ├── contact/              # Contact page (Framer)
│   └── blog/                 # Blog posts (Framer)
│
├── server.py                 # Frontend HTTP server
├── start.sh                  # Startup script for both servers
└── .replit                   # Replit configuration
```

## Technology Stack

### Backend
- **Framework**: Flask 3.1.2
- **Database**: MySQL (configured for external hosting)
- **CORS**: Enabled for frontend communication
- **Port**: 8000 (localhost)

### Frontend
- **Server**: Python HTTP server
- **Styling**: Custom CSS with DM Sans & Playfair Display fonts
- **API Client**: Vanilla JavaScript
- **Port**: 5000 (exposed to public)

### Key Features
1. **Restaurant Discovery**: Search, filter, and browse restaurants
2. **Location-Based**: Find nearby restaurants using geolocation
3. **User Accounts**: Registration, login, and profile management
4. **Reservations**: Book tables at restaurants
5. **Favorites**: Save and manage favorite restaurants
6. **Promotions**: View active deals and discounts
7. **Menu Browsing**: View restaurant menus
8. **Recommendations**: Get personalized restaurant suggestions

## API Endpoints

### Restaurants
- `GET /restaurants/recommend?user_lat=X&user_lon=Y` - Get recommended restaurants
- `GET /restaurants/search?q=query` - Search restaurants
- `GET /restaurants/<id>` - Get restaurant details

### Users
- `POST /users/register` - Create new user account
- `POST /users/login` - User authentication
- `GET /users/<id>` - Get user profile

### Reservations
- `POST /reservations/` - Create reservation
- `GET /reservations/user/<user_id>` - Get user's reservations

### Favorites
- `GET /favorites/<user_id>` - Get user favorites
- `POST /favorites/` - Add to favorites
- `DELETE /favorites/<id>` - Remove favorite

### Promotions
- `GET /promotions/active` - Get active promotions
- `GET /promotions/restaurant/<restaurant_id>` - Restaurant-specific deals

### Menu
- `GET /menu/<restaurant_id>` - Get restaurant menu items

## Environment Configuration

### Required Secrets (Stored in Replit Secrets)
- `MYSQL_HOST` - Database host URL
- `MYSQL_USER` - Database username
- `MYSQL_PASSWORD` - Database password
- `MYSQL_DATABASE` - Database name
- `MYSQL_PORT` - Database port (typically 3306)

**Note**: Database credentials are currently set for InfinityFree hosting but should be updated to Railway or AWS RDS for proper connectivity.

## Development Setup

### Running the Application
Both servers run simultaneously via `start.sh`:
- **Frontend**: http://0.0.0.0:5000 (public-facing)
- **Backend API**: http://127.0.0.1:8000 (internal)

### Workflow
The "Start Web Server" workflow executes `bash start.sh` which:
1. Starts Flask backend on port 8000
2. Starts frontend server on port 5000
3. Runs both processes in parallel

## Database Setup

### Current Status
- MySQL configuration is in place
- Database host needs to be configured (Railway/AWS RDS)
- Schema should match the models in `backend/models/`

### To Configure New Database:
1. Set up MySQL database on Railway or AWS RDS
2. Update the following Replit Secrets:
   - MYSQL_HOST
   - MYSQL_USER
   - MYSQL_PASSWORD
   - MYSQL_DATABASE
   - MYSQL_PORT
3. Backend will automatically connect using environment variables

## Pages

### Functional Pages (API-Integrated)
1. **Restaurants** (`/restaurants.html`) - Search and browse restaurants
2. **Login** (`/login.html`) - User authentication
3. **Sign Up** (`/signup.html`) - New user registration
4. **Favorites** (`/favorites.html`) - Saved restaurants
5. **Promotions** (`/promotions.html`) - Active deals and offers

### Template Pages (Framer Showcase)
1. **Home** (`/`) - Beautiful Framer template homepage
2. **About** (`/about/`) - Restaurant information template
3. **Menu** (`/menu/`) - Menu showcase template
4. **Blog** (`/blog/`) - Blog posts template
5. **Contact** (`/contact/`) - Contact page template
6. **Book** (`/book/`) - Booking page template

## Recent Changes

### 2025-11-23: Full-Stack Integration
- Cloned Flask backend from GitHub
- Configured secure environment variables for database
- Installed Flask, CORS, and MySQL dependencies
- Updated backend port to 8000 (avoid conflict with frontend)
- Created JavaScript API client for frontend-backend communication
- Built functional pages: restaurants, login, signup, favorites, promotions
- Configured dual-server workflow (frontend + backend)
- Updated Framer template structure to coexist with functional pages

## Known Issues & Next Steps

### Current Limitations
- Database connection pending (waiting for Railway/AWS RDS setup)
- API calls work but return empty data without database
- Some Framer template pages need API integration

### To-Do
1. Configure Railway or AWS RDS MySQL database
2. Test all API endpoints with live data
3. Integrate booking page with reservations API
4. Add restaurant detail pages
5. Implement photo gallery functionality
6. Set up user authentication flow
7. Configure deployment settings

## Notes
- Backend uses CORS to allow frontend API calls
- API client automatically determines correct backend URL
- Database credentials are securely stored in Replit Secrets
- Frontend cache control is disabled for development
- All new functional pages maintain the Framer template's visual style
