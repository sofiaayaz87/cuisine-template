/**
 * API Client for Smart Restaurant Finder Backend
 * Handles all communication with the Flask backend
 */

class RestaurantAPI {
    constructor() {
        // Determine the API base URL
        // In development/Replit, both frontend and backend run on same machine
        // Frontend on port 5000, backend on port 8000
        // But browser needs to call backend via proxy
        
        if (typeof window !== 'undefined') {
            // Browser environment - use current origin with port 8000
            const currentOrigin = window.location.origin;
            // Replace port 5000 with 8000 for API calls
            this.apiBase = currentOrigin.replace(/:\d+$/, ':8000');
        } else {
            // Node environment fallback
            this.apiBase = 'http://127.0.0.1:8000';
        }
        
        console.log('API Base URL:', this.apiBase);
    }

    /**
     * Generic fetch wrapper with error handling
     */
    async request(endpoint, options = {}) {
        try {
            const response = await fetch(`${this.apiBase}${endpoint}`, {
                ...options,
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers,
                },
            });

            if (!response.ok) {
                throw new Error(`API Error: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API Request failed:', error);
            throw error;
        }
    }

    // ==================== RESTAURANTS ====================
    
    /**
     * Get recommended restaurants
     * @param {number} userLat - User latitude (optional)
     * @param {number} userLon - User longitude (optional)
     */
    async getRecommendedRestaurants(userLat = null, userLon = null) {
        let endpoint = '/restaurants/recommend';
        if (userLat && userLon) {
            endpoint += `?user_lat=${userLat}&user_lon=${userLon}`;
        }
        return await this.request(endpoint);
    }

    /**
     * Search restaurants
     * @param {string} searchTerm - Search query
     */
    async searchRestaurants(searchTerm) {
        return await this.request(`/restaurants/search?q=${encodeURIComponent(searchTerm)}`);
    }

    /**
     * Get restaurant details by ID
     * @param {number} restaurantId
     */
    async getRestaurantDetails(restaurantId) {
        return await this.request(`/restaurants/${restaurantId}`);
    }

    // ==================== MENU ====================
    
    /**
     * Get menu items for a restaurant
     * @param {number} restaurantId
     */
    async getMenuItems(restaurantId) {
        return await this.request(`/menu/${restaurantId}`);
    }

    // ==================== USERS ====================
    
    /**
     * User login
     * @param {string} email
     * @param {string} password
     */
    async login(email, password) {
        return await this.request('/users/login', {
            method: 'POST',
            body: JSON.stringify({ email, password }),
        });
    }

    /**
     * User registration
     * @param {object} userData - User registration data
     */
    async register(userData) {
        return await this.request('/users/register', {
            method: 'POST',
            body: JSON.stringify(userData),
        });
    }

    /**
     * Get user profile
     * @param {number} userId
     */
    async getUserProfile(userId) {
        return await this.request(`/users/${userId}`);
    }

    // ==================== RESERVATIONS ====================
    
    /**
     * Create a reservation
     * @param {object} reservationData
     */
    async createReservation(reservationData) {
        return await this.request('/reservations/', {
            method: 'POST',
            body: JSON.stringify(reservationData),
        });
    }

    /**
     * Get user reservations
     * @param {number} userId
     */
    async getUserReservations(userId) {
        return await this.request(`/reservations/user/${userId}`);
    }

    // ==================== FAVORITES ====================
    
    /**
     * Get user favorites
     * @param {number} userId
     */
    async getUserFavorites(userId) {
        return await this.request(`/favorites/${userId}`);
    }

    /**
     * Add restaurant to favorites
     * @param {number} userId
     * @param {number} restaurantId
     */
    async addFavorite(userId, restaurantId) {
        return await this.request('/favorites/', {
            method: 'POST',
            body: JSON.stringify({ user_id: userId, restaurant_id: restaurantId }),
        });
    }

    /**
     * Remove restaurant from favorites
     * @param {number} favoriteId
     */
    async removeFavorite(favoriteId) {
        return await this.request(`/favorites/${favoriteId}`, {
            method: 'DELETE',
        });
    }

    // ==================== PROMOTIONS ====================
    
    /**
     * Get active promotions
     */
    async getActivePromotions() {
        return await this.request('/promotions/active');
    }

    /**
     * Get promotions for a specific restaurant
     * @param {number} restaurantId
     */
    async getRestaurantPromotions(restaurantId) {
        return await this.request(`/promotions/restaurant/${restaurantId}`);
    }

    // ==================== PHOTOS ====================
    
    /**
     * Get photos for a restaurant
     * @param {number} restaurantId
     */
    async getRestaurantPhotos(restaurantId) {
        return await this.request(`/photos/restaurant/${restaurantId}`);
    }

    // ==================== RECOMMENDATIONS ====================
    
    /**
     * Get personalized recommendations
     * @param {number} userId
     */
    async getPersonalizedRecommendations(userId) {
        return await this.request(`/recommend/${userId}`);
    }
}

// Create a singleton instance
const api = new RestaurantAPI();

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = api;
}
