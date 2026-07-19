import html

# ==========================================
# 1. DATASETS DEFINITIONS
# ==========================================

zodiac_sanskrit_absolute = [
    {
        "name": "Aries / Mesha", "range": "0° to 30°", "grid_pos": (1, 0),
        "padams": [
            ("Ashwini 1", "0° 00'"), ("Ashwini 2", "3° 20'"), ("Ashwini 3", "6° 40'"), ("Ashwini 4", "10° 00'"),
            ("Bharani 1", "13° 20'"), ("Bharani 2", "16° 40'"), ("Bharani 3", "20° 00'"), ("Bharani 4", "23° 20'"),
            ("Krittika 1", "26° 40'")
        ]
    },
    {
        "name": "Taurus / Vrishabha", "range": "30° to 60°", "grid_pos": (2, 0),
        "padams": [
            ("Krittika 2", "30° 00'"), ("Krittika 3", "33° 20'"), ("Krittika 4", "36° 40'"),
            ("Rohini 1", "40° 00'"), ("Rohini 2", "43° 20'"), ("Rohini 3", "46° 40'"), ("Rohini 4", "50° 00'"),
            ("Mrigashira 1", "53° 20'"), ("Mrigashira 2", "56° 40'")
        ]
    },
    {
        "name": "Gemini / Mithuna", "range": "60° to 90°", "grid_pos": (3, 0),
        "padams": [
            ("Mrigashira 3", "60° 00'"), ("Mrigashira 4", "63° 20'"),
            ("Ardra 1", "66° 40'"), ("Ardra 2", "70° 00'"), ("Ardra 3", "73° 20'"), ("Ardra 4", "76° 40'"),
            ("Punarvasu 1", "80° 00'"), ("Punarvasu 2", "83° 20'"), ("Punarvasu 3", "86° 40'")
        ]
    },
    {
        "name": "Cancer / Karka", "range": "90° to 120°", "grid_pos": (3, 1),
        "padams": [
            ("Punarvasu 4", "90° 00'"),
            ("Pushya 1", "93° 20'"), ("Pushya 2", "96° 40'"), ("Pushya 3", "100° 00'"), ("Pushya 4", "103° 20'"),
            ("Ashlesha 1", "106° 40'"), ("Ashlesha 2", "110° 00'"), ("Ashlesha 3", "113° 20'"), ("Ashlesha 4", "116° 40'")
        ]
    },
    {
        "name": "Leo / Simha", "range": "120° to 150°", "grid_pos": (3, 2),
        "padams": [
            ("Magha 1", "120° 00'"), ("Magha 2", "123° 20'"), ("Magha 3", "126° 40'"), ("Magha 4", "130° 00'"),
            ("Purva Phalguni 1", "133° 20'"), ("Purva Phalguni 2", "136° 40'"), ("Purva Phalguni 3", "140° 00'"), ("Purva Phalguni 4", "143° 20'"),
            ("Uttara Phalguni 1", "146° 40'")
        ]
    },
    {
        "name": "Virgo / Kanya", "range": "150° to 180°", "grid_pos": (3, 3),
        "padams": [
            ("Uttara Phalguni 2", "150° 00'"), ("Uttara Phalguni 3", "153° 20'"), ("Uttara Phalguni 4", "156° 40'"),
            ("Hasta 1", "160° 00'"), ("Hasta 2", "163° 20'"), ("Hasta 3", "166° 40'"), ("Hasta 4", "170° 00'"),
            ("Chitra 1", "173° 20'"), ("Chitra 2", "176° 40'")
        ]
    },
    {
        "name": "Libra / Tula", "range": "180° to 210°", "grid_pos": (2, 3),
        "padams": [
            ("Chitra 3", "180° 00'"), ("Chitra 4", "183° 20'"),
            ("Swati 1", "186° 40'"), ("Swati 2", "190° 00'"), ("Swati 3", "193° 20'"), ("Swati 4", "196° 40'"),
            ("Vishakha 1", "200° 00'"), ("Vishakha 2", "203° 20'"), ("Vishakha 3", "206° 40'")
        ]
    },
    {
        "name": "Scorpio / Vrishchika", "range": "210° to 240°", "grid_pos": (1, 3),
        "padams": [
            ("Vishakha 4", "210° 00'"),
            ("Anuradha 1", "213° 20'"), ("Anuradha 2", "216° 40'"), ("Anuradha 3", "220° 00'"), ("Anuradha 4", "223° 20'"),
            ("Jyeshtha 1", "226° 40'"), ("Jyeshtha 2", "230° 00'"), ("Jyeshtha 3", "233° 20'"), ("Jyeshtha 4", "236° 40'")
        ]
    },
    {
        "name": "Sagittarius / Dhanu", "range": "240° to 270°", "grid_pos": (0, 3),
        "padams": [
            ("Mula 1", "240° 00'"), ("Mula 2", "243° 20'"), ("Mula 3", "246° 40'"), ("Mula 4", "250° 00'"),
            ("Purva Ashadha 1", "253° 20'"), ("Purva Ashadha 2", "256° 40'"), ("Purva Ashadha 3", "260° 00'"), ("Purva Ashadha 4", "263° 20'"),
            ("Uttara Ashadha 1", "266° 40'")
        ]
    },
    {
        "name": "Capricorn / Makara", "range": "270° to 300°", "grid_pos": (0, 2),
        "padams": [
            ("Uttara Ashadha 2", "270° 00'"), ("Uttara Ashadha 3", "273° 20'"), ("Uttara Ashadha 4", "276° 40'"),
            ("Shravana 1", "280° 00'"), ("Shravana 2", "283° 20'"), ("Shravana 3", "286° 40'"), ("Shravana 4", "290° 00'"),
            ("Dhanishta 1", "293° 20'"), ("Dhanishta 2", "296° 40'")
        ]
    },
    {
        "name": "Aquarius / Kumbha", "range": "300° to 330°", "grid_pos": (0, 1),
        "padams": [
            ("Dhanishta 3", "300° 00'"), ("Dhanishta 4", "303° 20'"),
            ("Shatabhisha 1", "306° 40'"), ("Shatabhisha 2", "310° 00'"), ("Shatabhisha 3", "313° 20'"), ("Shatabhisha 4", "316° 40'"),
            ("Purva Bhadrapada 1", "320° 00'"), ("Purva Bhadrapada 2", "323° 20'"), ("Purva Bhadrapada 3", "326° 40'")
        ]
    },
    {
        "name": "Pisces / Meena", "range": "330° to 360°", "grid_pos": (0, 0),
        "padams": [
            ("Purva Bhadrapada 4", "330° 00'"),
            ("Uttara Bhadrapada 1", "333° 20'"), ("Uttara Bhadrapada 2", "336° 40'"), ("Uttara Bhadrapada 3", "340° 00'"), ("Uttara Bhadrapada 4", "343° 20'"),
            ("Revati 1", "346° 40'"), ("Revati 2", "350° 00'"), ("Revati 3", "353° 20'"), ("Revati 4", "356° 40'")
        ]
    }
]

