from .constants.constants import *
from reportlab.lib import colors
# Removed unused import statement
from reportlab.lib.styles import getSampleStyleSheet

def style_missing(data):

    styles = [
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
    ]

    for i, row in enumerate(data, start=0):

        if row[0].startswith(('M', 'C', '1', '2', '3', '0', '★')) and row[0] != MODULE:
            if not row[2]:
                styles.append(('BACKGROUND', (2, i), (2, i), colors.lightcoral))

            elif any(x in row[2] for x in ['U', 'x']):
                styles.append(('BACKGROUND', (2, i), (2, i), colors.mistyrose))

            elif any(x in row[2] for x in ['L', 'P', 'ic']):
                styles.append(('BACKGROUND', (2, i), (2, i), colors.lightgoldenrodyellow))


    return styles

def style_missing_legend(legend_data):

    styles_legend = [
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), 'black'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]

    for i, row in enumerate(legend_data, start=0):
        if len(row) > 1:
            if row[1].startswith(('✓', 'x', 'L', 'ic', 'P', 'U')) and row[1] != 'Element':
                if not row[1]:
                    styles_legend.append(('BACKGROUND', (1, i), (1, i), colors.mistyrose))
                elif any(x in row[1] for x in ['U', 'x']):
                    styles_legend.append(('BACKGROUND', (1, i), (1, i), colors.mistyrose))

                elif any(x in row[1] for x in ['L', 'P', 'ic']):
                    styles_legend.append(('BACKGROUND', (1, i), (1, i), colors.lightgoldenrodyellow))
            elif not row[1] and row[2].startswith(('not')):
                styles_legend.append(('BACKGROUND', (1, i), (1, i), colors.lightcoral))

    return styles_legend