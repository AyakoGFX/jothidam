import html

zodiac_detailed_data = [
    {
        "name": "Aries / Mesha",
        "range": "0° to 30°",
        "grid_pos": (1, 0),
        "padams": [
            ("Ashwini 1", "0° 00'"), ("Ashwini 2", "3° 20'"),
            ("Ashwini 3", "6° 40'"), ("Ashwini 4", "10° 00'"),
            ("Bharani 1", "13° 20'"), ("Bharani 2", "16° 40'"),
            ("Bharani 3", "20° 00'"), ("Bharani 4", "23° 20'"),
            ("Krittika 1", "26° 40'")
        ]
    },
    {
        "name": "Taurus / Vrishabha",
        "range": "30° to 60°",
        "grid_pos": (2, 0),
        "padams": [
            ("Krittika 2", "30° 00'"), ("Krittika 3", "33° 20'"), ("Krittika 4", "36° 40'"),
            ("Rohini 1", "40° 00'"), ("Rohini 2", "43° 20'"),
            ("Rohini 3", "46° 40'"), ("Rohini 4", "50° 00'"),
            ("Mrigashira 1", "53° 20'"), ("Mrigashira 2", "56° 40'")
        ]
    },
    {
        "name": "Gemini / Mithuna",
        "range": "60° to 90°",
        "grid_pos": (3, 0),
        "padams": [
            ("Mrigashira 3", "60° 00'"), ("Mrigashira 4", "63° 20'"),
            ("Ardra 1", "66° 40'"), ("Ardra 2", "70° 00'"),
            ("Ardra 3", "73° 20'"), ("Ardra 4", "76° 40'"),
            ("Punarvasu 1", "80° 00'"), ("Punarvasu 2", "83° 20'"), ("Punarvasu 3", "86° 40'")
        ]
    },
    {
        "name": "Cancer / Karka",
        "range": "90° to 120°",
        "grid_pos": (3, 1),
        "padams": [
            ("Punarvasu 4", "90° 00'"),
            ("Pushya 1", "93° 20'"), ("Pushya 2", "96° 40'"),
            ("Pushya 3", "100° 00'"), ("Pushya 4", "103° 20'"),
            ("Ashlesha 1", "106° 40'"), ("Ashlesha 2", "110° 00'"),
            ("Ashlesha 3", "113° 20'"), ("Ashlesha 4", "116° 40'")
        ]
    },
    {
        "name": "Leo / Simha",
        "range": "120° to 150°",
        "grid_pos": (3, 2),
        "padams": [
            ("Magha 1", "120° 00'"), ("Magha 2", "123° 20'"),
            ("Magha 3", "126° 40'"), ("Magha 4", "130° 00'"),
            ("Purva Phalguni 1", "133° 20'"), ("Purva Phalguni 2", "136° 40'"),
            ("Purva Phalguni 3", "140° 00'"), ("Purva Phalguni 4", "143° 20'"),
            ("Uttara Phalguni 1", "146° 40'")
        ]
    },
    {
        "name": "Virgo / Kanya",
        "range": "150° to 180°",
        "grid_pos": (3, 3),
        "padams": [
            ("Uttara Phalguni 2", "150° 00'"), ("Uttara Phalguni 3", "153° 20'"), ("Uttara Phalguni 4", "156° 40'"),
            ("Hasta 1", "160° 00'"), ("Hasta 2", "163° 20'"),
            ("Hasta 3", "166° 40'"), ("Hasta 4", "170° 00'"),
            ("Chitra 1", "173° 20'"), ("Chitra 2", "176° 40'")
        ]
    },
    {
        "name": "Libra / Tula",
        "range": "180° to 210°",
        "grid_pos": (2, 3),
        "padams": [
            ("Chitra 3", "180° 00'"), ("Chitra 4", "183° 20'"),
            ("Swati 1", "186° 40'"), ("Swati 2", "190° 00'"),
            ("Swati 3", "193° 20'"), ("Swati 4", "196° 40'"),
            ("Vishakha 1", "200° 00'"), ("Vishakha 2", "203° 20'"), ("Vishakha 3", "206° 40'")
        ]
    },
    {
        "name": "Scorpio / Vrishchika",
        "range": "210° to 240°",
        "grid_pos": (1, 3),
        "padams": [
            ("Vishakha 4", "210° 00'"),
            ("Anuradha 1", "213° 20'"), ("Anuradha 2", "216° 40'"),
            ("Anuradha 3", "220° 00'"), ("Anuradha 4", "223° 20'"),
            ("Jyeshtha 1", "226° 40'"), ("Jyeshtha 2", "230° 00'"),
            ("Jyeshtha 3", "233° 20'"), ("Jyeshtha 4", "236° 40'")
        ]
    },
    {
        "name": "Sagittarius / Dhanu",
        "range": "240° to 270°",
        "grid_pos": (0, 3),
        "padams": [
            ("Mula 1", "240° 00'"), ("Mula 2", "243° 20'"),
            ("Mula 3", "246° 40'"), ("Mula 4", "250° 00'"),
            ("Purva Ashadha 1", "253° 20'"), ("Purva Ashadha 2", "256° 40'"),
            ("Purva Ashadha 3", "260° 00'"), ("Purva Ashadha 4", "263° 20'"),
            ("Uttara Ashadha 1", "266° 40'")
        ]
    },
    {
        "name": "Capricorn / Makara",
        "range": "270° to 300°",
        "grid_pos": (0, 2),
        "padams": [
            ("Uttara Ashadha 2", "270° 00'"), ("Uttara Ashadha 3", "273° 20'"), ("Uttara Ashadha 4", "276° 40'"),
            ("Shravana 1", "280° 00'"), ("Shravana 2", "283° 20'"),
            ("Shravana 3", "286° 40'"), ("Shravana 4", "290° 00'"),
            ("Dhanishta 1", "293° 20'"), ("Dhanishta 2", "296° 40'")
        ]
    },
    {
        "name": "Aquarius / Kumbha",
        "range": "300° to 330°",
        "grid_pos": (0, 1),
        "padams": [
            ("Dhanishta 3", "300° 00'"), ("Dhanishta 4", "303° 20'"),
            ("Shatabhisha 1", "306° 40'"), ("Shatabhisha 2", "310° 00'"),
            ("Shatabhisha 3", "313° 20'"), ("Shatabhisha 4", "316° 40'"),
            ("Purva Bhadrapada 1", "320° 00'"), ("Purva Bhadrapada 2", "323° 20'"), ("Purva Bhadrapada 3", "326° 40'")
        ]
    },
    {
        "name": "Pisces / Meena",
        "range": "330° to 360°",
        "grid_pos": (0, 0),
        "padams": [
            ("Purva Bhadrapada 4", "330° 00'"),
            ("Uttara Bhadrapada 1", "333° 20'"), ("Uttara Bhadrapada 2", "336° 40'"),
            ("Uttara Bhadrapada 3", "340° 00'"), ("Uttara Bhadrapada 4", "343° 20'"),
            ("Revati 1", "346° 40'"), ("Revati 2", "350° 00'"),
            ("Revati 3", "353° 20'"), ("Revati 4", "356° 40'")
        ]
    }
]