zodiac_tamil_absolute = [
    {
        "name": "Aries / Mesham", "range": "0° to 30°", "grid_pos": (1, 0),
        "padams": [
            ("Ashwini 1", "0° 00'"), ("Ashwini 2", "3° 20'"), ("Ashwini 3", "6° 40'"), ("Ashwini 4", "10° 00'"),
            ("Bharani 1", "13° 20'"), ("Bharani 2", "16° 40'"), ("Bharani 3", "20° 00'"), ("Bharani 4", "23° 20'"),
            ("Kiruthigai 1", "26° 40'")
        ]
    },
    {
        "name": "Taurus / Rishabham", "range": "30° to 60°", "grid_pos": (2, 0),
        "padams": [
            ("Kiruthigai 2", "30° 00'"), ("Kiruthigai 3", "33° 20'"), ("Kiruthigai 4", "36° 40'"),
            ("Rohini 1", "40° 00'"), ("Rohini 2", "43° 20'"), ("Rohini 3", "46° 40'"), ("Rohini 4", "50° 00'"),
            ("Mirugaseerisham 1", "53° 20'"), ("Mirugaseerisham 2", "56° 40'")
        ]
    },
    {
        "name": "Gemini / Midhunam", "range": "60° to 90°", "grid_pos": (3, 0),
        "padams": [
            ("Mirugaseerisham 3", "60° 00'"), ("Mirugaseerisham 4", "63° 20'"),
            ("Thiruvadhirai 1", "66° 40'"), ("Thiruvadhirai 2", "70° 00'"), ("Thiruvadhirai 3", "73° 20'"), ("Thiruvadhirai 4", "76° 40'"),
            ("Punarpoosam 1", "80° 00'"), ("Punarpoosam 2", "83° 20'"), ("Punarpoosam 3", "86° 40'")
        ]
    },
    {
        "name": "Cancer / Kadagam", "range": "90° to 120°", "grid_pos": (3, 1),
        "padams": [
            ("Punarpoosam 4", "90° 00'"),
            ("Poosam 1", "93° 20'"), ("Poosam 2", "96° 40'"), ("Poosam 3", "100° 00'"), ("Poosam 4", "103° 20'"),
            ("Ayilyam 1", "106° 40'"), ("Ayilyam 2", "110° 00'"), ("Ayilyam 3", "113° 20'"), ("Ayilyam 4", "116° 40'")
        ]
    },
    {
        "name": "Leo / Simmam", "range": "120° to 150°", "grid_pos": (3, 2),
        "padams": [
            ("Magam 1", "120° 00'"), ("Magam 2", "123° 20'"), ("Magam 3", "126° 40'"), ("Magam 4", "130° 00'"),
            ("Pooram 1", "133° 20'"), ("Pooram 2", "136° 40'"), ("Pooram 3", "140° 00'"), ("Pooram 4", "143° 20'"),
            ("Uthiram 1", "146° 40'")
        ]
    },
    {
        "name": "Virgo / Kanni", "range": "150° to 180°", "grid_pos": (3, 3),
        "padams": [
            ("Uthiram 2", "150° 00'"), ("Uthiram 3", "153° 20'"), ("Uthiram 4", "156° 40'"),
            ("Hastham 1", "160° 00'"), ("Hastham 2", "163° 20'"), ("Hastham 3", "166° 40'"), ("Hastham 4", "170° 00'"),
            ("Chithirai 1", "173° 20'"), ("Chithirai 2", "176° 40'")
        ]
    },
    {
        "name": "Libra / Thulaam", "range": "180° to 210°", "grid_pos": (2, 3),
        "padams": [
            ("Chithirai 3", "180° 00'"), ("Chithirai 4", "183° 20'"),
            ("Swathi 1", "186° 40'"), ("Swathi 2", "190° 00'"), ("Swathi 3", "193° 20'"), ("Swathi 4", "196° 40'"),
            ("Visagam 1", "200° 00'"), ("Visagam 2", "203° 20'"), ("Visagam 3", "206° 40'")
        ]
    },
    {
        "name": "Scorpio / Viruchigam", "range": "210° to 240°", "grid_pos": (1, 3),
        "padams": [
            ("Visagam 4", "210° 00'"),
            ("Anusham 1", "213° 20'"), ("Anusham 2", "216° 40'"), ("Anusham 3", "220° 00'"), ("Anusham 4", "223° 20'"),
            ("Kettai 1", "226° 40'"), ("Kettai 2", "230° 00'"), ("Kettai 3", "233° 20'"), ("Kettai 4", "236° 40'")
        ]
    },
    {
        "name": "Sagittarius / Dhanusu", "range": "240° to 270°", "grid_pos": (0, 3),
        "padams": [
            ("Moolam 1", "240° 00'"), ("Moolam 2", "243° 20'"), ("Moolam 3", "246° 40'"), ("Moolam 4", "250° 00'"),
            ("Pooradam 1", "253° 20'"), ("Pooradam 2", "256° 40'"), ("Pooradam 3", "260° 00'"), ("Pooradam 4", "263° 20'"),
            ("Uthiradam 1", "266° 40'")
        ]
    },
    {
        "name": "Capricorn / Magaram", "range": "270° to 300°", "grid_pos": (0, 2),
        "padams": [
            ("Uthiradam 2", "270° 00'"), ("Uthiradam 3", "273° 20'"), ("Uthiradam 4", "276° 40'"),
            ("Thiruvonam 1", "280° 00'"), ("Thiruvonam 2", "283° 20'"), ("Thiruvonam 3", "286° 40'"), ("Thiruvonam 4", "290° 00'"),
            ("Avittam 1", "293° 20'"), ("Avittam 2", "296° 40'")
        ]
    },
    {
        "name": "Aquarius / Kumbham", "range": "300° to 330°", "grid_pos": (0, 1),
        "padams": [
            ("Avittam 3", "300° 00'"), ("Avittam 4", "303° 20'"),
            ("Sadayam 1", "306° 40'"), ("Sadayam 2", "310° 00'"), ("Sadayam 3", "313° 20'"), ("Sadayam 4", "316° 40'"),
            ("Poorattadhi 1", "320° 00'"), ("Poorattadhi 2", "323° 20'"), ("Poorattadhi 3", "326° 40'")
        ]
    },
    {
        "name": "Pisces / Meenam", "range": "330° to 360°", "grid_pos": (0, 0),
        "padams": [
            ("Poorattadhi 4", "330° 00'"),
            ("Uthirattadhi 1", "333° 20'"), ("Uthirattadhi 2", "336° 40'"), ("Uthirattadhi 3", "340° 00'"), ("Uthirattadhi 4", "343° 20'"),
            ("Revathi 1", "346° 40'"), ("Revathi 2", "350° 00'"), ("Revathi 3", "353° 20'"), ("Revathi 4", "356° 40'")
        ]
    }
]

