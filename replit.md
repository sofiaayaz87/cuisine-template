# MealMap - Smart Restaurant Finder

## Overview
MealMap is a full-stack restaurant discovery platform combining a beautiful Framer-based frontend with a Flask REST API backend. Users can search for restaurants, view menus, make reservations, save favorites, and discover promotions.

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
9. **Reviews & Ratings**: Customers can rate and review restaurants (MVP - see SECURITY_NOTES.md)

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

### Ratings & Reviews
- `POST /ratings/add` - Submit or update a rating/review (⚠️ MVP only - see SECURITY_NOTES.md)
- `GET /ratings/restaurant/<restaurant_id>` - Get all reviews for a restaurant
- `GET /ratings/user/<user_id>/restaurant/<restaurant_id>` - Get user's rating for a restaurant

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

### 2025-11-24: Restaurant Discovery Platform Transformation ✅
- **Homepage Redesigned** - Transformed from single-restaurant website to restaurant discovery platform
  - Hero section: "Discover Your Next Favorite Restaurant"
  - Highlights core features: find nearby restaurants, book tables, save favorites
  - Cuisine exploration: Italian, Chinese, Indian, Japanese categories (vs menu categories)
  - "Why Choose Us" section: Find Nearby, Instant Booking, Save Favorites, Promotions
  
- **Restaurant Listing Page Updates**
  - Title changed: "Our Menu" → "Discover Restaurants"
  - Description updated to reflect restaurant discovery purpose
  - Cuisine filters: Italian, Chinese, Indian, Middle Eastern, BBQ, Korean (vs Breakfast, Main Dishes, etc.)
  - Added cuisine-based stock images to restaurant cards
  - Added favorite heart buttons on each restaurant card with toggle functionality
  - Implemented proper async loading to show saved favorites on page load
  
- **Restaurant Detail Page Enhancements**
  - Added favorite button in hero section with toggle functionality
  - Implemented "Book a Table" section with:
    - Date and time picker
    - Guest count selector (1-9+ guests)
    - Special requests textarea
    - **Authentication required**: Non-logged-in users see login prompt instead of booking form
  - Booking form only visible to authenticated users
  - Successful bookings redirect to "My Reservations" page
  
- **Image Management**
  - Added cuisine-specific stock images mapped to restaurant cuisines
  - Images stored in `/frontend/images/cuisine/` directory
  - Fallback image for restaurants without matching cuisine types

### 2025-11-23: Reviews & Ratings System Added ⚠️
- **Customer Reviews Feature (MVP/Development Only)**
  - Added rating model and database table for customer reviews
  - Created backend endpoints: POST /ratings/add, GET /ratings/restaurant/<id>
  - Built interactive star rating component for 1-5 star selection
  - Created restaurant detail page (restaurant-detail.html) with review submission
  - Display all reviews with user info, ratings, dates on detail page
  - Updated restaurant cards to show average ratings and review counts
  - Restaurant ratings calculate dynamically via SQL aggregation (auto-update)
  - Added XSS protection via HTML entity escaping for review text
  - Fixed database configuration bug (MYSQL_PORT empty string handling)
  
- **⚠️ CRITICAL SECURITY LIMITATION:**
  - Reviews feature uses client-supplied UserID without server authentication
  - Safe for development/testing but NOT production-ready
  - See SECURITY_NOTES.md for full details and production requirements
  - JWT/session authentication REQUIRED before any public deployment

### 2025-11-23: Full-Stack Integration Completed ✅
- Cloned Flask backend from GitHub
- Configured secure environment variables for database
- Installed Flask, CORS, and MySQL dependencies
- Updated backend port to 8000 (avoid conflict with frontend)
- Created JavaScript API client with `/api` proxy routing
- Built proxy server in `server.py` to forward `/api/*` requests to backend
- Built functional pages: restaurants, login, signup, favorites, promotions
- Configured dual-server workflow (frontend + backend)
- Updated Framer template structure to coexist with functional pages
- **Added missing backend endpoints:**
  - `GET /restaurants/search` - Search restaurants by query
  - `GET /restaurants/<id>` - Get restaurant details
  - `GET /promotions/active` - Get all active promotions
  - `GET /recommend/<user_id>` - Get personalized recommendations
  - `GET /users/<id>` - Get user profile
- **Fixed all API endpoint mismatches** between frontend and backend
- **Verified proxy integration** - All API calls successfully route through `/api` proxy

## Integration Architecture

### Proxy Server Design
The frontend uses a proxy server approach to handle API communication in the Replit environment:
1. **Frontend** (port 5000): Serves static files and acts as proxy
2. **Backend** (port 8000): Flask API server (internal only)
3. **API Client**: All requests use `/api` prefix (e.g., `/api/restaurants/search`)
4. **Proxy**: `server.py` forwards `/api/*` requests to `http://127.0.0.1:8000`

This architecture ensures:
- ✅ Browser-compatible API calls (no CORS issues)
- ✅ Works in Replit iframe environment
- ✅ Clean separation of concerns
- ✅ Production-ready structure

## Known Issues & Next Steps

### Current Status
- ✅ Full-stack integration complete and verified
- ✅ All API endpoints properly aligned
- ✅ Proxy server working correctly
- ⏳ Database connection pending (waiting for Railway/AWS RDS setup)
- ⏳ API calls return empty data until database is configured

### To-Do
1. **Configure Railway or AWS RDS MySQL database** (Primary blocker)
2. Test all API endpoints with live data
3. Integrate booking page with reservations API
4. Add restaurant detail pages
5. Implement photo gallery functionality
6. Enhance personalized recommendations with user history
7. Configure deployment settings for production

## Notes
- Backend uses CORS to allow frontend API calls
- API client automatically determines correct backend URL
- Database credentials are securely stored in Replit Secrets
- Frontend cache control is disabled for development
- All new functional pages maintain the Framer template's visual style
