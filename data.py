# STUDENT MANAGEMENT SYSTEM - Central Data Repository
# This file contains all static data for states, cities, colleges, and departments

# ==================== STATES ====================
# Indian States and Union Territories

STATES = [
    # States (28)
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    # Union Territories (8)
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi",
    "Jammu and Kashmir",
    "Ladakh",
    "Lakshadweep",
    "Puducherry"
]

# ==================== CITIES BY STATE ====================
# Comprehensive list of cities organized by state

CITIES_BY_STATE = {
    "Andhra Pradesh": [
        "Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Kurnool", "Rajahmundry", "Tirupati",
        "Kadapa", "Anantapur", "Eluru", "Ongole", "Chittoor", "Machilipatnam", "Tenali", "Proddatur",
        "Vizianagaram", "Srikakulam", "Amadalavalasa", "Palasa", "Bobbili", "Narasannapeta",
        "Parvathipuram", "Ichchapuram", "Anakapalle", "Narsipatnam", "Pendurthi", "Yelamanchili",
        "Chodavaram", "Kakinada", "Amalapuram", "Mandapeta", "Ramachandrapuram", "Peddapuram",
        "Samalkot", "Tuni", "Razole", "Bhimavaram", "Tadepalligudem", "Narasapuram", "Tanuku",
        "Palakollu", "Nidadavole", "Jangareddygudem", "Gudivada", "Jaggaiahpet", "Nuzvid",
        "Mylavaram", "Avanigadda", "Kaikalur", "Mangalagiri", "Narasaraopet", "Chilakaluripet",
        "Piduguralla", "Sattenapalle", "Bapatla", "Repalle", "Ponnur", "Chirala", "Markapur",
        "Kandukur", "Addanki", "Giddalur", "Kavali", "Atmakur", "Gudur", "Venkatagiri", "Naidupet",
        "Sullurpeta", "Madanapalle", "Punganur", "Srikalahasti", "Nagari", "Palamaner", "Vayalpadu",
        "Pulivendula", "Jammalamadugu", "Mydukur", "Rayachoti", "Badvel", "Hindupur", "Dharmavaram",
        "Kadiri", "Guntakal", "Tadipatri", "Penukonda", "Kalyandurg", "Adoni", "Nandyal",
        "Yemmiganur", "Allagadda", "Banaganapalle", "Dhone", "Kodumur"
    ],
    "Arunachal Pradesh": [
        "Itanagar", "Naharlagun", "Nirjuli", "Banderdewa", "Pasighat", "Aalo", "Basar", "Likabali",
        "Ruksin", "Tawang", "Lumla", "Zemithang", "Jang", "Ziro", "Yachuli", "Daporijo", "Sagalee",
        "Kimin", "Tezu", "Wakro", "Changlang", "Jairampur", "Miao", "Khonsa", "Longding", "Roing",
        "Anini", "Seppa", "Bomdila", "Dirang", "Hawai", "Palin", "Koloriang", "Lemmi"
    ],
    "Assam": [
        "Guwahati", "Dibrugarh", "Silchar", "Jorhat", "Tezpur", "Nagaon", "Tinsukia", "Sivasagar",
        "Dhubri", "Goalpara", "Bongaigaon", "Karimganj", "Lakhimpur", "Morigaon", "Hojai",
        "Duliajan", "Digboi", "Margherita", "Nazira", "Sonari", "Moranhat", "Naharkatia",
        "Lanka", "Lumding", "Kampur", "Bokakhat", "Dergaon", "Barpeta", "Barpeta Road",
        "Abhayapuri", "Bijni", "Pathsala", "Rangia", "Gauripur", "Bilasipara", "Sapatgram",
        "Hailakandi", "Badarpur", "Lala", "Mangaldoi", "Udalguri", "Tangla", "Dhekiajuli",
        "Biswanath Chariali", "Diphu", "Bokajan", "Haflong", "Umrangso", "Kokrajhar",
        "Gossaigaon", "Chirang", "Golaghat", "Majuli", "Sarupathar", "Amguri", "Chapar", "Lakhipur"
    ],
    "Bihar": [
        "Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga", "Purnia", "Arrah", "Begusarai",
        "Bihar Sharif", "Katihar", "Munger", "Chapra", "Danapur", "Saharsa", "Sasaram", "Hajipur",
        "Dehri", "Siwan", "Motihari", "Nawada", "Bagaha", "Buxar", "Kishanganj", "Sitamarhi",
        "Jamalpur", "Jehanabad", "Aurangabad", "Lakhisarai", "Sheikhpura", "Bettiah", "Madhubani",
        "Samastipur", "Gopalganj", "Supaul", "Madhepura", "Khagaria", "Sheohar", "Araria"
    ],
    "Chhattisgarh": [
        "Raipur", "Bhilai", "Bilaspur", "Durg", "Korba", "Rajnandgaon", "Raigarh", "Jagdalpur",
        "Ambikapur", "Dhamtari", "Mahasamund", "Bhatapara", "Chirmiri", "Janjgir", "Sakti",
        "Dalli-Rajhara", "Tilda", "Manendragarh", "Champa", "Bemetara", "Patan", "Balod",
        "Simga", "Mungeli", "Dongargarh", "Baloda Bazar", "Kawardha"
    ],
    "Goa": [
        "Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda", "Bicholim", "Curchorem",
        "Sanquelim", "Cuncolim", "Quepem", "Canacona", "Valpoi", "Pernem", "Sanguem"
    ],
    "Gujarat": [
        "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar", "Bhavnagar", "Jamnagar",
        "Junagadh", "Anand", "Nadiad", "Morbi", "Surendranagar", "Bharuch", "Mehsana",
        "Gandhidham", "Vapi", "Navsari", "Veraval", "Porbandar", "Godhra", "Botad",
        "Amreli", "Deesa", "Jetpur", "Gondal", "Palanpur", "Valsad", "Patan", "Bhuj",
        "Dahod", "Modasa", "Kalol", "Visnagar", "Mandvi", "Vyara", "Himmatnagar"
    ],
    "Haryana": [
        "Gurugram", "Faridabad", "Panipat", "Ambala", "Yamunanagar", "Rohtak", "Hisar",
        "Karnal", "Sonipat", "Panchkula", "Bhiwani", "Sirsa", "Bahadurgarh", "Jind",
        "Thanesar", "Kaithal", "Rewari", "Palwal", "Gohana", "Hansi", "Narnaul",
        "Fatehabad", "Tohana", "Charkhi Dadri", "Mahendragarh", "Narwana", "Pundri"
    ],
    "Himachal Pradesh": [
        "Shimla", "Solan", "Mandi", "Dharamshala", "Palampur", "Kullu", "Hamirpur", "Bilaspur",
        "Kangra", "Una", "Nahan", "Chamba", "Sundarnagar", "Paonta Sahib", "Baddi", "Nalagarh",
        "Parwanoo", "Kasauli", "Rampur", "Arki", "Manali", "Jogindernagar", "Nurpur", "Dalhousie"
    ],
    "Jharkhand": [
        "Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh", "Giridih", "Ramgarh",
        "Deoghar", "Dumka", "Chaibasa", "Phusro", "Medininagar", "Chirkunda", "Sindri",
        "Gumla", "Sahibganj", "Godda", "Pakur", "Koderma", "Lohardaga", "Jamtara"
    ],
    "Karnataka": [
        "Bangalore", "Mysore", "Mangalore", "Hubli", "Belgaum", "Davangere", "Bellary", "Tumkur",
        "Shimoga", "Gulbarga", "Bidar", "Hassan", "Udupi", "Raichur", "Bijapur", "Chitradurga",
        "Mandya", "Kolar", "Bagalkot", "Gadag", "Chikmagalur", "Karwar", "Hospet", "Bhadravati",
        "Ranibennur", "Sirsi", "Haveri", "Yadgir", "Koppal", "Ramanagara", "Vijayapura", "Manipal", "Surathkal"
    ],
    "Kerala": [
        "Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kollam", "Palakkad", "Alappuzha",
        "Malappuram", "Kannur", "Kasaragod", "Kottayam", "Pathanamthitta", "Idukki", "Ernakulam",
        "Wayanad", "Thalassery", "Tirur", "Ponnani", "Kayamkulam", "Kottakkal", "Changanassery",
        "Manjeri", "Perinthalmanna", "Nilambur", "Attingal", "Cherthala", "Guruvayur"
    ],
    "Madhya Pradesh": [
        "Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain", "Sagar", "Dewas", "Satna",
        "Ratlam", "Rewa", "Murwara", "Singrauli", "Burhanpur", "Khandwa", "Morena", "Bhind",
        "Chhindwara", "Guna", "Shivpuri", "Vidisha", "Chhatarpur", "Damoh", "Mandsaur",
        "Khargone", "Neemuch", "Pithampur", "Hoshangabad", "Itarsi", "Sehore", "Betul",
        "Seoni", "Datia", "Nagda", "Dhar", "Barwani"
    ],
    "Maharashtra": [
        "Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Thane", "Solapur", "Amravati",
        "Kolhapur", "Nanded", "Sangli", "Akola", "Latur", "Jalgaon", "Ahmednagar", "Chandrapur",
        "Parbhani", "Ichalkaranji", "Jalna", "Bhusawal", "Panvel", "Satara", "Beed", "Yavatmal",
        "Kamptee", "Gondia", "Barshi", "Osmanabad", "Wardha", "Udgir", "Hinganghat",
        "Vita", "Buldhana", "Navi Mumbai", "Ulhasnagar", "Vasai-Virar", "Mira-Bhayandar",
        "Kalyan-Dombivli", "Bhiwandi", "Pimpri-Chinchwad", "Malegaon", "Dhule"
    ],
    "Manipur": [
        "Imphal", "Thoubal", "Bishnupur", "Churachandpur", "Kakching", "Ukhrul", "Senapati",
        "Tamenglong", "Chandel", "Jiribam", "Moreh", "Yairipok", "Wangjing", "Mayang Imphal"
    ],
    "Meghalaya": [
        "Shillong", "Tura", "Jowai", "Nongpoh", "Williamnagar", "Baghmara", "Nongstoin",
        "Resubelpara", "Mairang", "Cherrapunji", "Mawkyrwat"
    ],
    "Mizoram": [
        "Aizawl", "Lunglei", "Champhai", "Serchhip", "Kolasib", "Saiha", "Lawngtlai",
        "Mamit", "Tlabung", "Khawzawl", "Vairengte"
    ],
    "Nagaland": [
        "Kohima", "Dimapur", "Mokokchung", "Tuensang", "Wokha", "Zunheboto", "Phek",
        "Mon", "Kiphire", "Longleng", "Peren", "Chumukedima"
    ],
    "Odisha": [
        "Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur", "Puri", "Balasore",
        "Bhadrak", "Baripada", "Jeypore", "Barbil", "Jharsuguda", "Rayagada", "Balangir",
        "Angul", "Bargarh", "Kendujhar", "Dhenkanal", "Paradip", "Jajpur", "Kendrapara",
        "Sunabeda", "Bhawanipatna", "Koraput", "Phulbani", "Gunupur", "Brahmapur"
    ],
    "Punjab": [
        "Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda", "Mohali",
        "Pathankot", "Hoshiarpur", "Moga", "Batala", "Kapurthala", "Khanna", "Malerkotla",
        "Abohar", "Muktsar", "Barnala", "Rajpura", "Firozpur", "Phagwara", "Sangrur",
        "Faridkot", "Mansa", "Fazilka", "Rupnagar", "Fatehgarh Sahib", "Gurdaspur", "Chandigarh"
    ],
    "Rajasthan": [
        "Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer", "Bikaner", "Alwar", "Bharatpur",
        "Bhilwara", "Sikar", "Pali", "Sri Ganganagar", "Tonk", "Kishangarh", "Beawar",
        "Hanumangarh", "Churu", "Nagaur", "Jhunjhunu", "Chittorgarh", "Sawai Madhopur",
        "Bundi", "Jhalawar", "Barmer", "Jaisalmer", "Banswara", "Dungarpur", "Dausa",
        "Karauli", "Pratapgarh", "Rajsamand", "Sirohi", "Dholpur", "Pilani"
    ],
    "Sikkim": [
        "Gangtok", "Namchi", "Mangan", "Gyalshing", "Rangpo", "Jorethang", "Singtam",
        "Pelling", "Ravangla", "Yuksom"
    ],
    "Tamil Nadu": [
        "Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Tiruppur",
        "Erode", "Vellore", "Thoothukudi", "Dindigul", "Thanjavur", "Karur", "Kancheepuram",
        "Nagercoil", "Kumbakonam", "Cuddalore", "Krishnagiri", "Dharmapuri", "Namakkal",
        "Pudukkottai", "Ramanathapuram", "Sivakasi", "Virudhunagar", "Ambur", "Pollachi",
        "Hosur", "Tiruvannamalai", "Neyveli", "Nagapattinam", "Mayiladuthurai", "Palani",
        "Ooty", "Arakkonam", "Chengalpattu", "Tirupattur", "Tenkasi", "Ranipet"
    ],
    "Telangana": [
        "Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam", "Ramagundam", "Mahbubnagar",
        "Nalgonda", "Adilabad", "Suryapet", "Miryalaguda", "Jagtial", "Mancherial", "Nirmal",
        "Kamareddy", "Siddipet", "Sangareddy", "Vikarabad", "Wanaparthy", "Gadwal", "Nagarkurnool",
        "Sircilla", "Bhongir", "Jangaon", "Peddapalli", "Kothagudem", "Palwancha"
    ],
    "Tripura": [
        "Agartala", "Udaipur", "Dharmanagar", "Kailasahar", "Ambassa", "Belonia",
        "Sabroom", "Khowai", "Teliamura", "Amarpur", "Sonamura", "Kumarghat"
    ],
    "Uttar Pradesh": [
        "Lucknow", "Kanpur", "Agra", "Varanasi", "Noida", "Ghaziabad", "Meerut", "Allahabad",
        "Bareilly", "Aligarh", "Moradabad", "Saharanpur", "Gorakhpur", "Firozabad", "Jhansi",
        "Muzaffarnagar", "Mathura", "Rampur", "Shahjahanpur", "Farrukhabad", "Maunath Bhanjan",
        "Hapur", "Ayodhya", "Etawah", "Mirzapur", "Bulandshahr", "Sambhal", "Amroha", "Hardoi",
        "Fatehpur", "Raebareli", "Orai", "Sitapur", "Bahraich", "Modinagar", "Unnao", "Jaunpur",
        "Lakhimpur", "Hathras", "Budaun", "Chandausi", "Sultanpur", "Mainpuri", "Lalitpur",
        "Etah", "Deoria", "Gonda", "Basti", "Azamgarh", "Ballia", "Maharajganj", "Kushinagar"
    ],
    "Uttarakhand": [
        "Dehradun", "Haridwar", "Rishikesh", "Roorkee", "Haldwani", "Rudrapur", "Kashipur",
        "Nainital", "Mussoorie", "Pithoragarh", "Almora", "Bageshwar", "Champawat", "Pauri",
        "Tehri", "Uttarkashi", "Rudraprayag", "Chamoli", "Kotdwar", "Ramnagar", "Tanakpur",
        "Jaspur", "Sitarganj", "Kichha", "Manglaur"
    ],
    "West Bengal": [
        "Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri", "Bardhaman", "Malda",
        "Baharampur", "Habra", "Kharagpur", "Shantipur", "Dankuni", "Dhulian", "Ranaghat",
        "Haldia", "Raiganj", "Krishnanagar", "Nabadwip", "Medinipur", "Jalpaiguri",
        "Balurghat", "Bankura", "Darjeeling", "Alipurduar", "Purulia", "Jangipur",
        "Bolpur", "Bangaon", "Cooch Behar", "Barasat", "Basirhat", "Bongaon", "Tamluk"
    ],
    "Andaman and Nicobar Islands": [
        "Port Blair", "Diglipur", "Mayabunder", "Rangat", "Car Nicobar", "Hut Bay"
    ],
    "Chandigarh": [
        "Chandigarh"
    ],
    "Dadra and Nagar Haveli and Daman and Diu": [
        "Daman", "Diu", "Silvassa", "Amli", "Dadra"
    ],
    "Delhi": [
        "New Delhi", "North Delhi", "South Delhi", "East Delhi", "West Delhi",
        "Central Delhi", "North East Delhi", "North West Delhi", "South East Delhi",
        "South West Delhi", "Shahdara", "Dwarka", "Rohini"
    ],
    "Jammu and Kashmir": [
        "Srinagar", "Jammu", "Anantnag", "Baramulla", "Budgam", "Pulwama", "Kupwara",
        "Shopian", "Ganderbal", "Bandipora", "Udhampur", "Kathua", "Doda", "Ramban",
        "Kishtwar", "Poonch", "Rajouri", "Reasi", "Samba"
    ],
    "Ladakh": [
        "Leh", "Kargil", "Nubra", "Zanskar", "Dras", "Diskit"
    ],
    "Lakshadweep": [
        "Kavaratti", "Agatti", "Minicoy", "Amini", "Andrott", "Kalpeni"
    ],
    "Puducherry": [
        "Puducherry", "Karaikal", "Mahe", "Yanam", "Ozhukarai"
    ]
}