zodiac_sanskrit_relative = [
    {
        "name": "Mesha (0 to 30)", "grid_pos": (1, 0),
        "padams": [
            ("Ashwini", "Padam 1: 0° 00'"), ("Ashwini", "Padam 2: 3° 20'"), ("Ashwini", "Padam 3: 6° 40'"), ("Ashwini", "Padam 4: 10° 00'"),
            ("Bharani", "Padam 1: 13° 20'"), ("Bharani", "Padam 2: 16° 40'"), ("Bharani", "Padam 3: 20° 00'"), ("Bharani", "Padam 4: 23° 20'"),
            ("Krittika", "Padam 1: 26° 40'")
        ]
    },
    {
        "name": "Vrishabha (0 to 30)", "grid_pos": (2, 0),
        "padams": [
            ("Krittika", "Padam 2: 0° 00'"), ("Krittika", "Padam 3: 3° 20'"), ("Krittika", "Padam 4: 6° 40'"),
            ("Rohini", "Padam 1: 10° 00'"), ("Rohini", "Padam 2: 13° 20'"), ("Rohini", "Padam 3: 16° 40'"), ("Rohini", "Padam 4: 20° 00'"),
            ("Mrigashira", "Padam 1: 23° 20'"), ("Mrigashira", "Padam 2: 26° 40'")
        ]
    },
    {
        "name": "Mithuna (0 to 30)", "grid_pos": (3, 0),
        "padams": [
            ("Mrigashira", "Padam 3: 0° 00'"), ("Mrigashira", "Padam 4: 3° 20'"),
            ("Ardra", "Padam 1: 6° 40'"), ("Ardra", "Padam 2: 10° 00'"), ("Ardra", "Padam 3: 13° 20'"), ("Ardra", "Padam 4: 16° 40'"),
            ("Punarvasu", "Padam 1: 20° 00'"), ("Punarvasu", "Padam 2: 23° 20'"), ("Punarvasu", "Padam 3: 26° 40'")
        ]
    },
    {
        "name": "Karka (0 to 30)", "grid_pos": (3, 1),
        "padams": [
            ("Punarvasu", "Padam 4: 0° 00'"),
            ("Pushya", "Padam 1: 3° 20'"), ("Pushya", "Padam 2: 6° 40'"), ("Pushya", "Padam 3: 10° 00'"), ("Pushya", "Padam 4: 13° 20'"),
            ("Ashlesha", "Padam 1: 16° 40'"), ("Ashlesha", "Padam 2: 20° 00'"), ("Ashlesha", "Padam 3: 23° 20'"), ("Ashlesha", "Padam 4: 26° 40'")
        ]
    },
    {
        "name": "Simha (0 to 30)", "grid_pos": (3, 2),
        "padams": [
            ("Magha", "Padam 1: 0° 00'"), ("Magha", "Padam 2: 3° 20'"), ("Magha", "Padam 3: 6° 40'"), ("Magha", "Padam 4: 10° 00'"),
            ("Purva Phalguni", "Padam 1: 13° 20'"), ("Purva Phalguni", "Padam 2: 16° 40'"), ("Purva Phalguni", "Padam 3: 20° 00'"), ("Purva Phalguni", "Padam 4: 23° 20'"),
            ("Uttara Phalguni", "Padam 1: 26° 40'")
        ]
    },
    {
        "name": "Kanya (0 to 30)", "grid_pos": (3, 3),
        "padams": [
            ("Uttara Phalguni", "Padam 2: 0° 00'"), ("Uttara Phalguni", "Padam 3: 3° 20'"), ("Uttara Phalguni", "Padam 4: 6° 40'"),
            ("Hasta", "Padam 1: 10° 00'"), ("Hasta", "Padam 2: 13° 20'"), ("Hasta", "Padam 3: 16° 40'"), ("Hasta", "Padam 4: 20° 00'"),
            ("Chitra", "Padam 1: 23° 20'"), ("Chitra", "Padam 2: 26° 40'")
        ]
    },
    {
        "name": "Tula (0 to 30)", "grid_pos": (2, 3),
        "padams": [
            ("Chitra", "Padam 3: 0° 00'"), ("Chitra", "Padam 4: 3° 20'"),
            ("Swati", "Padam 1: 6° 40'"), ("Swati", "Padam 2: 10° 00'"), ("Swati", "Padam 3: 13° 20'"), ("Swati", "Padam 4: 16° 40'"),
            ("Vishakha", "Padam 1: 20° 00'"), ("Vishakha", "Padam 2: 23° 20'"), ("Vishakha", "Padam 3: 26° 40'")
        ]
    },
    {
        "name": "Vrishchika (0 to 30)", "grid_pos": (1, 3),
        "padams": [
            ("Vishakha", "Padam 4: 0° 00'"),
            ("Anuradha", "Padam 1: 3° 20'"), ("Anuradha", "Padam 2: 6° 40'"), ("Anuradha", "Padam 3: 10° 00'"), ("Anuradha", "Padam 4: 13° 20'"),
            ("Jyeshtha", "Padam 1: 16° 40'"), ("Jyeshtha", "Padam 2: 20° 00'"), ("Jyeshtha", "Padam 3: 23° 20'"), ("Jyeshtha", "Padam 4: 26° 40'")
        ]
    },
    {
        "name": "Dhanu (0 to 30)", "grid_pos": (0, 3),
        "padams": [
            ("Mula", "Padam 1: 0° 00'"), ("Mula", "Padam 2: 3° 20'"), ("Mula", "Padam 3: 6° 40'"), ("Mula", "Padam 4: 10° 00'"),
            ("Purva Ashadha", "Padam 1: 13° 20'"), ("Purva Ashadha", "Padam 2: 16° 40'"), ("Purva Ashadha", "Padam 3: 20° 00'"), ("Purva Ashadha", "Padam 4: 23° 20'"),
            ("Uttara Ashadha", "Padam 1: 26° 40'")
        ]
    },
    {
        "name": "Makara (0 to 30)", "grid_pos": (0, 2),
        "padams": [
            ("Uttara Ashadha", "Padam 2: 0° 00'"), ("Uttara Ashadha", "Padam 3: 3° 20'"), ("Uttara Ashadha", "Padam 4: 6° 40'"),
            ("Shravana", "Padam 1: 10° 00'"), ("Shravana", "Padam 2: 13° 20'"), ("Shravana", "Padam 3: 16° 40'"), ("Shravana", "Padam 4: 20° 00'"),
            ("Dhanishta", "Padam 1: 23° 20'"), ("Dhanishta", "Padam 2: 26° 40'")
        ]
    },
    {
        "name": "Kumbha (0 to 30)", "grid_pos": (0, 1),
        "padams": [
            ("Dhanishta", "Padam 3: 0° 00'"), ("Dhanishta", "Padam 4: 3° 20'"),
            ("Shatabhisha", "Padam 1: 6° 40'"), ("Shatabhisha", "Padam 2: 10° 00'"), ("Shatabhisha", "Padam 3: 13° 20'"), ("Shatabhisha", "Padam 4: 16° 40'"),
            ("Purva Bhadrapada", "Padam 1: 20° 00'"), ("Purva Bhadrapada", "Padam 2: 23° 20'"), ("Purva Bhadrapada", "Padam 3: 26° 40'")
        ]
    },
    {
        "name": "Meena (0 to 30)", "grid_pos": (0, 0),
        "padams": [
            ("Purva Bhadrapada", "Padam 4: 0° 00'"),
            ("Uttara Bhadrapada", "Padam 1: 3° 20'"), ("Uttara Bhadrapada", "Padam 2: 6° 40'"), ("Uttara Bhadrapada", "Padam 3: 10° 00'"), ("Uttara Bhadrapada", "Padam 4: 13° 20'"),
            ("Revati", "Padam 1: 16° 40'"), ("Revati", "Padam 2: 20° 00'"), ("Revati", "Padam 3: 23° 20'"), ("Revati", "Padam 4: 26° 40'")
        ]
    }
]

