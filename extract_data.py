import re
import csv

print("Reading the text file...")

# 1. Read the text file containing the Wikipedia data
with open('fifa squad 2026.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

records = []
current_team = None

# A list to help the script separate the League name from the Club name
leagues_keywords = [
    "Royal Dutch Football Association", "Football Association of the Czech Republic", "German Football Association",
    "The Football Association", "French Football Federation", "Portuguese Football Federation", "Mexican Football Federation",
    "Hellenic Football Federation", "Russian Football Union", "Turkish Football Federation", "Italian Football Federation",
    "Royal Spanish Football Federation", "Cyprus Football Association", "Saudi Arabian Football Federation",
    "Royal Belgian Football Association", "South African Football Association", "United States Soccer Federation",
    "Norwegian Football Federation", "Japan Football Association", "Danish Football Association", "Korea Football Association",
    "Austrian Football Association", "Chinese Football Association", "Scottish Football Association", "Football Association of Wales",
    "Football Association of Serbia", "Football Association of Bosnia and Herzegovina", "Kazakhstan Football Federation",
    "Croatian Football Federation", "Romanian Football Federation", "Canadian Soccer Association", "Qatar Football Association",
    "Swiss Football Association", "Brazilian Football Confederation", "Haitian Football Federation", "Hungarian Football Federation",
    "Slovak Football Association", "United Arab Emirates Football Association", "Royal Moroccan Football Federation",
    "Egyptian Football Association", "Football Australia", "Argentine Football Association", "Paraguayan Football Association",
    "Ecuadorian Football Federation", "Football Association of Slovenia", "Swedish Football Association", "Tunisian Football Federation",
    "Iraq Football Association", "Football Association of Thailand", "Uzbekistan Football Association", "Football Association of Indonesia",
    "Bulgarian Football Union", "Football Association of Ireland", "Ghana Football Association", "Football Association of Finland",
    "Israel Football Association", "New Zealand Football", "National Autonomous Federation of Football of Honduras",
    "Venezuelan Football Federation", "Panamanian Football Federation", "Football Federation of Chile", "Association of Football Federations of Azerbaijan",
    "Football Federation Islamic Republic of Iran", "Football Federation of Armenia"
]

# The list of teams to look for in the text
team_names = [
    "Czech Republic", "Mexico", "South Africa", "South Korea", "Bosnia and Herzegovina", "Canada", "Qatar", "Switzerland",
    "Brazil", "Haiti", "Morocco", "Scotland", "Australia", "Paraguay", "Turkey", "United States", "Curaçao", "Ecuador",
    "Germany", "Ivory Coast", "Japan", "Netherlands", "Sweden", "Tunisia", "Belgium", "Egypt", "Iran", "New Zealand",
    "Cape Verde", "Saudi Arabia", "Spain", "Uruguay", "France", "Iraq", "Norway", "Senegal", "Algeria", "Argentina",
    "Austria", "Jordan", "Colombia", "DR Congo", "Portugal", "Uzbekistan", "Croatia", "England", "Ghana", "Panama"
]

# The Regex pattern that identifies a player row
player_pattern = re.compile(r'^(\d+)\s+(GK|DF|MF|FW)\s+(.*?)\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).*?\(aged\s+(\d+)\)\s+(\d+)\s+(\d+)\s+(.*)$')

# 2. Extract the data line by line
for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # If the line is a country name, set it as the current active team
    if line in team_names:
        current_team = line
        continue
    
    # If the line looks like a player, extract their details
    match = player_pattern.match(line)
    if match and current_team:
        p_id, pos, player, age, caps, goals, club_str = match.groups()
        
        # Clean the player name (remove the word 'captain' if it's there)
        player = re.sub(r'\(captain\)', '', player, flags=re.IGNORECASE).strip()
        
        # Split the long string into League and Club
        league = ""
        club = club_str
        for l_kw in leagues_keywords:
            if club_str.startswith(l_kw):
                league = l_kw
                club = club_str[len(l_kw):].strip()
                break
        
        # Add the clean player to our master list
        records.append({
            "ID": p_id, "Team": current_team, "Position": pos, "Player": player,
            "Age": age, "Caps": caps, "Goals": goals, "WC Goals": "0",
            "League": league, "Club": club
        })

print(f"Extracted {len(records)} players. Saving to CSV...")

# 3. Save the final output as a CSV file
headers = ["ID", "Team", "Position", "Player", "Age", "Caps", "Goals", "WC Goals", "League", "Club"]

with open('extracted_world_cup_rosters.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(records)

print("Success! Your file 'extracted_world_cup_rosters.csv' is ready.")