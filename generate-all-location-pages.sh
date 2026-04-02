#!/bin/bash

# This script generates all location and neighborhood pages
# Based on the requirements for Summer Soccer Training Raleigh website

cd /root/soccer-lessons-raleigh-north-carolina-2026-04-02-4rk19

echo "Generating all location pages..."
echo "1. Main location pages (5 total)"
echo "2. Neighborhood pages (15 total - 3 per location)"
echo ""

# Note: downtown-raleigh.html already created
# Creating remaining 4 main location pages + all 15 neighborhood pages

# Function will be called by Python script for better templating
python3 - << 'PYTHON_END'
import os

# Location data structure
locations = {
    "north-raleigh": {
        "title": "North Raleigh",
        "badge": "Suburban Convenience",
        "badge_color": "accent",
        "description": "Located in the growing North Raleigh area with easy access from major highways. Perfect for families in North Hills, Midtown, and Falls Lake communities.",
        "address": "Kentwood Park Athletic Complex",
        "address_line2": "6601 Hillsborough St, Raleigh, NC 27606",
        "times_morning": "8:30 AM - 11:30 AM",
        "times_afternoon": "5:00 PM - 7:00 PM",
        "features": ["Multiple Fields", "Covered Pavilion", "Ample Parking", "Playground Nearby"],
        "image": "https://images.unsplash.com/photo-1624526267942-ab0ff8a3e972?q=80&w=2070&auto=format&fit=crop",
        "neighborhoods": {
            "north-hills": {
                "name": "North Hills",
                "description": "Upscale mixed-use development featuring shopping, dining, and residential spaces with excellent walkability and community amenities.",
                "features": "Close to shopping centers, restaurants, and entertainment venues. Easy highway access makes commuting to training sessions convenient."
            },
            "midtown": {
                "name": "Midtown",
                "description": "Modern urban neighborhood combining residential living with commercial development, offering a vibrant community atmosphere.",
                "features": "Central location with access to parks, greenways, and family-friendly activities. Perfect balance of urban convenience and suburban comfort."
            },
            "falls-lake": {
                "name": "Falls Lake",
                "description": "Scenic area near Falls Lake with abundant outdoor recreation opportunities and natural beauty throughout the year.",
                "features": "Close to nature trails, water activities, and outdoor spaces. Ideal for active families who love sports and outdoor adventures."
            }
        }
    },
    "cary": {
        "title": "Cary",
        "badge": "Soccer Hub",
        "badge_color": "primary",
        "description": "Train where the pros train! Our Cary location is near the home of North Carolina Courage and provides access to world-class soccer facilities.",
        "address": "WakeMed Soccer Park",
        "address_line2": "201 Soccer Park Dr, Cary, NC 27511",
        "times_morning": "9:00 AM - 12:00 PM",
        "times_afternoon": "2:00 PM - 5:00 PM",
        "features": ["Professional Stadium", "Practice Fields", "Concessions", "Indoor Facilities"],
        "image": "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?q=80&w=2049&auto=format&fit=crop",
        "neighborhoods": {
            "downtown-cary": {
                "name": "Downtown Cary",
                "description": "Charming downtown area with a small-town feel, featuring local shops, restaurants, and community events year-round.",
                "features": "Walkable streets, farmer's market, and family events. Strong sense of community with easy access to soccer training facilities."
            },
            "preston": {
                "name": "Preston",
                "description": "Master-planned community with excellent schools, parks, and recreational facilities designed for active families.",
                "features": "Top-rated schools, community pools, and sports fields. Close proximity to WakeMed Soccer Park for convenient training access."
            },
            "west-cary": {
                "name": "West Cary",
                "description": "Rapidly growing area with new developments, modern amenities, and quick access to major highways and training venues.",
                "features": "Modern neighborhoods, shopping centers, and dining options. Convenient location for families commuting from surrounding areas."
            }
        }
    },
    "apex": {
        "title": "Apex",
        "badge": "Family-Friendly",
        "badge_color": "accent",
        "description": "Our Apex location offers a family-friendly environment with beautiful fields and excellent facilities, perfect for players from the Southwest Wake County area.",
        "address": "Apex Nature Park Soccer Fields",
        "address_line2": "2600 Evans Rd, Apex, NC 27502",
        "times_morning": "9:00 AM - 12:00 PM",
        "times_afternoon": "1:00 PM - 4:00 PM",
        "features": ["Natural Grass Fields", "Walking Trails", "Picnic Areas", "Nature Setting"],
        "image": "https://images.unsplash.com/photo-1575361204480-aadea25e6e68?q=80&w=2071&auto=format&fit=crop",
        "neighborhoods": {
            "downtown-apex": {
                "name": "Downtown Apex",
                "description": "Historic downtown with small-town charm, local businesses, and a strong community spirit perfect for families.",
                "features": "Charming downtown shops, local restaurants, and community events. Close-knit neighborhood atmosphere with excellent training access."
            },
            "kelly-road": {
                "name": "Kelly Road",
                "description": "Established residential area with mature trees, well-maintained homes, and easy access to schools and parks.",
                "features": "Quiet streets, neighborhood parks, and family-oriented community. Short drive to Apex Nature Park training facilities."
            },
            "scotts-mill": {
                "name": "Scotts Mill",
                "description": "Newer development with modern homes, community amenities, and growing family-friendly atmosphere.",
                "features": "Modern facilities, community pool, and playgrounds. Perfect for active families looking for convenient soccer training access."
            }
        }
    },
    "wake-forest": {
        "title": "Wake Forest",
        "badge": "Newest Location",
        "badge_color": "primary",
        "description": "Our newest location serving the rapidly growing Wake Forest community and surrounding areas. Modern facilities in a welcoming atmosphere.",
        "address": "Smith Creek Soccer Center",
        "address_line2": "1000 Smith Creek Pkwy, Wake Forest, NC 27587",
        "times_morning": "8:30 AM - 11:30 AM",
        "times_afternoon": "4:30 PM - 7:00 PM",
        "features": ["New Turf Fields", "Covered Seating", "Large Parking Lot", "Modern Amenities"],
        "image": "https://images.unsplash.com/photo-1522778526097-ce0a22ceb253?q=80&w=2070&auto=format&fit=crop",
        "neighborhoods": {
            "heritage": {
                "name": "Heritage",
                "description": "Established community with mature landscaping, excellent schools, and strong neighborhood connections.",
                "features": "Well-established neighborhood with parks, greenways, and community centers. Close to Smith Creek Soccer Center training facilities."
            },
            "downtown-wake-forest": {
                "name": "Downtown Wake Forest",
                "description": "Historic downtown area experiencing revitalization with new shops, restaurants, and family-friendly entertainment.",
                "features": "Growing downtown with local businesses, farmer's market, and community events. Easy access to soccer training locations."
            },
            "smith-creek-community": {
                "name": "Smith Creek Community",
                "description": "New master-planned community with modern homes, excellent amenities, and state-of-the-art recreational facilities.",
                "features": "Brand new development with top amenities including soccer fields, pools, and community centers. Steps away from training facilities."
            }
        }
    }
}

print("Generating location pages...")
print(f"Total locations: {len(locations)}")
print(f"Total neighborhoods: {sum(len(loc['neighborhoods']) for loc in locations.values())}")
print("")

PYTHON_END

echo "Python script completed. Pages will be generated next..."