zodiac_tamil_relative = [
    {
        "name": "Mesham (0 to 30)", "grid_pos": (1, 0),
        "padams": [
            ("Ashwini", "Padam 1: 0° 00'"), ("Ashwini", "Padam 2: 3° 20'"), ("Ashwini", "Padam 3: 6° 40'"), ("Ashwini", "Padam 4: 10° 00'"),
            ("Bharani", "Padam 1: 13° 20'"), ("Bharani", "Padam 2: 16° 40'"), ("Bharani", "Padam 3: 20° 00'"), ("Bharani", "Padam 4: 23° 20'"),
            ("Kiruthigai", "Padam 1: 26° 40'")
        ]
    },
    {
        "name": "Rishabham (0 to 30)", "grid_pos": (2, 0),
        "padams": [
            ("Kiruthigai", "Padam 2: 0° 00'"), ("Kiruthigai", "Padam 3: 3° 20'"), ("Kiruthigai", "Padam 4: 6° 40'"),
            ("Rohini", "Padam 1: 10° 00'"), ("Rohini", "Padam 2: 13° 20'"), ("Rohini", "Padam 3: 16° 40'"), ("Rohini", "Padam 4: 20° 00'"),
            ("Mirugaseerisham", "Padam 1: 23° 20'"), ("Mirugaseerisham", "Padam 2: 26° 40'")
        ]
    },
    {
        "name": "Midhunam (0 to 30)", "grid_pos": (3, 0),
        "padams": [
            ("Mirugaseerisham", "Padam 3: 0° 00'"), ("Mirugaseerisham", "Padam 4: 3° 20'"),
            ("Thiruvadhirai", "Padam 1: 6° 40'"), ("Thiruvadhirai", "Padam 2: 10° 00'"), ("Thiruvadhirai", "Padam 3: 13° 20'"), ("Thiruvadhirai", "Padam 4: 16° 40'"),
            ("Punarpoosam", "Padam 1: 20° 00'"), ("Punarpoosam", "Padam 2: 23° 20'"), ("Punarpoosam", "Padam 3: 26° 40'")
        ]
    },
    {
        "name": "Kadagam (0 to 30)", "grid_pos": (3, 1),
        "padams": [
            ("Punarpoosam", "Padam 4: 0° 00'"),
            ("Poosam", "Padam 1: 3° 20'"), ("Poosam", "Padam 2: 6° 40'"), ("Poosam", "Padam 3: 10° 00'"), ("Poosam", "Padam 4: 13° 20'"),
            ("Ayilyam", "Padam 1: 16° 40'"), ("Ayilyam", "Padam 2: 20° 00'"), ("Ayilyam", "Padam 3: 23° 20'"), ("Ayilyam", "Padam 4: 26° 40'")
        ]
    },
    {
        "name": "Simmam (0 to 30)", "grid_pos": (3, 2),
        "padams": [
            ("Magam", "Padam 1: 0° 00'"), ("Magam", "Padam 2: 3° 20'"), ("Magam", "Padam 3: 6° 40'"), ("Magam", "Padam 4: 10° 00'"),
            ("Pooram", "Padam 1: 13° 20'"), ("Pooram", "Padam 2: 16° 40'"), ("Pooram", "Padam 3: 20° 00'"), ("Pooram", "Padam 4: 23° 20'"),
            ("Uthiram", "Padam 1: 26° 40'")
        ]
    },
    {
        "name": "Kanni (0 to 30)", "grid_pos": (3, 3),
        "padams": [
            ("Uthiram", "Padam 2: 0° 00'"), ("Uthiram", "Padam 3: 3° 20'"), ("Uthiram", "Padam 4: 6° 40'"),
            ("Hastham", "Padam 1: 10° 00'"), ("Hastham", "Padam 2: 13° 20'"), ("Hastham", "Padam 3: 16° 40'"), ("Hastham", "Padam 4: 20° 00'"),
            ("Chithirai", "Padam 1: 23° 20'"), ("Chithirai", "Padam 2: 26° 40'")
        ]
    },
    {
        "name": "Thulaam (0 to 30)", "grid_pos": (2, 3),
        "padams": [
            ("Chithirai", "Padam 3: 0° 00'"), ("Chithirai", "Padam 4: 3° 20'"),
            ("Swathi", "Padam 1: 6° 40'"), ("Swathi", "Padam 2: 10° 00'"), ("Swathi", "Padam 3: 13° 20'"), ("Swathi", "Padam 4: 16° 40'"),
            ("Visagam", "Padam 1: 20° 00'"), ("Visagam", "Padam 2: 23° 20'"), ("Visagam", "Padam 3: 26° 40'")
        ]
    },
    {
        "name": "Viruchigam (0 to 30)", "grid_pos": (1, 3),
        "padams": [
            ("Visagam", "Padam 4: 0° 00'"),
            ("Anusham", "Padam 1: 3° 20'"), ("Anusham", "Padam 2: 6° 40'"), ("Anusham", "Padam 3: 10° 00'"), ("Anusham", "Padam 4: 13° 20'"),
            ("Kettai", "Padam 1: 16° 40'"), ("Kettai", "Padam 2: 20° 00'"), ("Kettai", "Padam 3: 23° 20'"), ("Kettai", "Padam 4: 26° 40'")
        ]
    },
    {
        "name": "Dhanusu (0 to 30)", "grid_pos": (0, 3),
        "padams": [
            ("Moolam", "Padam 1: 0° 00'"), ("Moolam", "Padam 2: 3° 20'"), ("Moolam", "Padam 3: 6° 40'"), ("Moolam", "Padam 4: 10° 00'"),
            ("Pooradam", "Padam 1: 13° 20'"), ("Pooradam", "Padam 2: 16° 40'"), ("Pooradam", "Padam 3: 20° 00'"), ("Pooradam", "Padam 4: 23° 20'"),
            ("Uthiradam", "Padam 1: 26° 40'")
        ]
    },
    {
        "name": "Magaram (0 to 30)", "grid_pos": (0, 2),
        "padams": [
            ("Uthiradam", "Padam 2: 0° 00'"), ("Uthiradam", "Padam 3: 3° 20'"), ("Uthiradam", "Padam 4: 6° 40'"),
            ("Thiruvonam", "Padam 1: 10° 00'"), ("Thiruvonam", "Padam 2: 13° 20'"), ("Thiruvonam", "Padam 3: 16° 40'"), ("Thiruvonam", "Padam 4: 20° 00'"),
            ("Avittam", "Padam 1: 23° 20'"), ("Avittam", "Padam 2: 26° 40'")
        ]
    },
    {
        "name": "Kumbham (0 to 30)", "grid_pos": (0, 1),
        "padams": [
            ("Avittam", "Padam 3: 0° 00'"), ("Avittam", "Padam 4: 3° 20'"),
            ("Sadayam", "Padam 1: 6° 40'"), ("Sadayam", "Padam 2: 10° 00'"), ("Sadayam", "Padam 3: 13° 20'"), ("Sadayam", "Padam 4: 16° 40'"),
            ("Poorattadhi", "Padam 1: 20° 00'"), ("Poorattadhi", "Padam 2: 23° 20'"), ("Poorattadhi", "Padam 3: 26° 40'")
        ]
    },
    {
        "name": "Meenam (0 to 30)", "grid_pos": (0, 0),
        "padams": [
            ("Poorattadhi", "Padam 4: 0° 00'"),
            ("Uthirattadhi", "Padam 1: 3° 20'"), ("Uthirattadhi", "Padam 2: 6° 40'"), ("Uthirattadhi", "Padam 3: 10° 00'"), ("Uthirattadhi", "Padam 4: 13° 20'"),
            ("Revathi", "Padam 1: 16° 40'"), ("Revathi", "Padam 2: 20° 00'"), ("Revathi", "Padam 3: 23° 20'"), ("Revathi", "Padam 4: 26° 40'")
        ]
    }
]

