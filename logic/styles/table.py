from reportlab.lib.colors import Color
from reportlab.lib import colors
from reportlab.lib.units import inch

def generate_gradient_color(start_color, end_color, width, height):
    """
    Generate a gradient color for the background.

    Args:
    - start_color: tuple representing the RGB values of the starting color
    - end_color: tuple representing the RGB values of the ending color
    - width: width of the gradient
    - height: height of the gradient

    Returns:
    - colors.LinearGradient: Gradient color
    """

    gradient_colors = LinearGradient(0, 0, width, height, start_color, end_color)
    return gradient_colors


# gradient_colors = LinearShade(Color(0.5, 0, 0), Color(0, 0, 0.5))

bronze = colors.Color(0.8, 0.5, 0.2)

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
            ('FONTSIZE', (0, 0), (-1, 0), 8),
        ]

    return styles_completed

def styles_table_capstone(data):

    styles_completed = [
            ('GRID', (0, 0), (-1, -1), 1, (1, 1, 1)),
            ('BACKGROUND', (0, 0), (-1, 0), 'black'),
            ('TEXTCOLOR', (0, 0), (-1, 0), Color(255/255, 223/255, 0, alpha=1)),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
        ]

    return styles_completed

def styles_table_excellence(data):

    styles_completed = [
            ('GRID', (0, 0), (-1, -1), 1, (1, 1, 1)),
            ('BACKGROUND', (0, 0), (-1, 0), Color(255/255, 223/255, 0, alpha=1)),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'yellow'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
        ]

    return styles_completed

def styles_table_consistency(data):

    styles_completed = [
            ('GRID', (0, 0), (-1, -1), 1, (1, 1, 1)),
            ('BACKGROUND', (0, 0), (-1, 0), 'silver'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
        ]

    return styles_completed

def styles_table_engagement(data):

    styles_completed = [
            ('GRID', (0, 0), (-1, -1), 1, (1, 1, 1)),
            ('BACKGROUND', (0, 0), (-1, 0), bronze),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
        ]

    return styles_completed

def styles_table_team_player(data):

    styles_completed = [
            ('GRID', (0, 0), (-1, -1), 1, (1, 1, 1)),
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(128/255, 0, 128/255, alpha=1)),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'pink'),
            # ('FONTWEIGHT', (0, 0), (-1, 0), 'BOLD'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
        ]

    return styles_completed

def styles_capstone(data):

    styles_completed = [
            ('GRID', (0, 0), (-1, -1), 1, (1, 1, 1)),
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0, 0, 128/255, alpha=1)),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
            # ('FONTWEIGHT', (0, 0), (-1, 0), 'BOLD'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
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