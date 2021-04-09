#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, infos):
    report = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    
    content = [report_title, empty_line]
    for info in infos:
        report_info = Paragraph(info, styles["BodyText"])
        content.append(report_info)
        content.append(empty_line)

    report.build(content)