# ==========================================
# 2. RENDER ENGINES
# ==========================================

def get_shared_styles():
    return '''
    <style>
        .bg { fill: #fdfcf7; }
        .grid-line { stroke: #3e2723; stroke-width: 2.5; stroke-linecap: round; fill: none; }
        .center-bg { fill: #f5f1e6; }
        .sign-title { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 15px; font-weight: bold; fill: #1a1a1a; }
        .sign-range { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 11px; fill: #7f8c8d; font-weight: 500; }
        .padam-name { font-family: 'Courier New', Courier, monospace; font-size: 11px; font-weight: bold; fill: #2c3e50; }
        .padam-deg { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 11px; fill: #d35400; font-weight: bold; }
        .center-title { font-family: 'Georgia', serif; font-size: 32px; font-weight: bold; fill: #3e2723; text-anchor: middle; letter-spacing: 2px; }
    </style>
    '''

def draw_chart_skeleton(svg, width, height, box_size):
    # Base background
    svg.append(f'<rect width="{width}" height="{height}" class="bg" />')
    # Center space background & title
    svg.append(f'<rect x="{box_size}" y="{box_size}" width="{box_size*2}" height="{box_size*2}" class="center-bg" />')
    svg.append(f'<text x="{width/2}" y="{height/2 + 10}" class="center-title">NAKSHATRA PADAM CHART</text>')
    # Outer bound layout
    svg.append(f'<rect x="0" y="0" width="{width}" height="{height}" class="grid-line" />')
    # Center frame layout
    svg.append(f'<rect x="{box_size}" y="{box_size}" width="{box_size*2}" height="{box_size*2}" class="grid-line" />')

    # Non-crossing lines for layout integrity
    for i in [1, 2, 3]:
        pos = i * box_size
        svg.append(f'<line x1="{pos}" y1="0" x2="{pos}" y2="{box_size}" class="grid-line" />')
        svg.append(f'<line x1="{pos}" y1="{box_size*3}" x2="{pos}" y2="{height}" class="grid-line" />')
        svg.append(f'<line x1="0" y1="{pos}" x2="{box_size}" y2="{pos}" class="grid-line" />')
        svg.append(f'<line x1="{box_size*3}" y1="{pos}" x2="{width}" y2="{pos}" class="grid-line" />')

