import sys
import os
from config import db
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Rating:
    """Model for restaurant ratings and reviews"""
    
    @staticmethod
    def add_rating(user_id, restaurant_id, rating_score, review_text=None):
        """
        Add a new rating/review for a restaurant
        Returns: (success: bool, message: str)
        """
        cursor = db.cursor(buffered=True)
        try:
            # Verify user exists
            cursor.execute("SELECT Id FROM useraccount WHERE Id=%s", (user_id,))
            if not cursor.fetchone():
                cursor.close()
                return False, "User not found"
            
            # Verify restaurant exists
            cursor.execute("SELECT RestaurantID FROM restaurant WHERE RestaurantID=%s", (restaurant_id,))
            if not cursor.fetchone():
                cursor.close()
                return False, "Restaurant not found"
            
            # Sanitize review text
            if review_text:
                review_text = review_text.strip()[:1000]
            
            # Check if user already rated this restaurant
            cursor.execute(
                "SELECT RatingID FROM rating WHERE UserID=%s AND RestaurantID=%s",
                (user_id, restaurant_id)
            )
            existing = cursor.fetchone()
            
            if existing:
                # Update existing rating
                cursor.execute(
                    "UPDATE rating SET RatingScore=%s, Review=%s, CreatedAt=%s WHERE RatingID=%s",
                    (rating_score, review_text, datetime.now(), existing[0])
                )
            else:
                # Insert new rating
                cursor.execute(
                    "INSERT INTO rating (UserID, RestaurantID, RatingScore, Review, CreatedAt) VALUES (%s, %s, %s, %s, %s)",
                    (user_id, restaurant_id, rating_score, review_text, datetime.now())
                )
            
            db.commit()
            cursor.close()
            return True, "Rating added successfully"
                
        except Exception as e:
            db.rollback()
            cursor.close()
            print("Error adding rating:", e)
            return False, str(e)
    
    @staticmethod
    def get_restaurant_ratings(restaurant_id):
        """
        Get all ratings/reviews for a restaurant
        Returns: list of rating dictionaries with user info
        """
        cursor = db.cursor(buffered=True)
        try:
            sql = """
                SELECT 
                    r.RatingID,
                    r.UserID,
                    r.RatingScore,
                    r.Review,
                    r.CreatedAt,
                    u.FirstName,
                    u.LastName,
                    u.Email
                FROM rating r
                LEFT JOIN useraccount u ON r.UserID = u.Id
                WHERE r.RestaurantID = %s
                ORDER BY r.CreatedAt DESC
            """
            cursor.execute(sql, (restaurant_id,))
            rows = cursor.fetchall()
            cursor.close()
            
            ratings = []
            for row in rows:
                rating_id, user_id, score, review, created_at, first_name, last_name, email = row
                
                # Sanitize review text for safe HTML display
                sanitized_review = review.replace('<', '&lt;').replace('>', '&gt;') if review else review
                
                ratings.append({
                    "RatingID": rating_id,
                    "UserID": user_id,
                    "RatingScore": score,
                    "Review": sanitized_review,
                    "CreatedAt": created_at.isoformat() if created_at else None,
                    "UserFirstName": first_name,
                    "UserLastName": last_name,
                    "UserEmail": email
                })
            
            return ratings
            
        except Exception as e:
            cursor.close()
            print("Error getting ratings:", e)
            return []
    
    @staticmethod
    def get_user_rating(user_id, restaurant_id):
        """
        Get a specific user's rating for a restaurant
        Returns: rating dict or None
        """
        cursor = db.cursor(buffered=True)
        try:
            cursor.execute(
                "SELECT RatingID, RatingScore, Review, CreatedAt FROM rating WHERE UserID=%s AND RestaurantID=%s",
                (user_id, restaurant_id)
            )
            row = cursor.fetchone()
            cursor.close()
            
            if row:
                return {
                    "RatingID": row[0],
                    "RatingScore": row[1],
                    "Review": row[2],
                    "CreatedAt": row[3].isoformat() if row[3] else None
                }
            return None
            
        except Exception as e:
            cursor.close()
            print("Error getting user rating:", e)
            return None