# ==================== COLLEGES ====================
# Major Indian Colleges with State and City Information

COLLEGES = [
    {"name": "Indian Institute of Technology Delhi", "state": "Delhi", "city": "New Delhi"},
    {"name": "Indian Institute of Technology Bombay", "state": "Maharashtra", "city": "Mumbai"},
    {"name": "Indian Institute of Technology Madras", "state": "Tamil Nadu", "city": "Chennai"},
    {"name": "Indian Institute of Technology Kanpur", "state": "Uttar Pradesh", "city": "Kanpur"},
    {"name": "Indian Institute of Technology Kharagpur", "state": "West Bengal", "city": "Kharagpur"},
    {"name": "Indian Institute of Science Bangalore", "state": "Karnataka", "city": "Bangalore"},
    {"name": "Jawaharlal Nehru University", "state": "Delhi", "city": "New Delhi"},
    {"name": "University of Delhi", "state": "Delhi", "city": "New Delhi"},
    {"name": "Anna University", "state": "Tamil Nadu", "city": "Chennai"},
    {"name": "Jadavpur University", "state": "West Bengal", "city": "Kolkata"},
    {"name": "Banaras Hindu University", "state": "Uttar Pradesh", "city": "Varanasi"},
    {"name": "Aligarh Muslim University", "state": "Uttar Pradesh", "city": "Aligarh"},
    {"name": "National Institute of Technology Trichy", "state": "Tamil Nadu", "city": "Tiruchirappalli"},
    {"name": "National Institute of Technology Warangal", "state": "Telangana", "city": "Warangal"},
    {"name": "Vellore Institute of Technology", "state": "Tamil Nadu", "city": "Vellore"},
    {"name": "Birla Institute of Technology and Science Pilani", "state": "Rajasthan", "city": "Pilani"},
    {"name": "Manipal Academy of Higher Education", "state": "Karnataka", "city": "Manipal"},
    {"name": "University of Hyderabad", "state": "Telangana", "city": "Hyderabad"},
    {"name": "Amity University Noida", "state": "Uttar Pradesh", "city": "Noida"},
    {"name": "SRM Institute of Science and Technology", "state": "Tamil Nadu", "city": "Chennai"},
    {"name": "Savitribai Phule Pune University", "state": "Maharashtra", "city": "Pune"},
    {"name": "Gujarat University", "state": "Gujarat", "city": "Ahmedabad"},
    {"name": "Osmania University", "state": "Telangana", "city": "Hyderabad"},
    {"name": "Calcutta University", "state": "West Bengal", "city": "Kolkata"},
    {"name": "Mumbai University", "state": "Maharashtra", "city": "Mumbai"},
    {"name": "Bangalore University", "state": "Karnataka", "city": "Bangalore"},
    {"name": "Panjab University", "state": "Punjab", "city": "Chandigarh"},
    {"name": "Lucknow University", "state": "Uttar Pradesh", "city": "Lucknow"},
    {"name": "Cochin University of Science and Technology", "state": "Kerala", "city": "Kochi"},
    {"name": "National Institute of Technology Karnataka", "state": "Karnataka", "city": "Surathkal"}
]