def generate_absolute_chart(dataset, output_file):
    box_size = 280  
    width = height = box_size * 4
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">', get_shared_styles()]
    
    draw_chart_skeleton(svg, width, height, box_size)

    for sign in dataset:
        col, row = sign["grid_pos"]
        x_start, y_start = col * box_size, row * box_size
        
        svg.append(f'<text x="{x_start + 14}" y="{y_start + 28}" class="sign-title">{html.escape(sign["name"])}</text>')
        svg.append(f'<text x="{x_start + 14}" y="{y_start + 45}" class="sign-range">Total: {html.escape(sign["range"])}</text>')
        svg.append(f'<line x1="{x_start + 14}" y1="{y_start + 53}" x2="{x_start + box_size - 14}" y2="{y_start + 53}" stroke="#e0dbd1" stroke-width="1.5" />')
        
        y_offset = y_start + 74
        for name, degree in sign["padams"]:
            svg.append(f'<text x="{x_start + 16}" y="{y_offset}" class="padam-name">{html.escape(name)}</text>')
            svg.append(f'<text x="{x_start + box_size - 16}" y="{y_offset}" text-anchor="end" class="padam-deg">{html.escape(degree)}</text>')
            y_offset += 21

    svg.append('</svg>')
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Exported absolute format layout safely to '{output_file}'.")

