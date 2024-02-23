from reportlab.lib import colors

def styles_table_main(data):

    styles_table = [
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), 'black'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('TEXTCOLOR', (1, -1), (1, -1), colors.lightgrey),
        ('LEFTPADDING', (1, 0), (-1, 0), 0),
        ('RIGHTPADDING', (1, 0), (-1, 0), 0),
    ]

    return styles_table

def styles_table_completed(data):

    styles_completed = [
            ('GRID', (0, 0), (-1, -1), 1, (1, 1, 1)),
            ('BACKGROUND', (0, 0), (-1, 0), 'green'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
        ]

    return styles_completed

def styles_table_missing(data):

    styles_missing = [
                ('BACKGROUND', (0, 0), (-1, 0), colors._PCMYK_black),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),

                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0,0), (-1,-1), 1, colors.black)
            ]

    return styles_missing