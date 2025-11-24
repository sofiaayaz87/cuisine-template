-- Migration: Add OwnerID column to restaurant table
-- This migration adds the owner_id foreign key relationship between Restaurant and UserAccount tables
-- Execute this SQL on your MySQL database before using owner features

-- Add OwnerID column to restaurant table (nullable to allow existing restaurants)
ALTER TABLE restaurant 
ADD COLUMN OwnerID INT NULL;

-- Add foreign key constraint linking to UserAccount
ALTER TABLE restaurant 
ADD CONSTRAINT fk_restaurant_owner 
FOREIGN KEY (OwnerID) REFERENCES useraccount(Id) ON DELETE SET NULL;

-- Optional: Create index for faster owner lookups
CREATE INDEX idx_restaurant_owner ON restaurant(OwnerID);

-- Note: Existing restaurants will have OwnerID = NULL
-- You can update existing restaurants to assign owners:
-- UPDATE restaurant SET OwnerID = <user_id> WHERE RestaurantID = <restaurant_id>;