def generate_sanskrit_chart(output_file="south_indian_sanskrit_chart.svg"):
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
    
    # 2. Center Space
    svg.append(f'<rect x="{box_size}" y="{box_size}" width="{box_size*2}" height="{box_size*2}" class="center-bg" />')
    svg.append(f'<text x="{width/2}" y="{height/2 + 10}" class="center-title">NAKSHATRA PADAM CHART</text>')

    # 3. Outer Border
    svg.append(f'<rect x="0" y="0" width="{width}" height="{height}" class="grid-line" />')
    
    # 4. Center Box Frame
    svg.append(f'<rect x="{box_size}" y="{box_size}" width="{box_size*2}" height="{box_size*2}" class="grid-line" />')

    # 5. Clean Divider Segments
    for i in [1, 2, 3]:
        pos = i * box_size
        svg.append(f'<line x1="{pos}" y1="0" x2="{pos}" y2="{box_size}" class="grid-line" />')
        svg.append(f'<line x1="{pos}" y1="{box_size*3}" x2="{pos}" y2="{height}" class="grid-line" />')
        svg.append(f'<line x1="0" y1="{pos}" x2="{box_size}" y2="{pos}" class="grid-line" />')
        svg.append(f'<line x1="{box_size*3}" y1="{pos}" x2="{width}" y2="{pos}" class="grid-line" />')

    # 6. Render Sanskrit Text Data
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
        print(f"Chart with Sanskrit names saved to '{output_file}'.")

if __name__ == "__main__":
    generate_sanskrit_chart()
