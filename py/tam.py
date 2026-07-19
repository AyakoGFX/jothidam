import html

zodiac_detailed_data = [
    {
        "name": "Aries / Mesham",
        "range": "0° to 30°",
        "grid_pos": (1, 0),
        "padams": [
            ("Ashwini 1", "0° 00'"), ("Ashwini 2", "3° 20'"),
            ("Ashwini 3", "6° 40'"), ("Ashwini 4", "10° 00'"),
            ("Bharani 1", "13° 20'"), ("Bharani 2", "16° 40'"),
            ("Bharani 3", "20° 00'"), ("Bharani 4", "23° 20'"),
            ("Kiruthigai 1", "26° 40'")
        ]
    },
    {
        "name": "Taurus / Rishabham",
        "range": "30° to 60°",
        "grid_pos": (2, 0),
        "padams": [
            ("Kiruthigai 2", "30° 00'"), ("Kiruthigai 3", "33° 20'"), ("Kiruthigai 4", "36° 40'"),
            ("Rohini 1", "40° 00'"), ("Rohini 2", "43° 20'"),
            ("Rohini 3", "46° 40'"), ("Rohini 4", "50° 00'"),
            ("Mirugaseerisham 1", "53° 20'"), ("Mirugaseerisham 2", "56° 40'")
        ]
    },
    {
        "name": "Gemini / Midhunam",
        "range": "60° to 90°",
        "grid_pos": (3, 0),
        "padams": [
            ("Mirugaseerisham 3", "60° 00'"), ("Mirugaseerisham 4", "63° 20'"),
            ("Thiruvadhirai 1", "66° 40'"), ("Thiruvadhirai 2", "70° 00'"),
            ("Thiruvadhirai 3", "73° 20'"), ("Thiruvadhirai 4", "76° 40'"),
            ("Punarpoosam 1", "80° 00'"), ("Punarpoosam 2", "83° 20'"), ("Punarpoosam 3", "86° 40'")
        ]
    },
    {
        "name": "Cancer / Kadagam",
        "range": "90° to 120°",
        "grid_pos": (3, 1),
        "padams": [
            ("Punarpoosam 4", "90° 00'"),
            ("Poosam 1", "93° 20'"), ("Poosam 2", "96° 40'"),
            ("Poosam 3", "100° 00'"), ("Poosam 4", "103° 20'"),
            ("Ayilyam 1", "106° 40'"), ("Ayilyam 2", "110° 00'"),
            ("Ayilyam 3", "113° 20'"), ("Ayilyam 4", "116° 40'")
        ]
    },
    {
        "name": "Leo / Simmam",
        "range": "120° to 150°",
        "grid_pos": (3, 2),
        "padams": [
            ("Magam 1", "120° 00'"), ("Magam 2", "123° 20'"),
            ("Magam 3", "126° 40'"), ("Magam 4", "130° 00'"),
            ("Pooram 1", "133° 20'"), ("Pooram 2", "136° 40'"),
            ("Pooram 3", "140° 00'"), ("Pooram 4", "143° 20'"),
            ("Uthiram 1", "146° 40'")
        ]
    },
    {
        "name": "Virgo / Kanni",
        "range": "150° to 180°",
        "grid_pos": (3, 3),
        "padams": [
            ("Uthiram 2", "150° 00'"), ("Uthiram 3", "153° 20'"), ("Uthiram 4", "156° 40'"),
            ("Hastham 1", "160° 00'"), ("Hastham 2", "163° 20'"),
            ("Hastham 3", "166° 40'"), ("Hastham 4", "170° 00'"),
            ("Chithirai 1", "173° 20'"), ("Chithirai 2", "176° 40'")
        ]
    },
    {
        "name": "Libra / Thulaam",
        "range": "180° to 210°",
        "grid_pos": (2, 3),
        "padams": [
            ("Chithirai 3", "180° 00'"), ("Chithirai 4", "183° 20'"),
            ("Swathi 1", "186° 40'"), ("Swathi 2", "190° 00'"),
            ("Swathi 3", "193° 20'"), ("Swathi 4", "196° 40'"),
            ("Visagam 1", "200° 00'"), ("Visagam 2", "203° 20'"), ("Visagam 3", "206° 40'")
        ]
    },
    {
        "name": "Scorpio / Viruchigam",
        "range": "210° to 240°",
        "grid_pos": (1, 3),
        "padams": [
            ("Visagam 4", "210° 00'"),
            ("Anusham 1", "213° 20'"), ("Anusham 2", "216° 40'"),
            ("Anusham 3", "220° 00'"), ("Anusham 4", "223° 20'"),
            ("Kettai 1", "226° 40'"), ("Kettai 2", "230° 00'"),
            ("Kettai 3", "233° 20'"), ("Kettai 4", "236° 40'")
        ]
    },
    {
        "name": "Sagittarius / Dhanusu",
        "range": "240° to 270°",
        "grid_pos": (0, 3),
        "padams": [
            ("Moolam 1", "240° 00'"), ("Moolam 2", "243° 20'"),
            ("Moolam 3", "246° 40'"), ("Moolam 4", "250° 00'"),
            ("Pooradam 1", "253° 20'"), ("Pooradam 2", "256° 40'"),
            ("Pooradam 3", "260° 00'"), ("Pooradam 4", "263° 20'"),
            ("Uthiradam 1", "266° 40'")
        ]
    },
    {
        "name": "Capricorn / Magaram",
        "range": "270° to 300°",
        "grid_pos": (0, 2),
        "padams": [
            ("Uthiradam 2", "270° 00'"), ("Uthiradam 3", "273° 20'"), ("Uthiradam 4", "276° 40'"),
            ("Thiruvonam 1", "280° 00'"), ("Thiruvonam 2", "283° 20'"),
            ("Thiruvonam 3", "286° 40'"), ("Thiruvonam 4", "290° 00'"),
            ("Avittam 1", "293° 20'"), ("Avittam 2", "296° 40'")
        ]
    },
    {
        "name": "Aquarius / Kumbham",
        "range": "300° to 330°",
        "grid_pos": (0, 1),
        "padams": [
            ("Avittam 3", "300° 00'"), ("Avittam 4", "303° 20'"),
            ("Sadayam 1", "306° 40'"), ("Sadayam 2", "310° 00'"),
            ("Sadayam 3", "313° 20'"), ("Sadayam 4", "316° 40'"),
            ("Poorattadhi 1", "320° 00'"), ("Poorattadhi 2", "323° 20'"), ("Poorattadhi 3", "326° 40'")
        ]
    },
    {
        "name": "Pisces / Meenam",
        "range": "330° to 360°",
        "grid_pos": (0, 0),
        "padams": [
            ("Poorattadhi 4", "330° 00'"),
            ("Uthirattadhi 1", "333° 20'"), ("Uthirattadhi 2", "336° 40'"),
            ("Uthirattadhi 3", "340° 00'"), ("Uthirattadhi 4", "343° 20'"),
            ("Revathi 1", "346° 40'"), ("Revathi 2", "350° 00'"),
            ("Revathi 3", "353° 20'"), ("Revathi 4", "356° 40'")
        ]
    }
]

