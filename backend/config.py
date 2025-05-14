property_list = [
    {
        "name": "Is on Registry",
        "id": 82001,
        "parameters": {"Registry ID": "", "Registry Grouper": ""},
        "selector": {
            "1": "Present and active in any of the specified registries",
            "2": "Absent or inactive in all of the specified registries",
            "null": "Missing/invalid parameters or called from inclusion rule"
        },
        "database": "Generic Patient Database (EPT)",
        "function": "$$IsOnRegistry^BIMPATDATA()",
        "data_type": "Category - YES AND NO (I ECT 100)",
        "description": "Determines whether a record/contact is present and active in any of the specified registries."
    },
    {
        "name": "Is On Health Maintenance Modifier",
        "id": 82264,
        "parameters": {"HM modifiers": ""},
        "selector": {
            "1": "Patient is on at least one given HM modifier",
            "2": "Patient is not on any of the given HM modifiers"
        },
        "data_type": "String",
        "description": "Checks whether a patient is on at least one of the given Health Maintenance Modifiers."
    },
    {
        "name": "Was Problem Active in Problem List During Dates",
        "id": 82013,
        "parameters": {
            "Grouper ID": "", "Look Back Period": "", "Start Date": "", "Search Period Filter Rule": ""
        },
        "selector": {
            "1": "Match found in patient's active problem list during specified period",
            "2": "No match found"
        },
        "database": "Generic Patient Database (EPT)",
        "function": "$$WasInProblemList^BIMDXDATA()",
        "data_type": "Category - YES AND NO (I ECT 100)",
        "description": "Checks for matching diagnoses in the problem list active during a specific date range."
    },
    {
        "name": "Last Encounter Date for Diagnosis",
        "id": 82274,
        "parameters": {
            "Diagnosis Grouper ID": "", "Encounter Types to Include": "", "Encounter Types to Exclude": "",
            "Appointment Statuses to Include": "", "Appointment Statuses to Exclude": "",
            "Department Grouper to Include": "", "Department Grouper to Exclude": "",
            "Look Back Period": "", "Start Date": "", "Encounter Rule Filter": "",
            "Compare Diagnosis Code as of Encounter Date?": "", "Search Period Filter Rule": "",
            "Primary Diagnosis Only?": "", "Days Back to Consider Unterminated Encounters as Ongoing": "",
            "Unterminated Encounter Default Length": ""
        },
        "selector": {
            "value": "Most recent qualifying encounter date, or null if none match"
        },
        "database": "Generic Patient Database (EPT)",
        "function": "$$GetEncDate^BIMDXDATA()",
        "data_type": "Date",
        "description": "Returns the latest encounter date that matches diagnosis and encounter criteria."
    },
    {
        "name": "Last Invoice Date For Diagnosis",
        "id": 82029,
        "parameters": {
            "Allowed Diagnoses": "", "Payor": "", "Plan": "", "Procedure Category": "",
            "Minimum Number Of Matches": "", "Look Back Period": "", "Start Date": "",
            "Encounter Contact Filter": "", "Use Invoice ICD Code": "", "Search Period Filter Rule": ""
        },
        "selector": {
            "value": "Most recent accepted/closed invoice date matching criteria, or null if none"
        },
        "database": "Generic Patient Database (EPT)",
        "function": "$$GetInvDXDate^BIMDXDATA()",
        "data_type": "Date",
        "description": "Returns date of latest invoice with a matching diagnosis, if any."
    },
    {
        "name": "Always One",
        "id": 75000,
        "parameters": {},
        "selector": {
            "1": "Always returns 1"
        },
        "function": "1",
        "data_type": "Numeric",
        "description": "Always returns 1; used to force conditionals to always evaluate as true."
    }
]
