

elements.append(Spacer(1, 12))
elements.append(Spacer(1, 12))
elements.append(Paragraph("Fast Track:", legend_style))
for module, count in exercise_count_per_module.items():
    elements.append(Paragraph(f"{module}: {count} exercises", legend_style))

elements.append(Spacer(1, 12))
elements.append(Paragraph("Unsubmitted:", legend_style))
for module, exercises in unsubmitted_exercises.items():
    elements.append(Paragraph(f"{module}: {', '.join(exercises)} are unsubmitted", legend_style))