def generate_fixed_chart(output_file="south_indian_chart_fixed.svg"):
    box_size = 280  
    grid_size = 4
    width = box_size * grid_size
    height = box_size * grid_size
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">')
    
    svg.append('''
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
    ''')
    
    # 1. Base Background
    svg.append(f'<rect width="{width}" height="{height}" class="bg" />')
    
    # 2. Center Background Space
    svg.append(f'<rect x="{box_size}" y="{box_size}" width="{box_size*2}" height="{box_size*2}" class="center-bg" />')
    svg.append(f'<text x="{width/2}" y="{height/2 + 10}" class="center-title">NAKSHATRA PADAM CHART</text>')

    # 3. Outer Border of Entire Chart
    svg.append(f'<rect x="0" y="0" width="{width}" height="{height}" class="grid-line" />')
    
    # 4. Inner Center Box Border
    svg.append(f'<rect x="{box_size}" y="{box_size}" width="{box_size*2}" height="{box_size*2}" class="grid-line" />')

    # 5. Draw Clean Divider Line Segments (Skipping the center completely)
    for i in [1, 2, 3]:
        pos = i * box_size
        # Top Row vertical ticks (from y=0 down to the center box top edge)
        svg.append(f'<line x1="{pos}" y1="0" x2="{pos}" y2="{box_size}" class="grid-line" />')
        # Bottom Row vertical ticks (from center box bottom edge down to the layout bottom)
        svg.append(f'<line x1="{pos}" y1="{box_size*3}" x2="{pos}" y2="{height}" class="grid-line" />')
        # Left Column horizontal ticks (from x=0 across to the center box left edge)
        svg.append(f'<line x1="0" y1="{pos}" x2="{box_size}" y2="{pos}" class="grid-line" />')
        # Right Column horizontal ticks (from center box right edge across to layout right)
        svg.append(f'<line x1="{box_size*3}" y1="{pos}" x2="{width}" y2="{pos}" class="grid-line" />')

    # 6. Render Text Data
    for sign in zodiac_detailed_data:
        col, row = sign["grid_pos"]
        x_start = col * box_size
        y_start = row * box_size
        
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
        print(f"Fixed layout exported cleanly to '{output_file}'.")

if __name__ == "__main__":
    generate_fixed_chart()
