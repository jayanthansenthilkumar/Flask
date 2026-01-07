"""
Print utilities for invoice and receipt printing
"""
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.db import models
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
import io
from datetime import datetime

class PrintManager:
    """Handle all printing operations for invoices and receipts"""
    
    @staticmethod
    def generate_invoice_pdf(invoice):
        """Generate PDF invoice"""
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        
        header_style = ParagraphStyle(
            'Header',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=12,
            alignment=TA_LEFT
        )
        
        # Shop Header
        story.append(Paragraph("SriJai Tailoring", title_style))
        story.append(Paragraph("Professional Tailoring Services", styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Invoice details
        invoice_data = [
            ['Invoice Number:', invoice.invoice_number],
            ['Date:', invoice.created_at.strftime('%B %d, %Y')],
            ['Customer:', invoice.customer.name],
            ['Phone:', invoice.customer.phone],
            ['Due Date:', invoice.due_date.strftime('%B %d, %Y') if invoice.due_date else 'N/A']
        ]
        
        invoice_table = Table(invoice_data, colWidths=[2*inch, 3*inch])
        invoice_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 10),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ]))
        
        story.append(invoice_table)
        story.append(Spacer(1, 20))
        
        # Items table
        items_data = [['Description', 'Quantity', 'Unit Price', 'Total']]
        
        for item in invoice.order.orderitem_set.all():
            items_data.append([
                f"{item.garment_type.name} - {item.stitching_type.name}",
                str(item.quantity),
                f"₹{item.unit_price:.2f}",
                f"₹{item.total_price:.2f}"
            ])
        
        items_table = Table(items_data, colWidths=[3*inch, 1*inch, 1.5*inch, 1.5*inch])
        items_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,0), 10),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND', (0,1), (-1,-1), colors.beige),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
        ]))
        
        story.append(items_table)
        story.append(Spacer(1, 20))
        
        # Total section
        total_data = [
            ['Subtotal:', f"₹{invoice.subtotal:.2f}"],
            ['Tax:', f"₹{invoice.tax_amount:.2f}"],
            ['Discount:', f"₹{invoice.discount_amount:.2f}"],
            ['Total Amount:', f"₹{invoice.total_amount:.2f}"]
        ]
        
        total_table = Table(total_data, colWidths=[4*inch, 2*inch])
        total_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'RIGHT'),
            ('FONTNAME', (-1,-1), (-1,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (-1,-1), (-1,-1), 12),
            ('TEXTCOLOR', (-1,-1), (-1,-1), colors.darkblue),
            ('LINEBELOW', (-1,-1), (-1,-1), 2, colors.darkblue),
        ]))
        
        story.append(total_table)
        story.append(Spacer(1, 30))
        
        # Footer
        story.append(Paragraph("Thank you for choosing SriJai Tailoring!", styles['Normal']))
        story.append(Paragraph("Quality stitching with perfect fit guaranteed", styles['Italic']))
        
        doc.build(story)
        pdf = buffer.getvalue()
        buffer.close()
        return pdf
    
    @staticmethod
    def generate_receipt_pdf(payment):
        """Generate PDF receipt"""
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Receipt header
        title_style = ParagraphStyle(
            'ReceiptTitle',
            parent=styles['Heading2'],
            fontSize=16,
            alignment=TA_CENTER,
            textColor=colors.darkgreen
        )
        
        story.append(Paragraph("PAYMENT RECEIPT", title_style))
        story.append(Paragraph("SriJai Tailoring", styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Receipt details
        receipt_data = [
            ['Receipt No:', payment.payment_number or f"RCP-{payment.id:04d}"],
            ['Date:', payment.payment_date.strftime('%B %d, %Y')],
            ['Customer:', payment.customer.name],
            ['Invoice:', payment.invoice.invoice_number],
            ['Payment Method:', payment.get_payment_method_display()],
            ['Amount Paid:', f"₹{payment.amount:.2f}"]
        ]
        
        receipt_table = Table(receipt_data, colWidths=[2*inch, 3*inch])
        receipt_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 12),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('LINEBELOW', (-1,-1), (-1,-1), 2, colors.darkgreen),
        ]))
        
        story.append(receipt_table)
        story.append(Spacer(1, 30))
        
        # Balance information
        if payment.invoice:
            remaining = payment.invoice.total_amount - payment.invoice.payment_set.aggregate(
                total=models.Sum('amount'))['total'] or 0
            
            if remaining > 0:
                story.append(Paragraph(f"Remaining Balance: ₹{remaining:.2f}", styles['Normal']))
            else:
                story.append(Paragraph("Fully Paid - Thank You!", styles['Normal']))
        
        story.append(Spacer(1, 20))
        story.append(Paragraph("This is a computer generated receipt.", styles['Italic']))
        
        doc.build(story)
        pdf = buffer.getvalue()
        buffer.close()
        return pdf