# ==================== DEPARTMENTS ====================
# Engineering Departments List

DEPARTMENTS = [
    # Core / Traditional Engineering
    "Computer Science and Engineering",
    "Information Technology",
    "Electronics and Communication Engineering",
    "Electrical and Electronics Engineering",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Chemical Engineering",
    "Biotechnology Engineering",
    "Aerospace Engineering",
    "Automobile Engineering",
    "Industrial Engineering",
    "Production Engineering",
    "Manufacturing Engineering",
    "Metallurgical Engineering",
    "Mining Engineering",
    "Marine Engineering",
    "Naval Architecture",
    "Textile Engineering",
    "Petroleum Engineering",
    "Ceramic Engineering",
    "Agricultural Engineering",
    "Food Technology",
    "Food Processing Engineering",
    "Dairy Technology",
    "Polymer Engineering",
    "Printing Technology",
    "Paper Technology",
    "Rubber Technology",
    "Leather Technology",
    # Computer / IT Specializations
    "Artificial Intelligence and Machine Learning",
    "Artificial Intelligence and Data Science",
    "Computer Engineering",
    "Software Engineering",
    "Computer Science and Design",
    "Computer Science and Business Systems",
    "Computer Science and Information Security",
    "Computer Science and Networking",
    "Computer Science and Engineering with specialization in AI",
    "Computer Science and Engineering with specialization in Data Science",
    "Computer Science and Engineering (Cyber Security)",
    "Computer Science and Engineering (Artificial Intelligence and Machine Learning)",
    "Computer Science and Engineering (Cloud Computing)",
    "Computer Science and Artificial Intelligence",
    "Computer Science and Data Science",
    "Computer Science and Cyber Security",
    "Computer Science and Machine Learning",
    "Computer Science and Cloud Computing",
    "Computer Science and Blockchain Technology",
    "Computer Science and Internet of Things",
    "Computer Science and Game Development",
    "Information Science and Engineering",
    "Information Systems Engineering",
    "Data Engineering",
    "Big Data Engineering",
    "Cloud Engineering",
    "DevOps Engineering",
    "Full Stack Engineering",
    # Electronics / Electrical Specializations
    "Electronics and Instrumentation Engineering",
    "Electronics and Telecommunication Engineering",
    "Electronics Engineering",
    "Instrumentation Engineering",
    "Control and Instrumentation Engineering",
    "Power Engineering",
    "Power Systems Engineering",
    "Electrical Power Engineering",
    "Embedded Systems Engineering",
    "VLSI Design",
    "Microelectronics Engineering",
    "Nanoelectronics Engineering",
    "Communication Systems Engineering",
    "Signal Processing Engineering",
    # Mechanical / Allied Specializations
    "Mechatronics Engineering",
    "Robotics Engineering",
    "Industrial Automation Engineering",
    "Automotive Design Engineering",
    "Thermal Engineering",
    "Energy Engineering",
    "Renewable Energy Engineering",
    "Manufacturing Systems Engineering",
    "Production and Industrial Engineering",
    "Tool Engineering",
    "Materials Engineering",
    "Nanotechnology Engineering",
    "Biomedical Engineering",
    "Biomechanical Engineering",
    # Civil / Infrastructure Specializations
    "Structural Engineering",
    "Construction Engineering",
    "Construction Technology",
    "Environmental Engineering",
    "Geotechnical Engineering",
    "Transportation Engineering",
    "Water Resources Engineering",
    "Urban Engineering",
    "Smart Infrastructure Engineering",
    "Earthquake Engineering",
    "Coastal Engineering",
    "Harbour Engineering",
    "Remote Sensing and GIS",
    "Surveying Engineering",
    # Emerging / Interdisciplinary Engineering
    "Artificial Intelligence Engineering",
    "Machine Learning Engineering",
    "Data Analytics Engineering",
    "Data Science Engineering",
    "Cyber Security Engineering",
    "Internet of Things Engineering",
    "Blockchain Engineering",
    "Quantum Computing Engineering",
    "Augmented Reality Engineering",
    "Virtual Reality Engineering",
    "Game Technology Engineering",
    "Financial Technology Engineering",
    "Healthcare Engineering",
    "Systems Engineering",
    "Engineering Physics",
    "Engineering Mathematics",
    "Engineering Design",
    "Sustainable Engineering"
]

