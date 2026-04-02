#!/usr/bin/env python3
"""
Generate all location and neighborhood pages for Summer Soccer Training Raleigh
"""

import os

# Location data
locations = {
    "north-raleigh": {
        "title": "North Raleigh",
        "badge": "Suburban Convenience",
        "badge_color": "accent",
        "description": "Located in the growing North Raleigh area with easy access from major highways. Perfect for families in North Hills, Midtown, and Falls Lake communities.",
        "facility": "Kentwood Park Athletic Complex",
        "address": "6601 Hillsborough St, Raleigh, NC 27606",
        "times": {
            "morning": "8:30 AM - 11:30 AM",
            "evening": "5:00 PM - 7:00 PM"
        },
        "features": ["Multiple Fields", "Covered Pavilion", "Ample Parking", "Playground Nearby"],
        "image": "https://images.unsplash.com/photo-1624526267942-ab0ff8a3e972?q=80&w=2070&auto=format&fit=crop",
        "neighborhoods": {
            "north-hills": {
                "title": "North Hills",
                "description": "Upscale mixed-use community with shopping, dining, and entertainment just minutes from premier soccer training facilities.",
                "highlights": ["Walkable community", "Shopping & dining nearby", "Easy highway access", "Family-friendly"]
            },
            "midtown": {
                "title": "Midtown",
                "description": "Vibrant urban neighborhood offering convenient access to North Raleigh training with modern amenities and community parks.",
                "highlights": ["Central location", "Modern facilities", "Community parks", "Quick commute"]
            },
            "falls-lake": {
                "title": "Falls Lake",
                "description": "Scenic lakeside community providing a perfect balance of nature and convenience for active families and young athletes.",
                "highlights": ["Lakeside setting", "Nature trails", "Outdoor recreation", "Quiet neighborhoods"]
            }
        }
    },
    "cary": {
        "title": "Cary",
        "badge": "Professional Facilities",
        "badge_color": "primary",
        "description": "Train where the pros train! Our Cary location near the home of North Carolina Courage provides access to world-class soccer facilities.",
        "facility": "WakeMed Soccer Park",
        "address": "201 Soccer Park Dr, Cary, NC 27511",
        "times": {
            "morning": "9:00 AM - 12:00 PM",
            "afternoon": "2:00 PM - 5:00 PM"
        },
        "features": ["Professional Stadium", "Practice Fields", "Concessions", "Indoor Facilities"],
        "image": "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?q=80&w=2049&auto=format&fit=crop",
        "neighborhoods": {
            "downtown-cary": {
                "title": "Downtown Cary",
                "description": "Historic downtown charm meets modern convenience with excellent access to top-tier soccer training and family amenities.",
                "highlights": ["Historic district", "Local shops", "Community events", "Walkable streets"]
            },
            "preston": {
                "title": "Preston",
                "description": "Master-planned community offering resort-style amenities and close proximity to professional soccer facilities and training.",
                "highlights": ["Resort amenities", "Golf courses", "Community pools", "Walking trails"]
            },
            "west-cary": {
                "title": "West Cary",
                "description": "Growing suburban area with excellent schools and easy access to WakeMed Soccer Park for elite youth training programs.",
                "highlights": ["Top-rated schools", "New development", "Parks & recreation", "Family-oriented"]
            }
        }
    },
    "apex": {
        "title": "Apex",
        "badge": "Family-Friendly",
        "badge_color": "accent",
        "description": "Our Apex location offers a family-friendly environment with beautiful fields and excellent facilities, perfect for players from Southwest Wake County.",
        "facility": "Apex Nature Park Soccer Fields",
        "address": "2600 Evans Rd, Apex, NC 27502",
        "times": {
            "morning": "9:00 AM - 12:00 PM",
            "afternoon": "1:00 PM - 4:00 PM"
        },
        "features": ["Natural Grass Fields", "Walking Trails", "Picnic Areas", "Nature Setting"],
        "image": "https://images.unsplash.com/photo-1575361204480-aadea25e6e68?q=80&w=2071&auto=format&fit=crop",
        "neighborhoods": {
            "downtown-apex": {
                "title": "Downtown Apex",
                "description": "Charming small-town atmosphere with strong community spirit and convenient access to quality youth soccer training programs.",
                "highlights": ["Small-town charm", "Local businesses", "Community festivals", "Safe neighborhoods"]
            },
            "kelly-road": {
                "title": "Kelly Road",
                "description": "Established residential area near Apex Nature Park, offering families easy access to outdoor recreation and soccer training.",
                "highlights": ["Established homes", "Near nature park", "Quiet streets", "Community feel"]
            },
            "scotts-mill": {
                "title": "Scotts Mill",
                "description": "Family-focused neighborhood with excellent schools and quick access to Apex soccer training facilities and nature trails.",
                "highlights": ["Top schools", "Community pools", "Neighborhood events", "Family activities"]
            }
        }
    },
    "wake-forest": {
        "title": "Wake Forest",
        "badge": "Newest Location",
        "badge_color": "primary",
        "description": "Our newest location serving the rapidly growing Wake Forest community with modern facilities in a welcoming atmosphere.",
        "facility": "Smith Creek Soccer Center",
        "address": "1000 Smith Creek Pkwy, Wake Forest, NC 27587",
        "times": {
            "morning": "8:30 AM - 11:30 AM",
            "evening": "4:30 PM - 7:00 PM"
        },
        "features": ["New Turf Fields", "Covered Seating", "Large Parking Lot", "Modern Amenities"],
        "image": "https://images.unsplash.com/photo-1522778526097-ce0a22ceb253?q=80&w=2070&auto=format&fit=crop",
        "neighborhoods": {
            "heritage": {
                "title": "Heritage",
                "description": "Master-planned community combining traditional neighborhood design with modern amenities and easy access to soccer training.",
                "highlights": ["Planned community", "Community center", "Pools & parks", "Events & activities"]
            },
            "downtown-wake-forest": {
                "title": "Downtown Wake Forest",
                "description": "Historic downtown area with local charm, shops, and restaurants, minutes from Smith Creek Soccer Center training facilities.",
                "highlights": ["Historic downtown", "Local dining", "Community events", "Small-town feel"]
            },
            "smith-creek-community": {
                "title": "Smith Creek",
                "description": "Modern residential development surrounding the Smith Creek Soccer Center, offering the ultimate convenience for training families.",
                "highlights": ["New homes", "Adjacent to facility", "Walking distance", "Modern amenities"]
            }
        }
    }
}


