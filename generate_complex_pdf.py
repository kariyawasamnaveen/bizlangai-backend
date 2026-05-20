from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_complex_pdf():
    pdf_path = "/Users/naveensandeepa/Desktop/BizLangAI_Complex_Case_Study.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = styles['Heading1']
    subtitle_style = styles['Heading2']
    body_style = styles['BodyText']
    body_style.spaceAfter = 12

    story = []

    # Title
    story.append(Paragraph("Project Nova: Q3 2024 Financial & Operational Audit Report", title_style))
    story.append(Spacer(1, 12))

    # Executive Summary
    story.append(Paragraph("1. Executive Summary", subtitle_style))
    story.append(Paragraph("Project Nova was initiated in January 2024 to overhaul the supply chain logistics for the Southeast Asian sector. By the end of Q3 2024, the project achieved a 14% reduction in transit delays but overshot the allocated budget by $2.4M due to unexpected regulatory compliance costs in Vietnam and Indonesia. The primary goal of achieving a 20% carbon footprint reduction was only partially met at 12%, largely attributed to the delay in deploying EV transport units.", body_style))
    
    # Financial Discrepancies
    story.append(Paragraph("2. Financial Discrepancies & Budget Overruns", subtitle_style))
    story.append(Paragraph("The initial budget for Project Nova was set at $15M. However, Section 4.2 of the audit reveals that $3.8M was diverted to an emergency contractor (Vendor ID: V-8890) to handle a severe bottleneck at the Jakarta port facility in August. Furthermore, the software integration for the automated tracking system (System X-Ray) cost $850,000 more than anticipated because the legacy API was incompatible with the new microservices architecture. To compensate, the Marketing budget for Q4 has been frozen, and a mandatory 5% cut across all non-essential operational expenses has been implemented effective November 1st.", body_style))

    # HR Policies & Contractor Guidelines
    story.append(Paragraph("3. Updated Remote Work & Contractor Policies (Effective Immediately)", subtitle_style))
    story.append(Paragraph("Due to the budget constraints and the need for high-availability during the Q4 recovery phase, the HR department has revised the remote work policy (Policy HR-77B). Employees assigned directly to Project Nova must now mandate at least 3 days in-office per week, specifically Tuesdays, Wednesdays, and Thursdays. Furthermore, any contractor invoicing over 40 hours a week must get prior written approval from the Regional Director (currently Ms. Elena Rostova). Failure to obtain this signature will result in unpaid overtime.", body_style))

    # Strategic Risks for Q4
    story.append(Paragraph("4. Strategic Risks for Q4", subtitle_style))
    story.append(Paragraph("The primary risk moving into Q4 is the impending expiration of the primary logistics contract with 'AeroFreight Solutions' on December 15th. If a renewal is not negotiated at the current rate of $1.20 per kg, shipping costs could spike by an estimated 18%. The secondary risk involves the System X-Ray software; if the final patch is not deployed by November 20th, data desynchronization between the warehouse and the mobile application will result in a 5-day blackout period for customer tracking.", body_style))

    doc.build(story)
    print(f"Created PDF at: {pdf_path}")

if __name__ == "__main__":
    create_complex_pdf()