# ==================== DEPARTMENT SHORT NAMES ====================
# Abbreviated department names for compact display

DEPARTMENT_SHORT_NAMES = {
    "Computer Science and Engineering": "CSE",
    "Information Technology": "IT",
    "Electronics and Communication Engineering": "ECE",
    "Electrical and Electronics Engineering": "EEE",
    "Electrical Engineering": "EE",
    "Mechanical Engineering": "ME",
    "Civil Engineering": "CE",
    "Chemical Engineering": "CHE",
    "Biotechnology Engineering": "BT",
    "Aerospace Engineering": "AE",
    "Automobile Engineering": "AUTO",
    "Industrial Engineering": "IE",
    "Production Engineering": "PE",
    "Manufacturing Engineering": "MFG",
    "Metallurgical Engineering": "MET",
    "Mining Engineering": "MIN",
    "Marine Engineering": "MAR",
    "Naval Architecture": "NA",
    "Textile Engineering": "TEX",
    "Petroleum Engineering": "PETRO",
    "Ceramic Engineering": "CER",
    "Agricultural Engineering": "AGR",
    "Food Technology": "FT",
    "Food Processing Engineering": "FPE",
    "Dairy Technology": "DT",
    "Polymer Engineering": "POLY",
    "Printing Technology": "PRINT",
    "Paper Technology": "PAPER",
    "Rubber Technology": "RUB",
    "Leather Technology": "LT",
    "Artificial Intelligence and Machine Learning": "AIML",
    "Artificial Intelligence and Data Science": "AIDS",
    "Computer Engineering": "COMP",
    "Software Engineering": "SE",
    "Computer Science and Design": "CSD",
    "Computer Science and Business Systems": "CSBS",
    "Computer Science and Information Security": "CSIS",
    "Computer Science and Networking": "CSN",
    "Computer Science and Engineering with specialization in AI": "CSE (AI)",
    "Computer Science and Engineering with specialization in Data Science": "CSE (DS)",
    "Computer Science and Engineering (Cyber Security)": "CSE (CS)",
    "Computer Science and Engineering (Artificial Intelligence and Machine Learning)": "CSE (AIML)",
    "Computer Science and Engineering (Cloud Computing)": "CSE (Cloud)",
    "Computer Science and Artificial Intelligence": "CSAI",
    "Computer Science and Data Science": "CSDS",
    "Computer Science and Cyber Security": "CSCS",
    "Computer Science and Machine Learning": "CSML",
    "Computer Science and Cloud Computing": "CSCloud",
    "Computer Science and Blockchain Technology": "CSBlockchain",
    "Computer Science and Internet of Things": "CSIoT",
    "Computer Science and Game Development": "CSGameDev",
    "Information Science and Engineering": "ISE",
    "Information Systems Engineering": "IS",
    "Data Engineering": "DE",
    "Big Data Engineering": "BDE",
    "Cloud Engineering": "Cloud",
    "DevOps Engineering": "DevOps",
    "Full Stack Engineering": "FullStack",
    "Electronics and Instrumentation Engineering": "EI",
    "Electronics and Telecommunication Engineering": "ETC",
    "Electronics Engineering": "EC",
    "Instrumentation Engineering": "INST",
    "Control and Instrumentation Engineering": "CI",
    "Power Engineering": "PWR",
    "Power Systems Engineering": "PS",
    "Electrical Power Engineering": "EP",
    "Embedded Systems Engineering": "ES",
    "VLSI Design": "VLSI",
    "Microelectronics Engineering": "MICRO",
    "Nanoelectronics Engineering": "NANO-E",
    "Communication Systems Engineering": "COMM",
    "Signal Processing Engineering": "SP",
    "Mechatronics Engineering": "MECH",
    "Robotics Engineering": "ROBO",
    "Industrial Automation Engineering": "IA",
    "Automotive Design Engineering": "AUTO-D",
    "Thermal Engineering": "THERM",
    "Energy Engineering": "ENRG",
    "Renewable Energy Engineering": "RE",
    "Manufacturing Systems Engineering": "MSE",
    "Production and Industrial Engineering": "PIE",
    "Tool Engineering": "TOOL",
    "Materials Engineering": "MAT",
    "Nanotechnology Engineering": "NANO",
    "Biomedical Engineering": "BME",
    "Biomechanical Engineering": "BIOME",
    "Structural Engineering": "STRUC",
    "Construction Engineering": "CONST",
    "Construction Technology": "CT",
    "Environmental Engineering": "ENV",
    "Geotechnical Engineering": "GEOTECH",
    "Transportation Engineering": "TRANS",
    "Water Resources Engineering": "WR",
    "Urban Engineering": "URB",
    "Smart Infrastructure Engineering": "SMART-I",
    "Earthquake Engineering": "EQ",
    "Coastal Engineering": "COAST",
    "Harbour Engineering": "HARB",
    "Remote Sensing and GIS": "RSGIS",
    "Surveying Engineering": "SURV",
    "Artificial Intelligence Engineering": "AI",
    "Machine Learning Engineering": "ML",
    "Data Analytics Engineering": "DA",
    "Data Science Engineering": "DS",
    "Cyber Security Engineering": "CyberSec",
    "Internet of Things Engineering": "IoT",
    "Blockchain Engineering": "Blockchain",
    "Quantum Computing Engineering": "QC",
    "Augmented Reality Engineering": "AR",
    "Virtual Reality Engineering": "VR",
    "Game Technology Engineering": "GameTech",
    "Financial Technology Engineering": "FinTech",
    "Healthcare Engineering": "HealthTech",
    "Systems Engineering": "SYS",
    "Engineering Physics": "EP",
    "Engineering Mathematics": "EM",
    "Engineering Design": "ED",
    "Sustainable Engineering": "SUST"
}
