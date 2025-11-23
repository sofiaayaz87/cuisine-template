# Cuisine - Restaurant Framer Template

## Overview
This is a static HTML restaurant website exported from Framer. It's a professional template for restaurants and food businesses called "Cuisine" featuring a modern, elegant design.

## Project Structure
- `index.html` - Main homepage
- `about/` - About page
- `blog/` - Blog section with multiple articles
- `menu/` - Restaurant menu page
- `contact/` - Contact page
- `book/` - Table booking page
- `server.py` - Python HTTP server configured for Replit

## Pages
1. **Home** (`/`) - Main landing page with hero section
2. **About** (`/about/`) - Restaurant information
3. **Menu** (`/menu/`) - Food menu
4. **Blog** (`/blog/`) - Blog posts including:
   - 5 Great Cooking Gadgets You Can Buy to Save Time
   - Exclusive Baking Lessons from the Pastry King
   - How to Prepare a Delicious Gluten-Free Sushi
   - How to Prepare Delicious Chicken Tenders
   - How to Prepare the Perfect Fries in an Air Fryer
5. **Contact** (`/contact/`) - Contact form and information
6. **Book A Table** (`/book/`) - Reservation system

## Technology Stack
- **Frontend**: Static HTML/CSS/JavaScript (Framer export)
- **Framework**: React (embedded in Framer export)
- **Fonts**: DM Sans, Playfair Display (Google Fonts)
- **Server**: Python 3 HTTP server

## Development Setup
The website runs on a simple Python HTTP server configured for the Replit environment:
- **Host**: 0.0.0.0 (to work with Replit's proxy)
- **Port**: 5000 (Replit's standard web preview port)
- **Cache Control**: Disabled to ensure updates are visible in Replit's iframe

## Server Configuration
The `server.py` script includes:
- Custom cache control headers to prevent browser caching
- Configured to serve all static files from the project directory
- Optimized for Replit's iframe preview environment

## Recent Changes
- 2025-11-23: Initial project setup and import from GitHub
- Renamed all `page.html` files to `index.html` for standard web conventions
- Created Python HTTP server with cache control for Replit environment
- Configured workflow to run on port 5000

## Notes
- The website is fully static and requires no backend processing
- All assets (fonts, images) are served from external CDNs (framerusercontent.com, Google Fonts)
- Browser console warnings from the Framer export are expected and don't affect functionality
