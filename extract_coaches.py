import csv

print("Analyzing coach nationalities...")

# 1. Read your file (change the filename here if yours is named differently)
file_name = 'fifa squad 2026.txt' 
with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 2. A list of known foreign identifiers to watch out for
foreign_identifiers = [
    "Belgium", "Belgian", "Argentina", "Argentine", "Spain", "Spanish",
    "France", "French", "Germany", "German", "Italy", "Italian",
    "Netherlands", "Dutch", "Portugal", "Portuguese", "Brazil", "Brazilian",
    "Colombia", "Colombian", "Uruguay", "Uruguayan", "Croatia", "Croatian",
    "England", "English", "Serbia", "Serbian", "Switzerland", "Swiss",
    "Sweden", "Swedish", "Scotland", "Scottish", "Mexico", "Mexican"
]

teams = [
    "Czech Republic", "Mexico", "South Africa", "South Korea", "Bosnia and Herzegovina",
    "Canada", "Qatar", "Switzerland", "Brazil", "Haiti", "Morocco", "Scotland",
    "Australia", "Paraguay", "Turkey", "United States", "Curaçao", "Ecuador",
    "Germany", "Ivory Coast", "Japan", "Netherlands", "Sweden", "Tunisia",
    "Belgium", "Egypt", "Iran", "New Zealand", "Cape Verde", "Saudi Arabia",
    "Spain", "Uruguay", "France", "Iraq", "Norway", "Senegal", "Algeria",
    "Argentina", "Austria", "Jordan", "Colombia", "DR Congo", "Portugal",
    "Uzbekistan", "Croatia", "England", "Ghana", "Panama"
]

records = []
current_team = None

# 3. Read the file line by line
for line in lines:
    line = line.strip()

    if line in teams:
        current_team = line
        continue

    # When we find a coach line
    if line.startswith("Coach:"):
        # Remove the word "Coach:"
        raw_coach_text = line.replace("Coach:", "").strip()

        # Default assumption: The coach is Local (1)
        is_local = 1
        coach_nationality = current_team
        coach_name = raw_coach_text

        # Check if the text starts with any of our foreign identifiers
        for identifier in foreign_identifiers:
            if raw_coach_text.startswith(identifier + " "):
                is_local = 0  # Change to Foreign (0)
                coach_nationality = identifier  # Record their actual nationality
                # Remove the country name from their personal name
                coach_name = raw_coach_text.replace(identifier + " ", "").strip()
                break

        # Add to our master list
        records.append({
            "Team": current_team,
            "Coach Name": coach_name,
            "Coach Nationality": coach_nationality,
            "Is_Local_Coach": is_local
        })

print(f"Extracted {len(records)} coaches. Saving to CSV...")

# 4. Save to a new CSV file
headers = ["Team", "Coach Name", "Coach Nationality", "Is_Local_Coach"]

with open('coach_analysis.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(records)

print("Success! Your predictive analysis file 'coach_analysis.csv' is ready.")