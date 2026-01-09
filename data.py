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
# Comprehensive Indian Colleges Database organized by State
# Format: {"name": "College Name", "state": "State", "city": "City", "type": "Govt/Private/Deemed"}

COLLEGES = [
    # ===== ANDHRA PRADESH =====
    {"name": "Indian Institute of Technology Tirupati", "state": "Andhra Pradesh", "city": "Tirupati", "type": "Govt"},
    {"name": "National Institute of Technology Andhra Pradesh", "state": "Andhra Pradesh", "city": "Tadepalligudem", "type": "Govt"},
    {"name": "Andhra University", "state": "Andhra Pradesh", "city": "Visakhapatnam", "type": "Govt"},
    {"name": "JNTU Kakinada", "state": "Andhra Pradesh", "city": "Kakinada", "type": "Govt"},
    {"name": "JNTU Anantapur", "state": "Andhra Pradesh", "city": "Anantapur", "type": "Govt"},
    {"name": "Sri Venkateswara University", "state": "Andhra Pradesh", "city": "Tirupati", "type": "Govt"},
    {"name": "Acharya Nagarjuna University", "state": "Andhra Pradesh", "city": "Guntur", "type": "Govt"},
    {"name": "Krishna University", "state": "Andhra Pradesh", "city": "Machilipatnam", "type": "Govt"},
    {"name": "Vignan University", "state": "Andhra Pradesh", "city": "Guntur", "type": "Private"},
    {"name": "KL University", "state": "Andhra Pradesh", "city": "Vijayawada", "type": "Deemed"},
    {"name": "GITAM University", "state": "Andhra Pradesh", "city": "Visakhapatnam", "type": "Deemed"},
    {"name": "Centurion University", "state": "Andhra Pradesh", "city": "Visakhapatnam", "type": "Private"},
    {"name": "Adikavi Nannaya University", "state": "Andhra Pradesh", "city": "Rajahmundry", "type": "Govt"},
    {"name": "Vikrama Simhapuri University", "state": "Andhra Pradesh", "city": "Nellore", "type": "Govt"},
    {"name": "Rayalaseema University", "state": "Andhra Pradesh", "city": "Kurnool", "type": "Govt"},
    
    # ===== ARUNACHAL PRADESH =====
    {"name": "National Institute of Technology Arunachal Pradesh", "state": "Arunachal Pradesh", "city": "Itanagar", "type": "Govt"},
    {"name": "Rajiv Gandhi University", "state": "Arunachal Pradesh", "city": "Itanagar", "type": "Govt"},
    {"name": "North Eastern Regional Institute of Science and Technology", "state": "Arunachal Pradesh", "city": "Itanagar", "type": "Govt"},
    
    # ===== ASSAM =====
    {"name": "Indian Institute of Technology Guwahati", "state": "Assam", "city": "Guwahati", "type": "Govt"},
    {"name": "National Institute of Technology Silchar", "state": "Assam", "city": "Silchar", "type": "Govt"},
    {"name": "Gauhati University", "state": "Assam", "city": "Guwahati", "type": "Govt"},
    {"name": "Dibrugarh University", "state": "Assam", "city": "Dibrugarh", "type": "Govt"},
    {"name": "Tezpur University", "state": "Assam", "city": "Tezpur", "type": "Govt"},
    {"name": "Assam University", "state": "Assam", "city": "Silchar", "type": "Govt"},
    {"name": "Jorhat Engineering College", "state": "Assam", "city": "Jorhat", "type": "Govt"},
    {"name": "Assam Engineering College", "state": "Assam", "city": "Guwahati", "type": "Govt"},
    
    # ===== BIHAR =====
    {"name": "Indian Institute of Technology Patna", "state": "Bihar", "city": "Patna", "type": "Govt"},
    {"name": "National Institute of Technology Patna", "state": "Bihar", "city": "Patna", "type": "Govt"},
    {"name": "Patna University", "state": "Bihar", "city": "Patna", "type": "Govt"},
    {"name": "Magadh University", "state": "Bihar", "city": "Gaya", "type": "Govt"},
    {"name": "Bihar Institute of Technology", "state": "Bihar", "city": "Patna", "type": "Govt"},
    {"name": "Bhagalpur College of Engineering", "state": "Bihar", "city": "Bhagalpur", "type": "Govt"},
    {"name": "Muzaffarpur Institute of Technology", "state": "Bihar", "city": "Muzaffarpur", "type": "Govt"},
    {"name": "Lalit Narayan Mithila University", "state": "Bihar", "city": "Darbhanga", "type": "Govt"},
    {"name": "Aryabhatta Knowledge University", "state": "Bihar", "city": "Patna", "type": "Govt"},
    
    # ===== CHHATTISGARH =====
    {"name": "National Institute of Technology Raipur", "state": "Chhattisgarh", "city": "Raipur", "type": "Govt"},
    {"name": "Indian Institute of Information Technology Naya Raipur", "state": "Chhattisgarh", "city": "Raipur", "type": "Govt"},
    {"name": "Pt. Ravishankar Shukla University", "state": "Chhattisgarh", "city": "Raipur", "type": "Govt"},
    {"name": "Chhattisgarh Swami Vivekanand Technical University", "state": "Chhattisgarh", "city": "Bhilai", "type": "Govt"},
    {"name": "Guru Ghasidas University", "state": "Chhattisgarh", "city": "Bilaspur", "type": "Govt"},
    {"name": "Kalinga University", "state": "Chhattisgarh", "city": "Raipur", "type": "Private"},
    
    # ===== GOA =====
    {"name": "National Institute of Technology Goa", "state": "Goa", "city": "Ponda", "type": "Govt"},
    {"name": "Goa University", "state": "Goa", "city": "Panaji", "type": "Govt"},
    {"name": "Goa Engineering College", "state": "Goa", "city": "Ponda", "type": "Govt"},
    {"name": "Birla Institute of Technology and Science Goa", "state": "Goa", "city": "Sanquelim", "type": "Private"},
    
    # ===== GUJARAT =====
    {"name": "Indian Institute of Technology Gandhinagar", "state": "Gujarat", "city": "Gandhinagar", "type": "Govt"},
    {"name": "Nirma University", "state": "Gujarat", "city": "Ahmedabad", "type": "Private"},
    {"name": "DA-IICT Gandhinagar", "state": "Gujarat", "city": "Gandhinagar", "type": "Govt"},
    {"name": "National Institute of Technology Surat", "state": "Gujarat", "city": "Surat", "type": "Govt"},
    {"name": "Gujarat University", "state": "Gujarat", "city": "Ahmedabad", "type": "Govt"},
    {"name": "Sardar Vallabhbhai National Institute of Technology", "state": "Gujarat", "city": "Surat", "type": "Govt"},
    {"name": "Pandit Deendayal Petroleum University", "state": "Gujarat", "city": "Gandhinagar", "type": "Govt"},
    {"name": "Gujarat Technological University", "state": "Gujarat", "city": "Ahmedabad", "type": "Govt"},
    {"name": "LD College of Engineering", "state": "Gujarat", "city": "Ahmedabad", "type": "Govt"},
    {"name": "Sardar Patel University", "state": "Gujarat", "city": "Anand", "type": "Govt"},
    {"name": "MS University Vadodara", "state": "Gujarat", "city": "Vadodara", "type": "Govt"},
    {"name": "Saurashtra University", "state": "Gujarat", "city": "Rajkot", "type": "Govt"},
    {"name": "Dhirubhai Ambani Institute of Information and Communication Technology", "state": "Gujarat", "city": "Gandhinagar", "type": "Govt"},
    
    # ===== HARYANA =====
    {"name": "National Institute of Technology Kurukshetra", "state": "Haryana", "city": "Thanesar", "type": "Govt"},
    {"name": "Indian Institute of Technology Jodhpur Extension", "state": "Haryana", "city": "Karnal", "type": "Govt"},
    {"name": "Guru Jambheshwar University", "state": "Haryana", "city": "Hisar", "type": "Govt"},
    {"name": "Kurukshetra University", "state": "Haryana", "city": "Thanesar", "type": "Govt"},
    {"name": "Maharshi Dayanand University", "state": "Haryana", "city": "Rohtak", "type": "Govt"},
    {"name": "Deenbandhu Chhotu Ram University", "state": "Haryana", "city": "Sonipat", "type": "Govt"},
    {"name": "Manav Rachna University", "state": "Haryana", "city": "Faridabad", "type": "Private"},
    {"name": "Amity University Gurugram", "state": "Haryana", "city": "Gurugram", "type": "Private"},
    {"name": "SRM University Sonepat", "state": "Haryana", "city": "Sonipat", "type": "Private"},
    {"name": "The NorthCap University", "state": "Haryana", "city": "Gurugram", "type": "Private"},
    
    # ===== HIMACHAL PRADESH =====
    {"name": "National Institute of Technology Hamirpur", "state": "Himachal Pradesh", "city": "Hamirpur", "type": "Govt"},
    {"name": "Indian Institute of Technology Mandi", "state": "Himachal Pradesh", "city": "Mandi", "type": "Govt"},
    {"name": "Himachal Pradesh University", "state": "Himachal Pradesh", "city": "Shimla", "type": "Govt"},
    {"name": "Jaypee University of Information Technology", "state": "Himachal Pradesh", "city": "Solan", "type": "Private"},
    {"name": "Shoolini University", "state": "Himachal Pradesh", "city": "Solan", "type": "Private"},
    {"name": "Chitkara University", "state": "Himachal Pradesh", "city": "Solan", "type": "Private"},
    
    # ===== JHARKHAND =====
    {"name": "Indian Institute of Technology (ISM) Dhanbad", "state": "Jharkhand", "city": "Dhanbad", "type": "Govt"},
    {"name": "National Institute of Technology Jamshedpur", "state": "Jharkhand", "city": "Jamshedpur", "type": "Govt"},
    {"name": "Birla Institute of Technology Mesra", "state": "Jharkhand", "city": "Ranchi", "type": "Deemed"},
    {"name": "Ranchi University", "state": "Jharkhand", "city": "Ranchi", "type": "Govt"},
    {"name": "Vinoba Bhave University", "state": "Jharkhand", "city": "Hazaribagh", "type": "Govt"},
    {"name": "Sido Kanhu Murmu University", "state": "Jharkhand", "city": "Dumka", "type": "Govt"},
    {"name": "Kolhan University", "state": "Jharkhand", "city": "Chaibasa", "type": "Govt"},
    
    # ===== KARNATAKA =====
    {"name": "Indian Institute of Science Bangalore", "state": "Karnataka", "city": "Bangalore", "type": "Govt"},
    {"name": "Indian Institute of Technology Dharwad", "state": "Karnataka", "city": "Dharwad", "type": "Govt"},
    {"name": "National Institute of Technology Karnataka", "state": "Karnataka", "city": "Surathkal", "type": "Govt"},
    {"name": "Bangalore University", "state": "Karnataka", "city": "Bangalore", "type": "Govt"},
    {"name": "Visvesvaraya Technological University", "state": "Karnataka", "city": "Belgaum", "type": "Govt"},
    {"name": "Manipal Academy of Higher Education", "state": "Karnataka", "city": "Manipal", "type": "Deemed"},
    {"name": "PES University", "state": "Karnataka", "city": "Bangalore", "type": "Private"},
    {"name": "RV College of Engineering", "state": "Karnataka", "city": "Bangalore", "type": "Private"},
    {"name": "BMS College of Engineering", "state": "Karnataka", "city": "Bangalore", "type": "Private"},
    {"name": "MSRIT Bangalore", "state": "Karnataka", "city": "Bangalore", "type": "Private"},
    {"name": "BMSCE Bangalore", "state": "Karnataka", "city": "Bangalore", "type": "Private"},
    {"name": "NIE Mysore", "state": "Karnataka", "city": "Mysore", "type": "Govt"},
    {"name": "SJCE Mysore", "state": "Karnataka", "city": "Mysore", "type": "Private"},
    {"name": "MIT Manipal", "state": "Karnataka", "city": "Manipal", "type": "Private"},
    {"name": "NMIT Bangalore", "state": "Karnataka", "city": "Bangalore", "type": "Private"},
    {"name": "Dayananda Sagar College of Engineering", "state": "Karnataka", "city": "Bangalore", "type": "Private"},
    {"name": "JSS Science and Technology University", "state": "Karnataka", "city": "Mysore", "type": "Private"},
    {"name": "Mangalore University", "state": "Karnataka", "city": "Mangalore", "type": "Govt"},
    {"name": "Karnatak University", "state": "Karnataka", "city": "Dharwad", "type": "Govt"},
    {"name": "Gulbarga University", "state": "Karnataka", "city": "Gulbarga", "type": "Govt"},
    
    # ===== KERALA =====
    {"name": "Indian Institute of Technology Palakkad", "state": "Kerala", "city": "Palakkad", "type": "Govt"},
    {"name": "National Institute of Technology Calicut", "state": "Kerala", "city": "Kozhikode", "type": "Govt"},
    {"name": "Cochin University of Science and Technology", "state": "Kerala", "city": "Kochi", "type": "Govt"},
    {"name": "Kerala University", "state": "Kerala", "city": "Thiruvananthapuram", "type": "Govt"},
    {"name": "Mahatma Gandhi University", "state": "Kerala", "city": "Kottayam", "type": "Govt"},
    {"name": "Calicut University", "state": "Kerala", "city": "Kozhikode", "type": "Govt"},
    {"name": "Kannur University", "state": "Kerala", "city": "Kannur", "type": "Govt"},
    {"name": "APJ Abdul Kalam Technological University", "state": "Kerala", "city": "Thiruvananthapuram", "type": "Govt"},
    {"name": "College of Engineering Trivandrum", "state": "Kerala", "city": "Thiruvananthapuram", "type": "Govt"},
    {"name": "Government Engineering College Thrissur", "state": "Kerala", "city": "Thrissur", "type": "Govt"},
    {"name": "Amrita Vishwa Vidyapeetham", "state": "Kerala", "city": "Kollam", "type": "Deemed"},
    {"name": "Rajagiri School of Engineering and Technology", "state": "Kerala", "city": "Kochi", "type": "Private"},
    
    # ===== MADHYA PRADESH =====
    {"name": "Indian Institute of Technology Indore", "state": "Madhya Pradesh", "city": "Indore", "type": "Govt"},
    {"name": "National Institute of Technology Bhopal", "state": "Madhya Pradesh", "city": "Bhopal", "type": "Govt"},
    {"name": "Maulana Azad National Institute of Technology", "state": "Madhya Pradesh", "city": "Bhopal", "type": "Govt"},
    {"name": "Indian Institute of Information Technology Gwalior", "state": "Madhya Pradesh", "city": "Gwalior", "type": "Govt"},
    {"name": "Indian Institute of Information Technology Jabalpur", "state": "Madhya Pradesh", "city": "Jabalpur", "type": "Govt"},
    {"name": "Rajiv Gandhi Proudyogiki Vishwavidyalaya", "state": "Madhya Pradesh", "city": "Bhopal", "type": "Govt"},
    {"name": "Devi Ahilya Vishwavidyalaya", "state": "Madhya Pradesh", "city": "Indore", "type": "Govt"},
    {"name": "Barkatullah University", "state": "Madhya Pradesh", "city": "Bhopal", "type": "Govt"},
    {"name": "Jiwaji University", "state": "Madhya Pradesh", "city": "Gwalior", "type": "Govt"},
    {"name": "Rani Durgavati University", "state": "Madhya Pradesh", "city": "Jabalpur", "type": "Govt"},
    {"name": "Vikram University", "state": "Madhya Pradesh", "city": "Ujjain", "type": "Govt"},
    {"name": "Sagar University", "state": "Madhya Pradesh", "city": "Sagar", "type": "Govt"},
    
    # ===== MAHARASHTRA =====
    {"name": "Indian Institute of Technology Bombay", "state": "Maharashtra", "city": "Mumbai", "type": "Govt"},
    {"name": "Indian Institute of Technology Nagpur", "state": "Maharashtra", "city": "Nagpur", "type": "Govt"},
    {"name": "Veermata Jijabai Technological Institute", "state": "Maharashtra", "city": "Mumbai", "type": "Govt"},
    {"name": "Institute of Chemical Technology Mumbai", "state": "Maharashtra", "city": "Mumbai", "type": "Govt"},
    {"name": "College of Engineering Pune", "state": "Maharashtra", "city": "Pune", "type": "Govt"},
    {"name": "Visvesvaraya National Institute of Technology", "state": "Maharashtra", "city": "Nagpur", "type": "Govt"},
    {"name": "Mumbai University", "state": "Maharashtra", "city": "Mumbai", "type": "Govt"},
    {"name": "Savitribai Phule Pune University", "state": "Maharashtra", "city": "Pune", "type": "Govt"},
    {"name": "Nagpur University", "state": "Maharashtra", "city": "Nagpur", "type": "Govt"},
    {"name": "Shivaji University", "state": "Maharashtra", "city": "Kolhapur", "type": "Govt"},
    {"name": "North Maharashtra University", "state": "Maharashtra", "city": "Jalgaon", "type": "Govt"},
    {"name": "Dr. Babasaheb Ambedkar Technological University", "state": "Maharashtra", "city": "Lonere", "type": "Govt"},
    {"name": "Walchand College of Engineering", "state": "Maharashtra", "city": "Sangli", "type": "Govt"},
    {"name": "Government College of Engineering Aurangabad", "state": "Maharashtra", "city": "Aurangabad", "type": "Govt"},
    {"name": "BITS Pilani Goa Campus", "state": "Maharashtra", "city": "Sanquelim", "type": "Private"},
    {"name": "MIT World Peace University", "state": "Maharashtra", "city": "Pune", "type": "Private"},
    {"name": "Symbiosis Institute of Technology", "state": "Maharashtra", "city": "Pune", "type": "Private"},
    {"name": "VIT Pune", "state": "Maharashtra", "city": "Pune", "type": "Private"},
    {"name": "Sinhgad College of Engineering", "state": "Maharashtra", "city": "Pune", "type": "Private"},
    {"name": "Cummins College of Engineering", "state": "Maharashtra", "city": "Pune", "type": "Private"},
    {"name": "PICT Pune", "state": "Maharashtra", "city": "Pune", "type": "Private"},
    {"name": "DJ Sanghvi College of Engineering", "state": "Maharashtra", "city": "Mumbai", "type": "Private"},
    {"name": "KJ Somaiya College of Engineering", "state": "Maharashtra", "city": "Mumbai", "type": "Private"},
    {"name": "Thadomal Shahani Engineering College", "state": "Maharashtra", "city": "Mumbai", "type": "Private"},
    {"name": "SPIT Mumbai", "state": "Maharashtra", "city": "Mumbai", "type": "Private"},
    
    # ===== MANIPUR =====
    {"name": "National Institute of Technology Manipur", "state": "Manipur", "city": "Imphal", "type": "Govt"},
    {"name": "Manipur University", "state": "Manipur", "city": "Imphal", "type": "Govt"},
    {"name": "Manipur Technical University", "state": "Manipur", "city": "Imphal", "type": "Govt"},
    
    # ===== MEGHALAYA =====
    {"name": "National Institute of Technology Meghalaya", "state": "Meghalaya", "city": "Shillong", "type": "Govt"},
    {"name": "North-Eastern Hill University", "state": "Meghalaya", "city": "Shillong", "type": "Govt"},
    
    # ===== MIZORAM =====
    {"name": "National Institute of Technology Mizoram", "state": "Mizoram", "city": "Aizawl", "type": "Govt"},
    {"name": "Mizoram University", "state": "Mizoram", "city": "Aizawl", "type": "Govt"},
    
    # ===== NAGALAND =====
    {"name": "National Institute of Technology Nagaland", "state": "Nagaland", "city": "Dimapur", "type": "Govt"},
    {"name": "Nagaland University", "state": "Nagaland", "city": "Kohima", "type": "Govt"},
    
    # ===== ODISHA =====
    {"name": "Indian Institute of Technology Bhubaneswar", "state": "Odisha", "city": "Bhubaneswar", "type": "Govt"},
    {"name": "National Institute of Technology Rourkela", "state": "Odisha", "city": "Rourkela", "type": "Govt"},
    {"name": "International Institute of Information Technology Bhubaneswar", "state": "Odisha", "city": "Bhubaneswar", "type": "Govt"},
    {"name": "Utkal University", "state": "Odisha", "city": "Bhubaneswar", "type": "Govt"},
    {"name": "Sambalpur University", "state": "Odisha", "city": "Sambalpur", "type": "Govt"},
    {"name": "Berhampur University", "state": "Odisha", "city": "Berhampur", "type": "Govt"},
    {"name": "College of Engineering and Technology Bhubaneswar", "state": "Odisha", "city": "Bhubaneswar", "type": "Govt"},
    {"name": "VSSUT Burla", "state": "Odisha", "city": "Sambalpur", "type": "Govt"},
    {"name": "SOA University", "state": "Odisha", "city": "Bhubaneswar", "type": "Deemed"},
    {"name": "KIIT University", "state": "Odisha", "city": "Bhubaneswar", "type": "Deemed"},
    
    # ===== PUNJAB =====
    {"name": "Indian Institute of Technology Ropar", "state": "Punjab", "city": "Rupnagar", "type": "Govt"},
    {"name": "Thapar Institute of Engineering and Technology", "state": "Punjab", "city": "Patiala", "type": "Deemed"},
    {"name": "Panjab University", "state": "Punjab", "city": "Chandigarh", "type": "Govt"},
    {"name": "Punjab Engineering College", "state": "Punjab", "city": "Chandigarh", "type": "Govt"},
    {"name": "Punjab University", "state": "Punjab", "city": "Patiala", "type": "Govt"},
    {"name": "Guru Nanak Dev University", "state": "Punjab", "city": "Amritsar", "type": "Govt"},
    {"name": "Punjabi University", "state": "Punjab", "city": "Patiala", "type": "Govt"},
    {"name": "Sant Longowal Institute of Engineering and Technology", "state": "Punjab", "city": "Sangrur", "type": "Govt"},
    {"name": "Lovely Professional University", "state": "Punjab", "city": "Phagwara", "type": "Private"},
    {"name": "Chitkara University Punjab", "state": "Punjab", "city": "Rajpura", "type": "Private"},
    
    # ===== RAJASTHAN =====
    {"name": "Indian Institute of Technology Jodhpur", "state": "Rajasthan", "city": "Jodhpur", "type": "Govt"},
    {"name": "Birla Institute of Technology and Science Pilani", "state": "Rajasthan", "city": "Pilani", "type": "Deemed"},
    {"name": "Malaviya National Institute of Technology Jaipur", "state": "Rajasthan", "city": "Jaipur", "type": "Govt"},
    {"name": "National Institute of Technology Jaipur", "state": "Rajasthan", "city": "Jaipur", "type": "Govt"},
    {"name": "Rajasthan Technical University", "state": "Rajasthan", "city": "Kota", "type": "Govt"},
    {"name": "University of Rajasthan", "state": "Rajasthan", "city": "Jaipur", "type": "Govt"},
    {"name": "Jai Narain Vyas University", "state": "Rajasthan", "city": "Jodhpur", "type": "Govt"},
    {"name": "Maharana Pratap University of Agriculture and Technology", "state": "Rajasthan", "city": "Udaipur", "type": "Govt"},
    {"name": "Mohanlal Sukhadia University", "state": "Rajasthan", "city": "Udaipur", "type": "Govt"},
    {"name": "Banasthali Vidyapith", "state": "Rajasthan", "city": "Tonk", "type": "Deemed"},
    {"name": "LNM Institute of Information Technology", "state": "Rajasthan", "city": "Jaipur", "type": "Deemed"},
    {"name": "Manipal University Jaipur", "state": "Rajasthan", "city": "Jaipur", "type": "Private"},
    
    # ===== SIKKIM =====
    {"name": "National Institute of Technology Sikkim", "state": "Sikkim", "city": "Ravangla", "type": "Govt"},
    {"name": "Sikkim Manipal University", "state": "Sikkim", "city": "Gangtok", "type": "Private"},
    {"name": "Sikkim University", "state": "Sikkim", "city": "Gangtok", "type": "Govt"},
    
    # ===== TAMIL NADU =====
    {"name": "Indian Institute of Technology Madras", "state": "Tamil Nadu", "city": "Chennai", "type": "Govt"},
    {"name": "National Institute of Technology Tiruchirappalli", "state": "Tamil Nadu", "city": "Tiruchirappalli", "type": "Govt"},
    {"name": "Anna University", "state": "Tamil Nadu", "city": "Chennai", "type": "Govt"},
    {"name": "Vellore Institute of Technology", "state": "Tamil Nadu", "city": "Vellore", "type": "Deemed"},
    {"name": "SRM Institute of Science and Technology", "state": "Tamil Nadu", "city": "Chennai", "type": "Deemed"},
    {"name": "PSG College of Technology", "state": "Tamil Nadu", "city": "Coimbatore", "type": "Private"},
    {"name": "Coimbatore Institute of Technology", "state": "Tamil Nadu", "city": "Coimbatore", "type": "Private"},
    {"name": "College of Engineering Guindy", "state": "Tamil Nadu", "city": "Chennai", "type": "Govt"},
    {"name": "Madras Institute of Technology", "state": "Tamil Nadu", "city": "Chennai", "type": "Govt"},
    {"name": "Thiagarajar College of Engineering", "state": "Tamil Nadu", "city": "Madurai", "type": "Private"},
    {"name": "SSN College of Engineering", "state": "Tamil Nadu", "city": "Chennai", "type": "Private"},
    {"name": "Amrita Vishwa Vidyapeetham Coimbatore", "state": "Tamil Nadu", "city": "Coimbatore", "type": "Deemed"},
    {"name": "Kalasalingam Academy of Research and Education", "state": "Tamil Nadu", "city": "Virudhunagar", "type": "Deemed"},
    {"name": "Bharathiar University", "state": "Tamil Nadu", "city": "Coimbatore", "type": "Govt"},
    {"name": "Madurai Kamaraj University", "state": "Tamil Nadu", "city": "Madurai", "type": "Govt"},
    {"name": "Bharathidasan University", "state": "Tamil Nadu", "city": "Tiruchirappalli", "type": "Govt"},
    {"name": "Karunya Institute of Technology", "state": "Tamil Nadu", "city": "Coimbatore", "type": "Deemed"},
    {"name": "Sathyabama Institute of Science and Technology", "state": "Tamil Nadu", "city": "Chennai", "type": "Deemed"},
    
    # ===== TELANGANA =====
    {"name": "Indian Institute of Technology Hyderabad", "state": "Telangana", "city": "Hyderabad", "type": "Govt"},
    {"name": "National Institute of Technology Warangal", "state": "Telangana", "city": "Warangal", "type": "Govt"},
    {"name": "International Institute of Information Technology Hyderabad", "state": "Telangana", "city": "Hyderabad", "type": "Govt"},
    {"name": "Osmania University", "state": "Telangana", "city": "Hyderabad", "type": "Govt"},
    {"name": "Jawaharlal Nehru Technological University Hyderabad", "state": "Telangana", "city": "Hyderabad", "type": "Govt"},
    {"name": "University of Hyderabad", "state": "Telangana", "city": "Hyderabad", "type": "Govt"},
    {"name": "Kakatiya University", "state": "Telangana", "city": "Warangal", "type": "Govt"},
    {"name": "CBIT Hyderabad", "state": "Telangana", "city": "Hyderabad", "type": "Private"},
    {"name": "Vasavi College of Engineering", "state": "Telangana", "city": "Hyderabad", "type": "Private"},
    {"name": "BVRIT Hyderabad", "state": "Telangana", "city": "Hyderabad", "type": "Private"},
    {"name": "MGIT Hyderabad", "state": "Telangana", "city": "Hyderabad", "type": "Private"},
    {"name": "CVR College of Engineering", "state": "Telangana", "city": "Hyderabad", "type": "Private"},
    {"name": "MVSR Engineering College", "state": "Telangana", "city": "Hyderabad", "type": "Private"},
    
    # ===== TRIPURA =====
    {"name": "National Institute of Technology Agartala", "state": "Tripura", "city": "Agartala", "type": "Govt"},
    {"name": "Tripura University", "state": "Tripura", "city": "Agartala", "type": "Govt"},
    
    # ===== UTTAR PRADESH =====
    {"name": "Indian Institute of Technology Kanpur", "state": "Uttar Pradesh", "city": "Kanpur", "type": "Govt"},
    {"name": "Indian Institute of Technology BHU", "state": "Uttar Pradesh", "city": "Varanasi", "type": "Govt"},
    {"name": "Motilal Nehru National Institute of Technology Allahabad", "state": "Uttar Pradesh", "city": "Allahabad", "type": "Govt"},
    {"name": "Indian Institute of Information Technology Allahabad", "state": "Uttar Pradesh", "city": "Allahabad", "type": "Govt"},
    {"name": "Aligarh Muslim University", "state": "Uttar Pradesh", "city": "Aligarh", "type": "Govt"},
    {"name": "Banaras Hindu University", "state": "Uttar Pradesh", "city": "Varanasi", "type": "Govt"},
    {"name": "Harcourt Butler Technical University", "state": "Uttar Pradesh", "city": "Kanpur", "type": "Govt"},
    {"name": "Lucknow University", "state": "Uttar Pradesh", "city": "Lucknow", "type": "Govt"},
    {"name": "Dr. APJ Abdul Kalam Technical University", "state": "Uttar Pradesh", "city": "Lucknow", "type": "Govt"},
    {"name": "KNIT Sultanpur", "state": "Uttar Pradesh", "city": "Sultanpur", "type": "Govt"},
    {"name": "Agra University", "state": "Uttar Pradesh", "city": "Agra", "type": "Govt"},
    {"name": "Allahabad University", "state": "Uttar Pradesh", "city": "Allahabad", "type": "Govt"},
    {"name": "Jamia Millia Islamia", "state": "Uttar Pradesh", "city": "Noida", "type": "Govt"},
    {"name": "Amity University Noida", "state": "Uttar Pradesh", "city": "Noida", "type": "Private"},
    {"name": "Sharda University", "state": "Uttar Pradesh", "city": "Noida", "type": "Private"},
    {"name": "JSS Academy of Technical Education", "state": "Uttar Pradesh", "city": "Noida", "type": "Private"},
    {"name": "KIET Group of Institutions", "state": "Uttar Pradesh", "city": "Ghaziabad", "type": "Private"},
    {"name": "ABES Engineering College", "state": "Uttar Pradesh", "city": "Ghaziabad", "type": "Private"},
    {"name": "Gautam Buddha University", "state": "Uttar Pradesh", "city": "Noida", "type": "Govt"},
    
    # ===== UTTARAKHAND =====
    {"name": "Indian Institute of Technology Roorkee", "state": "Uttarakhand", "city": "Roorkee", "type": "Govt"},
    {"name": "National Institute of Technology Uttarakhand", "state": "Uttarakhand", "city": "Pauri", "type": "Govt"},
    {"name": "Govind Ballabh Pant University of Agriculture and Technology", "state": "Uttarakhand", "city": "Rudrapur", "type": "Govt"},
    {"name": "Hemvati Nandan Bahuguna Garhwal University", "state": "Uttarakhand", "city": "Pauri", "type": "Govt"},
    {"name": "Kumaun University", "state": "Uttarakhand", "city": "Nainital", "type": "Govt"},
    {"name": "Graphic Era University", "state": "Uttarakhand", "city": "Dehradun", "type": "Deemed"},
    {"name": "DIT University", "state": "Uttarakhand", "city": "Dehradun", "type": "Private"},
    {"name": "University of Petroleum and Energy Studies", "state": "Uttarakhand", "city": "Dehradun", "type": "Private"},
    
    # ===== WEST BENGAL =====
    {"name": "Indian Institute of Technology Kharagpur", "state": "West Bengal", "city": "Kharagpur", "type": "Govt"},
    {"name": "National Institute of Technology Durgapur", "state": "West Bengal", "city": "Durgapur", "type": "Govt"},
    {"name": "Jadavpur University", "state": "West Bengal", "city": "Kolkata", "type": "Govt"},
    {"name": "Calcutta University", "state": "West Bengal", "city": "Kolkata", "type": "Govt"},
    {"name": "Indian Institute of Engineering Science and Technology", "state": "West Bengal", "city": "Howrah", "type": "Govt"},
    {"name": "Bengal Engineering and Science University", "state": "West Bengal", "city": "Howrah", "type": "Govt"},
    {"name": "West Bengal University of Technology", "state": "West Bengal", "city": "Kolkata", "type": "Govt"},
    {"name": "Kalyani Government Engineering College", "state": "West Bengal", "city": "Kalyani", "type": "Govt"},
    {"name": "Heritage Institute of Technology", "state": "West Bengal", "city": "Kolkata", "type": "Private"},
    {"name": "Techno India University", "state": "West Bengal", "city": "Kolkata", "type": "Private"},
    {"name": "North Bengal University", "state": "West Bengal", "city": "Siliguri", "type": "Govt"},
    {"name": "Vidyasagar University", "state": "West Bengal", "city": "Medinipur", "type": "Govt"},
    
    # ===== DELHI =====
    {"name": "Indian Institute of Technology Delhi", "state": "Delhi", "city": "New Delhi", "type": "Govt"},
    {"name": "Delhi Technological University", "state": "Delhi", "city": "New Delhi", "type": "Govt"},
    {"name": "Netaji Subhas University of Technology", "state": "Delhi", "city": "New Delhi", "type": "Govt"},
    {"name": "Indraprastha Institute of Information Technology", "state": "Delhi", "city": "New Delhi", "type": "Govt"},
    {"name": "University of Delhi", "state": "Delhi", "city": "New Delhi", "type": "Govt"},
    {"name": "Jawaharlal Nehru University", "state": "Delhi", "city": "New Delhi", "type": "Govt"},
    {"name": "Jamia Millia Islamia University", "state": "Delhi", "city": "New Delhi", "type": "Govt"},
    {"name": "Indira Gandhi Delhi Technical University for Women", "state": "Delhi", "city": "New Delhi", "type": "Govt"},
    
    # ===== UNION TERRITORIES =====
    {"name": "Pondicherry University", "state": "Puducherry", "city": "Puducherry", "type": "Govt"},
    {"name": "Pondicherry Engineering College", "state": "Puducherry", "city": "Puducherry", "type": "Govt"},
    {"name": "National Institute of Technology Puducherry", "state": "Puducherry", "city": "Karaikal", "type": "Govt"},
    {"name": "University of Jammu", "state": "Jammu and Kashmir", "city": "Jammu", "type": "Govt"},
    {"name": "National Institute of Technology Srinagar", "state": "Jammu and Kashmir", "city": "Srinagar", "type": "Govt"},
    {"name": "Islamic University of Science and Technology", "state": "Jammu and Kashmir", "city": "Pulwama", "type": "Govt"},
    {"name": "Central University of Kashmir", "state": "Jammu and Kashmir", "city": "Srinagar", "type": "Govt"},
    {"name": "University of Kashmir", "state": "Jammu and Kashmir", "city": "Srinagar", "type": "Govt"},
]

# ==================== HELPER FUNCTIONS ====================

def get_colleges_by_state(state):
    """Return all colleges in a specific state"""
    return [college for college in COLLEGES if college["state"] == state]

def get_colleges_by_city(city):
    """Return all colleges in a specific city"""
    return [college for college in COLLEGES if college["city"] == city]

def get_colleges_by_type(college_type):
    """Return all colleges of a specific type (Govt/Private/Deemed)"""
    return [college for college in COLLEGES if college["type"] == college_type]

def get_college_names():
    """Return list of all college names"""
    return [college["name"] for college in COLLEGES]

def get_college_count_by_state():
    """Return dictionary with state-wise college count"""
    state_count = {}
    for college in COLLEGES:
        state = college["state"]
        state_count[state] = state_count.get(state, 0) + 1
    return state_count

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