def generate_relative_chart(dataset, output_file):
    box_size = 280  
    width = height = box_size * 4
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">', get_shared_styles()]
    
    draw_chart_skeleton(svg, width, height, box_size)

    for sign in dataset:
        col, row = sign["grid_pos"]
        x_start, y_start = col * box_size, row * box_size
        
        svg.append(f'<text x="{x_start + 14}" y="{y_start + 28}" class="sign-title">{html.escape(sign["name"])}</text>')
        svg.append(f'<line x1="{x_start + 14}" y1="{y_start + 40}" x2="{x_start + box_size - 14}" y2="{y_start + 40}" stroke="#e0dbd1" stroke-width="1.5" />')
        
        y_offset = y_start + 62
        for name, placement in sign["padams"]:
            svg.append(f'<text x="{x_start + 14}" y="{y_offset}" class="padam-name">{html.escape(name)}</text>')
            svg.append(f'<text x="{x_start + box_size - 14}" y="{y_offset}" text-anchor="end" class="padam-deg">{html.escape(placement)}</text>')
            y_offset += 23

    svg.append('</svg>')
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Exported relative format layout safely to '{output_file}'.")


# ==========================================
# 3. EXECUTION DRIVER
# ==========================================

if __name__ == "__main__":
    # Formats matching 0 to 360 absolute degrees
    generate_absolute_chart(zodiac_sanskrit_absolute, "sanskrit_chart_absolute_0_360.svg")
    generate_absolute_chart(zodiac_tamil_absolute, "tamil_chart_absolute_0_360.svg")
    
    # Formats matching clean relative 0 to 30 degrees configurations
    generate_relative_chart(zodiac_sanskrit_relative, "sanskrit_chart_relative_0_30.svg")
    generate_relative_chart(zodiac_relative_dataset := zodiac_tamil_relative, "tamil_chart_relative_0_30.svg")

