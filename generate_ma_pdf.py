from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors

def create_ma_pdf():
    pdf_path = "/Users/naveensandeepa/Desktop/Project_Titan_Confidential_MA_Report.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=colors.darkred,
        alignment=TA_CENTER,
        spaceAfter=20
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=colors.darkblue,
        spaceAfter=12,
        spaceBefore=16
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        alignment=TA_JUSTIFY,
        spaceAfter=10
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=body_style,
        leftIndent=20,
        bulletIndent=10,
        spaceAfter=8
    )

    story = []

    # Title & Header
    story.append(Paragraph("STRICTLY CONFIDENTIAL", title_style))
    story.append(Paragraph("DUE DILIGENCE REPORT: PROJECT TITAN", title_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.black, spaceAfter=20))

    # Executive Summary
    story.append(Paragraph("1. Executive Summary", subtitle_style))
    story.append(Paragraph("This document outlines the findings of the final stage due diligence conducted by Vanguard Holdings regarding the potential acquisition of Nexus AI Solutions (hereafter referred to as 'The Target'). The acquisition is valued at an estimated $420M. While The Target possesses proprietary machine learning algorithms that could significantly enhance Vanguard's SaaS ecosystem, several severe risk factors have been identified during the legal and financial audits conducted between September 1st and November 10th, 2024.", body_style))
    
    # Financial Discrepancies
    story.append(Paragraph("2. Financial Health & Discrepancies", subtitle_style))
    story.append(Paragraph("A thorough audit of The Target's Q2 and Q3 financial statements revealed a $3.4M discrepancy in recognized deferred revenue. It appears that enterprise subscription contracts signed in Q4 of the previous fiscal year were prematurely recognized as realized revenue. Consequently, the actual EBITDA for the trailing twelve months (TTM) stands at $18.2M, reflecting a 12% overstatement in the initial prospectus.", body_style))

    # Regulatory Liabilities (The Core Target for AI Extraction)
    story.append(Paragraph("3. Regulatory & Compliance Liabilities", subtitle_style))
    story.append(Paragraph("Our legal counsel has identified significant compliance vulnerabilities primarily related to European and Californian data protection frameworks. If left unresolved prior to acquisition, Vanguard Holdings will inherit these liabilities. The top 3 regulatory liabilities identified in the target company are:", body_style))
    
    story.append(Paragraph("• <b>GDPR Non-Compliance (EU):</b> The Target's cloud infrastructure currently fails to provide sufficient data localization for European users. Anticipated Financial Impact: Potential fines up to €12M, plus an estimated $2.5M required for infrastructure migration.", bullet_style))
    
    story.append(Paragraph("• <b>CCPA Data Breach Settlement (California):</b> A pending class-action lawsuit regarding a minor data breach in early 2023 remains unsettled. Anticipated Financial Impact: Settlement reserves require an immediate injection of $4.8M.", bullet_style))
    
    story.append(Paragraph("• <b>Unlicensed Open-Source Usage:</b> Code analysis revealed the integration of an open-source library governed by a strict AGPL v3 license within their core proprietary engine. Anticipated Financial Impact: $1.2M for complete code refactoring and potential licensing dispute settlements.", bullet_style))

    story.append(Paragraph("The combined estimated financial impact of these three regulatory liabilities exceeds $20.5M, which must be factored into the final valuation adjustment.", body_style))

    # Intellectual Property
    story.append(Paragraph("4. Intellectual Property & Patents", subtitle_style))
    story.append(Paragraph("The Target holds 14 active utility patents. However, Patent #US-88992-B (Neural Network Optimization Protocol) is currently under review by the USPTO due to prior art claims submitted by a competitor (Synapse Tech). Loss of this patent would degrade the valuation by an estimated $15M.", body_style))

    # Conclusion
    story.append(HRFlowable(width="100%", thickness=1, color=colors.grey, spaceBefore=20, spaceAfter=15))
    story.append(Paragraph("<b>CONFIDENTIALITY NOTICE:</b> This document contains trade secrets and privileged information. Unauthorized distribution is strictly prohibited under NDA Clause 4.A.", body_style))

    doc.build(story)
    print(f"Created PDF at: {pdf_path}")

if __name__ == "__main__":
    create_ma_pdf()