def generate_location_page(location_key, location_data):
    """Generate main location page HTML"""

    # Generate neighborhoods HTML
    neighborhoods_html = ""
    for idx, (neigh_key, neigh_data) in enumerate(location_data["neighborhoods"].items(), 1):
        neighborhoods_html += f'''
                <div class="card-hover bg-white border border-gray-200 rounded-lg p-8 shadow-md">
                    <div class="text-4xl mb-4 text-primary"><i class="fas fa-map-marked-alt"></i></div>
                    <h3 class="text-xl font-bold text-secondary mb-3">{neigh_data["title"]}</h3>
                    <p class="text-gray-600 mb-4">{neigh_data["description"]}</p>
                    <a href="{location_key}/{neigh_key}.html" class="text-primary hover:underline font-semibold">
                        Explore {neigh_data["title"]} →
                    </a>
                </div>
'''

    # Generate features HTML
    features_html = ""
    for feature in location_data["features"]:
        color = "primary" if location_data["badge_color"] == "primary" else "accent"
        features_html += f'<span class="location-badge bg-{color}/10 text-{color}">{feature}</span>\n                                    '

    # Time display
    time_html = ""
    if "evening" in location_data["times"]:
        time_html = f'Morning: {location_data["times"]["morning"]}<br>Evening: {location_data["times"]["evening"]}'
    elif "afternoon" in location_data["times"]:
        time_html = f'Morning: {location_data["times"]["morning"]}<br>Afternoon: {location_data["times"]["afternoon"]}'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Summer soccer training in {location_data["title"]} - Programs for all ages and skill levels. Expert coaching at {location_data["facility"]}.">
    <title>{location_data["title"]} Soccer Training | Summer Soccer Training Raleigh NC</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300,400,500,600,700&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Poppins', sans-serif; }}
        html {{ scroll-behavior: smooth; }}
        .text-primary {{ color: #FF5A5F; }}
        .bg-primary {{ background-color: #FF5A5F; }}
        .border-primary {{ border-color: #FF5A5F; }}
        .text-secondary {{ color: #1A1A1A; }}
        .bg-secondary {{ background-color: #1A1A1A; }}
        .text-accent {{ color: #FFD166; }}
        .bg-accent {{ background-color: #FFD166; }}
        .btn-solid {{
            background-color: #FF5A5F;
            color: white;
            padding: 12px 24px;
            border-radius: 4px;
            font-weight: 600;
            transition: all 0.3s ease-in-out;
            cursor: pointer;
            display: inline-block;
            border: 2px solid #FF5A5F;
        }}
        .btn-solid:hover {{
            background-color: white;
            color: #FF5A5F;
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(255, 90, 95, 0.3);
        }}
        .btn-outline {{
            background-color: transparent;
            border: 2px solid #FF5A5F;
            color: #FF5A5F;
            padding: 12px 24px;
            border-radius: 4px;
            font-weight: 600;
            transition: all 0.3s ease-in-out;
            display: inline-block;
        }}
        .btn-outline:hover {{
            background-color: #FF5A5F;
            color: white;
            transform: scale(1.05);
        }}
        .card-hover {{
            transition: all 0.3s ease-in-out;
        }}
        .card-hover:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        }}
        .dropdown-menu {{
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 0.5rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
            min-width: 240px;
            z-index: 1000;
            margin-top: 0.5rem;
        }}
        .dropdown-menu.active {{ display: block; }}
        .dropdown-item {{
            display: block;
            padding: 12px 20px;
            color: #374151;
            text-decoration: none;
            transition: all 300ms ease-out;
            border-bottom: 1px solid #e5e7eb;
            font-size: 15px;
        }}
        .dropdown-item:last-child {{ border-bottom: none; }}
        .dropdown-item:hover {{
            background-color: #fef2f2;
            color: #FF5A5F;
            padding-left: 24px;
        }}
        .btn-primary {{
            background-color: #FF5A5F;
            color: white;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s ease-in-out;
            display: inline-block;
            text-decoration: none;
            border: 2px solid #FF5A5F;
        }}
        .btn-primary:hover {{
            background-color: #e54950;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(255, 90, 95, 0.4);
        }}
        .location-badge {{
            display: inline-block;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 8px;
        }}
        nav button {{
            background: none;
            border: none;
            cursor: pointer;
        }}
    </style>
</head>
<body class="bg-white text-secondary">
    <!-- Header -->
    <header class="sticky top-0 z-50 bg-white shadow-md">
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-3">
                <i class="fas fa-futbol text-3xl text-primary"></i>
                <span class="text-xl font-bold text-secondary">Summer Soccer Training Raleigh</span>
            </a>

            <div class="hidden lg:flex items-center gap-8">
                <a href="index.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Home</a>

                <div class="relative services-link">
                    <button type="button" class="services-dropdown-btn text-gray-700 hover:text-primary transition-colors font-medium flex items-center gap-1">
                        Programs <i class="fas fa-chevron-down text-xs"></i>
                    </button>
                    <div class="dropdown-menu services-dropdown">
                        <a href="programs.html#summer-camps" class="dropdown-item">Summer Camps</a>
                        <a href="programs.html#skills-training" class="dropdown-item">Skills Training</a>
                        <a href="programs.html#private-lessons" class="dropdown-item">Private Lessons</a>
                    </div>
                </div>

                <div class="relative service-areas-link">
                    <button type="button" class="areas-dropdown-btn text-gray-700 hover:text-primary transition-colors font-medium flex items-center gap-1">
                        Locations <i class="fas fa-chevron-down text-xs"></i>
                    </button>
                    <div class="dropdown-menu areas-dropdown">
                        <a href="downtown-raleigh.html" class="dropdown-item">Downtown Raleigh</a>
                        <a href="north-raleigh.html" class="dropdown-item">North Raleigh</a>
                        <a href="cary.html" class="dropdown-item">Cary</a>
                        <a href="apex.html" class="dropdown-item">Apex</a>
                        <a href="wake-forest.html" class="dropdown-item">Wake Forest</a>
                    </div>
                </div>

                <a href="index.html#about" class="text-gray-700 hover:text-primary transition-colors font-medium">About</a>
                <a href="index.html#testimonials" class="text-gray-700 hover:text-primary transition-colors font-medium">Testimonials</a>
                <a href="index.html#contact" class="btn-primary">Register Now</a>
            </div>

            <button type="button" class="lg:hidden text-gray-700" id="mobile-menu-btn">
                <i class="fas fa-bars text-2xl"></i>
            </button>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="py-16 md:py-20 bg-gradient-to-br from-gray-50 to-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-8">
                <div class="inline-block bg-{location_data["badge_color"]}/10 text-{location_data["badge_color"]} px-4 py-2 rounded-full text-sm font-semibold mb-4">
                    <i class="fas fa-map-marker-alt mr-2"></i>{location_data["badge"]}
                </div>
                <h1 class="text-4xl md:text-5xl font-bold text-secondary mb-4">
                    {location_data["title"]} <span class="text-primary">Soccer Training</span>
                </h1>
                <p class="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
                    {location_data["description"]}
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mt-12">
                <div>
                    <h2 class="text-2xl font-bold text-secondary mb-6">Training Location</h2>
                    <div class="space-y-4">
                        <div class="flex items-start gap-3">
                            <i class="fas fa-location-dot text-primary mt-1"></i>
                            <div>
                                <h4 class="font-semibold text-secondary">Facility</h4>
                                <p class="text-gray-600">{location_data["facility"]}<br>{location_data["address"]}</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3">
                            <i class="fas fa-clock text-primary mt-1"></i>
                            <div>
                                <h4 class="font-semibold text-secondary">Training Times</h4>
                                <p class="text-gray-600">{time_html}</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3">
                            <i class="fas fa-star text-primary mt-1"></i>
                            <div>
                                <h4 class="font-semibold text-secondary">Features</h4>
                                <div class="flex flex-wrap gap-2 mt-2">
                                    {features_html}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="mt-8">
                        <a href="index.html#contact" class="btn-solid">Register at This Location</a>
                    </div>
                </div>
                <div class="relative">
                    <img src="{location_data["image"]}"
                         alt="{location_data["title"]} Soccer Training"
                         class="rounded-2xl shadow-2xl w-full h-[400px] object-cover">
                </div>
            </div>
        </div>
    </section>

    <!-- Programs Available Section -->
    <section class="py-16 md:py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-secondary mb-4">
                    Programs Available in {location_data["title"]}
                </h2>
                <p class="text-lg text-gray-600 max-w-2xl mx-auto">
                    All our comprehensive training programs are available at this location
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Summer Camps -->
                <div class="card-hover bg-gradient-to-br from-gray-50 to-white border border-gray-200 rounded-lg p-8 shadow-md">
                    <div class="text-4xl mb-4 text-primary"><i class="fas fa-campground"></i></div>
                    <h3 class="text-2xl font-bold text-secondary mb-4">Summer Camps</h3>
                    <p class="text-gray-600 mb-6">
                        Week-long intensive training camps designed to transform players in just five days. Ages 6-17 with skill-based grouping.
                    </p>
                    <ul class="space-y-2 mb-6 text-sm text-gray-600">
                        <li><i class="fas fa-check text-primary mr-2"></i>Monday - Friday format</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>Half-day or full-day options</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>4:1 player-to-coach ratio</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>All skill levels welcome</li>
                    </ul>
                    <a href="programs.html#summer-camps" class="btn-outline w-full text-center">Learn More</a>
                </div>

                <!-- Skills Training -->
                <div class="card-hover bg-gradient-to-br from-gray-50 to-white border border-gray-200 rounded-lg p-8 shadow-md">
                    <div class="text-4xl mb-4 text-primary"><i class="fas fa-dumbbell"></i></div>
                    <h3 class="text-2xl font-bold text-secondary mb-4">Skills Training</h3>
                    <p class="text-gray-600 mb-6">
                        8-week progressive curriculum focusing on technical skills, tactical awareness, and position-specific development.
                    </p>
                    <ul class="space-y-2 mb-6 text-sm text-gray-600">
                        <li><i class="fas fa-check text-primary mr-2"></i>Tuesday/Thursday or Saturday</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>Progressive 8-week program</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>Position-specific training</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>Game situation practice</li>
                    </ul>
                    <a href="programs.html#skills-training" class="btn-outline w-full text-center">Learn More</a>
                </div>

                <!-- Private Lessons -->
                <div class="card-hover bg-gradient-to-br from-gray-50 to-white border border-gray-200 rounded-lg p-8 shadow-md">
                    <div class="text-4xl mb-4 text-primary"><i class="fas fa-user-graduate"></i></div>
                    <h3 class="text-2xl font-bold text-secondary mb-4">Private Lessons</h3>
                    <p class="text-gray-600 mb-6">
                        Personalized 1-on-1 coaching tailored to your specific goals and areas for improvement with video analysis.
                    </p>
                    <ul class="space-y-2 mb-6 text-sm text-gray-600">
                        <li><i class="fas fa-check text-primary mr-2"></i>100% customized training</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>Flexible scheduling</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>Professional video analysis</li>
                        <li><i class="fas fa-check text-primary mr-2"></i>Multiple package options</li>
                    </ul>
                    <a href="programs.html#private-lessons" class="btn-outline w-full text-center">Learn More</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Neighborhoods Section -->
    <section class="py-16 md:py-20 bg-gradient-to-r from-gray-50 to-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-secondary mb-4">
                    Neighborhoods We Serve
                </h2>
                <p class="text-lg text-gray-600 max-w-2xl mx-auto">
                    Convenient training for families throughout the {location_data["title"]} area
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                {neighborhoods_html}
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-16 md:py-20 bg-gradient-to-r from-primary to-accent text-white">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl md:text-4xl font-bold mb-6">Ready to Join Us in {location_data["title"]}?</h2>
            <p class="text-lg md:text-xl mb-8 opacity-90">
                Register today and start your journey to soccer excellence!
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="index.html#contact" class="bg-white text-primary hover:bg-gray-100 px-8 py-4 rounded-lg font-semibold text-lg transition-all shadow-lg">
                    Register Now
                </a>
                <a href="programs.html" class="bg-transparent border-2 border-white hover:bg-white hover:text-primary px-8 py-4 rounded-lg font-semibold text-lg transition-all">
                    View All Programs
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-secondary text-white py-12 md:py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-8">
                <div>
                    <div class="flex items-center space-x-2 mb-4">
                        <div class="w-10 h-10 bg-primary rounded-lg flex items-center justify-center">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                            </svg>
                        </div>
                        <span class="font-semibold text-lg">Summer Soccer Raleigh</span>
                    </div>
                    <p class="text-gray-300 font-light text-sm leading-relaxed">
                        Elite youth soccer training and summer camps in Raleigh, NC. Developing confident, skilled players since day one.
                    </p>
                </div>
                <div>
                    <h3 class="font-semibold text-lg mb-4">Quick Links</h3>
                    <ul class="space-y-3">
                        <li><a href="programs.html" class="text-gray-300 hover:text-primary transition-colors duration-300 font-light">Programs</a></li>
                        <li><a href="locations.html" class="text-gray-300 hover:text-primary transition-colors duration-300 font-light">Locations</a></li>
                        <li><a href="index.html#contact" class="text-gray-300 hover:text-primary transition-colors duration-300 font-light">Register</a></li>
                        <li><a href="index.html#testimonials" class="text-gray-300 hover:text-primary transition-colors duration-300 font-light">Testimonials</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-semibold text-lg mb-4">Legal</h3>
                    <ul class="space-y-3">
                        <li><a href="#" class="text-gray-300 hover:text-primary transition-colors duration-300 font-light">Privacy Policy</a></li>
                        <li><a href="#" class="text-gray-300 hover:text-primary transition-colors duration-300 font-light">Terms of Service</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-semibold text-lg mb-4">Contact Info</h3>
                    <div class="space-y-3">
                        <p class="text-gray-300 font-light text-sm">
                            <span class="block">Serving Raleigh & Triangle Area</span>
                            <span class="block">Raleigh, NC 27601</span>
                        </p>
                        <p class="text-gray-300 font-light text-sm">
                            <a href="mailto:info@summersoccerraleigh.com" class="hover:text-primary transition-colors duration-300">info@summersoccerraleigh.com</a>
                        </p>
                    </div>
                </div>
            </div>
            <div class="border-t border-gray-700 pt-8">
                <div class="flex flex-col md:flex-row items-center justify-between">
                    <p class="text-gray-400 font-light text-sm mb-4 md:mb-0">
                        &copy; 2026 Summer Soccer Training Raleigh. All rights reserved.
                    </p>
                    <div class="flex space-x-6">
                        <a href="#" class="text-gray-400 hover:text-primary transition-colors duration-300" aria-label="Facebook">
                            <i class="fab fa-facebook-f"></i>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-primary transition-colors duration-300" aria-label="Twitter">
                            <i class="fab fa-twitter"></i>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-primary transition-colors duration-300" aria-label="Instagram">
                            <i class="fab fa-instagram"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!-- JavaScript -->
    <script>
        const servicesBtn = document.querySelector('.services-dropdown-btn');
        const servicesDropdown = document.querySelector('.services-dropdown');
        const areasBtn = document.querySelector('.areas-dropdown-btn');
        const areasDropdown = document.querySelector('.areas-dropdown');

        servicesBtn.addEventListener('click', () => {{
            servicesDropdown.classList.toggle('active');
            areasDropdown.classList.remove('active');
        }});

        areasBtn.addEventListener('click', () => {{
            areasDropdown.classList.toggle('active');
            servicesDropdown.classList.remove('active');
        }});

        document.addEventListener('click', (e) => {{
            if (!e.target.closest('.services-link') && !e.target.closest('.service-areas-link')) {{
                servicesDropdown.classList.remove('active');
                areasDropdown.classList.remove('active');
            }}
        }});
    </script>
</body>
</html>'''

    return html


def generate_neighborhood_page(location_key, location_title, neigh_key, neigh_data):
    """Generate neighborhood subpage HTML"""

    highlights_html = ""
    for highlight in neigh_data["highlights"]:
        highlights_html += f'<li><i class="fas fa-check text-primary mr-2"></i>{highlight}</li>\n                        '

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Summer soccer training in {neigh_data["title"]}, {location_title} - Convenient youth soccer programs near you.">
    <title>{neigh_data["title"]} Soccer Training | {location_title} | Summer Soccer Raleigh NC</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300,400,500,600,700&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Poppins', sans-serif; }}
        html {{ scroll-behavior: smooth; }}
        .text-primary {{ color: #FF5A5F; }}
        .bg-primary {{ background-color: #FF5A5F; }}
        .text-secondary {{ color: #1A1A1A; }}
        .bg-secondary {{ background-color: #1A1A1A; }}
        .text-accent {{ color: #FFD166; }}
        .btn-solid {{
            background-color: #FF5A5F;
            color: white;
            padding: 12px 24px;
            border-radius: 4px;
            font-weight: 600;
            transition: all 0.3s;
            display: inline-block;
            border: 2px solid #FF5A5F;
        }}
        .btn-solid:hover {{
            background-color: white;
            color: #FF5A5F;
            transform: scale(1.05);
        }}
        .btn-outline {{
            background-color: transparent;
            border: 2px solid #FF5A5F;
            color: #FF5A5F;
            padding: 12px 24px;
            border-radius: 4px;
            font-weight: 600;
            transition: all 0.3s;
            display: inline-block;
        }}
        .btn-outline:hover {{
            background-color: #FF5A5F;
            color: white;
        }}
        .dropdown-menu {{
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 0.5rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
            min-width: 240px;
            z-index: 1000;
            margin-top: 0.5rem;
        }}
        .dropdown-menu.active {{ display: block; }}
        .dropdown-item {{
            display: block;
            padding: 12px 20px;
            color: #374151;
            text-decoration: none;
            transition: all 300ms;
            border-bottom: 1px solid #e5e7eb;
        }}
        .dropdown-item:last-child {{ border-bottom: none; }}
        .dropdown-item:hover {{
            background-color: #fef2f2;
            color: #FF5A5F;
            padding-left: 24px;
        }}
        .btn-primary {{
            background-color: #FF5A5F;
            color: white;
            padding: 10px 24px;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s;
            display: inline-block;
            text-decoration: none;
            border: 2px solid #FF5A5F;
        }}
        .btn-primary:hover {{
            background-color: #e54950;
            transform: translateY(-2px);
        }}
        nav button {{
            background: none;
            border: none;
            cursor: pointer;
        }}
    </style>
</head>
<body class="bg-white text-secondary">
    <!-- Header -->
    <header class="sticky top-0 z-50 bg-white shadow-md">
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
            <a href="../index.html" class="flex items-center gap-3">
                <i class="fas fa-futbol text-3xl text-primary"></i>
                <span class="text-xl font-bold text-secondary">Summer Soccer Training Raleigh</span>
            </a>
            <div class="hidden lg:flex items-center gap-8">
                <a href="../index.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Home</a>
                <div class="relative services-link">
                    <button type="button" class="services-dropdown-btn text-gray-700 hover:text-primary transition-colors font-medium flex items-center gap-1">
                        Programs <i class="fas fa-chevron-down text-xs"></i>
                    </button>
                    <div class="dropdown-menu services-dropdown">
                        <a href="../programs.html#summer-camps" class="dropdown-item">Summer Camps</a>
                        <a href="../programs.html#skills-training" class="dropdown-item">Skills Training</a>
                        <a href="../programs.html#private-lessons" class="dropdown-item">Private Lessons</a>
                    </div>
                </div>
                <div class="relative service-areas-link">
                    <button type="button" class="areas-dropdown-btn text-gray-700 hover:text-primary transition-colors font-medium flex items-center gap-1">
                        Locations <i class="fas fa-chevron-down text-xs"></i>
                    </button>
                    <div class="dropdown-menu areas-dropdown">
                        <a href="../downtown-raleigh.html" class="dropdown-item">Downtown Raleigh</a>
                        <a href="../north-raleigh.html" class="dropdown-item">North Raleigh</a>
                        <a href="../cary.html" class="dropdown-item">Cary</a>
                        <a href="../apex.html" class="dropdown-item">Apex</a>
                        <a href="../wake-forest.html" class="dropdown-item">Wake Forest</a>
                    </div>
                </div>
                <a href="../index.html#about" class="text-gray-700 hover:text-primary transition-colors font-medium">About</a>
                <a href="../index.html#testimonials" class="text-gray-700 hover:text-primary transition-colors font-medium">Testimonials</a>
                <a href="../index.html#contact" class="btn-primary">Register Now</a>
            </div>
            <button type="button" class="lg:hidden text-gray-700">
                <i class="fas fa-bars text-2xl"></i>
            </button>
        </nav>
    </header>

    <!-- Breadcrumb -->
    <section class="py-4 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center gap-2 text-sm text-gray-600">
                <a href="../index.html" class="hover:text-primary">Home</a>
                <i class="fas fa-chevron-right text-xs"></i>
                <a href="../{location_key}.html" class="hover:text-primary">{location_title}</a>
                <i class="fas fa-chevron-right text-xs"></i>
                <span class="text-primary">{neigh_data["title"]}</span>
            </div>
        </div>
    </section>

    <!-- Hero Section -->
    <section class="py-16 md:py-20 bg-gradient-to-br from-gray-50 to-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl md:text-5xl font-bold text-secondary mb-4">
                {neigh_data["title"]} <span class="text-primary">Soccer Training</span>
            </h1>
            <p class="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed mb-8">
                {neigh_data["description"]}
            </p>
            <a href="../index.html#contact" class="btn-solid">Register Now</a>
        </div>
    </section>

    <!-- Community Highlights -->
    <section class="py-16 md:py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div>
                    <h2 class="text-3xl font-bold text-secondary mb-6">Why Train in {neigh_data["title"]}?</h2>
                    <ul class="space-y-3 text-gray-600">
                        {highlights_html}
                    </ul>
                    <div class="mt-8">
                        <a href="../{location_key}.html" class="btn-outline">
                            <i class="fas fa-arrow-left mr-2"></i>Back to {location_title}
                        </a>
                    </div>
                </div>
                <div>
                    <img src="https://images.unsplash.com/photo-1551958219-acbc608c6377?q=80&w=2070&auto=format&fit=crop"
                         alt="{neigh_data["title"]} Community"
                         class="rounded-2xl shadow-2xl w-full h-[400px] object-cover">
                </div>
            </div>
        </div>
    </section>

    <!-- Programs Available -->
    <section class="py-16 md:py-20 bg-gradient-to-r from-gray-50 to-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-secondary mb-4">
                    Programs Available
                </h2>
                <p class="text-lg text-gray-600">
                    All training programs are available for {neigh_data["title"]} residents
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-white border border-gray-200 rounded-lg p-6 shadow-md">
                    <h3 class="text-xl font-bold text-secondary mb-3">
                        <i class="fas fa-campground text-primary mr-2"></i>Summer Camps
                    </h3>
                    <p class="text-gray-600 mb-4">Week-long intensive training camps for all ages and skill levels.</p>
                    <a href="../programs.html#summer-camps" class="text-primary hover:underline font-semibold">Learn More →</a>
                </div>
                <div class="bg-white border border-gray-200 rounded-lg p-6 shadow-md">
                    <h3 class="text-xl font-bold text-secondary mb-3">
                        <i class="fas fa-dumbbell text-primary mr-2"></i>Skills Training
                    </h3>
                    <p class="text-gray-600 mb-4">8-week progressive program with position-specific development.</p>
                    <a href="../programs.html#skills-training" class="text-primary hover:underline font-semibold">Learn More →</a>
                </div>
                <div class="bg-white border border-gray-200 rounded-lg p-6 shadow-md">
                    <h3 class="text-xl font-bold text-secondary mb-3">
                        <i class="fas fa-user-graduate text-primary mr-2"></i>Private Lessons
                    </h3>
                    <p class="text-gray-600 mb-4">Personalized 1-on-1 coaching with video analysis and custom plans.</p>
                    <a href="../programs.html#private-lessons" class="text-primary hover:underline font-semibold">Learn More →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-16 md:py-20 bg-gradient-to-r from-primary to-accent text-white">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl md:text-4xl font-bold mb-6">Join {neigh_data["title"]} Players Today!</h2>
            <p class="text-lg mb-8 opacity-90">
                Start your soccer journey with expert coaching and comprehensive training programs
            </p>
            <a href="../index.html#contact" class="bg-white text-primary hover:bg-gray-100 px-8 py-4 rounded-lg font-semibold text-lg transition-all shadow-lg inline-block">
                Register Now
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-secondary text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p class="text-gray-400 text-sm">
                &copy; 2026 Summer Soccer Training Raleigh. All rights reserved.
            </p>
        </div>
    </footer>

    <script>
        const servicesBtn = document.querySelector('.services-dropdown-btn');
        const servicesDropdown = document.querySelector('.services-dropdown');
        const areasBtn = document.querySelector('.areas-dropdown-btn');
        const areasDropdown = document.querySelector('.areas-dropdown');

        servicesBtn.addEventListener('click', () => {{
            servicesDropdown.classList.toggle('active');
            areasDropdown.classList.remove('active');
        }});

        areasBtn.addEventListener('click', () => {{
            areasDropdown.classList.toggle('active');
            servicesDropdown.classList.remove('active');
        }});

        document.addEventListener('click', (e) => {{
            if (!e.target.closest('.services-link') && !e.target.closest('.service-areas-link')) {{
                servicesDropdown.classList.remove('active');
                areasDropdown.classList.remove('active');
            }}
        }});
    </script>
</body>
</html>'''

    return html


# Main execution
def main():
    print("Generating location pages...")

    # Generate main location pages
    for location_key, location_data in locations.items():
        filename = f"{location_key}.html"
        html = generate_location_page(location_key, location_data)
        with open(filename, 'w') as f:
            f.write(html)
        print(f"✅ Created {filename}")

        # Generate neighborhood pages
        for neigh_key, neigh_data in location_data["neighborhoods"].items():
            neigh_filename = f"{location_key}/{neigh_key}.html"
            neigh_html = generate_neighborhood_page(location_key, location_data["title"], neigh_key, neigh_data)
            with open(neigh_filename, 'w') as f:
                f.write(neigh_html)
            print(f"✅ Created {neigh_filename}")

    print("\n🎉 All location pages generated successfully!")
    print("\nGenerated files:")
    print("Main location pages: 4")
    print("Neighborhood pages: 12")
    print("Total: 16 new pages")


if __name__ == "__main__":
    main()
